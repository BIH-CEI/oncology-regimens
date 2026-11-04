# Cooperation, Attribution and Licensing - European SACT Regimen Catalog — Executable Knowledge Layer for Systemic Anti-Cancer Therapy Regimens v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* **Cooperation, Attribution and Licensing**

## Cooperation, Attribution and Licensing

### Cooperation, Attribution and Licensing

This Implementation Guide is a FHIR-native projection of the [HemOnc Knowledge Base](https://hemonc.org) (HemOncKB), the canonical oncology vocabulary in the OMOP Common Data Model. The IG is being developed in close cooperation with several communities; this page records the relationships, the licensing terms that travel with the content, and the operational commitments that make the cooperation verifiable rather than rhetorical.

#### Cooperation partners

* **HemOnc.org editorial team** — faithful semantic representation of regimens, sigs and clinical evidence; alignment on versioning cadence; round-tripping of FHIR-discovered ambiguities back into HemOncKB.
* **OHDSI / OMOP Oncology community** — identity parity between the OMOP-canonical HemOnc `concept_id` and the FHIR artifact, so that observational research (OMOP) and clinical workflow (FHIR) operate over the same underlying knowledge.
* **HL7 Europe PHOENIX** initiative and the European Common Cancer Model (ECCM) — alignment of the catalog layer with the EU patient-data layer as ECCM publishes FHIR profiles.
* **Medizininformatik-Initiative Onkologie working group** — a workable mapping (experimental) between the German cancer-registry protocol codes (`mii-cs-onko-systemische-therapie-protokolle`) and this clinical-ordering catalog.

#### Operational commitments

1. **Version lockstep with HemOnc.**Every IG release labels itself with the HemOnc snapshot date it was derived from. New HemOnc snapshot → new IG version within ≤4 weeks.
1. **Upstream issue feedback.**FHIR-discovered inconsistencies in HemOncKB are filed as HemOnc Dataverse / repository issues, not silently fixed locally. Every PlanDefinition carries a`relatedArtifact[type=derived-from]`pointing at its source row.
1. **OMOP round-trip preservation.**Every PlanDefinition carries the HemOnc CUI (which corresponds to an OMOP`concept_code`) as a`use=secondary`identifier, so tooling that round-trips OMOP↔FHIR can re-derive the OMOP concept without parsing canonical URLs.

#### Licensing

HemOnc content is distributed under **CC BY 4.0** ([Warner JL et al., 2019, J Biomed Inform](https://pubmed.ncbi.nlm.nih.gov/31238109/); [HemOnc Dataverse](https://dataverse.harvard.edu/dataverse/hemonc)). This IG carries the same licence. Attribution must be preserved in any downstream incorporation, in line with CC BY 4.0 §3.

Where this IG references other CodeSystems and standards (MII Onkologie, RxNorm, SNOMED CT, NCIt, ATC, LOINC), the original licensing terms of those resources apply to their respective concepts.

#### Not derived from NCCN or AWMF guidelines

The content of this IG is derived from primary clinical-trial publications, drug labels, and the HemOnc Knowledge Base. It is **not derived from NCCN Guidelines®, the NCCN Compendium®, NCCN Chemotherapy Order Templates™, or AWMF S3-Leitlinien**, and makes no claim of compatibility with those products. NCCN and AWMF are trademarks of their respective owners.

