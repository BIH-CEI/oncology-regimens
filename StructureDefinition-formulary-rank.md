# Formulary Rank - European SACT Regimen Catalog — Executable Knowledge Layer for Systemic Anti-Cancer Therapy Regimens v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Formulary Rank**

## Extension: Formulary Rank (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://hemonc.org/fhir/StructureDefinition/formulary-rank | *Version*:2026-03-12-0.1.0 |
| Draft as of 2026-11-12 | *Computable Name*:FormularyRank |

Optional rank of an entry within a formulary PlanDefinition. 1 = first choice. Absence means unranked.

**Context of Use**

**Usage info**

**Usages:**

* Examples for this Extension: [NZColorectalMFOLFOX6Formulary](PlanDefinition-nz-crc-mfolfox6-formulary.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/hemonc-fhir-regimen-catalog|current/StructureDefinition/StructureDefinition-formulary-rank.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-formulary-rank.csv), [Excel](StructureDefinition-formulary-rank.xlsx), [Schematron](StructureDefinition-formulary-rank.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "formulary-rank",
  "url" : "http://hemonc.org/fhir/StructureDefinition/formulary-rank",
  "version" : "2026-03-12-0.1.0",
  "name" : "FormularyRank",
  "title" : "Formulary Rank",
  "status" : "draft",
  "experimental" : true,
  "date" : "2026-11-12T18:44:05+00:00",
  "publisher" : "European SACT Regimen Catalog Working Group",
  "contact" : [{
    "name" : "European SACT Regimen Catalog Working Group",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/thome/oncology-regimens"
    }]
  }],
  "description" : "Optional rank of an entry within a formulary PlanDefinition. 1 = first choice. Absence means unranked.",
  "jurisdiction" : [{
    "coding" : [{
      "system" : "urn:iso:std:iso:3166",
      "code" : "DE",
      "display" : "Germany"
    }]
  }],
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  }],
  "kind" : "complex-type",
  "abstract" : false,
  "context" : [{
    "type" : "element",
    "expression" : "PlanDefinition.action"
  }],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Extension",
      "path" : "Extension",
      "short" : "Formulary Rank",
      "definition" : "Optional rank of an entry within a formulary PlanDefinition. 1 = first choice. Absence means unranked."
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://hemonc.org/fhir/StructureDefinition/formulary-rank"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "type" : [{
        "code" : "positiveInt"
      }]
    }]
  }
}

```
