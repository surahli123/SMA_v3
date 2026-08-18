# M0 Correction Round 4 Receipt

Completed: `2026-08-18T04:09:39-07:00`  
Run boundary: one Owner-authorized local correction run for the remaining admitted-evidence lineage defect and its missing tests only  
Terminal implementation state: `CORRECTED_LOCAL_INTEGRITY_EVIDENCE_READY_FOR_INDEPENDENT_REREVIEW`

## Exact bindings

The pre-edit aggregate was independently recomputed from the sorted repository-relative `.py`, `.json`, and `.md` files below `.agents/skills/kdd_data_agent/`, excluding `__pycache__`, `.pytest_cache`, and `.omc`.

| Binding | SHA-256 | Result |
| --- | --- | --- |
| Input package aggregate | `f32404705d3c32a9b1e09ba932db080ae1b1e63b6a55132c526457cec9e7c8ab` | exact hard-gate match; 59 files; byte-identical to the Round 3 after-manifest |
| Corrected package aggregate | `29040a66a97a50a21b02178bf494d378f709bc991aefc6b36ac8ba10294f0a02` | final 59-file manifest aggregate; every entry reverified |
| Frozen M0 packet | `82747da96d66dd8851c03edc837f38597264a07794a2b145cd530ca0a5f07b19` | unchanged |
| Frozen architecture | `9508b42979b5f708d3b0be7016ed414fd0b4c28d531b75fd0a4710eb46df8fc1` | unchanged |
| CE plan | `2b4bbd3583e2f289303b8e47b255e3b53bd0f3307f0b699b33299b57aa9e1daf` | unchanged |
| Sequencing plan | `8fec2f8c3c3d22aa9dc1b762769673789d007fd74dbbed9c34e5ea88fcd4725b` | unchanged |

Three package files changed and no package file was added or removed.

## Correction

The evaluator and serialized boundary now share one canonical admitted-evidence identity formula over the exact source receipt ID, frozen contract digest, canonical typed decision-metric output, and observed state. The packet serializes one minimal typed `admitted_evidence` object containing those fields and the recomputed identity. Unauthorized or otherwise unadmitted reads serialize `None`.

Construction and deserialization validate the exact payload and output schemas, require `observed` to be true, bind the payload to an authorized trusted body-bearing source receipt under the same source, interval, authorization, redaction, and frozen contract, and require the typed output identity to match the frozen decision metric. The stated admitted-evidence ID is recomputed rather than trusted. Every validator receipt must carry exactly that recomputed ID, or `None` when the packet payload is `None`; the verified payload itself is included in each check-specific validator evidence identity.

This remains an unkeyed local integrity contract protected at packet exposure by Round 3's required out-of-band expected packet digest. It is not a signature, secret, credential, authenticity guarantee, production authorization, or authority claim. No raw production data was added.

## Tests and adversarial evidence

Round 3 had 358 tests. Round 4 adds seven behavior cases and removes none, producing 365 tests: arbitrary admitted-ID replacement; stale payload identity; missing and extra exact-schema fields; fully resealed wrong typed-output relation; unauthorized `None`-to-digest promotion; and a fully resealed unauthorized forged payload.

| Evidence | Result |
| --- | --- |
| Initial focused red phase | new boundary cases failed because `admitted_evidence` did not exist and the old identity graph could not validate it |
| Final focused packet suite | `41 passed in 0.43s` |
| Repository-root full suite | `365 passed in 1.34s` |
| Package-root full suite | `365 passed in 1.34s` |
| Unrelated `/private/tmp` full suite | `365 passed in 1.33s` |
| Capability/import/no-write/no-network suite | `61 passed in 0.20s`; no `adapters/production` directory |
| Five hash seeds | seeds `0`, `1`, `42`, `99991`, and `random` produced identical canonical evidence |
| Canonical serialized bytes | `47075` |
| Serialized-byte SHA-256 | `7327bdb9b280a4b89212bf217b2f6addb40ac8dbd6ba6d46a171ffeb0bfac9cc` |
| Internal packet content digest | `sha256:652a3d9f18ff980dbd56059e7d699d6914826847f4d675555137ffa2f5b4caa0` |

A fresh package copy at `/private/tmp/kdd-round4-mut.H03p9S` bypassed both construction-time and deserialization-time calls to the admitted-evidence verifier while leaving the remainder of the graph intact. The admitted-lineage selection produced `5 failed, 2 passed`; the fully resealed wrong-output packet was accepted by the mutant, proving the new relation test is behavior-bearing. The live package rejects it.

The full suite continued to exercise all nineteen named validators and sealed corpus cases, trivial baselines, decoys, conflict/provenance behavior, six hard vetoes, the exact gap graph, and the trusted expected-digest boundary through the public evaluator. The five-axis owner review found no remaining critical correctness, readability, architecture, security, or performance issue in this narrow change. No dependency or capability was added.

## Proof boundary

This run establishes implementation-owner evidence for corrected local fixture-backed integrity, ready for a fresh independent rereview. It does not self-accept the correction. Phase A remains separate and was not readjudicated. Production authorization and production-backed capability remain unestablished; P2/P3/P4 remain open; M1/M2 remain unauthorized and incomplete; no deployment, publication, or Experiment Review Committee Acceptance occurred.

No production or network read, credential, external system, Git mutation, commit, push, PR, deployment, publication, or reviewer start occurred.
