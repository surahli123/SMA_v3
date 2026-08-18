# Handoff: Independent Opus 5 Review of the M0 Freeze Candidate and Phase A

Created: 2026-08-16  
Updated: 2026-08-17 after the Sol continuation completed Phase A  
Repository: `/Users/surahli/Documents/projects/SMA_v2`  
Branch: `codex/kdd-data-agent-practices-research`  
Mode: independent adversarial review; read-only except for the two review outputs named below

## Objective

Determine whether the current M0 alignment packet can be frozen and bound to semantic implementation without recreating the prior plan-to-spike mismatch. Review the actual dirty worktree, not a recap. Verify that Owner O1-O6, the 30 accepted Opus findings, the 8 adjudicated findings, C1-C9, and the current Phase A implementation have one coherent meaning.

## Authority Order

1. `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/owner-alignment-record.md`
2. `docs/research/kdd-data-agent-workshop/planning-decision-packet.md`
3. `docs/research/kdd-data-agent-workshop/wayfinder/freeze-canonical-domain-policy-contracts.md`
4. Current canonical specification and sequencing documents, where they conform to 1-3
5. Source-backed research and fixed-revision audits
6. Reviewer proposals and engineering choices

The packet under review is a freeze candidate, not authority until accepted and digest-bound.

The first Claude background attempt (`ed33fb08`) hit the Claude session quota
before reading this handoff and produced no review output or verdict. Treat it
as a failed start, not as review evidence.

## Read First

- `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/owner-alignment-record.md`
- `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md`
- `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/opus5-review.md`, especially C1-C9 and the prior-session reconstruction
- `docs/research/kdd-data-agent-workshop/reviews/2026-08-15-opus5-enterprise-plan-review/00-final-review.md`
- `docs/research/kdd-data-agent-workshop/reviews/2026-08-15-opus5-enterprise-plan-review/03-codex-disposition.md`
- `docs/research/kdd-data-agent-workshop/planning-decision-packet.md`
- `docs/research/kdd-data-agent-workshop/final-architecture-spec.md`
- `docs/research/kdd-data-agent-workshop/implementation-sequencing.md`
- `docs/research/kdd-data-agent-workshop/eval-acceptance-plan.md`
- `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md`
- `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-codex-continuation-handoff.md`
- `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-codex-continuation-status.json`
- `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-codex-continuation-receipt.md`
- `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-prealignment-foundation-status.json`
- `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-prealignment-foundation-receipt.md`
- `.agents/skills/kdd_data_agent/TOOLCHAIN_RECEIPT.md`
- the complete current `.agents/skills/kdd_data_agent/` implementation and tests

Do not use the old `handoff.md` or `m0-build-alignment-packet-draft.md` as current authority; both are explicitly superseded.

## Required Review Questions

1. Does the current worktree implement the 30 accepted findings according to the original Opus reviewer's intent, without semantic overreach?
2. Are the eight adjudicated dispositions implemented consistently?
   - B2: M0 first and main; M1/M2 remain in the same separately gated validation program.
   - B3: protected old SMA paths are read-only, but validated domain assets may be reused as candidates.
   - B11: M0 fixtures include trivial baselines, adversarial decoys, and independence/conflict receipts.
   - M1: never mutate a verdict; append a superseding revision, and use a new Case generation after closure.
   - M3: candidate diffs remain correct, valid, `not_applied`, human-only, and unavailable to automation consumers.
   - M18: low-entropy confidential values cannot use bare hashes; do not overgeneralize that rule to every full-file or image digest.
   - M19: first-version Trace is limited to Data Agent-owned runtime; no engineer IDE collection.
   - M20: Trace is optional unless a claim depends on it; missing optional Trace is a Coverage Gap.
3. Did C1-C9 reach the candidate and every controlling plan/spec/eval document with one meaning?
4. Is the proposed readiness contract unambiguous and safe?
   - `post_analysis_eligibility = eligible | blocked`
   - `analysis_use = decision_grade | directional_only | not_permitted`
   - legal combinations only: `eligible + decision_grade`, `blocked + directional_only`, `blocked + not_permitted`
   Challenge whether a valid pre-runtime read should be `blocked + directional_only`, and identify any downstream contradiction.
   Also challenge the three-state materiality contract: `material | non_material | unknown`; unknown/unclassified defaults material, `non_material` requires a preregistered versioned rule, `NOT_APPLICABLE` requires a versioned applicability rule, and runtime insufficiency remains material while directional when no other blocker applies.
5. Are all required M0 checks distinct and implementable, including CUPED non-interchangeability, primary-source versus scorecard/UI reconciliation, numerator/denominator/unit/ratio/relative-percent/percentage-point handling, independent recomputation, and source-change revalidation?
6. Is `NextSafeAction` typed tightly enough, and is its separation from `InvalidExperimentRemediation` exact?
7. Do the `VAL-*` IDs form one non-colliding registry with one meaning per ID? Are synthetic `VAL-UI-001` and P3-gated `VAL-UI-101` separated correctly?
8. Are the always-ready/always-blocked baseline rule, adversarial decoys, fixture-author/evaluator independence or conflict receipt, and suite-rejection behavior sufficient and threshold-free?
9. Does the P2/P3/P4 map prevent fixture evidence from being mislabeled as production, live-review, or calibrated evidence?
10. Are the deterministic halt triggers and budget contract measurable, non-invented, and sufficient? Verify that the prior drifting phrase “authorized 2026-08-16 build session” is gone and that the replacement binds only to handoff `m0-codex-continuation-20260817`, one non-recurring task run, its enumerated run/read/tool surface, its expiry, and named halt authority. Reject any wording that silently renews or converts that local cap into the four-to-six-week program budget.
11. Does the current Phase A code remain semantics-independent and replaceable, or has it silently chosen an unfrozen readiness/check/packet/UI meaning?
12. Independently test Phase A claims proportionately. Do not trust its self-authored green receipt. Check deep immutability, sealing, manifest/outcome binding, sentinel collisions, static capability-scanner boundaries, deterministic replay, no-network/no-write behavior, and actual test reachability.
13. Distinguish four proofs in the final verdict: Phase A foundation, local fixture-backed M0 MVP, production authorization, and Experiment Review Committee acceptance.

## Output Contract

Write exactly these English files:

1. `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-freeze-opus5-adversarial-review.md`
2. `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-freeze-opus5-review-status.json`

The Markdown report must include:

- model/session identity and review timestamp;
- files and commands actually inspected;
- verdict: `ACCEPT | ACCEPT_WITH_CHANGES | REJECT`;
- a C1-C9 table with `satisfied | partial | missing | overreach`;
- a 30/8 reconciliation verdict;
- blocker/major findings only, each with exact file/line evidence, consequence, and minimal fix;
- Phase A independent test evidence and untested boundaries;
- the exact packet sections eligible for freeze and every remaining blocker;
- a proposed Codex/Owner/Opus signoff row against the reviewed digest.

The JSON status must contain `status`, `verdict`, `reviewed_packet_path`, `reviewed_packet_sha256`, `blockers`, `major_findings`, `phase_a_verification`, `remaining_gates`, `session_id`, `model`, and `updated_at`.

## Hard Boundaries

- Do not edit canonical planning documents or `.agents/skills/kdd_data_agent/`.
- Do not commit, push, open a PR, install dependencies, access production, send messages, deploy, or mutate old SMA protected paths.
- Do not declare the packet frozen; only Codex writes the final freeze record after applying accepted findings.
- Do not infer Owner decisions from reviewer preference.
- Do not treat a green test suite as production authorization or Committee Acceptance.
- Preserve unrelated dirty-worktree changes.
