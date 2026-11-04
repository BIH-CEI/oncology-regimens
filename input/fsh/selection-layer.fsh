// ============================================================================
// SELECTION LAYER (L2) — formularies, derived protocols, terminology twin.
// Specification: input/pagecontent/selection-layer.md
// Worked example: New Zealand SACT Regimen Library (srl.org.nz), colorectal
// mFOLFOX6, read 2026-10-22. SRL ids are SNOMED CT NZ-extension concept ids.
// Everything here is experimental until reviewed with HemOnc.org / MII.
// ============================================================================

Alias: $hemonc        = http://hemonc.org/fhir/CodeSystem/hemonc
Alias: $pdtype        = http://terminology.hl7.org/CodeSystem/plan-definition-type
Alias: $uctx          = http://terminology.hl7.org/CodeSystem/usage-context-type
Alias: $sct           = http://snomed.info/sct
Alias: $iso3166       = urn:iso:std:iso:3166
Alias: $atype         = http://terminology.hl7.org/CodeSystem/action-type

// ----------------------------------------------------------------------------
// Terminology for the modification extension
// ----------------------------------------------------------------------------

CodeSystem: RegimenModificationKind
Id: regimen-modification-kind
Title: "Regimen Modification Kind"
Description: "Kinds of delta a derived (L2) PlanDefinition applies against its parent HemOnc variant."
* ^status = #draft
* ^experimental = true
* ^caseSensitive = true
* ^content = #complete
* #omit-action      "Omit action"      "An action present in the parent is removed (e.g. the fluorouracil bolus)."
* #add-action       "Add action"       "An action absent in the parent is added (e.g. a supportive-care medication)."
* #replace-dose     "Replace dose"     "Same drug, same schedule, different dose or dose basis (e.g. mg/m² → flat mg)."
* #replace-schedule "Replace schedule" "Same drug and dose, different days, frequency or infusion duration."
* #replace-route    "Replace route"    "Same drug and dose, different route."
* #replace-product  "Replace product"  "Different product for the same component (e.g. leucovorin → levoleucovorin)."

ValueSet: RegimenModificationKindVS
Id: regimen-modification-kind-vs
Title: "Regimen Modification Kind ValueSet"
Description: "All kinds of regimen modification."
* ^status = #draft
* ^experimental = true
* include codes from system RegimenModificationKind

// ----------------------------------------------------------------------------
// Extensions
// ----------------------------------------------------------------------------

Extension: RegimenModification
Id: regimen-modification
Title: "Regimen Modification"
Description: "One delta between a derived (L2) PlanDefinition and the HemOnc variant it is derived from. Provenance only: the derived PlanDefinition SHALL be complete on its own (Rule D-1)."
Context: PlanDefinition
* ^status = #draft
* ^experimental = true
* extension contains
    kind 1..1 MS and
    targetActionId 0..1 and
    component 0..1 and
    from 0..1 and
    to 0..1 and
    rationale 0..1
* extension[kind].value[x] only code
* extension[kind].valueCode from RegimenModificationKindVS (required)
* extension[kind] ^short = "omit-action | add-action | replace-dose | replace-schedule | replace-route | replace-product"
* extension[targetActionId].value[x] only string
* extension[targetActionId] ^short = "action.id in the parent PlanDefinition that is omitted or replaced"
* extension[component].value[x] only CodeableConcept
* extension[component] ^short = "Drug concerned (HemOnc component CUI, plus ATC/RxNorm where available)"
* extension[from].value[x] only string
* extension[from] ^short = "Parent value, human-readable"
* extension[to].value[x] only string
* extension[to] ^short = "New value, human-readable; absent for omit-action"
* extension[rationale].value[x] only markdown
* extension[rationale] ^short = "Why, in the issuing body's words"

Extension: FormularyRank
Id: formulary-rank
Title: "Formulary Rank"
Description: "Optional rank of an entry within a formulary PlanDefinition. 1 = first choice. Absence means unranked."
Context: PlanDefinition.action
* ^status = #draft
* ^experimental = true
* value[x] only positiveInt

Extension: FormularyParameter
Id: formulary-parameter
Title: "Formulary Parameter"
Description: "A parameter value a formulary entry pins on the referenced (parameterised) variant PlanDefinition. Forwarded by the CDS layer in the nested `parameters` of $apply."
Context: PlanDefinition.action
* ^status = #draft
* ^experimental = true
* extension contains
    name 1..1 and
    value 1..1
* extension[name].value[x] only string
* extension[name] ^short = "CQL parameter name declared by the variant's Library"
* extension[value].value[x] only boolean or decimal or integer or string or Quantity or CodeableConcept

// ----------------------------------------------------------------------------
// Derived protocol (L2) — SRL 588251000210108, mFOLFOX6 without 5-FU bolus
// Shown as a full copy because the L1 mFOLFOX6 Variant #06 PlanDefinition is
// not yet generated. Once it exists this collapses to a parameter set
// (IncludeFluorouracilBolus = false) on the formulary entry.
// ----------------------------------------------------------------------------

Instance: srl-588251000210108-mfolfox6-nobolus
InstanceOf: PlanDefinition
Usage: #example
* name = "SRLmFOLFOX6HighFANoBolus"
* title = "CRC Metastatic – mFOLFOX6 [high dose folinic acid], no fluorouracil bolus (SRL 588251000210108 v1.0.0)"
* status = #draft
* experimental = true
* version = "1.0.0"
* date = "2026-07-01"
* publisher = "European SACT Regimen Catalog Working Group (example; content attributed to Te Aho o Te Kahu / NZ Formulary)"
* type = $pdtype#clinical-protocol
* identifier[0].use = #official
* identifier[0].system = "https://srl.org.nz/regimens"
* identifier[0].value = "588251000210108"
* identifier[1].use = #secondary
* identifier[1].system = "http://hemonc.org/variant-cui"
* identifier[1].value = "133145"
* identifier[2].use = #secondary
* identifier[2].system = "http://hemonc.org/regimen-cui"
* identifier[2].value = "13849"
* useContext[0].code = $uctx#focus
* useContext[0].valueCodeableConcept = $hemonc#13849 "mFOLFOX6"
* useContext[1].code = $uctx#jurisdiction
* useContext[1].valueCodeableConcept = $iso3166#NZ "New Zealand"
* description = "Derived (L2) protocol: HemOnc mFOLFOX6 Variant #06 (cui 133145) with the fluorouracil 400 mg/m² bolus omitted, as published by the NZ SACT Regimen Library on 2026-07-01 following the NZ Society for Oncology Gastrointestinal Cancers Special Interest Group recommendation. Oxaliplatin 85 mg/m² IV over 120 min day 1; folinic acid 400 mg/m² IV over 120 min day 1; fluorouracil 2400 mg/m² IV over 46 h day 1; 14-day cycle. Supportive care (antiemetics, loperamide) as per SRL, not reproduced here."
* relatedArtifact[0].type = #derived-from
* relatedArtifact[0].label = "Parent HemOnc variant"
* relatedArtifact[0].resource = "http://hemonc.org/fhir/PlanDefinition/regimen-13849-variant-133145|2026-03-12"
* relatedArtifact[1].type = #justification
* relatedArtifact[1].label = "SRL entry 588251000210108 v1.0.0, published 2026-07-01"
* relatedArtifact[1].citation = "Te Aho o Te Kahu / New Zealand Formulary. SACT Regimen Library: CRC Metastatic – mFOLFOX6 [oxaliplatin, folinic acid and fluorouracil] [high dose folinic acid]. Version 1.0.0, 1 July 2026."
* relatedArtifact[1].url = "https://srl.org.nz/regimens/colorectal/588251000210108"
* extension[RegimenModification].extension[kind].valueCode = #omit-action
* extension[RegimenModification].extension[targetActionId].valueString = "fluorouracil-bolus-d1"
* extension[RegimenModification].extension[component].valueCodeableConcept.text = "Fluorouracil (bolus)"
* extension[RegimenModification].extension[from].valueString = "Fluorouracil 400 mg/m² IV bolus day 1"
* extension[RegimenModification].extension[rationale].valueMarkdown = "The fluorouracil bolus was removed following the recommendation of the New Zealand Society for Oncology (NZSO) Gastrointestinal Cancers Special Interest Group (GISIG)."
* action[0].id = "cycle"
* action[0].title = "14-day cycle, repeated until progression or unacceptable toxicity"
* action[0].timingTiming.repeat.frequency = 1
* action[0].timingTiming.repeat.period = 14
* action[0].timingTiming.repeat.periodUnit = #d
* action[0].groupingBehavior = #logical-group
* action[0].selectionBehavior = #all
* action[0].action[0].id = "oxaliplatin-d1"
* action[0].action[0].title = "Oxaliplatin 85 mg/m² IV over 120 min, day 1"
* action[0].action[0].type = $atype#create
* action[0].action[1].id = "folinic-acid-d1"
* action[0].action[1].title = "Folinic acid (calcium folinate) 400 mg/m² IV over 120 min, day 1"
* action[0].action[1].type = $atype#create
* action[0].action[1].relatedAction[0].actionId = "oxaliplatin-d1"
* action[0].action[1].relatedAction[0].relationship = #concurrent-with-start
* action[0].action[2].id = "fluorouracil-infusion-d1"
* action[0].action[2].title = "Fluorouracil 2400 mg/m² IV continuous over 46 h, day 1"
* action[0].action[2].type = $atype#create
* action[0].action[2].relatedAction[0].actionId = "folinic-acid-d1"
* action[0].action[2].relatedAction[0].relationship = #after-end

// ----------------------------------------------------------------------------
// Formulary (L2) — NZ colorectal, mFOLFOX6 family
// ----------------------------------------------------------------------------

Instance: nz-crc-mfolfox6-formulary
InstanceOf: PlanDefinition
Usage: #example
* name = "NZColorectalMFOLFOX6Formulary"
* title = "NZ colorectal formulary — mFOLFOX6 family (example, SRL read 2026-10-22)"
* status = #draft
* experimental = true
* version = "2026-10-22"
* date = "2026-10-24"
* publisher = "European SACT Regimen Catalog Working Group (example)"
* type = $pdtype#order-set
* identifier[0].use = #official
* identifier[0].system = "http://hemonc.org/fhir/example-formulary"
* identifier[0].value = "nz-crc-mfolfox6"
* useContext[0].code = $uctx#jurisdiction
* useContext[0].valueCodeableConcept = $iso3166#NZ "New Zealand"
* useContext[1].code = $uctx#focus
* useContext[1].valueCodeableConcept = $sct#363406005 "Malignant tumor of colon"
* useContext[2].code = $uctx#focus
* useContext[2].valueCodeableConcept = $hemonc#13849 "mFOLFOX6"
* description = "Example formulary (selection layer, §3 of the Selection Layer page). Lists the three mFOLFOX6 specifications the NZ SACT Regimen Library publishes for colorectal cancer and maps each to its HemOnc basis. Restriction: the other 19 HemOnc mFOLFOX6 variants are not offered. Extension: two entries have no HemOnc variant and are expressed as a parameter set and a derived protocol respectively."
* relatedArtifact[0].type = #documentation
* relatedArtifact[0].label = "Governance source"
* relatedArtifact[0].citation = "Te Aho o Te Kahu. SACT Regimen Library, colorectal group, as read 2026-10-22. Clinical governance: Haematology and Medical Oncology Working Groups; annual regimen review workshops."
* relatedArtifact[0].url = "https://srl.org.nz/regimens/colorectal"
* action[0].id = "choose-mfolfox6"
* action[0].title = "Choose one mFOLFOX6 specification"
* action[0].groupingBehavior = #logical-group
* action[0].selectionBehavior = #exactly-one
// Entry 1 — exact HemOnc variant
* action[0].action[0].id = "srl-52101000210105"
* action[0].action[0].title = "mFOLFOX6, high dose folinic acid, with bolus (SRL 52101000210105 v2.0.2)"
* action[0].action[0].code[0].coding[0].system = "https://srl.org.nz/regimens"
* action[0].action[0].code[0].coding[0].code = #52101000210105
* action[0].action[0].code[0].coding[0].version = "2.0.2"
* action[0].action[0].definitionCanonical = "http://hemonc.org/fhir/PlanDefinition/regimen-13849-variant-133145|2026-03-12"
* action[0].action[0].extension[FormularyRank].valuePositiveInt = 1
* action[0].action[0].condition[0].kind = #applicability
* action[0].action[0].condition[0].expression.description = "Metastatic or adjuvant intent"
* action[0].action[0].condition[0].expression.language = #text/cql.identifier
* action[0].action[0].condition[0].expression.expression = "Intent is adjuvant or palliative"
// Entry 2 — same HemOnc variant, parameterised (bolus off)
* action[0].action[1].id = "srl-588251000210108"
* action[0].action[1].title = "mFOLFOX6, high dose folinic acid, no bolus (SRL 588251000210108 v1.0.0)"
* action[0].action[1].code[0].coding[0].system = "https://srl.org.nz/regimens"
* action[0].action[1].code[0].coding[0].code = #588251000210108
* action[0].action[1].code[0].coding[0].version = "1.0.0"
* action[0].action[1].definitionCanonical = "http://hemonc.org/fhir/PlanDefinition/srl-588251000210108-mfolfox6-nobolus|1.0.0"
* action[0].action[1].extension[FormularyParameter].extension[name].valueString = "IncludeFluorouracilBolus"
* action[0].action[1].extension[FormularyParameter].extension[value].valueBoolean = false
* action[0].action[1].condition[0].kind = #applicability
* action[0].action[1].condition[0].expression.description = "Metastatic intent (SRL publishes the no-bolus entry for CRC Metastatic only)"
* action[0].action[1].condition[0].expression.language = #text/cql.identifier
* action[0].action[1].condition[0].expression.expression = "Intent is palliative"
// Entry 3 — derived dose (low-dose folinic acid); derived PD not yet authored
* action[0].action[2].id = "srl-52201000210102"
* action[0].action[2].title = "mFOLFOX6, low dose folinic acid 50 mg flat, with bolus (SRL 52201000210102 v2.0.0) — adjuvant, 12 cycles"
* action[0].action[2].code[0].coding[0].system = "https://srl.org.nz/regimens"
* action[0].action[2].code[0].coding[0].code = #52201000210102
* action[0].action[2].code[0].coding[0].version = "2.0.0"
* action[0].action[2].definitionCanonical = "http://hemonc.org/fhir/PlanDefinition/regimen-13849-variant-133145|2026-03-12"
* action[0].action[2].extension[FormularyParameter][0].extension[name].valueString = "FolinicAcidFlatDoseMg"
* action[0].action[2].extension[FormularyParameter][0].extension[value].valueDecimal = 50
* action[0].action[2].extension[FormularyParameter][1].extension[name].valueString = "MaxCycles"
* action[0].action[2].extension[FormularyParameter][1].extension[value].valueInteger = 12
* action[0].action[2].condition[0].kind = #applicability
* action[0].action[2].condition[0].expression.language = #text/cql.identifier
* action[0].action[2].condition[0].expression.expression = "Intent is adjuvant"

// ----------------------------------------------------------------------------
// Terminology twin
// ----------------------------------------------------------------------------

ValueSet: NZCRCPermittedVariants
Id: nz-crc-permitted-variants
Title: "NZ colorectal permitted mFOLFOX6 variants (example)"
Description: "Terminology twin of PlanDefinition/nz-crc-mfolfox6-formulary: the HemOnc variant CUIs and SRL-derived protocol ids a consumer may offer. SHALL stay equivalent to the formulary's definitionCanonical targets (Rule in §6)."
* ^status = #draft
* ^experimental = true
* ^version = "2026-10-22"
* $hemonc#133145 "mFOLFOX6 Variant #06"
* https://srl.org.nz/regimens#588251000210108 "CRC Metastatic – mFOLFOX6 [high dose folinic acid] (no bolus)"
* https://srl.org.nz/regimens#52201000210102 "CRC Adjuvant – mFOLFOX6 [low dose folinic acid]"

Instance: srl-to-hemonc-variant
InstanceOf: ConceptMap
Usage: #example
* name = "SRLToHemOncVariant"
* title = "SRL regimen id → HemOnc variant CUI (example, colorectal mFOLFOX6)"
* status = #draft
* experimental = true
* version = "2026-10-22"
* date = "2026-10-24"
* publisher = "European SACT Regimen Catalog Working Group (example)"
* description = "Bridge ConceptMap from NZ SACT Regimen Library entries to the HemOnc variant each is based on. equivalent = dose-for-dose match; relatedto = derived with a documented modification. Not a redistribution of SRL content."
* sourceUri = "https://srl.org.nz/regimens"
* targetUri = "http://hemonc.org/fhir/CodeSystem/hemonc"
* group[0].source = "https://srl.org.nz/regimens"
* group[0].target = $hemonc
* group[0].element[0].code = #52101000210105
* group[0].element[0].display = "CRC Metastatic – mFOLFOX6 [bolus and infusion] [high dose folinic acid] v2.0.2"
* group[0].element[0].target[0].code = #133145
* group[0].element[0].target[0].display = "mFOLFOX6 Variant #06"
* group[0].element[0].target[0].equivalence = #equivalent
* group[0].element[0].target[0].comment = "Oxaliplatin 85/2h, folinic acid 400/2h, 5-FU 400 bolus + 2400/46h, q14d. Infusion durations match."
* group[0].element[1].code = #588251000210108
* group[0].element[1].display = "CRC Metastatic – mFOLFOX6 [high dose folinic acid] (no bolus) v1.0.0"
* group[0].element[1].target[0].code = #133145
* group[0].element[1].target[0].display = "mFOLFOX6 Variant #06"
* group[0].element[1].target[0].equivalence = #relatedto
* group[0].element[1].target[0].comment = "omit-action: fluorouracil 400 mg/m² bolus. No HemOnc variant drops the bolus at otherwise identical doses."
* group[0].element[2].code = #52201000210102
* group[0].element[2].display = "CRC Adjuvant – mFOLFOX6 [low dose folinic acid] v2.0.0"
* group[0].element[2].target[0].code = #133145
* group[0].element[2].target[0].display = "mFOLFOX6 Variant #06"
* group[0].element[2].target[0].equivalence = #relatedto
* group[0].element[2].target[0].comment = "replace-dose: folinic acid 400 mg/m² IV 2 h → 50 mg flat IV 2 min. Lowest HemOnc leucovorin dose for mFOLFOX6 is 200 mg/m²."
