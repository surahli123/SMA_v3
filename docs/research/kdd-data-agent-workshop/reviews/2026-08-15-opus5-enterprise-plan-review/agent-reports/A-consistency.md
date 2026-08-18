# Mechanical Consistency Audit — KDD Data Agent Workshop Package

## 1. Identifier Consistency

**M0/M1/M2 milestones**
- DEFINED only in `enterprise-experiment-post-analysis-profile.md:12-17` (M0 Flight Readiness, M1 Metric Movement and Production Grounding, M2 Win/Loss Evidence, M3+ Self-serve Productization). The same doc explicitly disclaims canonical status: "M0/M1/M2 are proposed product milestones rather than frozen canonical terms" (`enterprise-experiment-post-analysis-profile.md:17`), and status line marks it "research synthesis draft... pending" (`enterprise-experiment-post-analysis-profile.md:4`).
- NOT FOUND after searching `planning-decision-packet.md`, `final-architecture-spec.md`, `implementation-sequencing.md`, `wayfinder/freeze-canonical-domain-policy-contracts.md`, `eval-acceptance-plan.md`, `wayfinder/map.md`, `completion-matrix.md`, `deliverable-readiness-matrix.md`, `deliverable-index.md`, `objective-completion-audit.md`, `cross-research-consistency-audit.md` — none of these define or reference M0/M1/M2 as product terms.
- **COLLISION**: `implementation-sequencing.md:105-106` uses bare `M1` as a mermaid node label meaning "Scenario A MVP decision" — a different referent from profile.md's `M1` ("Metric Movement and Production Grounding"). No namespace disambiguates them, and both sit in cross-referencing docs (`wayfinder/map.md:23` cites `implementation-sequencing.md`; `enterprise-experiment-post-analysis-profile.md:486` cites P1). Same bare token, two meanings.
- Profile.md's own reconciliation list (`enterprise-experiment-post-analysis-profile.md:470-480`) confirms this collision has not been resolved and that reconciliation is future work.

**Canonical eight stages** — DEFINED identically in `wayfinder/freeze-canonical-domain-policy-contracts.md:108-117` (1. `intake_and_freeze` … 8. `review_packet_and_handoff`) and `final-architecture-spec.md` §10.1 table (`final-architecture-spec.md:380-389`), same 8 names, same order. USED nowhere by name in `enterprise-experiment-post-analysis-profile.md` — grep for all 8 stage tokens against that file returns zero matches. Profile.md's M0/M1/M2 milestone scheme runs in parallel to, but never maps onto, the 8 canonical stages by name — a traceability gap (also relevant to item 4).

**Gates G0-G7** — consistent everywhere checked: `wayfinder/freeze-canonical-domain-policy-contracts.md` §"Gate 0–7 executable contract", `final-architecture-spec.md` §9, `implementation-sequencing.md` "Runtime Gate 0–7" table, `eval-acceptance-plan.md` §5 all restate identical pass/fail/ceiling language verbatim. No drift found.

**Eight state dimensions** — the task's own list names 7 (Case/Evidence/Claim/Cause Verdict/Recommendation Readiness/Approval/Incident); `Stage` is the 8th and is omitted from the task framing, not from the docs. Canonical enumeration is `wayfinder/freeze-canonical-domain-policy-contracts.md:39` and §"Independent state contracts" items 1–8 (Case lifecycle, Stage execution, Evidence usability, Claim evaluation, Cause Verdict, Recommendation Readiness, Action approval, Incident health). The count "eight" and the same 8-item enumeration recur consistently at `final-architecture-spec.md:830`, `completion-matrix.md:31`, `deliverable-readiness-matrix.md:29`, `objective-completion-audit.md:40`, `wayfinder/map.md:20`. No count mismatch found in any doc.

**P2/P3/P4** — DEFINED in `implementation-sequencing.md:51-56` (P1 closed; P2 production authority, P3 observability surface, P4 evaluation/calibration, all open-and-claimed). USED with identical scope in `final-architecture-spec.md` §17, `eval-acceptance-plan.md`, `deliverable-index.md`, `README.md:28-32`, `enterprise-experiment-post-analysis-profile.md:479,486,490`. No renaming or scope drift found.

**D0 + U1–U13** — fully DEFINED only in `implementation-sequencing.md`. Referenced (not redefined) at `wayfinder/map.md:23` and `enterprise-experiment-post-analysis-profile.md:488-489`, which correctly use U8's and U11's canonical meanings (U8 = Scenario A fixture workflow/packet; U11 = one authorized production path). No drift found.

## 3. Gate/Unit-to-Test Traceability (D0, U1–U13)

| Unit | Entry? | Exit? | Test IDs named? | Prod access? | Anchor |
|---|---|---|---|---|---|
| D0 | yes | yes | no (only "one hermetic test") | No | `implementation-sequencing.md:171-179` |
| U1 | yes | yes | POL-001…009 | No | `:181-201` |
| U2 | yes | yes | SKEL-001…004 | No (excluded) | `:203-218` |
| U3 | yes | yes | EVD-001…005 | No | `:220-236` |
| U4 | yes | yes | REV-001…005 | No | `:238-254` |
| U5 | yes | yes | ADP-001…005 | No (production adapters absent) | `:256-272` |
| U6 | yes | yes | ANA-001…006 | No | `:274-291` |
| U7 | yes | yes | ORC-001…006 | No | `:293-310` |
| U8 | yes | yes | A-001…008 | No (blocked by P2) | `:312-331` |
| U9 | yes | yes | UI-001…006 | N/A (synthetic only) | `:333-350` |
| U10 | yes | yes | EVAL-001…008 | No | `:352-371` |
| U11 | yes (mandatory gate: P2 closed) | yes | PROD-001…006 | **Yes** — this is the production path | `:373-390` |
| U12 | yes (P3 closed) | yes | **MISSING** — no "Required tests" block | No | `:392-398` |
| U13 | yes (multi-part, complex) | yes | **MISSING** — no formal test-ID block, only narrative | Conditional (P2 required for production-like replay rung only) | `:400-406` |

**Finding**: every unit D0/U1–U11 follows a uniform `XXX-00N` required-test convention; U12 and U13 break that pattern and specify no test IDs, only prose acceptance criteria. This is a structural inconsistency in the sequencing doc's own format, not merely a gap in content.

## 4. Requirement Coverage — `enterprise-experiment-post-analysis-profile.md` as source

This document is explicitly **not yet reconciled** into the canonical package (`enterprise-experiment-post-analysis-profile.md:482`: "Until reconciliation is complete, this document... does not supersede the canonical specification"; §14 lists 9 pending reconciliation changes, none yet applied). Consequently, essentially all of its proposed requirements have no downstream anchor in the canonical docs today:

- **M0/M1/M2 milestone gates** (`:65-78`) — no mapping to Gate 0–7 or the 8 canonical stages anywhere in `final-architecture-spec.md` or `wayfinder/freeze-canonical-domain-policy-contracts.md`. NOT FOUND.
- **`ExperimentReadContract`** (`:84-99`) — absent from the Required-entities table in `final-architecture-spec.md:209-230` (which lists `MetricQuestion`, `Case`, `CaseGeneration`, `RunAttempt`, `SourceRead`, `CoverageGap`, `EvidenceRevision`, `DerivedFactRevision`, `MappingRevision`, `ProductionChangeRevision`, `CandidateGroupRevision`, `ClaimRevision`, `GateReceipt`, `VerdictEvent`, `RecommendationRevision`, `RankingRevision`, `HumanRuling`, `PacketRevision`, `Acknowledgement`, `InvalidationEvent` — no experiment-read contract entity). NOT FOUND.
- **`FlightReadinessPacket` / `MetricMovementPacket` / `WinLossEvidencePacket`** (`:67-72`) — profile.md itself flags these as proposed, not integrated ("should be typed payloads or projections of the existing immutable `ReviewPacketRevision`... The physical choice... remains an engineering decision," `:76`). No implementation unit in `implementation-sequencing.md` names them.
- **25 acceptance cases in profile.md §12** (`:383-407`, e.g. CUPED/unadjusted mismatch, preregistered runtime incomplete, decision metric absent from registry, source migration with changed meaning) — compared against `eval-acceptance-plan.md` §19.1's 10 required case classes (`eval-acceptance-plan.md:716-725`): no name or scope overlap. NOT FOUND in `eval-acceptance-plan.md` after searching §3.1 and §19.1.
- **Host/Execution Adapter conformance contract** (`enterprise-experiment-post-analysis-profile.md` §10 item 1, §9) — no corresponding unit among D0/U1–U13.

This is by the document's own design an exhaustive, acknowledged gap — see its own §13 "Owner decisions required before canonical reconciliation" (15 items, `:448-464`) and §15 "Completion Claim Boundaries" (`:484-491`), which state the canonical docs remain unchanged and unreconciled pending owner decisions.

## 5. Internal Contradictions

- No enum drift found. Cause Verdict (`unassessed|suspected|confirmed|ruled_out|inconclusive`) and Recommendation Readiness (`not_applicable|blocked|proposal_ready|action_ready|rejected`) are byte-identical across `planning-decision-packet.md:45,47`, `wayfinder/freeze-canonical-domain-policy-contracts.md:161,182`, `final-architecture-spec.md:258-259`, `eval-acceptance-plan.md:110-111`, `README.md:46-47`.
- No contradiction found on "may the Agent emit a diff": `planning-decision-packet.md:15` ("Scenario A may produce an unapplied candidate diff") and `final-architecture-spec.md:34` ("the Agent may generate a candidate diff marked `not_applied`") agree.
- The `M1` label collision (item 1 above) is the one genuine identifier-level conflict found between `implementation-sequencing.md:105-106` and `enterprise-experiment-post-analysis-profile.md:13`.
- Staleness, not contradiction: `completion-matrix.md` (file mtime 2026-08-12 03:13) predates `enterprise-experiment-post-analysis-profile.md` (2026-08-14 22:50) by two days and could not and does not reference it; `completion-matrix.md:57`'s "Research and canonical specification artifacts: complete" claim is unmodified by the newer profile draft's "REVISE" status (`enterprise-experiment-post-analysis-profile.md:4`). Not a logical contradiction (different documents, different scope) but a currency gap a reader could miss without checking dates.

## 6. Link Integrity

Checked every relative markdown link in `README.md`, `deliverable-index.md`, and `wayfinder/map.md` by resolving each target against the filesystem: **all resolve; no broken links found.**

## 7. Status-Claim Hygiene (spot check, not exhaustive given word budget)

`completion-matrix.md:37` labels "Build and mechanically validate the observability prototype" as `complete`, with evidence consisting of self-reported critique scores ("3.6/5, 4.1/5, 4.5/5") and browser/static checks against a fixture prototype — i.e., document- and static-artifact-only evidence. The row itself caveats "does not prove reviewer utility or close P3," so it is self-aware, but the bare `complete` label without that caveat visible in the status cell is worth flagging per the strict criterion given. `completion-matrix.md:8,13` do define `complete` narrowly as "deliverable exists," which mitigates most other `complete` rows in that matrix — they are internally consistent with their own defined term. Did not exhaustively scan `objective-completion-audit.md`, `deliverable-readiness-matrix.md`, or `cross-research-consistency-audit.md` line-by-line for this item given the word cap; flagging as **NOT FULLY AUDITED** rather than claiming a clean result.
