# Codex Disposition of Opus 5 Enterprise Plan Findings

Date: 2026-08-15
Status: canonical-document reconciliation applied locally; not committed, pushed, or approved for implementation
Scope: documentation only; no implementation, production access, mutation, commit, push, PR, or deployment

## Authority and Method

This ledger disposes all 38 findings in the [Opus 5 final review](00-final-review.md): B1-B14 and M1-M24. Owner-confirmed contracts and specialist adjudications control over reviewer proposals. `ACCEPT` means the supported contract correction is staged. `PARTIAL` means only the narrowed specialist-approved correction is staged. `OWNER CONFIRMED` means the previously deferred product decision has now been made directly by the owner.

Canonical actions were reconciled against the current working tree by the main orchestrator. This ledger records documentation disposition only and does not authorize implementation, production access, mutation, deployment, or publication.

## Finding Ledger

| ID | Disposition | Evidence anchor | Canonical action and remaining gate |
| --- | --- | --- | --- |
| B1 | ACCEPT | [Review B1](00-final-review.md); [architecture G2 and exact target](../../final-architecture-spec.md) | Add a technology-neutral SymbolAttribution port. File-only identity makes G2 inconclusive and blocks an exact code target. Add U6 and acceptance tests. |
| B2 | OWNER CONFIRMED | [Review B2](00-final-review.md); [enterprise profile](../../enterprise-experiment-post-analysis-profile.md); [planning packet](../../planning-decision-packet.md) | Owner ruling on 2026-08-16: the first approved build/funding slice and main deliverable is M0 Flight Readiness only, producing `ExperimentReadContract` and `FlightReadinessPacket`. M1 Metric Movement and M2 Win/Loss remain direction-only and receive no funding in this slice. The broader architecture remains intact. This scope ruling does not itself authorize implementation. |
| B3 | PARTIAL | [Review B3](00-final-review.md); [sequencing protected paths](../../implementation-sequencing.md); [architecture reuse boundary](../../final-architecture-spec.md) | State the clean-room boundary: protected paths are read-only references, not migration targets; no legacy runtime import, stage/schema/threshold copy, or authority claim. Direct reuse requires interface, provenance, tests, security, and license review. Unmanifested or screenshot-observed components remain unavailable. |
| B4 | ACCEPT | [Review B4](00-final-review.md); [DeepSeek Trace research](../../deepseek-harness-practices.md) | Separate canonical packet projections from independently collected diagnostic Trace. Evidence controls divergence; Trace is never Evidence or counterevidence. |
| B5 | ACCEPT | [Review B5](00-final-review.md); [packet and Trace contracts](../../final-architecture-spec.md) | Use a versioned non-digested Trace-navigation annex. Keep Trace out of the immutable packet digest; stable cross-links remain authorization-scoped. Future alternatives remain an Engineering/P2 decision. |
| B6 | ACCEPT | [Review B6](00-final-review.md); [security contract](../../final-architecture-spec.md) | Add typed no-body `redaction_failure`, blocked coverage, and a dependent publish barrier. Pre-envelope intake must have owner, ACL, retention, approver, and deletion behavior or must not exist. Add tests. |
| B7 | ACCEPT | [Review B7](00-final-review.md); [P2 intake](../../wayfinder/production-evidence-authority-intake.md) | Require per-source credentials physically incapable of writes, a constrained broker, egress limits, and a real-credential denial receipt. Actual source credentials remain P2-gated. |
| B8 | ACCEPT | [Review B8](00-final-review.md); [P2 intake](../../wayfinder/production-evidence-authority-intake.md) | Add required identity-model, synthetic-principal, aggregate-only comparison, render-time entitlement, approver, and expiry fields. Concrete values remain P2/security decisions. |
| B9 | ACCEPT | [Review B9](00-final-review.md); [retention contract](../../final-architecture-spec.md) | Preserve append-only history while defining a conditional separately keyed, tombstoned, erasure-proof design. Retention periods, deletion authority, and backup handling remain P2/privacy gates. |
| B10 | ACCEPT | [Review B10](00-final-review.md); [G1 contract](../../final-architecture-spec.md) | Add a versioned SegmentationContract with preregistration, weighting, detectability, and multiplicity fields. Numeric values and the selected correction method remain owner/pilot-gated. |
| B11 | ACCEPT (scoped) | [Review B11](00-final-review.md); [evaluation contract](../../eval-acceptance-plan.md) | Preregister applicable always-abstain and most-recent-deploy baselines; reject an indistinguishable suite before Agent scoring; add adversarial decoys and sealed fixture-author/evaluator independence or conflict. No numeric threshold is invented. |
| B12 | ACCEPT | [Review B12](00-final-review.md); [sequencing U9](../../implementation-sequencing.md) | Make UI-001 a synthetic, technology-neutral pre-P3 proof. Final interaction acceptance and framework choice remain P3-gated. |
| B13 | ACCEPT | [Review B13](00-final-review.md); [deliverable index](../../deliverable-index.md); [source manifest](../../source-manifest.md) | Index the enterprise profile as supporting/non-authoritative, the verified DeepSeek increment as supporting research, and this review bundle/disposition as review history. Replace stale prototype self-scores with the current owner panel result. |
| B14 | ACCEPT | [Review B14](00-final-review.md); [sequencing U11](../../implementation-sequencing.md) | Add P2-approved per-case/per-window ceilings, a named halt role, tested disable path, and fail-closed Coverage Gap behavior. Values remain P2/P4-gated. |
| M1 | PARTIAL | [Review M1](00-final-review.md); [closed policy contract](../../wayfinder/freeze-canonical-domain-policy-contracts.md) | Never mutate a confirmed VerdictEvent. Within an active generation append superseding Claim/VerdictEvent revisions; for a closed generation or sealed packet reopen as a new linked generation. Preserve history. |
| M2 | ACCEPT | [Review M2](00-final-review.md); [typed relationship contract](../../final-architecture-spec.md) | Restrict HumanRuling support citations to admitted Evidence, DerivedFact, or GateReceipt revisions; enumerate legal typed edges; Trace cannot support a ruling. |
| M3 | ACCEPT | [Review M3](00-final-review.md); [candidate diff contract](../../final-architecture-spec.md) | Keep the `not_applied` diff syntactically valid and independently reviewable. Deliver only through authorized human review surfaces; prohibit automation-consumable apply/commit/PR/deploy/rollback/webhook/queue/polling interfaces. |
| M4 | ACCEPT | [Review M4](00-final-review.md); [G3/G4 contracts](../../final-architecture-spec.md) | Require G4 support to use a disjoint SourceRead set or a predeclared counterfactual challenge. Shared model narration or votes do not establish independence. |
| M5 | ACCEPT | [Review M5](00-final-review.md); [G6 contract](../../final-architecture-spec.md) | Missing G6 authority, coverage, or budget is inconclusive, never N/A. Reserve N/A for proven non-applicability with a named rationale. |
| M6 | ACCEPT | [Review M6](00-final-review.md); [invalid-experiment branch](../../final-architecture-spec.md) | Define assignment, exposure, join, metric-definition, and unit/variance gaps as material; unknown classification defaults to material and fails closed. |
| M7 | ACCEPT with owner gate | [Review M7](00-final-review.md); [enterprise profile](../../enterprise-experiment-post-analysis-profile.md) | Add optional outcome-class fields and `directional_only` behavior as proposals only. Do not expand owner-confirmed Scenario A outcome scope without an owner decision. |
| M8 | ACCEPT with scope deferral | [Review M8](00-final-review.md); [architecture scope](../../final-architecture-spec.md) | Keep Win/Loss Evidence in direction-only M2/follow-on work. It is not part of the funded M0 slice. |
| M9 | ACCEPT | [Review M9](00-final-review.md); [G1 arm parity](../../final-architecture-spec.md) | Require treatment/control parity for index generation, serving alias, ACL snapshot, and effective pipeline. Divergence caps cause and blocks comparability. |
| M10 | ACCEPT | [Review M10](00-final-review.md); [ExperimentReadContract](../../final-architecture-spec.md) | Add compositional SRM and zero-result delta checks to G1 and evaluation scenarios. Thresholds remain pilot-open. |
| M11 | ACCEPT | [Review M11](00-final-review.md); [G3/G4 contracts](../../final-architecture-spec.md) | Require a named position-bias/propensity correction or authorized interleaving before click-derived mechanism support. |
| M12 | ACCEPT | [Review M12](00-final-review.md); [E15 proposal](../../final-architecture-spec.md) | Add proposed E15 judgment/offline-evaluation Evidence with rubric, query-set, judge class, date, and coverage. Authority remains P2/P4-gated. |
| M13 | ACCEPT with schema gate | [Review M13](00-final-review.md); [typed change contract](../../final-architecture-spec.md) | Add proposed `index | connector | permission | presentation | telemetry` subtypes and exact identities. Domain-owner and Engineering acceptance remain open. |
| M14 | ACCEPT | [Review M14](00-final-review.md); [ranking contract](../../final-architecture-spec.md) | Define a reviewer-recomputable `uncalibrated_fixture` lexicographic comparator. Apply gate ceilings before ordering; do not present it as production priority. |
| M15 | ACCEPT | [Review M15](00-final-review.md); [evaluation vetoes](../../eval-acceptance-plan.md) | Annotate each veto detector as `deterministic | human | not_yet_implemented`, with owner and Coverage Gap. Missing detector coverage blocks acceptance. |
| M16 | ACCEPT | [Review M16](00-final-review.md); [blind-case contract](../../eval-acceptance-plan.md) | Add exact-string, n-gram, symbol, filename, prompt, index, and cache leakage checks; seal prompt/config digest; exclude widely published incidents from clean MVP blind gold. |
| M17 | ACCEPT, P3-owned | [Review M17](00-final-review.md); [P3 ticket](../../wayfinder/prototype-observability-first-review-surface.md) | Record wrong-record and inert-control defects as P3 blockers. Prototype implementation changes remain owned by the separate prototype task and are not in this patch. |
| M18 | PARTIAL | [Review M18](00-final-review.md); [digest contract](../../final-architecture-spec.md) | Permit ordinary hashes for public software and approved releasable artifacts. Prohibit bare hashes of confidential, secret, or low-entropy values; use opaque receipts or scoped keyed commitments when explicitly required. Digest proves byte identity only. |
| M19 | PARTIAL | [Review M19](00-final-review.md); [collector boundary](../../final-architecture-spec.md) | Limit collectors to Data Agent-owned enterprise-managed runtimes for authorized Case Generations. Prohibit personal endpoints, unrelated-session collection, and employee monitoring. Any future endpoint collection needs new authority and jurisdiction/processing-dependent privacy or labor review. |
| M20 | PARTIAL | [Review M20](00-final-review.md); [Trace contract](../../final-architecture-spec.md) | Require a minimal Data Agent-owned RunAttempt lifecycle/resource receipt. Cross-host Trace is optional. A required pin/capture gap blocks only its dependent operational assertion or diagnostic view; optional absence is a visible Coverage Gap, not negative Evidence or a global packet block. |
| M21 | ACCEPT | [Review M21](00-final-review.md); [revision and packet contract](../../final-architecture-spec.md) | Add predecessor-digest chaining and packet-manifest `(revision_id, content_digest)` pairs, with substitution/omission tests. |
| M22 | ACCEPT | [Review M22](00-final-review.md); [sequencing U2](../../implementation-sequencing.md) | Replace the universal negative test with a positive capability allowlist, typed denied-write receipts, and import-graph reachability checks. |
| M23 | ACCEPT with P2 boundary | [Review M23](00-final-review.md); [sequencing U6/U11](../../implementation-sequencing.md) | Keep pre-P2 U6 to fixture-backed interfaces and explicit unknown production behavior. Production matcher validation starts only after P2 through U11. |
| M24 | ACCEPT with Engineering gate | [Review M24](00-final-review.md); [ExperimentReadContract](../../final-architecture-spec.md) | Add assignment unit, analysis unit, ratio-metric variance estimator, and mismatch failure. Exact estimator choice remains an Engineering/domain decision and numeric values remain pilot-open. |

Count check: 14 blocker rows plus 24 major rows equals 38 unique findings. B2 is owner-confirmed; no B/M finding remains deferred for a product-scope decision. P2/P3/P4 and the named Engineering/domain decisions remain open.

## Minor-Finding Ledger

Approved minor findings are corrected where the evidence supports a mechanical contract or index repair. Items that require new authority remain deferred:

- Apply terminology, enum, typed-edge, receipt, stale-sequencing, source-index, and review-count corrections where supported.
- Keep M1/M2 implementation funding, concrete identity/retention values, production-source facts, UI acceptance, and numeric thresholds behind their owner/P2/P3/P4 gates. M0 is the only approved first build/funding slice.
- Keep the repeated-run count pilot-open; no default of five is accepted.
- Treat collector expansion and direct component reuse as deferred until their authority and license receipts exist.
- Replace stale prototype self-scores with the current owner panel result: `2.1`, `convergence.passed=false`. Prior agent scores are superseded history, not acceptance.

## Receipt Corrections

- The main orchestration task independently verified that all eight screenshot SHA-256 values match the enterprise profile. The raw images and rehash command path are no longer available in this workspace, so this disposition preserves the verification result without inventing a current path or command.
- The final DeepSeek report source was verified with `shasum -a 256` and SHA-256 `81feaa5e1c2514732707fa542a283162faafa435611f768e6887c8421bb64f52`. The reconciliation patch records the source receipt and any post-reconciliation staged hash separately.
- The review bundle comprises **8 review agents plus 1 image-extraction agent**.

## Remaining Gates

- Separate explicit authorization to start the owner-confirmed M0 implementation slice. The scope ruling alone is not execution authority.
- P2 production source, mapping, identity/ACL, credential, redaction, retention/erasure, E15, load-ceiling, and halt-authority decisions.
- P3 live owner/reviewer interaction acceptance and resolution of prototype blockers.
- P4 blind-case authority, baseline applicability, case inventory, detector coverage, repeated-run design, thresholds, ranking policy, and rung exits.
- Engineering/domain decisions for language, storage, framework, vendor, subtype schema, variance estimator, and any direct reuse after provenance/security/license review.
