# SRL regimen id → HemOnc variant CUI (example, colorectal mFOLFOX6) - European SACT Regimen Catalog — Executable Knowledge Layer for Systemic Anti-Cancer Therapy Regimens v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SRL regimen id → HemOnc variant CUI (example, colorectal mFOLFOX6)**

## ConceptMap: SRL regimen id → HemOnc variant CUI (example, colorectal mFOLFOX6) (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://hemonc.org/fhir/ConceptMap/srl-to-hemonc-variant | *Version*:2026-03-12-0.1.0 |
| Draft as of 2026-10-24 | *Computable Name*:SRLToHemOncVariant |

 
Bridge ConceptMap from NZ SACT Regimen Library entries to the HemOnc variant each is based on. equivalent = dose-for-dose match; relatedto = derived with a documented modification. Not a redistribution of SRL content. 



## Resource Content

```json
{
  "resourceType" : "ConceptMap",
  "id" : "srl-to-hemonc-variant",
  "url" : "http://hemonc.org/fhir/ConceptMap/srl-to-hemonc-variant",
  "version" : "2026-03-12-0.1.0",
  "name" : "SRLToHemOncVariant",
  "title" : "SRL regimen id → HemOnc variant CUI (example, colorectal mFOLFOX6)",
  "status" : "draft",
  "experimental" : true,
  "date" : "2026-10-24",
  "publisher" : "European SACT Regimen Catalog Working Group",
  "contact" : [{
    "name" : "European SACT Regimen Catalog Working Group",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/thome/oncology-regimens"
    }]
  }],
  "description" : "Bridge ConceptMap from NZ SACT Regimen Library entries to the HemOnc variant each is based on. equivalent = dose-for-dose match; relatedto = derived with a documented modification. Not a redistribution of SRL content.",
  "jurisdiction" : [{
    "coding" : [{
      "system" : "urn:iso:std:iso:3166",
      "code" : "DE",
      "display" : "Germany"
    }]
  }],
  "group" : [{
    "source" : "https://srl.org.nz/regimens",
    "target" : "http://hemonc.org/fhir/CodeSystem/hemonc",
    "element" : [{
      "code" : "52101000210105",
      "display" : "CRC Metastatic – mFOLFOX6 [bolus and infusion] [high dose folinic acid] v2.0.2",
      "target" : [{
        "code" : "133145",
        "display" : "mFOLFOX6 Variant #06",
        "equivalence" : "equivalent",
        "comment" : "Oxaliplatin 85/2h, folinic acid 400/2h, 5-FU 400 bolus + 2400/46h, q14d. Infusion durations match."
      }]
    },
    {
      "code" : "588251000210108",
      "display" : "CRC Metastatic – mFOLFOX6 [high dose folinic acid] (no bolus) v1.0.0",
      "target" : [{
        "code" : "133145",
        "display" : "mFOLFOX6 Variant #06",
        "equivalence" : "relatedto",
        "comment" : "omit-action: fluorouracil 400 mg/m² bolus. No HemOnc variant drops the bolus at otherwise identical doses."
      }]
    },
    {
      "code" : "52201000210102",
      "display" : "CRC Adjuvant – mFOLFOX6 [low dose folinic acid] v2.0.0",
      "target" : [{
        "code" : "133145",
        "display" : "mFOLFOX6 Variant #06",
        "equivalence" : "relatedto",
        "comment" : "replace-dose: folinic acid 400 mg/m² IV 2 h → 50 mg flat IV 2 min. Lowest HemOnc leucovorin dose for mFOLFOX6 is 200 mg/m²."
      }]
    }]
  }]
}

```
