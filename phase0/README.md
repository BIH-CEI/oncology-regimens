# Phase 0 — Carbo/Taxol Variant #83 end-to-end spike

Goal: prove the HemOnc → FHIR R4 knowledge artifact pipeline end-to-end with one
real regimen variant, so the patterns, canonical URLs, versioning, and CQL
layering can be validated before scaling to the full HemOncKB.

Source: HemOnc Dataverse, snapshot **2026-03-12**.
Regimen: `2554` "Carboplatin and Paclitaxel (CP)".
Variant: `144842` "Variant #83" (Carboplatin AUC 5 + Paclitaxel 175 mg/m², q21d,
3–6 cycles; first reported in MITO-2).

## Artifacts in this folder

```
phase0/
├── README.md                                              ← this file
├── cql/
│   └── HemOncDoseHelpers.cql                              ← source CQL
└── resources/
    ├── CodeSystem-hemonc-fragment.json                    ← HemOnc concepts (fragment)
    ├── CodeSystem-sig-target-type.json                    ← target-AUC, target-mg-per-m2, …
    ├── MedicationKnowledge-hemonc-drug-88-carboplatin.json
    ├── MedicationKnowledge-hemonc-drug-379-paclitaxel.json
    ├── ActivityDefinition-sig-carboplatin-auc5-d1-q21d.json
    ├── ActivityDefinition-sig-paclitaxel-175mgm2-d1-q21d.json
    ├── Library-hemonc-dose-helpers.json                   ← CQL embedded as base64
    ├── PlanDefinition-regimen-2554-variant-144842.json    ← the executable variant
    └── Bundle-phase0-knowledge.json                       ← collection manifest
```

## Canonical URL scheme (stable across releases)

```
http://hemonc.org/fhir/<ResourceType>/<stable-id>
```

* `CodeSystem/hemonc`
* `CodeSystem/sig-target-type`
* `MedicationKnowledge/hemonc-drug-<CUI>-<inn>`
* `ActivityDefinition/sig-<component>-<dose>-<schedule>` *(or a content hash once we scale)*
* `PlanDefinition/regimen-<regimen_cui>-variant-<variant_cui>`
* `Library/hemonc-dose-helpers`

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

Resources are hand-authored R4 JSON. **Not yet validated** against:
- HL7 FHIR R4 spec via `fhir validator`
- HAPI Clinical Reasoning `$apply` (would require a HAPI instance with the
  Library precompiled and a stub Patient bundle including height, weight,
  creatinine, age, sex)

Next concrete step is to spin up a local HAPI + cqf-fhir, post the Bundle,
post a stub Patient + Observations, and call
`PlanDefinition/$apply?subject=Patient/x` to confirm the emitted CarePlan
contains MedicationRequests with computed mg doses.

## Snapshot provenance

* HemOncKB README: `hemonckb-raw/HemOncKB README.pdf` (v2.1, 2026-03-13)
* Concept stage: `hemonckb-raw/2026-03-12 22-20-41.concept_stage.csv`
* Relationship stage: `hemonckb-raw/2026-04-09 16-04-42.concept_relationship_stage.csv`
* Source row for Variant #83: `hemonckb-raw/additional_tables/Tables/sigs.csv`
  filtered to `regimen_cui = 2554` and `variant_cui = 144842` (two rows:
  Carboplatin and Paclitaxel).
