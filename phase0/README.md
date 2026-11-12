# Phase 0 — Carbo/Taxol Variant #83 end-to-end spike

Goal: prove the HemOnc → FHIR R4 knowledge artifact pipeline end-to-end with one
real regimen variant, so the patterns, canonical URLs, versioning, and CQL
layering can be validated before scaling to the full HemOncKB.

Source: HemOnc Dataverse, snapshot **2026-03-12**.
Regimen: `2554` "Carboplatin and Paclitaxel (CP)".
Variant: `144842` "Variant #83" (Carboplatin AUC 5 + Paclitaxel 175 mg/m², q21d,
3–6 cycles; first reported in MITO-2).

## What is in this folder

```
phase0/
├── README.md                         ← this file
├── docker-compose.yml                ← HAPI FHIR 8.12.0 with Clinical Reasoning (cqf-fhir), port 8096
├── cql/HemOncDoseHelpers.cql         ← source CQL of Library/HemOncDoseHelpers (base64 in input/resources)
├── examples/                         ← demo patient + observations (height, weight, creatinine)
└── scripts/load-and-apply.sh         ← loads the IG into HAPI, runs three scenarios, prints $apply
```

The knowledge artifacts themselves live in the IG: hand-written JSON in
`input/resources/` (CodeSystems, two Medications, two sigs, the Library, the
variant PlanDefinition) and FSH in `input/fsh/`. The executable expectations
for `$apply` are the scenarios in `tests/apply/` (see its README).

## Canonical URL scheme (stable across releases)

```
http://hemonc.org/fhir/<ResourceType>/<stable-id>
```

* `CodeSystem/hemonc`
* `CodeSystem/sig-target-type`
* `Medication/hemonc-drug-<CUI>-<inn>` (catalog Medication; `MedicationKnowledge` is removed in FHIR R6)
* `ActivityDefinition/sig-<component>-<dose>-<schedule>` *(or a content hash once we scale)*
* `PlanDefinition/regimen-<regimen_cui>-variant-<variant_cui>`
* `Library/HemOncDoseHelpers`

Every resource carries `version = "2026-03-12"` (= the HemOnc snapshot date).
Future quarterly snapshots emit a new `version` against the same canonical URL.
The HemOnc CUI is also held as a `use=official` `identifier` so the CUI is
addressable even if the canonical scheme evolves.

## Pipeline (3-resource model — no MedicationDispense)

```
PlanDefinition  ─── action[].definitionCanonical ──►  ActivityDefinition
   │                                                       │
   │ $apply(subject=Patient/x, …)                          │ CQL
   ▼                                                       ▼
CarePlan + RequestGroup ──────────►  MedicationRequest (ordered: 310 mg, 625 mg)
                                          │  trace extension: BSA, GFR, formula, cap
                                          │  (banding if applied at order side)
                                          ▼
                                     MedicationAdministration (actual mg given)
```

The protocol intent (`175 mg/m²`, `AUC 5`) lives in the **ActivityDefinition**.
The patient-specific computed mg lives in the **MedicationRequest** emitted at
`$apply` time, carrying a `dose-calculation-trace` extension that records BSA
formula, GFR formula, caps applied, and inputs.
The administered mg lives in the **MedicationAdministration**.

## What is intentionally *out* of scope for Phase 0

| Deferred concern | Why | Where it goes |
|---|---|---|
| Premedication chains (Chlorpheniramine, Cimetidine, Dexamethasone) | These are listed as `component_role = secondary systemic` sigs under the same regimen but represent institution-level policy decisions wrapping the primary regimen | Separate ActivityDefinitions + PlanDefinition.action.relatedAction in a later phase |
| Dose-banding (BOPA / HOPA tables) | Site-specific policy, not protocol-specific | bd issue `interop-prototypes-ohv` — separate Library |
| Hold-for-counts (ANC, platelets, …) | CTCAE-aligned thresholds, site-specific overrides | bd issue `interop-prototypes-9au` — PlanDefinition.action.condition + Library |
| Dose-modification rules (reduce / hold / discontinue) | Institution-authored on top of HemOnc; not in HemOnc structured data | bd issue `interop-prototypes-qbt` — separate Library |
| MedicationDispense layer | Scope decision: this catalog is not modeling pharmacy operations | n/a |
| MII / ePA / gematik profile conformance | Phase 3 concern | Later IG layer |

## Validation status

* The IG builds with SUSHI and the IG Publisher (CI workflow `build-ig`).
* `PlanDefinition/$apply` is exercised by `tests/apply` against HAPI 8.12.0
  with cqf-fhir (CI workflow `apply-scenarios`): the variant yields a CarePlan
  with two MedicationRequests, 625 mg carboplatin (Phase 0 GFR constant) and
  323.75 mg paclitaxel (Phase 0 BSA constant), with provenance codes and
  versioned `instantiatesCanonical`. Patient-derived GFR and BSA, input checks,
  parameter overrides and cycle expansion are specified as expected-failure
  scenarios (beads oncology-regimens-m75, -hsd).
* The cqf-fhir 8.4.0 bug that blocked assigning a CQL Quantity to
  `doseQuantity` is gone in 8.12.0 (scenario `cql-quantity-dynamicvalue`
  passes), so the dose expressions can move from FHIRPath sub-fields back into
  the Library.
* R4 ↔ R6: every artifact round-trips through the maps in `maps/xver/`
  (CI workflow `xver-roundtrip`).

## Snapshot provenance

* HemOncKB README: `hemonckb-raw/HemOncKB README.pdf` (v2.1, 2026-03-13)
* Concept stage: `hemonckb-raw/2026-03-12 22-20-41.concept_stage.csv`
* Relationship stage: `hemonckb-raw/2026-04-09 16-04-42.concept_relationship_stage.csv`
* Source row for Variant #83: `hemonckb-raw/additional_tables/Tables/sigs.csv`
  filtered to `regimen_cui = 2554` and `variant_cui = 144842` (two rows:
  Carboplatin and Paclitaxel).
