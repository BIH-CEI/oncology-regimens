#!/usr/bin/env bash
# Load the Phase 0 knowledge artifacts + demo patient into HAPI, then invoke
# PlanDefinition/$apply and print the resulting CarePlan.
#
# Prereqs:
#   docker compose up -d   (from phase0/)
#   wait for http://localhost:8096/fhir/metadata to return 200
#
# Usage:
#   ./scripts/load-and-apply.sh
set -euo pipefail

BASE="${HAPI_BASE:-http://localhost:8096/fhir}"
HERE="$(cd "$(dirname "$0")/.." && pwd)"

post() {
  local file="$1"
  local id; id="$(jq -r '.id' "$file")"
  local rt; rt="$(jq -r '.resourceType' "$file")"
  echo "  PUT  ${rt}/${id}"
  curl -sS -X PUT -H "Content-Type: application/fhir+json" \
       "${BASE}/${rt}/${id}" --data-binary "@${file}" >/dev/null
}

echo "── load knowledge artifacts ─────────────────────────"
post "${HERE}/resources/CodeSystem-hemonc-fragment.json"
post "${HERE}/resources/CodeSystem-sig-target-type.json"
post "${HERE}/resources/MedicationKnowledge-hemonc-drug-88-carboplatin.json"
post "${HERE}/resources/MedicationKnowledge-hemonc-drug-379-paclitaxel.json"
post "${HERE}/resources/Library-HemOncDoseHelpers.json"
post "${HERE}/resources/ActivityDefinition-sig-carboplatin-auc5-d1-q21d.json"
post "${HERE}/resources/ActivityDefinition-sig-paclitaxel-175mgm2-d1-q21d.json"
post "${HERE}/resources/PlanDefinition-regimen-2554-variant-144842.json"

echo
echo "── load demo patient + observations ────────────────"
post "${HERE}/examples/Patient-demo.json"
curl -sS -X POST -H "Content-Type: application/fhir+json" \
     "${BASE}" --data-binary "@${HERE}/examples/Observations-demo.json" \
     | jq '.entry[] | .response.location // .response.status'

echo
echo "── invoke PlanDefinition/\$apply ─────────────────────"
PD_ID="regimen-2554-variant-144842"
APPLY_OUT="$(curl -sS \
  "${BASE}/PlanDefinition/${PD_ID}/\$apply?subject=Patient/demo-cp-1" \
  -H "Accept: application/fhir+json")"

echo "$APPLY_OUT" | jq '
  {
    resourceType,
    id,
    issues: ([.. | objects | select(.resourceType=="OperationOutcome") | .issue[]?] // []),
    careplan: (
      if .resourceType=="CarePlan" then {
        instantiates: .instantiatesCanonical,
        activities: [.activity[]?.reference?.reference, .activity[]?.detail?.kind] | flatten
      } elif .resourceType=="Bundle" then
        [.entry[].resource | {rt: .resourceType, id, doses: (.dosageInstruction[]?.doseAndRate[0].doseQuantity // null)}]
      else . end
    )
  }
'
