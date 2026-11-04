# European SACT Regimen Catalog

A FHIR R4 Implementation Guide that represents systemic anti-cancer therapy
(SACT) regimens as executable knowledge artifacts (`PlanDefinition`,
`ActivityDefinition`, `MedicationKnowledge`, `Library`, `CodeSystem`,
`ConceptMap`). Catalog-layer companion to the
[HL7 Europe PHOENIX Cancer Common Model](https://build.fhir.org/ig/hl7-eu/cancer-common/)
and the
[MII Onkologie](https://www.medizininformatik-initiative.de/Kerndatensatz/KDS_Onkologie_2026/MIIIGModulOnkologie.html)
module. First content source: the [HemOnc Knowledge Base](https://hemonc.org).

Developed in cooperation with **HemOnc.org**, the **OHDSI** oncology
community, **HL7-EU PHOENIX**, and the **MII Onkologie** working group.
Content licensed under **CC BY 4.0**.

> **Status: draft / experimental.** Not a medical device. Not for clinical
> use without independent validation. See [DISCLAIMERS](input/pagecontent/disclaimers.md).

---

## Repository layout

```
oncology-regimens/
├── sushi-config.yaml                  ← IG metadata
├── ig.ini                             ← IG-Publisher config
├── _genonce.sh / _updatePublisher.sh  ← build helpers
├── input/
│   ├── pagecontent/                   ← IG narrative pages
│   ├── resources/                     ← hand-authored FHIR R4 JSON
│   └── images/
├── phase0/                            ← end-to-end spike
│   ├── README.md                      ← reproduction recipe
│   ├── docker-compose.yml             ← HAPI + cqf-fhir on :8096
│   ├── cql/                           ← CQL source
│   ├── resources/                     ← phase 0 hand-authored JSON
│   ├── examples/                      ← demo Patient + Observations
│   └── scripts/load-and-apply.sh      ← load + $apply round-trip
└── hemonckb-raw/                      ← HemOnc Dataverse snapshot (CSVs)
```

## Building the IG

```bash
npm install -g fsh-sushi          # one-time
./_updatePublisher.sh             # one-time, downloads HL7 IG-Publisher jar
./_genonce.sh                     # builds the IG → output/index.html
```

## Running the Phase 0 spike

```bash
cd phase0
docker compose up -d              # HAPI + cqf-fhir on http://localhost:8096
./scripts/load-and-apply.sh       # load artefacts + run PlanDefinition/$apply
```

Expected output: a CarePlan with two contained MedicationRequests —
**Carboplatin 625 mg** (Calvert AUC 5) and **Paclitaxel 323.75 mg**
(175 mg/m² × 1.85 BSA) — each tagged with a `computed-from-target-*`
provenance code.

## Continuous integration

Two GitHub Actions workflows (`.github/workflows/`) build the IG with SUSHI +
the HL7 IG Publisher:

- **`build-ig.yml`** — on **push to `main`** the built IG is published to the
  `gh-pages` **root** (→ https://bih-cei.github.io/oncology-regimens/). On
  **every pull request** a parallel IG is built and deployed under
  `preview/pr-<N>/`, and the preview URL is posted as a PR comment.
- **`cleanup-preview.yml`** — removes the `preview/pr-<N>/` subtree when the PR
  is closed.

The build tolerates FHIR validation errors (this IG is `draft`/`experimental`);
see the uploaded `qa-report` artifact and `qa.html` for details. Preview deploys
require the PR branch to live in this repo (fork PRs get a read-only token).

## Cooperation and attribution

See [`input/pagecontent/cooperation.md`](input/pagecontent/cooperation.md)
for the full provenance, governance and licensing story, including the
explicit non-derivation from NCCN Guidelines® and AWMF S3-Leitlinien.

## Issue tracking

This project uses [`bd` (beads)](https://github.com/beads-issue-tracker)
for issue tracking; see `.beads/` in the parent repo. Run `bd ready`
for available work.
