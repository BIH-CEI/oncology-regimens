# Carboplatin and Paclitaxel (CP) — Variant #83 (Carbo AUC 5 + Paclitaxel 175 mg/m² q21d) - European SACT Regimen Catalog — Executable Knowledge Layer for Systemic Anti-Cancer Therapy Regimens v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Carboplatin and Paclitaxel (CP) — Variant #83 (Carbo AUC 5 + Paclitaxel 175 mg/m² q21d)**

## PlanDefinition: Carboplatin and Paclitaxel (CP) — Variant #83 (Carbo AUC 5 + Paclitaxel 175 mg/m² q21d) (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://hemonc.org/fhir/PlanDefinition/regimen-2554-variant-144842 | *Version*:2026-03-12-0.1.0 |
| Active as of 2026-03-12 | *Computable Name*:CarboplatinPaclitaxelVariant83 |
| *Other Identifiers:*http://hemonc.org/cui#144842 (use: official), http://hemonc.org/regimen-cui#2554 (use: secondary) | |
| **Usage:**Clinical Focus: Carboplatin and Paclitaxel (CP) | |

 
One executable variant of the Carboplatin + Paclitaxel regimen (HemOnc cui 2554). Single 21-day cycle pattern repeated 3–6 times: Carboplatin target AUC 5 + Paclitaxel 175 mg/m², both IV on day 1. Sourced from HemOncKB sigs.csv snapshot 2026-03-12 (variant_cui 144842, first reported in the MITO-2 trial). This Phase 0 artifact does not include premedications, dose-modification rules, or hold-for-counts logic — those are deferred to subsequent Library resources. 

* **Actions: **: **Url: **
  * : [Carboplatin and Paclitaxel (CP) — Variant #83 (Carbo AUC 5 + Paclitaxel 175 mg/m² q21d)](PlanDefinition-regimen-2554-variant-144842.md)
* **Actions: **: **Version: **
  * : 2026-03-12-0.1.0
* **Actions: **: ** Official **
  * :  144842 
* **Actions: **: ** Secondary **
  * :  2554 
* **Actions: **: **Title: **
  * : Carboplatin and Paclitaxel (CP) — Variant #83 (Carbo AUC 5 + Paclitaxel 175 mg/m² q21d)
* **Actions: **: **Experimental: **
  * : true
* **Actions: **: **Date: **
  * : 2026-03-12
* **Actions: **: **Publisher: **
  * : European SACT Regimen Catalog Working Group
* **Actions: **: **Description: **
  * : One executable variant of the Carboplatin + Paclitaxel regimen (HemOnc cui 2554). Single 21-day cycle pattern repeated 3–6 times: Carboplatin target AUC 5 + Paclitaxel 175 mg/m², both IV on day 1. Sourced from HemOncKB sigs.csv snapshot 2026-03-12 (variant_cui 144842, first reported in the MITO-2 trial). This Phase 0 artifact does not include premedications, dose-modification rules, or hold-for-counts logic — those are deferred to subsequent Library resources.
* **Actions: **: **Jurisdiction: **
  * : DE
* **Actions: **: **Topic: **
  * : treatment
* **Actions: **: **Libraries: **
  * : 
| |
| :--- |
| [http://hemonc.org/fhir/Library/HemOncDoseHelpers|2026-03-12](https://simplifier.net/resolve?scope=de.medizininformatikinitiative.kerndatensatz.onkologie@2026.0.3&canonical=http://hemonc.org/fhir/Library/HemOncDoseHelpers|2026-03-12) |




## Resource Content

```json
{
  "resourceType" : "PlanDefinition",
  "id" : "regimen-2554-variant-144842",
  "url" : "http://hemonc.org/fhir/PlanDefinition/regimen-2554-variant-144842",
  "identifier" : [{
    "use" : "official",
    "system" : "http://hemonc.org/cui",
    "value" : "144842"
  },
  {
    "use" : "secondary",
    "system" : "http://hemonc.org/regimen-cui",
    "value" : "2554"
  }],
  "version" : "2026-03-12-0.1.0",
  "name" : "CarboplatinPaclitaxelVariant83",
  "title" : "Carboplatin and Paclitaxel (CP) — Variant #83 (Carbo AUC 5 + Paclitaxel 175 mg/m² q21d)",
  "type" : {
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/plan-definition-type",
      "code" : "clinical-protocol"
    }]
  },
  "status" : "active",
  "experimental" : true,
  "date" : "2026-03-12",
  "publisher" : "European SACT Regimen Catalog Working Group",
  "contact" : [{
    "name" : "European SACT Regimen Catalog Working Group",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/thome/oncology-regimens"
    }]
  }],
  "description" : "One executable variant of the Carboplatin + Paclitaxel regimen (HemOnc cui 2554). Single 21-day cycle pattern repeated 3–6 times: Carboplatin target AUC 5 + Paclitaxel 175 mg/m², both IV on day 1. Sourced from HemOncKB sigs.csv snapshot 2026-03-12 (variant_cui 144842, first reported in the MITO-2 trial). This Phase 0 artifact does not include premedications, dose-modification rules, or hold-for-counts logic — those are deferred to subsequent Library resources.",
  "useContext" : [{
    "code" : {
      "system" : "http://terminology.hl7.org/CodeSystem/usage-context-type",
      "code" : "focus"
    },
    "valueCodeableConcept" : {
      "coding" : [{
        "system" : "http://hemonc.org/fhir/CodeSystem/hemonc",
        "code" : "2554",
        "display" : "Carboplatin and Paclitaxel (CP)"
      }]
    }
  }],
  "jurisdiction" : [{
    "coding" : [{
      "system" : "urn:iso:std:iso:3166",
      "code" : "DE",
      "display" : "Germany"
    }]
  }],
  "topic" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/definition-topic",
      "code" : "treatment"
    }]
  }],
  "relatedArtifact" : [{
    "type" : "derived-from",
    "label" : "HemOncKB Regimen + Variant rows, snapshot 2026-03-12",
    "citation" : "HemOnc Dataverse v2.1 (2026-03-12). regimen_cui=2554, variant_cui=144842.",
    "url" : "https://dataverse.harvard.edu/dataverse/hemonc",
    "document" : {
      "url" : "https://dataverse.harvard.edu/dataverse/hemonc"
    }
  },
  {
    "type" : "composed-of",
    "resource" : "http://hemonc.org/fhir/ActivityDefinition/sig-carboplatin-auc5-d1-q21d|2026-03-12"
  },
  {
    "type" : "composed-of",
    "resource" : "http://hemonc.org/fhir/ActivityDefinition/sig-paclitaxel-175mgm2-d1-q21d|2026-03-12"
  },
  {
    "type" : "depends-on",
    "resource" : "http://hemonc.org/fhir/Library/HemOncDoseHelpers|2026-03-12"
  }],
  "library" : ["http://hemonc.org/fhir/Library/HemOncDoseHelpers|2026-03-12"],
  "action" : [{
    "id" : "cycle",
    "title" : "21-day cycle, repeated 3–6 times",
    "description" : "Each cycle administers Carboplatin and Paclitaxel on day 1, then a 20-day rest period before the next cycle. HemOnc cyclesigs string: '21-day cycle for 3 to 6 cycles'.",
    "timingTiming" : {
      "repeat" : {
        "count" : 3,
        "countMax" : 6,
        "frequency" : 1,
        "period" : 21,
        "periodUnit" : "d"
      }
    },
    "groupingBehavior" : "logical-group",
    "selectionBehavior" : "all",
    "action" : [{
      "id" : "carboplatin-d1",
      "extension" : [{
        "url" : "http://hemonc.org/fhir/StructureDefinition/day-of-cycle",
        "valueInteger" : 1
      }],
      "title" : "Carboplatin AUC 5 IV day 1",
      "definitionCanonical" : "http://hemonc.org/fhir/ActivityDefinition/sig-carboplatin-auc5-d1-q21d|2026-03-12"
    },
    {
      "id" : "paclitaxel-d1",
      "extension" : [{
        "url" : "http://hemonc.org/fhir/StructureDefinition/day-of-cycle",
        "valueInteger" : 1
      }],
      "title" : "Paclitaxel 175 mg/m² IV day 1",
      "relatedAction" : [{
        "actionId" : "carboplatin-d1",
        "relationship" : "concurrent-with-start"
      }],
      "definitionCanonical" : "http://hemonc.org/fhir/ActivityDefinition/sig-paclitaxel-175mgm2-d1-q21d|2026-03-12"
    }]
  }]
}

```
