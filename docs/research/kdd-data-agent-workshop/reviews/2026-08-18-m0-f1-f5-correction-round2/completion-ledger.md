# M0 Correction Round 2 Completion Ledger

Scope: exactly `IR-M0-01-RR`, `IR-M0-03-RR`, and `IR-M0-TEST-RR` against input aggregate `sha256:c9c2d30fe588ce68fa1f45f93b83df768090f3ce7c0992516e8d31b224d4c901`.

| ID | Required outcome | Observable evidence | State |
| --- | --- | --- | --- |
| `IR-M0-01-RR` | Serialized packets verify every nested typed identity and binding before exposure | stale nested check, receipt ID/digest, core-set, contract, binding, gap, readiness, and check-lineage mutations rejected through `FlightReadinessPacket.deserialize`; copied-package bypass killed | `CORRECTED_PENDING_INDEPENDENT_REREVIEW` |
| `IR-M0-03-RR` | CHK-01 through CHK-19 each execute a deterministic semantic validator over raw observations, the contract, and admitted receipt lineage | trusted fixture passes only from structured observations; all nineteen contradictory cases fail; absent is `MISSING`; malformed is materiality-`UNKNOWN`; arbitrary presence bypass killed | `CORRECTED_PENDING_INDEPENDENT_REREVIEW` |
| `IR-M0-TEST-RR` | Restore public-evaluator semantic coverage without silent deletion | `344 passed`; nineteen-check contradiction matrix, unknown-materiality ceiling, unique validator receipts/evidence, malformed/absent observations, and nested identity tampering | `CORRECTED_PENDING_INDEPENDENT_REREVIEW` |
| Preserved closures | Preserve `IR-M0-02`, `IR-M0-04`, `IR-M0-05` plumbing, `IR-M0-06`, Phase A, and S1-S11/D1-D8 | three-directory suite, 19-case corpus, typed comparator, five seeds, exact frozen hashes, and local boundary scan | `VERIFIED_IN_THIS_BOUNDED_RUN` |
| Proof boundaries | Keep local fixture evidence distinct from all external gates and acceptance | receipt and status name production/P2/P3/P4/M1/M2/deployment/publication/Committee states separately | `COMPLETE` |
