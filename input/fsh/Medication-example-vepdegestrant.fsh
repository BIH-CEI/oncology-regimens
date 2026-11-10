// ============================================================================
// EXAMPLE 2 — investigational substance, UNII-first (no ATC yet).
//
// Vepdegestrant: in clinical trials, NOT approved. In HemOnc: investigational=TRUE,
// atc="No ATC Code". This is the case that justifies keeping UNII in the stack:
// UNII is the substance anchor exactly where ATC/ASK/RxNorm are still absent.
//
// Verified absent for this substance:
//   * ATC-WHO / ATC-DE  -> no ATC assigned yet
//   * ASK (BfArM)       -> 0 hits on the MII Ontoserver
//   * RxNorm            -> "Not in RxNorm Extension" (HemOnc rxnorm_map)
// Present:
//   * HemOnc CUI, UNII (FDA GSRS, via EMA SMS), IDMP/SMS_ID (EMA SPOR)
//   * WHO INN list no. 12157 (from EMA SMS INN_Number) — recorded as a note
//
// Resource choice: Medication (see Medication-example-carboplatin.fsh). The
// former MedicationKnowledge.productType "IMP" flag is carried by the
// medication-type extension (R6 mapping, FHIR-57378).
// ============================================================================

Instance: med-example-vepdegestrant
InstanceOf: Medication
Usage: #example
Title: "Vepdegestrant (catalog Medication, investigational, UNII-first)"
Description: "Kind-of-drug Medication for an investigational substance without ATC, ASK or RxNorm code: HemOnc CUI, UNII and EMA SPOR SMS only. Investigational status via medication-type."
* status = #active
* code.text = "Vepdegestrant"

// --- canonical metadata (R6 pre-adoption) --------------------------------------
* extension[$artifact-url].valueUri = "http://hemonc.org/fhir/Medication/med-example-vepdegestrant"
* extension[$artifact-version].valueString = "2026-03-12"
* extension[$artifact-name].valueString = "Vepdegestrant"
* extension[$artifact-publisher].valueString = "HemOnc.org"

// --- investigational medicinal product flag (was MedicationKnowledge.productType)
* extension[$medication-type].valueCodeableConcept.text = "Investigational medicinal product (IMP)"

// --- identity: HemOnc drug CUI -------------------------------------------------
* identifier[0].use = #official
* identifier[0].system = "http://hemonc.org/cui"
* identifier[0].value = "161163"

// --- substance anchors (all that exist for an investigational compound) --------
// HemOnc CUI (CC BY 4.0) — internal / OMOP anchor
* code.coding[+] = http://hemonc.org/fhir/CodeSystem/hemonc#161163 "Vepdegestrant"
* code.coding[=].version = "2026-03-12"
// UNII (FDA GSRS — public domain) — the early/universal substance id; present without ATC
* code.coding[+] = http://fdasis.nlm.nih.gov#WC1U3R1YMI "VEPDEGESTRANT"
// IDMP substance / EMA SPOR SMS — EU-native anchor (system URI: confirm final canonical)
* code.coding[+] = https://spor.ema.europa.eu/v2/substances#300000041131 "Vepdegestrant"

// --- classification (HemOnc, CC BY 4.0) — R6: Medication.classification -------
* extension[$medication-classification][0].extension[type].valueCodeableConcept = $classification-type#moa "Mechanism of Action"
* extension[$medication-classification][0].extension[type].valueCodeableConcept.text = "HemOnc main class"
* extension[$medication-classification][0].extension[classification].valueCodeableConcept.text = "Proteolysis-targeting chimera estrogen receptor degrader"
* extension[$medication-classification][0].extension[source].valueString = "HemOncKB drugs.csv main_class, snapshot 2026-03-12"
