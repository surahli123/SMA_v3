# M0 Correction Round 5 Completion Ledger

Scope: exactly the admitted metric value-to-authoritative-source-body relation gap and its missing regression coverage, against input aggregate `sha256:29040a66a97a50a21b02178bf494d378f709bc991aefc6b36ac8ba10294f0a02`.

| ID | Required outcome | Observable evidence | State |
| --- | --- | --- | --- |
| Trust-model decision | Determine whether an internally resealed metric value may diverge from the admitted authoritative body | documented `ReadResult` body-digest invariant and frozen authoritative-source/recomputation requirements | `VALID_FINDING` |
| Value-to-body correction | Recompute admitted output from a trusted canonical body at public verification without serializing retained body data | shared deterministic projection; trusted body digest/source receipt binding; exact derived-output comparison | `VERIFIED_IN_THIS_BOUNDED_RUN_PENDING_INDEPENDENT_REVIEW` |
| Adversarial coverage | Reject changed value, changed body relation, stale source binding, and fully consistent resealing under the trusted source boundary | five focused red/green public-deserializer cases; copied-package verifier bypass produced four failures and accepted the exact value attack | `VERIFIED_IN_THIS_BOUNDED_RUN_PENDING_INDEPENDENT_REVIEW` |
| Preserved behavior | Preserve all 365 tests, nineteen validators, corpus/baselines/decoys/conflict/vetoes, determinism, and capability limits | `370 passed` from three directories; five identical seeds; `61 passed` capability scan; unchanged frozen hashes; verified 59-file after-manifest | `VERIFIED_IN_THIS_BOUNDED_RUN` |
| Proof boundaries | Keep Phase A, local M0, production authority/capability, later phases, deployment/publication, and Committee Acceptance separate | receipt/status/handoff state each boundary explicitly | `VERIFIED_IN_THIS_BOUNDED_RUN` |
