# Paclitaxel 175 mg/m² IV over 3 h, day 1, q21d - HemOnc FHIR Regimen Catalog — Executable Knowledge Layer for Oncology Protocols v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Paclitaxel 175 mg/m² IV over 3 h, day 1, q21d**

## ActivityDefinition: Paclitaxel 175 mg/m² IV over 3 h, day 1, q21d (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://hemonc.org/fhir/ActivityDefinition/sig-paclitaxel-175mgm2-d1-q21d | *Version*:2026-03-12-0.1.0 |
| Active as of 2026-03-12 | *Computable Name*:PaclitaxelD1Q21D |
| *Other Identifiers:*http://hemonc.org/cui#regimen-2554+variant-144842+component-379 (use: official) | |
| **Usage:**Clinical Focus: Paclitaxel | |

 
One sig from HemOnc Regimen 2554 ('Carboplatin and Paclitaxel (CP)') Variant #83 (cui 144842). Paclitaxel as primary systemic component, 175 mg/m² IV over 3 hours, administered on day 1 of a 21-day cycle, for 3–6 cycles. Declared dose is per-m²; the dynamicValue invokes the HemOnc dose helper Library to compute the patient-specific mg at $apply time. 

**Exception generating Narrative: Error @1, 17: Premature ExpressionNode termination at unexpected token "=="**



## Resource Content

```json
{
  "resourceType" : "ActivityDefinition",
  "id" : "sig-paclitaxel-175mgm2-d1-q21d",
  "url" : "http://hemonc.org/fhir/ActivityDefinition/sig-paclitaxel-175mgm2-d1-q21d",
  "identifier" : [{
    "use" : "official",
    "system" : "http://hemonc.org/cui",
    "value" : "regimen-2554+variant-144842+component-379"
  }],
  "version" : "2026-03-12-0.1.0",
  "name" : "PaclitaxelD1Q21D",
  "title" : "Paclitaxel 175 mg/m² IV over 3 h, day 1, q21d",
  "status" : "active",
  "experimental" : true,
  "date" : "2026-03-12",
  "publisher" : "HemOnc FHIR Catalog Working Group",
  "contact" : [{
    "name" : "HemOnc FHIR Catalog Working Group",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/thome/oncology-regimens"
    }]
  }],
  "description" : "One sig from HemOnc Regimen 2554 ('Carboplatin and Paclitaxel (CP)') Variant #83 (cui 144842). Paclitaxel as primary systemic component, 175 mg/m² IV over 3 hours, administered on day 1 of a 21-day cycle, for 3–6 cycles. Declared dose is per-m²; the dynamicValue invokes the HemOnc dose helper Library to compute the patient-specific mg at $apply time.",
  "useContext" : [{
    "code" : {
      "system" : "http://terminology.hl7.org/CodeSystem/usage-context-type",
      "code" : "focus"
    },
    "valueCodeableConcept" : {
      "coding" : [{
        "system" : "http://hemonc.org/fhir/CodeSystem/hemonc",
        "code" : "379",
        "display" : "Paclitaxel"
      }]
    }
  }],
  "jurisdiction" : [{
    "coding" : [{
      "system" : "urn:iso:std:iso:3166",
      "code" : "DE",
      "display" : "Germany"
    }]
  }],
  "relatedArtifact" : [{
    "type" : "derived-from",
    "label" : "HemOncKB sigs.csv row, snapshot 2026-03-12",
    "citation" : "HemOnc Dataverse v2.1 (2026-03-12). regimen_cui=2554, variant_cui=144842, component_cui=379.",
    "url" : "https://dataverse.harvard.edu/dataverse/hemonc",
    "document" : {
      "url" : "https://dataverse.harvard.edu/dataverse/hemonc"
    }
  }],
  "library" : ["http://hemonc.org/fhir/Library/HemOncDoseHelpers"],
  "kind" : "MedicationRequest",
  "productReference" : {
    "reference" : "MedicationKnowledge/hemonc-drug-379-paclitaxel"
  },
  "dosage" : [{
    "extension" : [{
      "url" : "http://hemonc.org/fhir/StructureDefinition/day-of-cycle",
      "valueInteger" : 1
    }],
    "text" : "Paclitaxel 175 mg/m² IV over 3 hours on day 1 of a 21-day cycle",
    "patientInstruction" : "Premedications (corticosteroid + H1 + H2) required 30 min prior — see linked dose-modification policy.",
    "timing" : {
      "repeat" : {
        "boundsRange" : {
          "low" : {
            "value" : 3,
            "unit" : "1",
            "system" : "http://unitsofmeasure.org"
          },
          "high" : {
            "value" : 6,
            "unit" : "1",
            "system" : "http://unitsofmeasure.org"
          }
        },
        "duration" : 3,
        "durationUnit" : "h",
        "frequency" : 1,
        "period" : 21,
        "periodUnit" : "d"
      }
    },
    "route" : {
      "coding" : [{
        "system" : "http://snomed.info/sct",
        "code" : "47625008",
        "display" : "Intravenous route"
      }]
    },
    "doseAndRate" : [{
      "type" : {
        "coding" : [{
          "system" : "http://hemonc.org/fhir/CodeSystem/sig-target-type",
          "code" : "target-mg-per-m2"
        }]
      },
      "doseQuantity" : {
        "value" : 175,
        "unit" : "mg/m2",
        "system" : "http://unitsofmeasure.org",
        "code" : "mg/m2"
      }
    }]
  }],
  "dynamicValue" : [{
    "path" : "dosageInstruction[0].doseAndRate[0].doseQuantity.value",
    "expression" : {
      "language" : "text/fhirpath",
      "expression" : "175 * 1.85"
    }
  },
  {
    "path" : "dosageInstruction[0].doseAndRate[0].doseQuantity.unit",
    "expression" : {
      "language" : "text/fhirpath",
      "expression" : "'mg'"
    }
  },
  {
    "path" : "dosageInstruction[0].doseAndRate[0].doseQuantity.system",
    "expression" : {
      "language" : "text/fhirpath",
      "expression" : "'http://unitsofmeasure.org'"
    }
  },
  {
    "path" : "dosageInstruction[0].doseAndRate[0].doseQuantity.code",
    "expression" : {
      "language" : "text/fhirpath",
      "expression" : "'mg'"
    }
  },
  {
    "path" : "dosageInstruction[0].doseAndRate[0].type",
    "expression" : {
      "language" : "text/cql.identifier",
      "expression" : "DoseAndRateTypePaclitaxel"
    }
  }]
}

```
