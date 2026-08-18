# Codex Disposition of the Opus 5 Freeze-Review Handoff

Date: 2026-08-17  
Source handoff: [`m0-freeze-codex-fix-handoff.md`](m0-freeze-codex-fix-handoff.md)  
Reviewed source packet SHA-256: `40c7234f3c0d85f18ebfba656e7aec2ab5ab71b86451a077ecad340eac779396`  
Post-edit packet SHA-256: `67c844d10dcafcf2637388bf579dfcd9866d7d69ea6f4d3b456fd6b6b15dfcfa`  
Disposition state: `POST_REVIEW_CANDIDATE_NOT_FROZEN`

## Decision rule

Reviewer findings were treated as falsifiable claims, not instructions to apply
silently. A finding was applied only when its evidence matched the current bytes and
the proposed correction preserved Owner decisions and fail-closed behavior.

## Eight requested edits

| # | Finding | Disposition | Reason and applied meaning |
| --- | --- | --- | --- |
| 1 | §5.3 readiness fields (`MAJOR-1`) | **APPLIED** | `analysis_use` and `post_analysis_eligibility` were incorrectly described as orthogonal despite a closed three-row legality matrix. The packet now calls them coordinated stored fields and rejects every non-legal pair rather than interpreting or repairing it. Neither field has precedence. The wording was propagated to the controlling spec and implementation/planning surfaces. The review's derived-projection option was not selected because it would change the already propagated packet serialization contract; the review's explicitly permitted reject-invalid-pair option closes the ambiguity with less migration risk. |
| 2 | §5.2 check outcome versus materiality (`MAJOR-3`) | **APPLIED** | The original pronoun made `UNKNOWN` ambiguous across two enums. The packet now has separate labelled check-outcome and materiality rules. Unknown or unclassified materiality remains stored as `unknown`, while the applied decision ceiling treats it as material until a versioned ruling supersedes it. |
| 3 | §5.4 runtime completion and recomputation (`MAJOR-4`) | **APPLIED** | A sealed pre-runtime packet otherwise remained syntactically current after its triggering time. The reopen condition must now name the preregistered runtime end, packet expiry may not exceed it, and reaching it requires a new read and superseding packet. |
| 4 | `VAL-REM-002` validity scope (`MINOR-2`) | **APPLIED** | The acceptance row now says `validity/instrumentation/data-quality`, matching O3, §5.4, and the CE plan without broadening into product-logic remediation. |
| 5 | §13 controlling-spec binding (`MINOR-4`) | **APPLIED** | §13 now requires the freeze record to bind the exact revision label and SHA-256 of `final-architecture-spec.md` independently from the packet digest. The current post-edit spec candidate SHA-256 is `3b20c93859b78074b653d375fc29f60bd40993b3f3bcb4ee2ff481e8ba8706b8`. This is a candidate binding only; it is not a freeze declaration. |
| 6 | Triage key (`MINOR-3`) | **APPLIED** | The packet now states that triage uses `analysis_use` with `next_safe_action.kind`, never `post_analysis_eligibility` alone. This preserves the operational difference between waiting for sufficiency and performing corrective work. |
| 7 | CE plan `VAL-M0-002` mapping (`MAJOR-2`) | **APPLIED** | The undischarged `blocks or makes directional` disjunction was real. The CE plan now maps runtime or preregistered-power/MDE insufficiency with no other material blocker exactly to `blocked + directional_only`, and material validity/source/ACL/isolation/evidence failure exactly to `blocked + not_permitted`. |
| 8 | CE plan `VAL-UNIT-001` outcome (`MINOR-1`) | **APPLIED** | The CE plan now restores the required `blocked + not_permitted` result for a material assignment/analysis-unit or ratio-variance failure. |

## Additional corrections required by the cited full review

The handoff says there are zero blockers, but the cited full review and machine status
bind three blockers to the exact source packet digest, and all three failure shapes
were still present in the source bytes. They could not be silently ignored.

| Review finding | Evidence in source bytes | Disposition |
| --- | --- | --- |
| Spent authorization presented as live | Source packet lines 7 and 19 and `owner-alignment-record.md` line 75 treated the exhausted continuation handoff as future authority | **APPLIED.** All three now require a new Owner authorization and bounded start receipt. |
| `directional_only` had no reachable non-runtime sufficiency rule | Source contract had no power/MDE field or check while the controlling spec admitted valid-but-underpowered directional use | **APPLIED.** The contract, check inventory, plan, sequencing, spec, and evaluation surface now include preregistered power/MDE sufficiency. |
| M0 omitted arm-parity and legal-combination contract fields | The controlling spec required both while the packet omitted them | **APPLIED.** The packet now includes the legal-combination policy and treatment/control arm-parity identities; check 5, sequencing, plan, and evaluation now consume them. |

These corrections increase the M0 check inventory from 18 to 19 because arm parity is
integrated into check 5 and power/MDE sufficiency is check 19.

## Evidence conflict that prevents a freeze claim

The newest handoff and its cited evidence disagree materially:

- the handoff says `zero blockers`, while the full report and status JSON list three;
- the handoff says all eight adjudications are implemented, while the current corpus
  still lacks the complete B3 asset inventory and still carries unresolved M18, M19,
  and M20 required actions;
- the full 30-finding reconciliation remains only transitive/partial;
- the Opus reviewer performed Q11/Q12 probes but later declined those conclusions for
  conflict of interest because that session authored the original Phase A package and
  receipt;
- Codex is also not independent for Q11/Q12 because it authored the Phase A
  continuation.

Therefore this disposition does **not** copy the prior Opus verdict onto the new packet
digest. The prior `accept_with_changes` row remains evidence about
`40c7234f3c0d85f18ebfba656e7aec2ab5ab71b86451a077ecad340eac779396` only. A reviewer
must inspect the post-edit bytes before recording a verdict against
`67c844d10dcafcf2637388bf579dfcd9866d7d69ea6f4d3b456fd6b6b15dfcfa`.

## Current artifact bindings

| Artifact | SHA-256 |
| --- | --- |
| `m0-m2-build-alignment-packet.md` | `67c844d10dcafcf2637388bf579dfcd9866d7d69ea6f4d3b456fd6b6b15dfcfa` |
| `final-architecture-spec.md` | `3b20c93859b78074b653d375fc29f60bd40993b3f3bcb4ee2ff481e8ba8706b8` |
| `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md` | `52ce2763a365eb35ea884dfbc7f19b8b3d012b85edac544a21b356638126499c` |
| `implementation-sequencing.md` | `1d42e67c0ba5e2a1799960a3e151b12fa847a419f13b7a9f63362366dc3a29ee` |
| `eval-acceptance-plan.md` | `5dce10ca451f7ccbbf5d86896cefed2b8dd8a5b5cae480da4d3ea030d5603194` |
| `planning-decision-packet.md` | `7e68ad675b988f2dfc3f53cf13e6e5e4bbd24194ce896c38df395e62b06bd37c` |
| `owner-alignment-record.md` | `c868699a60ee9a7fc72ebcc8f9345a8cb65399002812fec64d1053be2084ae6e` |

## Gate state

- Packet semantics: post-review candidate, pending fresh exact-digest review.
- Phase A: not independently cleared; routed to a third session.
- Full 30-finding reconciliation: `PARTIAL`, not cleared.
- B3/M18/M19/M20 required actions: not represented as cleared.
- M0-F1 through M0-F5: not authorized and not started.
- Production access, M1/M2 implementation, P2/P3/P4, and Committee Acceptance: not
  authorized or closed.

No freeze record is valid until the independent Phase A reviewer returns, the post-edit
packet bytes receive an exact-digest verdict, and the Owner acknowledges the final
packet/spec binding.
