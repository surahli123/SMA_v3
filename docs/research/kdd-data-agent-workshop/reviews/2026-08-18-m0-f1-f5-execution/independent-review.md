# Independent Code-and-Evidence Review — Local M0-F1 through M0-F5

## Verdict

`REJECT_LOCAL_M0_EVIDENCE`

The exact review target is present and reproducible, so this is not a drift block. The three-directory test suite is green and the Phase A mechanical corrections survive independent mutation testing. However, the local M0 completion claim is not supported: a blocked packet can be reconstructed as decision-grade, an unauthorized source receipt can produce an eligible packet, most of the nineteen checks default to PASS without implementing their named validation, the F5 corpus is disconnected metadata, and the receipt's canonical packet byte/digest claim is false.

This verdict rejects the claimed local M0 evidence package. It grants no production authorization or capability, and it does not close P2, P3, P4, M1, M2, deployment, publication, or Committee Acceptance.

## Independence and scope

- The reviewer did not author the implementation bytes and treated the implementation receipt, completion ledger, status JSON, and `314 passed` claim as untrusted inputs.
- All destructive probes and mutations ran only in fresh disposable copies under `/private/tmp/kdd-m0-independent-review.vzgdnd`.
- No subagent or reviewer lane was started for this run. No production system, credential, network source, deployment, Git mutation, commit, push, or external publication was used.
- The prior Phase A review was used only to identify hypotheses for independent reproduction.

## Exact-byte binding

| Item | Independently recomputed SHA-256 | Result |
| --- | --- | --- |
| Review handoff | `1ecfc9b6316d0cfc2b88230cf9509220de685607381fc72ecd55b413bb1d1584` | exact match |
| Sorted package source manifest aggregate | `30d6b47ca55f1444ef8ba596aedabd90db5f21af58e60d53ad2320a5fc94c196` | exact match |
| Frozen packet | `82747da96d66dd8851c03edc837f38597264a07794a2b145cd530ca0a5f07b19` | exact match |
| Frozen architecture | `9508b42979b5f708d3b0be7016ed414fd0b4c28d531b75fd0a4710eb46df8fc1` | exact match |
| CE plan | `2b4bbd3583e2f289303b8e47b255e3b53bd0f3307f0b699b33299b57aa9e1daf` | exact match |
| Sequencing plan | `8fec2f8c3c3d22aa9dc1b762769673789d007fd74dbbed9c34e5ea88fcd4725b` | exact match |

The frozen v6 patch/review/status and steelman closure bindings also matched the freeze record. Aggregate identity is established; semantic acceptance is not.

## Independent reproduction

### Three working directories

The mandated command form was reproduced with `PYTHONDONTWRITEBYTECODE=1`, `-p no:cacheprovider`, and explicit `PYTHONPATH` for the unrelated temporary directory:

| Working directory | Result |
| --- | --- |
| Repository root | `314 passed in 0.45s` |
| Package root | `314 passed in 0.45s` |
| Unrelated `/private/tmp` directory | `314 passed in 0.44s` |

### Canonical packet reproduction

Five fresh processes with `PYTHONHASHSEED=0,1,42,99991,random` each executed the only canonical trusted builder found, `kdd_data_agent.tests._m0_fixtures.packet_for().serialize()`. Every process produced the same actual values:

```text
bytes: 18772
serialized_sha256: c8e4d7f4c813008793ad78ff8f79620673fa2492f6d89d4c25a0852bd25d58cc
internal_packet_digest: sha256:d51631746ee339681ac0c86d5ceb819dc587089d375274b03d7a5fdc65f9db79
```

The claimed values were 18,740 bytes and `51b7bc3bdeebb9422d022dcf293b63bb29d10d21a34b305bbc7a6a8e44a4f0f9`. Repository-wide search found those claimed values only in the handoff, receipt, and status, not in another canonical builder.

### Adversarial probes

The disposable probe returned:

```text
replace_bypass not_permitted FAIL decision_grade eligible FAIL
unauthorized_receipt_bypass unauthorized False decision_grade eligible PASS
matrix_manifest_overlap 0 13 8
baseline_result ('always_ready:contradicted', 'always_blocked:contradicted')
```

The first line promotes a packet that still contains CHK-16 `FAIL`. The second line passes the actual unauthorized, no-body fixture receipt into the evaluator and obtains CHK-16 `PASS`, `decision_grade`, and `eligible`. The third line proves that none of the thirteen advertised F5 case IDs is present in the eight-case executable manifest.

## Phase A mutation sensitivity

Each mutation was applied to its own fresh disposable package copy. A focused suite failure is the expected killed-mutation result.

| Mutation | Focused result | Disposition |
| --- | --- | --- |
| Remove `redaction_state` from receipt identity | `2 failed, 24 passed` | killed |
| Parse unknown authorization as authorized | `5 failed, 53 passed` | killed |
| Bypass registered rule-source membership | `1 failed, 25 passed` | killed |
| Remove per-revision verification from seal chain | `2 failed, 17 passed` | killed |
| Plant dead-branch relative production import | `1 failed, 60 passed` | killed |
| Plant a symlinked package directory | `6 failed, 55 passed` | killed |
| Remove resolved fixture-containment check | `1 failed, 57 passed` | killed |
| Replace a seam packet reference with garbage | authority test failed; one unrelated temp-layout path failure excluded | killed |
| Remove adapter authorization body guard | `2 failed, 82 passed`; Receipt-level guard also remained active | killed with defense in depth |

This independently supports the Phase A closure claims for receipt identity, fail-closed parsing, rule resolution, seal verification, import/symlink scanning, containment, seam authority, and retained-body policy. It does not cure the M0 semantic failures below.

## Findings

### IR-M0-01 — BLOCKER: public packet reconstruction permits false readiness

**Current anchors:** `.agents/skills/kdd_data_agent/m0/packet.py:130-158`; `.agents/skills/kdd_data_agent/m0/packet.py:160-166`; `.agents/skills/kdd_data_agent/tests/test_m0_contracts.py:72-78`.

`FlightReadinessPacket.__post_init__` checks shape, receipt presence, and contract authorization equality, but it never derives or validates `analysis_use`, blockers, next action, or gaps from the check results. `dataclasses.replace(blocked, analysis_use=DECISION_GRADE)` is accepted, derives `eligible`, and retains CHK-16 `FAIL`. The existing immutability test covers direct field assignment only, not reconstruction through the public dataclass constructor.

**Impact:** an in-process caller can mint a sealed-looking false-readiness packet that violates the frozen hard veto and readiness contract.

**Minimal correction:** make packet construction factory-only, or recompute and require exact equality of readiness, blockers, next action, and required gaps from the checks in `__post_init__`; add reconstruction, deserialization, and tampered-packet tests.

### IR-M0-02 — BLOCKER: unauthorized source receipts are accepted as decision evidence

**Current anchors:** `.agents/skills/kdd_data_agent/m0/evaluator.py:33-45`; `.agents/skills/kdd_data_agent/m0/evaluator.py:57-63`; `.agents/skills/kdd_data_agent/m0/evaluator.py:66-111`; `.agents/skills/kdd_data_agent/m0/evaluator.py:147-175`; `.agents/skills/kdd_data_agent/m0/checks.py:225-226`; `.agents/skills/kdd_data_agent/m0/packet.py:149-156`.

The code defines `admit_observed_evidence`, but `build_recomputation_evidence` and `evaluate_flight` never call it. They do not bind the reported receipt's source, snapshot, interval, authorization, redaction, outcome, retained body, or contract digest to the contract. CHK-16 examines contract fields only. The actual `m0-read-unauthorized-001` receipt therefore drives a decision-grade eligible packet.

**Impact:** the evaluator admits the exact false-evidence path the authorization and false-readiness hard vetoes are supposed to prohibit.

**Minimal correction:** require a `ReadResult` or typed admitted-evidence record, call the admission gate before recomputation, verify all source/interval/auth/redaction/outcome/body bindings against the contract, and map any non-admitted or mismatched receipt to a material fail-closed check.

### IR-M0-03 — BLOCKER: unimplemented material checks default to PASS

**Current anchors:** `.agents/skills/kdd_data_agent/m0/checks.py:180-226`; `.agents/skills/kdd_data_agent/m0/checks.py:244-260`; `.agents/skills/kdd_data_agent/tests/test_m0_checks.py:93-104`.

The evaluator computes only identity decoys, ratio variance presence, runtime, arm parity, contract authorization/redaction, and sample sufficiency. Every other registry entry is filled with `CheckOverride(PASS, NON_MATERIAL, "check passed", ...)`, and every check receives the same receipt IDs and synthetic evidence IDs. Tests for many named material failures inject caller-controlled overrides instead of executing validators.

**Impact:** absent validation is represented as positive evidence. SRM/compositional SRM, exposure integrity, population/scope, numerator/denominator/join arithmetic, completeness/pagination/late arrival, estimator consistency, scorecard reconciliation, source-change revalidation, cross-read attribution/freshness/scope, and disagreement/gap closure can all appear PASS without being evaluated.

**Minimal correction:** require an explicit validator result and check-specific evidence binding for all nineteen checks. A missing validator or missing evidence must yield `MISSING` or `UNKNOWN` and apply the material ceiling; no registry check may have a default PASS path.

### IR-M0-04 — MAJOR: D4/D6 comparison is a caller assertion, not a recomputation comparison

**Current anchors:** `.agents/skills/kdd_data_agent/m0/evaluator.py:48-63`; `.agents/skills/kdd_data_agent/m0/evaluator.py:66-110`; `.agents/skills/kdd_data_agent/m0/evaluator.py:155-168`.

The recomputed output is accepted only as an arbitrary digest string, while `comparison_matches` is a caller-provided boolean defaulting to `True`. No reported output value or digest is extracted and no versioned comparator is executed. CHK-14 fails only when the caller says the comparison failed.

**Impact:** the claimed independent D4/D6 recomputation can be marked matching without any executable comparison, so decision-grade readiness is not independently supported.

**Minimal correction:** accept typed reported and recomputed outputs, derive the comparison result inside the evaluator using the contract-bound comparison rule, record both input digests and comparator digest, and remove the public boolean assertion.

### IR-M0-05 — BLOCKER: F5 matrix, baselines, provenance, and hard vetoes are disconnected metadata

**Current anchors:** `.agents/skills/kdd_data_agent/m0/validation.py:32-78`; `.agents/skills/kdd_data_agent/m0/validation.py:84-90`; `.agents/skills/kdd_data_agent/m0/validation.py:93-111`; `.agents/skills/kdd_data_agent/tests/test_m0_hard_vetoes.py:18-61`; `.agents/skills/kdd_data_agent/evals/fixtures/m0/manifest.json:1-44`; `.agents/skills/kdd_data_agent/adapters/fixture.py:78-84`; `.agents/skills/kdd_data_agent/adapters/fixture.py:161-166`.

`FIXTURE_MATRIX` digests its own labels rather than fixture bytes. Its thirteen IDs have zero overlap with the eight manifest IDs. The manifest still records `alignment_pending` for every final readiness. The baseline function merely observes that its own labels contain at least one ready and one blocked row; it never runs an evaluator. Hard-veto tests call `hard_veto(kind)` directly, but the evaluator does not integrate those vetoes. Decoy tests inject `ObservedReadIdentity` rather than executing sealed decoy fixture cases.

**Impact:** F5-001 through F5-005 are self-referential and do not prove that the real evaluator rejects trivial baselines, unauthorized/stale/partial/conflicting/superseded inputs, reviewer conflicts, or hard-veto conditions.

**Minimal correction:** create one byte-bound executable manifest containing every required scenario and planted truth; execute all cases, both trivial evaluators, decoys, reviewer-conflict paths, and hard vetoes through the real evaluator; compare observed packet results to independently authored truth.

### IR-M0-06 — MAJOR: the implementation receipt's canonical packet evidence is false

**Current anchors:** `docs/research/kdd-data-agent-workshop/reviews/2026-08-18-m0-f1-f5-execution/independent-review-handoff.md:12`; `docs/research/kdd-data-agent-workshop/reviews/2026-08-18-m0-f1-f5-execution/implementation-receipt.md:42-45`; `docs/research/kdd-data-agent-workshop/reviews/2026-08-18-m0-f1-f5-execution/implementation-status.json:12-16`; `.agents/skills/kdd_data_agent/tests/_m0_fixtures.py:102-119`.

The named canonical builder is hash-seed stable, but it produces 18,772 bytes, serialized SHA-256 `c8e4d7f4...`, and internal packet digest `sha256:d5163174...`, not the claimed 18,740 bytes and `51b7bc3b...`.

**Impact:** the handoff's required packet evidence cannot be reproduced and the receipt/status do not accurately identify the reviewed packet bytes.

**Minimal correction:** regenerate the byte count, serialized digest, and internal packet digest from the exact canonical builder; record the command and distinguish serialized-byte SHA-256 from the packet's internal content digest.

## Completion-ledger disposition

| Ledger class | Independent disposition | Basis |
| --- | --- | --- |
| Phase A correction closure | verified for the nine mandated mutation classes | all mutations were killed in isolated copies |
| Run prerequisites and frozen binding | verified | exact package aggregate and frozen digests match |
| M0-F1 | rejected | public false-readiness reconstruction invalidates packet/readiness integrity |
| M0-F2 | rejected | unauthorized receipt admission and caller-asserted D4/D6 comparison |
| M0-F3 | rejected | most named checks default to PASS without validators |
| M0-F4 | rejected | reconstructed false-ready packet can retain failed checks; packet evidence receipt is wrong |
| M0-F5 | rejected | metadata-only matrix, baselines, provenance, decoys, and hard vetoes are not executed against the real corpus/evaluator |

## Preserved proof boundaries

The matching aggregate, frozen bindings, green suite, and Phase A mutation results remain valid local evidence for their narrow claims. They do not outweigh the reproduced false-readiness paths or establish local M0 completion. No conclusion in this review authorizes production capability, a production read, P2/P3/P4, M1/M2, deployment, publication, or Committee Acceptance.

## Conflicts and limitations

- The implementation author also authored the fixture builder, evaluator tests, completion ledger, and receipt; this review therefore independently executed bytes and adversarial probes rather than adopting those conclusions.
- The review is local and fixture-only. It did not and was not authorized to test production systems.
- The seam mutation's focused run also encountered one expected disposable-layout missing-doc path; that unrelated harness failure was excluded, while the targeted garbage-authority assertion independently failed.
