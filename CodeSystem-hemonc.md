# HemOnc Ontology (fragment, Phase 0 spike) - European SACT Regimen Catalog — Executable Knowledge Layer for Systemic Anti-Cancer Therapy Regimens v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **HemOnc Ontology (fragment, Phase 0 spike)**

## CodeSystem: HemOnc Ontology (fragment, Phase 0 spike) (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://hemonc.org/fhir/CodeSystem/hemonc | *Version*:2026-03-12-0.1.0 |
| Active as of 2026-03-12 | *Computable Name*:HemOnc |
| *Other Identifiers:*https://dataverse.harvard.edu/dataset.xhtml#HemOncKB | |
| **Copyright/Legal**: © HemOnc.org. Distributed under CC BY 4.0. | |

 
Fragment of the HemOnc ontology, sufficient to support the Carboplatin + Paclitaxel Variant #83 example used in the Phase 0 spike, plus the mFOLFOX6 concepts referenced by the Selection Layer example. The full CodeSystem will be emitted as content=complete from the OMOP concept_stage table in a later phase. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [NZ colorectal permitted mFOLFOX6 variants (example)](ValueSet-nz-crc-permitted-variants.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "hemonc",
  "url" : "http://hemonc.org/fhir/CodeSystem/hemonc",
  "identifier" : [{
    "system" : "https://dataverse.harvard.edu/dataset.xhtml",
    "value" : "HemOncKB"
  }],
  "version" : "2026-03-12-0.1.0",
  "name" : "HemOnc",
  "title" : "HemOnc Ontology (fragment, Phase 0 spike)",
  "status" : "active",
  "experimental" : true,
  "date" : "2026-03-12",
  "publisher" : "European SACT Regimen Catalog Working Group",
  "contact" : [{
    "name" : "European SACT Regimen Catalog Working Group",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/thome/oncology-regimens"
    }]
  }],
  "description" : "Fragment of the HemOnc ontology, sufficient to support the Carboplatin + Paclitaxel Variant #83 example used in the Phase 0 spike, plus the mFOLFOX6 concepts referenced by the Selection Layer example. The full CodeSystem will be emitted as content=complete from the OMOP concept_stage table in a later phase.",
  "jurisdiction" : [{
    "coding" : [{
      "system" : "urn:iso:std:iso:3166",
      "code" : "DE",
      "display" : "Germany"
    }]
  }],
  "copyright" : "© HemOnc.org. Distributed under CC BY 4.0.",
  "caseSensitive" : true,
  "content" : "fragment",
  "property" : [{
    "code" : "concept-class-id",
    "description" : "HemOnc concept_class_id (e.g. Component, Regimen, Regimen Variant, Unit, Route, Frequency)",
    "type" : "string"
  },
  {
    "code" : "atc",
    "description" : "WHO ATC code",
    "type" : "string"
  },
  {
    "code" : "rxnorm",
    "description" : "RxNorm IN code (preferred mapping per HemOnc rxnorm_map)",
    "type" : "string"
  },
  {
    "code" : "inn",
    "description" : "International Nonproprietary Name",
    "type" : "string"
  }],
  "concept" : [{
    "code" : "88",
    "display" : "Carboplatin",
    "property" : [{
      "code" : "concept-class-id",
      "valueString" : "Component"
    },
    {
      "code" : "atc",
      "valueString" : "L01XA02"
    },
    {
      "code" : "rxnorm",
      "valueString" : "40048"
    },
    {
      "code" : "inn",
      "valueString" : "carboplatin"
    }]
  },
  {
    "code" : "379",
    "display" : "Paclitaxel",
    "property" : [{
      "code" : "concept-class-id",
      "valueString" : "Component"
    },
    {
      "code" : "atc",
      "valueString" : "L01CD01"
    },
    {
      "code" : "rxnorm",
      "valueString" : "56946"
    },
    {
      "code" : "inn",
      "valueString" : "paclitaxel"
    }]
  },
  {
    "code" : "2554",
    "display" : "Carboplatin and Paclitaxel (CP)",
    "property" : [{
      "code" : "concept-class-id",
      "valueString" : "Regimen"
    }]
  },
  {
    "code" : "144842",
    "display" : "Variant #83",
    "property" : [{
      "code" : "concept-class-id",
      "valueString" : "Regimen Variant"
    }]
  },
  {
    "code" : "134425",
    "display" : "AUC",
    "property" : [{
      "code" : "concept-class-id",
      "valueString" : "Unit"
    }]
  },
  {
    "code" : "134448",
    "display" : "mg/m^2",
    "property" : [{
      "code" : "concept-class-id",
      "valueString" : "Unit"
    }]
  },
  {
    "code" : "134430",
    "display" : "hour",
    "property" : [{
      "code" : "concept-class-id",
      "valueString" : "Unit"
    }]
  },
  {
    "code" : "134451",
    "display" : "minute",
    "property" : [{
      "code" : "concept-class-id",
      "valueString" : "Unit"
    }]
  },
  {
    "code" : "44957",
    "display" : "IV",
    "property" : [{
      "code" : "concept-class-id",
      "valueString" : "Route"
    }]
  },
  {
    "code" : "139563",
    "display" : "once",
    "property" : [{
      "code" : "concept-class-id",
      "valueString" : "Frequency"
    }]
  },
  {
    "code" : "13849",
    "display" : "mFOLFOX6",
    "property" : [{
      "code" : "concept-class-id",
      "valueString" : "Regimen"
    }]
  },
  {
    "code" : "133145",
    "display" : "mFOLFOX6 Variant #06",
    "property" : [{
      "code" : "concept-class-id",
      "valueString" : "Regimen Variant"
    }]
  },
  {
    "code" : "133143",
    "display" : "mFOLFOX6 Variant #04",
    "property" : [{
      "code" : "concept-class-id",
      "valueString" : "Regimen Variant"
    }]
  }]
}

```
