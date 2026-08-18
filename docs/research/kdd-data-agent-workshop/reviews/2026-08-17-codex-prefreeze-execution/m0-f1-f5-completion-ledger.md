# M0-F1 through M0-F5 Completion Ledger

Status: `DRAFT_ACCEPTANCE_LEDGER_NOT_EXECUTED`  
Scope: one future bounded, local, hermetic M0-F1-F5 run  
Binding: the final packet/spec path, revision, and SHA-256 values must come from the accepted start receipt.

This ledger defines observable completion evidence. It does not report that implementation has started or that any row has passed.

## Binding and run-level prerequisites

| ID | Requirement | Observable evidence | Current state |
| --- | --- | --- | --- |
| `RUN-BIND-001` | Exact packet and controlling-spec binding | Start receipt and every semantic unit record the same final paths, revision labels, and SHA-256 values; recomputation matches before and after the run | `UNVERIFIED` |
| `RUN-AUTH-001` | Fresh independent verdicts and Owner start | Exact-digest independent verdicts plus Owner acknowledgement and one-run authorization exist and predate implementation | `UNVERIFIED` |
| `RUN-BUDGET-001` | Bounded execution | Named lead, active-time cap, full-suite cap, read cap, tool cap, expiry, halt owner, and actual usage are recorded | `UNVERIFIED` |
| `RUN-ISO-001` | Authorized local roots only | Before/after file inventory and dirty-state receipt prove no canonical docs, protected references, production paths, Git state, or external state changed | `UNVERIFIED` |

## M0-F1 — Contracts and packet shape

| ID | Requirement | Observable acceptance evidence | Current state |
| --- | --- | --- | --- |
| `F1-001` | Contract completeness and fail-closed unknowns | Schema/constructor tests reject missing Flight identity, units, estimator, source, authorization, named roles, digest, and required policy inputs without guessing | `UNVERIFIED` |
| `F1-002` | Single stored readiness state | Serialized packet stores `analysis_use` only; attempts to persist or independently set `post_analysis_eligibility` fail; renderer projection is exactly `decision_grade -> eligible`, otherwise `blocked` | `UNVERIFIED` |
| `F1-003` | Declared sufficiency without post-hoc power | Policy accepts only `runtime_only | runtime_and_sample`; tests prove observed runtime/sample compare only with preregistered inputs and no achieved/post-hoc power field or computation is reachable | `UNVERIFIED` |
| `F1-004` | Sufficiency failure mapping | Failed declared threshold with no other blocker produces `directional_only`; missing required `runtime_and_sample` inputs produces `not_permitted` plus `contract_correction` | `UNVERIFIED` |
| `F1-005` | Arm-parity applicability | Missing required per-arm identities produces `MISSING`, `not_permitted`, and `evidence_collection`; a versioned applicability rule alone permits `NOT_APPLICABLE`; divergent applicable arms produce material `FAIL` | `UNVERIFIED` |
| `F1-006` | Materiality and typed next action | Unknown/unclassified materiality remains stored as `unknown` while applying a material ceiling; `non_material` and `NOT_APPLICABLE` require versioned rules; next-action enum has only the five accepted values and no exact target/diff | `UNVERIFIED` |
| `F1-007` | Immutable history and packet envelope | Revision, predecessor, supersession, authorization/redaction, expiry, digest, and named-human fields validate and cannot be mutated in place | `UNVERIFIED` |

## M0-F2 — Fixture reads, Evidence, and recomputation

| ID | Requirement | Observable acceptance evidence | Current state |
| --- | --- | --- | --- |
| `F2-001` | Fixture-only adapter boundary | Import/capability scan and runtime probes show no production adapter, network, secret, subprocess, arbitrary execution, mutation, messaging, or publication capability | `UNVERIFIED` |
| `F2-002` | Typed read outcomes | Trusted, blocked, partial, stale, conflicting, unauthorized, unavailable, and redaction-failure fixtures produce their exact typed receipts and Coverage Gaps | `UNVERIFIED` |
| `F2-003` | No false Evidence | Zero reads, partial pages, denial, unavailable source, and no-body redaction failure cannot establish observed Evidence or a complete result | `UNVERIFIED` |
| `F2-004` | Independent recomputation | Reported and independently recomputed metric reads carry separate source/derivation receipts, and disagreement remains visible and fail-closed | `UNVERIFIED` |
| `F2-005` | Append-only and isolated | New observations append revisions; cases, authorization, receipts, and fixture identities do not leak or overwrite across case boundaries | `UNVERIFIED` |

## M0-F3 — Deterministic readiness checks

| ID | Requirement | Observable acceptance evidence | Current state |
| --- | --- | --- | --- |
| `F3-001` | Exact frozen inventory | Registry/test enumerates all 19 accepted checks once, with stable IDs, rule sources, outcomes, materiality, receipts, reasons, and reopen conditions | `UNVERIFIED` |
| `F3-002` | Trusted decision-grade case | Complete authorized consistent fixture produces stored `analysis_use=decision_grade`, derived `eligible`, and no M1/M2 object | `UNVERIFIED` |
| `F3-003` | Runtime/sample directional case | Pre-runtime and declared sample-insufficient fixtures produce stored `directional_only`, derived `blocked`, and no M1 promotion; no post-hoc power is computed | `UNVERIFIED` |
| `F3-004` | Contract-incomplete sufficiency case | `runtime_and_sample` with missing required inputs produces check `MISSING`, stored `not_permitted`, derived `blocked`, and `contract_correction` | `UNVERIFIED` |
| `F3-005` | Material validity and authority cases | SRM, CUPED-mode, unit/ratio-estimator, source-version, arm-parity, ACL/isolation, and material Evidence failures produce stored `not_permitted` and derived `blocked` | `UNVERIFIED` |
| `F3-006` | Deterministic reproduction | Two clean evaluations over identical frozen inputs reproduce byte-identical checks and packet digest | `UNVERIFIED` |

## M0-F4 — Immutable packet and synthetic review projection

| ID | Requirement | Observable acceptance evidence | Current state |
| --- | --- | --- | --- |
| `F4-001` | Immutable seal and supersession | Packet digest is reproducible; corrected input creates a new packet/digest and invalidates old acknowledgement without editing history | `UNVERIFIED` |
| `F4-002` | Derived eligibility projection | Presenter derives eligibility from sealed `analysis_use`, cannot persist a second readiness field, and shows the same packet digest on every view | `UNVERIFIED` |
| `F4-003` | Review completeness | Blockers, disagreements, Coverage Gaps, source/read/derivation/check receipts, typed next action, and named human state are reachable from the synthetic projection | `UNVERIFIED` |
| `F4-004` | M0 contamination barrier | Packet rejects Cause Claims, product-logic candidates/rankings/Recommendations, Win/Loss labels, and Trace-only facts; remediation link resolves only to the separately gated artifact | `UNVERIFIED` |
| `F4-005` | P3 separation | Evidence labels the projection as synthetic `VAL-UI-001`; `VAL-UI-101` remains unpassed without a named live-review receipt | `UNVERIFIED` |

## M0-F5 — Fixtures, adversarial controls, and review evidence

| ID | Requirement | Observable acceptance evidence | Current state |
| --- | --- | --- | --- |
| `F5-001` | Required fixture matrix | Sealed fixtures cover trusted, directional, invalid, materially unknown, conflicting, stale, partial, unauthorized, superseded, and reviewer-conflict cases | `UNVERIFIED` |
| `F5-002` | Trivial-baseline rejection | Always-ready and always-blocked evaluators are each contradicted by sealed planted truth; otherwise suite stops before Agent scoring | `UNVERIFIED` |
| `F5-003` | Adversarial decoys | Metric-version, CUPED-mode, and source-identity decoys are caught by their exact validators | `UNVERIFIED` |
| `F5-004` | Reviewer provenance | Every sealed fixture records author, evaluator/reviewer, and independence or disclosed conflict; conflict remains visible and unresolved by timeout/seniority | `UNVERIFIED` |
| `F5-005` | Hard vetoes | False readiness, cross-case/tenant leakage, secret exposure, unsafe redaction, write reachability, or unauthorized delivery produces hard NO-GO independent of aggregate results | `UNVERIFIED` |
| `F5-006` | Threshold-free evidence | Review correctness, resource use, and failures are recorded without invented numeric GO thresholds or production claims | `UNVERIFIED` |

## Completion-state separation

These states require separate evidence and must never be collapsed:

| State | Meaning | Evidence required | What it does not prove |
| --- | --- | --- | --- |
| **Phase A verification** | Existing semantics-independent foundation reproduces under the reviewed package aggregate | Independent exact-aggregate verdict, commands, tests/probes, gaps, and unchanged-byte receipt | M0-F1-F5 implementation, accepted freeze, production safety, or Committee Acceptance |
| **Local M0 MVP completion** | Every M0-F1-F5 ledger row passes under one accepted binding and bounded run | Exact-digest start receipt, hermetic implementation evidence, deterministic packet/check evidence, fixtures, hard vetoes, and completion receipt | P2/P3/P4 closure, a real production Flight decision, M1/M2 start, or production authorization |
| **Production authorization** | A named source/credential/scope/ACL/retention/load/halt path is approved for a specific production use | P2 or narrower exact authority receipt plus least-privilege and write-denial evidence | Product correctness, Committee Acceptance, mutation authority, or authorization for other sources/rungs |
| **Committee Acceptance** | The Experiment Review Committee decides pass/change/block for one real Flight | Immutable real-Flight packet, Experiment Owner evidence, independent DS challenge, exact Committee ruling and digest-bound acknowledgement | Agent execution, deployment, publication, or generalized production readiness |

## Ledger close rule

The bounded run may report `COMPLETE_LOCAL_M0_EVIDENCE` only when every `F1-*` through `F5-*` row is `VERIFIED`, all run-level prerequisites are `VERIFIED`, and no halt condition is open. Any missing row yields `PARTIAL_HALTED` or `NOT_STARTED`, with the exact blocker and next safe action preserved.

