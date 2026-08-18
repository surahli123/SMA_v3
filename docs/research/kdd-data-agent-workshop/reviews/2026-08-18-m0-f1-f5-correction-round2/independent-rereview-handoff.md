# Independent Rereview Handoff — M0 Correction Round 2

## Requested review

Perform a fresh, report-only independent rereview of exactly `IR-M0-01-RR`, `IR-M0-03-RR`, and `IR-M0-TEST-RR`. Do not adopt this implementation owner’s conclusions. Preserve the separate accepted dispositions for `IR-M0-02`, `IR-M0-04`, `IR-M0-05` plumbing, and `IR-M0-06`, but probe them if the new bytes could have regressed them.

This handoff does not start a reviewer. It records the next authorized review surface only.

## Hard binding

Before reviewing, independently recompute the sorted `.py`/`.json`/`.md` package manifest below `.agents/skills/kdd_data_agent/`, excluding `__pycache__`, `.pytest_cache`, and `.omc`. Require exact aggregate:

`sha256:52d4c82e2a80ffc5a42bc80918165b33ebed0b03256a27c7c7bc78bd8046d2f6`

Stop `BLOCKED_BY_DRIFT` if it differs. Independently verify these unchanged supporting bindings:

- frozen packet: `82747da96d66dd8851c03edc837f38597264a07794a2b145cd530ca0a5f07b19`;
- controlling architecture: `9508b42979b5f708d3b0be7016ed414fd0b4c28d531b75fd0a4710eb46df8fc1`;
- CE plan: `2b4bbd3583e2f289303b8e47b255e3b53bd0f3307f0b699b33299b57aa9e1daf`; and
- sequencing plan: `8fec2f8c3c3d22aa9dc1b762769673789d007fd74dbbed9c34e5ea88fcd4725b`.

Read this directory’s receipt, status, ledger, and both manifests, plus the prior independent rereview and frozen contract.

## Required adversarial probes

1. Reproduce the prior digest-valid promotion attempt: alter a blocking check outcome, retain its stale `result_digest`, update readiness and outer packet digest, and require rejection before a document is returned.
2. Probe stale and fully re-sealed nested check, core-set, contract, frozen-binding, receipt ID/digest, Coverage Gap, inventory, receipt-lineage, and evidence-lineage mutations.
3. Replace all nineteen raw observations with present contradictory garbage. Require zero `PASS` outcomes and `not_permitted`.
4. For each CHK-01 through CHK-19, mutate the underlying observation while preserving unrelated observations. Require the named check to fail closed through the public evaluator.
5. Remove one observation and make another malformed. Require `MISSING` and materiality-`UNKNOWN` respectively, never default `PASS`.
6. Verify every trusted check has a unique evidence identity and a unique check-validator receipt, and that those receipts bind the source receipt, contract digest, and observation digest.
7. Re-run the real unauthorized/no-body fixture, typed-output disagreement, `same_pipeline`, all nineteen sealed corpus cases, trivial baselines, three decoys, reviewer conflict, and six hard vetoes.
8. Mutate a trusted fixture byte without updating the corpus pin and mutate planted truth without changing evaluator output. Both must be killed.

## Reproduction commands and expected evidence

Use `PYTHONDONTWRITEBYTECODE=1` and `-p no:cacheprovider`. Run the complete suite from repository root, package root, and unrelated `/private/tmp`; the implementation-owner result was `344 passed` in each. Run the named canonical builder under seeds `0`, `1`, `42`, `99991`, and `random`; every run should report:

```text
serialized_byte_count: 44044
serialized_byte_sha256: cea0119be0588fe5746c2d6bd2da57c577332952c8ec17cf86171d9e8176dc4f
internal_content_digest: sha256:4135a724d70e0300d44ee431d1299fcdb9882b67a144b72e7cdaa4f88594c076
```

Inspect the capability/import/no-write/no-network boundary and confirm that `adapters/production` is absent. No production, network, credential, Git, deployment, publication, or external action is needed or authorized.

## Test-count reconciliation to challenge

Original: `314`; Round 1: `313`; Round 2: `344`. Round 2 claims 31 new cases over Round 1 and net `+30` over the original: 19 per-check contradiction cases, the restored unknown-materiality ceiling, arbitrary-present and absent-observation regressions, and ten serialized-boundary cases. Confirm that all nine semantic cases identified as removed in the prior rereview have equivalent or stronger public-evaluator coverage and that no count was inflated by metadata-only assertions.

## Proof boundary

An independent green rereview may accept only corrected local fixture-backed M0 evidence. It must not promote the separately bounded Phase A evidence, claim production authorization or production-backed M0 capability, close P2/P3/P4, authorize or complete M1/M2, deploy, publish, or claim Experiment Review Committee Acceptance.
