# Phase 0 Spike — Carboplatin + Paclitaxel Variant - HemOnc FHIR Regimen Catalog — Executable Knowledge Layer for Oncology Protocols v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* **Phase 0 Spike — Carboplatin + Paclitaxel Variant**

## Phase 0 Spike — Carboplatin + Paclitaxel Variant

### Phase 0 Spike — Carboplatin + Paclitaxel Variant #83

The Phase 0 spike validates the end-to-end pipeline on one regimen variant from HemOncKB, against a local HAPI FHIR + cqf-fhir Clinical Reasoning instance.

#### What's included

* HemOnc regimen `2554` "Carboplatin and Paclitaxel (CP)" variant `144842` (Variant #83), first reported in the MITO-2 trial: Carbo AUC 5 + Paclitaxel 175 mg/m², IV day 1 of a 21-day cycle, for 3–6 cycles.
* All seven FHIR artifacts: `CodeSystem` (HemOnc fragment), `CodeSystem` (sig-target-type), two `MedicationKnowledge`, two `ActivityDefinition` (one per sig), one `Library` (BSA + Calvert helpers), one `PlanDefinition` (the variant with its cycle action).
* A demo Patient + height + weight + creatinine Observation Bundle.
* A `load-and-apply.sh` script that loads everything into HAPI and invokes `$apply`, returning a `CarePlan` with two computed `MedicationRequest` resources: **Carboplatin 625 mg** (Calvert) and **Paclitaxel 323.75 mg** (BSA), both with `computed-from-target-*` provenance codes.

#### Validated outcomes

1. `PlanDefinition/$apply`produces a`CarePlan`containing two`MedicationRequest`resources.
1. Each`MedicationRequest.dosageInstruction.doseAndRate`carries both the computed mg dose and the provenance code identifying the target paradigm (AUC for carboplatin, mg/m² for paclitaxel).
1. The`MedicationRequest.medicationReference`points at the IG's`MedicationKnowledge`, which carries ATC + RxNorm + HemOnc CUI for downstream RxNorm-anchored systems.
1. `instantiatesCanonical`on every emitted`MedicationRequest`resolves to the catalog`ActivityDefinition`, preserving full knowledge-to-instance provenance.

#### Known limitations (tracked)

* Dose computation is split between a CQL `Library` (the `type` CodeableConcepts) and FHIRPath in `ActivityDefinition.dynamicValue` (the `doseQuantity.value`). The CQL `System.Quantity` literal hits a coercion bug in cqf-fhir 8.4.0 when assigned to `Dosage.doseAndRate .doseQuantity`; the FHIRPath sub-field assignment works around it. Tracked for re-migration once the upstream fix lands.
* Cycle expansion (emitting per-cycle RequestGroups with calendar offsets) is not yet wired; the spike emits one MedicationRequest per sig, with the cycle structure declared in `PlanDefinition.action .timingTiming` but not unrolled.
* Premedications (Chlorpheniramine, Cimetidine, Dexamethasone for Paclitaxel) are intentionally omitted; they belong in a separate PlanDefinition layer in subsequent phases.

#### Reproducing the spike locally

The full reproduction recipe lives in `phase0/README.md` in the project repository, including the Docker Compose definition for HAPI + cqf-fhir and the `load-and-apply.sh` script. See the [Disclaimers page](disclaimers.md) — this is sandbox software, not for clinical use.

