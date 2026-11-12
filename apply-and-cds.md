# PlanDefinition $apply and CDS Hooks - European SACT Regimen Catalog — Executable Knowledge Layer for Systemic Anti-Cancer Therapy Regimens v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* **PlanDefinition $apply and CDS Hooks**

## PlanDefinition $apply and CDS Hooks

### PlanDefinition $apply and CDS Hooks

The catalog is consumed at runtime via the FHIR Clinical Reasoning `$apply` operation, which takes a `PlanDefinition` and a patient context and produces a `CarePlan` containing concrete `MedicationRequest` resources with patient-specific computed doses. The same artifacts can be surfaced via CDS Hooks for in-workflow delivery at the EHR ordering moment.

#### The three-resource pipeline

```
PlanDefinition (knowledge: protocol + variant)
        │
        │  $apply(subject=Patient/x, parameters=…)
        ▼
MedicationRequest (instance: ordered, with calculation trace)
        │
        │  administered at the bedside
        ▼
MedicationAdministration (instance: actually given)

```

`MedicationDispense` is intentionally out of scope — see [Background](background.md). Pharmacy operations sit outside this IG's catalog and ordering responsibility.

#### Dose computation

Per-patient dose computation is split between `Library/HemOncDoseHelpers` (CQL: the provenance codes) and `ActivityDefinition.dynamicValue` (FHIRPath: the dose magnitude). In Phase 0 the magnitudes are constants (GFR 100 mL/min, BSA 1.85 m²); the Library declares the parameters (BSA formula and cap, GFR formula and cap, target AUC, mg/m² dose) that institution policy will supply at `$apply` time through the nested `parameters` Parameters resource, but does not read them yet. The split was a work-around for a cqf-fhir 8.4.0 bug that is gone in HAPI 8.12.0, so the computation can move into the Library; the `$apply` scenarios in `tests/apply/` (Cockcroft-Gault from creatinine, GFR cap, Mosteller BSA, missing or stale inputs, parameter override) are its specification and run as expected failures until then.

#### Input modes (which patient data, which parameters)

Four mechanisms compose freely:

1. **Server-side persisted data**. Patient + Observations live in the same FHIR server;`$apply`reads them.
1. **Inline `data` Bundle**.`Parameters`body to`$apply`carries the patient + observations as an inline Bundle;`useServerData=false`.
1. **Scalar parameters**. The nested`parameters`Parameters resource carries already-computed values (BSA, GFR, TargetAUC) directly, bypassing Observation retrieval.
1. **`dataEndpoint`**. The CR engine reads patient data from a separate FHIR server (e.g., the hospital EHR over TI), keeping knowledge artifacts on the catalog server.

#### CDS Hooks delivery

A CDS service consumes an `order-sign` hook from the EHR, invokes `PlanDefinition/$apply` internally, and returns a card containing a transaction `Bundle` of CarePlan + RequestGroup + MedicationRequests as `suggestions[0].actions[0].resource`. The clinician accepts; the EHR creates the orders.

HAPI's cqf-fhir exposes a `$cds-services` endpoint automatically for every PlanDefinition carrying an `action.trigger.type = named-event` with a CDS Hook id (e.g. `order-sign`). The same artifacts work in both delivery modes.

#### Testing $apply

`tests/apply/` holds executable scenarios: patient fixtures, the PlanDefinition, optional parameters and FHIRPath assertions over the returned CarePlan. `scripts/apply/apply_tests.py` runs them against HAPI FHIR 8.12.0 with Clinical Reasoning, locally through `phase0/docker-compose.yml` and in CI. Scenarios marked as expected failures specify open work and fail the build when they start passing, so that the marker is removed together with the issue.

