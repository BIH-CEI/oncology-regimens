#!/usr/bin/env bash
# Phase 0 demo: load the IG into HAPI (cqf-fhir) and show PlanDefinition/$apply
# for the Carboplatin + Paclitaxel variant. The executable expectations live in
# tests/apply (python3 scripts/apply/apply_tests.py); this script is the
# interactive walk-through.
#
# Prereqs:
#   docker compose up -d        (from phase0/)
#   sushi .                     (from the repository root)
#   pip install fhirpathpy
set -euo pipefail

BASE="${HAPI_BASE:-http://localhost:8096/fhir}"
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"

echo "── load IG resources (fsh-generated + input/resources) and run the scenarios ──"
python3 "${ROOT}/scripts/apply/apply_tests.py" --base "${BASE}" --wait 300 --load --only calvert-base paclitaxel-base regimen-structure

echo
echo "── PlanDefinition/\$apply for the demo patient ─────────────────────────────"
curl -sS "${BASE}/PlanDefinition/regimen-2554-variant-144842/\$apply?subject=Patient/demo-cp-1" \
  -H "Accept: application/fhir+json" | python3 -c '
import json, sys
cp = json.load(sys.stdin)
print(cp["resourceType"], cp.get("instantiatesCanonical"))
for c in cp.get("contained", []):
    if c["resourceType"] == "MedicationRequest":
        d = c["dosageInstruction"][0]["doseAndRate"][0]
        print(f'"'"'  {c["medicationReference"]["reference"]}: {d["doseQuantity"]["value"]} {d["doseQuantity"]["code"]} ({d["type"]["coding"][0]["code"]})'"'"')
'
