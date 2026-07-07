# Carboplatin AUC 5 IV over 30–60 min, day 1, q21d - HemOnc FHIR Regimen Catalog — Executable Knowledge Layer for Oncology Protocols v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Carboplatin AUC 5 IV over 30–60 min, day 1, q21d**

## ActivityDefinition: Carboplatin AUC 5 IV over 30–60 min, day 1, q21d (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://hemonc.org/fhir/ActivityDefinition/sig-carboplatin-auc5-d1-q21d | *Version*:2026-03-12-0.1.0 |
| Active as of 2026-03-12 | *Computable Name*:CarboplatinAUC5D1Q21D |
| *Other Identifiers:*http://hemonc.org/cui#regimen-2554+variant-144842+component-88 (use: official, ) | |
| **Usage:**Clinical Focus: Carboplatin | |

 
One sig from HemOnc Regimen 2554 ('Carboplatin and Paclitaxel (CP)') Variant #83 (cui 144842). Carboplatin as primary systemic component, target AUC 5 IV over 30–60 minutes, day 1 of a 21-day cycle, for 3–6 cycles. The declared dose is a target AUC; the dynamicValue invokes the Calvert helper to compute the mg at $apply time using the patient's GFR. 

**Exception generating Narrative: Error @1, 17: Premature ExpressionNode termination at unexpected token "=="**



## Resource Content

```json
{
  "resourceType" : "ActivityDefinition",
  "id" : "sig-carboplatin-auc5-d1-q21d",
  "url" : "http://hemonc.org/fhir/ActivityDefinition/sig-carboplatin-auc5-d1-q21d",
  "identifier" : [{
    "use" : "official",
    "system" : "http://hemonc.org/cui",
    "value" : "regimen-2554+variant-144842+component-88"
  }],
  "version" : "2026-03-12-0.1.0",
  "name" : "CarboplatinAUC5D1Q21D",
  "title" : "Carboplatin AUC 5 IV over 30–60 min, day 1, q21d",
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
  "description" : "One sig from HemOnc Regimen 2554 ('Carboplatin and Paclitaxel (CP)') Variant #83 (cui 144842). Carboplatin as primary systemic component, target AUC 5 IV over 30–60 minutes, day 1 of a 21-day cycle, for 3–6 cycles. The declared dose is a target AUC; the dynamicValue invokes the Calvert helper to compute the mg at $apply time using the patient's GFR.",
  "useContext" : [{
    "code" : {
      "system" : "http://terminology.hl7.org/CodeSystem/usage-context-type",
      "code" : "focus"
    },
    "valueCodeableConcept" : {
      "coding" : [{
        "system" : "http://hemonc.org/fhir/CodeSystem/hemonc",
        "code" : "88",
        "display" : "Carboplatin"
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
    "citation" : "HemOnc Dataverse v2.1 (2026-03-12). regimen_cui=2554, variant_cui=144842, component_cui=88.",
    "url" : "https://dataverse.harvard.edu/dataverse/hemonc",
    "document" : {
      "url" : "https://dataverse.harvard.edu/dataverse/hemonc"
    }
  },
  {
    "type" : "documentation",
    "label" : "Calvert et al. 1989, J Clin Oncol 7(11):1748-1756",
    "citation" : "Calvert AH, Newell DR, Gumbrell LA, et al. Carboplatin dosage: prospective evaluation of a simple formula based on renal function. J Clin Oncol. 1989;7(11):1748-56."
  }],
  "library" : ["http://hemonc.org/fhir/Library/HemOncDoseHelpers"],
  "kind" : "MedicationRequest",
  "productReference" : {
    "reference" : "MedicationKnowledge/hemonc-drug-88-carboplatin"
  },
  "dosage" : [{
    "extension" : [{
      "url" : "http://hemonc.org/fhir/StructureDefinition/day-of-cycle",
      "valueInteger" : 1
    }],
    "sequence" : 1,
    "text" : "Carboplatin AUC 5 IV over 30–60 minutes on day 1 of a 21-day cycle",
    "patientInstruction" : "Dose target is exposure (AUC), not milligrams. Computed mg = 5 × (effective GFR + 25) at $apply time. GFR formula and cap are institution policy.",
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
        "duration" : 30,
        "durationMax" : 60,
        "durationUnit" : "min",
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
          "code" : "target-AUC"
        }]
      },
      "doseQuantity" : {
        "value" : 5,
        "unit" : "AUC",
        "system" : "http://hemonc.org/fhir/CodeSystem/hemonc",
        "code" : "134425"
      }
    }]
  }],
  "dynamicValue" : [{
    "path" : "dosageInstruction[0].doseAndRate[0].doseQuantity.value",
    "expression" : {
      "description" : "Calvert: targetAUC × (effectiveGFR + 25). Phase 0 hardcodes targetAUC=5, GFR=100; production replaces with patient-derived GFR.",
      "language" : "text/fhirpath",
      "expression" : "5 * (100.0 + 25)"
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
      "expression" : "DoseAndRateTypeCarboplatin"
    }
  }]
}

```
