# Formulary Parameter - European SACT Regimen Catalog — Executable Knowledge Layer for Systemic Anti-Cancer Therapy Regimens v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Formulary Parameter**

## Extension: Formulary Parameter (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://hemonc.org/fhir/StructureDefinition/formulary-parameter | *Version*:2026-03-12-0.1.0 |
| Draft as of 2026-11-12 | *Computable Name*:FormularyParameter |

A parameter value a formulary entry pins on the referenced (parameterised) variant PlanDefinition. Forwarded by the CDS layer in the nested `parameters` of $apply.

**Context of Use**

**Usage info**

**Usages:**

* Examples for this Extension: [NZColorectalMFOLFOX6Formulary](PlanDefinition-nz-crc-mfolfox6-formulary.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/hemonc-fhir-regimen-catalog|current/StructureDefinition/StructureDefinition-formulary-parameter.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-formulary-parameter.csv), [Excel](StructureDefinition-formulary-parameter.xlsx), [Schematron](StructureDefinition-formulary-parameter.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "formulary-parameter",
  "url" : "http://hemonc.org/fhir/StructureDefinition/formulary-parameter",
  "version" : "2026-03-12-0.1.0",
  "name" : "FormularyParameter",
  "title" : "Formulary Parameter",
  "status" : "draft",
  "experimental" : true,
  "date" : "2026-11-12T17:59:01+00:00",
  "publisher" : "European SACT Regimen Catalog Working Group",
  "contact" : [{
    "name" : "European SACT Regimen Catalog Working Group",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/thome/oncology-regimens"
    }]
  }],
  "description" : "A parameter value a formulary entry pins on the referenced (parameterised) variant PlanDefinition. Forwarded by the CDS layer in the nested `parameters` of $apply.",
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
      "short" : "Formulary Parameter",
      "definition" : "A parameter value a formulary entry pins on the referenced (parameterised) variant PlanDefinition. Forwarded by the CDS layer in the nested `parameters` of $apply."
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "min" : 2
    },
    {
      "id" : "Extension.extension:name",
      "path" : "Extension.extension",
      "sliceName" : "name",
      "short" : "CQL parameter name declared by the variant's Library",
      "min" : 1,
      "max" : "1"
    },
    {
      "id" : "Extension.extension:name.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:name.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "name"
    },
    {
      "id" : "Extension.extension:name.value[x]",
      "path" : "Extension.extension.value[x]",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:value",
      "path" : "Extension.extension",
      "sliceName" : "value",
      "min" : 1,
      "max" : "1"
    },
    {
      "id" : "Extension.extension:value.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:value.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "value"
    },
    {
      "id" : "Extension.extension:value.value[x]",
      "path" : "Extension.extension.value[x]",
      "type" : [{
        "code" : "boolean"
      },
      {
        "code" : "decimal"
      },
      {
        "code" : "integer"
      },
      {
        "code" : "string"
      },
      {
        "code" : "CodeableConcept"
      },
      {
        "code" : "Quantity"
      }]
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://hemonc.org/fhir/StructureDefinition/formulary-parameter"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "max" : "0"
    }]
  }
}

```
