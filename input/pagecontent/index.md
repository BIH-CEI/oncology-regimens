### HemOnc FHIR Regimen Catalog

A FHIR R4 projection of the [HemOnc Knowledge Base](https://hemonc.org) as
executable knowledge artifacts (`PlanDefinition`, `ActivityDefinition`,
`MedicationKnowledge`, `Library`, `CodeSystem`, `ConceptMap`).

This IG provides the **catalog layer** — *what to give* — that complements
the MII Onkologie Modul's **recording layer** — *what was given*. Together
they close the loop from registry-mandated reporting back to executable
clinical-decision support, anchored on a single, openly-licenced source of
truth for oncology regimens.

The IG is published in cooperation with **HemOnc.org**, the **OHDSI**
oncology community, **HL7 Europe PHOENIX**, and the **MII Onkologie**
working group. See [Cooperation, Attribution and Licensing](cooperation.html)
for the full provenance and governance story.

#### Status

This IG is `draft` / `experimental`. The Phase 0 spike (one regimen,
Carbo/Paclitaxel Variant #83) is validated end-to-end against the HAPI
FHIR Clinical Reasoning engine — see [the Phase 0 page](phase0.html).
Phase 1A (active + strongly-evidenced HemOnc regimens with experimental
MII Onkologie bindings) is in progress.

#### Read next

- [Background and Scope](background.html) — what this IG is and isn't
- [Cooperation, Attribution and Licensing](cooperation.html) — how the
  catalog is developed and which obligations travel with the content
- [Disclaimers and Intended Use](disclaimers.html) — **not a medical
  device; not intended for direct clinical use without validation**
- [Versioning Strategy](versioning.html) — how snapshots tie back to
  HemOnc and how MII / PHOENIX bindings co-evolve
- [`$apply` and CDS Hooks](apply-and-cds.html) — the runtime delivery
  model
- [Phase 0 Spike](phase0.html) — the end-to-end demonstration

#### Not a medical device

The artifacts in this distribution are reference content, not a medical
device or medical-device software under Regulation (EU) 2017/745 or
21 U.S.C. § 321(h). No CE marking or FDA clearance has been sought.
See [Disclaimers and Intended Use](disclaimers.html) for the full
intended-use statement.
