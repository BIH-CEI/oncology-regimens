### FHIR Versions — R4 Baseline, R5 and R6 Adaptations

*Status: draft starting point for Phase 1A deliverable A.8. Facts checked
against the FHIR R6 CI build (6.0.0-snapshot1, 2026-11-09) and HL7 JIRA on
2026-11-10.*

#### Baseline: FHIR R4

This IG is published on **FHIR R4 (4.0.1)**. Reasons:

- The German MII Onkologie module (dependency, 2026.0.3) is R4.
- PlanDefinition execution and CDS Hooks run today on HAPI FHIR with
  cqf-fhir on R4; there is no clinical-reasoning implementation for R6.
- R6 is not final. The first normative ballot ran in September 2026;
  publication is announced for the first half of 2027.

The design rule for every artifact type is therefore: **model in R4 so
that the R6 migration is a mechanical rename, not a remodelling.** Where
R4 lacks an element that R6 has, the IG pre-adopts the element through
the standard extension from `hl7.fhir.uv.extensions` (the same URLs exist
in the R4, R5 and R6 flavours of that package).

#### R5 with R4 backport

The second rule is "R5 semantics, R4 syntax". Where an R5 element is
needed in R4, the cross-version extension package
`hl7.fhir.uv.xver-r5.r4` provides it. **Currently no cross-version
extension is in use**, because none of the R5 changes touches an element
this IG relies on:

| Resource | R4 → R5 change | Affects this IG? |
|---|---|---|
| `Medication` | `form` → `doseForm`; `ingredient.item[x]` → CodeableReference; adds `definition`, `marketingAuthorizationHolder`, `totalVolume` | No. The catalog `Medication` uses `identifier`, `code`, `status` and extensions only. |
| `ActivityDefinition` | `product[x]` reference targets add `Ingredient`, `SubstanceDefinition`; `subject[x]` adds canonical | No. `productReference` targets `Medication`, valid in R4, R5 and R6. |
| `PlanDefinition` | adds `actor`, `action.location` (CodeableReference), `action.type` binding changes | No. The regimen, variant, derived-protocol and formulary PlanDefinitions use `action.definitionCanonical`, `action.selectionBehavior`, `action.timingTiming`, `relatedArtifact`, `useContext`. |
| `ConceptMap` | `group.element.target.equivalence` → `relationship` (new code set) | Yes, at publication time: the R4 `equivalence` codes map 1:1 to R5 `relationship` codes for the values used here (`equivalent`, `narrower`/`source-is-broader-than-target`, `wider`/`source-is-narrower-than-target`, `unmatched`/`not-related-to`). Tooling handles this; no extension needed. |
| `Library`, `CodeSystem`, `ValueSet` | no structural change for the elements used | No. |

#### R6: what changes per artifact type

| Artifact type | R4 representation in this IG | R6 target |
|---|---|---|
| `Medication` (kind of drug, catalog level) | `Medication` with `identifier` (HemOnc CUI), `code` (coding stack), `status`; canonical metadata via `artifact-url`, `artifact-version`, `artifact-name`, `artifact-publisher` extensions (`artifact-status` is not used: it is a modifier extension and `Medication.status` already exists); classes via `medication-classification` extension | `Medication` as **canonical resource** ([FHIR-57813](https://jira.hl7.org/browse/FHIR-57813)): the four `artifact-*` extensions become native `url`, `version`, `name`, `publisher`; `status` is re-bound to the union of publication and medication status, `active` stays valid. `medication-classification` becomes native `Medication.classification` ([FHIR-59521](https://jira.hl7.org/browse/FHIR-59521), [FHIR-59525](https://jira.hl7.org/browse/FHIR-59525)). `identifier` and `code` unchanged. |
| `MedicationKnowledge` | **not used** (removed from this IG 2026-11-10) | **Removed from the specification** ([FHIR-50845](https://jira.hl7.org/browse/FHIR-50845), Pharmacy WG, Madrid WGM May 2025, vote 12-0-4). Not moved to an incubator. Element mapping published with [FHIR-57378](https://jira.hl7.org/browse/FHIR-57378); see below. |
| `ActivityDefinition` (sig) | `kind = MedicationRequest`, `productReference → Medication`, `dosage`, `dynamicValue`, `library` | Unchanged for the elements used. `product` cannot reference `MedicationKnowledge` in any FHIR version, which is the second reason the catalog drug resource is `Medication`. |
| `PlanDefinition` (regimen, variant, derived protocol, formulary) | see [Selection Layer](selection-layer.html) | No removal known. To be re-verified against the R6 build at publication. |
| `Library` (CQL, FHIRPath) | `type = logic-library`, `content` | Unchanged. |
| `CodeSystem`, `ValueSet`, `ConceptMap` | HemOnc fragment, sig-target-type, MII bindings | `ConceptMap` as in the R5 row. Others unchanged. |
| Extensions `day-of-cycle`, `formulary-rank`, `formulary-parameter`, `regimen-modification` | defined in this IG | Unchanged (extension URLs are version-independent). |

##### MedicationKnowledge → this IG

Mapping of the `MedicationKnowledge` elements this IG used in Phase 0,
following the Pharmacy WG mapping in FHIR-57378 (Rotterdam WGM, May 2026):

| MedicationKnowledge (R4/R5) | Here (R4) | R6 |
|---|---|---|
| `code` | `Medication.code` | same |
| `status` | `Medication.status` | same |
| `synonym` (R4 only) | not carried; synonyms belong to the terminology layer (`CodeSystem.concept.designation` of the HemOnc fragment) | same |
| `medicineClassification` | extension `medication-classification` (`type`, `classification`, `source`) | `Medication.classification` |
| `productType` (e.g. investigational) | extension `medication-type` | same extension |
| `kinetics`, `monograph`, `relatedMedicationKnowledge` | not carried (narrative only in Phase 0) | undecided in FHIR-57378 |
| `cost`, `regulatory`, `packaging` | never used | `FormularyItem`, `MedicinalProductDefinition` family |

#### FormularyItem (R6 Additional Resource)

`FormularyItem` is published by the Pharmacy WG in the
[R6 Pharmacy Incubator](https://build.fhir.org/ig/HL7/phx-incubator/)
as an *Additional Resource*, i.e. outside the core specification, usable
with R6 through the `resourceDefinition` mechanism. It describes "a
product or service that is available through a program and includes the
conditions and constraints of availability". Key elements: `status`,
`category`, `context` (Organization | InsurancePlan), `subject`
(CodeableReference to `Medication`, `ActivityDefinition`,
`MedicinalProductDefinition`, `PackagedProductDefinition`,
`DeviceDefinition`, `NutritionProduct`, `ObservationDefinition`), `cost`,
`availabilityStatus`, `availabilityPeriod`, `coverageInformation`,
`substitution`, `maxDispense`, `indicationGuideline`, `associatedItems`.

Relationship to the [Selection Layer](selection-layer.html):

| Selection-layer concept | R4 (this IG) | R6 |
|---|---|---|
| Which protocols a site or body offers (restriction), ranked, with pinned parameters | formulary `PlanDefinition` with `action.definitionCanonical`, `formulary-rank`, `formulary-parameter` | **stays `PlanDefinition`.** `FormularyItem.subject` cannot reference `PlanDefinition`, so a formulary of regimens is not a set of FormularyItems. |
| Drug-level availability, substitution, maximum dispense, cost, coverage for a program | out of scope (no element in this IG) | `FormularyItem` with `subject → Medication` (the catalog Medication of this IG), `context → Organization`. |
| Sig-level constraints of a program (e.g. a site allows one sig of a drug) | out of scope | `FormularyItem` with `subject → ActivityDefinition` (the sig). |

Open point for feedback to the Pharmacy WG (deliverable C.5): add
`PlanDefinition` to `FormularyItem.subject`, so that a formulary entry can
be a protocol rather than a drug or a single sig. Until then, protocol
formularies remain `PlanDefinition` in all FHIR versions, which is also the
representation `$apply` and CDS Hooks consume.

#### Decision log

| Date | Decision | Source |
|---|---|---|
| 2026-11-10 | Catalog drug resource is `Medication`, not `MedicationKnowledge`; canonical metadata via `artifact-*` extensions; classes via `medication-classification` | FHIR-50845, FHIR-57378, FHIR-57813; Pharmacy WG minutes Madrid 2025-05-12 |
| 2026-11-10 | No cross-version extensions in use; `hl7.fhir.uv.xver-r5.r4` is the designated package if one becomes necessary | this page |
| 2026-11-10 | Protocol formularies stay `PlanDefinition`; `FormularyItem` is the R6 target for drug- and sig-level program constraints only | phx-incubator FormularyItem 0.1.0 |
