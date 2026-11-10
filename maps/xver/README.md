# Cross-version maps (FHIR Mapping Language)

Hand-written FML maps for the artifact types of this IG whose R4 → R6
conversion is **not** covered by the generated cross-version maps. The
generated maps (164 R4→R6, 63 R6→R4) are Brian Postlethwaite's, taken from
https://github.com/aleksandrkislitsyn/fml-r4-r6-fhir-server (`fml-maps/`),
and are imported by URL (`http://hl7.org/fhir/uv/xver/StructureMap/*4to6`).

| Map | Direction | Status |
|---|---|---|
| `Medication_4to6.fml` | catalog Medication R4 → R6 | written, **not executed** |
| `Medication_6to4.fml` | catalog Medication R6 → R4 | written, **not executed** |
| `ActivityDefinition_4to6.fml` | sig R4 → R6 (DosageInstruction remodel) | **to do** (oncology-regimens issue) |

Not executed means: no engine has run these maps yet. The HL7 validator
(6.9.10) does not load map files through `-ig` for `-transform`, and it
cannot hold R4 and R6 definitions at once. The engine that can is the
FHIRPath Lab executor (TypeScript) used by the server above; wiring it
into CI is tracked as an issue. Until then the maps document the intended
rules; the IG page "FHIR Versions" is the normative description.

Why these maps exist at all: the generated `Medication_4to6` was produced
from 6.0.0-ballot5, where Medication had no canonical elements. The CI
build (6.0.0-snapshot1) has them (FHIR-57813). This IG pre-adopts them in
R4 through the `artifact-*` extensions, so the map has to turn those
extensions into native elements and back.

Design rule from the FHIR Camp 2026 experiment (Health Samurai,
"One FHIR Store, Two Versions"): one stored/authored version (here R4),
other versions derived by maps, and every artifact must survive the
round trip R4 → R6 → R4 unchanged. That round trip is the acceptance test
for these maps once an engine runs them.
