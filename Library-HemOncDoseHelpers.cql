library HemOncDoseHelpers version '2026-03-12'

using FHIR version '4.0.1'

include FHIRHelpers version '4.0.1' called FHIRHelpers

codesystem "SigTargetType": 'http://hemonc.org/fhir/CodeSystem/sig-target-type'

code "ComputedFromTargetAUC":     'computed-from-target-AUC'         from "SigTargetType"
code "ComputedFromTargetMgPerM2": 'computed-from-target-mg-per-m2'   from "SigTargetType"

// -----------------------------------------------------------------------------
// Phase 0 status
// -----------------------------------------------------------------------------
// The dose-magnitude computations (Mosteller/Du Bois BSA, Cockcroft-Gault,
// Calvert) are emitted via FHIRPath dynamicValues in the ActivityDefinition
// resources, because cqf-fhir 8.4.0 has a bug coercing CQL System.Quantity
// literals into FHIR.SimpleQuantity at dynamicValue assignment time (surfaces
// as 'Type org.hl7.fhir.r4.model.DateTimeType is not comparable').
//
// This library still owns the *coded* provenance markers — those work fine
// via text/cql.identifier and are referenced from
// ActivityDefinition.dynamicValue for the doseAndRate[0].type path.
//
// Once the cqf-fhir bug is fixed (track upstream), the dose-magnitude
// expressions move back into this library and gain real BSA/GFR computation
// from Patient + Observation context.
// -----------------------------------------------------------------------------

context Patient

define DoseAndRateTypeCarboplatin:
  Concept { codes: { "ComputedFromTargetAUC" } }

define DoseAndRateTypePaclitaxel:
  Concept { codes: { "ComputedFromTargetMgPerM2" } }
