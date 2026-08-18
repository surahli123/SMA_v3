# Independent Review Handoff — M0 Correction Round 5

## Requested independent decision

Independently review only the Round 5 correction for the admitted metric value-to-authoritative-source-body relation gap and its five regressions. Do not inherit the implementation owner's conclusion. Return a fresh accept/reject verdict for corrected local fixture-backed M0 evidence only.

Do not edit the package, frozen/canonical documents, prior artifacts, Git, production, or external systems. Use disposable copies for adversarial mutations. Do not promote Phase A, production authorization/capability, P2/P3/P4, M1/M2, deployment/publication, or Committee Acceptance.

Round 4 has no independent acceptance. Its reviewer identified the valid value-to-body relation gap before a platform classifier interrupted report writing. Treat Round 4 as rejected evidence, not as an incomplete acceptance.

## Hard gate

Independently recompute the sorted `.py`/`.json`/`.md` package manifest below `.agents/skills/kdd_data_agent/`, excluding `__pycache__`, `.pytest_cache`, and `.omc`. Require exactly 59 files and aggregate:

`sha256:9eea3014cb74acc48e9bbd24a486d2b6a5a4a4f57ae76191f42d037a5988b19a`

Require the recomputed manifest to be byte-identical to `source-manifest-after.sha256`. Stop on drift.

Also require unchanged bindings:

- Frozen packet: `82747da96d66dd8851c03edc837f38597264a07794a2b145cd530ca0a5f07b19`
- Frozen architecture: `9508b42979b5f708d3b0be7016ed414fd0b4c28d531b75fd0a4710eb46df8fc1`
- CE plan: `2b4bbd3583e2f289303b8e47b255e3b53bd0f3307f0b699b33299b57aa9e1daf`
- Sequencing plan: `8fec2f8c3c3d22aa9dc1b762769673789d007fd74dbbed9c34e5ea88fcd4725b`

## Trust model to challenge

The correction treats the authorized retained source body as the value-recomputation trust anchor. The packet's unkeyed hashes and caller-supplied expected packet digest remain local integrity bindings and cannot authenticate an attacker-controlled fully resealed packet. The body is supplied transiently out of band at public deserialization, its canonical digest must match the admitted source receipt, and the decision metric is reprojected from that exact body. The body is not serialized or returned.

Reject this model if the frozen contract instead establishes the admitted packet output as authoritative independently of its source body. Otherwise, require the value-to-body relation described below. Do not reinterpret the transient body as a signature, secret, production credential, authorization proof, or Committee decision.

## Changed integrity surface

- `m0/packet.py` defines the shared deterministic source-body projection and verifies the admitted source receipt, canonical body digest, derived typed output, and unadmitted-body symmetry during construction and public deserialization.
- `m0/corrected_evaluator.py` uses the same projection for live evaluator output.
- `tests/test_m0_packet.py` adds the fully resealed value, changed body, stale body/source, and missing trust-boundary regressions.
- `tests/test_m0_corrections.py` supplies the authoritative fixture body when exercising the public deserializer.

The named canonical builder reports:

- bytes: `47075`
- serialized-byte SHA-256: `7327bdb9b280a4b89212bf217b2f6addb40ac8dbd6ba6d46a171ffeb0bfac9cc`
- internal packet digest: `sha256:652a3d9f18ff980dbd56059e7d699d6914826847f4d675555137ffa2f5b4caa0`

## Required fresh attacks

At the public deserializer, independently supply an attacker's newly resealed outer digest and verify rejection of:

1. An admitted metric value changed while retaining the original trusted body, with the admitted ID, all nineteen validator receipts/evidence identities, and packet digest fully resealed.
2. A trusted body whose decision value is changed while the packet and source receipt remain unchanged.
3. A trusted body with a stale non-metric field that changes the canonical body digest while leaving the metric output unchanged.
4. A fully resealed admitted source receipt/reference that no longer names the authoritative body-bearing receipt.
5. An admitted packet presented without the required out-of-band authoritative body.
6. An unadmitted or unauthorized packet supplied with an unexpected trusted body.

Also mutate the shared source-body projection independently of the evaluator and verify that relation tests fail. Confirm that the body cannot enter serialized bytes or the returned immutable document.

## Reproduction evidence to recheck

- Full suite from repository root, package root, and unrelated `/private/tmp`: `370 passed` each.
- Test-count delta: Round 4 `365`; Round 5 `370`; five added and zero removed.
- Capability/import/no-write/no-network suite: `61 passed`; no `adapters/production` directory.
- Seeds `0`, `1`, `42`, `99991`, and `random`: identical named-builder evidence.
- Preserve all nineteen validators, 19-case sealed corpus, baselines, decoys, conflict/provenance cases, six hard vetoes, exact gap graph, trusted expected-digest boundary, and Round 4 admitted-lineage relations.
- Use a fresh copied-package mutation of `_verify_authoritative_source_body`; require the new tests to fail and the fully resealed value attack to survive the mutant.

## Proof boundary

A green review may accept only the Round 5 corrected local fixture-backed M0 value-integrity relation. It cannot accept production authorization or capability, later phases, deployment, publication, or Committee approval. It must not claim Phase A was readjudicated. No independent acceptance exists until the reviewer completes and saves a fresh report against the exact aggregate above.
