# Background and Scope - European SACT Regimen Catalog — Executable Knowledge Layer for Systemic Anti-Cancer Therapy Regimens v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* **Background and Scope**

## Background and Scope

### Background and Scope

#### Why this IG exists

Existing FHIR work in oncology — mCODE, MII Onkologie, the HL7 Europe Cancer Common Model (ECCM), Te Aho o Te Kahu, IDEA4RC — defines profiles on patient-level resources (Condition, Observation, MedicationRequest, MedicationStatement, Procedure) for **recording what was done to a patient**. It does not provide a catalog of executable treatment protocols, nor patient-specific dose computation, nor a CDS-Hooks-shaped delivery model. That gap is structural: most national oncology IGs are authored by registry and documentation stakeholders, not by ordering or decision-support stakeholders.

One national catalog of executable-grade regimen specifications does exist outside FHIR: the New Zealand SACT Regimen Library (Te Aho o Te Kahu / NZ Formulary, ~840 regimens, SNOMED CT NZ concept ids, semantic versions, per-cycle dose tables including supportive care). It is not openly licensed and not FHIR, and the companion ACT-NOW FHIR IG covers only patient-level CarePlan/MedicationAdministration. It is used here as a comparator and as the worked example of the [Selection Layer](selection-layer.md).

This IG fills the gap at the catalog layer.

#### Conceptual layering

```
   ┌─────────────────────────────────────────┐
   │  Patient-level recording (existing)     │
   │   mCODE / MII Onko Procedure +          │
   │   MedicationStatement / ECCM            │ ← what was given
   │   CancerTreatment.SystemicTreatment     │
   └────────────────┬────────────────────────┘
                    │ instantiated by
                    ▼
   ┌─────────────────────────────────────────┐
   │  Catalog (this IG)                      │ ← what to give
   │   PlanDefinition (regimen + variant)    │
   │   ActivityDefinition (sig)              │
   │   MedicationKnowledge (drug + class)    │
   │   Library (BSA, Calvert, …)             │
   └─────────────────────────────────────────┘
                    ▲
                    │ derived from
   ┌─────────────────────────────────────────┐
   │  Source of truth                         │
   │   HemOncKB (CC BY 4.0, OMOP-canonical)  │
   │   + primary clinical-trial publications │
   └─────────────────────────────────────────┘

```

#### In scope

* FHIR R4 `CodeSystem`, `ValueSet`, `ConceptMap` for HemOnc concepts and the small `sig-target-type` vocabulary.
* `MedicationKnowledge` per HemOnc drug, with ATC / RxNorm / HemOnc CUI codings.
* `PlanDefinition` per HemOnc regimen variant, identified by HemOnc regimen + variant CUIs (stable, sharp), with experimental MII Onkologie protocol-code bindings as secondary identifiers.
* `ActivityDefinition` per HemOnc sig.
* `Library` (CQL + FHIRPath) for dose computation.
* A small set of profiles only on resources where this IG makes load-bearing decisions; everything else uses base R4.

#### Out of scope (now)

* Per-patient FHIR profiles. Use mCODE / MII Onko / ECCM downstream.
* `MedicationDispense`. Pharmacy operations are out of scope.
* Dose-banding, hold-for-counts, dose-modification rules. Site policy, tracked as future Libraries.
* PZN / national drug-product code resolution. Companion IG pattern with empty ConceptMap stubs; institutions populate from their licensed Pharmadatenbank.
* AWMF S3-Leitlinien content. Different licensing surface.

#### Versioning

Every artifact carries `version = <HemOnc snapshot date>` (e.g. `2026-03-12`), so consumers can pin a catalog version against a specific HemOnc release. See the [Versioning page](versioning.md) for the policy details and the relationship to PHOENIX / ECCM publication cycles.

