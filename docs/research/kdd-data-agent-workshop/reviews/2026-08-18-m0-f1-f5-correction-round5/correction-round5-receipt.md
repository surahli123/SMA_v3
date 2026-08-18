# M0 Correction Round 5 Receipt

Completed: `2026-08-18T04:32:18-07:00`  
Run boundary: one Owner-authorized local correction run for the admitted metric value-to-authoritative-source-body relation gap and its missing regressions only  
Terminal implementation state: `CORRECTED_LOCAL_FIXTURE_BACKED_M0_READY_FOR_INDEPENDENT_REVIEW`

## Trust-model disposition

The Round 4 review finding is valid under the documented local trust model. A retained `ReadResult` originally binds `receipt.body_digest` to the canonical retained body, and the evaluator derives the admitted decision-metric output from that body. Round 4 packet verification retained only the receipt body digest and an internally resealable admitted-output identity. An attacker who changed the metric value and consistently resealed the admitted identity, all nineteen validator receipts and evidence identities, the packet digest, and the caller-supplied expected digest could therefore break the original value-to-body relation.

The falsifier for this disposition would have been a documented contract that made the packet's admitted output, rather than the authorized retained source body, the out-of-band trust anchor. The frozen contract and implementation lineage do not establish that model.

## Exact bindings

The pre-edit aggregate was independently recomputed from the sorted repository-relative `.py`, `.json`, and `.md` files below `.agents/skills/kdd_data_agent/`, excluding `__pycache__`, `.pytest_cache`, and `.omc`.

| Binding | SHA-256 | Result |
| --- | --- | --- |
| Input package aggregate | `29040a66a97a50a21b02178bf494d378f709bc991aefc6b36ac8ba10294f0a02` | exact hard-gate match; 59 files |
| Corrected package aggregate | `9eea3014cb74acc48e9bbd24a486d2b6a5a4a4f57ae76191f42d037a5988b19a` | final 59-file after-manifest aggregate; every entry reverified |
| Frozen M0 packet | `82747da96d66dd8851c03edc837f38597264a07794a2b145cd530ca0a5f07b19` | unchanged |
| Frozen architecture | `9508b42979b5f708d3b0be7016ed414fd0b4c28d531b75fd0a4710eb46df8fc1` | unchanged |
| CE plan | `2b4bbd3583e2f289303b8e47b255e3b53bd0f3307f0b699b33299b57aa9e1daf` | unchanged |
| Sequencing plan | `8fec2f8c3c3d22aa9dc1b762769673789d007fd74dbbed9c34e5ea88fcd4725b` | unchanged |

Four package files changed and no package file was added or removed.

## Correction

`m0.packet.decision_metric_output_from_source_body` is now the single deterministic, technology-neutral projection from a canonical source body to the typed decision-metric output. The corrected evaluator uses that function instead of maintaining a separate output construction path.

The public `FlightReadinessPacket.deserialize` boundary now requires a transient `trusted_source_body` whenever admitted evidence is present. Before exposing the document, it canonicalizes that body, requires its digest to equal the admitted source receipt's `body_digest`, requires the admitted source receipt identity to remain current, projects the metric output from the exact body, and requires exact equality with the admitted typed output. Unadmitted evidence requires no trusted body and rejects an extra body. Construction applies the same invariant to its retained `ReadResult` body.

The trusted body is neither serialized nor returned. This preserves the existing redaction and retention boundary. The correction adds no self-referential identity layer, secret, signature, credential, network path, production data, production adapter, or capability. The existing out-of-band expected packet digest remains a separate local byte-integrity binding; the authoritative body is the value-recomputation trust boundary.

## Tests and adversarial evidence

The focused red test reproduced the exact Round 4 bypass: changing the admitted output value to `0.5`, recomputing the admitted identity, all nineteen validator receipts and evidence identities, and the packet digest, then supplying the attacker's digest, was accepted before the correction (`Failed: DID NOT RAISE`).

Round 4 had 365 tests. Round 5 adds five behavior cases and removes none, producing 370 tests. The cases cover a fully resealed changed metric value against the original trusted body, a changed trusted-body value, a stale body binding with unchanged metric output, a fully resealed stale admitted-source receipt binding, and absence of the required authoritative body.

| Evidence | Result |
| --- | --- |
| Focused source-body selection | `5 passed, 41 deselected` |
| Repository-root full suite | `370 passed in 1.46s` |
| Package-root full suite | `370 passed in 1.44s` |
| Unrelated `/private/tmp` full suite | `370 passed in 1.42s` |
| Capability/import/no-write/no-network suite | `61 passed in 0.20s`; `adapters/production` absent |
| Five hash seeds | seeds `0`, `1`, `42`, `99991`, and `random` produced identical canonical evidence |
| Named canonical builder | `kdd_data_agent.tests.canonical_packet_builder:canonical_packet_evidence` |
| Canonical serialized bytes | `47075` |
| Serialized-byte SHA-256 | `7327bdb9b280a4b89212bf217b2f6addb40ac8dbd6ba6d46a171ffeb0bfac9cc` |
| Internal packet content digest | `sha256:652a3d9f18ff980dbd56059e7d699d6914826847f4d675555137ffa2f5b4caa0` |

A fresh package copy at `/private/tmp/kdd-round5-mut.bJTz2A` replaced `_verify_authoritative_source_body` with an immediate return. The focused selection produced `4 failed, 1 passed, 41 deselected`; the exact fully resealed metric-value attack was accepted by the mutant. This demonstrates that the new public-boundary tests depend on the corrected value-to-body relation rather than incidental validation.

The full suite preserves all nineteen deterministic validators, the 19-case sealed fixture corpus, trivial baselines, decoys, conflict/provenance cases, six hard vetoes, exact gap correspondence, Round 3 relation and trusted-digest regressions, and Round 4 admitted-lineage regressions. No existing test was removed or weakened.

## Proof boundary

This is implementation-owner evidence for corrected local fixture-backed M0 behavior only, ready for fresh independent review. It is not independent acceptance. Round 4 remains rejected evidence because its reviewer identified the valid gap and was interrupted before saving a report; that interruption is not acceptance.

Phase A remains preserved and separate, not readjudicated. Production authorization is not established and production-backed capability is not demonstrated. P2, P3, and P4 remain open. M1 and M2 remain unauthorized and incomplete. No deployment, publication, or Experiment Review Committee Acceptance occurred.

No production or network read, credential use, external-system access, Git mutation, commit, push, PR, deployment, publication, or reviewer start occurred.
