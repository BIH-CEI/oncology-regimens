# hemonc-drug-88-carboplatin - European SACT Regimen Catalog — Executable Knowledge Layer for Systemic Anti-Cancer Therapy Regimens v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **hemonc-drug-88-carboplatin**

## MedicationKnowledge: hemonc-drug-88-carboplatin

Information Source: [HemOncKB drugs.csv row drug_CUI=88, snapshot 2026-03-12](https://simplifier.net/resolve?scope=de.medizininformatikinitiative.kerndatensatz.onkologie@2026.0.3&canonical=http://fhir.org/packages/de.medizininformatikinitiative.kerndatensatz.onkologie/HemOncKB drugs.csv row drug_CUI=88, snapshot 2026-03-12)

**code**: Carboplatin

**status**: Active

**synonym**: carboplatin, CBDCA

> **medicineClassification****type**: main-class**classification**: Platinum agent

> **medicineClassification****type**: CanMED-major**classification**: Alkylating agent

> **kinetics**



## Resource Content

```json
{
  "resourceType" : "MedicationKnowledge",
  "id" : "hemonc-drug-88-carboplatin",
  "meta" : {
    "source" : "HemOncKB drugs.csv row drug_CUI=88, snapshot 2026-03-12"
  },
  "code" : {
    "coding" : [{
      "system" : "http://hemonc.org/fhir/CodeSystem/hemonc",
      "code" : "88",
      "display" : "Carboplatin"
    },
    {
      "system" : "http://www.nlm.nih.gov/research/umls/rxnorm",
      "code" : "40048",
      "display" : "carboplatin"
    },
    {
      "system" : "http://www.whocc.no/atc",
      "code" : "L01XA02",
      "display" : "carboplatin"
    }],
    "text" : "Carboplatin"
  },
  "status" : "active",
  "synonym" : ["carboplatin", "CBDCA"],
  "medicineClassification" : [{
    "type" : {
      "coding" : [{
        "system" : "http://hemonc.org/fhir/CodeSystem/hemonc-classification-axis",
        "code" : "main-class"
      }]
    },
    "classification" : [{
      "coding" : [{
        "system" : "http://hemonc.org/fhir/CodeSystem/hemonc",
        "code" : "PlatinumAgent",
        "display" : "Platinum agent"
      }]
    }]
  },
  {
    "type" : {
      "coding" : [{
        "system" : "http://hemonc.org/fhir/CodeSystem/hemonc-classification-axis",
        "code" : "CanMED-major"
      }]
    },
    "classification" : [{
      "coding" : [{
        "system" : "http://hemonc.org/fhir/CodeSystem/hemonc",
        "code" : "AlkylatingAgent",
        "display" : "Alkylating agent"
      }]
    }]
  }],
  "kinetics" : [null]
}

```
