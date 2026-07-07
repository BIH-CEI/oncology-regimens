# Disclaimers and Intended Use - HemOnc FHIR Regimen Catalog — Executable Knowledge Layer for Oncology Protocols v2026-03-12-0.1.0

* [**Table of Contents**](toc.md)
* **Disclaimers and Intended Use**

## Disclaimers and Intended Use

### Disclaimers and Intended Use

#### Intended use

This Implementation Guide and its accompanying FHIR resources are published solely as a reference re-encoding of the publicly available HemOnc Knowledge Base into FHIR R4 Knowledge Artifacts. They are intended for use by software developers, researchers, terminologists and informaticists. They are **NOT intended for use, and SHALL NOT be used, in the diagnosis, prevention, monitoring, treatment, or alleviation of disease in individual patients without separate, independent clinical validation by a competent healthcare professional and, where applicable, conformity assessment under Regulation (EU) 2017/745, 21 CFR 820, or equivalent national medical-device law.**

#### Not a medical device

The artifacts in this distribution are reference content, not a medical device or medical-device software (MDSW) as defined by Regulation (EU) 2017/745, Article 2(1), or by 21 U.S.C. § 321(h). No CE marking, FDA clearance, or other regulatory conformity has been sought or granted. Any integration of these artifacts into a system intended to influence individual patient care creates an obligation on the integrator to perform the appropriate regulatory qualification, classification, and conformity assessment of that system.

#### No warranty of clinical accuracy

The dose, schedule, route and indication content is derived programmatically from HemOncKB. Errors may exist due to (a) the source data itself, (b) the transform, (c) the FHIR R4 representation, or (d) the interpretation by downstream software. The publishers disclaim, to the maximum extent permitted by law, all warranties, express or implied, including any warranty of fitness for any particular clinical purpose. Users SHALL NOT administer, prescribe, or order any therapy on the basis of these artifacts without independent verification against an authoritative primary source (e.g., the originating clinical trial publication, the regulatory label, or institutional protocol) by a competent healthcare professional.

#### Sandbox software

Any companion HAPI FHIR / cqf-fhir Docker images, scripts or example bundles in this repository are configured for illustration only. They are unauthenticated, have no audit trail compliant with §75c SGB V, GDPR Art. 32, or 21 CFR Part 11, and contain experimental Clinical Reasoning behaviour. They **SHALL NOT** be deployed into any environment processing real patient data. Production deployments require independent hardening, authentication (TI-Telematikinfrastruktur where applicable), audit-logging, and qualification of the containing medical-device software.

