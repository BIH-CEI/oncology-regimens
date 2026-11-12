# `$apply` scenarios

Executable expectations for `PlanDefinition/$apply` on the catalog, run by
[`scripts/apply/apply_tests.py`](../../scripts/apply/apply_tests.py) against
HAPI FHIR with Clinical Reasoning (cqf-fhir), locally via
`phase0/docker-compose.yml` and in CI (`.github/workflows/apply-scenarios.yml`).

```bash
cd phase0 && docker compose up -d && cd ..
pip install fhirpathpy
sushi .
python3 scripts/apply/apply_tests.py --load            # load IG resources, run everything
python3 scripts/apply/apply_tests.py --only calvert    # subset, server already loaded
```

A scenario is one JSON file in `scenarios/`: patient fixtures (transaction
bundles in `fixtures/`, idempotent through conditional updates), the
PlanDefinition, optional `$apply` parameters and FHIRPath assertions
(evaluated with the R4 model, so `medication.reference` and
`timing.repeat` work on the choice elements) over the returned CarePlan.

Scenarios with `expectedFailure` are the specification of work that is not
done yet. They must fail; when one passes the run fails with XPASS, which
means: remove the marker and close or update the issue it names.

| Scenario | Checks | State |
|---|---|---|
| `calvert-base` | carboplatin 625 mg with the Phase 0 GFR constant, provenance code `computed-from-target-AUC`, versioned `instantiatesCanonical`, q21d, 3 to 6 cycles, day-of-cycle 1 | pass |
| `paclitaxel-base` | 323.75 mg with the Phase 0 BSA constant, `computed-from-target-mg-per-m2`, 3 h infusion, SNOMED route | pass |
| `regimen-structure` | one RequestGroup, cycle action with timing, two day-1 actions, paclitaxel `concurrent-with-start` carboplatin, two MedicationRequests | pass |
| `parameters-post-accepted` | POST form with a `parameters` resource is accepted | pass |
| `unknown-plandefinition` | 404 with OperationOutcome | pass |
| `mii-stub-no-actions` | MII protocol skeleton applies to an empty RequestGroup | pass |
| `formulary-structure` | selection-layer formulary keeps the exactly-one choice and its three SRL-coded entries | pass |
| `cql-quantity-dynamicvalue` | a CQL Quantity assigned to `doseQuantity` in one dynamicValue (test fixture library) | pass on HAPI 8.12.0; failed on 8.4.0 (oncology-regimens-r4g) |
| `calvert-gfr-from-creatinine`, `calvert-gfr-cap`, `paclitaxel-bsa-mosteller`, `missing-creatinine`, `stale-creatinine`, `parameter-target-auc-override` | doses derived from Patient and Observations, GFR cap, input checks, Library parameters honoured | expected failure, oncology-regimens-m75 |
| `missing-weight`, `missing-height`, `weight-in-pounds`, `creatinine-in-umol`, `implausible-values` | negative cases: no dose without the inputs a formula needs (weight for Cockcroft-Gault and BSA, height for BSA), an OperationOutcome via `cqf-messages` naming the missing input, unit conversion (lb, µmol/L), refusal of implausible values | expected failure, oncology-regimens-m75 |
| `cycle-expansion` | per-cycle groups with day offsets | expected failure, oncology-regimens-hsd |
| `formulary-pinned-parameters` | formulary entries resolve to catalog variants, applicability conditions evaluate, pinned parameters apply | expected failure, oncology-regimens-v96 |

Messages: in `$apply` results, warnings and errors arrive as an
`OperationOutcome` contained in the CarePlan and linked from the
RequestGroup through the `cqf-messages` extension; the negative scenarios
assert on `contained.ofType(OperationOutcome).issue.diagnostics`. In CDS
Hooks the same information becomes cards (`indicator` info, warning,
critical; `summary`, `detail`, `suggestions`), which is not tested yet
(oncology-regimens-718).

What this does not test: FHIR R6 (there is no `$apply` implementation for
R6; the derived R6 resources are only validated, see `maps/xver/`), CDS
Hooks delivery, and anything a real ordering system does with the CarePlan.
