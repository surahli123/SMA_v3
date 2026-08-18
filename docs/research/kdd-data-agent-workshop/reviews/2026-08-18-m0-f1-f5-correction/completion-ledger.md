# M0 Independent-Review Correction Completion Ledger

Correction scope: exactly `IR-M0-01` through `IR-M0-06` against input aggregate `sha256:30d6b47ca55f1444ef8ba596aedabd90db5f21af58e60d53ad2320a5fc94c196`.

| ID | Required correction | Observable evidence | State |
| --- | --- | --- | --- |
| `IR-M0-01` | Readiness cannot be minted by construction or deserialization | reconstruction and digest-valid tamper tests; killed mutation | `CORRECTED_PENDING_INDEPENDENT_REREVIEW` |
| `IR-M0-02` | Contract-bound typed read admission before recomputation | unauthorized and mismatch fail-closed tests; killed mutation | `CORRECTED_PENDING_INDEPENDENT_REREVIEW` |
| `IR-M0-03` | Explicit validator result and evidence for all 19 checks | absent-validator and distinct-evidence tests; killed mutation | `CORRECTED_PENDING_INDEPENDENT_REREVIEW` |
| `IR-M0-04` | Internal versioned typed-output comparator | no public comparison boolean; disagreement test; killed mutation | `CORRECTED_PENDING_INDEPENDENT_REREVIEW` |
| `IR-M0-05` | One byte-bound executable corpus through evaluator/baselines/decoys/conflicts/vetoes | pinned corpus execution; byte-drift mutation killed | `CORRECTED_PENDING_INDEPENDENT_REREVIEW` |
| `IR-M0-06` | One truthful canonical builder and digest namespaces | five identical seed runs; reporting mutation killed | `CORRECTED_PENDING_INDEPENDENT_REREVIEW` |

## Preserved and separate proof states

| State | Disposition |
| --- | --- |
| Independently verified Phase A behavior | preserved; final mutation probes pending |
| Corrected local fixture-backed M0 evidence | three-directory and five-seed evidence complete; independent rereview pending |
| Production authorization/capability | not established |
| P2 / P3 / P4 | open external gates |
| M1 / M2 | not implemented or authorized |
| Deployment / publication | not performed or authorized |
| Committee Acceptance | external and not established |
