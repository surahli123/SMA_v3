# Fable 5 Architecture Finalization Handoff

## Mission

Act as the architecture facilitator and final synthesizer for the enterprise
Experiment Post-Analysis Data Agent. Discuss unresolved architecture decisions with
the Owner in Chinese, one consequential question at a time. After the Owner confirms
shared understanding and the active independent reviews are reconciled, finalize an
English architecture design document and two self-contained English HTML diagrams.

This is a design and documentation task. It is not product-code implementation.

## Working language and interaction contract

- Speak with the Owner in concise, plain Chinese.
- Ask exactly one architecture-changing question per turn and wait for the answer.
- For every question, state your recommended answer and the main tradeoff in simple
  language.
- Do not ask the Owner for repository facts that you can inspect.
- Start by briefly restating the current shared understanding and then ask the first
  highest-leverage unresolved question.
- Record every resolved Owner decision in the English decision ledger with its source
  and date. Do not turn a reviewer preference into an Owner decision.
- When you believe the design is coherent, show the Owner a concise Chinese summary of
  the proposed architecture, remaining gaps, and exact planned writeback. Ask for an
  explicit freeze/writeback confirmation before finalizing canonical documents.

## Required skills

Read and use these skills and their directly required references before producing the
corresponding work:

- `/Users/surahli/.agents/skills/fable5-best-practice/SKILL.md`
  - especially the blind-spot pass, pre-mortem, model routing, evidence-backed status,
    and bounded workflow guidance;
- `/Users/surahli/.codex/skills/grill-with-docs/SKILL.md`;
- `/Users/surahli/.codex/skills/grilling/SKILL.md`;
- `/Users/surahli/.codex/skills/domain-modeling/SKILL.md`;
- `/Users/surahli/.codex/skills/documentation-and-adrs/SKILL.md`;
- `/Users/surahli/.codex/skills/repo-diagram-generator/references/diagram-design/SKILL.md`;
- `/Users/surahli/.codex/skills/repo-diagram-generator/references/diagram-design/style-guide.md`;
- `/Users/surahli/.codex/skills/repo-diagram-generator/references/diagram-design/type-architecture.md`;
- `/Users/surahli/.codex/skills/repo-diagram-generator/references/diagram-design/type-flowchart.md`.

Use the editorial `diagram-design` visual system as the authority. If you inspect the
Cocoon architecture skill, reuse only useful self-contained HTML/SVG mechanics; reject
its dark neon cyan/purple skin and blanket monospaced typography.

## Current authority and facts to verify

Verify these against the live worktree before relying on them:

- Repository: `/Users/surahli/Documents/projects/SMA_v2`
- Expected branch: `codex/kdd-data-agent-practices-research`
- Expected starting HEAD: `28cbbda6e4d4d7f08134952d38433e52d3ee8768`
- The worktree is heavily dirty and contains user-owned work. Preserve it.
- The main first deliverable is M0 Flight Readiness. `Flight` means one A/B test and
  is equivalent to one `Experiment`.
- The program target is a fixture-backed local M0 MVP first, then one authorized
  production Flight through the M0-M2 validation slice. Technical packet completion
  is not Experiment Review Committee acceptance.
- The Experiment Owner runs the experiment, the Independent DS Consultant challenges
  it, and the Experiment Review Committee makes the final review decision.
- The first M0 path defaults to one decision metric, while the target contract must
  support a frozen set of multiple equally important decision metrics.
- Old SMA metric definitions, schema catalogs, business-table routes, fixtures, code,
  and architecture are historical candidates only. Current production authorities
  and named owners control real metric and data meaning.
- Invalid experiments permit only validity, instrumentation, or data-quality
  remediation. The Agent may produce a correct, reviewable, unapplied candidate diff
  only when its exact-target and safety gates are satisfied. It never mutates,
  applies, deploys, or rolls back anything.
- The primary builder's 2026-08-24 through 2026-09-14 leave is excluded from active
  engineering time. End of September is a stretch target, not a promised approval
  date. Architecture must support a reproducible continuity checkpoint.
- Phase A currently claims `PASS_WITH_GAPS`, 225 tests from three working directories,
  deterministic replay across `PYTHONHASHSEED=0/1/12345`, and package aggregate
  SHA-256 `2f1001b93b19b2318c4c6419205ed2f7778ac23c02533e78a0c0899f15bf7d1e`.
  Treat Python as a provisional, replaceable M0-F0 engineering choice, not an
  Owner-frozen architecture decision.
- M0-F1 through M0-F5 have not started. The prior implementation authorization is
  exhausted. This task grants no implementation authority.
- Current freeze candidate:
  `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md`
- Candidate SHA-256 observed before this dispatch:
  `40c7234f3c0d85f18ebfba656e7aec2ab5ab71b86451a077ecad340eac779396`.
  Recompute it before citing it because active reviews may require changes.

The latest durable Owner record outranks older planning prose. When documents conflict,
surface the conflict and ask only if it changes Owner intent; never silently choose the
convenient interpretation.

## Read-first evidence order

Read these before the interview so that questions target judgment rather than facts:

1. `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/owner-alignment-record.md`
2. `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-owner-six-question-grill.html`
3. `docs/research/kdd-data-agent-workshop/session-records/grill-me-decision-log.md`
4. `docs/research/kdd-data-agent-workshop/planning-decision-packet.md`
5. `docs/research/kdd-data-agent-workshop/wayfinder/freeze-canonical-domain-policy-contracts.md`
6. `docs/research/kdd-data-agent-workshop/final-architecture-spec.md`
7. `docs/research/kdd-data-agent-workshop/implementation-sequencing.md`
8. `docs/research/kdd-data-agent-workshop/eval-acceptance-plan.md`
9. `docs/research/kdd-data-agent-workshop/enterprise-experiment-post-analysis-profile.md`
10. `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md`
11. `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-codex-continuation-receipt.md`
12. `.agents/skills/kdd_data_agent/TOOLCHAIN_RECEIPT.md`
13. `docs/research/kdd-data-agent-workshop/source-manifest.md`
14. `docs/research/kdd-data-agent-workshop/research-synthesis.md`
15. `docs/research/kdd-data-agent-workshop/cross-research-consistency-audit.md`
16. `docs/research/kdd-data-agent-workshop/champion-repo-reverse-audit.md`
17. `docs/research/kdd-data-agent-workshop/fourth-place-repo-reverse-audit.md`
18. `docs/research/kdd-data-agent-workshop/creative-team1286-practices.md`
19. `docs/research/kdd-data-agent-workshop/creative-team1401-practices.md`
20. `docs/research/kdd-data-agent-workshop/deepseek-harness-practices.md`

Use the KDD and DeepSeek work at the mechanism level: bounded stages, narrow tools,
artifact workspaces, deterministic replay, evidence receipts, visible trace, recovery,
and independent review. Do not cargo-cult their language, runtime, benchmark harness,
UI, or architecture into an enterprise production system without evidence.

## Active reviews that must be reconciled

Two independent reviews were active when this task was dispatched:

- Opus 5 freeze review: background ID `671d8db1`, full session ID
  `671d8db1-a104-40ae-8dde-acaef53cf2e0`.
- Fable 5 independent adversarial review: background ID `4bda4e93`, full session ID
  `4bda4e93-77b6-4361-acb1-37e9bbfbadc4`.

Their expected durable outputs are under:

- `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/`
- `docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-m0-adversarial-review/`

Do not assume either reviewer has accepted the freeze. Read only completed, persisted
outputs. Classify every imported point as Owner decision, observed evidence, reviewer
finding, engineering proposal, or open gate. Reconcile evidence-backed findings before
final writeback. If a required review is still incomplete, you may continue the Owner
interview and drafts, but the final state must remain `DRAFT_AWAITING_REVIEW`; do not
claim the architecture is frozen.

## Architecture questions to settle

Do not mechanically ask this list. Inspect what is already resolved, run a blind-spot
pass and pre-mortem, then ask only the highest-leverage unresolved questions one at a
time. The finalized design must nevertheless make these areas explicit:

1. The exact M0 decision and the boundary between local readiness, production
   authorization, review readiness, and Committee acceptance.
2. The canonical `ExperimentReadContract` and `FlightReadinessPacket` responsibilities,
   without silently freezing implementation-language schemas.
3. Legal readiness-state pairs, materiality, checks, `NextSafeAction`, stop conditions,
   budget ceilings, and acceptance-ID semantics.
4. How current production metric/catalog/table authority is resolved, versioned,
   scoped, and represented as a Coverage Gap when unavailable or contradictory.
5. Evidence, Claim, Cause Verdict, Recommendation Readiness, Action Approval, Case
   generation, Incident State, and immutable supersession boundaries.
6. The enterprise A/B evidence path from intended treatment through assignment,
   exposure, metric derivation, heterogeneity, production change candidates, causal
   challenge, verification, recommendation, and human ruling.
7. Separation between canonical packet/evidence projections and diagnostic Trace;
   Trace is not universally mandatory, and only Trace-dependent claims are blocked
   when capture receipts are missing.
8. Safe valid-but-unapplied candidate diffs, capability isolation, human-only handoff,
   and explicit exclusion of automation consumers.
9. Fixture difficulty, trivial baselines, decoys, blind gold, independence/conflict
   receipts, calibration, and pilot-owned numeric thresholds.
10. Continuity, replaceable interfaces, recovery, and what another builder needs during
    the Owner's leave.
11. The minimum M0 implementation slice that proves the architecture without pretending
    M1/M2, production access, or Committee approval already exists.
12. Which decisions are truly architectural and deserve ADRs; avoid ADR inflation.

## Domain-model discipline

Use the `domain-modeling` skill while interviewing. Preserve orthogonality between:

- Case lifecycle and Case generation;
- Stage;
- Evidence and Derived Fact;
- Claim;
- Cause Verdict (`observed`, `suspected`, `action-ready`, `confirmed`);
- Recommendation Readiness;
- Action Approval;
- Incident State;
- packet generation, review readiness, production authorization, Committee decision,
  and production outcome.

Challenge overloaded terms immediately. Update a glossary only for genuinely resolved
domain language and keep implementation details out of it. Create or revise an ADR only
when the decision is hard to reverse, surprising without context, and based on a real
tradeoff.

## Workflow and model budget

Fable 5 owns judgment, interview, conflict resolution, and final synthesis. It may use
no more than five total subagents or workflow lanes, including nested delegation.

- Prefer Opus 5 for a fresh architecture/domain-model challenge, security/capability
  boundary review, statistical/causal contract review, and diagram/taste critique.
- Use Sonnet 5 only for bounded evidence extraction, cross-document consistency tables,
  and mechanical link/language/HTML checks.
- Keep first-pass reviewer conclusions independent. Require compact evidence packets,
  not hidden reasoning transcripts.
- Fable must personally verify the evidence behind every BLOCKER and every final
  architecture decision.
- Fable and all delegated agents remain documentation/review-only. They may not write
  product code.

## File ownership and phases

### Phase 1: discussion and draft

Until the Owner explicitly confirms the proposed design and authorizes canonical
writeback, write only inside this directory:

- `architecture-decision-ledger.md`
- `architecture-design-draft.md`
- `architecture-overview-draft.html`
- `m0-review-flow-draft.html`
- `architecture-finalization-status.json`

Keep each artifact visibly marked `DRAFT`. Do not modify canonical planning,
architecture, sequencing, evaluation, glossary, ADR, prototype, or implementation
files in Phase 1.

### Phase 2: finalization after explicit Owner confirmation

After the Owner explicitly approves the shared understanding and says to freeze/write
back, and after completed active-review findings are reconciled:

1. Produce these final English artifacts in this directory:
   - `architecture-design-final.md`
   - `architecture-overview.html`
   - `m0-review-flow.html`
   - `architecture-freeze-record.json`
2. Update only the minimum canonical English documentation required for consistency:
   - `docs/research/kdd-data-agent-workshop/final-architecture-spec.md`
   - `docs/research/kdd-data-agent-workshop/implementation-sequencing.md`
   - `docs/research/kdd-data-agent-workshop/deliverable-index.md`
   - a domain glossary or ADR only when the skill's strict creation criteria are met.
3. Re-read each target immediately before editing and preserve unrelated user changes.
4. Record exact file digests, revision label, source review paths, unresolved gates,
   and the Owner approval evidence in `architecture-freeze-record.json`.

If the Owner approves the design but an active review remains incomplete or contains an
unresolved BLOCKER, produce final-shaped artifacts labeled `APPROVED_PENDING_GATE` and
stop before canonical writeback or freeze claims.

## Diagram requirements

Create self-contained HTML with inline SVG and embedded CSS. No external images and no
JavaScript is required. Labels and explanatory text in durable artifacts are English.

### Architecture overview

- Editorial light style: warm paper, ink, muted slate, and one coral accent.
- Maximum nine nodes, twelve arrows, and two accent elements.
- Group by authority/trust boundary and keep one clear primary flow.
- Show production authorities and read-only adapters feeding an evidence workspace;
  deterministic gates and claim/evidence reasoning; immutable packet/review surface;
  and human roles/Committee decision.
- Show diagnostic Trace as a separate, untrusted operational store cross-linked to
  Evidence, not as part of the immutable packet digest unless a stable digest contract
  is explicitly decided.
- Make no node decorative. Every node must answer an architectural question.

### M0 review flow

- Top-down flowchart. Shape, not color, communicates node type.
- Label every branch.
- Distinguish invalid experiment, missing authority, Coverage Gap, blocked readiness,
  eligible decision-grade readiness, typed next-safe action, human review, and the
  Committee boundary.
- Never imply that an M0 packet authorizes mutation, deployment, rollback, M1/M2 causal
  conclusions, or Committee acceptance.

Run the diagram skill's taste gate: no neon/glow, no shadows, no generic equal card
wall, no blanket mono font, no excessive accent colors, no unlabeled decision branches,
and no diagram that a short paragraph would explain better.

## Final architecture document requirements

The final document must be implementation-ready without pretending open production
facts are known. Include:

- scope and non-goals;
- actors, authority, and human decision boundaries;
- canonical domain model and invariants;
- system context, trust boundaries, and read-only capability model;
- component responsibilities and replaceable ports;
- M0 end-to-end sequence and decision logic;
- evidence authority, provenance, ACL/privacy/redaction, and Coverage Gap behavior;
- packet, revision, digest, supersession, and dependency invalidation contracts;
- Trace versus Evidence semantics;
- candidate-diff safety and delivery boundary;
- fixture/evaluation/calibration contract;
- failure, recovery, stop, and continuity behavior;
- M0-to-M2 sequencing and explicit gates;
- KDD/DeepSeek Adopt/Adapt/Reject decisions;
- alternatives rejected and why;
- unresolved production decisions with named owners and falsifiers;
- acceptance evidence and a traceability table from Owner decisions and accepted review
  findings to architecture sections.

Separate target architecture from migration/toolchain choices. Python/Pytest and any
specific schema library remain provisional unless the evidence and Owner explicitly
freeze them.

## Verification and stop conditions

Before any final claim:

- verify branch, HEAD, dirty state, and all modified paths;
- verify completed review output paths and exact digests;
- check local Markdown links for files touched;
- run `git diff --check`;
- confirm all durable final docs and diagram labels are English;
- open/render both HTML diagrams and inspect them at desktop and narrow widths;
- verify no product code, test, fixture, Git history, branch, remote, production system,
  external message, or deployment was modified;
- distinguish `DRAFT`, `APPROVED_PENDING_GATE`, and `FROZEN` precisely.

Stop and report `BLOCKED` rather than guessing when a product decision, completed
independent review, production authority, or Owner freeze confirmation is missing.

## Forbidden actions

- No product or agent code changes.
- No changes to `.agents/skills/kdd_data_agent/` or legacy SMA implementation paths.
- No test or fixture changes.
- No production access, credentials, real company data, network mutation, or external
  messages.
- No commit, push, pull request, branch creation/switch, package installation, or global
  configuration change.
- No M0-F1 through M0-F5 implementation and no implementation authorization claim.
- No silent canonical freeze while active review findings or Owner decisions remain
  unresolved.

## First response

After reading the required evidence, begin in Chinese with:

1. a compact statement of what you believe is already decided;
2. the single most important architecture ambiguity that remains;
3. your recommended answer and why;
4. exactly one question for the Owner.

Do not start with a long plan, a generic greeting, or multiple questions.
