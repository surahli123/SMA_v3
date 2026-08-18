# Independent Rereview — M0 Correction Round 3

## Verdict

`REJECT_LOCAL_M0_EVIDENCE`

The required 59-file package aggregate and all four frozen/supporting bindings reproduce exactly. The original trusted digest rejects a fully self-consistent CHK-05 promotion; the enumerated actor, validator-ID, outcome, reason, contract, source-receipt, source-body, derivation-input, evidence-lineage, and exact-gap mutations are rejected; all 358 tests pass from three directories; the canonical builder is invariant under five seeds; and the evaluator, corpus, drift checks, and local-only capability boundary otherwise reproduce.

The package is nevertheless not acceptable local M0 integrity evidence. A fresh attacker-digest probe changed the serialized validator receipt's typed `admitted_evidence_id` to an arbitrary valid digest, resealed the receipt/check/gap/outer identities, supplied the attacker's outer digest, and `FlightReadinessPacket.deserialize` returned the document. The field is required by the exact validator-detail schema but is omitted from `validator_evidence_identity` and is checked only for digest syntax. The passing suite has no regression for this remaining typed evidence-lineage field.

This verdict rejects only the current local fixture-backed M0 evidence claim. Phase A remains separate. Production authorization and production-backed capability, P2/P3/P4, M1/M2, deployment, publication, and Experiment Review Committee Acceptance remain open, unestablished, or unauthorized.

## Independence and scope

- The reviewer did not author the implementation or correction bytes and treated all receipts, planted truth, pass counts, and prior verdicts as unverified claims.
- No subagent or second reviewer was started. No external or production system, credential, network source, Git mutation, commit, push, deployment, publication, or other external action was used.
- Adversarial and mutation-kill work used disposable copies under `/private/tmp`.
- The only repository outputs written are this report and `independent-rereview-status.json`.

## Exact-byte binding

| Item | Independently recomputed SHA-256 | Result |
| --- | --- | --- |
| Round 3 handoff | `ec623136140e7eb25d4e4d24ebeefed5fcb435dcc01c889537b386af9cf11a16` | observed current handoff |
| Sorted 59-file package aggregate | `f32404705d3c32a9b1e09ba932db080ae1b1e63b6a55132c526457cec9e7c8ab` | exact required match; generated manifest byte-identical to `source-manifest-after.sha256` |
| Frozen packet | `82747da96d66dd8851c03edc837f38597264a07794a2b145cd530ca0a5f07b19` | exact match |
| Controlling architecture | `9508b42979b5f708d3b0be7016ed414fd0b4c28d531b75fd0a4710eb46df8fc1` | exact match |
| CE plan | `2b4bbd3583e2f289303b8e47b255e3b53bd0f3307f0b699b33299b57aa9e1daf` | exact match |
| Sequencing plan | `8fec2f8c3c3d22aa9dc1b762769673789d007fd74dbbed9c34e5ea88fcd4725b` | exact match |

The package aggregate was recomputed from sorted repository-relative `.py`, `.json`, and `.md` paths below `.agents/skills/kdd_data_agent/`, excluding `__pycache__`, `.pytest_cache`, and `.omc`. The freeze record requires the two exact artifact bindings and preserves the open external gates at `docs/research/kdd-data-agent-workshop/reviews/2026-08-18-m0-canonical-freeze/m0-canonical-freeze-record.md:10-15,48-61`. No drift block applies.

## Required verification

### Suites, test-count reconciliation, and deterministic builder

| Verification | Independent result |
| --- | --- |
| Repository root | `358 passed in 1.12s` |
| Package root | `358 passed in 1.13s` |
| Unrelated `/private/tmp` with explicit `PYTHONPATH` | `358 passed in 1.11s` |
| Capability suite | `61 passed in 0.21s` |
| Round 2 exact package | all 59 files matched the Round 3 before-manifest; `344 tests collected` |
| Round 2 to Round 3 node-ID comparison | exactly 14 additions, zero removals |
| Seeds `0`, `1`, `42`, `99991`, `random` | identical on every run |
| Serialized byte count | `46628` |
| Serialized-byte SHA-256 | `47a3e56a7de91895087d2a7ce4437aae48daf39b2abdaf027390d4cc44676ddd` |
| Internal packet digest | `sha256:9a421e1c3d003db70e14c6c9a0f4cc0263111e5c31c926b269b2948a8ebf4838` |

The 14 additions are the direct hard-veto serialized graph case plus missing/mismatched trusted digest, fully resealed promotion, present-but-wrong validator, eight enumerated validator-relation mutations, arbitrary evidence lineage, and exact gap correspondence. No prior semantic node ID disappeared or weakened. Current anchors are `.agents/skills/kdd_data_agent/tests/test_m0_packet.py:203-305` and `.agents/skills/kdd_data_agent/tests/test_m0_corrections.py:17-51`.

### Public API, validators, readiness, and evidence admission

- `.agents/skills/kdd_data_agent/m0/evaluator.py:1-21` remains the public typed evaluator API and delegates to `corrected_evaluator.py`; callers cannot provide a comparison boolean. Typed outputs are compared internally under `m0-comparison-rule/v1` and both output digests plus the comparator result are receipted at `.agents/skills/kdd_data_agent/m0/corrected_evaluator.py:158-210`.
- All nineteen named validators rejected their check-specific semantic contradiction. Separate fresh loops over every check produced `MISSING` for every absent observation and `UNKNOWN` for every malformed or garbage observation, with zero `PASS` outcomes. The validator dispatch and missing/malformed ceilings are at `.agents/skills/kdd_data_agent/m0/corrected_evaluator.py:445-510`; semantic validator examples and the common exact comparison are at `.agents/skills/kdd_data_agent/m0/corrected_evaluator.py:238-443`.
- Every evaluator-created check bound exactly one source receipt and one unique validator receipt; all nineteen evidence IDs and validator receipt IDs were unique. The deserializer enforces the pair and uniqueness at `.agents/skills/kdd_data_agent/m0/packet.py:374-443`.
- Readiness, blockers, and next-safe action are rederived from sealed checks before return at `.agents/skills/kdd_data_agent/m0/packet.py:737-785`; authorization and redaction remain contract-bound at `.agents/skills/kdd_data_agent/m0/packet.py:717-736,786-789`.
- The unauthorized/no-body fixture yields no admitted evidence, CHK-16 `FAIL`, and `not_permitted`; typed disagreement yields CHK-14 `FAIL`; `same_pipeline` yields CHK-14 `UNKNOWN`. Current tests are `.agents/skills/kdd_data_agent/tests/test_m0_reads.py:17-24,42-62,75-86`.

### Required attacks and exact gap correspondence

Calling `deserialize` without a trusted digest and with a mismatched digest failed before return. A fully resealed blocked CHK-05-to-PASS promotion failed against the original trusted digest. With the attacker digest supplied, the required present-but-wrong receipt and mutations of validator actor, validator ID, outcome, reason, contract digest, source receipt, source-body digest, derivation inputs, and arbitrary check evidence lineage all failed. The trusted binding is enforced at `.agents/skills/kdd_data_agent/m0/packet.py:627-637,671-675,790-792`; the enumerated relation checks are at `.agents/skills/kdd_data_agent/m0/packet.py:388-443`.

Fresh independently constructed mutations of CHK-05 gap reason, evidence references, materiality, rule source, and next-safe-check all failed. Exact correspondence is enforced at `.agents/skills/kdd_data_agent/m0/packet.py:446-476,702-715,785`.

### Corpus, baselines, decoys, conflict, vetoes, and independent drift kills

All nineteen planted cases ran through the public evaluator: one `decision_grade`, one `directional_only`, and seventeen `not_permitted`. Both trivial baselines were contradicted. The three decoys, reviewer conflict, and all six typed hard vetoes reached their fail-closed outcomes through the same evaluator. The executable path and truth comparison are `.agents/skills/kdd_data_agent/m0/validation.py:135-157,160-220`; assertions are `.agents/skills/kdd_data_agent/tests/test_m0_hard_vetoes.py:18-63`.

In disposable package copies:

- changing the trusted fixture bytes without its pin was killed during collection with `fixture bytes drifted for m0-read-trusted-001`;
- changing only planted truth was killed with `real evaluator contradicted planted truth for m0-trusted`;
- disabling the trusted-digest comparison produced the two intended trusted-digest regression failures;
- disabling the check-relation verifier produced twelve intended serialized-boundary failures; and
- disabling the gap verifier produced the intended exact-gap regression failure.

Fixture byte binding is implemented at `.agents/skills/kdd_data_agent/m0/validation.py:132-157`; real evaluator/truth comparison is at `.agents/skills/kdd_data_agent/m0/validation.py:160-220`.

### Frozen and local-only capability boundary

The four frozen/supporting hashes remained invariant. `.agents/skills/kdd_data_agent/core/capabilities.py:18-38` declares only `fixture_read`, `local_deterministic_compute`, and `in_memory_append`; `adapters/production` is absent. This is static and fixture-local capability evidence only, consistent with the freeze's explicit separation of program capability, per-Flight readiness, production authorization, and Committee Acceptance at `docs/research/kdd-data-agent-workshop/reviews/2026-08-18-m0-canonical-freeze/m0-canonical-freeze-record.md:38-61`.

## Findings

### IR-M0-01-RR — BLOCKER: serialized admitted-evidence lineage is syntactic, not relationally bound

**Current anchors:** `.agents/skills/kdd_data_agent/m0/packet.py:314-328`; `.agents/skills/kdd_data_agent/m0/packet.py:388-425`; `.agents/skills/kdd_data_agent/m0/corrected_evaluator.py:118-136`; `.agents/skills/kdd_data_agent/m0/corrected_evaluator.py:485-510`.

`corrected_evaluator` places the admitted record's `evidence_id` in every validator receipt as `admitted_evidence_id`. Deserialization requires that field in the exact validator-detail schema, but `validator_evidence_identity` omits it. The verifier accepts any non-null value that merely has digest syntax and has no serialized admitted-evidence record against which to recompute it.

Fresh attack result:

```text
ACCEPTED_INVALID_ATTACKER_ADMITTED_EVIDENCE_ID
```

The attack began with a blocked CHK-05 packet, changed only `detail.admitted_evidence_id` to `sha256:` plus 64 zeros, recomputed the validator receipt ID/digest, rebound and resealed the CHK-05 check and gap, recomputed the outer packet digest, supplied that attacker digest, and received a deserialized document.

**Impact:** a serialized packet accepted by the public verifier can make a false typed claim about which evidence record was admitted. That breaks the required exact evidence-lineage graph and prevents the packet from serving as trustworthy local fixture-backed integrity evidence, even though the original trusted digest still prevents substituting these bytes for the original packet.

**Minimal correction:** either serialize the admitted `EvidenceRecord` (or an equivalent deterministic identity payload) and recompute `admitted_evidence_id` from its exact receipt, contract, and typed output fields during deserialization, or remove the unverifiable field and any claim that it is bound lineage. Include the field in `validator_evidence_identity`, enforce its expected `None`/digest relation, and add attacker-digest regressions for both arbitrary replacement and unauthorized `None -> digest` promotion.

### IR-M0-TEST-RR — MAJOR: the Round 3 relational matrix omits admitted-evidence identity

**Current anchors:** `.agents/skills/kdd_data_agent/tests/test_m0_packet.py:241-292`; `.agents/skills/kdd_data_agent/m0/packet.py:389-425`.

The eight parameterized mutations cover actor, validator ID, outcome, reason, contract digest, source receipt, source-body digest, and derivation inputs; the separate case covers arbitrary check `evidence_ids`. None mutates `detail.admitted_evidence_id`, although that field is mandatory in the exact schema. Consequently all 358 tests pass while the attack above is accepted.

**Impact:** the suite can report a complete relation-graph seal while leaving one serialized evidence-lineage claim attacker-controlled.

**Minimal correction:** add public-deserializer tests that fully reseal `admitted_evidence_id` mutations under the attacker digest, including an authorized packet's real-ID replacement and an unauthorized/no-body packet's `None -> digest` replacement; require rejection before returning a document.

## Disposition and preserved boundaries

| Item | Independent disposition | Basis |
| --- | --- | --- |
| `IR-M0-01-RR` | `REJECTED` | original trusted digest and enumerated relations close, but admitted-evidence lineage remains unbound |
| `IR-M0-TEST-RR` | `REJECTED` | 14 valid additions and no removals, but the remaining typed lineage attack is absent |
| `IR-M0-02` | `PRESERVED_CORRECTED` | unauthorized/no-body evaluator path remains fail-closed |
| `IR-M0-03-RR` | `PRESERVED_CORRECTED` | all nineteen validators and missing/malformed/garbage ceilings pass |
| `IR-M0-04` | `PRESERVED_CORRECTED` | typed outputs are compared internally under the versioned rule |
| `IR-M0-05` | `PLUMBING_PRESERVED_WITH_REJECTING_SERIALIZATION_DEPENDENCY` | corpus, baselines, decoys, conflict, vetoes, and drift checks execute correctly |
| `IR-M0-06` | `PRESERVED_CORRECTED` | five-seed named builder and both digest namespaces reproduce |

No part of this rereview promotes Phase A evidence, establishes production authorization or production-backed M0 capability, closes P2/P3/P4, authorizes or completes M1/M2, deploys, publishes, or establishes Experiment Review Committee Acceptance.
