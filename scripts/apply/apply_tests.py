#!/usr/bin/env python3
"""$apply scenario tests for the European SACT Regimen Catalog.

A scenario (tests/apply/scenarios/*.json) is patient data, a PlanDefinition,
optional $apply parameters and FHIRPath assertions on the result:

    {
      "title": "Carboplatin AUC 5: Calvert dose",
      "planDefinition": "regimen-2554-variant-144842",
      "subject": "Patient/demo-cp-1",
      "fixtures": ["fixtures/patient-demo-cp-1.json"],       # bundles or resources, loaded first
      "parameters": {"TargetAUC": 6},                        # optional, sent as Parameters
      "expect": {
        "status": 200,
        "assertions": [
          {"fhirpath": "contained.ofType(MedicationRequest).count()", "equals": 2},
          {"fhirpath": "…doseQuantity.value", "approx": 512, "tolerance": 0.05},
          {"fhirpath": "…", "exists": true},
          {"fhirpath": "…", "count": 3}
        ]
      },
      "expectedFailure": {"issue": "oncology-regimens-m75", "reason": "…"}   # optional
    }

Scenarios with expectedFailure are the specification of work that is not
done yet: they must fail (XFAIL); when they pass (XPASS) the run fails so
that the marker is removed.

    python3 scripts/apply/apply_tests.py --load          # load IG resources, run all
    python3 scripts/apply/apply_tests.py --only calvert  # subset, server already loaded

Needs a running HAPI FHIR with Clinical Reasoning (phase0/docker-compose.yml,
http://localhost:8096/fhir) and the Python package fhirpathpy.
"""
import argparse
import glob
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

try:
    import fhirpathpy
    from fhirpathpy.models import models as fhirpath_models
except ImportError:  # pragma: no cover
    print("fhirpathpy is required: pip install fhirpathpy", file=sys.stderr)
    sys.exit(2)

R4 = fhirpath_models["r4"]   # choice elements (medication[x], timing[x], value[x]) need the model

ROOT = Path(__file__).resolve().parents[2]
TESTS = ROOT / "tests" / "apply"
HEADERS = {"Content-Type": "application/fhir+json", "Accept": "application/fhir+json"}


def http(method, url, body=None, timeout=300):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        raw = e.read().decode(errors="replace")
        try:
            return e.code, json.loads(raw)
        except ValueError:
            return e.code, {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "diagnostics": raw[:500]}]}


def wait_for(base, seconds):
    deadline = time.time() + seconds
    while time.time() < deadline:
        try:
            status, _ = http("GET", f"{base}/metadata", timeout=10)
            if status == 200:
                return True
        except Exception:
            pass
        time.sleep(5)
    return False


def transaction(base, resources):
    entries = []
    for r in resources:
        entries.append({"resource": r, "request": {"method": "PUT", "url": f"{r['resourceType']}/{r['id']}"}})
    status, out = http("POST", base, {"resourceType": "Bundle", "type": "transaction", "entry": entries})
    if status >= 300:
        raise RuntimeError(f"transaction failed ({status}): {json.dumps(out)[:800]}")
    return out


def load_ig(base):
    """Load every IG resource: SUSHI output and the hand-written JSON."""
    resources = []
    for pattern in ("fsh-generated/resources/*.json", "input/resources/*.json"):
        for f in sorted(glob.glob(str(ROOT / pattern))):
            r = json.load(open(f))
            if r["resourceType"] == "ImplementationGuide":
                continue
            resources.append(r)
    out = transaction(base, resources)
    print(f"  loaded {len(out['entry'])} IG resources")


def load_fixture(base, path):
    r = json.load(open(path))
    if r["resourceType"] == "Bundle":
        status, out = http("POST", base, r)
        if status >= 300:
            raise RuntimeError(f"fixture {path.name} failed ({status}): {json.dumps(out)[:800]}")
    else:
        status, out = http("PUT", f"{base}/{r['resourceType']}/{r['id']}", r)
        if status >= 300:
            raise RuntimeError(f"fixture {path.name} failed ({status}): {json.dumps(out)[:800]}")


def apply(base, scenario):
    pd = scenario["planDefinition"]
    params = scenario.get("parameters")
    if params is None:
        return http("GET", f"{base}/PlanDefinition/{pd}/$apply?subject={scenario['subject']}")
    body = {"resourceType": "Parameters", "parameter": [
        {"name": "subject", "valueString": scenario["subject"]},
        {"name": "parameters", "resource": {"resourceType": "Parameters", "parameter": [
            _param(k, v) for k, v in params.items()]}},
    ]}
    return http("POST", f"{base}/PlanDefinition/{pd}/$apply", body)


def _param(name, value):
    if isinstance(value, bool):
        return {"name": name, "valueBoolean": value}
    if isinstance(value, int):
        return {"name": name, "valueInteger": value}
    if isinstance(value, float):
        return {"name": name, "valueDecimal": value}
    return {"name": name, "valueString": str(value)}


def check(assertion, resource):
    expr = assertion["fhirpath"]
    try:
        result = fhirpathpy.evaluate(resource, expr, {}, R4)
    except Exception as e:  # noqa: BLE001
        return False, f"FHIRPath error: {e}"
    if "equals" in assertion:
        want = assertion["equals"]
        got = result[0] if len(result) == 1 else result
        ok = _num_equal(got, want) if isinstance(want, (int, float)) and not isinstance(want, bool) else got == want
        return ok, f"{expr} = {got!r}, expected {want!r}"
    if "approx" in assertion:
        want, tol = assertion["approx"], assertion.get("tolerance", 0.02)
        if len(result) != 1 or not isinstance(result[0], (int, float)):
            return False, f"{expr} = {result!r}, expected about {want}"
        ok = abs(result[0] - want) <= abs(want) * tol
        return ok, f"{expr} = {result[0]}, expected {want} ±{tol * 100:g}%"
    if "exists" in assertion:
        ok = (len(result) > 0) == assertion["exists"]
        return ok, f"{expr} -> {len(result)} item(s), expected {'some' if assertion['exists'] else 'none'}"
    if "count" in assertion:
        ok = len(result) == assertion["count"]
        return ok, f"{expr} -> {len(result)} item(s), expected {assertion['count']}"
    if "minCount" in assertion:
        ok = len(result) >= assertion["minCount"]
        return ok, f"{expr} -> {len(result)} item(s), expected at least {assertion['minCount']}"
    return False, f"{expr}: assertion has no operator"


def _num_equal(got, want):
    try:
        return abs(float(got) - float(want)) < 1e-9
    except (TypeError, ValueError):
        return False


def run_scenario(base, path):
    sc = json.load(open(path))
    for fx in sc.get("fixtures", []):
        load_fixture(base, TESTS / fx)
    status, result = apply(base, sc)
    failures = []
    want_status = sc.get("expect", {}).get("status", 200)
    if status != want_status:
        failures.append(f"HTTP {status}, expected {want_status}: {json.dumps(result)[:300]}")
    for a in sc.get("expect", {}).get("assertions", []):
        ok, msg = check(a, result)
        if not ok:
            failures.append(msg)
    return sc, failures, result


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default=os.environ.get("APPLY_BASE", "http://localhost:8096/fhir"))
    ap.add_argument("--load", action="store_true", help="load the IG resources into the server first")
    ap.add_argument("--wait", type=int, default=0, help="seconds to wait for the server")
    ap.add_argument("--only", nargs="*", help="scenario file names containing one of these strings")
    ap.add_argument("--keep", help="directory to write every $apply result to")
    args = ap.parse_args()

    if args.wait and not wait_for(args.base, args.wait):
        print(f"server {args.base} not reachable")
        sys.exit(2)
    if args.load:
        print("== loading IG resources")
        load_ig(args.base)

    files = sorted((TESTS / "scenarios").glob("*.json"))
    if args.only:
        files = [f for f in files if any(o in f.name for o in args.only)]
    print(f"== {len(files)} scenarios against {args.base}")
    counts = {"pass": 0, "fail": 0, "xfail": 0, "xpass": 0, "error": 0}
    for f in files:
        try:
            sc, failures, result = run_scenario(args.base, f)
        except Exception as e:  # noqa: BLE001
            counts["error"] += 1
            print(f"  ERROR  {f.stem}: {e}")
            continue
        if args.keep:
            Path(args.keep).mkdir(parents=True, exist_ok=True)
            (Path(args.keep) / f"{f.stem}.json").write_text(json.dumps(result, indent=2, ensure_ascii=False))
        xf = sc.get("expectedFailure")
        if failures and xf:
            counts["xfail"] += 1
            print(f"  XFAIL  {f.stem}  ({xf.get('issue', '')}: {xf.get('reason', '')})")
        elif failures:
            counts["fail"] += 1
            print(f"  FAIL   {f.stem}")
            for m in failures:
                print(f"         - {m}")
        elif xf:
            counts["xpass"] += 1
            print(f"  XPASS  {f.stem}  (passes although marked as expected failure for {xf.get('issue', '')}: remove the marker)")
        else:
            counts["pass"] += 1
            print(f"  PASS   {f.stem}")
    print("== summary: " + ", ".join(f"{v} {k}" for k, v in counts.items() if v))
    sys.exit(1 if counts["fail"] or counts["xpass"] or counts["error"] else 0)


if __name__ == "__main__":
    main()
