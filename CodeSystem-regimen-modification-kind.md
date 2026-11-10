# Regimen Modification Kind - European SACT Regimen Catalog — Executable Knowledge Layer for Systemic Anti-Cancer Therapy Regimens v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Regimen Modification Kind**

## CodeSystem: Regimen Modification Kind (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://hemonc.org/fhir/CodeSystem/regimen-modification-kind | *Version*:2026-03-12-0.1.0 |
| Draft as of 2026-11-10 | *Computable Name*:RegimenModificationKind |

 
Kinds of delta a derived (L2) PlanDefinition applies against its parent HemOnc variant. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Regimen Modification Kind ValueSet](ValueSet-regimen-modification-kind-vs.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "regimen-modification-kind",
  "url" : "http://hemonc.org/fhir/CodeSystem/regimen-modification-kind",
  "version" : "2026-03-12-0.1.0",
  "name" : "RegimenModificationKind",
  "title" : "Regimen Modification Kind",
  "status" : "draft",
  "experimental" : true,
  "date" : "2026-11-10T21:38:12+00:00",
  "publisher" : "European SACT Regimen Catalog Working Group",
  "contact" : [{
    "name" : "European SACT Regimen Catalog Working Group",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/thome/oncology-regimens"
    }]
  }],
  "description" : "Kinds of delta a derived (L2) PlanDefinition applies against its parent HemOnc variant.",
  "jurisdiction" : [{
    "coding" : [{
      "system" : "urn:iso:std:iso:3166",
      "code" : "DE",
      "display" : "Germany"
    }]
  }],
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 6,
  "concept" : [{
    "code" : "omit-action",
    "display" : "Omit action",
    "definition" : "An action present in the parent is removed (e.g. the fluorouracil bolus)."
  },
  {
    "code" : "add-action",
    "display" : "Add action",
    "definition" : "An action absent in the parent is added (e.g. a supportive-care medication)."
  },
  {
    "code" : "replace-dose",
    "display" : "Replace dose",
    "definition" : "Same drug, same schedule, different dose or dose basis (e.g. mg/m² → flat mg)."
  },
  {
    "code" : "replace-schedule",
    "display" : "Replace schedule",
    "definition" : "Same drug and dose, different days, frequency or infusion duration."
  },
  {
    "code" : "replace-route",
    "display" : "Replace route",
    "definition" : "Same drug and dose, different route."
  },
  {
    "code" : "replace-product",
    "display" : "Replace product",
    "definition" : "Different product for the same component (e.g. leucovorin → levoleucovorin)."
  }]
}

```
