# Day of Cycle - European SACT Regimen Catalog — Executable Knowledge Layer for Systemic Anti-Cancer Therapy Regimens v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Day of Cycle**

## Extension: Day of Cycle (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://hemonc.org/fhir/StructureDefinition/day-of-cycle | *Version*:2026-03-12-0.1.0 |
| Draft as of 2026-11-12 | *Computable Name*:DayOfCycle |

Day within a treatment cycle on which a sig or a plan action is given. Day 1 is the first day of the cycle.

**Context of Use**

**Usage info**

**Usages:**

* Examples for this Extension: [CarboplatinAUC5D1Q21D](ActivityDefinition-sig-carboplatin-auc5-d1-q21d.md), [PaclitaxelD1Q21D](ActivityDefinition-sig-paclitaxel-175mgm2-d1-q21d.md) and [CarboplatinPaclitaxelVariant83](PlanDefinition-regimen-2554-variant-144842.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/hemonc-fhir-regimen-catalog|current/StructureDefinition/StructureDefinition-day-of-cycle.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-day-of-cycle.csv), [Excel](StructureDefinition-day-of-cycle.xlsx), [Schematron](StructureDefinition-day-of-cycle.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "day-of-cycle",
  "url" : "http://hemonc.org/fhir/StructureDefinition/day-of-cycle",
  "version" : "2026-03-12-0.1.0",
  "name" : "DayOfCycle",
  "title" : "Day of Cycle",
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
  "description" : "Day within a treatment cycle on which a sig or a plan action is given. Day 1 is the first day of the cycle.",
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
    "expression" : "Dosage"
  },
  {
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
      "short" : "Day of Cycle",
      "definition" : "Day within a treatment cycle on which a sig or a plan action is given. Day 1 is the first day of the cycle."
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://hemonc.org/fhir/StructureDefinition/day-of-cycle"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "min" : 1,
      "type" : [{
        "code" : "integer"
      }]
    }]
  }
}

```
