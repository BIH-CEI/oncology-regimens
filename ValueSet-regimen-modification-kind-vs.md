# Regimen Modification Kind ValueSet - European SACT Regimen Catalog — Executable Knowledge Layer for Systemic Anti-Cancer Therapy Regimens v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Regimen Modification Kind ValueSet**

## ValueSet: Regimen Modification Kind ValueSet (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://hemonc.org/fhir/ValueSet/regimen-modification-kind-vs | *Version*:2026-03-12-0.1.0 |
| Draft as of 2026-11-12 | *Computable Name*:RegimenModificationKindVS |

 
All kinds of regimen modification. 

 **References** 

* [Regimen Modification](StructureDefinition-regimen-modification.md)

### Logical Definition (CLD)

 

### Expansion

-------

 Explanation of the columns that may appear on this page: 

| | |
| :--- | :--- |
| Level | A few code lists that FHIR defines are hierarchical - each code is assigned a level. In this scheme, some codes are under other codes, and imply that the code they are under also applies |
| System | The source of the definition of the code (when the value set draws in codes defined elsewhere) |
| Code | The code (used as the code in the resource instance) |
| Display | The display (used in the*display*element of a[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding)). If there is no display, implementers should not simply display the code, but map the concept into their application |
| Definition | An explanation of the meaning of the concept |
| Comments | Additional notes about how to use the code |



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "regimen-modification-kind-vs",
  "url" : "http://hemonc.org/fhir/ValueSet/regimen-modification-kind-vs",
  "version" : "2026-03-12-0.1.0",
  "name" : "RegimenModificationKindVS",
  "title" : "Regimen Modification Kind ValueSet",
  "status" : "draft",
  "experimental" : true,
  "date" : "2026-11-12T19:05:05+00:00",
  "publisher" : "European SACT Regimen Catalog Working Group",
  "contact" : [{
    "name" : "European SACT Regimen Catalog Working Group",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/thome/oncology-regimens"
    }]
  }],
  "description" : "All kinds of regimen modification.",
  "jurisdiction" : [{
    "coding" : [{
      "system" : "urn:iso:std:iso:3166",
      "code" : "DE",
      "display" : "Germany"
    }]
  }],
  "compose" : {
    "include" : [{
      "system" : "http://hemonc.org/fhir/CodeSystem/regimen-modification-kind"
    }]
  }
}

```
