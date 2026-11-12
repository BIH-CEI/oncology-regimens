#!/usr/bin/env python3
"""Cross-version build and round-trip test for the European SACT Regimen Catalog.

Runs the hand-written FHIR Mapping Language maps in maps/xver with the HL7
validator: every R4 artifact of the IG is converted to R6 (derived view),
the R6 result is validated against the R6 core package, converted back to
R4 and compared with the original. A difference fails the run.

    python3 scripts/xver/xver.py            # representative subset
    python3 scripts/xver/xver.py --all      # every resource
    python3 scripts/xver/xver.py --only Medication --keep-going

Everything the script needs (validator, core packages, a private FHIR
package cache) lives in .xver/ at the repository root and is downloaded on
first use. See maps/xver/README.md for the design and the validator quirks
this script works around.
"""
import argparse
import concurrent.futures
import difflib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
XVER = ROOT / ".xver"
HOME = XVER / "home"                     # java user.home -> private package cache
TOOLS = XVER / "tools"
PKGS = XVER / "pkgs"
MAPS_SRC = ROOT / "maps" / "xver"
MAPS_OUT = XVER / "maps"
OUT = XVER / "out"
LOGS = XVER / "logs"

VALIDATOR_VERSION = os.environ.get("XVER_VALIDATOR_VERSION", "7.0.5")
VALIDATOR_URL = f"https://github.com/hapifhir/org.hl7.fhir.core/releases/download/{VALIDATOR_VERSION}/validator_cli.jar"
R6_URL = os.environ.get("XVER_R6_URL", "https://build.fhir.org/hl7.fhir.r6.core.tgz")
R4_URL = "https://packages2.fhir.org/packages/hl7.fhir.r4.core/4.0.1"
TX = os.environ.get("XVER_TX", "http://tx.fhir.org")
JAVA_OPTS = os.environ.get("XVER_JAVA_OPTS", "-Djava.net.preferIPv4Stack=true").split()

# Validator quirk 1: a core package of another FHIR version loaded with -ig is
# given version-prefixed canonicals (http://hl7.org/fhir/<v>/StructureDefinition/..),
# but the R6 loader (RNToRNLoader.versionString) prefixes with 5.0, not 6.0.
R6_SIDE_PREFIX = "http://hl7.org/fhir/5.0/StructureDefinition/"
R4_SIDE_PREFIX = "http://hl7.org/fhir/4.0/StructureDefinition/"
NATIVE_PREFIX = "http://hl7.org/fhir/StructureDefinition/"
XVER_R4 = "http://hl7.org/fhir/4.0/StructureDefinition/"
XVER_R6 = "http://hl7.org/fhir/6.0/StructureDefinition/"

NUMERIC = {"integer", "integer64", "decimal", "positiveInt", "unsignedInt"}
PRIMITIVES = NUMERIC | {"boolean", "string", "code", "uri", "url", "canonical", "oid", "uuid", "id",
                        "markdown", "base64Binary", "instant", "date", "dateTime", "time", "xhtml"}

# Validation messages on the derived R6 output that are accepted, with the reason.
VALIDATION_ALLOW = [
    # The IG's own code systems and extensions are R4 definitions and are not
    # loaded into the R6 validation context.
    (r"CodeSystem 'http://hemonc\.org/", "IG code system, not loaded in R6 context"),
    (r"http://hemonc\.org/fhir/StructureDefinition/", "IG extension, R4 definition"),
]


def log(msg):
    print(msg, flush=True)


def download(url, dest):
    dest.parent.mkdir(parents=True, exist_ok=True)
    log(f"  download {url}")
    with urllib.request.urlopen(url, timeout=600) as r, open(dest, "wb") as f:
        shutil.copyfileobj(r, f)


def package_version(tgz):
    with tarfile.open(tgz) as t:
        return json.load(t.extractfile("package/package.json"))["version"]


def ensure_tools(refresh_r6=False):
    jar = TOOLS / f"validator_cli-{VALIDATOR_VERSION}.jar"
    if not jar.exists():
        download(VALIDATOR_URL, jar)
    r4 = PKGS / "hl7.fhir.r4.core-4.0.1.tgz"
    if not r4.exists():
        download(R4_URL, r4)
    r6 = PKGS / "hl7.fhir.r6.core-cibuild.tgz"
    if refresh_r6 or not r6.exists():
        download(R6_URL, r6)
    r6_version = package_version(r6)
    # Private package cache: the R6 CI build is installed under the version it
    # declares, so that "-version 6.0" resolves to the CI build and not to the
    # (older) package of the same version on the registry.
    cache = HOME / ".fhir" / "packages"
    cache.mkdir(parents=True, exist_ok=True)
    stamp = cache / f"hl7.fhir.r6.core#{r6_version}" / ".xver-stamp"
    want = f"{r6.stat().st_size}:{int(r6.stat().st_mtime)}"
    if not stamp.exists() or stamp.read_text() != want:
        target = stamp.parent
        if target.exists():
            shutil.rmtree(target)
        target.mkdir(parents=True)
        with tarfile.open(r6) as t:
            t.extractall(target)
        stamp.write_text(want)
        log(f"  installed R6 CI build as hl7.fhir.r6.core#{r6_version} in private cache")
    # Speed: seed the private cache from the user's cache (never the R6 core package).
    user_cache = Path.home() / ".fhir" / "packages"
    if user_cache.exists() and user_cache != cache:
        for p in user_cache.iterdir():
            if p.is_dir() and "#" in p.name and not p.name.startswith("hl7.fhir.r6.core") and not (cache / p.name).exists():
                shutil.copytree(p, cache / p.name)
    return jar, r4, r6, r6_version


def prepare_maps():
    """Rewrite the canonical xver 'uses' URLs into what the validator resolves."""
    maps = {"4to6": {}, "6to4": {}}
    for d in maps:
        (MAPS_OUT / d).mkdir(parents=True, exist_ok=True)
    for f in sorted(MAPS_SRC.glob("*.fml")):
        text = f.read_text()
        m = re.search(r'^map\s+"([^"]+)"\s*=', text, re.M)
        if not m:
            log(f"  skip {f.name}: no map header")
            continue
        url = m.group(1)
        src_type = re.search(r'^uses\s+"[^"]*/StructureDefinition/(\w+)"\s+alias\s+\w+\s+as\s+source', text, re.M).group(1)
        if f.name.endswith("_4to6.fml"):
            d, repl = "4to6", ((XVER_R4, NATIVE_PREFIX), (XVER_R6, R6_SIDE_PREFIX))
        elif f.name.endswith("_6to4.fml"):
            d, repl = "6to4", ((XVER_R6, NATIVE_PREFIX), (XVER_R4, R4_SIDE_PREFIX))
        else:
            continue
        # Only the 'uses' declarations are rewritten; cross-version extension
        # URLs in the rules keep the canonical 4.0 / 6.0 scheme.
        lines = []
        for line in text.splitlines():
            if line.startswith("uses "):
                for a, b in repl:
                    line = line.replace(a, b)
            lines.append(line)
        text = "\n".join(lines) + "\n"
        (MAPS_OUT / d / f.name).write_text(text)
        maps[d][src_type] = url
    return maps


def collect_sources(all_, only):
    files = sorted((ROOT / "input" / "resources").glob("*.json"))
    gen = ROOT / "fsh-generated" / "resources"
    if gen.exists():
        seen_plan = 0
        for f in sorted(gen.glob("*.json")):
            if f.name.startswith(("ImplementationGuide-", "StructureDefinition-")):
                continue
            if f.name.startswith("PlanDefinition-") and not all_ and not only:
                seen_plan += 1
                if seen_plan > 2:
                    continue
            files.append(f)
    if only:
        files = [f for f in files if any(o in f.name for o in only)]
    return files


# ---------------------------------------------------------------- retyping
class Definitions:
    """StructureDefinitions of one package, for retyping JSON primitives."""

    def __init__(self, tgz):
        self.sds = {}
        with tarfile.open(tgz) as t:
            for m in t.getmembers():
                if m.name.startswith("package/StructureDefinition-") and m.name.endswith(".json"):
                    sd = json.load(t.extractfile(m))
                    if "snapshot" in sd:
                        self.sds[sd["type"]] = sd
                        self.sds[sd["url"]] = sd

    def elements(self, type_name):
        sd = self.sds.get(type_name)
        return sd["snapshot"]["element"] if sd else []


def retype(obj, defs):
    """Convert numeric and boolean primitives that the engine wrote as strings.

    Validator quirk 2: on the version-patched side the engine does not know the
    primitive type of an element and the JSON writer quotes every value. The
    target definitions say which elements are numbers or booleans.
    """
    rt = obj.get("resourceType")
    if not rt:
        return obj
    _retype_node(obj, rt, rt, defs)
    return obj


def _find(elements, path):
    for e in elements:
        if e["path"] == path:
            return e
    return None


def _retype_node(node, type_name, path, defs):
    elements = defs.elements(type_name)
    if not elements:
        return
    for key, value in list(node.items()):
        if key in ("resourceType",) or key.startswith("_"):
            continue
        ed = _find(elements, f"{path}.{key}")
        chosen_type = None
        if ed is None:
            # choice: path[x] with a type suffix
            for e in elements:
                if e["path"].endswith("[x]") and e["path"].startswith(path + ".") and "." not in e["path"][len(path) + 1:]:
                    stem = e["path"][len(path) + 1:-3]
                    if key.startswith(stem) and len(key) > len(stem):
                        suffix = key[len(stem):]
                        for t in e.get("type", []):
                            code = t["code"]
                            if code[:1].upper() + code[1:] == suffix:
                                ed, chosen_type = e, code
                                break
                    if ed:
                        break
        if ed is None:
            continue
        if "contentReference" in ed:
            ref = ed["contentReference"].split("#")[-1]
            for v in (value if isinstance(value, list) else [value]):
                if isinstance(v, dict):
                    _retype_node(v, type_name, ref, defs)
            continue
        types = [t["code"] for t in ed.get("type", [])]
        code = chosen_type or (types[0] if types else None)
        if code is None:
            continue
        code = code.split("/")[-1]  # patched URLs never occur here, but be safe
        if code in NUMERIC or code == "boolean":
            node[key] = [_coerce(v, code) for v in value] if isinstance(value, list) else _coerce(value, code)
        elif code in PRIMITIVES or code == "http://hl7.org/fhirpath/System.String":
            continue
        elif code in ("BackboneElement", "Element") and _find(elements, f"{ed['path']}.id"):
            for v in (value if isinstance(value, list) else [value]):
                if isinstance(v, dict):
                    _retype_node(v, type_name, ed["path"], defs)
        else:
            for v in (value if isinstance(value, list) else [value]):
                if isinstance(v, dict):
                    _retype_node(v, code, code, defs)


def _coerce(v, code):
    if not isinstance(v, str):
        return v
    if code == "boolean":
        return {"true": True, "false": False}.get(v, v)
    try:
        if code == "decimal":
            return int(v) if re.fullmatch(r"-?\d+", v) else float(v)
        return int(v)
    except ValueError:
        return v


# ---------------------------------------------------------------- running
class Runner:
    def __init__(self, jar, r4, r6):
        self.jar, self.r4, self.r6 = jar, r4, r6

    def java(self, args, logfile):
        cmd = ["java", f"-Duser.home={HOME}", *JAVA_OPTS, "-jar", str(self.jar), *args]
        with open(logfile, "w") as lf:
            lf.write(" ".join(cmd) + "\n\n")
            lf.flush()
            p = subprocess.run(cmd, stdout=lf, stderr=subprocess.STDOUT, cwd=ROOT)
        return p.returncode, Path(logfile).read_text()

    def transform(self, direction, map_url, src, out):
        out.parent.mkdir(parents=True, exist_ok=True)
        if out.exists():
            out.unlink()
        if direction == "4to6":
            version, side = "4.0", self.r6
        else:
            version, side = "6.0", self.r4
        LOGS.mkdir(parents=True, exist_ok=True)
        logfile = LOGS / f"{direction}-{src.stem}.log"
        rc, text = self.java(["transform", map_url, str(src), "-version", version, "-tx", TX,
                              "-ig", str(side), "-ig", str(MAPS_OUT / direction), "-output", str(out)], logfile)
        failure = re.search(r"\.\.\.Failure: (.*)", text)
        if failure or not out.exists():
            msg = failure.group(1) if failure else "no output written"
            tail = "\n".join(l for l in text.splitlines() if "rror" in l or "xception" in l)[-1500:]
            return False, f"{msg}\n{tail}"
        return True, ""

    def validate(self, files, version, extra_igs):
        logfile = LOGS / f"validate-{version}.log"
        args = [str(f) for f in files] + ["-version", version, "-tx", TX]
        for ig in extra_igs:
            args += ["-ig", str(ig)]
        rc, text = self.java(args, logfile)
        issues = []
        for line in text.splitlines():
            m = re.match(r"\s*(Error|Fatal) @ (.*)", line)
            if m:
                issues.append(m.group(2))
        return issues, text


def diff_json(a, b, name_a, name_b):
    sa = json.dumps(a, indent=1, sort_keys=True, ensure_ascii=False).splitlines()
    sb = json.dumps(b, indent=1, sort_keys=True, ensure_ascii=False).splitlines()
    return "\n".join(difflib.unified_diff(sa, sb, name_a, name_b, lineterm="", n=2))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--all", action="store_true", help="convert every resource, not the representative subset")
    ap.add_argument("--only", nargs="*", help="only files whose name contains one of these strings")
    ap.add_argument("--jobs", type=int, default=1, help="parallel validator processes (the package cache lock is not safe for more than one)")
    ap.add_argument("--no-validate", action="store_true", help="skip R6 validation of the derived output")
    ap.add_argument("--no-roundtrip", action="store_true", help="only derive R6, do not convert back")
    ap.add_argument("--refresh-r6", action="store_true", help="download the current R6 CI build again")
    args = ap.parse_args()

    log("== tools")
    jar, r4, r6, r6_version = ensure_tools(args.refresh_r6)
    log(f"  validator {VALIDATOR_VERSION}, R6 CI build package {r6_version}")
    log("== maps")
    maps = prepare_maps()
    for d in maps:
        log(f"  {d}: {', '.join(sorted(maps[d]))}")
    sources = collect_sources(args.all, args.only)
    sources = [s for s in sources if json.load(open(s)).get("resourceType") in maps["4to6"]]
    log(f"== {len(sources)} source resources")

    runner = Runner(jar, r4, r6)
    defs6 = Definitions(r6)
    defs4 = Definitions(r4)
    r6_dir, r4_dir = OUT / "r6", OUT / "r4-roundtrip"
    results = {}

    def work(src):
        rt = json.load(open(src)).get("resourceType")
        out6 = r6_dir / src.name
        ok, msg = runner.transform("4to6", maps["4to6"][rt], src, out6)
        if not ok:
            return src, "4to6 failed", msg
        j6 = retype(json.load(open(out6)), defs6)
        out6.write_text(json.dumps(j6, indent=2, ensure_ascii=False) + "\n")
        if args.no_roundtrip:
            return src, "derived", ""
        if rt not in maps["6to4"]:
            return src, "derived (no 6to4 map)", ""
        out4 = r4_dir / src.name
        ok, msg = runner.transform("6to4", maps["6to4"][rt], out6, out4)
        if not ok:
            return src, "6to4 failed", msg
        j4 = retype(json.load(open(out4)), defs4)
        out4.write_text(json.dumps(j4, indent=2, ensure_ascii=False) + "\n")
        orig = json.load(open(src))
        if orig == j4:
            return src, "round trip ok", ""
        return src, "round trip differs", diff_json(orig, j4, "original", "round-trip")

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as ex:
        for src, status, detail in ex.map(work, sources):
            results[src] = (status, detail)
            log(f"  {status:22} {src.name}")
            if detail:
                log("    " + detail.replace("\n", "\n    "))

    failed = [s for s, (st, _) in results.items() if "fail" in st or "differs" in st]

    if not args.no_validate and r6_dir.exists():
        log("== validating derived R6 output against the R6 CI build")
        files = sorted(r6_dir.glob("*.json"))
        issues, _ = runner.validate(files, "6.0", [r6_dir])
        blocking = []
        for issue in issues:
            if any(re.search(p, issue) for p, _ in VALIDATION_ALLOW):
                continue
            blocking.append(issue)
        for i in blocking:
            log(f"  ERROR {i}")
        log(f"  {len(issues)} errors, {len(blocking)} not allow-listed")
        if blocking:
            failed.append("R6 validation")

    log("== summary")
    for st in sorted(set(st for st, _ in results.values())):
        log(f"  {sum(1 for s, _ in results.values() if s == st):3} {st}")
    if failed:
        log(f"FAILED: {len(failed)}")
        sys.exit(1)
    log("OK")


if __name__ == "__main__":
    main()
