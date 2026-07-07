# Onboarding — HemOnc FHIR Regimen Catalog

**Projekt:** `oncology-regimens` (HemOnc FHIR Regimen Catalog)
**Kontext:** BIH / MII Onkologie / HL7 Europe **PHOENIX**
**Für:** Gastwissenschaftlerin, die den Katalog inhaltlich erarbeitet
**Betreuung:** Thomas Debertshäuser (BIH), Prof. Sylvia Thun (BIH)
**Status des Repos:** `draft` / `experimental` — Phase 0 (1 Regimen) fertig, Phase 1A beginnt
**Lizenz der Inhalte:** CC BY 4.0

> Dieses Dokument ist auf Deutsch geschrieben; der **IG-Inhalt selbst ist auf Englisch**
> (FHIR-Konvention). Eine englische Fassung dieses Onboardings kann bei Bedarf erstellt
> werden — einfach ansprechen.

---

## 1. Worum geht es? (Das Big Picture in 3 Minuten)

In der Onkologie gibt es viele FHIR-Projekte, die dokumentieren, **was einem Patienten
gegeben wurde** (mCODE, MII Onkologie, HL7-EU Cancer Common Model). Es gibt aber **keinen
FHIR-Katalog, der beschreibt, was man geben *soll*** — also die Therapieprotokolle selbst
als ausführbare, maschinenlesbare Wissensartefakte mit patientenindividueller Dosisberechnung.

Genau diese Lücke füllt dieses Projekt. Wir projizieren die **HemOnc-Wissensbasis**
(die kanonische Onkologie-Terminologie im OMOP-Datenmodell) in **ausführbare FHIR-R4-
Artefakte**. Das Drei-Ebenen-Modell:

```
   ┌──────────────────────────────────────────────┐
   │  Aufzeichnungs-Ebene (existiert bereits)      │  ← was gegeben wurde
   │   mCODE · MII Onkologie · HL7-EU ECCM         │
   │   (Procedure / MedicationStatement)           │
   └───────────────────┬──────────────────────────┘
                       │ instanziiert von
                       ▼
   ┌──────────────────────────────────────────────┐
   │  Katalog-Ebene  ← DIESES PROJEKT              │  ← was zu geben ist
   │   PlanDefinition (Regimen + Variante)         │
   │   ActivityDefinition (einzelne "sig")         │
   │   MedicationKnowledge (Wirkstoff + Klasse)    │
   │   Library (BSA-, Calvert-Dosisformeln, CQL)   │
   └───────────────────▲──────────────────────────┘
                       │ abgeleitet aus
   ┌──────────────────────────────────────────────┐
   │  Source of Truth                              │
   │   HemOncKB (CC BY 4.0, OMOP-kanonisch)         │
   │   + primäre Studienpublikationen              │
   └──────────────────────────────────────────────┘
```

**Zur Laufzeit** wird eine `PlanDefinition` über die FHIR-Operation `$apply` mit einem
Patientenkontext aufgerufen und erzeugt einen `CarePlan` mit konkreten, dosierten
`MedicationRequest`-Ressourcen (z. B. „Carboplatin 625 mg" nach Calvert-Formel).

### Der Kerngedanke der Identität

Die stabile Identität jeder `PlanDefinition` hängt am **HemOnc Regimen-CUI + Varianten-CUI**
(scharf, variantengenau). Der **deutsche MII-Onkologie-Protokollcode** wird nur als
*sekundärer, experimenteller* Identifier drangehängt. So ist der Katalog eine
**gleichrangige Companion-Ressource** zu MII Onkologie — nicht ihr untergeordnet — und
kann später ebenso an HL7-EU PHOENIX/ECCM oder andere Länder-Bindungen andocken.

---

## 2. Die Akteure & alle Links

### Quelldaten & Terminologie
| Ressource | Link | Rolle im Projekt |
|---|---|---|
| **HemOnc.org** (Wissensbasis) | https://hemonc.org | Inhaltliche Source of Truth (Regimen, sigs, Evidenz) |
| **HemOnc Dataverse** (Datendownload) | https://dataverse.harvard.edu/dataverse/hemonc | Quelle der `hemonckb-raw/`-Snapshots |
| **HemOnc-Publikation** (Warner et al. 2019) | https://pubmed.ncbi.nlm.nih.gov/31238109/ | Zitier- & Lizenzgrundlage (CC BY 4.0) |
| **OHDSI / OMOP Oncology** | https://www.ohdsi.org/ | HemOnc ist OMOP-kanonisch; Identitätsparität OMOP↔FHIR |
| **RxNorm** | https://www.nlm.nih.gov/research/umls/rxnorm/ | Wirkstoff-Coding in `MedicationKnowledge` |
| **ATC/WHO** | https://atcddd.fhi.no/atc_ddd_index/ | Wirkstoffklassifikation |
| **SNOMED CT** | https://www.snomed.org/ | Bedingungen/Wirkstoffe |
| **NCIt** | https://ncithesaurus.nci.nih.gov/ | Bedingungs-Mapping |

### Ziel-/Companion-Spezifikationen
| Ressource | Link | Rolle |
|---|---|---|
| **MII Onkologie Modul (2026)** | https://www.medizininformatik-initiative.de/Kerndatensatz/KDS_Onkologie_2026/MIIIGModulOnkologie.html | Aufzeichnungs-Ebene; liefert die 164 Protokollcodes (Dependency `2026.0.3`) |
| **HL7 Europe PHOENIX / Cancer Common Model (ECCM)** | https://build.fhir.org/ig/hl7-eu/cancer-common/ | EU-Patientendaten-Ebene; Alignment-Ziel |
| **mCODE** | https://build.fhir.org/ig/HL7/fhir-mCODE-ig/ | Verwandte US-Aufzeichnungs-Ebene (Vergleich) |
| **FHIR Clinical Reasoning ($apply)** | https://hl7.org/fhir/R4/plandefinition-operation-apply.html | Laufzeit-Mechanismus |
| **CQL (Clinical Quality Language)** | https://cql.hl7.org/ | Dosisberechnungs-Logik in `Library` |
| **cqf-fhir / HAPI Clinical Reasoning** | https://github.com/cqframework/clinical-reasoning | Engine für den Phase-0-Spike |
| **FHIR Shorthand (FSH) / SUSHI** | https://fshschool.org/ | Autoren-Werkzeug für FHIR-Ressourcen |
| **HL7 IG Publisher** | https://github.com/HL7/fhir-ig-publisher | Baut den IG (HTML) |

### Nachgelagerte Konsumenten (relevant für Kooperation)
| Ressource | Link | Rolle |
|---|---|---|
| **bzkf / obds-to-fhir** | https://github.com/bzkf/obds-to-fhir | Unmittelbarer Downstream-Konsument der Protokoll-Bindung |

---

## 3. Repository & lokales Setup

### Layout
```
oncology-regimens/
├── sushi-config.yaml                  ← IG-Metadaten
├── ig.ini                             ← IG-Publisher-Konfiguration
├── _genonce.sh / _updatePublisher.sh  ← Build-Helfer
├── input/
│   ├── pagecontent/                   ← IG-Erzähltexte (index, background, …)
│   ├── resources/                     ← handgeschriebene FHIR-R4-JSON-Artefakte
│   └── images/
├── phase0/                            ← End-to-End-Spike (1 Regimen, lauffähig)
│   ├── README.md                      ← Reproduktions-Rezept
│   ├── docker-compose.yml             ← HAPI + cqf-fhir auf :8096
│   ├── cql/                           ← CQL-Quelle (Dosisformeln)
│   ├── resources/                     ← Phase-0-JSON-Artefakte
│   ├── examples/                      ← Demo-Patient + Observations
│   └── scripts/load-and-apply.sh      ← Lade- + $apply-Round-Trip
├── docs/
│   ├── ONBOARDING.md                  ← dieses Dokument
│   └── HemOnc-FHIR-Catalog-Summary.pdf
└── hemonckb-raw/                      ← HemOnc-Dataverse-Snapshot (CSVs) → siehe §4
```

### IG bauen
```bash
npm install -g fsh-sushi        # einmalig
./_updatePublisher.sh           # einmalig, lädt den HL7 IG-Publisher-JAR
./_genonce.sh                   # baut den IG → output/index.html
```

### Phase-0-Spike lokal ausführen (empfohlener erster Lauf)
```bash
cd phase0
docker compose up -d            # HAPI + cqf-fhir auf http://localhost:8096
./scripts/load-and-apply.sh     # lädt Artefakte + ruft PlanDefinition/$apply
```
**Erwartetes Ergebnis:** ein `CarePlan` mit zwei `MedicationRequest`-Ressourcen —
**Carboplatin 625 mg** (Calvert AUC 5) und **Paclitaxel 323,75 mg** (175 mg/m² × 1,85 BSA) —
jeweils mit einem `computed-from-target-*`-Provenienz-Code. **Das einmal reproduziert zu
haben, ist das beste Onboarding in die Mechanik.**

### Werkzeuge, die du brauchst
- **git**, **Docker** (Compose), **Node.js/npm** (für SUSHI), **Python 3** (CSV-Verarbeitung)
- Java (für den IG-Publisher; wird vom Script geladen)
- Editor mit FHIR/FSH-Unterstützung (VS Code + „vscode-language-fsh")

---

## 4. Die Datensätze (`hemonckb-raw/`)

Alle CSVs sind ein **HemOnc-Dataverse-Snapshot vom 12.03.2026** (Concept-Relationship-Datei
09.04.2026). Es gibt **zwei Schichten**:

**(A) OMOP-„stage"-Dateien** — HemOnc als OMOP-Vokabular (groß, generisch):

| Datei | Zeilen | Schlüsselspalten | Bedeutung |
|---|---|---|---|
| `…concept_stage.csv` | ~130 300 | `concept_id, concept_name, domain_id, vocabulary_id, concept_class_id, standard_concept, concept_code, valid_start_date, valid_end_date, invalid_reason` | Alle HemOnc-Konzepte (Drug, Regimen, Regimen Variant, Condition …). `concept_code` = **HemOnc CUI**. |
| `…concept_synonym_stage.csv` | ~159 500 | `synonym_concept_id, synonym_name, synonym_concept_code, …` | Synonyme (wichtig fürs Matching von Akronymen/Handelsnamen). |
| `…concept_relationship_stage.csv` | ~511 800 | `concept_id_1, concept_id_2, relationship_id, …` | Beziehungen: Regimen „has component" Drug, Regimen „has variant" Variant usw. |

**(B) Kuratierte „additional_tables"** — menschenlesbar, das inhaltliche Herzstück:

| Datei | Zeilen | Wichtigste Spalten | Wozu wir sie brauchen |
|---|---|---|---|
| `Tables/regimens.csv` | ~2 795 | `regimen_name, regimen_cui, regimen_type, sact, sact_modalities, components, studies, highest_evidence, first_studied, last_published, variant.count` | **Zentraler Regimen-Katalog.** Basis fürs MII↔HemOnc-Matching und die `PlanDefinition`-Identität. `highest_evidence` + `last_published` steuern den Phase-1A-Filter. |
| `Tables/variants.csv` | ~27 400 | `regimen_cui, variant, variant_cui, portions, components, timings, branches, sigs, routes, allSIGsHave*`-Flags | **Regimen-Varianten** (studienspezifische Dosierschemata). `variant_cui` verankert die `PlanDefinition`. Die `allSIGsHave*`-Flags zeigen Datenvollständigkeit (Dose/Unit/Route/Schedule …). |
| `Tables/sigs.csv` | ~24 555 | `regimen_cui, variant_cui, component, component_cui, component_role, cycle_length_lb/ub/unit, timing_sequence, timing, branch, step_number` | **Atomare Dosieranweisungen** („gib Wirkstoff X in Dosis Y an Schema Z"). Quelle für die `ActivityDefinition`s. `component_role` unterscheidet Primär- von Begleit-/Prämedikation. |
| `Tables/drugs.csv` | ~874 | `drug, drug_CUI, drug_INN, atc, investigational, multiagent, main_class, class_type, CanMED_major_class(_CUI), CanMED_minor_class(_CUI)` | **Wirkstoff-Wörterbuch** → `MedicationKnowledge`. Enthält **ATC** + INN + Klassenzuordnung. |
| `Mapping/rxnorm_map.csv` | ~902 | `parent, code, hemonc_preferred_rxnorm, rxnorm_type, IN_rxnorm, …` | HemOnc-Drug → **RxNorm**-Mapping für `MedicationKnowledge.code`. |
| `Tables/conditions.csv` | ~319 | `condition, condition_cui, map_NCIT, map_SNOMED, map_OncoTree, map_ICD10CM, map_ICDO3 …` | Indikations-/Diagnose-Konzepte mit Mappings (NCIt, SNOMED, ICD-10, ICD-O-3). |
| `Tables/indications.csv` | ~3 550 | `component, component_cui, regulator, date, condition, accelerated, withdrawn, prior_therapy, …` | Regulatorische Zulassungs-Indikationen (FDA/EMA), inkl. Vortherapie-Kriterien. |
| `Tables/variant_eligibility.csv` | ~635 | `regimen_cui, variant_cui, string, type, logic, unit, logic_count` | Einschluss-/Ausschluss-Kriterien pro Variante (für Studien-Matching/CDS). |
| `Tables/studies.csv` | ~7 698 | `study, study_cui, registry, trial_id, condition, phase, study_arms, sact, start, end, sponsor` | Klinische Studien (Evidenzkontext der Regimen). |
| `Tables/study_results.csv` | ~14 728 | `study_cui, regimen_cui, comparator, efficacy, toxicity, endpoint, endpoint_class, arm_type, metric` | Wirksamkeits-/Toxizitäts-Ergebnisse. |
| `Tables/refs.csv` | ~11 260 | `study_cui, reference_cui, title, pmid, doi, url, journal, pub.date` | Referenzen/Publikationen (für `relatedArtifact[derived-from]`). |
| `Tables/hemonc_classes.csv` | ~149 | `description, domain, OMOP.domain_id, class_type, concept_class_id, …` | Klassen-Metadaten / OMOP-Domänen-Zuordnung. |
| `Tables/hemonc_rels.csv` | ~96 | `relationship_id, description, heritable, …` | Definition der Beziehungstypen. |
| `Tables/inclusions.csv` / `exclusions.csv` | ~10 500 / ~18 200 | `pmid, reason, …` | Kuratierungs-Nachweis (welche PMIDs ein-/ausgeschlossen). Für uns i. d. R. nicht relevant. |
| `Tables/authors.csv` / `persons.csv` | ~180 000 / ~53 500 | Autor-/Personendaten | Bibliometrie; **für dieses Projekt nicht relevant**. |
| `Tables/pointers.csv`, `canonical.triples.csv` | ~21 900 / ~221 | Navigations-/Klassen-Tripel | HemOnc-interne Struktur; Randbedarf. |

**Referenz-/Doku-Dateien im selben Ordner:**
- `data.dictionary.xlsx` — **offizielles Data Dictionary** (Spaltendefinitionen). Bei Unklarheit zu einer Spalte: hier zuerst nachschlagen.
- `HemOncKB README.pdf` (v2.1) — Überblick über die Wissensbasis.
- `…whats_new.xlsx` — Changelog des Snapshots.

> **Wichtig:** CUI = „Concept Unique Identifier" (HemOnc-intern, stabil). Regimen-CUI und
> Varianten-CUI sind die Anker unserer FHIR-Identität — siehe §7.

---

## 5. Was wir bauen (FHIR-Artefakt-Architektur)

Pro Regimen-Variante entsteht ein kleiner Satz zusammenhängender Ressourcen:

| Artefakt | 1 pro… | Quelle | Inhalt |
|---|---|---|---|
| `PlanDefinition` | Regimen-Variante | `variants.csv` + `sigs.csv` | Der ausführbare Protokoll-Baum (Zyklen, Aktionen, Timing). Identität = Regimen-CUI + Varianten-CUI. |
| `ActivityDefinition` | „sig" (Einzelgabe) | `sigs.csv` | „Gib Wirkstoff X, Dosis Y (z. B. 175 mg/m²), Route, Schema". |
| `MedicationKnowledge` | Wirkstoff | `drugs.csv` + `rxnorm_map.csv` | Wirkstoff mit ATC + RxNorm + HemOnc-CUI-Codings, Klassenzuordnung. |
| `Library` | Katalog (wenige) | `phase0/cql/` | CQL/FHIRPath-Dosisformeln: BSA (Mosteller/Du Bois/Haycock), Cockcroft-Gault-GFR, Calvert. |
| `CodeSystem` / `ValueSet` | Katalog | `concept_stage.csv` | HemOnc-Konzept-Fragment + kleines `sig-target-type`-Vokabular. |
| `ConceptMap` | Bridge | Matching-Ergebnis | `mii-onko-protokoll-to-hemonc` (MII-Code → HemOnc-CUI), `status=draft, experimental=true`. |

Profile werden **nur dort** geschrieben, wo der IG eine tragende Entscheidung trifft;
alles andere nutzt Basis-R4. **Nicht** im Scope: Per-Patient-Profile (→ mCODE/MII/ECCM),
`MedicationDispense` (Apothekenbetrieb), Dosis-Banding/Hold-for-Counts/Dosis-Modifikation
(Standort-Policy, spätere Libraries), PZN-Auflösung, NCCN-/AWMF-Inhalte.

---

## 6. Anforderungsbeschreibung — Arbeitspaket Phase 1A

**Ziel:** Aus dem End-to-End-Beweis (Phase 0, 1 Regimen) einen ersten inhaltlich
sinnvollen Katalog machen: die **starke-Evidenz-Schnittmenge zwischen den deutschen
MII-Onkologie-Protokollcodes und HemOnc**.

### 6.1 Eingaben
- **MII-Seite:** `mii-cs-onko-systemische-therapie-protokolle` **v2026.0.3** — **164 Codes**
  (deutsche Krebsregister-Protokollcodes; Dependency des IG).
- **HemOnc-Seite:** `regimens.csv` (~2 794 Regimen), **gefiltert** auf
  `highest_evidence = 'Phase 3 RCT'` **UND** `last_published ≥ 2011` (~1 597 Kandidaten).

### 6.2 Arbeitsschritte (Deliverables)

1. **Matching MII ↔ HemOnc** *(bd: `interop-prototypes-o23`, `interop-prototypes-xx7`)*
   Matche die 164 MII-Codes gegen die HemOnc-Kandidaten mit drei Strategien:
   - (a) **Akronym-Match** im HemOnc-`regimen_name`-Klammerzusatz
     (z. B. „Carboplatin and Paclitaxel (CP)" → `CP`).
   - (b) **Kuratierte Synonymliste** für deutsche Varianten
     (z. B. `BEACOPP-basis` vs. `-eskaliert`, AIO-Studiencodes).
   - (c) **Sub-Code-Disambiguierung** auf Variantenebene
     (z. B. `FOLFOX4` → konkrete HemOnc-`variant_cui`).

   **Output:** `matches.csv`, `ambiguous.csv`, `unmatched.csv`.
   `matches.csv`-Spalten: `mii_code, mii_display, hemonc_regimen_name,
   hemonc_regimen_cui, recommended_variant_cui, match_method, confidence`.

2. **Artefakt-Generierung** *(bd: `interop-prototypes-d47`)*
   Für jeden **gematchten** Protokollcode:
   - 1 `PlanDefinition` (Regimen + empfohlene Variante),
   - je `ActivityDefinition` pro sig,
   - `MedicationKnowledge` pro beteiligtem Wirkstoff.
   Für **ungematchte** Codes: Stub-`PlanDefinition` mit `status=draft`.

3. **Bridge-ConceptMap** *(bd: `interop-prototypes-lzf`)*
   `mii-onko-protokoll-to-hemonc`, `status=draft`, `experimental=true`,
   `equivalence=relatedto` (ein MII-Code → oft mehrere HemOnc-Varianten).
   Erst nach expliziter Abstimmung mit den MII-Onkologie-Maintainern auf `active`.

4. **IG-Integration & Build**
   Artefakte nach `input/resources/` (bzw. FSH → SUSHI), IG bauen (`./_genonce.sh`),
   gegen den FHIR-R4-Validator prüfen, mindestens 1–2 neue Regimen zusätzlich zum
   Phase-0-Beispiel end-to-end via `$apply` verifizieren.

### 6.3 Definition of Done (Phase 1A)
- [ ] `matches.csv` / `ambiguous.csv` / `unmatched.csv` liegen versioniert im Repo.
- [ ] Für alle Matches existieren valide `PlanDefinition` + `ActivityDefinition` +
      `MedicationKnowledge` (R4-validator-clean).
- [ ] `mii-onko-protokoll-to-hemonc` ConceptMap generiert (draft/experimental).
- [ ] IG baut ohne Fehler; mindestens ein neues Regimen läuft via `$apply` durch.
- [ ] Jede `PlanDefinition` trägt `relatedArtifact[derived-from]` auf die HemOnc-Quellzeile.
- [ ] Identifier-Muster eingehalten (§7): `official` = HemOnc-CUI, `secondary` = MII-Code.

### 6.4 Spätere Phasen (Kontext, **nicht** Teil von 1A)
- **Phase 1B/2:** pan-europäische Abdeckung, PHOENIX/ECCM-Bindung *(bd `interop-prototypes-5d9`, `-5vv`)*.
- **Post-Phase-0-Libraries:** Dosis-Banding `-ohv`, Hold-for-Counts `-9au`,
  Dosis-Modifikation `-qbt`.

> **Aufgabenverwaltung:** Das Repo nutzt **Beads (`bd`)**. `bd ready` zeigt verfügbare
> Arbeit, `bd show <id>` die Details. Die oben referenzierten IDs sind die maßgeblichen
> Arbeitspakete. Bitte **keine** parallele TODO-Liste führen — alles in `bd`.

---

## 7. Konventionen (verbindlich)

### Canonical-URL-Schema (stabil über Releases)
```
http://hemonc.org/fhir/<ResourceType>/<stable-id>
```
- `CodeSystem/hemonc`, `CodeSystem/sig-target-type`
- `MedicationKnowledge/hemonc-drug-<CUI>-<inn>`
- `ActivityDefinition/sig-<component>-<dose>-<schedule>`
- `PlanDefinition/regimen-<regimen_cui>-variant-<variant_cui>`
- `Library/hemonc-dose-helpers`

Canonicals ändern sich **nie** nach Erstvergabe. Konsumenten pinnen Canonical + Version.

### Versionierung
- **`Resource.version` = HemOnc-Snapshot-Datum** im Format `YYYY-MM-DD` (z. B. `2026-03-12`).
  Neuer HemOnc-Snapshot (quartalsweise) → neue `version` gegen dieselbe Canonical.
- `Resource.date` = gleicher Snapshot-Zeitstempel.
- `Resource.status`: `active`, solange HemOncs `date_deprecated` leer ist; sonst `retired`.
- `Resource.effectivePeriod` = `date_added` … `date_deprecated` (HemOnc-Lebenszeit explizit).

### Identifier-Muster auf `PlanDefinition`
```yaml
identifier:
  - use: official                       # scharfe HemOnc-Identität
    system: http://hemonc.org/cui
    value: "18203"                       # Regimen-CUI
  - use: secondary
    system: http://hemonc.org/variant-cui
    value: "144530"                      # Varianten-CUI
  - use: secondary                       # experimentelle MII-Bindung
    system: https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/CodeSystem/mii-cs-onko-systemische-therapie-protokolle
    value: "FOLFOX4"
```

### Kooperations-Verpflichtungen (operativ, nicht bloß rhetorisch)
1. **Versions-Gleichschritt mit HemOnc** — jede IG-Version trägt das HemOnc-Snapshot-Datum;
   neuer Snapshot → neue IG-Version innerhalb ≤ 4 Wochen.
2. **Upstream-Feedback** — FHIR-entdeckte Inkonsistenzen in HemOnc werden als
   HemOnc-Dataverse-/Repo-Issues gemeldet, **nicht** lokal stillschweigend gefixt.
3. **OMOP-Round-Trip** — HemOnc-CUI (= OMOP `concept_code`) bleibt als `secondary`
   Identifier erhalten, damit OMOP↔FHIR ohne URL-Parsing rückführbar ist.

---

## 8. Governance, Lizenz, Haftung (bitte lesen)

- **Lizenz:** HemOnc-Inhalte stehen unter **CC BY 4.0** (Warner et al. 2019). Dieser IG
  übernimmt sie. **Attribution muss in jeder Weiterverwendung erhalten bleiben.**
- **Nicht abgeleitet** von NCCN Guidelines®, NCCN Compendium®, NCCN Order Templates™ oder
  **AWMF S3-Leitlinien.** Inhalte stammen aus HemOncKB, primären Studienpublikationen und
  Fachinformationen. NCCN/AWMF sind Marken der jeweiligen Inhaber — **nicht** referenzieren
  oder ableiten.
- **Kein Medizinprodukt.** Die Artefakte sind Referenzinhalte, **kein** MDSW nach
  Verordnung (EU) 2017/745 bzw. 21 U.S.C. § 321(h). Kein CE-/FDA-Status.
- **Keine klinische Nutzung** ohne unabhängige Validierung durch Fachpersonal.
- **Sandbox-Software:** die HAPI/cqf-fhir-Container sind unauthentifiziert, ohne Audit-Trail
  (§75c SGB V, DSGVO Art. 32, 21 CFR Part 11) — **niemals** mit echten Patientendaten
  betreiben. Details: `input/pagecontent/disclaimers.md`.

---

## 9. Glossar

| Begriff | Bedeutung |
|---|---|
| **HemOnc / HemOncKB** | Offene onkologische Wissensbasis (Regimen, sigs, Evidenz), OMOP-kanonisch, CC BY 4.0 |
| **CUI** | **Concept Unique Identifier** — eindeutige, **stabile** numerische ID für ein HemOnc-Konzept (Wirkstoff, Regimen, Variante, Diagnose …). Ändert sich nie, auch wenn der *Name* sich ändert. In der OMOP-`concept_stage.csv` = Spalte `concept_code` (⇒ HemOnc-CUI = OMOP `concept_code`, Basis des OMOP↔FHIR-Round-Trips). Beispiele: Regimen `2554` (Carbo/Paclitaxel), Variante `144842`. Anker unserer FHIR-Identität (Canonical-URL + `official`-Identifier). Begriff stammt aus dem UMLS (`C0004238`), HemOnc nutzt aber **eigene** numerische CUIs — nicht die UMLS-Codes. |
| **Regimen** | Benanntes Therapieprotokoll (z. B. FOLFOX, R-CHOP) |
| **Variante (variant)** | Studienspezifisches Dosierschema eines Regimens |
| **sig** | Einzelne Dosieranweisung („gib Wirkstoff X, Dosis Y, Schema Z") |
| **OMOP** | Common Data Model der Beobachtungsforschung (OHDSI) |
| **MII Onkologie** | Kerndatensatz-Modul Onkologie der Medizininformatik-Initiative (DE) |
| **PHOENIX / ECCM** | HL7-Europe-Initiative bzw. European Cancer Common Model (EHDS-Kontext) |
| **PlanDefinition / ActivityDefinition** | FHIR-Wissensressourcen für Protokoll bzw. Einzelaktion |
| **$apply** | FHIR-Operation: PlanDefinition + Patient → CarePlan mit konkreten Orders |
| **CQL** | Clinical Quality Language — Logiksprache für Dosisberechnung |
| **BSA / Calvert / GFR** | Körperoberfläche / Carboplatin-Dosisformel / Nierenfunktion |
| **FSH / SUSHI** | FHIR Shorthand bzw. dessen Compiler |
| **bd (Beads)** | Git-gestütztes Issue-Tracking dieses Projekts |

---

## 10. Erste Schritte — Checkliste Woche 1

1. [ ] Repo klonen, `docs/ONBOARDING.md` (dieses Dokument) und die IG-Seiten unter
       `input/pagecontent/` lesen (`background.md`, `versioning.md`, `cooperation.md`).
2. [ ] **Phase-0-Spike lokal reproduzieren** (§3) — CarePlan mit Carbo 625 mg + Paclitaxel
       323,75 mg erzeugen. Das erklärt die Mechanik besser als jeder Text.
3. [ ] `HemOncKB README.pdf` + `data.dictionary.xlsx` überfliegen; in `regimens.csv`,
       `variants.csv`, `sigs.csv`, `drugs.csv` hineinsehen.
4. [ ] `bd ready` / `bd show interop-prototypes-o23` — mit dem Matching (Schritt 6.2.1)
       beginnen: den Phase-1A-Kandidatenfilter (`Phase 3 RCT`, `last_published ≥ 2011`)
       auf `regimens.csv` anwenden und den Akronym-Match gegen die 164 MII-Codes prototypen.
5. [ ] Fragen sammeln → mit Thomas besprechen (MII-Zugang, Synonymliste, Grenzfälle).

**Fragen jederzeit an Thomas Debertshäuser.** Willkommen im Team! 🎗️
