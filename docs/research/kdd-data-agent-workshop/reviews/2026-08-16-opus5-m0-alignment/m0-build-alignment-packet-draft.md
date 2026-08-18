# M0 Build Alignment Packet — Superseded Historical Draft

Status: superseded by [`m0-m2-build-alignment-packet.md`](m0-m2-build-alignment-packet.md); retained for review provenance  
Date: 2026-08-16  
Scope: M0 Flight Readiness only

> This draft predates the completed Owner grill. Its M0-only funding boundary, open Owner questions, role language, metric cardinality, invalid-experiment diff prohibition, and legacy-authority assumptions are no longer current. Do not use it as an implementation or planning contract.

## 1. Purpose

This packet is the proposed three-party build contract for the first Data Agent slice. It exists to prevent the implementation from drifting away from the Owner's real experiment post-analysis workflow or from importing direction-only M1/M2 architecture into M0.

The three required reviewers are:

1. **Owner:** controls product meaning, usefulness, human workflow, and whether the packet matches the real job.
2. **Claude Code Opus 5:** acts as an independent adversarial reviewer of requirement coverage, ambiguity, overreach, and implementability.
3. **Codex:** maintains the evidence ledger, reconciles review findings against current repository authority, and implements only after a separate start authorization.

No reviewer may convert this packet into implementation authority. The Owner must issue a separate explicit build-start decision after this packet is accepted and frozen.

## 2. Owner-Confirmed Scope

The only first build/funding slice and main deliverable is **M0 Flight Readiness**.

M0 answers one question:

> Can the experiment setup and primary metric read be trusted enough to start post-analysis?

M0 accepts a versioned `ExperimentReadContract`, performs authorized and independently receipted checks, and seals an immutable `FlightReadinessPacket`.

M1 Metric Movement and Production Grounding, M2 Win/Loss Evidence, full Scenario A causal analysis, and Scenario B SEV analysis remain direction-only. They receive no implementation funding in M0.

## 3. User Job and Decision

The real user needs to avoid spending investigation time on an experiment whose identity, exposure, metric definition, analysis unit, estimator, data read, or runtime state is invalid, incomplete, stale, contradictory, unauthorized, or materially unknown.

M0 must let the reviewer decide one of two safe outcomes:

- **Ready for post-analysis:** all material prerequisites are supported by admitted Evidence and receipts.
- **Blocked:** at least one material prerequisite failed, is missing, is contradictory, is unauthorized, or remains unknown.

M0 does not decide why the metric moved or what production code should change.

## 4. Required Input: `ExperimentReadContract`

The frozen input must include, or explicitly mark unknown, at least:

- experiment identity and contract version;
- hypothesis and decision purpose;
- treatment and control identities;
- primary metric name, definition version, decision role, and owner;
- population, eligibility, tenant/surface/locale scope, and exclusion rules;
- assignment unit, analysis unit, exposure definition, and join keys;
- estimator and any required ratio-metric variance method;
- analysis window, timezone, ramp, planned runtime, and actual runtime;
- source identity, snapshot/version, freshness rule, and authoritative owner;
- expected assignment/exposure and SRM/compositional-SRM plan;
- authorization, tenant/ACL, redaction, retention, and allowed recipient scope;
- named Experiment Owner, reviewer, and approver;
- contract digest, expiry, predecessor, and supersession link.

Missing required authority or identity must remain `UNKNOWN` or `MISSING`; the Agent must not infer it.

## 5. Required M0 Checks

Every check returns `PASS | FAIL | MISSING | UNKNOWN | NOT_APPLICABLE`, materiality, rule source, Evidence/receipt IDs, reason, and reopen condition.

The minimum check set is:

1. experiment identity and contract version;
2. preregistered runtime versus observed runtime;
3. primary metric registration and definition version;
4. assignment-unit and analysis-unit consistency;
5. treatment/control assignment and exposure integrity;
6. SRM and applicable compositional SRM;
7. population, eligibility, exclusions, and scope consistency;
8. join-key and denominator integrity;
9. completeness, freshness, and partial-read handling;
10. estimator and variance-method consistency;
11. source and lineage identity;
12. reported primary read versus independent recomputation;
13. authorization, tenant/ACL, recipient, and redaction status;
14. disagreement, contradiction, and Coverage Gap closure state.

Unclassified validity gaps default to material until a named owner supplies a versioned rule.

## 6. Required Output: `FlightReadinessPacket`

The immutable packet must contain:

- frozen `ExperimentReadContract` revision and digest;
- source-read and derivation receipts;
- every required check and outcome;
- material failures, disagreements, and Coverage Gaps;
- readiness decision and blocking reasons;
- next safe action and reopen condition;
- named reviewer/approver state;
- authorization/redaction manifest;
- packet manifest, digest, expiry, predecessor, and supersession link.

The packet must contain **no** Cause Claim, causal verdict, production candidate, ranking, Recommendation, candidate diff, Win/Loss label, or Trace-only fact.

## 7. Proposed First-Screen Contract

The M0 first screen is packet-, check-, and receipt-centered. It is not an Evidence Graph or a generic dashboard.

The first screen must show, in this order:

1. **Readiness decision:** ready or blocked, packet revision, freshness, and named human state.
2. **Blocking checks:** all material failed, missing, unknown, contradictory, or unauthorized prerequisites.
3. **Primary read comparison:** reported value versus independently recomputed value, with units, estimator, window, and receipt links.
4. **Coverage Gaps and disagreements:** what is unavailable, conflicting, partial, stale, or outside authority.
5. **Next safe action:** the exact evidence, owner, or contract correction needed to reopen.
6. **Receipt access:** source, derivation, authorization, redaction, and packet-manifest receipts.

Every visible conclusion must resolve to a receipt. The screen must not imply a production cause, show a candidate ranking, or reuse the direction-only M1 Evidence Room as the M0 conclusion surface.

## 8. First Vertical Spike After Alignment

After a separate implementation-start decision, the first executable artifact must be one hermetic, fixture-backed end-to-end path:

```text
ExperimentReadContract
  -> authorized fixture read
  -> independent primary-metric recomputation
  -> deterministic readiness checks
  -> immutable FlightReadinessPacket
  -> packet-centered M0 review screen
```

The team must stop after this path and obtain Owner plus Opus 5 review before expanding the check set, adapters, fixtures, or UI. Passing a unit test without matching the accepted packet and screen is not acceptance.

## 9. Acceptance Scenarios

| ID | Scenario | Required result |
| --- | --- | --- |
| `M0-CON-001` | Complete, internally consistent frozen contract | Contract accepted with stable digest; no inferred fields |
| `M0-READ-001` | Authorized complete fixture read and independent recomputation | Source and derivation receipts resolve; comparison is visible |
| `M0-VAL-001` | Material identity, assignment, exposure, metric, unit, estimator, or join failure | Packet is blocked; no post-analysis or cause output |
| `M0-DET-001` | Identical frozen inputs repeated | Identical check results and packet digest |
| `M0-PKT-001` | Attempt to insert Cause Claim, candidate, ranking, Recommendation, diff, Win/Loss, or Trace-only fact | Schema/policy rejection |
| `M0-SEC-001` | Unauthorized, ACL-conflicting, or redaction-failed read | No body retained or rendered; packet is blocked with typed receipt |
| `M0-UI-001` | Named reviewer inspects one trusted and one blocked packet | Reviewer can state decision, blocker, disagreement, receipt, and next safe action without inferring a cause |

Numeric thresholds, final case count, and production-source behavior remain P2/P4 or pilot decisions and must not be invented for this packet.

## 10. Required Three-Party Alignment Record

Before implementation, each reviewer must record:

- `accept | accept_with_changes | reject`;
- exact packet sections reviewed;
- requested changes and rationale;
- unresolved owner decisions;
- conflicts of interpretation;
- reviewed content digest and timestamp.

The packet may be frozen only when:

1. the Owner accepts the user job, M0 boundary, output, first screen, and acceptance scenarios;
2. Opus 5 finds no unresolved requirement ambiguity that would make two competent implementers build materially different products;
3. Codex maps every accepted requirement to a startable implementation unit and test ID;
4. all remaining unknowns are explicitly gated rather than guessed.

## 11. Owner Decisions Still Required

The Owner must still confirm:

1. whether the ready/blocked decision wording matches the real review workflow;
2. which named roles review and approve M0 packets in the actual organization;
3. which real, de-identified experiment examples should become the first fixtures;
4. which disagreements are material by product policy rather than engineering inference;
5. which receipt details must be visible on the first screen versus one click away;
6. whether the proposed first-screen order matches the way reviewers make the decision;
7. whether a blocked packet should recommend only evidence collection, contract correction, or both;
8. what constitutes owner acceptance of the first vertical spike.

Technology, language, storage, and UI framework remain Engineering proposals unless they change the accepted product behavior.

## 12. Change Control

After the packet is frozen, any change to the M0 question, required inputs, check meaning, packet content, forbidden outputs, first-screen hierarchy, or acceptance scenarios requires a new alignment revision and named Owner approval.

Implementation convenience, legacy architecture, framework defaults, or reviewer preference cannot silently change this contract.
