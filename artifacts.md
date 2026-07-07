# Artifacts Summary - HemOnc FHIR Regimen Catalog — Executable Knowledge Layer for Oncology Protocols v2026-03-12-0.1.0

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

### Terminology: Code Systems 

These define new code systems used by systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [HemOnc Ontology (fragment, Phase 0 spike)](CodeSystem-hemonc.md) | Fragment of the HemOnc ontology, sufficient to support the Carboplatin + Paclitaxel Variant #83 example used in the Phase 0 spike. The full CodeSystem will be emitted as content=complete from the OMOP concept_stage table in a later phase. |
| [HemOnc Sig Dose Target Type](CodeSystem-sig-target-type.md) | Small code system distinguishing the **target** expressed by a Sig's doseQuantity from the **computed** mg dose. Used as ActivityDefinition.dosage.doseAndRate.type. A target requires a CQL helper to convert into an administered mg quantity at $apply time. |

### Other 

These are resources that are used within this implementation guide that do not fit into one of the other categories.

| |
| :--- |
| [hemonc-drug-379-paclitaxel](MedicationKnowledge-hemonc-drug-379-paclitaxel.md) |
| [hemonc-drug-88-carboplatin](MedicationKnowledge-hemonc-drug-88-carboplatin.md) |

