# FHIR Versions — R4 Baseline, R5 and R6 Adaptations - European SACT Regimen Catalog — Executable Knowledge Layer for Systemic Anti-Cancer Therapy Regimens v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* **FHIR Versions — R4 Baseline, R5 and R6 Adaptations**

## FHIR Versions — R4 Baseline, R5 and R6 Adaptations

### FHIR Versions — R4 Baseline, R5 and R6 Adaptations

**Status: draft starting point for Phase 1A deliverable A.8. Facts checked against the FHIR R6 CI build (6.0.0-snapshot1, generated 2026-11-09), HL7 JIRA and the generated cross-version maps on 2026-11-10.**

#### Baseline: FHIR R4

This IG is published on **FHIR R4 (4.0.1)**. Reasons:

* The German MII Onkologie module (dependency, 2026.0.3) is R4.
* PlanDefinition execution and CDS Hooks run today on HAPI FHIR with cqf-fhir on R4; there is no clinical-reasoning implementation for R6.
* R6 is not final. The first normative ballot ran in September 2026; publication is announced for the first half of 2027. Between 6.0.0-ballot5 and the current build, Medication, Dosage and MedicationRequest changed again (see below).

#### Cross-version strategy: one source, derived views

The pattern follows the FHIR Camp 2026 experiment described by Health Samurai ("One FHIR Store, Two Versions: Serving R4 and R6 with FML", 2026-11-08): **one stored version, every other version computed by FHIR Mapping Language maps, and every write must survive the round trip** (R6 → R4 → R6 unchanged). There the store is a server and the maps run per request. Here the "store" is this repository and its R4 package, the maps run at build time, and the derived R5 and R6 packages are build outputs. Rules adopted from that work:

1. **R4 is authored and validated; R5 and R6 are derived, never edited.**A change in modelling is a change in the R4 source plus the map.
1. **Every artifact must round-trip R4 → R6 → R4 without loss.**That is the acceptance test for the maps (issue oncology-regimens-d0w).
1. **Pre-adopt R6 elements in R4 through extensions that exist in every version**, preferring the published`artifact-*`and`medication-*`extensions of`hl7.fhir.uv.extensions`over the generic cross-version URL scheme`http://hl7.org/fhir/6.0/StructureDefinition/extension-<path>`. The generic scheme is used only where no published extension exists (lossy code translations, see Medication status below).
1. **Maps are the generated cross-version maps where they are correct, hand-written where this IG's modelling needs more**(see[`maps/xver/`](https://github.com/thome/oncology-regimens/tree/main/maps/xver)in the repository). The generated maps are the 164 R4→R6 and 63 R6→R4 maps from the FHIRPath Lab executor used in that experiment.
1. **No map has been executed yet.**The HL7 validator does not run cross-version maps; the TypeScript executor has to be wired into CI first. Until then this page is the normative description and the maps are its machine-readable draft.

#### R5 with R4 backport

The rule is "R5 semantics, R4 syntax". Where an R5 element is needed in R4, the cross-version extension package `hl7.fhir.uv.xver-r5.r4` provides it. **Currently no cross-version extension is in use**:

| | | |
| :--- | :--- | :--- |
| `Medication` | `form`→`doseForm`;`ingredient.item[x]`→ CodeableReference; adds`definition`,`marketingAuthorizationHolder`,`totalVolume` | No. The catalog`Medication`uses`identifier`,`code`,`status`and extensions only. |
| `ActivityDefinition` | `product[x]`reference targets add`Ingredient`,`SubstanceDefinition`;`subject[x]`adds canonical | No.`productReference`targets`Medication`, valid in R4, R5 and R6. |
| `PlanDefinition` | adds`actor`,`action.location`,`action.input/output`become backbone elements | No. This IG uses`action.definitionCanonical`,`action.selectionBehavior`,`action.timingTiming`,`action.relatedAction`,`action.code`(at most one),`relatedArtifact`,`useContext`. |
| `ConceptMap` | `group.element.target.equivalence`→`relationship` | Yes, at publication: the generated map does**not**read`equivalence`, so the hand-written map must translate`equivalent`,`wider`→`source-is-narrower-than-target`,`narrower`→`source-is-broader-than-target`,`unmatched`→`not-related-to`. No ConceptMap instance exists in the IG yet. |
| `Library`,`CodeSystem`,`ValueSet` | no structural change for the elements used | No. |

#### R6: what changes per artifact type

| | | | |
| :--- | :--- | :--- | :--- |
| `Medication`(kind of drug, catalog level) | `identifier`(HemOnc CUI),`code`(coding stack),`status`; canonical metadata via`artifact-url`,`artifact-version`,`artifact-name`,`artifact-publisher`; classes via`medication-classification`; investigational flag via`medication-type` | `Medication`**is a canonical resource**([FHIR-57813](https://jira.hl7.org/browse/FHIR-57813)): the four`artifact-*`extensions become native`url`,`version`,`name`,`publisher`.`status`is bound to PublicationStatus ([FHIR-59543](https://jira.hl7.org/browse/FHIR-59543)):`active`unchanged,`inactive`and`entered-in-error`become`retired`.**`Medication.classification` is not in the build**;[FHIR-59521](https://jira.hl7.org/browse/FHIR-59521)is open, so`medication-classification`stays an extension. | hand-written`Medication_4to6`/`_6to4`(the generated map was made from ballot5, where Medication had no canonical elements) |
| `MedicationKnowledge` | **not used**(removed from this IG 2026-11-10) | **Removed from the specification**([FHIR-50845](https://jira.hl7.org/browse/FHIR-50845), Pharmacy WG, Madrid WGM May 2025, 12-0-4). Not moved to an incubator. Element mapping in[FHIR-57378](https://jira.hl7.org/browse/FHIR-57378); see below. | none needed |
| `ActivityDefinition`(sig) | `kind = MedicationRequest`,`productReference → Medication`,`dosage`0..* with`sequence`,`timing`,`route`,`doseAndRate`;`dynamicValue`paths on`MedicationRequest.dosageInstruction[0]...` | **Remodelled.**`dosage`becomes`dosageInstruction`0..1 of the new type`DosageInstruction`([FHIR-53721](https://jira.hl7.org/browse/FHIR-53721),[FHIR-54340](https://jira.hl7.org/browse/FHIR-54340)):`renderedInstruction`,`repeatCycle`(Duration,[FHIR-54252](https://jira.hl7.org/browse/FHIR-54252)),`step[]`with`start`/`end`(RelativeTime),`count`,`component`(Dosage 1..*),`safety`.`Dosage`loses`sequence`and`maxDose*`, gains`condition`,`safety`, and`doseExpression`/`rateExpression`.`MedicationRequest.dosageInstruction`is 0..1`DosageInstruction`as well, so every`dynamicValue.path`changes.`timing[x]`drops dateTime and Period (unused here).`product`may not reference`Substance`(unused). | hand-written,**to do**(issue oncology-regimens-u7w). The generated map puts each R4`Dosage`into its own sequential`step`, which is wrong for concurrent components sharing one`sequence`. |
| `PlanDefinition`(regimen, variant, derived protocol, formulary) | see[Selection Layer](selection-layer.md) | `action.code`becomes 0..1 (this IG uses at most one);`action.relatedAction.actionId`→`targetId`;`action.timing[x]`drops dateTime and Period (this IG uses Timing);`action.input/output`become backbone elements (unused). No removal. | generated map sufficient |
| `Library`(CQL, FHIRPath) | `type = logic-library`,`content` | Unchanged. The CQL itself must be re-checked where it reads`dosageInstruction`. | generated |
| `CodeSystem`,`ValueSet`,`ConceptMap` | HemOnc fragment, sig-target-type, MII bindings | `ConceptMap`as in the R5 row. Others unchanged. | generated (+ hand-written ConceptMap once one exists) |
| Extensions`day-of-cycle`,`formulary-rank`,`formulary-parameter`,`regimen-modification` | defined in this IG | URLs are version-independent.`day-of-cycle`is the one whose**meaning**has a native R6 home:`DosageInstruction.step.start`as RelativeTime offset from the cycle start. | part of the sig map |

##### Why the R6 dosage model matters for this IG

The R6 `DosageInstruction` expresses what this IG currently builds from R4 `Dosage` plus extensions:

| | | |
| :--- | :--- | :--- |
| cycle length (q21d) | `Dosage.timing.repeat.period = 21 d` | `DosageInstruction.repeatCycle = 21 d` |
| day of cycle | extension`day-of-cycle`on`Dosage` | `step.start`(RelativeTime offset) |
| concurrent components of one day | several`Dosage`with the same`sequence` | several`component`in one`step` |
| sequential phases | `Dosage.sequence`1, 2, … or chained PlanDefinition actions | `step[]`in order,`step.count` |
| dose formula (Calvert, mg/m²) | `dynamicValue`with FHIRPath/CQL on the request | `doseAndRate.doseExpression`(Expression) in the definition itself;`dynamicValue`still available |
| hold / modify rules | out of scope (site policy, future Library) | `Dosage.condition`(DosageCondition),`safety`(DosageSafety with dose limits) |
| number of cycles (3–6) | `timing.repeat.boundsRange`in cycles | not an element: "It does not say how many cycles are taken" (dosage.html).`renderedInstruction`or PlanDefinition context. Feedback item. |

This is the one place where R6 is a remodel rather than a rename. The R4 sig profile of this IG will be constrained so that the mapping is deterministic (same `sequence` = one step; `day-of-cycle` = step offset; one `period` = `repeatCycle`), and the R6 shape is reported back to the Pharmacy WG with worked oncology examples (issue oncology-regimens-pxp).

##### MedicationKnowledge → this IG

Mapping of the `MedicationKnowledge` elements this IG used in Phase 0, following the Pharmacy WG mapping in FHIR-57378 (Rotterdam WGM, May 2026):

| | | |
| :--- | :--- | :--- |
| `code` | `Medication.code` | same |
| `status` | `Medication.status` | PublicationStatus |
| `synonym`(R4 only) | not carried; synonyms belong to the terminology layer (`CodeSystem.concept.designation`of the HemOnc fragment) | same |
| `medicineClassification` | extension`medication-classification`(`type`,`classification`,`source`) | same extension until FHIR-59521 lands as`Medication.classification` |
| `productType`(e.g. investigational) | extension`medication-type` | same extension |
| `kinetics`,`monograph`,`relatedMedicationKnowledge` | not carried (narrative only in Phase 0) | undecided in FHIR-57378 |
| `cost`,`regulatory`,`packaging` | never used | `FormularyItem`,`MedicinalProductDefinition`family |

#### FormularyItem (R6 Additional Resource)

`FormularyItem` is published by the Pharmacy WG in the [R6 Pharmacy Incubator](https://build.fhir.org/ig/HL7/phx-incubator/) as an **Additional Resource**, i.e. outside the core specification, usable with R6 through the `resourceDefinition` mechanism. It describes "a product or service that is available through a program and includes the conditions and constraints of availability". Key elements: `status`, `category`, `context` (Organization | InsurancePlan), `subject` (CodeableReference to `Medication`, `ActivityDefinition`, `MedicinalProductDefinition`, `PackagedProductDefinition`, `DeviceDefinition`, `NutritionProduct`, `ObservationDefinition`), `cost`, `availabilityStatus`, `availabilityPeriod`, `coverageInformation`, `substitution`, `maxDispense`, `indicationGuideline`, `associatedItems`.

Relationship to the [Selection Layer](selection-layer.md):

| | | |
| :--- | :--- | :--- |
| Which protocols a site or body offers (restriction), ranked, with pinned parameters | formulary`PlanDefinition`with`action.definitionCanonical`,`formulary-rank`,`formulary-parameter` | **stays `PlanDefinition`.**`FormularyItem.subject`cannot reference`PlanDefinition`, so a formulary of regimens is not a set of FormularyItems. |
| Drug-level availability, substitution, maximum dispense, cost, coverage for a program | out of scope (no element in this IG) | `FormularyItem`with`subject → Medication`(the catalog Medication of this IG),`context → Organization`. |
| Sig-level constraints of a program (e.g. a site allows one sig of a drug) | out of scope | `FormularyItem`with`subject → ActivityDefinition`(the sig). |

Open point for feedback to the Pharmacy WG (deliverable C.5): add `PlanDefinition` to `FormularyItem.subject`, so that a formulary entry can be a protocol rather than a drug or a single sig. Until then, protocol formularies remain `PlanDefinition` in all FHIR versions, which is also the representation `$apply` and CDS Hooks consume.

#### Decision log

| | | |
| :--- | :--- | :--- |
| 2026-11-10 | Catalog drug resource is`Medication`, not`MedicationKnowledge`; canonical metadata via`artifact-*`extensions; classes via`medication-classification` | FHIR-50845, FHIR-57378, FHIR-57813; Pharmacy WG minutes Madrid 2025-05-12 |
| 2026-11-10 | No cross-version extensions in use;`hl7.fhir.uv.xver-r5.r4`is the designated package if one becomes necessary | this page |
| 2026-11-10 | Protocol formularies stay`PlanDefinition`;`FormularyItem`is the R6 target for drug- and sig-level program constraints only | phx-incubator FormularyItem 0.1.0 |
| 2026-11-10 | One R4 source, derived R5/R6 views by FML maps at build time, round-trip as acceptance test; generated maps where correct, hand-written for Medication (canonical elements) and the sig (DosageInstruction) | Health Samurai FHIR Camp 2026 write-up; generated maps from ballot5; R6 snapshot1 |

