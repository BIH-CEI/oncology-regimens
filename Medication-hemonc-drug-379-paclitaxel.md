# Paclitaxel - European SACT Regimen Catalog — Executable Knowledge Layer for Systemic Anti-Cancer Therapy Regimens v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Paclitaxel**

## Medication: Paclitaxel

Information Source: [https://dataverse.harvard.edu/dataverse/hemonc#drugs.csv;drug_CUI=379;snapshot=2026-03-12](https://simplifier.net/resolve?scope=de.medizininformatikinitiative.kerndatensatz.onkologie@2026.0.3&canonical=https://dataverse.harvard.edu/dataverse/hemonc#drugs.csv;drug_CUI=379;snapshot=2026-03-12)

**Artifact URL**: [http://hemonc.org/fhir/Medication/hemonc-drug-379-paclitaxel](https://simplifier.net/resolve?scope=de.medizininformatikinitiative.kerndatensatz.onkologie@2026.0.3&canonical=http://hemonc.org/fhir/Medication/hemonc-drug-379-paclitaxel)

**ArtifactVersion**: 2026-03-12

**ArtifactName**: Paclitaxel

**Artifact Publisher**: HemOnc.org

> **Medication Classification**
* type: HemOnc main class
* classification: Taxane
* source: HemOncKB drugs.csv main_class, snapshot 2026-03-12

**identifier**: `http://hemonc.org/cui`/379 (use: official)

**code**: Paclitaxel

**status**: Active



## Resource Content

```json
{
  "resourceType" : "Medication",
  "id" : "hemonc-drug-379-paclitaxel",
  "meta" : {
    "source" : "https://dataverse.harvard.edu/dataverse/hemonc#drugs.csv;drug_CUI=379;snapshot=2026-03-12"
  },
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/artifact-url",
    "valueUri" : "http://hemonc.org/fhir/Medication/hemonc-drug-379-paclitaxel"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/artifact-version",
    "valueString" : "2026-03-12"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/artifact-name",
    "valueString" : "Paclitaxel"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/artifact-publisher",
    "valueString" : "HemOnc.org"
  },
  {
    "extension" : [{
      "url" : "type",
      "valueCodeableConcept" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/medication-classification-type",
          "code" : "pharmacologic",
          "display" : "Pharmacologic Class"
        }],
        "text" : "HemOnc main class"
      }
    },
    {
      "url" : "classification",
      "valueCodeableConcept" : {
        "coding" : [{
          "system" : "http://hemonc.org/fhir/CodeSystem/hemonc",
          "code" : "Taxane",
          "display" : "Taxane"
        }]
      }
    },
    {
      "url" : "source",
      "valueString" : "HemOncKB drugs.csv main_class, snapshot 2026-03-12"
    }],
    "url" : "http://hl7.org/fhir/StructureDefinition/medication-classification"
  }],
  "identifier" : [{
    "use" : "official",
    "system" : "http://hemonc.org/cui",
    "value" : "379"
  }],
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
  "status" : "active"
}

```
