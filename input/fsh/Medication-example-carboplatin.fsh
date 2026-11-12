// ============================================================================
// EXAMPLE — fully-coded Medication (kind-of-drug, catalog level) for one
// substance (Carboplatin). Demonstrates the assembled coding stack + licensing
// posture.
//
// Why Medication and not MedicationKnowledge: MedicationKnowledge is removed in
// FHIR R6 (FHIR-50845); Medication becomes an optional canonical resource there
// (FHIR-57813). In R4 the canonical metadata is carried by the artifact-*
// extensions and the classification by medication-classification
// (hl7.fhir.uv.extensions). See the "FHIR versions" page.
//
// Publish-vs-reference:
//   * HemOnc CUI, RxNorm, UNII, IDMP/SMS  -> open data, safe to publish.
//   * ATC-WHO / ATC-DE (BfArM)            -> REFERENCE ONLY. We do NOT ship the
//     ATC CodeSystem content (content=not-present); consumers resolve via a
//     licensed terminology server. Assignment provenance = HemOnc (CC BY 4.0),
//     validated live (ATC-WHO v2025 @ HL7-EU tx; ATC-DE v2026 @ MII Ontoserver).
//   * ASK (BfArM) -> DE substance id; check BfArM reuse terms before republishing.
//
// Every coding carries `version` so cross-refs are unambiguous.
// ============================================================================

Alias: $artifact-url = http://hl7.org/fhir/StructureDefinition/artifact-url
Alias: $artifact-version = http://hl7.org/fhir/StructureDefinition/artifact-version
Alias: $artifact-name = http://hl7.org/fhir/StructureDefinition/artifact-name
Alias: $artifact-publisher = http://hl7.org/fhir/StructureDefinition/artifact-publisher
Alias: $medication-classification = http://hl7.org/fhir/StructureDefinition/medication-classification
Alias: $medication-type = http://hl7.org/fhir/StructureDefinition/medication-type
Alias: $classification-type = http://hl7.org/fhir/medication-classification-type

Instance: med-example-carboplatin
InstanceOf: Medication
Usage: #example
Title: "Carboplatin (catalog Medication, fully coded)"
Description: "Kind-of-drug Medication for carboplatin with the full coding stack (HemOnc CUI, RxNorm, UNII, EMA SPOR SMS, ATC-WHO, ATC-DE, ASK) and HemOnc classification. Canonical metadata via artifact-* extensions (R6: native Medication.url/version/name/publisher)."
* status = #active
* code.text = "Carboplatin"

// --- canonical metadata (R6 pre-adoption: Medication as canonical resource) ----
* extension[$artifact-url].valueUri = "http://hemonc.org/fhir/Medication/med-example-carboplatin"
* extension[$artifact-version].valueString = "2026-03-12"
* extension[$artifact-name].valueString = "Carboplatin"
* extension[$artifact-publisher].valueString = "HemOnc.org"

// --- identity: HemOnc drug CUI -------------------------------------------------
* identifier[0].use = #official
* identifier[0].system = "http://hemonc.org/cui"
* identifier[0].value = "88"

// --- open, publishable codings -------------------------------------------------
// HemOnc CUI (CC BY 4.0) — internal / OMOP round-trip anchor
* code.coding[+] = http://hemonc.org/fhir/CodeSystem/hemonc#88 "Carboplatin"
* code.coding[=].version = "2026-03-12"
// RxNorm (NLM — open)
* code.coding[+] = http://www.nlm.nih.gov/research/umls/rxnorm#40048 "carboplatin"
// UNII (FDA GSRS — public domain) — sourced from EMA SPOR SMS
* code.coding[+] = http://fdasis.nlm.nih.gov#BG3F62OND5 "CARBOPLATIN"
// IDMP substance / EMA SPOR SMS — EU-native anchor  (system URI: confirm final canonical)
* code.coding[+] = https://spor.ema.europa.eu/v2/substances#100000092564 "Carboplatin"

// --- reference-only codings (restricted CodeSystems — not republished) ---------
// ATC-WHO — WHO copyright; carried as a binding, resolved by a licensed TS
* code.coding[+] = http://www.whocc.no/atc#L01XA02 "carboplatin"
* code.coding[=].version = "2025"
// ATC-DE (BfArM) — derived from WHO ATC; binding only
* code.coding[+] = http://fhir.de/CodeSystem/bfarm/atc#L01XA02 "Carboplatin"
* code.coding[=].version = "2026"
// ASK (BfArM Arzneistoffkatalog) — DE substance identifier
* code.coding[+] = http://fhir.de/CodeSystem/ask#23168 "Carboplatin"
* code.coding[=].version = "20260105"

// --- classification (HemOnc, CC BY 4.0) — R6: Medication.classification -------
* extension[$medication-classification][0].extension[type].valueCodeableConcept = $classification-type#pharmacologic "Pharmacologic Class"
* extension[$medication-classification][0].extension[type].valueCodeableConcept.text = "HemOnc main class"
* extension[$medication-classification][0].extension[classification].valueCodeableConcept.text = "Platinum agent"
* extension[$medication-classification][0].extension[source].valueString = "HemOncKB drugs.csv main_class, snapshot 2026-03-12"
* extension[$medication-classification][1].extension[type].valueCodeableConcept = $classification-type#moa "Mechanism of Action"
* extension[$medication-classification][1].extension[type].valueCodeableConcept.text = "CanMED major class"
* extension[$medication-classification][1].extension[classification].valueCodeableConcept.text = "Alkylating agent"
* extension[$medication-classification][1].extension[source].valueString = "HemOncKB drugs.csv CanMED_major_class, snapshot 2026-03-12"
