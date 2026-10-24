# Selection Layer — Formularies and Variant Choice - HemOnc FHIR Regimen Catalog — Executable Knowledge Layer for Oncology Protocols v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* **Selection Layer — Formularies and Variant Choice**

## Selection Layer — Formularies and Variant Choice

### Selection Layer — Formularies, Derived Protocols and Call-Time Variant Choice

> **Status: draft specification (2026-10-24).** Normative language (**SHALL**, **SHOULD**, **MAY**) is used so the rules can be tested, but the whole layer is `experimental = true` until reviewed with HemOnc.org and the MII Onkologie maintainers. Tracked as beads issue `oncology-regimens-hg6`.

#### 1. Problem statement

The HemOnc Knowledge Base does not define a canonical dosing for a regimen. A regimen concept (one CUI, e.g. mFOLFOX6 = `13849`) carries a name, a drug set and membership in regimen classes. Doses exist only on its **variants**, one per study or group of studies that dosed the regimen identically. The `Has variant` relationship is a flat, unranked list. Variant numbers reflect processing order, not preference (mFOLFOX6 Variant #01 is the CAO/ARO/AIO-04 rectal arm with oxaliplatin 100 mg/m² and no bolus; the dosing most clinics mean by "mFOLFOX6" is Variant #06, cui `133145`). The words **canonical** and **version** in HemOncKB mean sig-structure class and snapshot marker respectively, never "the reference protocol".

Consequently:

* A `PlanDefinition` in this IG is **variant-exact** (see [Versioning](versioning.md)). There is no regimen-level `PlanDefinition` that could be applied.
* Any "recommended variant" per MII protocol code or per site **cannot be derived from HemOnc**. It is a policy decision made elsewhere.
* National catalogs that **have** made that decision (e.g. the New Zealand SACT Regimen Library, see §9) also contain consensus modifications with no HemOnc variant at all (low-dose folinic acid 50 mg flat; mFOLFOX6 without the fluorouracil bolus).

This page specifies the layer that holds those decisions, so that the HemOnc catalog stays faithful to its source and the choice becomes an explicit, versioned, attributable input to `$apply`.

#### 2. Layering

```
   ┌──────────────────────────────────────────────────────────────────┐
   │  L3  Call-time inputs                                            │
   │      subject (Patient) · protocol (variant-level PlanDefinition  │
   │      canonical) · preferred start date · scalar overrides        │
   ├──────────────────────────────────────────────────────────────────┤
   │  L2  Selection layer (this page)                                 │
   │      Formulary PlanDefinitions  (restriction)                    │
   │      Derived PlanDefinitions    (extension)                      │
   │      Permitted-variant ValueSets · bridge ConceptMaps            │
   ├──────────────────────────────────────────────────────────────────┤
   │  L1  HemOnc catalog (variant-exact, no defaults)                 │
   │      PlanDefinition per regimen+variant · ActivityDefinition     │
   │      per sig · MedicationKnowledge · Library                     │
   ├──────────────────────────────────────────────────────────────────┤
   │  L0  HemOncKB snapshot (CSV / OMOP)                              │
   └──────────────────────────────────────────────────────────────────┘

```

**Rule L1-1.** L1 artifacts **SHALL NOT** carry a preferred, default or recommended marker. Preference is an L2 property.

**Rule L1-2.** L1 `PlanDefinition`s **MAY** expose **parameters** (§5) so that a bounded set of modifications can be applied without copying the protocol.

#### 3. Formulary PlanDefinition (restriction)

A **formulary** is a `PlanDefinition` that enumerates the protocols a jurisdiction, institution or programme permits for one clinical situation. It is a closed list; what it does not list is not offered.

| | |
| :--- | :--- |
| `type` | **SHALL**be`plan-definition-type#order-set`. |
| `useContext` | **SHALL**carry at least one`jurisdiction`or`venue`context (who the formulary is for) and**SHOULD**carry a`focus`context (condition) and**MAY**carry`program`(intent/setting, e.g. adjuvant). |
| `identifier` | **SHALL**carry an`official`identifier in the issuing body's system. |
| `action`(top level) | Exactly one group with`selectionBehavior = exactly-one`and`groupingBehavior = logical-group`. |
| `action.action[*].definitionCanonical` | **SHALL**reference either an L1 variant`PlanDefinition`or an L2 derived`PlanDefinition`(§4), always with an explicit`|version`. |
| `action.action[*].condition` | **MAY**carry`applicability`conditions (CQL or FHIRPath) over intent, stage, biomarker, prior therapy, organ function. |
| `action.action[*].code` | **SHOULD**carry the issuing body's own protocol code for that entry (e.g. SRL concept, MII protocol code, site code). |
| `action.action[*].extension[formulary-rank]` | **MAY**rank entries; absence means unranked. |
| `relatedArtifact` | **SHALL**cite the governance decision (minutes, guideline, consensus statement) with date. |

**Rule F-1 (restriction).** A consumer that applies a formulary **SHALL NOT** offer a protocol absent from it, even though that protocol remains resolvable in L1.

**Rule F-2 (no inheritance).** A formulary **SHALL NOT** be derived from another formulary. Two sites with overlapping policy publish two formularies. Keeping formularies flat keeps the restriction auditable.

**Rule F-3 (version pinning).** Every `definitionCanonical` in a formulary **SHALL** pin a version. A formulary therefore changes version whenever any referenced protocol changes version.

#### 4. Derived PlanDefinition (extension)

A **derived protocol** is an L2 `PlanDefinition` that represents a dosing with no exact HemOnc variant, expressed as a delta against the closest one.

| | |
| :--- | :--- |
| `type` | `clinical-protocol`, as for L1. |
| `identifier[official]` | The issuing body's identifier (SRL concept id, MII code, site code).**SHALL NOT**use`http://hemonc.org/cui`as`official`. |
| `identifier[secondary]` | **SHALL**carry the parent variant CUI (`http://hemonc.org/variant-cui`) and regimen CUI (`http://hemonc.org/regimen-cui`) so OMOP round-trips still land on HemOnc concepts. |
| `relatedArtifact[derived-from]` | **SHALL**reference the parent L1`PlanDefinition`canonical with version. |
| `extension[regimen-modification]` | **SHALL**list every delta (§4.1), one entry each. An empty list is an error: use the parent instead. |
| `relatedArtifact[justification]` | **SHALL**cite the source that authorises the delta (consensus statement, guideline, national library entry with version). |
| `version` | **SHOULD**follow the issuing body's versioning (e.g. SRL`2.0.2`), not the HemOnc snapshot date. |
| `status` | `draft`until the issuing body confirms;`active`thereafter;`retired`when superseded. |

**Rule D-1 (full content).** A derived `PlanDefinition` **SHALL** be complete and applicable on its own. The modification extension is provenance, not an instruction to compute the content at `$apply` time. FHIR R4 has no inheritance for `PlanDefinition`; a consumer must not need the parent to execute the child.

**Rule D-2 (re-derivation).** When the parent L1 variant changes version (new HemOnc snapshot) or the justification source changes version, the derived protocol **SHALL** be re-diffed and its `version` or `status` updated. Tooling **SHOULD** flag derived protocols whose parent version no longer matches `relatedArtifact[derived-from]`.

##### 4.1 Modification extension

`http://hemonc.org/fhir/StructureDefinition/regimen-modification` (complex extension, context `PlanDefinition`), see [StructureDefinition](StructureDefinition-regimen-modification.md).

| | | |
| :--- | :--- | :--- |
| `kind` | `code`from[regimen-modification-kind](CodeSystem-regimen-modification-kind.md) | `omit-action`·`add-action`·`replace-dose`·`replace-schedule`·`replace-route`·`replace-product` |
| `targetActionId` | `string` | `action.id`in the parent that is omitted or replaced; absent for`add-action`. |
| `component` | `CodeableConcept` | The drug concerned (HemOnc component CUI, plus ATC/RxNorm where available). |
| `from` | `string` | Human-readable parent value (e.g.`folinic acid 400 mg/m² IV over 2 h`). |
| `to` | `string` | Human-readable new value (e.g.`folinic acid 50 mg flat IV over 2 min`); absent for`omit-action`. |
| `rationale` | `markdown` | Why, in the issuing body's words. |

#### 5. Parameterised variants (preferred over copies)

Where a modification is a **toggle or a scalar** that leaves the action tree intact, the L1 variant **SHOULD** accept it as a parameter instead of forcing a derived copy. The formulary entry then references the L1 variant and supplies fixed parameter values.

Mechanism (cqf-fhir / HAPI Clinical Reasoning compatible):

* The variant's `Library` declares the parameter with a default equal to the HemOnc value, e.g. ````parameter IncludeFluorouracilBolus Boolean default true parameter FolinicAcidDosePerM2 Decimal default 400.0 ```` 
* The action that may be omitted carries an `applicability` condition referencing the parameter: 

```
action.condition[0].kind = applicability
action.condition[0].expression.language = text/cql.identifier
action.condition[0].expression.expression = "Fluorouracil bolus applicable"

```

 
* Dose overrides are consumed by the existing `dynamicValue` path (`doseQuantity.value`), see [$apply](apply-and-cds.md).
* The formulary entry pins the values via `extension[formulary-parameter]` (name + value) which the CDS layer forwards in the nested `parameters` resource of `$apply`.

**Rule P-1 (envelope).** The variant **SHALL** declare, per parameter, the admissible range in `Library.parameter` (`min`/`max` via `ParameterDefinition` extensions or documentation). Values outside the envelope **SHALL** be rejected by the CDS layer, not silently applied.

**Rule P-2 (when to copy).** Adding a drug, changing cycle structure, or changing more than the declared parameters **SHALL** produce a derived `PlanDefinition` (§4), not a parameter set.

**Rule P-3 (provenance).** A `CarePlan` produced with non-default parameters **SHALL** record them (`CarePlan.extension[applied-parameters]` or the `Parameters` resource referenced from `Provenance.entity`).

#### 6. Terminology twin

The same policy is published in terminology form so validators, search and non-CDS consumers can see it without executing a `PlanDefinition`.

| | | |
| :--- | :--- | :--- |
| `ValueSet`**permitted variants** | `compose.include`of variant CUIs from`http://hemonc.org/fhir/CodeSystem/hemonc`plus derived-protocol codes from the issuing body's CodeSystem. | **SHALL**be equivalent to the set of`definitionCanonical`targets of the formulary; tooling**SHOULD**generate one from the other. |
| `CodeSystem`**issuing body protocols** | One concept per derived protocol (and optionally per formulary entry), property`parent-variant-cui`. | `content = complete`for the body's own codes;**SHALL NOT**restate HemOnc concepts. |
| `ConceptMap`**bridge** | Issuing-body code → HemOnc variant CUI.`equivalence = equivalent`for exact dose matches,`relatedto`for derived protocols,`narrower`for a national code that maps to several variants. | `status = draft`,`experimental = true`until the issuing body reviews. |

#### 7. Call-time inputs and the two-step CDS flow

Variant choice is an **input**, never a catalog property.

| | | |
| :--- | :--- | :--- |
| Patient | `$apply``subject` | yes |
| Protocol | the`PlanDefinition`being applied (variant-level L1 or derived L2), by canonical with version | yes |
| Preferred start date | nested`parameters`→ CQL`parameter TreatmentStart Date` | yes for timed CarePlans; absent means relative timing only |
| Scalar overrides | nested`parameters`(BSA method, weight basis, variant parameters §5) | no |

**Step 1 — candidate listing.** The CDS service applies the **formulary** `PlanDefinition` with `subject` (and intent/stage inputs). Because the group is `exactly-one`, the resulting `RequestGroup` is a choice list with applicability already evaluated. Delivered as CDS Hooks cards (`order-select`) with one `suggestion` per candidate; each suggestion carries the candidate canonical and any pinned parameters.

**Step 2 — instantiation.** The chosen canonical is applied with `subject`, `TreatmentStart` and parameters. The result is the cycle-level `CarePlan` with `MedicationRequest`s, `instantiatesCanonical` set to the chosen protocol (L1 or L2), and `Provenance` naming the formulary used.

**Rule C-1.** A consumer **SHALL NOT** apply a regimen-level concept. There is nothing to apply. A request naming only a regimen CUI **SHALL** be answered with Step 1.

**Rule C-2.** `CarePlan.instantiatesCanonical` **SHALL** reference the protocol actually applied, with version. The formulary **SHALL** be recorded in `Provenance`, not in `instantiatesCanonical`.

#### 8. Feedback and round-trip

Three loops, of which only the third reaches HemOnc.

1. **Into this catalog.**A derived protocol is a first-class L2`PlanDefinition`(§4). It is registered, versioned and listed by the formulary like any L1 entry.
1. **Into the formulary, from use.**Aggregating`CarePlan.instantiatesCanonical`over a period gives per-variant usage. Issuing bodies**MAY**use it to rank, add or retire entries. This is the architecture of the New Zealand ACT-NOW programme (regimen`CarePlan`→ national database), reused here at site scale.
1. **Into HemOnc.**HemOnc variants are study-derived. A consensus modification without a trial has no slot in HemOncKB unless the editors accept the consensus source as a citable reference. Until that is agreed with HemOnc.org (see[Cooperation](cooperation.md)), derived protocols**SHALL**be assumed to live permanently in L2.

#### 9. Worked example — NZ colorectal mFOLFOX6

Source: SACT Regimen Library, Te Aho o Te Kahu / NZ Formulary, [https://srl.org.nz](https://srl.org.nz), colorectal group, read 2026-10-22. Entry ids are SNOMED CT NZ-extension concepts; versions are the SRL's own.

| | | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CRC Metastatic – mFOLFOX6 [bolus and infusion] [high dose FA] | `52101000210105`· 2.0.2 | 85 mg/m² / 2 h | 400 mg/m² / 2 h | 400 mg/m² | 2400 mg/m² / 46 h | mFOLFOX6 Variant #06, cui`133145`(IDEA / N0147 / NSABP C-08 / CALGB 80702) —**exact** |
| CRC Adjuvant – mFOLFOX6 [low dose FA] | `52201000210102`· 2.0.0 | 85 | **50 mg flat / 2 min** | 400 | 2400 / 46 h | none → derived from`133145`,`replace-dose` |
| CRC Metastatic – mFOLFOX6 [high dose FA] (no bolus) | `588251000210108`· 1.0.0 | 85 | 400 | **—** | 2400 / 46 h | none →`133145`with`IncludeFluorouracilBolus = false` |

Artifacts in this IG:

* [`PlanDefinition/nz-crc-mfolfox6-formulary`](PlanDefinition-nz-crc-mfolfox6-formulary.md) — formulary with three entries, `exactly-one`.
* [`PlanDefinition/srl-588251000210108-mfolfox6-nobolus`](PlanDefinition-srl-588251000210108-mfolfox6-nobolus.md) — derived protocol (§4) shown as a full copy because the L1 mFOLFOX6 Variant #06 `PlanDefinition` is not yet generated; once it is, this entry collapses to a parameter set (§5).
* [`ValueSet/nz-crc-permitted-variants`](ValueSet-nz-crc-permitted-variants.md) — terminology twin of the formulary.
* [`ConceptMap/srl-to-hemonc-variant`](ConceptMap-srl-to-hemonc-variant.md) — bridge, three rows.

The SRL is not openly licensed (NZF standard terms, NZ jurisdiction). The example reproduces dosing facts for a technical demonstration and does not redistribute SRL content.

#### 10. Relationship to Phase 1A

The Phase 1A plan (onboarding guide §6.2) foresees a `recommended_variant_cui` column in `matches.csv` and "one `PlanDefinition` (regimen + recommended variant)" per matched MII code. Under this specification:

* `recommended_variant_cui` becomes an **L2 decision** with a documented method and confidence per row, never a HemOnc property.
* The MII-facing deliverable is a **formulary** per MII protocol code (jurisdiction DE, issuing body MII Onkologie or the site) listing the admissible HemOnc variants, plus derived protocols for German consensus dosing (AWMF S3, Onkopedia) that HemOnc lacks.
* The bridge `ConceptMap/mii-onko-protokoll-to-hemonc` keeps `relatedto` at regimen level and gains `equivalent`/`narrower` rows at variant level from the formulary.

#### 11. Open questions

1. Will HemOnc.org accept national consensus documents as variant sources? Determines whether §8 loop 3 is ever closed.
1. Should the formulary be an`order-set``PlanDefinition`(chosen here, executable) or a`Composition`/`List`(simpler, not executable)? R4`CatalogEntry`was considered and rejected (draft, removed in R5).
1. Parameter envelope representation:`ParameterDefinition`has no min/max; candidates are a`Library`extension or a`Questionnaire`with`minValue`/`maxValue`as the parameter form.
1. Licensing of national libraries (SRL, eviQ, NHS) for publishing bridge`ConceptMap`s that quote their codes and names.

