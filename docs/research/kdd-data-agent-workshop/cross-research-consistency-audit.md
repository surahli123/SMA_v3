# Cross-Research Consistency Audit

Date: 2026-08-12

Status: Current-authority audit of the English research and specification package. M0 is the first gate and main deliverable in an Owner-aligned one-Flight M0-M2 validation program. The current executable scope is the local fixture-backed M0 MVP; production authority, M1/M2 implementation, calibrated evaluation, and live review-surface acceptance remain separately gated. The single authorized terminal Fable attempt failed closed at the live availability gate. This document does not authorize production access, mutation, commit, push, or publication.

## 1. Audit Scope and Proof Standard

This audit checks whether the research record, planning decisions, canonical specification, implementation sequence, evaluation design, and source manifest describe one coherent greenfield Data Agent.

It uses the following authority order:

1. Owner-confirmed product decisions in the [Owner alignment record](reviews/2026-08-16-opus5-m0-alignment/owner-alignment-record.md) and [planning decision packet](planning-decision-packet.md).
2. The digest-bound M0 alignment packet after its independent review and freeze record; until then it is a freeze candidate, not higher authority.
3. The closed [canonical domain and policy contract](wayfinder/freeze-canonical-domain-policy-contracts.md).
4. The [canonical architecture specification](final-architecture-spec.md).
5. Closed future Wayfinder resolutions for the decision surface they own.
6. The [implementation sequence](implementation-sequencing.md) and [evaluation acceptance plan](eval-acceptance-plan.md), where they conform to higher authority.
7. Direct source observations and fixed-source audits recorded in the [source manifest](source-manifest.md).
8. Author claims, reviewer inferences, and engineering proposals, each retaining its original label.

Absence of a detected conflict is not proof of completion. A requirement is complete only when the named authoritative artifact and its required receipt, human ruling, or observed evidence exist. An open Wayfinder ticket cannot be closed by source inference, a green mechanical check, or this audit.

Historical reports may preserve what was observed, claimed, or undecided when they were written. When their old planning vocabulary conflicts with the current contract, the source observation remains valid but the old product interpretation is superseded. Current authority must be stated explicitly; historical text must not silently become normative.

## 2. Current Authority Snapshot

### 2.1 Frozen Logical Contract

The following items are no longer open design questions:

- One Flight is one A/B Experiment. M0 Flight Readiness is the first gate and main deliverable: freeze `ExperimentReadContract`, verify the setup and decision-metric read, and seal `FlightReadinessPacket`. M1 production grounding and M2 Win/Loss continue the same validation program after their named gates and separate implementation-start receipts ([Owner alignment record](reviews/2026-08-16-opus5-m0-alignment/owner-alignment-record.md)).
- Scenario B is deferred: it later adds SEV changepoint, rollback-ready packet, recovery verification, continuing RCA, and human incident-state behavior while reusing the shared substrate ([architecture specification, Section 11](final-architecture-spec.md)).
- Cause Verdict is `unassessed | suspected | confirmed | ruled_out | inconclusive` ([closed policy contract, Cause Verdict](wayfinder/freeze-canonical-domain-policy-contracts.md)).
- Recommendation Readiness is `not_applicable | blocked | proposal_ready | action_ready | rejected` ([closed policy contract, Recommendation Readiness](wayfinder/freeze-canonical-domain-policy-contracts.md)).
- `observed` belongs to Evidence or an Observed Fact Claim. It is not a Cause Verdict ([closed policy contract, canonical language](wayfinder/freeze-canonical-domain-policy-contracts.md)).
- Runtime Gates `G0`–`G7` are the only causal-promotion gate set. `confirmed` requires all applicable gate conditions plus the independent G7 causal ruling ([closed policy contract, Gate 0–7](wayfinder/freeze-canonical-domain-policy-contracts.md)).
- Evidence Graph and Trace are different cross-linked projections. Tool order, retries, logs, model narration, and timing do not become claim Evidence merely because they appear in Trace ([architecture specification, Section 14](final-architecture-spec.md)).
- Critical Experiment invalidity permits only typed validity, instrumentation, or data-quality guidance and, after exact-target, authority, validation, capability-isolation, and human-only delivery gates, a separately typed correct `not_applied` remediation diff. Production-cause and product-logic hypotheses remain blocked ([Owner alignment record, O3](reviews/2026-08-16-opus5-m0-alignment/owner-alignment-record.md)).
- HIGH risk or large blast radius cannot become `action_ready`, even when Cause is `confirmed` ([closed policy contract, fail-closed behavior](wayfinder/freeze-canonical-domain-policy-contracts.md)).
- Causal Reviewer, Action Approver, Experiment Owner/code-domain reviewer, and Incident Owner have separate responsibilities. Human judgment never replaces missing Evidence ([closed policy contract, human responsibility split](wayfinder/freeze-canonical-domain-policy-contracts.md)).
- Corrections are append-only; `supersedes`, `invalidated_by`, dependency-closure recomputation, new Case Generations, and superseding immutable packets preserve history ([architecture specification, Section 12](final-architecture-spec.md)).
- No state, gate, verdict, readiness value, packet, or human ruling gives the Agent mutation authority. Candidate diffs remain `not_applied`; rollback-ready packets remain human-facing ([architecture specification, Sections 5 and 16](final-architecture-spec.md)).

### 2.2 Open Prerequisites

The following are explicitly not complete:

| ID | Current evidence | Still required before closure |
| --- | --- | --- |
| P2 — Production evidence authority | The ticket is open and claimed; a structured intake exists ([P2 ticket](wayfinder/establish-production-evidence-authority.md)). | Production owner, Engineering, and security/privacy must identify and approve authoritative sources, mapping ownership, tenant/ACL boundaries, raw-evidence handling, retention/redaction, credentials, and safe read limits. |
| P3 — Observability-first review surface | A research/design prototype is available, but the ticket remains open and claimed ([P3 ticket](wayfinder/prototype-observability-first-review-surface.md)). | Live owner/reviewer use must show that the hierarchy and interactions improve observability and review efficiency. A screenshot or static critique cannot close this gate. |
| P4 — Evaluation gold and calibration | A threshold-free contract is prepared; the ticket remains open and claimed ([P4 ticket](wayfinder/freeze-evaluation-gold-and-calibration.md)). | Blind historical adjudication, code/domain and production Evidence, pilot distributions, human baseline, dispute receipts, calibrated numeric decisions, and named owner/Eng/security/privacy approvals. |
| Terminal adversarial review | The [availability receipt](fable-terminal-review-availability-receipt.md) records that the single authorized 03:00 attempt reached the live gate and was blocked because Claude Code explicitly marked `claude-fable-5` unavailable. | No review or findings exist. The one-time automation is paused. Any future attempt requires fresh owner authorization; Fable remains a reviewer, not a fact source. |

The canonical logical spec can therefore be used as the design authority, but the package cannot claim Scenario A production GO, approved production access, calibrated reliability, or accepted final UI interaction.

## 3. Cross-Artifact Consistency Findings

### C1 — Scenario Scope and Greenfield Boundary: Consistent

The [Owner alignment record](reviews/2026-08-16-opus5-m0-alignment/owner-alignment-record.md), [planning decision packet](planning-decision-packet.md), [architecture specification](final-architecture-spec.md), [implementation sequence](implementation-sequencing.md), and [evaluation plan](eval-acceptance-plan.md) consistently make M0 Flight Readiness the first gate and main deliverable, place M1/M2 in the same separately gated one-Flight validation program, and defer Scenario B. Old SMA, the workshop, and winning systems are rejectable references rather than compatibility or migration constraints.

Evidence anchors:

- [Planning decision packet, confirmed destination](planning-decision-packet.md)
- [Architecture specification, product outcome and scope](final-architecture-spec.md)
- [Implementation sequence, target design versus delivery path](implementation-sequencing.md)
- [Research synthesis, executive conclusion](research-synthesis.md)

Disposition: preserve. No report may imply that old modules, schemas, language, storage, or orchestration must be carried into the new system.

### C2 — Canonical State Vocabulary and Gate Contract: Consistent in Current Authority; Historical Vocabulary Superseded

The closed policy ticket and final specification agree on the two independent axes, the location of `observed`, legal axis combinations, human separation, append-only correction, and fail-closed `G0`–`G7` behavior. Older research phrases such as a single `observed | suspected | action-ready | confirmed` axis, `actionable | likely | confirmed`, or `Gate 0–3` are historical research vocabulary, not alternative contracts.

Evidence anchors:

- [Closed policy contract, independent state contracts](wayfinder/freeze-canonical-domain-policy-contracts.md)
- [Closed policy contract, deterministic two-axis policy matrix](wayfinder/freeze-canonical-domain-policy-contracts.md)
- [Architecture specification, canonical state and policy](final-architecture-spec.md)
- [Architecture specification, Gate 0–7 contract](final-architecture-spec.md)
- [Team 1286 current-authority terminology note](creative-team1286-practices.md)
- [Team 1401 current-authority terminology note](creative-team1401-practices.md)

Disposition: current canonical language governs implementation and acceptance. Historical labels may remain only when clearly attributed to their source era and accompanied by a supersession note.

### C3 — Planning Prerequisites P1–P4 Versus Runtime Gates G0–G7: Consistent and Must Remain Distinct

The implementation sequence deliberately renames the four Wayfinder decisions `P1`–`P4` so they cannot be confused with per-Case causal gates `G0`–`G7` ([implementation sequence, Two kinds of gates](implementation-sequencing.md)). P1 is closed. P2–P4 are open human/program prerequisites. Runtime G0–G7 operate on a Case and produce GateReceipts; they do not close planning prerequisites.

Illegal conflations include:

- treating P2 source authorization as a passed G2 runtime reachability receipt;
- treating a G7 human causal ruling as P3 live UI acceptance;
- treating a green fixture run as P4 calibration closure;
- renaming P1–P4 to G1–G4 in future implementation material;
- allowing any P-ticket closure to promote Cause Verdict or Recommendation Readiness automatically.

Disposition: preserve the naming and responsibility split throughout plans, tickets, implementation, and evaluation receipts.

### C4 — Invalid Experiment, HIGH Risk, and Human Authority: Consistent

The current spec, evaluation plan, and closed policy contract all fail closed:

- critical invalidity blocks production-change Recommendations and permits only validity, instrumentation, and data-quality repairs;
- HIGH risk or large blast radius caps Recommendation Readiness at `blocked`;
- missing authority, material contradiction, or human timeout remains visible and blocks publication or progression;
- causal review, action approval, and incident status are distinct;
- no human ruling or state grants Agent mutation authority.

Evidence anchors:

- [Architecture specification, system invariants](final-architecture-spec.md)
- [Architecture specification, invalid-experiment branch](final-architecture-spec.md)
- [Closed policy contract, fail-closed behavior](wayfinder/freeze-canonical-domain-policy-contracts.md)
- [Evaluation acceptance plan, Gate receipts and hard vetoes](eval-acceptance-plan.md)

Disposition: preserve. Any future shorthand such as “human approved” must identify the human role, exact immutable input, decision type, expiry, and what authority it does not grant.

### C5 — Candidate Diff and Rollback Packet Semantics: Consistent

Scenario A may produce an exact deployed-target-bound diff only when the experiment is valid and the required policy conditions pass. The diff is rendered and serialized as `not_applied`. Scenario B may later produce a rollback-ready packet bound to the deployed SHA and scope, but the Agent never rolls back. These are recommendation artifacts, not mutation commands.

Evidence anchors:

- [Planning decision packet, success criteria](planning-decision-packet.md)
- [Architecture specification, candidate diff](final-architecture-spec.md)
- [Architecture specification, Scenario B extension](final-architecture-spec.md)
- [Implementation sequence, Scenario A workflow](implementation-sequencing.md)

Disposition: preserve the literal `not_applied` marker in schema, packet, UI, evaluation, and handoff. Do not replace it with a vague label such as “preview.”

### C6 — Evidence Graph, Trace, and Winning-System Observations: Consistent After Temporal Supersession

The source studies support four different observations:

- Team 1286 video shows a source graph, groups, node/group detail, `Re-layout`, findings navigation, and an answer-path graph. It does not prove production causal edges, claim invalidation, graph filtering, or a complete A/B chain ([Team 1286 graph packet](creative-team1286-practices.md)).
- Team 1401 video shows schema/PDF graphs, typed relation visuals, clusters, collapse/expand, type filtering, detail, and page location. It does not prove extraction accuracy, server enforcement, deployed runtime mapping, or production causality ([Team 1401 graph and trace observations](creative-team1401-practices.md)).
- Champion has no observed interactive evidence graph; its static architecture graphic and logged trajectories are not one ([Champion graph audit](champion-repo-reverse-audit.md)).
- Fourth-place has no observed node-edge evidence graph; its matrix, dashboard, and click-through trace viewer serve evaluation/debugging instead ([Fourth-place graph audit](fourth-place-repo-reverse-audit.md)).

No winning system proves the required production chain from metric through surface/component, query/result, ACL/corpus, pipeline/runtime, typed deployed change, Claim, verification, and Recommendation.

The historical Creative Track reports correctly say that the graph product contract was unconfirmed when those observations were written. Their current-authority notes now distinguish that historical statement from the frozen logical contract. The canonical specification now freezes the logical Evidence Graph/Trace separation, required node/edge semantics, local-first review entry, and alternative non-graph projections. P3 still owns final interaction and visual acceptance.

Evidence anchors:

- [Research synthesis, Evidence Graph and Review UI](research-synthesis.md)
- [Architecture specification, Evidence Graph, Trace, and review surface](final-architecture-spec.md)
- [P3 ticket and human gate](wayfinder/prototype-observability-first-review-surface.md)

Disposition: adopt observed navigation ideas selectively; reject graph decoration, arbitrary causal arrows, and Trace-as-Evidence. Do not describe P3 as reopening the frozen logical Evidence Graph contract.

### C7 — Evaluation Sequence and P4 Closure: Consistent

The evaluation design and implementation sequence agree on the order:

1. threshold-free fixture schemas, hard vetoes, and measurement hooks;
2. sealed rung-specific authorization;
3. authorized Evidence collection while P4 remains open;
4. applicable blind-case, replay, pilot, human-baseline, adjudication, and decision receipts;
5. named-human P4 closure;
6. Scenario A production GO only after the approved criteria pass with no hard veto.

P4 closure is not required before every offline fixture or before collecting the Evidence required to close P4. Production-like replay still requires P2 closure and explicit Engineering/security/privacy authorization. Narrow shadow-read requires additional named scope, isolation, retention, load, stop, reviewer, and exit authorization.

Ranking-bearing work before P4 closure now has an explicit non-circular path: the Evaluation Owner seals a non-production `pilot_ranking_policy` before Agent output, bound to the named rung and snapshot set, fixed features and normalization, deterministic ordering or pilot-only weights, stable tie-breaking, version/digest, expiry, and full-list retention. It may generate calibration Evidence but cannot authorize production priority or GO. A production-grounded blind historical case separately requires either P2 closure or a case-specific archival-snapshot authority receipt. Without exact deployed identity it may test abstention and workflow behavior, but not exact-target acceptance.

### C8 — G4 Challenge Semantics, Invalid Experiments, and G6: Consistent

G4 now separates challenge execution from causal result. A completed supporting challenge passes; a completed falsifier fails and yields Claim=`falsified`, Cause=`ruled_out`; a nondiscriminating result or blocked/failed execution is inconclusive. G7 requires the supporting pass, not mere receipt completion.

The invalid-experiment branch preserves discovered system hypotheses only as non-ranked, non-publishable blocked leads. It excludes them from production candidate output and keeps production Recommendations and candidate diffs `not_applicable`; only validity, instrumentation, and data-quality fixes are publishable.

For an unapplied Scenario A proposal, G6 may be satisfied by targeted pre-action replay/regression and guardrail Evidence while recovery and post-action recurrence are `not_applicable`. Recurrence-prevention and monitoring plans affect Recommendation Readiness separately; later action outcomes create superseding receipts rather than becoming a prerequisite for historical Cause confirmation.

Evidence anchors:

- [Architecture specification, evaluation and acceptance evidence](final-architecture-spec.md)
- [Implementation sequence, evaluation unit and start-before-gate table](implementation-sequencing.md)
- [Evaluation acceptance plan](eval-acceptance-plan.md)
- [P4 ticket, closure checklist](wayfinder/freeze-evaluation-gold-and-calibration.md)

Disposition: preserve this sequence. Do not invent top-k, run-count, SLA, cost, latency, stability, risk-weight, or shadow-exit thresholds before pilot distributions and required human decisions.

### C8 — Research and Design Boundary: Consistent

All current controlling artifacts remain research/design documents. The implementation sequence is a future execution order, not authorization to run `ce-work`. The package does not authorize implementation, production access, secrets, live adapter calls, candidate-diff application, deployment, rollback, commit, push, PR, or publication.

Evidence anchors:

- [Wayfinder map, Notes and Out of scope](wayfinder/map.md)
- [Architecture specification, authority and conformance](final-architecture-spec.md)
- [Implementation sequence, status and authority](implementation-sequencing.md)
- [Source manifest, usage rules](source-manifest.md)

Disposition: preserve until the owner explicitly opens an implementation phase and identifies its bounded starting unit.

## 4. Historical Reports and Canonical Supersession

Historical source reports serve two purposes that must not be collapsed:

1. preserve direct observations, timestamps, fixed SHAs, author claims, reviewer inferences, and unresolved contradictions; and
2. record the planning interpretation that was valid at the time.

Only the first remains timeless. The second is superseded where current authority has since resolved it.

| Historical statement class | Current treatment |
| --- | --- |
| Video/repo/source observation | Preserve unless stronger primary evidence directly corrects it; never rewrite a speaker claim as a repo fact. |
| “Owner has not confirmed the graph contract” | Preserve as historical context, but add that logical Evidence Graph/Trace semantics are now frozen and only P3 interaction acceptance remains open. |
| “Dual-axis enums are incomplete” | Superseded by the closed policy contract. |
| “Gate 0–7 fields/executors are proposals” | Superseded for the canonical contract by the closed policy ticket and final spec; still not an industry or winning-system fact. |
| `observed` used as a generic verdict | Superseded; it belongs only to Evidence or Observed Fact Claim state. |
| `Gate 0–3` or single-axis verdict shorthand | Preserve only as pre-contract research terminology with an explicit current-authority note. |
| “Final spec, Wayfinder, or implementation sequencing does not exist” | Materially false in the current repository and must not appear as current status. |
| Adopt/Adapt/Reject conclusion | Reviewer recommendation unless the planning packet or closed ticket explicitly promotes it to an owner decision. |

The [research synthesis](research-synthesis.md) remains a research-layer routing document, not competing authority. It now identifies the [planning packet](planning-decision-packet.md), closed policy ticket, and final specification as the current logical contract; P3 governs only the unresolved live interaction/visual gate.

## 5. Evidence Provenance That Must Remain Unchanged

The following facts are consistent across the source manifest and focused audits:

- Both workshop recordings have full-duration ASR coverage, but the transcript is not verbatim truth ([meeting alignment](meeting-audio-alignment.md)).
- All 73 screenshots are indexed and topic-aligned; screenshots are partial slides, so audio-only material must remain ([screenshot index](screenshot-index.md)).
- The OpenRouter Qwen attempt produced no usable second transcript; HTTP 400 is a coverage failure, not a model-quality verdict ([ASR comparison](qwen-whisper-asr-comparison.md)).
- `0.65` versus `0.69`, `25c` versus `35c`, the opening Qwen3.5 suffix, and Team 1401's `3-page PDF` versus graph `1 page` remain unresolved ([source manifest](source-manifest.md)).
- Champion source claims are anchored to fixed SHA `bdc874fc4260e3565ae0dce041728fdf5b376709`; its interrupted auxiliary extractor produced no independent evidence layer ([Champion audit](champion-repo-reverse-audit.md)).
- Fourth-place release source is anchored to `ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a`, separately from Phase 2 commit `13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65`; a derivative agent does not add independent confirmation ([Fourth-place audit](fourth-place-repo-reverse-audit.md)).

Disposition: preserve source class, timestamp/page/file/SHA anchor, uncertainty, and coverage. A missing source or failed retrieval stays a Coverage Gap rather than negative Evidence.

## 6. Completion Matrix

| Requirement | Authoritative evidence | Audit verdict |
| --- | --- | --- |
| Problem-driven greenfield boundary | Planning packet; final spec Sections 1–3 | **Proven** |
| M0 first gate/main deliverable; M1/M2 in the same separately gated validation program; Scenario B deferred | Owner alignment record; planning packet; final spec Sections 2, 3, and 11; implementation sequence | **Proven as Owner scope; local fixture-backed M0 implementation authorized** |
| Frozen dual-axis contract and `observed` placement | Closed P1 ticket; final spec Section 8 | **Proven** |
| Runtime G0–G7 and independent human review | Closed P1 ticket; final spec Section 9 | **Proven** |
| Evidence Graph distinct from Trace | Final spec Section 14; graph source audits | **Proven logically; P3 interaction acceptance open** |
| `not_applied` diff and no mutation | Planning packet; final spec Sections 5, 10.5, and 16 | **Proven as contract; optional invalid-Experiment remediation remains gated and implementation status must be checked separately** |
| Invalid-experiment and HIGH-risk ceilings | Closed P1 ticket; final spec Sections 5, 8, and 10.3 | **Proven** |
| Human responsibility separation | Closed P1 ticket; final spec Section 4 | **Proven** |
| Production source/access authority | P2 ticket and intake | **Not achieved; human evidence missing** |
| Numeric evaluation/calibration and pilot evidence | P4 ticket; evaluation plan | **Not achieved; threshold-free preparation only** |
| Final observability interaction/visual acceptance | P3 ticket and prototype | **Not achieved; live owner/reviewer acceptance missing** |
| Terminal Fable review and disposition | Availability receipt; no session or substitute review was created | **Attempted and correctly failed closed; review absent because Fable was unavailable** |
| Scenario A production GO | Requires P2–P4 closure, evaluation receipts, and no hard veto | **Not achieved** |
| Scenario B implementation readiness | Requires Scenario A decision and a separate owner-approved plan | **Deferred by design** |

## 7. Current GO / NO-GO Statement

**GO:** use the [canonical architecture specification](final-architecture-spec.md), [implementation sequence](implementation-sequencing.md), [evaluation acceptance plan](eval-acceptance-plan.md), and closed P1 policy contract as the coherent design package for final research review and a future bounded M0 implementation-authorization decision.

**NO-GO:** claim whole-program or production completion, close P2/P3/P4, select numeric thresholds, access production, treat a prototype as accepted, treat Fable as a fact source, implement the Agent, apply a diff, deploy, roll back, commit, push, or open a PR. This does not contradict completion of the narrower research/specification package in the current local worktree.

The next consistency audit must consume actual P2/P3/P4 human receipts. A future terminal Fable disposition is required only if the owner separately authorizes another attempt and that review successfully runs; the blocked attempt must not be hidden or rewritten as a completed review.
