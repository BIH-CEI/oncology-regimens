# Artifacts Summary - European SACT Regimen Catalog — Executable Knowledge Layer for Systemic Anti-Cancer Therapy Regimens v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* **Artifacts Summary**

## Artifacts Summary

This page provides a list of the FHIR artifacts defined as part of this implementation guide.

### Knowledge Artifacts: Activity Definitions 

These define activities that can be performed as part of content in this implementation guide.

| | |
| :--- | :--- |
| [Carboplatin AUC 5 IV over 30–60 min, day 1, q21d](ActivityDefinition-sig-carboplatin-auc5-d1-q21d.md) | One sig from HemOnc Regimen 2554 ('Carboplatin and Paclitaxel (CP)') Variant #83 (cui 144842). Carboplatin as primary systemic component, target AUC 5 IV over 30–60 minutes, day 1 of a 21-day cycle, for 3–6 cycles. The declared dose is a target AUC; the dynamicValue invokes the Calvert helper to compute the mg at $apply time using the patient's GFR. |
| [Paclitaxel 175 mg/m² IV over 3 h, day 1, q21d](ActivityDefinition-sig-paclitaxel-175mgm2-d1-q21d.md) | One sig from HemOnc Regimen 2554 ('Carboplatin and Paclitaxel (CP)') Variant #83 (cui 144842). Paclitaxel as primary systemic component, 175 mg/m² IV over 3 hours, administered on day 1 of a 21-day cycle, for 3–6 cycles. Declared dose is per-m²; the dynamicValue invokes the HemOnc dose helper Library to compute the patient-specific mg at $apply time. |

### Knowledge Artifacts: Plan Definitions 

These define workflows, rules, strategies, or protocols as part of content in this implementation guide.

| | |
| :--- | :--- |
| [Carboplatin and Paclitaxel (CP) — Variant #83 (Carbo AUC 5 + Paclitaxel 175 mg/m² q21d)](PlanDefinition-regimen-2554-variant-144842.md) | One executable variant of the Carboplatin + Paclitaxel regimen (HemOnc cui 2554). Single 21-day cycle pattern repeated 3–6 times: Carboplatin target AUC 5 + Paclitaxel 175 mg/m², both IV on day 1. Sourced from HemOncKB sigs.csv snapshot 2026-03-12 (variant_cui 144842, first reported in the MITO-2 trial). This Phase 0 artifact does not include premedications, dose-modification rules, or hold-for-counts logic — those are deferred to subsequent Library resources. |

### Knowledge Artifacts: Libraries 

These define logic, asset collections and other libraries as part of content in this implementation guide.

| | |
| :--- | :--- |
| [HemOnc dose-computation helpers (BSA, Calvert)](Library-HemOncDoseHelpers.md) | CQL library providing BSA (Mosteller/Du Bois/Haycock), Cockcroft-Gault GFR, Calvert carboplatin formula, and per-sig dose helpers referenced by ActivityDefinition.dynamicValue. Phase 0 spike — covers paclitaxel and carboplatin only. Institution policy (BSA formula, BSA cap, GFR formula, GFR cap) is set via $apply Parameters. |

### Structures: Extension Definitions 

These define constraints on FHIR data types for systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [Formulary Parameter](StructureDefinition-formulary-parameter.md) | A parameter value a formulary entry pins on the referenced (parameterised) variant PlanDefinition. Forwarded by the CDS layer in the nested `parameters` of $apply. |
| [Formulary Rank](StructureDefinition-formulary-rank.md) | Optional rank of an entry within a formulary PlanDefinition. 1 = first choice. Absence means unranked. |
| [Regimen Modification](StructureDefinition-regimen-modification.md) | One delta between a derived (L2) PlanDefinition and the HemOnc variant it is derived from. Provenance only: the derived PlanDefinition SHALL be complete on its own (Rule D-1). |

### Terminology: Value Sets 

These define sets of codes used by systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [NZ colorectal permitted mFOLFOX6 variants (example)](ValueSet-nz-crc-permitted-variants.md) | Terminology twin of PlanDefinition/nz-crc-mfolfox6-formulary: the HemOnc variant CUIs and SRL-derived protocol ids a consumer may offer. SHALL stay equivalent to the formulary's definitionCanonical targets (Rule in §6). |
| [Regimen Modification Kind ValueSet](ValueSet-regimen-modification-kind-vs.md) | All kinds of regimen modification. |

### Terminology: Code Systems 

These define new code systems used by systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [HemOnc Ontology (fragment, Phase 0 spike)](CodeSystem-hemonc.md) | Fragment of the HemOnc ontology, sufficient to support the Carboplatin + Paclitaxel Variant #83 example used in the Phase 0 spike, plus the mFOLFOX6 concepts referenced by the Selection Layer example. The full CodeSystem will be emitted as content=complete from the OMOP concept_stage table in a later phase. |
| [HemOnc Sig Dose Target Type](CodeSystem-sig-target-type.md) | Small code system distinguishing the **target** expressed by a Sig's doseQuantity from the **computed** mg dose. Used as ActivityDefinition.dosage.doseAndRate.type. A target requires a CQL helper to convert into an administered mg quantity at $apply time. |
| [Regimen Modification Kind](CodeSystem-regimen-modification-kind.md) | Kinds of delta a derived (L2) PlanDefinition applies against its parent HemOnc variant. |

### Example: Example Instances 

These are example instances that show what data produced and consumed by systems conforming with this implementation guide might look like.

| | |
| :--- | :--- |
| [CRC Metastatic – mFOLFOX6 [high dose folinic acid], no fluorouracil bolus (SRL 588251000210108 v1.0.0)](PlanDefinition-srl-588251000210108-mfolfox6-nobolus.md) | Derived (L2) protocol: HemOnc mFOLFOX6 Variant #06 (cui 133145) with the fluorouracil 400 mg/m² bolus omitted, as published by the NZ SACT Regimen Library on 2026-07-01 following the NZ Society for Oncology Gastrointestinal Cancers Special Interest Group recommendation. Oxaliplatin 85 mg/m² IV over 120 min day 1; folinic acid 400 mg/m² IV over 120 min day 1; fluorouracil 2400 mg/m² IV over 46 h day 1; 14-day cycle. Supportive care (antiemetics, loperamide) as per SRL, not reproduced here. |
| [NZ colorectal formulary — mFOLFOX6 family (example, SRL read 2026-10-22)](PlanDefinition-nz-crc-mfolfox6-formulary.md) | Example formulary (selection layer, §3 of the Selection Layer page). Lists the three mFOLFOX6 specifications the NZ SACT Regimen Library publishes for colorectal cancer and maps each to its HemOnc basis. Restriction: the other 19 HemOnc mFOLFOX6 variants are not offered. Extension: two entries have no HemOnc variant and are expressed as a parameter set and a derived protocol respectively. |
| [SRL regimen id → HemOnc variant CUI (example, colorectal mFOLFOX6)](ConceptMap-srl-to-hemonc-variant.md) | Bridge ConceptMap from NZ SACT Regimen Library entries to the HemOnc variant each is based on. equivalent = dose-for-dose match; relatedto = derived with a documented modification. Not a redistribution of SRL content. |

### Other 

These are resources that are used within this implementation guide that do not fit into one of the other categories.

| |
| :--- |
| [hemonc-drug-379-paclitaxel](MedicationKnowledge-hemonc-drug-379-paclitaxel.md) |
| [hemonc-drug-88-carboplatin](MedicationKnowledge-hemonc-drug-88-carboplatin.md) |

