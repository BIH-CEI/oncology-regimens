# hemonc-drug-379-paclitaxel - European SACT Regimen Catalog — Executable Knowledge Layer for Systemic Anti-Cancer Therapy Regimens v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **hemonc-drug-379-paclitaxel**

## MedicationKnowledge: hemonc-drug-379-paclitaxel

Information Source: [HemOncKB drugs.csv row drug_CUI=379, snapshot 2026-03-12](https://simplifier.net/resolve?scope=de.medizininformatikinitiative.kerndatensatz.onkologie@2026.0.3&canonical=http://fhir.org/packages/de.medizininformatikinitiative.kerndatensatz.onkologie/HemOncKB drugs.csv row drug_CUI=379, snapshot 2026-03-12)

**code**: Paclitaxel

**status**: Active

**synonym**: paclitaxel, Taxol

### MedicineClassifications

| | | |
| :--- | :--- | :--- |
| - | **Type** | **Classification** |
| * | main-class | Taxane |

> **kinetics**



## Resource Content

```json
{
  "resourceType" : "MedicationKnowledge",
  "id" : "hemonc-drug-379-paclitaxel",
  "meta" : {
    "source" : "HemOncKB drugs.csv row drug_CUI=379, snapshot 2026-03-12"
  },
  "code" : {
    "coding" : [{
      "system" : "http://hemonc.org/fhir/CodeSystem/hemonc",
      "code" : "379",
      "display" : "Paclitaxel"
    },
    {
      "system" : "http://www.nlm.nih.gov/research/umls/rxnorm",
      "code" : "56946",
      "display" : "paclitaxel"
    },
    {
      "system" : "http://www.whocc.no/atc",
      "code" : "L01CD01",
      "display" : "paclitaxel"
    }],
    "text" : "Paclitaxel"
  },
  "status" : "active",
  "synonym" : ["paclitaxel", "Taxol"],
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
        "code" : "Taxane",
        "display" : "Taxane"
      }]
    }]
  }],
  "kinetics" : [null]
}

```
