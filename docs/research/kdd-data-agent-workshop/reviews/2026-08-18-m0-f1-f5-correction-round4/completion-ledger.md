# M0 Correction Round 4 Completion Ledger

Scope: exactly the remaining admitted-evidence lineage defect under `IR-M0-01-RR` and its missing `IR-M0-TEST-RR` coverage, against input aggregate `sha256:f32404705d3c32a9b1e09ba932db080ae1b1e63b6a55132c526457cec9e7c8ab`.

| ID | Required outcome | Observable evidence | State |
| --- | --- | --- | --- |
| `IR-M0-01-RR` | Serialize one minimal typed admitted-evidence payload, recompute its identity, enforce source/contract/output/observed relations and exact None symmetry, and bind it into every validator evidence identity | shared canonical identity formula; exact-schema public verifier; authorized and unauthorized fully resealed attacks rejected | `VERIFIED_IN_THIS_BOUNDED_RUN_PENDING_INDEPENDENT_REREVIEW` |
| `IR-M0-TEST-RR` | Add authorized and unauthorized admitted-lineage regressions without removing or weakening the 358-test suite | red phase reproduced; seven new semantic cases; `365 passed` from three directories; zero prior cases removed | `VERIFIED_IN_THIS_BOUNDED_RUN_PENDING_INDEPENDENT_REREVIEW` |
| Preserved behavior | Preserve Round 3 relations, trusted digest, gaps, nineteen validators, corpus, baselines, decoys, conflict, vetoes, and local-only capability | three full suites; five identical seeds; `61 passed` capability scan; five copied-package mutation failures; unchanged frozen hashes | `VERIFIED_IN_THIS_BOUNDED_RUN` |
| Proof boundaries | Keep local integrity evidence separate from authorization, deployment, and acceptance | receipt and status preserve Phase A, production, P2/P3/P4, M1/M2, deployment/publication, and Committee gates separately | `VERIFIED_IN_THIS_BOUNDED_RUN` |
