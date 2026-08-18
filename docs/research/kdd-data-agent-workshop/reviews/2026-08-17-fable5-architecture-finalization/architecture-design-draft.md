# Enterprise Experiment Post-Analysis Data Agent — Architecture Design (DRAFT v3)

Status: `DRAFT` — Phase 1 discussion draft, revision `arch-final-draft-3` (budget closeout revision). Not frozen. Not design approval. Not an implementation authorization. The Owner closed the steelman discussion (S-close) and routed reconciliation, exact-byte review, and packaging to Codex; this job stops at `DRAFT` (see §21).
Facilitator: Claude Fable 5, Claude Code job `05b209ef`, 2026-08-18.
Owner conversation: Chinese. This document and its diagrams: English.
Companion files: `architecture-decision-ledger.md` (D1-D8, S1-S14, S-close, F1-F25), `architecture-overview-draft.html`, `m0-review-flow-draft.html`, `architecture-finalization-status.json`.

How to read this document:

- **Owner decision** rows cite `owner-alignment-record.md` (O1-O6), the closed P1 contract, or a `D*`/`S*` row in the decision ledger. They are product authority. Where a facilitator ruling conflicts with S1-S14 or D1-D8, the Owner decision controls.
- **Reviewer finding** rows cite the completed Opus 5 review (job `671d8db1`, sha256 `aa0a3b5d…`), the recovered main-session review (`b9d777ba`), or the sealed Fable Phase I findings (job `4bda4e93`, `FB-*`). They are evidence, not authority.
- **Facilitator ruling** rows (`F*`) are engineering or domain-model rulings proposed here. The Owner confirms or rejects them at freeze time.
- `PRODUCTION_BINDING_REQUIRED` marks a value that exists only on the company laptop and must not be invented (S2). `OPEN GATE` marks a decision nobody has made.

---

## 0. One-paragraph summary

The Data Agent is a read-only, evidence-first system. M0 decides whether one A/B `Flight` and its decision-metric read can be trusted. M1 explains the metric movement, grounds it in production, and may issue an explicit non-binding advisory. M2 collects query-level win/loss evidence. It never mutates, deploys, rolls back, or messages anyone. Every conclusion is a sealed, digest-bound packet whose facts trace to source-read receipts and deterministic derivations. Humans decide: the Experiment Owner prepares, the Independent DS Consultant challenges, and the Experiment Review Committee rules. `M0 capability demonstrated` is reached only when one real, authorized Flight runs end to end on the company laptop, its fixed core checks execute, its result is independently adjudicated as correct, and a reviewer-auditable packet exists (S1, S13); that is a program state, separate from any Flight's `analysis_use`. Fixture-backed M0 is pre-production evidence (S2). M0 blocking constrains M1 claims but does not forbid M1 investigation (S9).

---

## 1. Scope and non-goals

### 1.1 In scope (target architecture)

- M0 Flight Readiness: `ExperimentReadContract` in, immutable `FlightReadinessPacket` out.
- M1 Metric Movement and Production Grounding, including the non-binding Flight advisory (S6-S8), and M2 Win/Loss Evidence, as later slices of the same one-Flight validation program (O5), on the same substrate.
- Read-only evidence adapters, append-only workspace, deterministic checks, immutable packets, human review surface, separate diagnostic Trace.

### 1.2 In scope (currently authorized build)

- Phase A foundation exists and independently reproduces (225 tests; 19/22 and 34/38 mutation probes caught in two independent batteries).
- `M0-F1`-`M0-F5` (fixture-backed M0, pre-production evidence) have not started. The prior authorization is exhausted; a new Owner start receipt is required. The Owner has routed the next steps (reconcile, exact-byte review, M0 prototype, packaging, commit/push) to Codex (S-close).
- The first real Flight run on the company laptop is authorized only by a laptop-scoped M0 authorization receipt (D8), which does not exist yet.

### 1.3 Non-goals

- Migrating or wrapping old SMA, the KDD repositories, or DeepSeek Harness. They are mechanism references only. M0 fixtures do not derive from old SMA assets (D5).
- Any write path: diff apply, commit, push, PR, deploy, rollback, flag change, message, publication, incident-state change.
- A general-purpose data agent, arbitrary code execution, or an automation-consumable action or advisory feed.
- Treating a tool trace, model narration, vote, graph proximity, or repository commit as evidence.
- Committee acceptance, production authorization beyond D8, or numeric thresholds. These are external human decisions or `PRODUCTION_BINDING_REQUIRED`.
- Component-level guardrails or hidden thresholds invented after results are seen (S5).

---

## 2. Actors, authority, and human decision boundaries

| Actor | Owns | Must not own |
| --- | --- | --- |
| Experiment Owner | Flight design and execution; contract inputs; evidence package; answers to review questions | Final approval of their own production Flight |
| Independent DS Consultant | Independent challenge of methods, reads, evidence, uncertainty, risk; the challenge record attached to any M1 advisory (F21) | Final approval; evidence substitution |
| Experiment Review Committee | Experimentation triage/review; final `pass | change | block` for a real Flight; contextual component trade-off rulings (S5) | Agent execution; evidence invention; silent contract revision |
| Production / Engineering owner | Source authority, deployed identity, mapping, runtime reachability, load | Product-metric meaning; Committee acceptance |
| Security / privacy owner | ACL, tenant, sensitive fields, retention, redaction, credentials, recipients; informed party for the D8 receipt | Causal or launch decision |
| Evaluation Owner (P4) | Gold integrity, blinding, sealing, adjudication, calibration | Business judgment; weakening hard vetoes |
| Data Agent | Bounded read-only collection, validation, deterministic checks, packet generation, candidate preparation, explicit non-binding advisory (M1) | Mutation, approval, deploy, rollback, messaging, publication, hidden guardrails |

Boundaries (O4, S1, S2, S6):

- Fixture-only local work may record a time-bounded role overlap. A production Flight may not.
- **Five states are never interchangeable** (§6.6): fixture readiness, program `M0 capability demonstrated`, per-Flight `analysis_use`, M1 advisory readiness, Committee acceptance. The review surface shows program capability status and per-Flight `analysis_use` as two distinct fields (S13).
- The official metric result, the Agent advisory, and the Committee ruling are three separate records (S6).

---

## 3. Canonical domain model and invariants

### 3.1 Terms (glossary deltas proposed for `CONTEXT.md` in Phase 2)

| Term | Meaning | Not the same as |
| --- | --- | --- |
| `Flight` | One A/B `Experiment` (O1) | rollout window, run attempt, packet |
| `ExperimentReadContract` | The frozen, versioned statement of what is read: Flight identity, decision-metric set and `DecisionMetricPolicy`, units, estimator, population, window, sources, authority, roles, digest | dashboard config, query |
| `DecisionMetricPolicy` | The frozen rule naming decision metrics, how they combine, the preregistered `sufficiency_rule` (D1), the `comparison_rule_id` (F18), the multiplicity control when co-primary (F16), and the estimator registry reference (F16) | guardrail list |
| `Query Success` | The main decision metric: union of `TraditionalResultSuccess` and `AIAnswerSuccess` at query grain; thresholds fixed within a Flight and identical across arms (S3); values `PRODUCTION_BINDING_REQUIRED` | either component alone; a guardrail |
| Component metric | `TraditionalResultSuccess`, `AIAnswerSuccess`: diagnostic inputs of the union; not guardrails (S5) | decision metric |
| Preregistered sufficiency | Whether the observed Flight reached what was preregistered: runtime, and when declared, sample/units (D1). Not validity; not post-hoc power | validity, significance |
| Arm parity | Whether treatment and control were served by the same index generation, serving alias, ACL snapshot, effective pipeline (D2) | assignment balance, SRM |
| `M0CheckResult` | One check's outcome, materiality, rule id, evidence IDs, reason, reopen condition; IDs `CHK-01..CHK-19` (F11) | Gate receipt (M1) |
| `analysis_use` | The single stored M0 readiness state: `decision_grade | directional_only | not_permitted` (D3) | Cause Verdict; advisory |
| `post_analysis_eligibility` | Derived projection: `eligible` iff `decision_grade`, else `blocked` (D3) | a second stored field |
| Core material-check set | The S11 fixed core (authorization/identity; assignment/exposure/arm parity; metric formula, components, symmetric thresholds; population/grain/window; source authority, freshness, coverage; independent recomputation and registered statistical method; preregistered sufficiency) plus Flight-specific checks and `NOT_APPLICABLE` decisions selected before outcome reads, version- and digest-bound; unknown applicability defaults material; nothing removed after outcomes are observed | "all checks that happened to run" |
| `program_capability_status` | `not_demonstrated | demonstrated` for the program; `demonstrated` requires one real authorized Flight with fixed core executed, independent adjudication of the blocking/eligibility result, and a reviewer-auditable packet (S13); outcome-agnostic; never equals gate passage, launch approval, production authorization, or Committee Acceptance | per-Flight `analysis_use` |
| Recomputation independence class | `independent_source | independent_transform | same_pipeline` (D4); M0 minimum `independent_transform`; shared snapshot is a typed Coverage Gap (D6) | "we ran it twice" |
| `evidence_class` | `fixture | production_authorized` on every packet and receipt (F12) | a note in prose |
| `authorization_scope` | `fixture | laptop_owner_entitlement | p2_authorized` on every production-touching packet (D8) | P2 closure |
| Coverage Gap | Missing authority, timeout, unavailable/partial/stale/conflicting/redaction-failed read, unknown mapping, unchecked plane, shared source snapshot; never negative evidence (F1) | `evidence_state=stale`, `contradicts` |
| `NextSafeAction` | Exactly one of `evidence_collection | contract_correction | validity_fix | instrumentation_fix | data_quality_fix`; precedence F17; no target, no diff | remediation diff; advisory |
| `InvalidExperimentRemediation` | Typed guidance plus, only after gates, an exact unapplied diff (O3) | product-logic recommendation |
| `FlightReadinessPacket` | The immutable, digest-bound M0 output | report, dashboard |
| `human_state` | Experiment Owner submission state; DS challenge record; Committee decision `pending | pass | change | block`; acknowledgement and expiry (F10) | readiness; approval of the Agent |
| `FlightAdvisory` (M1) | An explicit, non-binding, evidence-bound opinion `recommend_pass | recommend_change | recommend_block | insufficient_evidence` with `target`, `basis`, scope bound to the Flight generation, evidence IDs, counterevidence, falsifier, and its own next safe action (`urgent_investigation`, validity remediation/rerun, …) (S6, S10, S12); a distinct dimension, not a Cause Verdict, not Recommendation Readiness, not `analysis_use` (F23); never implies a candidate diff (S14) | Committee ruling; Recommendation item; candidate diff |
| Orthogonal outcome evidence | A valid, scope-matched outcome-evidence stream not mechanically derived from the union metric (S7); by preference preregistered (F24); a post-unblinding stream carries change/block only after independent confirmation (S12) | a component of the union; a re-cut of the same events |
| `candidate_diff_eligibility` | The separate evidence- and change-type-driven gate a candidate diff must pass (S14): exact deployed identity and SHA, file/symbol attribution, reachability, supported mechanism, alternative/counterevidence challenge, independent code-domain review, LOW/MEDIUM risk; M2 corroboration mandatory for user-visible search semantics, rule-based `NOT_APPLICABLE` for deterministic technical corrections | advisory; Recommendation Readiness |
| Trace | Diagnostic record of what the Agent did. Cross-linked, never evidence | Evidence, receipt |

Orthogonal dimensions that stay independent (P1): Case lifecycle, Case generation, Stage, Evidence state, Claim state, Cause Verdict, Recommendation Readiness, Action Approval, Incident State. This design adds `analysis_use` (M0) and `FlightAdvisory` (M1) as further independent dimensions. No field implicitly changes another.

### 3.2 Invariants

1. Read-only authority: adapters have no write method; the workspace has append and resolve only.
2. Validity first: a materially invalid or unknown Flight yields no cause, candidate, ranking, product-logic recommendation, or advisory.
3. Sufficiency is preregistered, never post-hoc (D1).
4. Setup integrity includes arm parity (D2).
5. Fail closed: missing authority, zero reads, timeout, partial, stale, conflict, redaction failure, budget exhaustion, or human timeout becomes a Coverage Gap or blocker, never negative evidence or implicit approval.
6. Materiality defaults material; `non_material` needs a preregistered versioned rule; `NOT_APPLICABLE` needs a versioned applicability rule; stored materiality stays `unknown` when nobody classified it while the applied ceiling is material (F4).
7. One stored readiness state; eligibility is a projection (D3).
8. Deterministic facts: identical frozen inputs give byte-identical checks, packet, and digest.
9. Append-only history: corrections and supersession create new revisions; sealed packets are never edited.
10. Trace is not evidence and is not inside the packet digest.
11. No forced answer: `blocked` plus a typed next safe action, or `insufficient_evidence`, is a complete, acceptable result.
12. Current production authority wins over old SMA; adopted facts carry provenance, validation receipt, effective scope, and drift (O6). Fixtures never derive from old SMA (D5).
13. Fixture evidence is never production validation; every packet and receipt carries `evidence_class` and `authorization_scope` (S2, F12, D8).
14. The union is the sole decision metric; components are diagnostic; no hidden guardrail may be created after results are seen (S5).
15. An advisory that challenges an improving official metric requires at least one valid, scope-matched, orthogonal outcome-evidence stream (S7); a stream discovered after unblinding needs independent confirmation first (S12); otherwise `insufficient_evidence`.
16. The fixed core plus Flight-specific material checks are sealed before outcome reads and never removed afterwards (S11; D7 subsumed).
17. M0 blocking constrains M1 claims per evidence dependency; it does not forbid M1 investigation, and no blocker is waived by entering M1 (S9).
18. A validity-based `recommend_block` targets only `use_of_this_flight_as_decision_evidence`; it never blocks launch, authorizes rollback, or requests mutation (S10).
19. No advisory implies a candidate diff; diffs pass `candidate_diff_eligibility` (S14).

---

## 4. System context, trust boundaries, and capability model

Trust zones, outermost first:

1. **Production authorities (untrusted input, authoritative meaning).** Experiment platform, metric registry, source tables, scorecard/UI, deployed-identity systems, ACL/tenant systems. Reached in two ways only: (a) on the company laptop, under the D8 laptop-scoped receipt, through the Owner's existing read-only entitlement; (b) later, through P2-authorized read-only credentials physically incapable of writes plus an egress allowlist. Nothing here exists in the fixture-backed M0; the fixture adapter stands in.
2. **Capability Broker (constrained boundary, outside model execution).** Validates tool, adapter, resource, page/cursor, path, scope, budget, and cancellation before any read. Source content cannot expand capability. Denied requests create receipts and Coverage Gaps.
3. **Evidence workspace (append-only, case- and authorization-isolated).** SourceRead receipts, materialized immutable source-snapshot receipts (F25), Evidence revisions, derivations, Coverage Gaps, check results, revisions with predecessor digests.
4. **Deterministic gate and reasoning layer.** Flight Readiness Evaluator (M0); later Gate 0-7, policy engine, ranking, advisory builder (M1). Pure functions of frozen inputs; unknown rules fail closed.
5. **Immutable packet and review surface.** `PacketService.seal`, projection renderer, human handoff with named recipient, expiry, acknowledgement.
6. **Humans and Committee.** Outside the Agent's authority. Their rulings cite evidence IDs; they cannot replace missing evidence.
7. **Diagnostic Trace store.** Separate, untrusted operational store, cross-linked to SourceReads and stages, rendered under the same authorization context, never digested into the packet.

Company-laptop boundary (S2, D8, F22): the laptop is the only environment where production evidence exists. Raw evidence and source snapshots stay there. The durable export is the packet, its receipts, and the redaction manifest, each digest-bound. Deterministic replay against production is a laptop-side receipt; this repository holds contracts, fixtures, and exported non-sensitive packets only.

Capability isolation in the current package is static assurance (allowlist scan over every Python file, no dynamic import, no network/clock/filesystem write reachable), proven by mutation and audit-hook probes. It is not an OS or interpreter sandbox and must not be described as one. Known escapes (attribute chains, from-import smuggling; FB-05) must be closed and the receipt wording narrowed before `M0-F1` exit. Any future generated-code or plugin mechanism requires a non-replaceable runtime boundary that does not exist and is not authorized.

---

## 5. Component responsibilities and replaceable ports

Logical ports are technology-neutral (spec §6.2). Python, Pytest, and the current schema encoding are provisional M0-F0 choices (§18).

| Component | M0 responsibility | Failure behavior |
| --- | --- | --- |
| Case and Generation Manager | Frozen contract digest, generation identity, budgets, core-check preregistration (D7) | Never reactivates a closed generation |
| Capability Broker | Allowlist, scope, pagination, budget, cancellation, `authorization_scope` enforcement | Denial creates receipt + Coverage Gap |
| Evidence Adapter Port | Fixture reads now; laptop entitlement read under D8; one P2 source later | No write method; production adapters blocked before D8/P2 |
| Evidence Admission | Identity, authorization, freshness, digest, scope, validator, materiality; materializes an immutable snapshot receipt for the primary read (F25) | Tool success alone admits nothing; zero reads never become `observed` |
| Append-only Workspace | Revisions, typed relations, dependency edges, projections | No update/delete API; case and authorization isolation |
| Deterministic Derivation Engine | Metric recomputation of the union and its components with `independence_class`, input manifest, transform digest, output digest (D4/D6) | Every number names nonzero SourceRead IDs |
| Flight Readiness Evaluator | Contract validation, 19 checks, materiality, disagreement, Coverage Gaps, `analysis_use`, `next_safe_action`, component-divergence observed fact (§6.5), core-set execution status (D7) | Pure evaluation; emits no Claim, candidate, diff, advisory, or Win/Loss label |
| Packet and Handoff Service | Immutable `FlightReadinessPacket`, projection manifest, digest, expiry, supersession, acknowledgement, `evidence_class`, `authorization_scope` | Any material dependency revision requires a superseding packet |
| Projection Renderer | Packet-centered read-only M0 review projection; derives `post_analysis_eligibility` at render (D3); shows `evidence_class` and `authorization_scope` on the first screen (F12) | Maintains no truth; P3 gates final interaction |
| Trace Store | Optional diagnostic events, cross-links | Holds no canonical truth; loss is a diagnostic anomaly or Coverage Gap |
| Evaluation Harness | Hermetic fixtures, trivial baselines, decoys, independence receipts, replay checks (F13) | No numeric GO thresholds before P4 |
| Advisory Builder (M1, planned) | `FlightAdvisory` from M1 claims + preregistered orthogonal evidence + DS challenge record (S6-S8, F21, F24) | Never renders without the official metric result; `insufficient_evidence` when the floor is unmet |

Replaceable seams: adapter port (fixture -> laptop entitlement -> P2 source), derivation engine (recomputation path class), packet serialization (canonical JSON now; RFC 8785 or cross-language digest later), projection renderer (P3), Trace store (optional), advisory evidence registry (F24).

---

## 6. M0 end-to-end sequence and decision logic

### 6.1 Sequence

1. **Intake and freeze.** Accept an `ExperimentReadContract`. Validate required fields; keep unknowns as `UNKNOWN`/`MISSING`, never inferred. Compute the contract digest. Open a Case generation with a frozen-input digest, budget, `authorization_scope`, and the preregistered core material-check set (D7).
2. **Read.** Through the broker, request the primary decision-metric read and the sources named by the contract. Every read returns a receipt: identity, query digest, page/read set, completeness, authorization state, body policy, result digest, or a typed failure. The primary read is materialized as an immutable snapshot receipt (F25).
3. **Admit.** Evidence Admission turns each read into an Evidence revision or a Coverage Gap with kind and materiality.
4. **Recompute.** The Derivation Engine recomputes `Query Success` and both components through a separately versioned transform on the same snapshot; records `independence_class`, input manifest, transform digest, output digest (D4/D6).
5. **Evaluate.** Run `CHK-01..CHK-19` (§6.3). Each yields `PASS | FAIL | MISSING | UNKNOWN | NOT_APPLICABLE`, materiality, rule id, evidence IDs, reason, reopen condition.
6. **Decide.** Apply §6.4 to produce `analysis_use`, exactly one `next_safe_action`, and the core-set execution status.
7. **Seal.** Seal the packet: contract revision, snapshot and derivation receipts, checks, disagreements, Coverage Gaps (including `shared_source_snapshot`), `analysis_use`, blockers, next safe action, component-divergence observed fact, `human_state`, `evidence_class`, `authorization_scope`, authorization/redaction manifest, digest, expiry, supersession link. Optional link to a typed `InvalidExperimentRemediation`.
8. **Review.** Render the packet-centered projection. Human roles act on the sealed digest. Committee acceptance is external.

### 6.2 Contract fields (M0)

Everything in the post-edit packet §5.1 plus, by this design:

- `DecisionMetricPolicy.sufficiency_rule ∈ {runtime_only, runtime_and_sample}` with preregistered runtime and, when declared, preregistered sample/units (D1). No post-hoc power field.
- Decision-metric shape: `kind = union_composite`, components `TraditionalResultSuccess`, `AIAnswerSuccess`, overlap rule (query-level OR), per-component threshold identity fixed within the Flight and equal across arms; threshold values `PRODUCTION_BINDING_REQUIRED` (S3).
- Arm-parity field group per arm: index generation, serving alias, ACL snapshot, effective pipeline; may be `MISSING`; may be declared `NOT_APPLICABLE` by a versioned applicability rule (D2).
- Legal readiness-combination policy version reference.
- Recomputation contract: shared source-snapshot identity, `independence_class`, transform version, `comparison_rule_id` (D4/D6/F18).
- Estimator registry reference for the named variance estimator; multiplicity control when co-primary (F16).
- CUPED covariate window (must precede exposure) and metric-definition identity binding capping/winsorization/dedup (F19).
- Core material-check set id and version (D7); `authorization_scope` and `evidence_class` (D8, F12).
- `human_state` schema version (F10).
- Preregistered orthogonal-evidence stream declarations for later M1 (F24) — declared before unblinding, not consumed by M0.

### 6.3 Check inventory (`CHK-01..CHK-19`) and the fixed core

Numbering follows the post-edit packet §5.2. The S11 fixed core maps to: CHK-01 (identity), CHK-16 (authorization), CHK-05 (assignment, exposure, arm parity), CHK-03 (formula, components, symmetric thresholds), CHK-07 (population/scope) with grain/window from CHK-08/CHK-09, CHK-12/CHK-09/CHK-17 (source authority, freshness, coverage), CHK-14 and CHK-04/CHK-10 (independent recomputation, registered statistical method), CHK-19 (preregistered sufficiency). Flight-specific checks and `NOT_APPLICABLE` decisions are sealed with version and digest before outcome reads. Extensions by this design:

- **CHK-03 decision-metric registration**: includes the union formula, component instrumentation identity, overlap rule, and equal-across-arms threshold identity (S3, S4).
- **CHK-05 assignment, exposure, and arm parity** (D2).
- **CHK-14 independent recomputation**: PASS requires shared-snapshot identity match, `independence_class ≥ independent_transform`, receipts present, and agreement under `comparison_rule_id`; `same_pipeline` or missing snapshot identity → `UNKNOWN` (D4/D6/F18).
- **CHK-19 preregistered sufficiency**: compares observed runtime, and when the policy declares `runtime_and_sample`, observed sample/units, against preregistered values. Never computes post-hoc power. `runtime_only` is a legal declared rule (D1).
- **CHK-09 completeness/freshness**: material failure → `not_permitted`, never `directional_only` (F14).

### 6.4 Decision logic (deterministic, total, ordered)

```text
1. If any check with materiality = material (stored `unknown` counts as material)
   has an outcome other than PASS or rule-backed NOT_APPLICABLE,
   excluding the single case CHK-19 = FAIL
      -> analysis_use = not_permitted
         next_safe_action by precedence:
           contract_correction > evidence_collection > validity_fix
           > instrumentation_fix > data_quality_fix
         (CHK-19 MISSING/UNKNOWN, e.g. runtime_and_sample declared without inputs,
          lands here with contract_correction)
2. Else, if CHK-19 (preregistered sufficiency) = FAIL
      -> analysis_use = directional_only
         next_safe_action = evidence_collection
         packet.expiry <= preregistered sufficiency completion time (F3)
         reopen_condition names that completion
3. Else -> analysis_use = decision_grade
post_analysis_eligibility := (analysis_use == decision_grade) ? eligible : blocked   [derived]

core_set_status := every fixed-core check outcome in {PASS, FAIL} ? executed : unproven   [S11, D7]
program_capability_status := demonstrated only after core_set_status = executed AND an
                    independent adjudication receipt confirms the blocking/eligibility result [S13]
unblinding_event := the first admitted arm-level primary read receipt of the generation
                    (core set and F24 declarations must carry receipts earlier than it)
```

Materiality: identity/policy, assignment/exposure/arm parity, population/scope, numerator/denominator/join/unit, estimator/CUPED, authoritative source identity, recomputation, freshness, and authorization/isolation failures are always material. Sufficiency insufficiency (CHK-19 FAIL) is material but maps to `directional_only` when nothing else blocks. Unknown or unclassified stays stored as `unknown` with the material ceiling applied (F4). A `non_material` FAIL never blocks and is listed in the packet with its rule id. Triage keys on `analysis_use` and `next_safe_action.kind`, never on eligibility alone.

### 6.5 What M0 emits about components (S4, S5, S7)

M0 recomputes both components as diagnostic derived facts. It records an **observed fact** `component_directions` (each component's sign and the union's sign) and, when the signs disagree, sets `m1_investigation_required = true`. This is an observed fact, not a Cause Claim, not a validity failure (S4), not a guardrail (S5), and not an advisory. M0 emits no advisory.

### 6.6 The five states (kept separate)

| State | Meaning | Evidence | Who can grant |
| --- | --- | --- | --- |
| Fixture readiness | `M0-F1`-`M0-F5` pass hermetically; fixture behavior correct; false readiness NO-GO | `evidence_class = fixture` packets | Owner + independent local reviewer |
| Program `M0 capability demonstrated` (S1, S13) | One real authorized Flight ran end to end on the company laptop; the fixed core executed against real evidence; the blocking/eligibility result was independently adjudicated as correct; packet is reviewer-auditable, whatever `analysis_use` it carries; a correctly blocked Flight qualifies and records Coverage Gap `positive_production_path_unverified` | `evidence_class = production_authorized`, `authorization_scope = laptop_owner_entitlement`, `core_set_status = executed`, adjudication receipt | Owner, on the packet digest plus the independent adjudication receipt |
| Flight eligibility | `analysis_use = decision_grade` for that Flight | the packet | Deterministic evaluator |
| M1 advisory readiness | M1 claims grounded and the S7 evidence floor met, or `insufficient_evidence` | M1 packet + `FlightAdvisory` + DS challenge record | Deterministic policy + named DS Consultant record |
| Committee acceptance | Explicit `pass | change | block` on the packet digest | `human_state.committee_decision` | Experiment Review Committee only |

A correct `not_permitted` packet can demonstrate program capability only if `core_set_status = executed` and the result was independently adjudicated (S11, S13). The review surface renders program capability status and per-Flight `analysis_use` as two distinct fields and never equates the first with gate passage, launch approval, production authorization, or Committee Acceptance (S13).

### 6.7 `human_state` (F10)

`experiment_owner_submission ∈ {draft, submitted}`; `ds_challenge ∈ {pending, agree, disagree, abstain}` with challenge record digest; `committee_decision ∈ {pending, pass, change, block}` (real Flight only; fixture overlap recorded); `acknowledgement` with recipient, digest, expiry. Materiality ruling actor: deterministic rule first, then the preregistered rule owner. No human state changes `analysis_use`.

---

## 7. Evidence authority, provenance, ACL/privacy/redaction, and Coverage Gap behavior

- Production authority: only sources, owners, credentials, tenants, ACLs, retention, redaction, load ceilings, and halt authority named by P2 (or, for the first Flight, by the D8 receipt) are authoritative. Every production field is `PRODUCTION_BINDING_REQUIRED` until then.
- Old SMA: discovery candidate only (O6). Adopted facts carry old source, production validator, validation receipt, drift, adopted revision. Fixtures never derive from it (D5).
- ACL/privacy: raw queries, results, memberships, tenant identifiers, credentials, and secrets never enter model context, Trace, packets, logs, or this repository. Denial reveals no existence, locator, digest, count, or cardinality. Redaction failure emits a typed no-body receipt and blocks only dependent content.
- **Coverage Gap taxonomy (F1).** `freeze:61` is a glossary definition, not a closed enum. The M0 packet contract owns a versioned `coverage_gap_kind` enum: the nine implemented values plus `shared_source_snapshot` (D6). `stale_read` and `conflicting_sources` are admission-time read outcomes; `evidence_state=stale` and `contradicts` apply only to admitted evidence. `DEFAULT_GAP_KIND_BY_OUTCOME` is acceptable as a versioned total classification only when it is part of the frozen contract; where it guesses (FB-27), `kind = UNKNOWN` must be allowed instead.
- **Registries (F11, F16, F24).** Check IDs `CHK-01..CHK-19`; a versioned materiality/applicability rule registry (DS/Committee-authored); a preregistered estimator × metric-form registry; a preregistered orthogonal-evidence stream registry with declared harm direction per stream. Registry owners are named in the contract; contents on the laptop are `PRODUCTION_BINDING_REQUIRED`.

---

## 8. Packet, revision, digest, supersession, and invalidation

- Every revision has a stable logical ID, immutable revision ID, schema version, actor, time, reason, input IDs, content digest, predecessor digest.
- `FlightReadinessPacket` binds: contract revision and digest, manifest of `(revision_id, content_digest)` for every included receipt/check/gap, `analysis_use`, `next_safe_action`, `human_state`, `evidence_class`, `authorization_scope`, core-set status, authorization/redaction manifest, projection manifest, expiry, superseded packet ID, packet digest.
- Supersession: a corrected read after sealing creates a new packet with a new digest; the prior acknowledgement is invalid; history is not edited (`VAL-SUP-001`).
- Insufficient (`directional_only`) packet: `expiry <= preregistered sufficiency completion`; the reopen condition names it; reaching it requires a new read and superseding packet (F3; applied in candidate §5.4).
- Dependency invalidation follows reverse `depends_on` edges and recomputes only the affected closure; renderer-only invalidation never changes evidence or readiness.
- The freeze binds the alignment packet, `final-architecture-spec.md`, `implementation-sequencing.md`, `eval-acceptance-plan.md`, and CE plan digests (F8), and carries an open-decision register with blocked-behavior mapping (FB-11).

---

## 9. Trace versus Evidence

- Trace = allowlisted stage/tool order, request/result metadata, retries, errors, worker/model identity, tokens, cost, latency, approved artifact digests.
- Stored separately, cross-linked (`trace_event --cross_links_to--> source_read | stage | failure`), rendered under the same authorization, a separately versioned non-digested annex to the packet.
- Trace never `supports`, `contradicts`, or `explains`; a HumanRuling cannot cite it.
- Trace is optional. Missing optional Trace is a visible Coverage Gap, not negative evidence and not a global blocker. Only a Trace-dependent operational assertion or diagnostic view is blocked when its capture receipt or pin is missing. The Trace-dependent assertion set is preregistered per generation and cannot be narrowed after the fact (M20).
- Collectors run only inside Data Agent-owned enterprise-managed runtimes for authorized generations; no personal IDE or endpoint collection (M19). On the company laptop, Trace stays on the laptop.

---

## 10. Candidate-diff safety and delivery boundary

- Only an invalid Flight may receive an `InvalidExperimentRemediation` (O3). First path: typed guidance and a reopen condition.
- A diff is attached only after exact-target, authority, validator, capability-isolation, and human-only delivery gates pass. It is syntactically valid, independently reviewable, marked `not_applied`, bound to deployed revision not default-branch HEAD, contains no secret, and becomes invalid when its target, context, policy, or dependency changes.
- Delivery: only through an authorized human review surface with recipient/channel enforcement. The Agent exposes no apply, commit, PR, deploy, rollback, webhook, queue, polling, or automation-consumable action feed. Safety comes from capability isolation, not from corrupting the diff.
- **`candidate_diff_eligibility` (S14).** No advisory implies a diff. A diff of any kind (M0 remediation or later M1 change) requires exact deployed artifact identity and SHA; file/symbol attribution (line when reliable); runtime and scope reachability; a supported causal mechanism; material-alternative and counterevidence challenge; independent code-domain review; LOW or MEDIUM action risk. M2 corroboration is mandatory when the change touches relevance, ranking, AI-answer behavior, presentation, or another user-visible search semantic; a versioned applicability rule may mark it `NOT_APPLICABLE` for deterministic instrumentation, assignment, configuration, flag, ACL, or pipeline-wiring corrections whose evidence does not depend on query-level user-value interpretation.
- The same delivery boundary applies to `FlightAdvisory`: no automation-consumable advisory feed; the advisory reaches humans only, beside the official metric result (S6, F21).

---

## 11. M1 advisory contract (planned; S6-S8)

- **Entry (S9).** Once the M0 packet is sealed the case may enter M1 whatever `analysis_use` it carries. Publication authority is evaluated per M1 claim against its evidence dependencies: a `not_permitted` (invalid) Flight supports validity, instrumentation, data-quality, and remediation analysis but no treatment-causal or production-change claim that depends on the invalid comparison; a `directional_only` Flight supports explicitly directional component and orthogonal-outcome analysis; a local Coverage Gap blocks only dependent claims. Every M0 blocker stays visible and cannot be waived by entering M1.
- **Trigger for the metric-challenge advisory.** `m1_investigation_required = true` from M0 (component divergence) or an M1 case opened for a `decision_grade` Flight.
- **Scoped invalid-Flight block advisory (S10).** When M0 is `not_permitted` because the experiment is invalid, M1 emits `recommend_block` with `target = use_of_this_flight_as_decision_evidence`, `basis = invalid_experiment`, scope bound to the exact Flight generation, and validity remediation or rerun as next safe action. It advises the Committee not to rely on that Flight for the launch decision; it never blocks launch, authorizes rollback, or requests mutation, and it needs no orthogonal user-outcome stream because it does not challenge the metric's user-value semantics.
- **Inputs.** M1 claims (mechanism, substitution, mix shift, user-value semantics) with Gate 0-7 receipts; the official `Query Success` result; the component observed facts; preregistered orthogonal outcome-evidence streams (F24) read under authority.
- **Floor (S7).** `recommend_change` or `recommend_block` requires at least one valid, scope-matched, orthogonal outcome-evidence stream that (a) is in the preregistered registry, (b) was declared for this Flight with a receipt earlier than the unblinding event (§6.4), (c) is not mechanically derived from the union events, and (d) shows the harm direction it was preregistered to detect. *Scope-matched* means the same population, window, arms, and grain as the union read, or a coarser scope named in the declaration. Otherwise `insufficient_evidence`. Component divergence alone → `insufficient_evidence` plus mandatory investigation record.
- **Post-unblinding evidence (S12).** A stream discovered after unblinding may trigger mandatory urgent investigation but cannot by itself carry `recommend_change`/`recommend_block`. It needs at least one independent confirmation first: a blind or preregistered reproduction; reproduction through an independently versioned data or transform path; or a named independent DS/Committee reviewer challenge confirmation with evidence citations. Until then the advisory is `insufficient_evidence` with next safe action `urgent_investigation`, and the discovered signal, selection timing, tested-analysis inventory, counterevidence, and falsifier are preserved in the Evidence record.
- **Independence and accountability (F21).** The advisory carries evidence IDs, counterevidence, an explicit falsifier ("this advisory is wrong if …"), and the Independent DS Consultant's challenge record (`agree | disagree | abstain`, digest) before it reaches the Committee. It never renders without the official metric result beside it.
- **M2 optional (S8).** M2 query/result examples may strengthen or falsify the advisory. Their absence is a visible query-level Coverage Gap on the advisory, not a blocker.
- **Orthogonality (F23, S14).** `FlightAdvisory` is its own dimension: it is legal beside Cause Verdict `suspected` when the S7 floor is met; it is not a Recommendation item, never authorizes action, and never implies a candidate diff.

---

## 12. Fixture, evaluation, and calibration contract

- Local M0 uses de-identified hermetic fixtures only (`evidence_class = fixture`). Cases: trusted, insufficient directional, invalid, materially unknown, conflicting, stale, partial, unauthorized, superseded, reviewer-conflict, arm-parity divergent (D2), `same_pipeline` recompute (D4), union with component divergence (S4), threshold-parity mismatch across arms (S3).
- Fixtures are synthesized from scratch (D5); per-arm decomposition is required (FB-14). Each fixture receipt records author, evaluator/reviewer, and independence or disclosed conflict; a conflict never expires by seniority or timeout.
- Threshold-free structure (F13): per-check planted-failure fixture + near-miss clean twin; always-ready, always-blocked, and runtime-only trivial baselines each contradicted per twin before Agent scoring; decoys for metric-definition version, CUPED mode, source identity, arm parity, pp-vs-relative swap, timezone off-by-one, exposure-trigger mismatch, stale snapshot with fresh `recorded_at`, scorecard rounding, dedup difference, `same_pipeline` recompute.
- No numeric GO. Blind gold, pilot ranking policy, calibration, and numeric thresholds are P4. Fixture authorization is not production ACL evidence.

---

## 13. Failure, recovery, stop, and continuity

- Stop conditions: packet §12 items 1-13. Cap/expiry exceeded halts unconditionally; "green command + partial packet" is the halt-state requirement, not an exemption (F15). Local halt owner is the M0 lead named in the start receipt (1-6); 7-13 route to the contract's authority. A halt preserves receipts, emits the Coverage Gap, and never widens scope to go green.
- Budget: every start receipt binds an active-time cap, run/read/tool cap, expiry, and halt owner. The `m0-codex-continuation-20260817` cap is exhausted; `M0-F1`-`M0-F5` need a new receipt.
- Recovery: bounded, failure-typed retries; transport retries the same read; query repair repairs only the query; no scope widening. On the laptop, an interrupted production read closes as `unknown`; it is never blindly retried against a live source without a new receipt.
- Continuity Checkpoint before 2026-08-24 (O5): clean-checkout branch and immutable revision, locked prerequisites, one hermetic command, fixture manifest with no secrets, unit/scenario ledger, receipts and gaps, next bounded task, fresh-context rehearsal, half-day return runbook, start-here index that marks superseded files (FB-16). **Hazard:** `docs/research/` and `.agents/skills/kdd_data_agent/` are untracked; the checkpoint cannot exist until they are committed on the working branch (Owner action; this job may not commit). Harness `.omc/state` files inside the package must be removed before any aggregate digest is re-receipted.

---

## 14. M0-to-M2 sequencing and gates

| Slice | Outcome | Gate to start | Gate to exit |
| --- | --- | --- | --- |
| V0 | Continuity-ready foundation | done (Phase A) | checkpoint rehearsal; committed revision |
| V1 (`M0-F1`-`M0-F5`) | Fixture-backed M0 (`evidence_class = fixture`) | frozen packet digest + new Owner start receipt | all `VAL-M0/PRE/CUP/UNIT/SRC/SUP/CONF/REM/BASE/DECOY/SEC/UI-001` pass; false readiness NO-GO |
| V1p (new) | Program `M0 capability demonstrated` (S1, S13) | V1 + D8 laptop-scoped receipt + sealed fixed core and Flight-specific applicability (S11) | one real Flight packet, `core_set_status = executed`, independent adjudication receipt, reviewer-auditable, exported per F22; `positive_production_path_unverified` recorded when the Flight is blocked |
| V2 | One P2 production path | P2 closed for one source | write-denial, scope, mapping, freshness, halt receipts |
| V3 | M1 incl. advisory | sealed M0 packet (any `analysis_use`, claim-scoped gating per S9) + V2 + start receipt | ranked falsifiable claims capped by M0 dependencies; advisory with floor, scoped invalid-Flight block, or `insufficient_evidence` |
| V4 | M2 | review-ready M1 + replay/ACL/comparability authority | win/loss/unclear/not_comparable with receipts |
| V5 | Review-ready handoff | V1-V4 | Committee acceptance remains external |

`VAL-*` to unit binding (F7): `VAL-FLT-001, VAL-MET-001/002` -> `M0-F1`; `VAL-M0-001/002, VAL-PRE-001, VAL-CUP-001, VAL-UNIT-001, VAL-SRC-001` -> `M0-F3`; `VAL-SUP-001, VAL-CONF-001, VAL-REM-001/002, VAL-APR-001, VAL-UI-001` -> `M0-F4`; `VAL-SEC-001, VAL-BASE-001, VAL-DECOY-001, VAL-CON-001` -> `M0-F5`; new `VAL-DET-001` (digest determinism), `VAL-PROD-001` (S1 production-backed packet with `core_set_status = executed`), `VAL-ADV-001` (advisory floor unmet → `insufficient_evidence`) proposed; `VAL-UI-101` -> P3; `VAL-M1-*, VAL-M2-*, VAL-ROL-001, VAL-OLD-001` -> V3-V5.

---

## 15. KDD / DeepSeek Adopt-Adapt-Reject (mechanism level)

| Mechanism | Disposition | Use here |
| --- | --- | --- |
| Bounded stages with code-owned control (Champion, Fourth) | Adopt principle | Two M0 stages; deterministic evaluator owns the decision |
| Narrow tool allowlists and phase timeouts (Fourth) | Adopt/Adapt | Capability Broker; static allowlist scan; per-receipt caps |
| Artifact workspace and experiment lineage (Fourth) | Adapt | Append-only workspace with predecessor digests |
| Deterministic replay (DeepSeek Harness requirement) | Adopt requirement, not implementation | Byte-identical replay across processes/seeds; avoid compaction-shadowing |
| Evidence receipts / exact SQL receipt (Team 1401) | Adapt | SourceRead receipts as the only path to evidence |
| Visible trace / trace viewer (Fourth, Codex Trajectory) | Adapt as separate Trace | Separate, non-digested, cross-linked store; never evidence |
| Recovery: close as `unknown`, never blind retry (Harness) | Adopt vocabulary; mechanize in Phase B | Failure-typed bounded retries |
| Independent review / judge (Harness required-test list) | Adapt | Fixture-author/evaluator independence receipts; independent local reviewer; DS challenge record |
| Self-consistency voting, consensus as verdict (Champion, Fourth) | Reject | Votes are not evidence |
| Forced terminal submit, fail-open checks, arbitrary code (Fourth) | Reject | Budget exhaustion yields a partial packet, never a forced answer |
| Heuristic joins, Event Log as evidence graph, uploaded-files-only substrate (Team 1401) | Reject | Not verified lineage |
| Fail-open human timer, narration as evidence (Team 1286) | Reject | Timeout is not approval |
| Monotonic deny in a non-replaceable boundary (Harness) | Adopted structurally | No plugin tree, no dynamic import |
| DuckDB read-only backend (old KDD local) | Reference only | Stronger than its own audit says; not imported |

Caveats from the local audits: the KDD trace subsystem is dead code in the pinned repo and must not be presented as a working donor; `latency_governor` bounds differ from claims (FB-38 confirms principle-level transfer with no cargo-cult artifacts).

---

## 16. Alternatives rejected and why

| Alternative | Rejected because |
| --- | --- |
| M0 = validity only; runtime is the sole `directional_only` trigger | A full-runtime, under-enrolled Flight would become `decision_grade` (Owner Q1) |
| Mandatory preregistered MDE/power for every Flight | Stricter than most platforms can supply (Owner Q1) |
| Arm parity deferred to M1 | M0 would tell the Committee "the read is trusted" while the arms were not comparable (Owner Q2) |
| Store both readiness fields and reject illegal pairs | Redundant field that must always agree (Owner Q3); note the post-edit candidate encodes this and must be revised |
| Leave recomputation independence to P2/implementation | Two competent implementers would diverge (Owner Q4) |
| Derive M0 fixtures from old SMA assets with provenance | Owner rejected any derivation (Owner Q5) |
| Core check set = all always-material checks | DoD would be hostage to data-source availability on the first Flight (Owner Q6) |
| Core check set chosen on the laptop | Floor could be chosen empty (Owner Q6) |
| First real Flight requires full P2 closure | DoD would wait for every third-party owner (Owner Q7) |
| Laptop receipt with security/privacy signature | Adds an external signature dependency the Owner did not want (Owner Q7) |
| A third readiness enum value | Prior review (C2) showed the separated design prevents promotion of a directional read |
| Trace inside the packet digest | Trace schema is unfrozen and deletable |
| Port a KDD or Harness runtime first | Spends the M0 budget on a port while semantics are unfrozen |
| Advisory allowed on component divergence alone | Would let the Agent overrule the official metric on re-cuts of the same events (S7) |
| Advisory waits for M2 | Delays a well-grounded advisory behind query-level evidence that may not be authorized (S8) |
| M1 forbidden until M0 is `decision_grade` | Would hide validity/instrumentation analysis and the scoped block advisory an invalid Flight needs (S9, S10) |
| Post-unblinding streams banned outright | Would make unexpected harm invisible; S12 admits them after independent confirmation |
| One `M0 complete` boolean | Conflates program capability with Flight decision-grade status (S13) |
| Advisory implies a diff / M2 always mandatory for a diff | S14 separates the diff gate and makes M2 corroboration conditional on change semantics |

---

## 17. Unresolved decisions and production bindings (named owners, falsifiers)

| Decision / binding | Owner | Falsifier / closure evidence |
| --- | --- | --- |
| P2: authoritative sources, owners, credentials, tenants, ACL, retention, redaction, load, halt (for V2 and beyond) | Production owner, Eng, security/privacy | Signed intake; write-denial receipt for the one source |
| D8 laptop-scoped receipt for the first Flight | Owner (security/privacy informed) | The receipt exists with all D8 fields; `authorization_scope` on the packet |
| Per-arm index generation / ACL snapshot as evidence sources (D2) | Eng / search platform | Named source; else CHK-05 parity part stays `MISSING` |
| `Query Success` thresholds, timer bindings, event schemas, table/catalog identities (S3) | `PRODUCTION_BINDING_REQUIRED` on the laptop | Contract fields filled from production registry with owner |
| Orthogonal-evidence stream registry contents (F24) | DS Consultant + Owner, before the first M1 | Registry version and per-Flight declaration receipt |
| Materiality/applicability rule registry contents (F11) | DS/Committee | Registry version |
| Estimator × metric-form registry (F16) | DS/P4 | Registry reference in the policy |
| Semantic revalidation owner when a source/definition migrates (`profile` item 3) | Owner + production owner | Named owner |
| P3: packet-centered first screen and interactions | Owner + named reviewers | Live-review receipt (`VAL-UI-101`) |
| P4: sealed gold, blind cases, calibration, numeric thresholds | Evaluation Owner | Adjudication and pilot receipts |
| New Owner start receipt for `M0-F1`-`M0-F5` | Owner | Receipt binding packet path, revision, sha256, caps, expiry, halt owner |
| Committee acceptance for a real Flight | Experiment Review Committee | Explicit ruling on packet digest |
| `profile:446-455` items 1, 5-9 | Owner + domain authorities | Explicit decisions |
| Adjudications M18 (screenshot digests), B3 inventory page | Owner / Codex | Reclassified digests; one-page inventory (trivial under D5) |
| Continuity Checkpoint commit authorization | Owner | Committed revision on the working branch |

---

## 18. Migration and toolchain (separated from target architecture)

- Python, Pytest, canonical-JSON digest, and `.agents/skills/kdd_data_agent/` are provisional M0-F0 choices. Keep/replace triggers: `TOOLCHAIN_RECEIPT.md` §3 items 1-4 plus FB-29 (target host lacks a supported interpreter) and FB-05 (security review requires a runtime sandbox the stdlib cannot provide). None fires today; the company laptop's interpreter version is `PRODUCTION_BINDING_REQUIRED`.
- No schema library, database, UI framework, model vendor, or agent framework is frozen.
- Phase A engineering debts before `M0-F1` exit: three unproven guards (671d8db1 MAJOR-5), scanner escapes and receipt wording (FB-05), seam `packet_reference` update (MAJOR-1/FB-06), docstring IDs (MAJOR-3), `rule_source` strip check (L1), decode-side reserved key (L4), float/surrogate/timestamp canonicalization (L5/L6/FB-28), gap-kind guessing (FB-27), remove `.omc/state` and caches from the package (FB-31/FB-40).

---

## 19. Blind-spot pass and pre-mortem (steelman attacks)

| Attack | Strongest case it lands | Strongest case it fails | Decision-changing variable | Disposition |
| --- | --- | --- | --- | --- |
| A correctly blocked packet is presented as production validation or Flight eligibility | A `not_permitted` packet full of Coverage Gaps looks "complete" on the first screen | Five separate states (§6.6); `evidence_class`, `authorization_scope`, `core_set_status` rendered on the first screen; eligibility is a projection of `analysis_use` | whether the projection shows the three labels before anything else | Closed by S1 + D7 + F12; P3 must verify reviewers read them (`VAL-PROD-001`) |
| Core checks chosen post hoc to manufacture completion | On the laptop, unavailable sources tempt a smaller core | Fixed core (S11) plus Flight-specific applicability sealed with version and digest before outcome reads; nothing removed afterwards; `MISSING` on core → unproven; capability needs independent adjudication (S13) | whether the receipt is sealed before the first read | Closed by S11 + S13 (Owner); falsifier: any core-set edit after the read invalidates `core_set_status` |
| One orthogonal stream lets the Agent cherry-pick harm | Seven candidate stream families; pick the one that agrees | Preregistered registry preferred (F24); post-unblinding streams need independent confirmation before change/block (S12); falsifier stated on every advisory; tested-analysis inventory preserved | whether the confirmation step is independent of the discoverer | Closed by S12 (Owner) + F24; falsifier: an advisory citing a post-unblinding stream without a confirmation receipt |
| M1 advisory becomes unaccountable product policy | The Agent overrules an improving official metric | Advisory is non-binding, evidence-bound, carries a falsifier and the DS challenge record, never renders alone, never authorizes action; the Committee rules | whether the DS challenge record is mandatory before Committee handoff | Closed by F21/F23; residual: Committee habit of deferring to the Agent is a P3/organizational risk, not a contract defect |
| Making M2 optional undermines falsification or Committee usability | Without query examples the advisory is abstract | Advisory carries falsifiers M2 can test; query-level absence is a visible Coverage Gap; S8 is an Owner decision | whether the falsifier is concrete enough for M2 to execute | Closed by S8 + F21; residual gate: M2 replay authority |
| Company-laptop-only boundary breaks handoff, replay, retention | Nothing durable leaves the laptop; another builder cannot reproduce | Export contract (F22): packet + receipts + redaction manifest with digests; laptop-side replay receipt; materialized snapshot receipt (F25); retention period in the D8 receipt | whether the export manifest is enough for a Committee reviewer without laptop access | Partly closed; residual: retention period and export redaction policy are `PRODUCTION_BINDING_REQUIRED` |
| `independent_transform` is claimed but the transform is a copy of the reporting pipeline | The Agent cannot always see the reporting transform code | The recomputation receipt carries the transform digest and Data-Agent ownership; the DS Consultant's challenge record reviews the independence claim; a matching digest with the reporting transform is a FAIL | whether the reporting transform digest is obtainable on the laptop | Residual: independence is attested and reviewed, not proven; recorded as a Coverage Gap `independence_attested_only` when the reporting digest is unavailable |
| Source has no immutable snapshot, so D6 "same snapshot" is unsatisfiable | Live tables change under the read | The Agent materializes its own immutable snapshot receipt of the primary read (F25); recomputation runs on that materialization | whether the primary read can be materialized within the D8 retention rules | Closed by F25; residual: retention |
| Threshold parity across arms silently broken by treatment UI change | Dwell thresholds mean something different when the UI changes | CHK-03 checks threshold identity equality; semantic shift is M1 (S4) | none | Closed by S3/S4 |
| Two Opus reviews clobbering the same output path; "zero blockers" handoff | Codex freezes on an incomplete finding set | Disposition document caught it; this job recovered the overwritten review; freeze requires exact-digest review of the post-edit bytes | none | Process hazard, recorded; no design change |
| Untracked planning tree and package lost before the checkpoint | Machine loss erases months of work | Only a commit fixes it; this job may not commit | Owner commit authorization | Open hazard |

---

## 20. Acceptance evidence and traceability

### 20.1 Owner decisions -> sections

| Decision | Sections |
| --- | --- |
| O1 Flight identity | 3.1, 6.2 |
| O2 metric set + policy | 3.1, 6.2, 6.3 |
| O3 remediation | 3.1, 10 |
| O4 roles | 2, 6.6, 6.7 |
| O5 slice, leave, continuity | 13, 14 |
| O6 old SMA | 3.2 (12), 7 |
| P1 orthogonal states | 3.1, 3.2, 11 |
| D1 preregistered sufficiency | 3.1, 6.2, 6.3, 6.4, 16 |
| D2 arm parity in M0 | 3.1, 6.2, 6.3, 12, 17 |
| D3 single stored state + projection | 3.1, 5, 6.4, 16 |
| D4/D6 independence class, shared snapshot | 3.1, 5, 6.2, 6.3, 7, 19 |
| D5 no fixture derivation | 3.2, 12, 16 |
| D7 core set floor | 3.1, 6.1, 6.4, 6.6, 19 |
| D8 laptop-scoped receipt | 1.2, 3.1, 4, 6.6, 14, 17 |
| S1 production-backed DoD | 0, 2, 6.6, 14 |
| S2 environment boundary | 4, 7, 17 |
| S3 decision-metric shape | 3.1, 6.2, 6.3, 12 |
| S4 M0/M1 boundary | 6.5, 11 |
| S5 no component guardrails | 3.2, 6.5 |
| S6 non-binding advisory | 2, 3.1, 10, 11 |
| S7 evidence floor | 3.2, 11, 19 |
| S8 M1 without M2 | 11, 19 |

### 20.2 Accepted review findings -> disposition

Full table in the decision ledger §C.2 and §C.3. Summary: 671d8db1 BLOCKER-1/2/3 → post-edit candidate + D1/D2; MAJOR-1..7 → engineering (Phase B) or rulings F1/F5/F7; b9d777ba MAJOR-1..4, MINOR-1..4 → D3, F3, F4, F8 and candidate edits (applied); Fable FB-01..FB-41 → D1-D5, D7, F1, F10-F19, engineering; multiagent L1-L7 → engineering and F1.

### 20.3 Acceptance evidence for this design

- Owner confirmations D1-D8 and S1-S8 recorded with source and date in the ledger.
- Reviewer findings imported with classification and disposition.
- Every architecture section maps to at least one Owner decision, closed contract, facilitator ruling awaiting confirmation, or explicit `OPEN GATE`/`PRODUCTION_BINDING_REQUIRED`.

---

## 21. Gate state and final-state ceiling

This job ends at `DRAFT` under the Owner's budget closeout. Outstanding before any `FROZEN` claim: (1) Fable adversarial final review and status (job `4bda4e93`, Phase I sealed, final pending with the steelman delta); (2) third independent Phase A reviewer (Q11/Q12) — handoff only; (3) exact-digest review of the post-edit packet `67c844d1…` and spec `3b20c938…`, and of any Codex reconciliation candidate that supersedes them; (4) revision of the candidate for D3 (single stored state), D1 semantics of CHK-19, D4/D6 fields, D7/D8, S1-S14; (5) Owner confirmation of the F-rulings and of the design as a whole (the steelman closure is not design approval); (6) Phase 2 canonical writeback, which this job does not perform. Codex owns the next sequence per S-close.

---

## 22. ADR proposals (strict criteria: hard to reverse, surprising, real tradeoff)

1. **ADR-0009 — M0 readiness is validity plus preregistered sufficiency, stored as one state.** (D1 + D3.)
2. **ADR-0010 — Per-arm serving parity is an M0 setup-integrity check.** (D2.)
3. **ADR-0011 — The Agent may issue a non-binding advisory that challenges an improving official metric only on preregistered orthogonal outcome evidence.** (S6 + S7 are Owner decisions; the preregistration requirement is facilitator ruling F24 and needs Owner confirmation before this ADR is written.) Hard to reverse (Committee workflow), surprising (Agent may say block when the metric improved), real tradeoff (usefulness vs cherry-picking).
4. **ADR-0012 — Program `M0 capability demonstrated` requires one real Flight under a laptop-scoped receipt with independent adjudication, not fixtures and not full P2, and is separate from per-Flight decision-grade status.** (S1 + S13 + D8.) Hard to reverse (schedule and authority model), surprising, real tradeoff (speed vs formal approval).
5. **ADR-0013 (candidate) — M0 blocking constrains M1 claims per evidence dependency and yields a scoped, non-binding block advisory; it does not forbid M1 investigation.** (S9 + S10.) Surprising to readers who expect a hard M0→M1 gate; real tradeoff between usefulness on invalid Flights and the risk of laundering causal claims through them.
6. Optional: fold D5 (no fixture derivation from old SMA) into ADR-0008 as an amendment rather than a new ADR. S14 (candidate-diff gate) extends ADR-0005 and should be an amendment to it, not a new ADR.

D4/D6 (independence class), D7 (core set), and the F rulings are contract definitions recorded in the design and glossary, not ADRs.

---

## Appendix A — Owner decision ledger

See `architecture-decision-ledger.md` (D1-D8, S1-S14, S-close, F1-F25, sources, dates). Custody: Codex preserved the v2 drafts at the digests in `fable5-architecture-custody-receipt.md`; this v3 revision supersedes them with new digests recorded in `architecture-finalization-status.json`.

## Appendix B — Reviews reconciled

- Opus 5 job `671d8db1` (complete): `ACCEPT_WITH_CHANGES` on `40c7234f…`, 3 blockers, 7 majors, Phase A `PASS_WITH_GAPS`.
- Main session `b9d777ba` (overwritten on disk; recovered from transcript): `ACCEPT_WITH_CHANGES` on Q1-Q10/Q13, COI on Q11/Q12; its eight edits applied by the orchestrator → post-edit candidate `67c844d1…`.
- Fable 5 job `4bda4e93`: Phase I sealed (`BLOCKED` because the packet changed mid-review; provisional design verdict `ACCEPT_WITH_CHANGES`); final review pending with steelman delta.
- Codex disposition `m0-freeze-codex-disposition.md`: `POST_REVIEW_CANDIDATE_NOT_FROZEN`.
- Third Phase A reviewer: handoff only.

## Appendix C — Research evidence packet

The Sonnet extraction lane never returned a report and the Opus architecture-challenge lane failed on the Claude session limit (2026-08-18 07:35Z). Per the two-strike rule, the facilitator performed the architecture challenge, the diagram taste gate, and the mechanical checks personally; those passes are labeled **self-verification** in the status file. The Adopt/Adapt/Reject table in §15 relies on `final-architecture-spec.md` §20, `TOOLCHAIN_RECEIPT.md`, and Fable FB-38, all read directly by the facilitator.
