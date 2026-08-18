# Greenfield Data Agent Requirements

> [!WARNING]
> **Historical research draft. Non-canonical.** This document preserves an earlier requirements-first research snapshot. It has been superseded by the owner-confirmed [`planning-decision-packet.md`](planning-decision-packet.md), the closed [`freeze-canonical-domain-policy-contracts.md`](wayfinder/freeze-canonical-domain-policy-contracts.md) resolution, and the [`final-architecture-spec.md`](final-architecture-spec.md). It must not guide implementation or override later decisions. In particular, its `actionable`, `investigate`, `likely`, `insufficient_evidence`, and Gate 0–3 language is historical and non-canonical. The current contract uses independent Cause Verdict (`unassessed | suspected | confirmed | ruled_out | inconclusive`) and Recommendation Readiness (`not_applicable | blocked | proposal_ready | action_ready | rejected`) axes plus canonical G0–G7 receipts. No state authorizes mutation. Production authority, calibrated evaluation, and live review-surface acceptance remain open gates.

Date: 2026-08-11
Status: Historical research draft / non-canonical. Defines requirements, evidence, and acceptance conditions only. It does not select a final architecture.

## 1. Goal and boundaries

Redesign the data agent from two real scenarios.

- **A — Post-experiment**: A metric misses expectations. Explain why. Tie the explanation to production code. State what should change.
- **B — SEV**: A metric drops. Find potentially related production code, config, flag, model, or data changes. Support incident review.

The needs and success criteria of these two scenarios are the only sources of the target design. KDD-winning systems, the workshop, and old SMA code or architecture are candidate references only. A practice can enter the requirements only after an `Adopt / Adapt / Reject` assessment. These references impose no compatibility, module, data, framework, or migration constraints.

The goal is not to clone a KDD agent, preserve the old framework, or patch old code. The final design must follow from the evidence and decision needs of scenarios A and B.

Default authority is read-only. This document does not authorize changes to production data, code, experiment configuration, feature flags, deployments, or incident state.

## 2. Evidence boundaries

### 2.1 Workshop

The original attachments have been located and copied to stable locations. The workshop evidence package contains two recordings:

- `workshop`: `Workshop main recording` (raw media not included because of size, privacy, and source availability); `7997.098667s`, about `2:13:17`; SHA-256 `24b5fd98fb9dc426039ea3eac3cc18ce8ba9dbe7074db4ba0e3b6c8ac7718929`.
- `intro`: `Workshop intro recording` (raw media not included because of size, privacy, and source availability); `348.330667s`, about `5:48`; SHA-256 `2adf77325cec0f5a78ccc784794c2744bdb7f1a0ff34aff2e36696075332a9a2`.

Their combined duration is `8345.429334s`, about `2:19:05`. The raw local Whisper transcript and a faithful timestamped timeline have been completed. Current coverage is recorded in `meeting-audio-alignment.md`: `workshop 7997.098667 / 7997.098667s`, `intro 348.330667 / 348.330667s`, and aggregate `8345.429334 / 8345.429334s`, all **100%**.

Processing contract:

- **Both recordings form the evidence package.** `workshop` and `intro` must each reach 100% transcription, segmentation, and summary coverage. The total-coverage denominator must not include only the `2h13m` workshop recording.
- **Screenshots cover only part of the workshop slides.** The 73 screenshots are not a complete deck and do not represent complete topic coverage. There is no evidence of screenshots corresponding to `intro`, so none may be implied.
- **Audio-only segments must be preserved.** Segments without matching screenshots must not be deleted, downgraded as irrelevant, or excluded from speaker-practice extraction.
- **Cross-aligned segments are priority verification zones.** When audio and screenshots align, use the screenshots to verify terms, numbers, process, speaker, and topic.
- **Screenshots may correct ASR only.** A screenshot-supported correction must preserve the original audio time range and the reason for the correction. Slide content that was not spoken must not be inserted into the transcript.
- **A missing screenshot is not negative evidence.** It cannot support a claim that a speaker did not say something or that a slide did not exist.
- **Write `cannot confirm` when audio or visuals are unclear.** Do not fill speaker wording from secondary summaries.

Workshop delivery must report these separately:

1. `audio_coverage`: report processed duration / `7997.098667s` for `workshop`, processed duration / `348.330667s` for `intro`, and aggregate processed duration / `8345.429334s`. List every untranscribed interval and its cause. Both recordings must reach 100%.
2. `screenshot_coverage`: for `workshop` only, report screenshots reviewed / `73`, including unreadable, duplicate, or unknown-time items. Do not invent screenshot coverage for `intro`.
3. `cross_aligned_coverage`: report only intervals and screenshots successfully aligned to `workshop` audio. This measures cross-verification; it does not invalidate the remaining workshop audio or any intro audio.

Each speaker-practice record must contain at least: audio file (`workshop` or `intro`), speaker (`cannot confirm` if unresolved), audio start and end time, verbatim or approximate-transcript label, topic, explicit claim, context, corresponding screenshot ID (workshop only, if available), ASR correction (if any), and evidence state.

Complete transcript coverage has reached 100%. `meeting-audio-alignment.md` records faithful summaries, speaker/topic, screenshot corrections, inference boundaries, and confidence by audio file and timestamp. All 73 screenshots have wall-clock mappings and topic-level cross-alignment. This is not verbatim speech verification and does not imply a complete deck. Speaker-derived practices may now enter `Adopt / Adapt / Reject` assessment, but their strength still depends on confidence for the corresponding interval. Low-confidence segments, names, distant-room questions, and repeated ASR segments must continue to say `cannot confirm`. Screenshot alignment raises confidence in terminology and topics for the matching interval only; it does not reduce the validity of audio-only workshop segments or intro segments.

### 2.2 KDD primary evidence

- Fixed source clone of the public champion repository: commit `bdc874fc4260e3565ae0dce041728fdf5b376709`. Local research notes contain exact source anchors. [Evidence: `docs/research/kdd-data-agent-workshop/kdd-source-practices.md`]
- Local `KDD_Competition`: commit `7270e3bcc24a039ac458e45caeab7a283c62eca8`. Used for success, failure, and NO-GO evidence. It is not the champion repository.
- Independent source audit: `primary-source-audit.md`. It directly verifies that the existing references lack complete production change discovery, and it supports requirements for a typed change inventory, runtime identity, and metric-segment-to-symbol mapping. [Evidence: `primary-source-audit.md:218-242`]
- The champion placement appears only in the public repository's own description. This research did not independently verify the official leaderboard.

Two Creative Track primary-source packages have been assessed:

- Team 1286: complete video and paper research. Output: `creative-team1286-practices.md`. Paper coverage is `23/23` pages; video audio and visuals are fully covered from `00:00–07:58.04`. [Evidence: `creative-team1286-practices.md:18-31`]
- Team 1401: complete video-only research. Output: `creative-team1401-practices.md`. Video duration is `08:32.48`; `audio_coverage` is `08:32.14 / 08:32.48`, with about `0.34s` of trailing material and no discernible speech; `visual_coverage` is 102 frames sampled every five seconds plus 12 key frames. [Evidence: `creative-team1401-practices.md:18-31`]

These packages provide candidate practices only. They are not sources of requirements. Only practices that pass the A/B needs test are included in Section 7. Team 1286 lacks production telemetry, experiment validity, a typed change timeline, exact deployed SHA, and a rollback evidence plane. [Evidence: `creative-team1286-practices.md:8-16,177-195`] Team 1401 lacks a production repository, deployed SHA, change timeline, experiment validity, SEV changepoint, and counterfactual. [Evidence: `creative-team1401-practices.md:8-16,278-310`] Neither package supports production attribution requirements. The absence of a Team 1401 paper is not negative evidence and does not permit speculative reconstruction of design details.

### 2.3 Evidence strength

- **Strong**: directly implemented in source, or reproducible with a frozen fixture.
- **Medium**: README, run ledger, or review receipt. Proves only the conclusion recorded at that time.
- **Weak**: design draft, estimate, or unrerun claim.
- **Unknown**: original material is missing or cannot be interpreted.

Every output must distinguish `observed`, `inferred`, and `unknown`. Temporal correlation is not causation.

## 3. Scenario A: Post-experiment

### 3.1 User need

The experiment owner needs to know:

1. Whether the result is interpretable and whether the experiment first passes validity checks.
2. Which metric component, segment, or system path explains the miss.
3. Which production behavior is consistent with the change mechanism.
4. Which deployed code, config, or model change deserves inspection.
5. What should change, including expected impact, risk, validation, and rollback.

### 3.2 Required inputs

- Experiment identity, hypothesis, owner, and decision deadline.
- Treatment/control, exposure unit, allocation, ramp history, and analysis window.
- Primary metric, guardrails, metric-definition version, expected effect, and variance assumptions.
- SRM, sample size, missingness, and logging/schema changes.
- Metric rows and decomposable dimensions.
- Production topology, telemetry, and deploy/flag/config/model timeline.
- Exact `owner/repo`, deployed SHA, diff, and code ownership.
- Typed production change inventory. It must cover `code | config | flag | model | data`; searching only Git commits is insufficient.
- Runtime identity receipt. It must prove the service build, commit, config, flag state, model version, and data/schema version actually running in the affected environment.
- Versioned metric-segment -> runtime path -> repo/file/symbol mapping, with owner and source.

When a critical input is missing, return `insufficient_evidence`. Do not invent assumptions.

### 3.3 Deterministic stages

> [!NOTE]
> Historical workflow proposal only. The stage names and the `actionable | investigate | insufficient_evidence` review result below are not current enums. Use the final architecture specification's canonical stages, state axes, and G0–G7 policy.

1. **Freeze input**: Freeze query time, definition versions, source receipts, and authority scope.
2. **Validate experiment**: Check SRM, sample size, ramp, window, missingness, and guardrails.
3. **Recompute metric**: Recompute aggregate and decomposed results in code. The LLM must not alter numbers.
4. **Locate loss**: Find the largest contributing component, segment, and time slice.
5. **Map system path**: Map metric definition to event, service, endpoint/job, and code symbol.
6. **Build hypotheses**: Produce at least one primary hypothesis, one alternative hypothesis, and one disconfirmation path.
7. **Test evidence**: Run read-only queries, align traces, and compare deployment or rollout cohorts.
8. **Draft change options**: Bind each option to repo/ref/file/symbol, expected effect, risk, test, and rollback.
9. **Review gate**: Decide `actionable`, `investigate`, or `insufficient_evidence`.

Code advances the stages. Models handle semantic judgment and candidate explanations only. A failure retries only the current stage.

### 3.4 Outputs

- Experiment-validity verdict.
- Effect summary and component/segment decomposition.
- Ranked competing hypotheses.
- Supporting, contradicting, and missing evidence for each hypothesis.
- Production path and deployed-change links.
- `change_proposal[]`: target, proposed delta, expected metric effect, counter-metric, blast radius, owner, test, rollback, and confidence.
- Items that cannot be confirmed and the cheapest next validation action.

### 3.5 Success criteria

- Every number can be recomputed from frozen input.
- Every causal claim cites at least one item of metric evidence and one item of system/code evidence.
- A code claim must resolve to an exact repository, deployed SHA, file, or symbol. A label such as "ranking/pipeline" is not sufficient.
- A recommendation must be executable, testable, and reversible.
- If SRM or a critical authority check fails, no ship or revert recommendation may be issued.
- A reviewer can trace an output back to the original row, query, trace, deployment, and diff.

## 4. Scenario B: SEV metric drop

### 4.1 User need

The incident commander needs to know quickly:

1. Whether the drop is real, when it began, and which scope it affects.
2. Which code, config, flag, model, or data changes were deployed in the same window.
3. Which changes match timing, scope, and mechanism.
4. Which evidence contradicts each candidate.
5. What the next safe validation is and whether there is enough evidence for a human rollback decision.

### 4.2 Required inputs

- Alert, metric definition/version, baseline, changepoint, and affected dimensions.
- Raw metric rows, logging health, and pipeline freshness.
- Incident/deploy/feature-flag/config/schema/model/experiment timeline.
- Service topology, traces, logs, and sample requests.
- Exact repository identity, deployed SHA, parent SHA, PR/commit, rollout scope, and owner.
- Rollback, holdout, unaffected cohort, or adjacent metric as a counterfactual signal.
- Typed production change inventory. Every change has a type, stable event ID, effective interval, scope, source link, runtime identity, and rollback state.
- Metric-segment -> service/route -> repo/file/symbol mapping. Unknown mappings must remain explicit and must not degrade into fuzzy repository-wide guessing.

### 4.3 Deterministic stages

> [!NOTE]
> Historical workflow proposal only. The `suspected | likely | confirmed | insufficient_evidence` result below is a superseded single-axis model. `likely` and `insufficient_evidence` are not current Cause Verdict values; missing evidence is represented through Coverage Gaps, blockers, and the canonical fail-closed policy.

1. **Verify signal**: Rule out instrumentation, freshness, and definition drift.
2. **Detect changepoint**: Freeze start time, confidence interval, scope, and timezone.
3. **Assemble timeline**: Merge deploy, flag, config, model, data, experiment, and incident events.
4. **Resolve deployed changes**: Include only changes that reached the affected production scope.
5. **Map mechanism**: Map change -> runtime path -> metric component.
6. **Rank candidates**: Score timing, scope overlap, mechanism, rollback/counterfactual, and independent corroboration separately.
7. **Seek disconfirmation**: Check unaffected cohorts, contrary metrics, undeployed commits, and concurrent events.
8. **Review gate**: Output `suspected`, `likely`, `confirmed`, or `insufficient_evidence`.

Do not automatically promote the most recent deployment to root cause. Do not omit config, flag, model, or data changes.

### 4.4 Outputs

- Verified incident timeline.
- Affected scope and blast-radius estimate.
- `code_change_candidate[]`: deploy ID, repo, SHA, PR/commit, files/symbols, owner, rollout scope, time delta, and diff digest.
- `change_attribution[]`: supporting, contradicting, and missing evidence, plus component scores.
- Next safe checks. If needed, produce a rollback review packet for a human; the agent does not execute rollback.
- Conclusion state and confidence falsifier.

### 4.5 Success criteria

- Every candidate has deployment proof. Undeployed commits must not appear as production candidates.
- All candidates use the same timezone and an explicit window.
- Ranking uses timing, scope, and mechanism together. Proximity alone is insufficient.
- Show at least one alternative cause and one disconfirmation check.
- `confirmed` requires deployment proof, scope overlap, mechanism evidence, and at least one of rollback, holdout, or independent validation.
- The output is replayable in an incident review. Humans can see missing authority and stale sources.

## 5. Shared evidence graph

The agent must build a queryable, traceable evidence graph. It is not a free-text narrative.

```text
metric definition/version
  -> metric observation -> component/segment/changepoint
  -> event/trace -> service/runtime path -> repo/file/symbol
  -> deploy/flag/config/model change -> rollout scope
  -> hypothesis -> supporting/contradicting/missing evidence
  -> verdict -> proposed check/change -> validation/rollback
```

Every node has at least: `evidence_id`, type, source system, stable source ID, `observed_at`, `retrieved_at`, scope, authorization, freshness, content digest, redaction, and status.

Every edge has at least: source, target, relation, basis, generation method, confidence, and falsifier. An `inferred` edge must be labeled explicitly and must not masquerade as a source fact.

Each experiment or incident is an isolated case. A case must freeze `case_id`, identity, source manifest, authorization, time range, model/tool versions, and evidence digest. Cross-case memory may be used for navigation only; without human promotion, it cannot become evidence in the current case. Separate UI workspaces do not prove storage, tenant, or cache isolation.

### 5.1 Typed production change inventory

`production_change` is a required A/B evidence type, not an optional appendix. Minimum fields:

- `change_id` and `change_type`: `code | config | flag | model | data`.
- `effective_from`, `effective_to`, timezone, and rollout progression.
- Environment, region, tenant/cohort, and service/route scope.
- Source-system receipt, author/owner, approval/rollout ID, and rollback state.
- Type-specific identity: repository/SHA/diff for code; key/version/digest for config; rule/allocation for flag; artifact/version/route for model; dataset/schema/pipeline version for data.
- Observed runtime identity. A planned deployment or caller-asserted version is insufficient.

The inventory must cover all five change types in the suspect window. If a source for one type is inaccessible, report a coverage gap for that type. Do not rewrite "not found" as "no change."

### 5.2 Runtime identity

Every production claim must bind to runtime fact, not source-control state alone. `runtime_identity` must answer which environment, service instance/build, commit, config digest, flag snapshot, model artifact, and data/schema version were active in that scope and interval. If identities conflict or cannot be verified, a candidate can be no stronger than `suspected`.

### 5.3 Metric-segment -> symbol mapping

A versioned mapping must connect an affected metric component, segment, or query class to service, route/job, repository, file, symbol, and owner. Every mapping has a source, applicable scope, update time, and confidence. Static catalogs, runtime traces, and ownership metadata may jointly support a mapping; retain all conflicts. If mapping is missing, keyword search results must not masquerade as a production path.

## 6. Shared tool requirements

Tools are defined by user tasks, not by old modules.

- `read_metric_definition`: returns version, formula, dimensions, and owner.
- `query_metric`: read-only and parameterized; returns exact query, parameters, rows, row count, result digest, metric-definition version, truncation, and receipt.
- `validate_query_result`: recomputes with an independent implementation and frozen input; returns validator version, result digest, differences, and receipt. Reusing the same faulty logic is not independent validation.
- `validate_experiment`: SRM, ramp, sample, window, and guardrails.
- `detect_changepoint`: returns method, parameters, interval, and sensitivity.
- `search_runtime_evidence`: retrieves evidence by trace/event/service.
- `list_production_changes`: deploy, flag, config, schema, model, and experiment changes.
- `verify_runtime_identity`: verifies the effective version from runtime, deploy, config, flag, model, and data systems; it must not trust caller self-report.
- `map_metric_segment_to_symbols`: uses a versioned catalog and runtime traces to return service/route/repo/file/symbol/owner, preserving conflicts and unknowns.
- `inspect_deployed_diff`: verifies the exact repository and deployed SHA before reading a diff or symbol.
- `resolve_ownership`: service, repository, file, and on-call owner.
- `run_counterfactual_check`: holdout, rollback, unaffected cohort, or adjacent metric.
- `render_review_packet`: renders only from the structured graph and does not rewrite numbers.

Common return fields: `ok`, `data`, `error_class`, `source_receipt`, `authorization`, `freshness`, `timing`, `provenance`, and `truncated`.

SQL requires two read-only layers: a statement allowlist and a read-only connection at the storage layer. SCM, deployment, and incident tools are also read-only. Tools must not receive a general-purpose shell, arbitrary filesystem access, or implicit write authority.

Every tool must have a server-side capability contract: read/write class, source allowlist, exact target, input/output schema, timeout, budget, and auth identity. A UI toggle is only a control surface. The tool server must enforce denial and return an auditable receipt.

## 7. Candidate practices: Adopt / Adapt / Reject

| Source | Candidate practice | Decision | Why it fits the need | Greenfield adaptation | Evidence |
| --- | --- | --- | --- | --- | --- |
| Workshop | Bounded stages, mechanical gates, schema control plane, traceable tool execution, selective parallelism, and human control | **Adopt principle / Adapt mechanism** | Both recordings have 100% coverage; all 73 screenshots have topic-level alignment; audio-only segments are fully retained | Use one deterministic evidence lifecycle for A/B; rewrite stages, routing, budgets, and approval by scenario; do not copy competition parameters or treat a demo as production proof | `meeting-audio-alignment.md`; primary audio `00:18:05–00:37:20, 00:41:35–01:07:55, 01:12:20–01:25:45, 01:26:42–01:40:13, 01:42:28–02:08:18`; medium to high |
| Champion source | Fixed Python main flow; model judgment only at uncertain nodes | **Adopt** | A/B both require replayable stages and explicit failure points | Define stages from experiment/incident needs; do not copy the competition flow | Strong; `zz_agent_v2.py` anchors in `kdd-source-practices.md` |
| Champion source | Relevance filtering fails open; underlying evidence remains recoverable | **Adopt** | Prevents context pruning from deleting a critical deploy or trace | Filtering affects default context only, never the graph/source registry | Strong; `doc_relevance_agent.py` and `table_relevance_agent.py` in the same source |
| Champion source | Narrow tool surface | **Adopt** | Reduces excessive authority, path guessing, and ambiguous traces | Use the diagnostic tools in Section 6; do not copy competition tool names | Strong; `solver_agent.py` in the same source |
| Champion source | Mechanical validation before semantic judgment | **Adopt** | Code can decide SRM, schema, time, and deploy-proof invariants | Run invariants before every gate | Strong; `fanout_struct.py` in the same source |
| Champion source | Layered recovery; clean the current failed artifact before retry | **Adapt** | Prevents corrupted state from accumulating | Retry only the current adapter, query, or semantic layer; preserve read-only evidence | Strong; `zz_agent_v2.py` in the same source |
| KDD_Competition | Trusted run ledger | **Adapt** | A/B both require input, commit, metrics, artifact, and rerun recipe | Extend it into evidence-graph receipts; do not preserve competition verdicts or schema | Strong; `kdd/trusted_run_ledger.py:31-175` |
| KDD_Competition | `SELECT/WITH` allowlist plus SQLite read-only mode | **Adopt** | The authority boundary can be enforced mechanically | Every data adapter uses storage-level read-only mode plus statement checks | Strong; `core/sql_executor.py:99-177` |
| KDD_Competition | Broad self-consistency voting | **Reject by default** | Stable errors can be amplified at roughly N times the cost | Trigger selectively only at calibrated high-variance nodes; abstain if there is no majority | Strong; `kdd/voting.py:1-20,50-87` |
| KDD_Competition | Task-shaped hardcoded fast path | **Reject** | Benchmark success does not imply real-scenario generalization | Allow deterministic rules only when supported by a metric definition or versioned policy | Strong/medium; `kdd-source-practices.md` |
| Team 1286 | Humans and agents share structured, replayable evidence state | **Adapt** | A/B reviewers must verify what the agent saw, omitted, and inferred | Replace the shared workspace with this evidence graph; retain tool calls, stage decisions, receipts, citations, and short explanations, not hidden reasoning | Strong; paper pp. 1–4, 17–19; video `02:05–03:19`; `creative-team1286-practices.md:35-43` |
| Team 1286 | Deterministic stages, independent review, bounded repair, and abstention | **Adopt principle / Adapt stages** | Supports replay, local repair, and refusal | Define stages from A/B needs; repair by failure type; do not copy the competition answer flow or generated-code authority | Strong; paper pp. 2–4, 19; video `05:24–06:25`; same file `:55-63` |
| Team 1286 | Human wall: humans make judgments, not evidence | **Adopt** | Material ambiguity and production action require explicit human decisions | Human rulings are guidance only; causal claims still pass the evidence gate; rollback/deploy still need separate authorization | Strong; paper pp. 2, 13–14; video `04:06–04:53,06:12–06:25`; same file `:65-73` |
| Team 1286 | Contract-gated publication | **Adapt** | Prevents unsupported claims from entering A/B decision outputs | Gate metric plus runtime/change evidence completeness; do not copy the KDD column contract | Strong; paper pp. 3, 17, 19; same file `:75-83` |
| Team 1286 | Separate feedback and memory from current evidence | **Adapt** | Enables local correction without allowing old state to masquerade as production fact | Feedback invalidates dependencies and triggers targeted recomputation; memory is navigation only, with scope/version/expiry/approval | Strong; paper pp. 2–5, 13; video `03:19–04:53`; same file `:85-103` |
| Team 1286 | Automatically use benchmark-gold learning in live diagnosis | **Reject** | Production outcomes are not clean gold and can contaminate policy | Permit only offline, versioned, human-gated evaluation improvement | Strong; paper pp. 3, 6; same file `:115-122` |
| Team 1286 | PiTrace workspace graph as the production evidence plane | **Reject as-is** | It lacks typed production changes, runtime identity, and metric-segment-to-symbol mapping | Borrow control principles only; define the production evidence plane independently in Section 5 | Strong; same file `:14,43,177-195` |
| Team 1401 | Visible plan, tool action, raw input, result, and source-backed evidence | **Adopt** | A/B reviewers need to inspect inputs, actions, numeric provenance, and failure points | Show structured stages, tool receipts, and source locators; do not claim to expose full chain-of-thought | Video-only, medium; `01:07.54–01:23.54,06:00.78–06:21.18,06:37.46–06:44.22`; `creative-team1401-practices.md:106-118` |
| Team 1401 | Exact query plus independent validator | **Adapt** | A/B numbers must be mechanically reproducible to prevent bad joins, bad filters, or LLM rewriting | Code records query, parameters, digest, row count, truncation, and metric version; an independent validator recomputes; correct SQL does not establish causality | UI evidence medium; independent-check claim weak; video `06:12.02–06:21.18,07:41.94–07:54.14`; same file `:120-132` |
| Team 1401 | Per-tool enablement and sensitive-tool labels | **Adapt** | A/B require least privilege and cannot rely on frontend switches | Convert to a server-side capability contract bound to source, target, schema, budget, and identity; denial must produce a receipt | Video-only, medium; server-side enforcement unknown; video `03:15.22–03:53.22`; same file `:134-146` |
| Team 1401 | Pause for approval before every tool call | **Adapt** | High-risk steps need human decisions, but B cannot wait on every safe read | Run ordinary allowlisted reads automatically; pause only for sensitive sources, large scans, PII, and change/rollback packets; bind approval to immutable action digest, identity, and expiry; require reapproval after edits | Video-only, medium; quality and latency effects unknown; video `06:21.18–06:54.98`; same file `:148-160` |
| Team 1401 | Case/session isolation for files, conversation, and settings | **Adopt** | Prevents evidence, authority, and settings from crossing experiments or incidents | Freeze identity, source manifest, authorization, time range, versions, and digest per case; do not treat UI separation as proof of security isolation | UI and speaker claim, medium; security isolation unknown; video `00:54.14–01:07.54`; same file `:190-201` |
| Team 1401 | Uploaded-files-only sandbox | **Reject** | A/B must read authoritative metric, runtime, SCM, deploy, flag, config, model, and data systems | Use allowlisted read-only adapters; every call returns identity, freshness, authorization, and receipt | Explicit author disclosure, medium; video `01:47.18–01:52.56,08:24.34–08:28.32`; same file `:230-241` |
| Team 1401 | Heuristic cross-database join as evidence | **Reject** | Same-name fields do not prove semantics, cardinality, or lineage and can produce false numbers and causal chains | At most generate a candidate; require confirmation by catalog, lineage, type, uniqueness, owner, and verified query | Video-only, medium; error rate unknown; video `04:43.50–05:01.84,08:18.10–08:24.34`; same file `:217-228` |
| Team 1401 | ReAct / DRAGIN / Multi-agent / Hybrid-B competition route | **Reject** | No A/B ablation, route rule, or failure evidence supports the target design | Reconsider only if same-cohort A/B evaluation proves a quality lift with acceptable p95 and cost | Video-only, weak; video `02:59.50–03:15.22`; same file `:243-253` |
| Old SMA | "No significant change" is a valid diagnosis | **Adopt** | Prevents explanation pressure from manufacturing causal stories | Use it as a variance gate and abstention policy | Medium; `.agents/skills/sma/SKILL.md:35-37` |
| Old SMA | Check instrumentation first; rank hypotheses by cost and frequency | **Adapt** | A/B both need measurement artifacts ruled out first | Compute ranking dynamically from scenario evidence; do not freeze the old domain ordering | Medium; `.agents/skills/sma/SKILL.md:79-89` |
| Old SMA | Require a contrarian hypothesis in addition to the primary one | **Adopt** | Directly supports disconfirmation and incident safety | Require supporting, contradicting, and missing evidence in the graph | Medium; `.agents/skills/sma/SKILL.md:192-201` |
| Old SMA | Probable cause plus evidence, confidence falsifier, and next step | **Adapt** | Matches the A/B decision output | Add production provenance, deploy proof, rollback, and test | Medium; `.agents/skills/sma/SKILL.md:69-75` |
| Old SMA | Original pipeline, artifact names, old schema, and thresholds | **Reject** | They are not constraints derived from A/B needs | Reimplement from the contracts and evaluation cases in this document | Not a design input |

## 8. Review gates

> [!IMPORTANT]
> **Superseded pre-contract gate model.** Gates 0–3 below are retained for research provenance and must not be implemented. The current contract defines G0–G7, GateReceipt inputs and outcomes, dependency invalidation, ceilings, and independent Cause Verdict and Recommendation Readiness axes in the closed canonical policy ticket and final architecture specification.

### Gate 0 — Authority

- The source is in the allowlist.
- The current identity has read-only permission.
- Redaction and retention policy are known.
- Repository identity is confirmed exactly.

Failure result: `blocked`. Do not attempt a bypass.

### Gate 1 — Evidence quality

- Metric definition/version is frozen.
- Source freshness meets policy.
- The query is not truncated, or truncation is handled explicitly.
- Evidence IDs resolve and digests match.
- Unknown, partial, and unauthorized states are not hidden.
- The five-type production change inventory is covered; uncovered types are explicit coverage gaps.
- Runtime identity is verified or explicitly conflicting/unknown.
- Metric-segment-to-symbol mapping has a source, version, and applicable scope.
- Numeric results retain the exact query and execution receipt and pass an independent validator; the validator does not reuse the same execution result.

Failure result: `insufficient_evidence` or a downgraded conclusion.

### Gate 2 — Causal discipline

- Measurement and instrumentation have been checked.
- At least two candidate hypotheses exist.
- Supporting, contradicting, and missing evidence are all shown.
- Timing, scope, and mechanism are judged separately.
- Correlation is not described as a confirmed cause.

Failure result: at most `suspected`.

### Gate 3 — Actionability

- Exact repository, deployed SHA, target file/symbol, and owner are confirmed.
- The proposal includes expected effect, counter-metric, blast radius, test, and rollback.
- A's experiment validity passes.
- B's rollback packet still requires incident-commander approval.
- An approval-required action is bound to an immutable digest, approving identity, and expiry. Parameter changes require reapproval. Ordinary allowlisted read-only calls do not pause step by step.

Failure result: recommend further investigation only.

## 9. Minimum evaluation cases

### A — Post-experiment

1. A treatment-only component drops; the only trace resolves to a deployed symbol.
2. Control and treatment drop together; classify it as a systemic change, not an experiment effect.
3. SRM fails; block the change recommendation.
4. The metric definition changes inside the window; recompute by version or abstain.
5. Mix shift explains the aggregate; there is no within-segment regression.
6. Two similar services exist; only one has trace and deploy proof.
7. The proposed target is correct but rollback/test is missing; Gate 3 fails.
8. Ground truth is normal variance; output no significant change.

### B — SEV

1. The most recent deployment does not overlap the affected scope; the metric recovers after an older change is rolled back. Rank the older change higher.
2. A commit exists but was not deployed; do not list it as a production candidate.
3. The logging pipeline is stale; classify measurement incident first.
4. A config or flag change is causal; do not search code commits only.
5. Events use multiple timezones; normalize them before ranking.
6. Rollback and metric recovery are only temporally correlated and lack scope proof; do not mark `confirmed`.
7. SCM access is unavailable; preserve the candidate gap and do not guess the diff.
8. Two concurrent changes exist; output competing hypotheses rather than forcing a single cause.

### Shared failure cases

- Source timeout, stale, partial, unauthorized, or truncated.
- Evidence digest mismatch.
- Prompt injection appears in a log, PR, or document.
- A secret or PII appears in a diff or query row.
- LLM narrative rewrites structured numbers.
- Tool retry exceeds budget.

Score every case on: factual accuracy, evidence recall, false-cause rate, abstention calibration, production-provenance completeness, review-gate correctness, latency, token/cost, and authority safety.

## 10. Authority boundaries

- Read-only by default. Prohibit `INSERT/UPDATE/DELETE`, configuration changes, flag changes, deployment, rollback, commit, PR, and incident mutation.
- Inherit source-system permissions. The agent identity must not expand what a user may see.
- Private code, logs, and customer rows enter authorized context only. Redact outputs at the field level.
- Production action requires a separate tool, separate authorization, exact target, and human confirmation. It is outside this requirements draft's MVP.
- Trigger approval by risk. Sensitive sources, large scans, PII, and change/rollback packets require a pause. Approval cannot be reused across actions or cases.
- Budget, timeout, concurrency, and retry all have hard caps. On exhaustion, preserve the best-known evidence and abstain.
- Trace tool, query/diff locator, receipt, error, token usage, and wall time. Do not put secrets in traces.
- Isolate case state, cache, retrieval index, trace, and authorization by `case_id`. Cross-case promotion requires human review of permission, freshness, and provenance.

## 11. Greenfield MVP validation order

1. Freeze evidence node/edge, tool response, and A/B output schemas.
2. Build synthetic metric, experiment, timeline, deployment, and local-Git fixtures.
3. Implement deterministic validators, stages, and review gates.
4. Run the cases in Section 9 first. Require zero false `confirmed` results.
5. Connect local read-only adapters. Verify exact repository/deployed SHA and provenance.
6. Then run production shadow reads. Humans still perform every action.
7. Discuss broader rollout only after same-cohort baseline comparison proves quality lift, acceptable p95/cost, and authority safety.

## 12. Open product and organizational questions

- The speaker roster and some individual names still cannot be verified reliably from distant-room audio alone. This does not affect topic-level practice assessment.
- What are the real source systems, SLAs, permissions, and retention policies for the two scenarios?
- Which incident/experiment approvals does `confirmed` require in the organization?
- Who maintains the authoritative metric -> runtime -> repository mapping?
- Which production code may expose a full diff, and which may expose only a digest/locator?
- What are the expected-effect target for A and the incident-latency target for B?

Until these questions are answered, contracts and offline cases can be validated, but production readiness cannot be claimed.
