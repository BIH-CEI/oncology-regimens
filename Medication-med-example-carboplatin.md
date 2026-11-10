# Carboplatin - European SACT Regimen Catalog — Executable Knowledge Layer for Systemic Anti-Cancer Therapy Regimens v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Carboplatin**

## Example Medication: Carboplatin

**Artifact URL**: [http://hemonc.org/fhir/Medication/med-example-carboplatin](https://simplifier.net/resolve?scope=de.medizininformatikinitiative.kerndatensatz.onkologie@2026.0.3&canonical=http://hemonc.org/fhir/Medication/med-example-carboplatin)

**ArtifactVersion**: 2026-03-12

**ArtifactName**: Carboplatin

**Artifact Publisher**: HemOnc.org

> **Medication Classification**
* type: HemOnc main class
* classification: Platinum agent
* source: HemOncKB drugs.csv main_class, snapshot 2026-03-12

> **Medication Classification**
* type: CanMED major class
* classification: Alkylating agent
* source: HemOncKB drugs.csv CanMED_major_class, snapshot 2026-03-12

**identifier**: `http://hemonc.org/cui`/88 (use: official)

**code**: Carboplatin

**status**: Active



## Resource Content

```json
{
  "resourceType" : "Medication",
  "id" : "med-example-carboplatin",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/artifact-url",
    "valueUri" : "http://hemonc.org/fhir/Medication/med-example-carboplatin"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/artifact-version",
    "valueString" : "2026-03-12"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/artifact-name",
    "valueString" : "Carboplatin"
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
          "system" : "http://hl7.org/fhir/CodeSystem/medication-classification-type",
          "code" : "pharmacologic",
          "display" : "Pharmacologic Class"
        }],
        "text" : "HemOnc main class"
      }
    },
    {
      "url" : "classification",
      "valueCodeableConcept" : {
        "text" : "Platinum agent"
      }
    },
    {
      "url" : "source",
      "valueString" : "HemOncKB drugs.csv main_class, snapshot 2026-03-12"
    }],
    "url" : "http://hl7.org/fhir/StructureDefinition/medication-classification"
  },
  {
    "extension" : [{
      "url" : "type",
      "valueCodeableConcept" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/CodeSystem/medication-classification-type",
          "code" : "moa",
          "display" : "Mechanism of Action"
        }],
        "text" : "CanMED major class"
      }
    },
    {
      "url" : "classification",
      "valueCodeableConcept" : {
        "text" : "Alkylating agent"
      }
    },
    {
      "url" : "source",
      "valueString" : "HemOncKB drugs.csv CanMED_major_class, snapshot 2026-03-12"
    }],
    "url" : "http://hl7.org/fhir/StructureDefinition/medication-classification"
  }],
  "identifier" : [{
    "use" : "official",
    "system" : "http://hemonc.org/cui",
    "value" : "88"
  }],
  "code" : {
    "coding" : [{
      "system" : "http://hemonc.org/fhir/CodeSystem/hemonc",
      "version" : "2026-03-12",
      "code" : "88",
      "display" : "Carboplatin"
    },
    {
      "system" : "http://www.nlm.nih.gov/research/umls/rxnorm",
      "code" : "40048",
      "display" : "carboplatin"
    },
    {
      "system" : "http://fdasis.nlm.nih.gov",
      "code" : "BG3F62OND5",
      "display" : "CARBOPLATIN"
    },
    {
      "system" : "https://spor.ema.europa.eu/v2/substances",
      "code" : "100000092564",
      "display" : "Carboplatin"
    },
    {
      "system" : "http://www.whocc.no/atc",
      "version" : "2025",
      "code" : "L01XA02",
      "display" : "carboplatin"
    },
    {
      "system" : "http://fhir.de/CodeSystem/bfarm/atc",
      "version" : "2026",
      "code" : "L01XA02",
      "display" : "Carboplatin"
    },
    {
      "system" : "http://fhir.de/CodeSystem/ask",
      "version" : "20260105",
      "code" : "23168",
      "display" : "Carboplatin"
    }],
    "text" : "Carboplatin"
  },
  "status" : "active"
}

```
