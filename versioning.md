# Versioning Strategy - European SACT Regimen Catalog — Executable Knowledge Layer for Systemic Anti-Cancer Therapy Regimens v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* **Versioning Strategy**

## Versioning Strategy

### Versioning Strategy

This IG operates over content that itself has four orthogonal version axes; the strategy below picks one as the authoritative version stamp and surfaces the others as identifiers / extensions where consumers need them.

#### Authoritative version of every artifact

The HemOncKB snapshot date in `YYYY-MM-DD` form (e.g. `2026-03-12`). Every `CodeSystem`, `ValueSet`, `MedicationKnowledge`, `ActivityDefinition`, `PlanDefinition` and `Library` in this IG carries this value as `Resource.version`. A new HemOnc snapshot (quarterly) produces a new version against the same canonical URL.

`Resource.date` is set to the same snapshot timestamp.

#### Canonical URLs are stable across releases

All canonical URLs are of the form `http://hemonc.org/fhir/<ResourceType>/<stable-id>`. Consumers pin the canonical and pick a version; canonical URLs never change once issued.

The HemOnc CUI is also held as a `use=official` identifier with system `http://hemonc.org/cui`, so the CUI remains addressable even if the canonical scheme evolves.

#### Lifecycle and deprecation

`Resource.status` follows the HemOnc concept's lifecycle:

* `active` while HemOnc's `date_deprecated` is null.
* `retired` once `date_deprecated` is set.

`Resource.effectivePeriod.start = <date_added>` and `Resource.effectivePeriod.end = <date_deprecated>` carry the HemOnc-side lifetime explicitly so consumers can answer "was this concept active in 2018?" without parsing the changelog.

#### Co-evolving identifiers

The MII Onkologie protocol-code binding is carried as a `use=secondary` identifier on `PlanDefinition`:

```
identifier:
  - use: official
    system: http://hemonc.org/cui
    value: "18203"                       # HemOnc regimen CUI
  - use: secondary
    system: http://hemonc.org/variant-cui
    value: "144530"                      # HemOnc variant CUI
  - use: secondary
    system: https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/CodeSystem/mii-cs-onko-systemische-therapie-protokolle
    value: "FOLFOX4"                     # MII protocol code

```

The MII binding is **experimental** until reviewed by the MII Onkologie maintainers. The mapping itself lives in `ConceptMap/mii-onko-protokoll-to-hemonc` (`status: draft`, `experimental: true`), with `equivalence: relatedto` reflecting that one MII code typically maps to multiple HemOnc variants.

When PHOENIX / ECCM publishes its own FHIR profiles and binds them to terminology, additional `use=secondary` identifiers can be added without disturbing canonical identity or HemOnc-derived versions.

#### Relationship to HL7 ballot cycles

PHOENIX / ECCM publishes on HL7 ballot cadence (typically annual). This IG publishes on HemOnc cadence (typically quarterly). The companion pattern is: each HL7-ballot snapshot of ECCM pins a specific version of this IG via `dependsOn`; mid-cycle HemOnc updates are visible to non-PHOENIX consumers immediately.

