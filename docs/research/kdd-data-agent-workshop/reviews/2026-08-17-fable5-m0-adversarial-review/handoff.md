# Fable 5 Independent Adversarial Review Handoff

## Authority and purpose

The Owner authorizes one independent Claude Code Fable 5 review task at `high`
effort. Fable 5 is the lead adversarial reviewer and may organize up to five
subagents or workflow lanes in total.

This is not a ceremonial approval pass. Its purpose is to try to falsify the
current M0 design, implementation assumptions, evaluation approach, and claimed
evidence before the Owner funds M0-F1 through M0-F5.

Fable 5 may read the full repository, the controlling documents, the KDD research
bundle, the Phase A implementation and tests, and the current receipts. It may run
read-only inspection, tests, deterministic replay, isolated mutation tests, and
other non-production verification.

## Hard boundary

This entire Fable task is review-only.

Allowed writes are limited to the three review artifacts named in this handoff,
inside this directory. Fable 5 and every subagent or workflow lane MUST NOT modify:

- product or agent source code;
- `.agents/skills/kdd_data_agent/`;
- tests or fixtures;
- controlling architecture, planning, policy, evaluation, or sequencing documents;
- Git state, branches, commits, remotes, or pull requests;
- production systems, credentials, datasets, or external services.

An Opus subagent used inside this review inherits the same review-only boundary.
The Owner may later authorize a separate Opus implementation task that can write
code within a named ownership boundary; this handoff does not grant that authority.

Do not freeze the packet, authorize implementation, or start M0-F1 through M0-F5.

## Current state to verify, not trust

- Repository: `/Users/surahli/Documents/projects/SMA_v2`
- Branch observed by the orchestrator: `codex/kdd-data-agent-practices-research`
- HEAD observed by the orchestrator:
  `28cbbda6e4d4d7f08134952d38433e52d3ee8768`
- The worktree is heavily dirty and contains user-owned work. Preserve it.
- Freeze candidate:
  `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md`
- Candidate SHA-256 observed before dispatch:
  `40c7234f3c0d85f18ebfba656e7aec2ab5ab71b86451a077ecad340eac779396`
- Phase A package:
  `.agents/skills/kdd_data_agent/`
- Phase A package aggregate SHA-256 claimed in the continuation receipt:
  `2f1001b93b19b2318c4c6419205ed2f7778ac23c02533e78a0c0899f15bf7d1e`
- Phase A result claimed by Codex/Sol: `PASS_WITH_GAPS`, 225 tests passed from
  three working directories, deterministic replay under
  `PYTHONHASHSEED=0/1/12345`, and no M0-F1 through M0-F5 implementation.
- The prior implementation authorization is exhausted. A new Owner authorization
  and handoff are required even if a freeze is later accepted.
- A separate Opus 5 freeze review is active. It has no accepted verdict yet.

Recompute relevant digests and rerun important checks. A receipt is evidence to
challenge, not authority to inherit.

## Independence protocol

The Fable review has two phases.

### Phase I: blind adversarial review

Form an independent view before reading the current Opus freeze verdict. Until the
Phase I artifact is written and its SHA-256 is recorded in the status file, do not
read either of these files if they appear:

- `../2026-08-16-opus5-m0-alignment/m0-freeze-opus5-adversarial-review.md`
- `../2026-08-16-opus5-m0-alignment/m0-freeze-opus5-review-status.json`

Historical review evidence such as `opus5-review.md` may be read because the
candidate explicitly claims to address it. Do not let another reviewer's proposed
verdict replace independent inspection.

Write and seal `fable5-phase1-independent-findings.md` before Phase II.

### Phase II: conflict and coverage arbitration

After Phase I is sealed, read the current Opus freeze outputs if both exist. Compare
the two reviews finding by finding. Identify agreements, conflicts, missing coverage,
and findings that are unsupported by evidence.

If the current Opus outputs do not yet exist, complete Phase I, write status
`awaiting_opus`, and stop. The main orchestrator will resume this same task after the
Opus outputs are available. Do not invent the missing verdict.

## Model and workflow use

Fable 5 is the lead. It may use no more than five total subagents or workflow lanes.
The five-lane cap includes nested delegation; a subagent may not create an uncounted
second tree.

Use stronger judgment where it changes acceptance:

- Prefer Opus 5 for architecture, causal/statistical contract review, security and
  capability-boundary review, critical code review, and enterprise workflow judgment.
- Use Sonnet 5 only for bounded evidence extraction, repository search, deterministic
  test execution, and compact source packets.
- Keep initial specialist conclusions independent. Do not show one specialist's
  conclusion to another before both have returned their first evidence packet.
- Require each lane to return only conclusions, evidence anchors, verification
  results, unknowns, and blockers. Do not request hidden reasoning transcripts.
- Fable 5 must personally inspect the evidence behind every BLOCKER and every final
  architecture conclusion before including it in the final verdict.

Suggested lanes, which Fable may refine without exceeding the cap:

1. Owner-contract and architecture consistency adversary.
2. Phase A implementation, capability isolation, digest, and mutation adversary.
3. Experiment validity, statistics, fixtures, and evaluation adversary.
4. Enterprise reviewer workflow, production authority, ACL/privacy, and usability
   adversary.
5. KDD winner/DeepSeek practice transfer and toolchain decision adversary.

## Required sources

Start with these local sources. Read additional repository files only when they are
needed to verify a claim.

### Authority and alignment

- `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/owner-alignment-record.md`
- `docs/research/kdd-data-agent-workshop/planning-decision-packet.md`
- `docs/research/kdd-data-agent-workshop/wayfinder/freeze-canonical-domain-policy-contracts.md`
- `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md`
- `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-freeze-opus5-review-handoff.md`
- `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/opus5-review.md`

### Architecture, sequencing, and evaluation

- `docs/research/kdd-data-agent-workshop/final-architecture-spec.md`
- `docs/research/kdd-data-agent-workshop/implementation-sequencing.md`
- `docs/research/kdd-data-agent-workshop/eval-acceptance-plan.md`
- `docs/research/kdd-data-agent-workshop/enterprise-experiment-post-analysis-profile.md`
- `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md`

### Research and source authority

- `docs/research/kdd-data-agent-workshop/source-manifest.md`
- `docs/research/kdd-data-agent-workshop/research-synthesis.md`
- `docs/research/kdd-data-agent-workshop/cross-research-consistency-audit.md`
- `docs/research/kdd-data-agent-workshop/champion-repo-reverse-audit.md`
- `docs/research/kdd-data-agent-workshop/fourth-place-repo-reverse-audit.md`
- `docs/research/kdd-data-agent-workshop/creative-team1286-practices.md`
- `docs/research/kdd-data-agent-workshop/creative-team1401-practices.md`
- `docs/research/kdd-data-agent-workshop/deepseek-harness-practices.md`
- `docs/research/kdd-data-agent-workshop/kdd-source-practices.md`

### Phase A implementation evidence

- `.agents/skills/kdd_data_agent/`
- `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-prealignment-foundation-handoff.md`
- `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-prealignment-foundation-receipt.md`
- `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-codex-continuation-receipt.md`
- `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-codex-continuation-status.json`
- `.agents/skills/kdd_data_agent/TOOLCHAIN_RECEIPT.md`

Fixed public source references may be opened read-only only when a transfer claim is
materially disputed. Do not repeat broad KDD research that is already grounded in the
local audits.

## Adversarial questions

At minimum, attack these questions:

1. Does the freeze candidate preserve every Owner decision without silently adding a
   new product decision?
2. Are `ExperimentReadContract`, `FlightReadinessPacket`, readiness states,
   materiality, `NextSafeAction`, acceptance IDs, stop conditions, and budget rules
   complete and mutually consistent across all controlling documents?
3. Can the M0 packet actually support the Owner's real workflow: experiment Owner
   runs the A/B test, DS acts as an independent consultant, and an Experimentation
   Review Committee makes the final review decision?
4. Does every metric and business-table assumption defer to the current production
   schema/catalog/routine rather than trusting old SMA definitions?
5. Do the 30 accepted prior findings and eight specially disputed findings have a
   traceable, evidence-backed disposition? Identify any semantic drift.
6. Does Phase A implement a real, replaceable foundation, or only tests that confirm
   its own assumptions? Try to falsify digest correctness, append-only history,
   fixture authority, deterministic replay, read boundaries, import/capability
   isolation, and failure propagation.
7. Are static AST checks described honestly as static assurance rather than a runtime
   sandbox? Identify capability escapes, TOCTOU gaps, hidden clocks, filesystem
   reads/writes, network paths, dynamic import paths, or mutation-test weaknesses.
8. Is the evaluation design hard enough to distinguish the Agent from trivial
   baselines and recent-deploy guessing? Check decoys, fixture difficulty,
   author/evaluator conflicts, false-positive controls, power/variance, and sealed
   gold handling.
9. Are KDD winner and DeepSeek mechanisms adopted at the right level, or has the plan
   cargo-culted their artifacts, language, or orchestration without production
   evidence?
10. Is provisional Python a sound M0-F0 choice behind replaceable ports, or is the
    current toolchain receipt self-justifying? Give explicit keep/replace triggers.
11. Can M0-F1 through M0-F5 be completed as a coherent local fixture-backed vertical
    slice without pretending that production authorization or Committee acceptance
    has occurred?
12. Can another engineer continue during the Owner's August 24 to September 14
    absence, and can the Owner restart after three weeks without reconstructing
    hidden context?
13. What is the smallest evidence-backed implementation sequence that maximizes
    learning while preventing semantic drift and duplicate implementations?
14. What failure scenario would make an apparently green local M0 dangerous or
    misleading in the enterprise review process?

## Verification expectations

- Verify branch, HEAD, dirty state, and relevant file digests at start and finish.
- Run the Phase A suite from the documented working directories.
- Reproduce deterministic replay independently.
- Use isolated copies for mutation or fault injection. Do not mutate the live package.
- Audit acceptance-ID definitions and references mechanically.
- Check English-only controlling documents and local Markdown links where relevant.
- Distinguish product defect, planning drift, test weakness, missing evidence,
  production-authorization gap, and reviewer preference.
- A passing test suite is not production authorization, Committee acceptance, or a
  freeze verdict.

## Required finding format

Each finding must include:

- stable ID and severity: `BLOCKER`, `MAJOR`, `MINOR`, or `NOTE`;
- concise claim;
- evidence with exact file/line or command/result anchors;
- affected Owner decision, contract, implementation surface, or acceptance criterion;
- strongest counterargument;
- falsifier or closure evidence;
- disposition: `fix_before_freeze`, `fix_before_implementation`, `defer_with_gate`,
  `owner_decision_required`, or `reject_finding`;
- whether it changes the candidate packet bytes.

Do not report speculative concerns as confirmed defects.

## Required outputs

Write only these files in this directory:

1. `fable5-phase1-independent-findings.md`
2. `fable5-final-adversarial-review.md`
3. `fable5-review-status.json`

The final report must include:

- executive verdict: `ACCEPT`, `ACCEPT_WITH_CHANGES`, `REJECT`, or `BLOCKED`;
- reviewed packet path, exact SHA-256, branch, and HEAD;
- Phase A package aggregate digest and reproduced test evidence;
- subagent/workflow roster with model, lane, and status;
- finding counts and a complete finding table;
- comparison with the current Opus freeze review after Phase I is sealed;
- explicit conflict resolutions and unresolved Owner decisions;
- exact corrections required before freeze;
- exact gates that remain after a local M0 freeze;
- recommendation for the next implementation session and which model should execute
  and independently verify each critical slice.

The JSON status must include at least:

- `reviewer`, `model`, `effort`, `status`, and `verdict`;
- `reviewed_packet_path` and `reviewed_packet_sha256`;
- `phase_a_package_sha256`;
- `phase1_report_sha256`;
- `subagents_used` and `workflow_lanes_used`;
- severity counts;
- `opus_comparison_status`;
- `blocked_by`;
- `allowed_writes`;
- `forbidden_actions`.

If the packet changes during review, stop with `BLOCKED` and identify the old and new
digests. Do not silently review mixed bytes.

## Stop condition

Stop when the required outputs are complete, or when an unavailable prerequisite
prevents evidence-backed completion. Do not start implementation. Do not repair code
or controlling documents. Return corrections to the main orchestrator as findings.
