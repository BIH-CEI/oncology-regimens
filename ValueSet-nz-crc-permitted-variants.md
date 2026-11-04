# NZ colorectal permitted mFOLFOX6 variants (example) - European SACT Regimen Catalog — Executable Knowledge Layer for Systemic Anti-Cancer Therapy Regimens v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **NZ colorectal permitted mFOLFOX6 variants (example)**

## ValueSet: NZ colorectal permitted mFOLFOX6 variants (example) (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://hemonc.org/fhir/ValueSet/nz-crc-permitted-variants | *Version*:2026-03-12-0.1.0 |
| Draft as of 2026-11-04 | *Computable Name*:NZCRCPermittedVariants |

 
Terminology twin of PlanDefinition/nz-crc-mfolfox6-formulary: the HemOnc variant CUIs and SRL-derived protocol ids a consumer may offer. SHALL stay equivalent to the formulary's definitionCanonical targets (Rule in §6). 

 **References** 

This value set is not used here; it may be used elsewhere (e.g. specifications and/or implementations that use this content)

### Logical Definition (CLD)

 

### Expansion

No Expansion for this valueset (Unknown Code System)

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
  "id" : "nz-crc-permitted-variants",
  "url" : "http://hemonc.org/fhir/ValueSet/nz-crc-permitted-variants",
  "version" : "2026-03-12-0.1.0",
  "name" : "NZCRCPermittedVariants",
  "title" : "NZ colorectal permitted mFOLFOX6 variants (example)",
  "status" : "draft",
  "experimental" : true,
  "date" : "2026-11-04T08:45:26+00:00",
  "publisher" : "European SACT Regimen Catalog Working Group",
  "contact" : [{
    "name" : "European SACT Regimen Catalog Working Group",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/thome/oncology-regimens"
    }]
  }],
  "description" : "Terminology twin of PlanDefinition/nz-crc-mfolfox6-formulary: the HemOnc variant CUIs and SRL-derived protocol ids a consumer may offer. SHALL stay equivalent to the formulary's definitionCanonical targets (Rule in §6).",
  "jurisdiction" : [{
    "coding" : [{
      "system" : "urn:iso:std:iso:3166",
      "code" : "DE",
      "display" : "Germany"
    }]
  }],
  "compose" : {
    "include" : [{
      "system" : "http://hemonc.org/fhir/CodeSystem/hemonc",
      "concept" : [{
        "code" : "133145",
        "display" : "mFOLFOX6 Variant #06"
      }]
    },
    {
      "system" : "https://srl.org.nz/regimens",
      "concept" : [{
        "code" : "588251000210108",
        "display" : "CRC Metastatic – mFOLFOX6 [high dose folinic acid] (no bolus)"
      },
      {
        "code" : "52201000210102",
        "display" : "CRC Adjuvant – mFOLFOX6 [low dose folinic acid]"
      }]
    }]
  }
}

```
