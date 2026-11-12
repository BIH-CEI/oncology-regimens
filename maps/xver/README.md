# Cross-version maps (FHIR Mapping Language)

Hand-written, self-contained FML maps that derive the FHIR R6 view of this
IG from its R4 source and convert it back. They are executed by
[`scripts/xver/xver.py`](../../scripts/xver/xver.py) with the HL7 validator,
locally and in CI (`.github/workflows/xver-roundtrip.yml`). The normative
description of the modelling decisions is the IG page **FHIR Versions**.

```
python3 scripts/xver/xver.py              # representative subset, round trip + R6 validation
python3 scripts/xver/xver.py --all        # every resource of input/ and fsh-generated/
python3 scripts/xver/xver.py --only Medication --no-validate
```

Outputs land in `.xver/out/r6/` (derived R6 resources) and
`.xver/out/r4-roundtrip/`; logs in `.xver/logs/`. `.xver/` is git-ignored
and holds the validator, the core packages and a private package cache.

## Maps

| Map | Direction | What it does | Status |
|---|---|---|---|
| `Medication_4to6` / `_6to4` | catalog Medication | `artifact-*` extensions ↔ native canonical elements (`url`, `version`, `name`, `publisher`, …); `status` ↔ PublicationStatus with the original code kept on the primitive when lossy; `manufacturer`/`form`/`batch` renames; `medication-classification` stays an extension | round trip passes |
| `ActivityDefinition_4to6` / `_6to4` | sig | `dosage[]` ↔ `dosageInstruction` (one Dosage = one step with one component; `day-of-cycle` ↔ `step.start` offset; `timing.repeat.period` → `repeatCycle`; `sequence` kept on the step); `dynamicValue.path` rewritten; `timing[x]`, `location`, `product`, requirement references | round trip passes |
| `PlanDefinition_4to6` / `_6to4` | regimen, variant, protocol, formulary | `action.code` 0..* ↔ 0..1 (overflow in an extension), `relatedAction.actionId` ↔ `targetId`, `input`/`output` ↔ `requirement`, `timing[x]` type changes, string ↔ markdown copies; R6-only elements kept in extensions | round trip passes |
| `Library_4to6` / `_6to4` | CQL/FHIRPath libraries | element copies, `usage` string ↔ markdown | round trip passes |
| `CodeSystem_4to6` / `_6to4`, `ValueSet_4to6` / `_6to4` | terminology | element copies; R6-only metadata kept in extensions | round trip passes |
| `ConceptMap_4to6` / `_6to4` | mappings | `source[x]`/`target[x]` ↔ `sourceScope[x]`/`targetScope[x]`, `equivalence` ↔ `relationship` with a concept map (lossy codes kept on the primitive), `unmapped.url` ↔ `otherMap`, `dependsOn` remodel | round trip passes |

## Design rules

1. **R4 is authored; R6 is derived, never edited.** A modelling change is a
   change to the R4 source plus the map.
2. **Every artifact must survive R4 → R6 → R4 unchanged.** The harness
   compares the round-trip result with the original JSON and fails on any
   difference. This is the acceptance test, taken from the FHIR Camp 2026
   experiment described by Health Samurai ("One FHIR Store, Two Versions").
3. **Prefer published extensions for pre-adoption** (`artifact-*`,
   `medication-*` from `hl7.fhir.uv.extensions`). The generic cross-version
   scheme `http://hl7.org/fhir/<4.0|6.0>/StructureDefinition/extension-<path>`
   is used only for elements without a counterpart and for lossy code
   translations, where the original code is kept as an extension on the
   primitive (`_status`, `_relationship`).
4. **Self-contained maps.** No `imports` of the generated xver datatype maps:
   complex types are copied (`src.x as v -> tgt.x = v`), extensions are
   copied by an explicit `Extension` group. The validator can then run each
   map with only the two core packages.
5. **R6 target = the R6 CI build** (`https://build.fhir.org/hl7.fhir.r6.core.tgz`).
   The package labels itself `6.0.0-snapshot1`, but the published
   `6.0.0-snapshot1` package on the registry (2026-09-10) predates the
   canonical `Medication` (FHIR-57813) and the `DosageInstruction` type. The
   harness therefore installs the CI build into a private package cache under
   that version. `--refresh-r6` fetches the current build again.

## Validator quirks the harness works around

The maps use the standard cross-version conventions (`map "url" = "name"`
header, `uses "http://hl7.org/fhir/4.0/StructureDefinition/…"` and
`…/6.0/…`). The harness rewrites only the `uses` lines before a run:

| Quirk (validator 7.0.5) | Effect | Work-around |
|---|---|---|
| `-version 4.0 -ig hl7.fhir.r6.core#…` is refused ("parameters are inconsistent") | cannot name the second core package by id | the second core package is loaded from a local `.tgz` path |
| A second core package is loaded with version-prefixed canonicals, but `RNToRNLoader.versionString()` returns `5.0` for R6 | R6 definitions are reachable as `http://hl7.org/fhir/5.0/StructureDefinition/…` | `6.0/` → `5.0/` in `uses` for 4to6 runs; R4 side packages are correctly `4.0/` |
| The main version's definitions keep native URLs | `uses` of the main version must be native | `4.0/` → native in 4to6 runs, `6.0/` → native in 6to4 runs |
| `-version 6.0` resolves to the registry package `hl7.fhir.r6.core#6.0.0-snapshot1` | that package lacks the canonical Medication | private cache (`-Duser.home`) seeded with the CI build under that version |
| On the version-patched side, children of a **polymorphic** element cannot be created (`Unable to find type Duration for element offsetDuration`) | `create()` into `offset[x]`, `value[x]` fails | build the element stand-alone (`create('Duration') as off, off.value = …`) and copy it (`st.offset = off`), or use a FHIRPath expression that yields a typed primitive (`(… ).truncate()`) |
| On the version-patched side every primitive is written as a JSON string (`"value": "21"`, `"experimental": "true"`) | invalid JSON typing for numbers and booleans | the harness retypes the output from the target version's StructureDefinitions |
| `///` metadata headers are rejected (`Found "url" expecting "map"`), `conceptmap` must precede `uses` | parse errors | maps use the `map` header and the grammar order |
| `transform` accepts exactly one source per run; the package cache lock is not safe for parallel processes | one JVM start per resource | the default run converts a representative subset; `--all` converts everything |
| The new SSRF check rejects NAT64 addresses for `tx.fhir.org` | no terminology server | `XVER_JAVA_OPTS` (default `-Djava.net.preferIPv4Stack=true`) |

The first three and the polymorphic/primitive limitations are worth an
upstream report (org.hl7.fhir.core); tracked as beads issue oncology-regimens-bjk.

## Adding a map

1. Write `<Type>_4to6.fml` and `<Type>_6to4.fml` in this folder (header
   `map "http://hemonc.org/fhir/StructureMap/<Type>4to6" = "ESRC<Type>4to6"`,
   `uses` with the `4.0`/`6.0` prefixes).
2. `python3 scripts/xver/skeleton.py <R4 package dir> .xver/pkgs/hl7.fhir.r6.core-cibuild.tgz <Type>`
   lists which element paths are identical (copy) and which differ.
3. `python3 scripts/xver/xver.py --only <Type>` until the round trip passes
   and the R6 validation is clean.
