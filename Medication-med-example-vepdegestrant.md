# Vepdegestrant - European SACT Regimen Catalog — Executable Knowledge Layer for Systemic Anti-Cancer Therapy Regimens v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Vepdegestrant**

## Example Medication: Vepdegestrant

**Artifact URL**: [http://hemonc.org/fhir/Medication/med-example-vepdegestrant](https://simplifier.net/resolve?scope=de.medizininformatikinitiative.kerndatensatz.onkologie@2026.0.3&canonical=http://hemonc.org/fhir/Medication/med-example-vepdegestrant)

**ArtifactVersion**: 2026-03-12

**ArtifactName**: Vepdegestrant

**Artifact Publisher**: HemOnc.org

**Medication Type**: Investigational medicinal product (IMP)

> **Medication Classification**
* type: HemOnc main class
* classification: Proteolysis-targeting chimera estrogen receptor degrader
* source: HemOncKB drugs.csv main_class, snapshot 2026-03-12

**identifier**: `http://hemonc.org/cui`/161163 (use: official)

**code**: Vepdegestrant

**status**: Active



## Resource Content

```json
{
  "resourceType" : "Medication",
  "id" : "med-example-vepdegestrant",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/artifact-url",
    "valueUri" : "http://hemonc.org/fhir/Medication/med-example-vepdegestrant"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/artifact-version",
    "valueString" : "2026-03-12"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/artifact-name",
    "valueString" : "Vepdegestrant"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/artifact-publisher",
    "valueString" : "HemOnc.org"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/medication-type",
    "valueCodeableConcept" : {
      "text" : "Investigational medicinal product (IMP)"
    }
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
        "text" : "HemOnc main class"
      }
    },
    {
      "url" : "classification",
      "valueCodeableConcept" : {
        "text" : "Proteolysis-targeting chimera estrogen receptor degrader"
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
    "value" : "161163"
  }],
  "code" : {
    "coding" : [{
      "system" : "http://hemonc.org/fhir/CodeSystem/hemonc",
      "version" : "2026-03-12",
      "code" : "161163",
      "display" : "Vepdegestrant"
    },
    {
      "system" : "http://fdasis.nlm.nih.gov",
      "code" : "WC1U3R1YMI",
      "display" : "VEPDEGESTRANT"
    },
    {
      "system" : "https://spor.ema.europa.eu/v2/substances",
      "code" : "300000041131",
      "display" : "Vepdegestrant"
    }],
    "text" : "Vepdegestrant"
  },
  "status" : "active"
}

```
