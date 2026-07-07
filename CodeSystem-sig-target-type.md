# HemOnc Sig Dose Target Type - HemOnc FHIR Regimen Catalog — Executable Knowledge Layer for Oncology Protocols v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **HemOnc Sig Dose Target Type**

## CodeSystem: HemOnc Sig Dose Target Type (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://hemonc.org/fhir/CodeSystem/sig-target-type | *Version*:2026-03-12-0.1.0 |
| Active as of 2026-03-12 | *Computable Name*:HemOncSigTargetType |

 
Small code system distinguishing the **target** expressed by a Sig's doseQuantity from the **computed** mg dose. Used as ActivityDefinition.dosage.doseAndRate.type. A target requires a CQL helper to convert into an administered mg quantity at $apply time. 

 This Code system is referenced in the content logical definition of the following value sets: 

* This CodeSystem is not used here; it may be used elsewhere (e.g. specifications and/or implementations that use this content)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "sig-target-type",
  "url" : "http://hemonc.org/fhir/CodeSystem/sig-target-type",
  "version" : "2026-03-12-0.1.0",
  "name" : "HemOncSigTargetType",
  "title" : "HemOnc Sig Dose Target Type",
  "status" : "active",
  "experimental" : true,
  "date" : "2026-03-12",
  "publisher" : "HemOnc FHIR Catalog Working Group",
  "contact" : [{
    "name" : "HemOnc FHIR Catalog Working Group",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/thome/oncology-regimens"
    }]
  }],
  "description" : "Small code system distinguishing the *target* expressed by a Sig's doseQuantity from the *computed* mg dose. Used as ActivityDefinition.dosage.doseAndRate.type. A target requires a CQL helper to convert into an administered mg quantity at $apply time.",
  "jurisdiction" : [{
    "coding" : [{
      "system" : "urn:iso:std:iso:3166",
      "code" : "DE",
      "display" : "Germany"
    }]
  }],
  "caseSensitive" : true,
  "content" : "complete",
  "concept" : [{
    "code" : "target-mg-per-m2",
    "display" : "Target dose expressed in mg/m² (multiply by BSA at $apply)",
    "definition" : "The doseQuantity is the literal per-m² target from the protocol. Computed mg = doseQuantity.value × BSA(patient, formula, cap)."
  },
  {
    "code" : "target-AUC",
    "display" : "Carboplatin AUC target (apply Calvert formula)",
    "definition" : "The doseQuantity is the target AUC. Computed mg = AUC × (effectiveGFR + 25), where effectiveGFR is min(GFR(patient, formula), GFR-cap)."
  },
  {
    "code" : "target-mg-per-kg",
    "display" : "Target dose expressed in mg/kg (multiply by weight)",
    "definition" : "The doseQuantity is the literal per-kg target. Computed mg = doseQuantity.value × WeightKg(patient)."
  },
  {
    "code" : "target-absolute-mg",
    "display" : "Literal absolute mg dose (no patient-specific computation needed)",
    "definition" : "The doseQuantity is the dispensed mg as-is. CQL helpers are not invoked."
  },
  {
    "code" : "computed-from-target-AUC",
    "display" : "Computed mg dose derived from a target-AUC (provenance marker)",
    "definition" : "Set on MedicationRequest.dosageInstruction.doseAndRate.type after $apply, so the original target paradigm is recoverable from the order."
  },
  {
    "code" : "computed-from-target-mg-per-m2",
    "display" : "Computed mg dose derived from a per-m² target (provenance marker)",
    "definition" : "Set on MedicationRequest.dosageInstruction.doseAndRate.type after $apply."
  }]
}

```
