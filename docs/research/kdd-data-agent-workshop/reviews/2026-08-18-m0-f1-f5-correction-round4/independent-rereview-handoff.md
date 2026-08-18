# Independent Rereview Handoff — M0 Correction Round 4

## Requested independent decision

Independently rereview only the Round 4 correction for the remaining admitted-evidence lineage portion of `IR-M0-01-RR` and its `IR-M0-TEST-RR` regressions. Do not inherit the implementation owner's conclusion. Return a fresh accept/reject verdict for corrected local fixture-backed integrity evidence only.

Do not edit the package, frozen/canonical documents, prior artifacts, Git, production, or external systems. Use disposable copies for adversarial mutations. Do not promote Phase A, production authorization/capability, P2/P3/P4, M1/M2, deployment/publication, or Committee Acceptance.

## Hard gate

Independently recompute the sorted `.py`/`.json`/`.md` package manifest below `.agents/skills/kdd_data_agent/`, excluding `__pycache__`, `.pytest_cache`, and `.omc`. Require exactly 59 files and aggregate:

`sha256:29040a66a97a50a21b02178bf494d378f709bc991aefc6b36ac8ba10294f0a02`

Require the recomputed manifest to be byte-identical to `source-manifest-after.sha256`. Stop on drift.

Also require unchanged bindings:

- Frozen packet: `82747da96d66dd8851c03edc837f38597264a07794a2b145cd530ca0a5f07b19`
- Frozen architecture: `9508b42979b5f708d3b0be7016ed414fd0b4c28d531b75fd0a4710eb46df8fc1`
- CE plan: `2b4bbd3583e2f289303b8e47b255e3b53bd0f3307f0b699b33299b57aa9e1daf`
- Sequencing plan: `8fec2f8c3c3d22aa9dc1b762769673789d007fd74dbbed9c34e5ea88fcd4725b`

## Changed integrity surface

- `m0/packet.py` defines the shared canonical admitted-evidence formula, typed packet payload, exact-schema and relation verifier, `None` symmetry, and validator-evidence payload binding.
- `m0/corrected_evaluator.py` derives the admitted identity through that shared formula and supplies the typed payload to the packet and every validator evidence identity, including hard vetoes.
- `tests/test_m0_packet.py` adds seven semantic cases and removes none.

The named canonical builder reports:

- bytes: `47075`
- serialized-byte SHA-256: `7327bdb9b280a4b89212bf217b2f6addb40ac8dbd6ba6d46a171ffeb0bfac9cc`
- internal packet digest: `sha256:652a3d9f18ff980dbd56059e7d699d6914826847f4d675555137ffa2f5b4caa0`

## Required fresh attacks

At the public deserializer, supply the attacker's newly resealed outer digest and independently verify rejection of:

1. An authorized real admitted ID replaced by an arbitrary digest, with validator receipts, checks, gaps, and outer identity resealed.
2. An admitted payload mutation with its old ID retained.
3. A payload and ID fully resealed while source, contract, typed output, or observed relation is wrong.
4. Missing or extra admitted-payload fields.
5. An unauthorized/no-body packet promoted from `None` to a digest.
6. An unauthorized/no-body packet given a fully forged payload and matching resealed ID/bindings.

Also independently confirm that the verified payload, not merely its attacker-controlled ID, changes each validator evidence identity; that every validator ID is exactly the recomputed packet identity; and that `None` payload if and only if all validator admitted IDs are `None`.

## Reproduction evidence to recheck

- Full suite from repository root, package root, and unrelated `/private/tmp`: `365 passed` each.
- Capability/import/no-write/no-network suite: `61 passed`; no `adapters/production` directory.
- Seeds `0`, `1`, `42`, `99991`, and `random`: identical named-builder evidence.
- Preserve all nineteen validators, 19-case sealed corpus, baselines, decoys, conflict/provenance cases, six hard vetoes, exact gap graph, and required out-of-band expected packet digest.
- Use a fresh copied-package mutation that bypasses the admitted-evidence verifier and require the new tests to fail.

## Proof boundary

The expected packet digest and admitted-evidence hashes are local integrity bindings only. They are not secrets, signatures, credentials, authenticity proofs, production authorization, or Committee decisions. Even a green independent rereview may accept only corrected local fixture-backed M0 integrity evidence. All other proof states remain separate and open as recorded in `correction-round4-status.json`.
