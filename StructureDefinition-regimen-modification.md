# Regimen Modification - HemOnc FHIR Regimen Catalog — Executable Knowledge Layer for Oncology Protocols v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Regimen Modification**

## Extension: Regimen Modification (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://hemonc.org/fhir/StructureDefinition/regimen-modification | *Version*:2026-03-12-0.1.0 |
| Draft as of 2026-10-24 | *Computable Name*:RegimenModification |

One delta between a derived (L2) PlanDefinition and the HemOnc variant it is derived from. Provenance only: the derived PlanDefinition SHALL be complete on its own (Rule D-1).

**Context of Use**

**Usage info**

**Usages:**

* Examples for this Extension: [SRLmFOLFOX6HighFANoBolus](PlanDefinition-srl-588251000210108-mfolfox6-nobolus.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/hemonc-fhir-regimen-catalog|current/StructureDefinition/StructureDefinition-regimen-modification.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-regimen-modification.csv), [Excel](StructureDefinition-regimen-modification.xlsx), [Schematron](StructureDefinition-regimen-modification.sch) 

#### Terminology Bindings

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "regimen-modification",
  "url" : "http://hemonc.org/fhir/StructureDefinition/regimen-modification",
  "version" : "2026-03-12-0.1.0",
  "name" : "RegimenModification",
  "title" : "Regimen Modification",
  "status" : "draft",
  "experimental" : true,
  "date" : "2026-10-24T21:02:11+00:00",
  "publisher" : "HemOnc FHIR Catalog Working Group",
  "contact" : [{
    "name" : "HemOnc FHIR Catalog Working Group",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/thome/oncology-regimens"
    }]
  }],
  "description" : "One delta between a derived (L2) PlanDefinition and the HemOnc variant it is derived from. Provenance only: the derived PlanDefinition SHALL be complete on its own (Rule D-1).",
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
    "expression" : "PlanDefinition"
  }],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Extension",
      "path" : "Extension",
      "short" : "Regimen Modification",
      "definition" : "One delta between a derived (L2) PlanDefinition and the HemOnc variant it is derived from. Provenance only: the derived PlanDefinition SHALL be complete on its own (Rule D-1)."
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "min" : 1
    },
    {
      "id" : "Extension.extension:kind",
      "path" : "Extension.extension",
      "sliceName" : "kind",
      "short" : "omit-action | add-action | replace-dose | replace-schedule | replace-route | replace-product",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:kind.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:kind.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "kind"
    },
    {
      "id" : "Extension.extension:kind.value[x]",
      "path" : "Extension.extension.value[x]",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://hemonc.org/fhir/ValueSet/regimen-modification-kind-vs"
      }
    },
    {
      "id" : "Extension.extension:targetActionId",
      "path" : "Extension.extension",
      "sliceName" : "targetActionId",
      "short" : "action.id in the parent PlanDefinition that is omitted or replaced",
      "min" : 0,
      "max" : "1"
    },
    {
      "id" : "Extension.extension:targetActionId.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:targetActionId.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "targetActionId"
    },
    {
      "id" : "Extension.extension:targetActionId.value[x]",
      "path" : "Extension.extension.value[x]",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:component",
      "path" : "Extension.extension",
      "sliceName" : "component",
      "short" : "Drug concerned (HemOnc component CUI, plus ATC/RxNorm where available)",
      "min" : 0,
      "max" : "1"
    },
    {
      "id" : "Extension.extension:component.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:component.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "component"
    },
    {
      "id" : "Extension.extension:component.value[x]",
      "path" : "Extension.extension.value[x]",
      "type" : [{
        "code" : "CodeableConcept"
      }]
    },
    {
      "id" : "Extension.extension:from",
      "path" : "Extension.extension",
      "sliceName" : "from",
      "short" : "Parent value, human-readable",
      "min" : 0,
      "max" : "1"
    },
    {
      "id" : "Extension.extension:from.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:from.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "from"
    },
    {
      "id" : "Extension.extension:from.value[x]",
      "path" : "Extension.extension.value[x]",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:to",
      "path" : "Extension.extension",
      "sliceName" : "to",
      "short" : "New value, human-readable; absent for omit-action",
      "min" : 0,
      "max" : "1"
    },
    {
      "id" : "Extension.extension:to.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:to.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "to"
    },
    {
      "id" : "Extension.extension:to.value[x]",
      "path" : "Extension.extension.value[x]",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:rationale",
      "path" : "Extension.extension",
      "sliceName" : "rationale",
      "short" : "Why, in the issuing body's words",
      "min" : 0,
      "max" : "1"
    },
    {
      "id" : "Extension.extension:rationale.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:rationale.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "rationale"
    },
    {
      "id" : "Extension.extension:rationale.value[x]",
      "path" : "Extension.extension.value[x]",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://hemonc.org/fhir/StructureDefinition/regimen-modification"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "max" : "0"
    }]
  }
}

```
