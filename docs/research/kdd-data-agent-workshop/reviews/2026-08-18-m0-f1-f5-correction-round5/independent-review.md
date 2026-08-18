# Independent Review — M0 Correction Round 5

Completed: `2026-08-18T04:43:17-07:00`  
Review lane: fresh defensive review of exact Round 5 local fixture-backed M0 evidence only  
Verdict: `ACCEPT_LOCAL_M0_EVIDENCE`

## Decision

The Round 5 correction is accepted as local fixture-backed M0 evidence for the admitted metric value-to-authoritative-source-body relation. No Critical or required-change finding remains in this bounded scope.

The transient caller-supplied canonical source body is a valid out-of-band trust anchor for this local model because the frozen contract requires the reported and recomputed metric relation to use the same immutable authoritative source snapshot, scope, interval, and receipt. The frozen contract does not establish the packet's internally resealable admitted output as authoritative independently of that source body.

This trust anchor has a narrow meaning. It is valid only when the caller independently possesses the authorized retained body. It is not a signature, secret, credential, production authorization, or defense against an attacker who controls both the packet and the caller's supposed trust input. The packet's unkeyed digests remain local integrity bindings.

## Hard gate

The package manifest was recomputed independently before review and again after all checks from the sorted repository-relative `.py`, `.json`, and `.md` files below `.agents/skills/kdd_data_agent/`, excluding `__pycache__`, `.pytest_cache`, and `.omc`.

| Binding | Fresh result |
| --- | --- |
| Package file count | `59` |
| Package manifest aggregate | `9eea3014cb74acc48e9bbd24a486d2b6a5a4a4f57ae76191f42d037a5988b19a` |
| `source-manifest-after.sha256` comparison | byte-identical before and after review |
| Frozen packet | `82747da96d66dd8851c03edc837f38597264a07794a2b145cd530ca0a5f07b19` |
| Frozen architecture | `9508b42979b5f708d3b0be7016ed414fd0b4c28d531b75fd0a4710eb46df8fc1` |
| CE plan | `2b4bbd3583e2f289303b8e47b255e3b53bd0f3307f0b699b33299b57aa9e1daf` |
| Sequencing plan | `8fec2f8c3c3d22aa9dc1b762769673789d007fd74dbbed9c34e5ea88fcd4725b` |

No drift occurred.

## Integrity relation review

`m0.packet.decision_metric_output_from_source_body` is the single deterministic projection of the six typed decision-metric fields. `m0.corrected_evaluator` imports and uses that projection for admitted live evaluator output. Public deserialization canonicalizes the transient body, matches its canonical digest to the admitted source receipt, resolves that exact receipt through `admitted_evidence.source_receipt_id`, reprojects the metric output from the body, and requires exact typed equality with the admitted output.

The body is neither serialized nor returned. A recursive inspection of the returned immutable document found no `body`, `trusted_source_body`, or `authoritative_source_body` field; serialized bytes contained neither `check_observations` nor the source body's `numerator` or `denominator`. Canonical serialized size remained `47075` bytes.

## Fresh adversarial evidence

| Case | Result |
| --- | --- |
| Fully resealed admitted value `0.5` with original authoritative body, admitted ID, nineteen validator receipts/evidence identities, and outer digest resealed | rejected: admitted output does not match authoritative body |
| Trusted body metric value changed while packet and receipt remain unchanged | rejected: body digest mismatch |
| Trusted body non-metric field changed while metric projection remains unchanged | rejected: body digest mismatch |
| Fully resealed stale admitted source-receipt reference | rejected: source is not admitted under the contract |
| Admitted packet without the out-of-band authoritative body | rejected: authoritative body required |
| Unadmitted packet supplied with an unexpected trusted body | rejected: unadmitted evidence cannot receive a trusted body |

The five checked-in Round 5 relation regressions passed: `5 passed in 0.09s`. The sixth symmetry case was independently executed against the public deserializer and rejected.

An independent runtime mutation changed only the packet-side projection after evaluator construction; public deserialization rejected the resulting projection divergence. In a fresh disposable copied package, `_verify_authoritative_source_body` was replaced with an immediate return. The five Round 5 tests then produced exactly `4 failed, 1 passed`, and the exact fully resealed value attack was accepted by the mutant. This demonstrates that the new tests depend on the corrected value-to-body relation.

## Reproduction and preservation

| Evidence | Fresh result |
| --- | --- |
| Repository-root full suite | `370 passed in 1.45s` |
| Package-root full suite | `370 passed in 1.44s` |
| Unrelated `/private/tmp` full suite | `370 passed in 1.43s` |
| Capability/import/no-write/no-network suite | `61 passed in 0.23s` |
| `adapters/production` | absent |
| Focused M0 relation/preservation suite | `103 passed in 0.93s` |
| Named semantic validators | `19` |
| Sealed corpus | `19` declared and `19` executed |
| Hard veto kinds | `6` |
| Seeds | `0`, `1`, `42`, `99991`, and `random` identical |
| Serialized byte count | `47075` |
| Serialized-byte SHA-256 | `7327bdb9b280a4b89212bf217b2f6addb40ac8dbd6ba6d46a171ffeb0bfac9cc` |
| Internal packet digest | `sha256:652a3d9f18ff980dbd56059e7d699d6914826847f4d675555137ffa2f5b4caa0` |

The exact Round 4 test files were independently matched to the Round 5 before-manifest using a local disposable Round 4 copy. Collected node IDs compared as `365` before and `370` after, with exactly five additions and zero removals. The additions are the five named authoritative-body relation cases in `test_m0_packet.py`.

The green suites preserve all nineteen validator identities, the 19-case sealed corpus, both contradicted trivial baselines, all three exact-validator decoys, disclosed-conflict reviewer provenance, conflict/read disagreement cases, six hard vetoes, exact Coverage Gap correspondence, the trusted expected-packet-digest boundary, and the Round 4 admitted-lineage relations.

## Five-axis review

- Correctness: the source receipt, canonical body digest, admitted output, validator graph, and expected packet digest are separately bound and fail closed under the required attacks.
- Readability and simplicity: one small named projection is shared; the public boundary orders checks clearly and does not add another serialized identity layer.
- Architecture: the correction preserves the fixture-only immutable packet boundary and keeps retained source data out of packet artifacts.
- Security: caller input is canonicalized and validated, unadmitted-body symmetry is enforced, and no secret, network, production adapter, write, or external capability is introduced.
- Performance: deserialization adds one bounded canonicalization, digest, and six-field projection over the supplied fixture body; no unbounded external I/O or new hot-path dependency exists in this local evidence scope.

## Gaps and proof boundary

There is no residual gap that blocks the exact Round 5 local fixture-backed M0 value-integrity evidence.

This verdict does not authenticate a caller-controlled body, readjudicate Phase A, establish production authority or production-backed capability, close P2/P3/P4, authorize or complete M1/M2, authorize deployment or publication, or establish Experiment Review Committee Acceptance. No production or network access, credential use, Git mutation, commit, push, PR, deployment, publication, or external-system action was performed.
