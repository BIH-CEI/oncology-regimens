# HemOnc dose-computation helpers (BSA, Calvert) - HemOnc FHIR Regimen Catalog — Executable Knowledge Layer for Oncology Protocols v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **HemOnc dose-computation helpers (BSA, Calvert)**

## Library: HemOnc dose-computation helpers (BSA, Calvert) (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://hemonc.org/fhir/Library/HemOncDoseHelpers | *Version*:2026-03-12-0.1.0 |
| Active as of 2026-03-12 | *Computable Name*:HemOncDoseHelpers |
| **Usage:**Workflow Task: Treatment | |

 
CQL library providing BSA (Mosteller/Du Bois/Haycock), Cockcroft-Gault GFR, Calvert carboplatin formula, and per-sig dose helpers referenced by ActivityDefinition.dynamicValue. Phase 0 spike — covers paclitaxel and carboplatin only. Institution policy (BSA formula, BSA cap, GFR formula, GFR cap) is set via $apply Parameters. 

* * **Content: **text/cql: ````library HemOncDoseHelpers version '2026-03-12' using FHIR version '4.0.1' include FHIRHelpers version '4.0.1' called FHIRHelpers codesystem "SigTargetType": 'http://hemonc.org/fhir/CodeSystem/sig-target-type' code "ComputedFromTargetAUC": 'computed-from-target-AUC' from "SigTargetType" code "ComputedFromTargetMgPerM2": 'computed-from-target-mg-per-m2' from "SigTargetType" // ----------------------------------------------------------------------------- // Phase 0 status // ----------------------------------------------------------------------------- // The dose-magnitude computations (Mosteller/Du Bois BSA, Cockcroft-Gault, // Calvert) are emitted via FHIRPath dynamicValues in the ActivityDefinition // resources, because cqf-fhir 8.4.0 has a bug coercing CQL System.Quantity // literals into FHIR.SimpleQuantity at dynamicValue assignment time (surfaces // as 'Type org.hl7.fhir.r4.model.DateTimeType is not comparable'). // // This library still owns the *coded* provenance markers — those work fine // via text/cql.identifier and are referenced from // ActivityDefinition.dynamicValue for the doseAndRate[0].type path. // // Once the cqf-fhir bug is fixed (track upstream), the dose-magnitude // expressions move back into this library and gain real BSA/GFR computation // from Patient + Observation context. // ----------------------------------------------------------------------------- context Patient define DoseAndRateTypeCarboplatin: Concept { codes: { "ComputedFromTargetAUC" } } define DoseAndRateTypePaclitaxel: Concept { codes: { "ComputedFromTargetMgPerM2" } } ````: **Id: **
  * ?: HemOncDoseHelpers
* * **Content: **text/cql: ````library HemOncDoseHelpers version '2026-03-12' using FHIR version '4.0.1' include FHIRHelpers version '4.0.1' called FHIRHelpers codesystem "SigTargetType": 'http://hemonc.org/fhir/CodeSystem/sig-target-type' code "ComputedFromTargetAUC": 'computed-from-target-AUC' from "SigTargetType" code "ComputedFromTargetMgPerM2": 'computed-from-target-mg-per-m2' from "SigTargetType" // ----------------------------------------------------------------------------- // Phase 0 status // ----------------------------------------------------------------------------- // The dose-magnitude computations (Mosteller/Du Bois BSA, Cockcroft-Gault, // Calvert) are emitted via FHIRPath dynamicValues in the ActivityDefinition // resources, because cqf-fhir 8.4.0 has a bug coercing CQL System.Quantity // literals into FHIR.SimpleQuantity at dynamicValue assignment time (surfaces // as 'Type org.hl7.fhir.r4.model.DateTimeType is not comparable'). // // This library still owns the *coded* provenance markers — those work fine // via text/cql.identifier and are referenced from // ActivityDefinition.dynamicValue for the doseAndRate[0].type path. // // Once the cqf-fhir bug is fixed (track upstream), the dose-magnitude // expressions move back into this library and gain real BSA/GFR computation // from Patient + Observation context. // ----------------------------------------------------------------------------- context Patient define DoseAndRateTypeCarboplatin: Concept { codes: { "ComputedFromTargetAUC" } } define DoseAndRateTypePaclitaxel: Concept { codes: { "ComputedFromTargetMgPerM2" } } ````: **Version: **
  * ?: 2026-03-12-0.1.0
* * **Content: **text/cql: ````library HemOncDoseHelpers version '2026-03-12' using FHIR version '4.0.1' include FHIRHelpers version '4.0.1' called FHIRHelpers codesystem "SigTargetType": 'http://hemonc.org/fhir/CodeSystem/sig-target-type' code "ComputedFromTargetAUC": 'computed-from-target-AUC' from "SigTargetType" code "ComputedFromTargetMgPerM2": 'computed-from-target-mg-per-m2' from "SigTargetType" // ----------------------------------------------------------------------------- // Phase 0 status // ----------------------------------------------------------------------------- // The dose-magnitude computations (Mosteller/Du Bois BSA, Cockcroft-Gault, // Calvert) are emitted via FHIRPath dynamicValues in the ActivityDefinition // resources, because cqf-fhir 8.4.0 has a bug coercing CQL System.Quantity // literals into FHIR.SimpleQuantity at dynamicValue assignment time (surfaces // as 'Type org.hl7.fhir.r4.model.DateTimeType is not comparable'). // // This library still owns the *coded* provenance markers — those work fine // via text/cql.identifier and are referenced from // ActivityDefinition.dynamicValue for the doseAndRate[0].type path. // // Once the cqf-fhir bug is fixed (track upstream), the dose-magnitude // expressions move back into this library and gain real BSA/GFR computation // from Patient + Observation context. // ----------------------------------------------------------------------------- context Patient define DoseAndRateTypeCarboplatin: Concept { codes: { "ComputedFromTargetAUC" } } define DoseAndRateTypePaclitaxel: Concept { codes: { "ComputedFromTargetMgPerM2" } } ````: **Url: **
  * ?: [HemOnc dose-computation helpers (BSA, Calvert)](Library-HemOncDoseHelpers.md)
* * **Content: **text/cql: ````library HemOncDoseHelpers version '2026-03-12' using FHIR version '4.0.1' include FHIRHelpers version '4.0.1' called FHIRHelpers codesystem "SigTargetType": 'http://hemonc.org/fhir/CodeSystem/sig-target-type' code "ComputedFromTargetAUC": 'computed-from-target-AUC' from "SigTargetType" code "ComputedFromTargetMgPerM2": 'computed-from-target-mg-per-m2' from "SigTargetType" // ----------------------------------------------------------------------------- // Phase 0 status // ----------------------------------------------------------------------------- // The dose-magnitude computations (Mosteller/Du Bois BSA, Cockcroft-Gault, // Calvert) are emitted via FHIRPath dynamicValues in the ActivityDefinition // resources, because cqf-fhir 8.4.0 has a bug coercing CQL System.Quantity // literals into FHIR.SimpleQuantity at dynamicValue assignment time (surfaces // as 'Type org.hl7.fhir.r4.model.DateTimeType is not comparable'). // // This library still owns the *coded* provenance markers — those work fine // via text/cql.identifier and are referenced from // ActivityDefinition.dynamicValue for the doseAndRate[0].type path. // // Once the cqf-fhir bug is fixed (track upstream), the dose-magnitude // expressions move back into this library and gain real BSA/GFR computation // from Patient + Observation context. // ----------------------------------------------------------------------------- context Patient define DoseAndRateTypeCarboplatin: Concept { codes: { "ComputedFromTargetAUC" } } define DoseAndRateTypePaclitaxel: Concept { codes: { "ComputedFromTargetMgPerM2" } } ````: **Experimental: **
  * ?: true
* * **Content: **text/cql: ````library HemOncDoseHelpers version '2026-03-12' using FHIR version '4.0.1' include FHIRHelpers version '4.0.1' called FHIRHelpers codesystem "SigTargetType": 'http://hemonc.org/fhir/CodeSystem/sig-target-type' code "ComputedFromTargetAUC": 'computed-from-target-AUC' from "SigTargetType" code "ComputedFromTargetMgPerM2": 'computed-from-target-mg-per-m2' from "SigTargetType" // ----------------------------------------------------------------------------- // Phase 0 status // ----------------------------------------------------------------------------- // The dose-magnitude computations (Mosteller/Du Bois BSA, Cockcroft-Gault, // Calvert) are emitted via FHIRPath dynamicValues in the ActivityDefinition // resources, because cqf-fhir 8.4.0 has a bug coercing CQL System.Quantity // literals into FHIR.SimpleQuantity at dynamicValue assignment time (surfaces // as 'Type org.hl7.fhir.r4.model.DateTimeType is not comparable'). // // This library still owns the *coded* provenance markers — those work fine // via text/cql.identifier and are referenced from // ActivityDefinition.dynamicValue for the doseAndRate[0].type path. // // Once the cqf-fhir bug is fixed (track upstream), the dose-magnitude // expressions move back into this library and gain real BSA/GFR computation // from Patient + Observation context. // ----------------------------------------------------------------------------- context Patient define DoseAndRateTypeCarboplatin: Concept { codes: { "ComputedFromTargetAUC" } } define DoseAndRateTypePaclitaxel: Concept { codes: { "ComputedFromTargetMgPerM2" } } ````: **Date: **
  * ?: 2026-03-12
* * **Content: **text/cql: ````library HemOncDoseHelpers version '2026-03-12' using FHIR version '4.0.1' include FHIRHelpers version '4.0.1' called FHIRHelpers codesystem "SigTargetType": 'http://hemonc.org/fhir/CodeSystem/sig-target-type' code "ComputedFromTargetAUC": 'computed-from-target-AUC' from "SigTargetType" code "ComputedFromTargetMgPerM2": 'computed-from-target-mg-per-m2' from "SigTargetType" // ----------------------------------------------------------------------------- // Phase 0 status // ----------------------------------------------------------------------------- // The dose-magnitude computations (Mosteller/Du Bois BSA, Cockcroft-Gault, // Calvert) are emitted via FHIRPath dynamicValues in the ActivityDefinition // resources, because cqf-fhir 8.4.0 has a bug coercing CQL System.Quantity // literals into FHIR.SimpleQuantity at dynamicValue assignment time (surfaces // as 'Type org.hl7.fhir.r4.model.DateTimeType is not comparable'). // // This library still owns the *coded* provenance markers — those work fine // via text/cql.identifier and are referenced from // ActivityDefinition.dynamicValue for the doseAndRate[0].type path. // // Once the cqf-fhir bug is fixed (track upstream), the dose-magnitude // expressions move back into this library and gain real BSA/GFR computation // from Patient + Observation context. // ----------------------------------------------------------------------------- context Patient define DoseAndRateTypeCarboplatin: Concept { codes: { "ComputedFromTargetAUC" } } define DoseAndRateTypePaclitaxel: Concept { codes: { "ComputedFromTargetMgPerM2" } } ````: **Publisher: **
  * ?: HemOnc FHIR Catalog Working Group
* * **Content: **text/cql: ````library HemOncDoseHelpers version '2026-03-12' using FHIR version '4.0.1' include FHIRHelpers version '4.0.1' called FHIRHelpers codesystem "SigTargetType": 'http://hemonc.org/fhir/CodeSystem/sig-target-type' code "ComputedFromTargetAUC": 'computed-from-target-AUC' from "SigTargetType" code "ComputedFromTargetMgPerM2": 'computed-from-target-mg-per-m2' from "SigTargetType" // ----------------------------------------------------------------------------- // Phase 0 status // ----------------------------------------------------------------------------- // The dose-magnitude computations (Mosteller/Du Bois BSA, Cockcroft-Gault, // Calvert) are emitted via FHIRPath dynamicValues in the ActivityDefinition // resources, because cqf-fhir 8.4.0 has a bug coercing CQL System.Quantity // literals into FHIR.SimpleQuantity at dynamicValue assignment time (surfaces // as 'Type org.hl7.fhir.r4.model.DateTimeType is not comparable'). // // This library still owns the *coded* provenance markers — those work fine // via text/cql.identifier and are referenced from // ActivityDefinition.dynamicValue for the doseAndRate[0].type path. // // Once the cqf-fhir bug is fixed (track upstream), the dose-magnitude // expressions move back into this library and gain real BSA/GFR computation // from Patient + Observation context. // ----------------------------------------------------------------------------- context Patient define DoseAndRateTypeCarboplatin: Concept { codes: { "ComputedFromTargetAUC" } } define DoseAndRateTypePaclitaxel: Concept { codes: { "ComputedFromTargetMgPerM2" } } ````: **Description: **
  * ?: CQL library providing BSA (Mosteller/Du Bois/Haycock), Cockcroft-Gault GFR, Calvert carboplatin formula, and per-sig dose helpers referenced by ActivityDefinition.dynamicValue. Phase 0 spike — covers paclitaxel and carboplatin only. Institution policy (BSA formula, BSA cap, GFR formula, GFR cap) is set via $apply Parameters.
* * **Content: **text/cql: ````library HemOncDoseHelpers version '2026-03-12' using FHIR version '4.0.1' include FHIRHelpers version '4.0.1' called FHIRHelpers codesystem "SigTargetType": 'http://hemonc.org/fhir/CodeSystem/sig-target-type' code "ComputedFromTargetAUC": 'computed-from-target-AUC' from "SigTargetType" code "ComputedFromTargetMgPerM2": 'computed-from-target-mg-per-m2' from "SigTargetType" // ----------------------------------------------------------------------------- // Phase 0 status // ----------------------------------------------------------------------------- // The dose-magnitude computations (Mosteller/Du Bois BSA, Cockcroft-Gault, // Calvert) are emitted via FHIRPath dynamicValues in the ActivityDefinition // resources, because cqf-fhir 8.4.0 has a bug coercing CQL System.Quantity // literals into FHIR.SimpleQuantity at dynamicValue assignment time (surfaces // as 'Type org.hl7.fhir.r4.model.DateTimeType is not comparable'). // // This library still owns the *coded* provenance markers — those work fine // via text/cql.identifier and are referenced from // ActivityDefinition.dynamicValue for the doseAndRate[0].type path. // // Once the cqf-fhir bug is fixed (track upstream), the dose-magnitude // expressions move back into this library and gain real BSA/GFR computation // from Patient + Observation context. // ----------------------------------------------------------------------------- context Patient define DoseAndRateTypeCarboplatin: Concept { codes: { "ComputedFromTargetAUC" } } define DoseAndRateTypePaclitaxel: Concept { codes: { "ComputedFromTargetMgPerM2" } } ````: **Jurisdiction: **
  * ?: DE



## Resource Content

```json
{
  "resourceType" : "Library",
  "id" : "HemOncDoseHelpers",
  "url" : "http://hemonc.org/fhir/Library/HemOncDoseHelpers",
  "version" : "2026-03-12-0.1.0",
  "name" : "HemOncDoseHelpers",
  "title" : "HemOnc dose-computation helpers (BSA, Calvert)",
  "status" : "active",
  "experimental" : true,
  "type" : {
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/library-type",
      "code" : "logic-library"
    }]
  },
  "date" : "2026-03-12",
  "publisher" : "HemOnc FHIR Catalog Working Group",
  "contact" : [{
    "name" : "HemOnc FHIR Catalog Working Group",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/thome/oncology-regimens"
    }]
  }],
  "description" : "CQL library providing BSA (Mosteller/Du Bois/Haycock), Cockcroft-Gault GFR, Calvert carboplatin formula, and per-sig dose helpers referenced by ActivityDefinition.dynamicValue. Phase 0 spike — covers paclitaxel and carboplatin only. Institution policy (BSA formula, BSA cap, GFR formula, GFR cap) is set via $apply Parameters.",
  "useContext" : [{
    "code" : {
      "system" : "http://terminology.hl7.org/CodeSystem/usage-context-type",
      "code" : "task"
    },
    "valueCodeableConcept" : {
      "coding" : [{
        "system" : "http://terminology.hl7.org/CodeSystem/definition-topic",
        "code" : "treatment"
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
  "parameter" : [{
    "name" : "BSAFormula",
    "use" : "in",
    "min" : 0,
    "max" : "1",
    "type" : "string"
  },
  {
    "name" : "BSACapM2",
    "use" : "in",
    "min" : 0,
    "max" : "1",
    "type" : "decimal"
  },
  {
    "name" : "GFRFormula",
    "use" : "in",
    "min" : 0,
    "max" : "1",
    "type" : "string"
  },
  {
    "name" : "CarboGFRCapMlMin",
    "use" : "in",
    "min" : 0,
    "max" : "1",
    "type" : "decimal"
  },
  {
    "name" : "TargetAUC",
    "use" : "in",
    "min" : 0,
    "max" : "1",
    "type" : "decimal"
  },
  {
    "name" : "PaclitaxelDoseMgPerM2",
    "use" : "in",
    "min" : 0,
    "max" : "1",
    "type" : "decimal"
  },
  {
    "name" : "PaclitaxelComputedDose",
    "use" : "out",
    "min" : 0,
    "max" : "1",
    "type" : "Quantity"
  },
  {
    "name" : "CarboplatinCalvertDose",
    "use" : "out",
    "min" : 0,
    "max" : "1",
    "type" : "Quantity"
  }],
  "content" : [{
    "contentType" : "text/cql",
    "data" : "bGlicmFyeSBIZW1PbmNEb3NlSGVscGVycyB2ZXJzaW9uICcyMDI2LTAzLTEyJwoKdXNpbmcgRkhJUiB2ZXJzaW9uICc0LjAuMScKCmluY2x1ZGUgRkhJUkhlbHBlcnMgdmVyc2lvbiAnNC4wLjEnIGNhbGxlZCBGSElSSGVscGVycwoKY29kZXN5c3RlbSAiU2lnVGFyZ2V0VHlwZSI6ICdodHRwOi8vaGVtb25jLm9yZy9maGlyL0NvZGVTeXN0ZW0vc2lnLXRhcmdldC10eXBlJwoKY29kZSAiQ29tcHV0ZWRGcm9tVGFyZ2V0QVVDIjogICAgICdjb21wdXRlZC1mcm9tLXRhcmdldC1BVUMnICAgICAgICAgZnJvbSAiU2lnVGFyZ2V0VHlwZSIKY29kZSAiQ29tcHV0ZWRGcm9tVGFyZ2V0TWdQZXJNMiI6ICdjb21wdXRlZC1mcm9tLXRhcmdldC1tZy1wZXItbTInICAgZnJvbSAiU2lnVGFyZ2V0VHlwZSIKCi8vIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCi8vIFBoYXNlIDAgc3RhdHVzCi8vIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCi8vIFRoZSBkb3NlLW1hZ25pdHVkZSBjb21wdXRhdGlvbnMgKE1vc3RlbGxlci9EdSBCb2lzIEJTQSwgQ29ja2Nyb2Z0LUdhdWx0LAovLyBDYWx2ZXJ0KSBhcmUgZW1pdHRlZCB2aWEgRkhJUlBhdGggZHluYW1pY1ZhbHVlcyBpbiB0aGUgQWN0aXZpdHlEZWZpbml0aW9uCi8vIHJlc291cmNlcywgYmVjYXVzZSBjcWYtZmhpciA4LjQuMCBoYXMgYSBidWcgY29lcmNpbmcgQ1FMIFN5c3RlbS5RdWFudGl0eQovLyBsaXRlcmFscyBpbnRvIEZISVIuU2ltcGxlUXVhbnRpdHkgYXQgZHluYW1pY1ZhbHVlIGFzc2lnbm1lbnQgdGltZSAoc3VyZmFjZXMKLy8gYXMgJ1R5cGUgb3JnLmhsNy5maGlyLnI0Lm1vZGVsLkRhdGVUaW1lVHlwZSBpcyBub3QgY29tcGFyYWJsZScpLgovLwovLyBUaGlzIGxpYnJhcnkgc3RpbGwgb3ducyB0aGUgKmNvZGVkKiBwcm92ZW5hbmNlIG1hcmtlcnMg4oCUIHRob3NlIHdvcmsgZmluZQovLyB2aWEgdGV4dC9jcWwuaWRlbnRpZmllciBhbmQgYXJlIHJlZmVyZW5jZWQgZnJvbQovLyBBY3Rpdml0eURlZmluaXRpb24uZHluYW1pY1ZhbHVlIGZvciB0aGUgZG9zZUFuZFJhdGVbMF0udHlwZSBwYXRoLgovLwovLyBPbmNlIHRoZSBjcWYtZmhpciBidWcgaXMgZml4ZWQgKHRyYWNrIHVwc3RyZWFtKSwgdGhlIGRvc2UtbWFnbml0dWRlCi8vIGV4cHJlc3Npb25zIG1vdmUgYmFjayBpbnRvIHRoaXMgbGlicmFyeSBhbmQgZ2FpbiByZWFsIEJTQS9HRlIgY29tcHV0YXRpb24KLy8gZnJvbSBQYXRpZW50ICsgT2JzZXJ2YXRpb24gY29udGV4dC4KLy8gLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCmNvbnRleHQgUGF0aWVudAoKZGVmaW5lIERvc2VBbmRSYXRlVHlwZUNhcmJvcGxhdGluOgogIENvbmNlcHQgeyBjb2RlczogeyAiQ29tcHV0ZWRGcm9tVGFyZ2V0QVVDIiB9IH0KCmRlZmluZSBEb3NlQW5kUmF0ZVR5cGVQYWNsaXRheGVsOgogIENvbmNlcHQgeyBjb2RlczogeyAiQ29tcHV0ZWRGcm9tVGFyZ2V0TWdQZXJNMiIgfSB9Cg==",
    "title" : "HemOncDoseHelpers.cql"
  }]
}

```
