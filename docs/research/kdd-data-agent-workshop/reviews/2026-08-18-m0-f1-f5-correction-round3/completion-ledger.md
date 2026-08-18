# M0 Correction Round 3 Completion Ledger

Scope: exactly `IR-M0-01-RR` and `IR-M0-TEST-RR` against input aggregate `sha256:52d4c82e2a80ffc5a42bc80918165b33ebed0b03256a27c7c7bc78bd8046d2f6`.

| ID | Required outcome | Observable evidence | State |
| --- | --- | --- | --- |
| `IR-M0-01-RR` | Public deserialization validates the complete check/source/validator/evidence/gap relation graph and requires an out-of-band trusted expected packet digest | exact fully resealed and relational mutations rejected before a document is exposed; three copied-package mutations killed | `CORRECTED_PENDING_INDEPENDENT_REREVIEW` |
| `IR-M0-TEST-RR` | Add exact public-boundary regressions without weakening or deleting the 344-test semantic suite | 14 behavior cases added, zero removed; `358 passed` from three directories | `CORRECTED_PENDING_INDEPENDENT_REREVIEW` |
| Preserved behavior | Preserve the nineteen validators, corpus, baselines, decoys, conflicts, hard vetoes, capabilities, and deterministic builder | full suite, direct hard-veto serialization, five seeds, frozen hashes, and `61 passed` capability scan | `VERIFIED_IN_THIS_BOUNDED_RUN` |
| Proof boundaries | Keep local integrity evidence separate from authority and deployment claims | status and receipt preserve every external proof boundary | `COMPLETE` |
