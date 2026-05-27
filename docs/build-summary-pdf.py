#!/usr/bin/env python3
"""Build docs/HemOnc-FHIR-Catalog-Summary.pdf.

Hand-authored landscape-A4 summary of the project: what HemOnc's additional
tables add beyond the OMOP core, with two worked examples — FOLFOX4
(HemOnc regimen CUI 13829) and the chemo + targeted-kinase-inhibitor
combination mFOLFOX6 + Lenvatinib + Pembrolizumab (HemOnc cui 28874).

The committed PDF is a build artefact; this script is the source of truth.
Run from the project root:

    python3 docs/build-summary-pdf.py
"""
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
)
from datetime import date
import pathlib

OUT = pathlib.Path(__file__).parent / "HemOnc-FHIR-Catalog-Summary.pdf"
PAGE = landscape(A4)  # 29.7 cm × 21 cm

# ── Page footer ─────────────────────────────────────────────────────────────
def footer(canv, doc):
    canv.saveState()
    canv.setFont("Helvetica", 8)
    canv.setFillColor(colors.HexColor("#666666"))
    canv.drawString(
        2 * cm, 1.0 * cm,
        "HemOnc FHIR Regimen Catalog — Summary (draft / experimental)")
    canv.drawRightString(PAGE[0] - 2 * cm, 1.0 * cm, f"Page {doc.page}")
    canv.restoreState()


# ── Styles ──────────────────────────────────────────────────────────────────
ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=ss["Heading1"], fontName="Helvetica-Bold",
                    fontSize=18, leading=22, spaceBefore=14, spaceAfter=10,
                    textColor=colors.HexColor("#1f3a5f"))
H2 = ParagraphStyle("H2", parent=ss["Heading2"], fontName="Helvetica-Bold",
                    fontSize=13, leading=16, spaceBefore=14, spaceAfter=6,
                    textColor=colors.HexColor("#1f3a5f"))
H3 = ParagraphStyle("H3", parent=ss["Heading3"], fontName="Helvetica-Bold",
                    fontSize=11, leading=14, spaceBefore=8, spaceAfter=4,
                    textColor=colors.HexColor("#3a4f6f"))
BODY = ParagraphStyle("BODY", parent=ss["BodyText"], fontName="Helvetica",
                    fontSize=10, leading=14, alignment=TA_JUSTIFY, spaceAfter=6)
SMALL = ParagraphStyle("SMALL", parent=BODY, fontSize=8.5, leading=11,
                    textColor=colors.HexColor("#555555"))
CAPTION = ParagraphStyle("CAPTION", parent=BODY, fontSize=8.5, leading=11,
                    textColor=colors.HexColor("#666666"),
                    alignment=TA_LEFT, spaceAfter=10)
TITLE = ParagraphStyle("TITLE", parent=ss["Title"], fontName="Helvetica-Bold",
                    fontSize=28, leading=34, alignment=TA_CENTER,
                    textColor=colors.HexColor("#1f3a5f"), spaceAfter=10)
SUBT = ParagraphStyle("SUBT", parent=ss["Normal"], fontName="Helvetica",
                    fontSize=13, leading=17, alignment=TA_CENTER,
                    textColor=colors.HexColor("#3a4f6f"), spaceAfter=4)
CELL = ParagraphStyle("CELL", parent=ss["Normal"], fontName="Helvetica",
                    fontSize=9, leading=12, alignment=TA_LEFT, spaceAfter=0)
CELLH = ParagraphStyle("CELLH", parent=CELL, fontName="Helvetica-Bold")


def P(text, style=CELL):
    """Wrap a string in a Paragraph so table cells reflow at column width."""
    return Paragraph(text, style)


def tbl(header, rows, col_widths):
    data = [[P(h, CELLH) for h in header]]
    for r in rows:
        data.append(
            [c if hasattr(c, "wrap") else P(str(c), CELL) for c in r])
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("VALIGN",         (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING",    (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",   (0, 0), (-1, -1), 5),
        ("TOPPADDING",     (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 4),
        ("BACKGROUND",     (0, 0), (-1,  0), colors.HexColor("#e8eef6")),
        ("LINEBELOW",      (0, 0), (-1,  0), 0.5, colors.HexColor("#1f3a5f")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [colors.white, colors.HexColor("#f7f9fc")]),
    ]))
    return t


# ── Content groups ──────────────────────────────────────────────────────────
GROUPS = [
    ("Executable protocol content", "the heart of the catalogue", [
        ("regimens",              "2 794",
         "Regimen-family metadata: type, modality, component count, study count, "
         "highest evidence, first studied year, last published date"),
        ("variants",             "27 393",
         "Per-(study, regimen, variant) full encoding of the dosing protocol. "
         "Self-contained — no diffs, no inheritance"),
        ("sigs",                 "24 555",
         "Atomic dosing unit: drug, dose (mg/m², AUC, mg/kg), route, day pattern, "
         "frequency, cycle length, infusion duration, role, relative sequencing"),
        ("variant_eligibility",     "635",
         "Dose-eligibility criteria: age, weight, lab thresholds"),
    ]),
    ("Drug knowledge", "beyond a code list", [
        ("drugs",                   "873",
         "INN, ATC, main_class (Platinum agent, Taxane, Anti-PD-1, …), CanMED "
         "axis, investigational + multi-agent flags"),
        ("rxnorm_map",              "901",
         "HemOnc ↔ RxNorm crosswalk with semantic type (IN, SCD, …)"),
        ("indications",           "3 549",
         "FDA/EMA approvals by condition: date, accelerated, withdrawn, biomarker, "
         "prior-therapy, demographics, narrative reason"),
    ]),
    ("Disease conditions", "with eight crosswalks", [
        ("conditions",              "318",
         "HemOnc disease concepts with mappings to NCIt, SNOMED CT, OncoTree, "
         "ICD-9-CM, ICD-10-CM, ICD-O-3, ICD-O-3 morphology, SEER"),
    ]),
    ("Evidence base", "the EBM backbone", [
        ("studies",               "7 697",
         "Clinical trials: registry (CT.gov, EudraCT, …), trial ID, condition, "
         "biomarker, enrolment, phase, arms, design, sponsor, group"),
        ("study_results",        "14 727",
         "RCT endpoints with HR/OR/RR, CI bounds, p-values, comparator code, "
         "landmark — maps to FHIR EffectEvidenceSynthesis"),
        ("refs",                 "11 259",
         "Publications: PMID, DOI, PMCID, title, journal, biblio, pub-date, "
         "ref type, errata, citation count"),
        ("authors",             "180 345",
         "Per-publication author records with order, role, affiliation"),
        ("persons",              "53 545",
         "Per-author rollup, normalized across publications"),
    ]),
    ("Curation transparency", "the epistemic honesty layer", [
        ("inclusions",           "10 494",
         "Publications HemOnc accepted with the reason (criteria-driven or "
         "SOP-exception)"),
        ("exclusions",           "18 198",
         "Publications HemOnc reviewed and rejected with the reason — bigger "
         "than inclusions, by design"),
    ]),
    ("Wiki linkage and schema-meta", "supporting structure", [
        ("pointers",             "21 935",
         "Versioned URL backlinks to the HemOnc.org wiki Table-of-Contents "
         "(narrative explanations, dose-modification rules)"),
        ("hemonc_classes",          "148", "Concept class definitions"),
        ("hemonc_rels",              "95", "Relationship type definitions"),
        ("canonical.triples",       "220",
         "Allowed (class₁ — relationship — class₂) combinations — the schema "
         "constraint"),
    ]),
]


def build():
    doc = SimpleDocTemplate(
        str(OUT), pagesize=PAGE,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=1.8 * cm, bottomMargin=1.6 * cm,
        title="HemOnc FHIR Regimen Catalog — Summary",
        author="HemOnc FHIR Catalog Working Group",
    )

    story = []

    # Title page
    story += [
        Spacer(1, 3 * cm),
        Paragraph("HemOnc FHIR Regimen Catalog", TITLE),
        Paragraph(
            "Executable Knowledge Layer for Oncology Treatment Protocols",
            SUBT),
        Spacer(1, 0.5 * cm),
        Paragraph(
            "Beyond OMOP: what HemOnc’s additional tables add — with worked "
            "examples for FOLFOX4 and a chemo + targeted kinase inhibitor "
            "combination", SUBT),
        Spacer(1, 1.5 * cm),
        Paragraph(f"Draft / experimental — {date.today().isoformat()}", SUBT),
        Spacer(1, 0.4 * cm),
        Paragraph(
            "Developed in cooperation with HemOnc.org · OHDSI Oncology · "
            "HL7 Europe PHOENIX · MII Onkologie Working Group", SUBT),
        Spacer(1, 2.5 * cm),
        Paragraph(
            "<i>Not a medical device. Not for clinical use without "
            "independent validation.</i>", SMALL),
        PageBreak(),
    ]

    # ── Section 1
    story += [
        Paragraph("1. Two layers of HemOnc, only one of them widely known", H1),
        Paragraph(
            "The HemOnc Knowledge Base (HemOncKB) is the canonical oncology "
            "vocabulary in the OMOP Common Data Model, distributed via "
            "Athena/OHDSI since 2019 (Warner JL et al., "
            "<i>J Biomed Inform</i>). What most consumers see is the "
            "OMOP-format core: three flat triple-shaped tables that list "
            "concepts, relationships and synonyms. Useful, but intentionally "
            "limited — OMOP triples cannot represent dosing schedules, "
            "target-AUC computations, multi-component protocols, or "
            "evidence-graph relationships. Those live in the eighteen "
            "<b>additional tables</b> that ship alongside the OMOP core and "
            "that, until now, have not had a structured machine-readable "
            "consumer interface. This IG is that consumer interface.",
            BODY),
        Spacer(1, 0.3 * cm),
        Paragraph("Two layers, two consumers", H3),
        tbl(
            ["Layer", "Tables", "Rows (snapshot 2026-03-12)",
             "Typical consumer"],
            [
                ["OMOP core",
                 "concept_stage, concept_relationship_stage, "
                 "concept_synonym_stage",
                 "~800 k",
                 "OHDSI research sites, observational analytics"],
                ["Additional tables",
                 "18 tables across 6 functional groups",
                 "~310 k",
                 "This IG — clinical-ordering, CDS, evidence linkage"],
            ],
            col_widths=[3.4 * cm, 8.6 * cm, 4 * cm, 9.5 * cm],
        ),
        PageBreak(),
    ]

    # ── Section 2: groups
    story += [
        Paragraph(
            "2. What the additional tables carry, organized by purpose", H1),
        Paragraph(
            "The 18 additional tables group into six functional clusters. "
            "Together they carry the content that makes HemOnc clinically "
            "actionable — not just terminology, but executable protocols "
            "with full provenance.", BODY),
    ]
    for title_, subtitle, rows in GROUPS:
        story.append(Paragraph(f"{title_} — <i>{subtitle}</i>", H2))
        story.append(tbl(
            ["Table", "Rows", "Adds"], rows,
            col_widths=[4 * cm, 2 * cm, 19.5 * cm]))
        story.append(Spacer(1, 0.2 * cm))
    story.append(PageBreak())

    # ── Section 3: FOLFOX4
    story += [
        Paragraph("3. Worked example — FOLFOX4", H1),
        Paragraph(
            "FOLFOX4 is the canonical first-line systemic therapy for "
            "metastatic colorectal cancer and the prototype of bi-weekly "
            "cytotoxic combinations. It is in the MII Onkologie protocol "
            "code list as <font face='Courier'>FOLFOX4</font> and in HemOnc "
            "as regimen CUI 13829 with 5 variants across 28 studies. First "
            "studied 1995, last published 2024-11-15. <i>Phase 3 RCT</i> "
            "evidence level.", BODY),
        Spacer(1, 0.2 * cm),
        Paragraph("3.1 Regimen-level metadata", H2),
        tbl(
            ["Field", "Value"],
            [
                ["regimen_name",       "FOLFOX4"],
                ["regimen_cui",        "13829"],
                ["regimen_type",       "Component-based regimen"],
                ["MII protocol code",
                 P("<font face='Courier'>FOLFOX4</font> from "
                   "<font face='Courier'>mii-cs-onko-systemische-therapie-"
                   "protokolle</font> v2026.0.3", CELL)],
                ["sact",               "TRUE (systemic anticancer therapy)"],
                ["components",
                 "3 — Fluorouracil + Leucovorin + Oxaliplatin"],
                ["studies",            "28"],
                ["variants",           "5"],
                ["highest_evidence",   "Phase 3 RCT"],
                ["first_studied",      "1995"],
                ["last_published",     "2024-11-15"],
            ],
            col_widths=[5 * cm, 20.5 * cm],
        ),
        Spacer(1, 0.3 * cm),
        Paragraph(
            "3.2 Per-component sigs (canonical variant 132249, q14d cycle)",
            H2),
        tbl(
            ["Component", "Dose", "Route", "Day", "Frequency",
             "Duration", "Step"],
            [
                ["Fluorouracil", "400 mg/m²",  "IV", "1, 2", "once per day",
                 "1 min", "1 of 2 (bolus)"],
                ["Fluorouracil", "600 mg/m²",  "IV", "1, 2", "continuous",
                 "22 h",  "2 of 2 (CI)"],
                ["Leucovorin",   "200 mg/m²",  "IV", "1, 2", "once per day",
                 "2 h",   "1 of 1"],
                ["Oxaliplatin",  "85 mg/m²",   "IV", "1",    "once",
                 "—",     "1 of 1"],
            ],
            col_widths=[3 * cm, 2.6 * cm, 1.6 * cm, 1.6 * cm,
                        4 * cm, 2.5 * cm, 10.2 * cm],
        ),
        Paragraph(
            "Cycle length 14 days. The four sig rows above correspond to "
            "four FHIR <font face='Courier'>ActivityDefinition</font> "
            "resources, orchestrated by one "
            "<font face='Courier'>PlanDefinition</font> for the variant. "
            "Each ActivityDefinition is "
            "<font face='Courier'>kind = MedicationRequest</font>, "
            "references a <font face='Courier'>MedicationKnowledge</font> "
            "by canonical, and carries the dose as "
            "<font face='Courier'>doseQuantity { value, unit: 'mg/m2', "
            "system: UCUM }</font>. At <font face='Courier'>$apply</font> "
            "time the Library’s BSA helper multiplies by the patient’s "
            "BSA to produce the absolute mg dose.", CAPTION),
        Paragraph("3.3 Regulatory indications", H2),
        tbl(
            ["Regulator", "Date", "Condition", "Stage", "Prior therapy"],
            [
                ["FDA", "2002-08-09", "Colorectal cancer",
                 "Metastatic", "after FOLFIRI"],
                ["FDA", "2004-01-09", "Colorectal cancer",
                 "(any)",      "—"],
            ],
            col_widths=[3 * cm, 3.6 * cm, 6 * cm, 4 * cm, 8.9 * cm],
        ),
        Paragraph(
            "Each row becomes a "
            "<font face='Courier'>PlanDefinition.useContext</font> entry "
            "plus a "
            "<font face='Courier'>relatedArtifact[type=documentation]</font> "
            "pointing at the regulatory label. Biomarker-conditional "
            "approvals (KRAS-WT, BRAF V600E) also live in this table — "
            "they generate "
            "<font face='Courier'>PlanDefinition.action.condition</font> "
            "CQL expressions at the catalog level so downstream CDS Hooks "
            "responses can be biomarker-aware without the calling EHR "
            "encoding the rule itself.", CAPTION),
        Paragraph("3.4 Supporting studies (selected, by appearance frequency)",
                  H2),
        tbl(
            ["Study", "Trial ID", "Condition", "Phase", "First publication"],
            [
                ["MOSAIC",             "—",
                 "Colorectal cancer (adjuvant)", "Phase 3",
                 "André T et al., NEJM 2004"],
                ["NCCTG N9741",        "—",
                 "Metastatic colorectal cancer", "Phase 3",
                 "Goldberg RM et al., JCO 2004"],
                ["EORTC 40983 (EPOC)", "NCT00006479",
                 "CRC liver metastases",         "Phase 3",
                 "Nordlinger B et al., Lancet 2008"],
                ["PRIME",              "NCT00364013",
                 "Metastatic CRC (KRAS-WT)",     "Phase 3",
                 "Douillard JY et al., NEJM 2013"],
                ["EACH",               "NCT00471965",
                 "Hepatocellular carcinoma",     "Phase 3",
                 "Qin S et al., JCO 2013"],
                ["IDEA",               "—",
                 "Colon cancer (adjuvant)",      "Phase 3",
                 "Grothey A et al., NEJM 2018"],
            ],
            col_widths=[4 * cm, 3.5 * cm, 7 * cm, 2 * cm, 9 * cm],
        ),
        Paragraph(
            "Every study maps to a FHIR "
            "<font face='Courier'>ResearchStudy</font> with the registry ID "
            "as <font face='Courier'>identifier</font>. Every published "
            "endpoint result maps to "
            "<font face='Courier'>EffectEvidenceSynthesis</font> (HR, CI, "
            "p). The PlanDefinition carries "
            "<font face='Courier'>relatedArtifact[type=derived-from]</font> "
            "pointing at each supporting study and at the primary "
            "publication via DOI/PMID. <b>This is the closing-the-loop "
            "instrumentation</b> — every administered dose at a downstream "
            "site traces back, via the knowledge artifact, to the trial "
            "that justified it.", CAPTION),
        PageBreak(),
    ]

    # ── Section 4: chemo + PKI
    story += [
        Paragraph(
            "4. Worked example — chemo + targeted kinase inhibitor combination",
            H1),
        Paragraph(
            "<b>mFOLFOX6 + Lenvatinib + Pembrolizumab</b> (HemOnc cui 28874) "
            "is a contemporary five-component regimen combining a classical "
            "cytotoxic backbone with a multikinase inhibitor (Lenvatinib, "
            "ATC L01EX08, hits VEGFR-1/2/3, FGFR-1/2/3/4, RET, KIT, PDGFRα) "
            "and a checkpoint inhibitor (Pembrolizumab, anti-PD-1 mAb). "
            "Phase 3 RCT evidence, first studied 2021, five HemOnc "
            "components, three sact modalities (cytotoxic, targeted, "
            "immune). Demonstrates that the same FHIR catalog mechanics "
            "scale from a 1995-era cytotoxic protocol to a 2021-era "
            "multi-modality regimen with no structural changes to the IG.",
            BODY),
        Spacer(1, 0.2 * cm),
        Paragraph("4.1 The six sigs, side-by-side", H2),
        tbl(
            ["Component", "Class", "Dose", "Route", "Day pattern", "Cycle"],
            [
                ["Fluorouracil",  "Fluoropyrimidine",
                 "400 mg/m²",   "IV bolus", "day 1",      "14 d"],
                ["Fluorouracil",  "Fluoropyrimidine",
                 "2 400 mg/m²", "IV CI",    "day 1",      "14 d"],
                ["Leucovorin",    "Folate-reduction agent",
                 "400 mg/m²",   "IV",       "day 1",      "14 d"],
                ["Oxaliplatin",   "Platinum agent",
                 "85 mg/m²",    "IV",       "day 1",      "14 d"],
                ["Lenvatinib",    "Multikinase inhibitor (TKI)",
                 "8 mg",        "Oral",     "continuous", "42 d"],
                ["Pembrolizumab", "Anti-PD-1 antibody",
                 "400 mg",      "IV",       "day 1",      "42 d"],
            ],
            col_widths=[4 * cm, 5.5 * cm, 3.2 * cm, 2.5 * cm, 4 * cm, 6.3 * cm],
        ),
        Paragraph(
            "Two cycle lengths in one regimen (q14d chemo + q42d "
            "Lenvatinib/Pembro) is a common modern pattern that the catalog "
            "handles natively via nested "
            "<font face='Courier'>PlanDefinition.action</font> groups with "
            "independent <font face='Courier'>timingTiming</font>. The "
            "dose-target paradigm differs by component: mg/m² for cytotoxics "
            "(multiply by BSA), absolute-mg for Lenvatinib (no patient "
            "scaling) and Pembrolizumab (the FDA-approved fixed dose), with "
            "provenance preserved per-component via the "
            "<font face='Courier'>sig-target-type</font> CodeSystem.",
            CAPTION),
        Paragraph("4.2 Dose-modification surface for Lenvatinib", H2),
        Paragraph(
            "Lenvatinib has the most clinically active dose-modification "
            "rule of any drug in this regimen: starting 8 mg PO daily "
            "continuous, reduced to 4 mg every other day after grade 3 "
            "adverse events, with discontinuation thresholds. None of this "
            "lives in HemOnc’s structured tables — it is in the FDA label "
            "and in the HemOnc.org wiki narrative reached via the "
            "<font face='Courier'>pointers</font> backlink. In our IG "
            "architecture, dose-modification rules become a separate "
            "institution-authored CQL Library that the catalog PlanDefinition "
            "references via "
            "<font face='Courier'>relatedArtifact[type=depends-on]</font>. "
            "Site policy plugs in at this seam without touching the catalog "
            "content. <i>This is why we deliberately separate "
            "protocol-knowledge from institution-policy from order-banding "
            "from administration-recording.</i>", BODY),
        PageBreak(),
    ]

    # ── Section 5: closing the loop
    story += [
        Paragraph("5. Why this matters — closing the loop", H1),
        Paragraph(
            "Today, oncology protocols live as PDFs in pharmacy binders, as "
            "proprietary order sets inside individual EHR vendors (NCCN "
            "Templates™, Epic Beacon, Cerner PowerPlans), and as free-text "
            "Protokoll fields in cancer registry submissions. There is no "
            "openly-licensed, executable, versioned, machine-actionable "
            "catalogue of oncology regimens at European or US scale. "
            "HemOncKB has the content; OMOP has the vocabulary; this IG "
            "supplies the missing piece — a FHIR R4 projection of HemOnc "
            "that downstream EHR / CDS / registry / research systems can "
            "address by canonical URL.", BODY),
        Paragraph(
            "The strategic value is not the catalog itself. The strategic "
            "value is the round-trip: an institution administering a "
            "HemOnc-derived FOLFOX4 cycle today, with structured "
            "MedicationRequests carrying provenance back to the trial that "
            "justified the dose, produces structured MedicationAdministration "
            "data tomorrow that flows back through MII Onkologie / mCODE / "
            "PHOENIX ECCM into OMOP, where the next HemOnc curation cycle "
            "sees the real-world outcome. "
            "<b>Knowledge → care delivery → real-world evidence → "
            "knowledge.</b> One vocabulary on both sides of the loop, "
            "instead of two.", BODY),
        Spacer(1, 0.4 * cm),
        Paragraph("5.1 What is in the repository today", H2),
        tbl(
            ["Artifact", "Status", "Notes"],
            [
                ["sushi-config.yaml + ig.ini",
                 "scaffold ready",
                 "IG-Publisher consumable; declares dependency on "
                 "de.medizininformatikinitiative.kerndatensatz.onkologie "
                 "2026.0.3"],
                ["8 hand-authored R4 JSON resources",
                 "validated",
                 "Carboplatin + Paclitaxel Variant #83 end-to-end (2 "
                 "CodeSystem, 2 MedicationKnowledge, 2 ActivityDefinition, "
                 "1 Library, 1 PlanDefinition)"],
                ["CQL Library + FHIRPath dynamicValues",
                 "validated",
                 "BSA + Calvert + provenance codes; cqf-fhir 8.4.0 quirks "
                 "documented in beads memory"],
                ["HAPI FHIR + cqf-fhir Docker compose",
                 "running locally",
                 "Port 8096; load + $apply round-trip green; demo Patient "
                 "+ Observations produce Carbo 625 mg + Taxol 323.75 mg"],
                ["7 IG narrative pages",
                 "first draft",
                 "index, background, cooperation, disclaimers, versioning, "
                 "$apply/CDS, phase 0"],
                ["beads issue tracker",
                 "13 open issues",
                 "Phase 1A scope, MII∩HemOnc match script, PHOENIX "
                 "engagement, regulatory framing, IP posture, ConceptMap, "
                 "etc."],
            ],
            col_widths=[6.5 * cm, 4 * cm, 15 * cm],
        ),
        Spacer(1, 0.3 * cm),
        Paragraph("5.2 What this is not", H2),
        Paragraph(
            "<b>This is not a medical device.</b> It is reference content "
            "under MDR/IVDR and 21 CFR. It is not CE-marked, FDA-cleared, "
            "or otherwise regulatorily conformed. Integration into any "
            "system intended to influence individual patient care creates "
            "an obligation on the integrator — not on the publisher — to "
            "perform appropriate regulatory qualification and conformity "
            "assessment of that downstream system. See the IG’s "
            "<i>Disclaimers and Intended Use</i> page for the full "
            "statement.", BODY),
        Paragraph(
            "<b>This is not derived from NCCN Guidelines®, the NCCN "
            "Compendium®, or AWMF S3-Leitlinien.</b> All dose, schedule and "
            "indication content traces back, via HemOncKB, to primary "
            "clinical-trial publications and to FDA/EMA labels — facts that "
            "are not copyrightable. The HemOncKB itself is CC BY 4.0 and "
            "has operated independently of NCCN since 2014.", BODY),
        Spacer(1, 0.4 * cm),
        Paragraph(
            "<b>Contact and cooperation:</b> Developed in cooperation with "
            "HemOnc.org / OHDSI Oncology / HL7 Europe PHOENIX / MII "
            "Onkologie. Issues and feedback via the project repository.",
            SMALL),
    ]

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    return OUT


if __name__ == "__main__":
    out = build()
    sz = out.stat().st_size
    print(f"OK wrote {out} ({sz:,} bytes, landscape A4)")
