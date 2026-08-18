# Requirements-first Data Agent Research

Date: 2026-08-11

Scope: Research and design. No models were run. No agent was modified.

The goal is a ground-up redesign based on two real needs. This is neither a copy of KDD nor a patch for the old SMA. Requirements and success criteria come first; candidate practices from the workshop, KDD-winning entries, and the old SMA code and architecture are evaluated afterward.

Each practice from all three reference groups must be assessed individually as `adopt / adapt / reject`. These references impose no compatibility constraints, require no legacy framework, and do not determine the target architecture.

Creative Track primary-source status:

- Team 1286: video + 23-page paper. Research complete: [`creative-team1286-practices.md`](creative-team1286-practices.md).
- Team 1401: video-only. Research complete: [`creative-team1401-practices.md`](creative-team1401-practices.md).

Both Team 1286 and Team 1401 are included for scenarios A and B. Team 1401 has only a video, not a paper; its mechanisms, author claims, and this report's inferences remain separate.

Independent source-code audit: [`primary-source-audit.md`](primary-source-audit.md). References to the old KDD and SMA follow that audit's canonical files, symbols, and exact line anchors.

## 1. Needs

### A. Post-experiment

The input is a completed or closing experiment whose metric missed expectations.

Questions to answer:

1. Are the experiment and metric signal trustworthy?
2. Does the miss come from measurement, exposure, mix shift, or the product mechanism?
3. Which production code supports or contradicts that explanation?
4. What code, config, rollout, or experiment design should change?
5. What validation could falsify the recommendation?

### B. SEV

The input is a production metric drop and an incident window. Candidate changes include code, config, flags, models, and data.

Questions to answer:

1. Is the drop real? When did it begin? Which segments are affected?
2. What code, config, flag, model, data, deploy, or dependency changes occurred around the breakpoint?
3. Which changes can explain the affected path?
4. Which evidence is merely temporal, and which has mechanistic support?
5. Is the next step rollback, mitigation, added observability, or further investigation?

### Shared problems

- Metric, experiment, deploy, and repo identities are easy to mismatch.
- Correlation is easily presented as causation.
- Raw values, code diffs, and model narratives are easily conflated.
- Source pruning can omit evidence, while unlimited context increases cost and noise.
- Retries, fan-out, and voting compound costs and can amplify shared errors.
- A final answer without a query, commit, diff, and validation chain cannot be reviewed.

## 2. Success criteria

### A. Post-experiment

Completion criteria:

- Fix the experiment id, variant, population, time window, metric definition, and expected direction.
- Recompute the observed delta. Check exposure, sample size, holdout, SRM, freshness, and completeness.
- Decompose the overall miss into actionable segments. Distinguish within-segment change from mix shift.
- Connect at least one primary hypothesis to both metric evidence and production code evidence.
- Point the recommendation to a file, symbol, diff, or config. State the expected impact, risk, and falsifier.
- When confirmation is impossible, return `inconclusive` and the smallest next step. Do not invent causality.

### B. SEV

Completion criteria:

- Fix the incident window, baseline, breakpoint, affected segment, and severity.
- Build a timeline of code, config, flag, model, and data changes around the breakpoint.
- Give every suspect change a stable identity, effective time, affected path, and supporting and contradicting evidence. Code changes also require a commit and diff hunk.
- Temporal order must satisfy `change before effect`. An unknown time does not pass.
- Return ranked candidates. Clearly distinguish confirmed, probable, possible, and ruled out.
- Provide a safe action, owner, validation method, and stopping condition.

### Shared quality gates

- Values come from a rerunnable query or deterministic computation.
- Code claims come from a fixed repo, commit, and diff.
- Every conclusion includes a source id and evidence strength.
- Each run records the route, tool calls, errors, repairs, tokens, cost, wall time, and final artifact.
- Quality, coverage, p95 latency, and cost are evaluated separately for A and B.

## 3. Required evidence and tools

| Evidence | A. Post-experiment | B. SEV | Minimum tool interface |
|---|---|---|---|
| Metric | definition, query, rows, CI, segment, freshness | query, breakpoint, segment, baseline | `query_metric`, `validate_metric` |
| Experiment | id, arms, exposure, holdout, SRM, rollout | Same if the SEV involves an experiment | `inspect_experiment` |
| Runtime | production version, config, flag, model, data dependency | incident service, deploy/config/flag/model/data timeline, runtime version | `inspect_runtime`, `list_changes` |
| Code | serving path, metric instrumentation, candidate mechanism | commits, diffs, owners, affected call path | `search_code_changes`, `read_diff`, `trace_code_path` |
| Validation | counterfactual slice, recompute, targeted test | rollback/canary evidence, targeted test, log corroboration | `test_hypothesis`, `validate_claim` |
| Artifact | claim, evidence, confidence, falsifier, action | suspect change, evidence, confidence, safe action | `publish_report` |

All tools should return `ok`, `data`, `source_id`, `identity`, `time_range`, `error_class`, and `timing`. Read and write tools remain separate. Production access is read-only by default. Actions with side effects require explicit approval.

## 4. Candidate practices

Evidence strength:

- **Strong**: Directly implemented in source code, or directly supported by a high-confidence workshop audio segment with contemporaneous screenshots used only to correct terminology or topic identification.
- **Medium-strong**: Implementation plus unit tests, but no production result.
- **Medium**: README, design contract, verified playbook, or synthetic fixture.
- **Weak**: Estimate or design claim that cannot establish an effect by itself.

Evidence narrative labels:

- **Observed**: Directly visible or audible in source code, a paper, audio, or the screen at the specified anchor.
- **Speaker/Paper claim**: Explicitly stated by the author, but not independently verified in the current materials by a receipt, source code, or a controlled experiment.
- **Reviewer inference**: A selection or risk judgment made by this report from the A/B requirements. It cannot retroactively alter primary evidence.

### 4.1 Workshop speaker evidence

> **Status: Audio-aligned.** [`meeting-audio-alignment.md`](meeting-audio-alignment.md) covers intro `348.330667/348.330667s`, workshop `7997.098667/7997.098667s`, and aggregate 100%. Time mapping and topic-level cross-alignment are complete for 73/73 screenshots.

The complete intro and workshop recordings (raw media not included because of size, privacy, and source availability) are the meeting's primary record. The alignment is an ASR-assisted, faithful summary in Chinese, not a transcript, and it has no manual speaker diarization. Distant Q&A, names, proper nouns, and explicitly low-confidence segments remain marked "unconfirmed."

The 73 screenshots are sparse samples of presentation slides, not a complete deck. Topic-level alignment shows only that a screenshot matches the contemporaneous audio topic; it can correct terminology, team names, or numbers, but does not verify spoken words verbatim. Audio-only segments are fully preserved. Missing screenshots are not negative evidence.

#### W1. Bounded stages and independent verification

- **Practice**: `PLAN -> EXPLORE -> ANSWER -> VERIFY`. Each stage has its own goal, tools, and completion criteria. A failed VERIFY may return to ANSWER a limited number of times.
- **Evidence anchor**: Workshop audio `00:45:00–00:48:00`; results and boundaries `00:51:20–00:54:20`. Contemporaneous screenshots 12–19; see chunk 03 in `meeting-audio-alignment.md`.
- **Problem addressed**: Limits unconstrained exploration and separates completion judgment from generation.
- **Evidence strength**: Strong for the mechanism; medium for the effect. High-confidence audio supports the four stages, independent review, and bounded fallback. The audio only summarizes higher local comparisons and fewer missing answers; specific score values come from a contemporaneous slide, not verbatim speech. The speaker explicitly states that the end-to-end gains cannot be attributed entirely to phase gates and reports that an automated improvement loop failed because of prompt leakage.
- **Conditions**: Both A and B may use stages and gates. Requirements determine the number of stages; the slide count is not copied.

#### W2. Layered validation and bounded repair

- **Practice**: Separate pre-execution, post-execution, and independent review. After a failure, repair the SQL and revalidate a limited number of times.
- **Evidence anchor**: Workshop audio `00:48:00–00:51:20`; feedback, repair, revalidation, and provenance-artifact discussion at `01:17:20–01:23:40`.
- **Problem addressed**: Catches mechanical errors before semantic errors and prevents unbounded retries.
- **Evidence strength**: Strong for the mechanism. High-confidence audio supports pre-execution SQL structure checks, post-execution empty-result and output-shape checks, an independent reviewer, and bounded repair. A repair count seen only on a slide is not presented as a general fact. Benefits for A and B are unknown.
- **Conditions**: Mechanical gates must precede the LLM reviewer. Repairs require an error type and a budget.

#### W3. Convert large inputs into compact structures first

- **Practice**: A doc-reader stores prose records as CSV, which the main agent then processes as a table with Python. A video reader combines frames, SRT, and OCR.
- **Evidence anchor**: Workshop audio `00:57:30–01:02:25`; document extraction at `00:06:20–00:08:35` and video/ASR at `00:08:35–00:12:30`.
- **Problem addressed**: Prevents overflow in the main context and improves extraction accuracy for numbers and characters.
- **Evidence strength**: Strong for the mechanism; weak for the effect. High-confidence audio supports doc/video readers, main-context control, and frame/subtitle/OCR merging. The first team's audio-only segment also supports a record universe, divided extraction work, and temporal alignment. Estimated gains cannot be attributed independently or extrapolated to production.
- **Observed failure boundary**: Workshop audio `01:19:30–01:23:40`. The speaker reports that a complex hard-join SQL approach performed poorly; full pre-indexing did not finish on the first run, so the team switched to on-demand evidence retrieval. **Reviewer inference**: This shows that a specific competition approach failed. It does not show that Python is generally superior to SQL or that all pre-indexing is unsuitable.
- **Conditions**: Enable only for long specs, large diffs, long incident timelines, or multimodal evidence. Raw evidence must remain retrievable.

#### W4. An independent reviewer helps but can corrupt a correct answer

- **Practice**: The reviewer is instructed to criticize rather than approve and to redo work when necessary.
- **Evidence anchor**: Workshop audio `01:00:00–01:02:25`; contemporaneous screenshot 24.
- **Problem addressed**: Reduces executor self-review bias.
- **Evidence strength**: Strong for the mechanism; weak for the gain. High-confidence audio supports treating executor output as a possibly incorrect hypothesis. Specific gains come primarily from a slide and do not establish an effect for A or B. The adjacent negative-result segment shows that a reviewer or ensemble is not consistently effective.
- **Conditions**: The reviewer may check only the claim/evidence contract. Any changed value or evidence must pass the deterministic gate again.

#### W5. Default fan-out and voting have no stable gain

- **Practice/failure evidence**: Playbooks showed no clear gains. Two executors plus a reviewer often selected the wrong answer. Three executors plus majority vote sometimes performed better locally but had no clear effect on the A-board.
- **Evidence anchor**: Workshop audio `01:02:25–01:05:15`; contemporaneous screenshot 25. NVIDIA's coverage-first retry at `00:26:45–00:33:10` shows only selective budget allocation within the competition.
- **Problem addressed**: Prevents treating additional sampling as reliability.
- **Evidence strength**: Strong for this team's negative result. High-confidence audio directly supports the absence of clear, stable gains from playbooks, two executors plus a reviewer, and three executors with majority vote. This argues against default broad voting; it does not show that all selective fan-out is ineffective.
- **Conditions**: Allow only difficulty-aware, low-confidence, high-value selective fan-out. Measure quality, cost, and p95 latency on the same batch.

#### W6. Schema as the control plane

- **Practice**: `Ingest -> Profile -> Route -> Execute -> Validate`. Each step consumes an explicit contract and emits a narrower representation. Unstructured evidence supplies only rules or mappings; exact values are computed from canonical structured sources.
- **Evidence anchor**: Workshop audio `01:42:28–01:46:50`, `01:47:32–01:53:25`; contemporaneous screenshots 56–63. ASR repeatedly degrades at `01:46:52–01:47:32`, so the content is unconfirmed.
- **Problem addressed**: Controls context, tools, and output while preventing narratives from rewriting exact values.
- **Evidence strength**: Strong for the mechanism; medium for the competition-deliverability claim. High-confidence audio supports task-level schemas, source-role routing, canonical structured values, bounded tools, answer schemas, empty-output rejection, and bounded fresh-context review. The speaker also explicitly notes remaining run-to-run variance. Effects in new scenarios are unverified.
- **Conditions**: Claims, metrics, changes, and validations all require typed schemas. A schema must not become a legacy-system compatibility burden.

#### W7. Inspectability, difficulty routing, human control, and budgets

- **Practice**: A trace links tool calls, observations, errors, retries, and output. The route depends on task difficulty. Step and tool-result budgets are bounded. Side-effecting tools require approval.
- **Evidence anchor**: Workshop audio `01:55:48–02:08:18`; contemporaneous screenshots 65–73.
- **Problem addressed**: Supports review and mid-run intervention while avoiding unnecessary computation.
- **Evidence strength**: Strong for the mechanism; weak to medium for the effect. High-confidence audio supports visible traces, difficulty-aware routing, error/stall/budget recovery, Autopilot/Co-pilot, and approval. Cost, latency, and backbone comparisons lack sufficient production evidence.
- **Conditions**: Set routes and budgets separately for A and B. When the budget is exhausted, preserve the best-known finding and coverage gap.

Extrapolation limit: In workshop audio `02:05:20–02:08:18`, the speaker explicitly states that external validity, difficulty/modality confounding, and systematic stability remain insufficiently validated. Contemporaneous screenshot 73 supports terminology correction. A competition demo cannot be extrapolated into production proof.

#### W8. Guard-removal ablation: consensus cannot replace deterministic guards

- **Observed**: Workshop audio-only `01:30:00–01:31:25,01:34:30–01:39:31`. Three computational paths initially agreed, but the eligibility/follow-up guard still rejected the result. Removing guards one by one caused the system to accept a biased answer when the eligibility check was removed, even though all three paths still agreed.
- **Speaker claim**: The speaker explicitly concludes that consensus cannot replace an eligibility guard.
- **Reviewer inference**: A and B must encode critical guards such as experiment eligibility, exposure, runtime scope, and change effective interval as deterministic gates. Multiple agents, multiple queries, or majority agreement cannot promote an answer with a missing guard to confirmed.
- **Evidence strength**: Strong for this demo ablation; the production effect is unknown.
- **A/B decision**: **Adopt / Adopt**. A/B requirements and authoritative evidence define the guards; medical-domain conditions are not copied.

### 4.2 KDD champion / KDD_Competition evidence

Source-code identity:

- Champion source: [`zhezh/kddcup2026_champion@bdc874fc4260e3565ae0dce041728fdf5b376709`](https://github.com/zhezh/kddcup2026_champion/tree/bdc874fc4260e3565ae0dce041728fdf5b376709).
- Local iteration source: `KDD_Competition` (local source, not included), audit commit `7270e3bcc24a039ac458e45caeab7a283c62eca8`.
- `zz_agent_v2.py` is in the Champion clone. The current `KDD_Competition` tree has no file by that name. The inheritance relationship between the two repos is **unconfirmed**.
- The Champion README describes the entry as Top1. The ranking was not independently verified against the official leaderboard, so the ranking evidence is medium.

#### K1. Code-controlled primary flow

- **Practice**: Code handles input isolation, evidence reading, relevance filtering, structuring, solver scaffolding, execution, recovery, artifact checks, and tracing in sequence. The model makes judgments or writes analysis logic only at bounded points.
- **Code anchor**: [`zhezh/kddcup2026_champion@bdc874…/src/data_agent_baseline/zz_agent_v2.py:173-228,235-385,519-641`](https://github.com/zhezh/kddcup2026_champion/blob/bdc874fc4260e3565ae0dce041728fdf5b376709/src/data_agent_baseline/zz_agent_v2.py#L173-L641).
- **Problem addressed**: Prevents omitted steps and makes failure locations clear.
- **Evidence strength**: Strong; directly implemented in source code.
- **Conditions**: Fix the evidence lifecycle in the new agent. The model handles only uncertain decomposition, hypotheses, and explanations.

#### K2. Fan out only after a structured plan

- **Practice**: The planner first defines sections, the record universe, the schema, and normalization rules. Code validates the plan, workers extract independently, and results are merged by stable id.
- **Code anchor**: `zhezh/kddcup2026_champion@bdc874fc4260e3565ae0dce041728fdf5b376709/src/data_agent_baseline/doc_tools/fanout_struct.py:81-149,666-722,780-845,1557-1665`.
- **Problem addressed**: Reduces missing fields, mixed rows, and context overflow in long inputs. Failed blocks can be retried independently.
- **Evidence strength**: Strong.
- **Conditions**: Each fan-out unit must be a falsifiable hypothesis and mergeable by evidence id.

#### K3. Fail-open filtering with retrievable underlying evidence

- **Practice**: A relevance timeout or missed classification defaults to relevant. Table filtering collapses only prompt descriptions and does not delete underlying tables. The solver can rediscover a table.
- **Code anchor**: `zhezh/kddcup2026_champion@bdc874fc4260e3565ae0dce041728fdf5b376709/src/data_agent_baseline/agents_v2/doc_relevance_agent.py:487-586`; `zhezh/kddcup2026_champion@bdc874fc4260e3565ae0dce041728fdf5b376709/src/data_agent_baseline/agents_v2/table_relevance_agent.py:326-354,431-515`; `zhezh/kddcup2026_champion@bdc874fc4260e3565ae0dce041728fdf5b376709/src/data_agent_baseline/zz_agent_v2.py:348-376`.
- **Problem addressed**: Reduces default context while limiting losses from false filtering.
- **Evidence strength**: Strong.
- **Conditions**: Only context may fail open. A metric-quality gate cannot treat missing fields as trustworthy.

#### K4. Narrow tools, layered context, and deterministic gates

- **Practice**: The solver has only four tools: explore, run, read, and edit. Complete data stays in the data layer, and the prompt includes only relevant previews. Code checks JSON, columns, row count, ids, and SQL read-only status first.
- **Code anchor**: `zhezh/kddcup2026_champion@bdc874fc4260e3565ae0dce041728fdf5b376709/src/data_agent_baseline/agents_v2/solver_agent.py:136-197`; `zhezh/kddcup2026_champion@bdc874fc4260e3565ae0dce041728fdf5b376709/src/data_agent_baseline/doc_tools/fanout_struct.py:650-660,702-722,748-816`; `KDD_Competition/core/sql_executor.py:99-113,148-177` (local source, not included), symbols `execute_sql`, `_check_write_block`, `_run_sqlite`; `KDD_Competition/kdd/sanity_checker.py:1-13,33,87-181` (local source, not included), symbols `check_sanity`, `_check_zero_rows`, `_check_magnitude`; audit commits `bdc874fc4260e3565ae0dce041728fdf5b376709`, `7270e3bcc24a039ac458e45caeab7a283c62eca8`.
- **Problem addressed**: Reduces unauthorized action and fabrication. Catches structural errors cheaply.
- **Evidence strength**: Strong.
- **Conditions**: A and B use narrow tools oriented around evidence actions. Business thresholds require calibration in the target environment.

#### K5. Layered recovery without continuing from corrupt state

- **Practice**: Before a solver retry, restore a clean scaffold and remove old artifacts. A planner or section failure retries only that layer. The local KDD also distinguishes transport, parse, SQL, empty-result, sanity, and serialization failures.
- **Code anchor**: `zhezh/kddcup2026_champion@bdc874fc4260e3565ae0dce041728fdf5b376709/src/data_agent_baseline/zz_agent_v2.py:519-589`; `zhezh/kddcup2026_champion@bdc874fc4260e3565ae0dce041728fdf5b376709/src/data_agent_baseline/doc_tools/fanout_struct.py:702-722,789-816`; `KDD_Competition/kdd/runner.py:4128-4172,4184-4233,4294-4353,4530-4610,4659-4670` (local source, not included); audit commits `bdc874fc4260e3565ae0dce041728fdf5b376709`, `7270e3bcc24a039ac458e45caeab7a283c62eca8`.
- **Problem addressed**: Prevents corrupt state from contaminating the next attempt and controls retry amplification.
- **Evidence strength**: Strong.
- **Conditions**: Bound transport, query, evidence, and reasoning retries separately. Preserve read-only evidence and failure reasons.

#### K6. Selective fan-out and voting, not broad voting

- **Practice**: Parallelism is limited to specific high-variance points such as video answers, relevance, and section extraction. The local KDD votes only on low-confidence or verified flipper cases and explicitly states that majority vote amplifies stable errors.
- **Code anchor**: `zhezh/kddcup2026_champion@bdc874fc4260e3565ae0dce041728fdf5b376709/src/data_agent_baseline/agents_v2/video_result_agent.py:514-610`; `KDD_Competition/kdd/submission_loop.py:34-47,195-218,256-290` (local source, not included), constant `SQL_FLIPPER_TASKS` and symbol `run_one_task`; audit commits `bdc874fc4260e3565ae0dce041728fdf5b376709`, `7270e3bcc24a039ac458e45caeab7a283c62eca8`.
- **Problem addressed**: Adds cost only at unstable nodes and prevents shared blind spots from becoming majority consensus.
- **Evidence strength**: Strong.
- **Conditions**: Start with a cheap baseline, trigger, and stopping condition. Without shared evidence, return unconfirmed.

#### K7. Code-serialized evidence with complete traces and budgets

- **Practice**: Fixed code writes the final numeric artifact. The trace stores messages, tools, exceptions, tokens, cache tokens, requests, stage durations, routes, and provenance. Task concurrency, LLM inflight, per-task budget, and total budget are bounded separately.
- **Code anchor**: `zhezh/kddcup2026_champion@bdc874fc4260e3565ae0dce041728fdf5b376709/src/data_agent_baseline/tools_v2/scaffold_tool.py:58-109,141-160`; `zhezh/kddcup2026_champion@bdc874fc4260e3565ae0dce041728fdf5b376709/src/data_agent_baseline/zz_agent_v2.py:31-101,543-572,631-640,716-802`; `KDD_Competition/kdd/trusted_run_ledger.py:31,110-176` (local source, not included), symbols `entry_from_manifest`, `build_entry`, `write_ledger_entry`; `KDD_Competition/trace/span.py:17-50` (local source, not included), type `TraceSpan`; `KDD_Competition/trace/collector.py:44-79,93-153` (local source, not included), symbols `emit`, `emit_seam`, `agent_context_for`; `KDD_Competition/kdd/latency_governor.py:61-85,144-228,259-279` (local source, not included); audit commits `bdc874fc4260e3565ae0dce041728fdf5b376709`, `7270e3bcc24a039ac458e45caeab7a283c62eca8`.
- **Problem addressed**: Prevents the LLM from changing values and supports reruns, cost analysis, and tail-latency control.
- **Evidence strength**: Strong for the implemented mechanism; the actual benefit to a new agent is unknown.
- **Conditions**: Code writes the metric, query, runtime, commit, diff, and validation. The LLM writes only explanations that cite these fields.

### 4.3 Creative Track Team 1286: PiTrace

Evidence sources: 23-page paper SHA-256 `1114180be5df7c6a00217518b4602c18e51e5cd882bf4f559521819c56b0a572`; complete `07:58` video SHA-256 `492976a5e113b9d7aa15f5dca262c9add5986b3d16d102adfeba48348c29b15b`. Raw media is not included because of size, privacy, and source availability. Paper page numbers refer to physical PDF pages. Video timestamps come from cross-checking the full-audio transcription against embedded subtitles. `visual-only` means the content is visible on screen but has no corresponding narration.

#### T1286-1. Shared, replayable evidence state

- **Practice**: Humans and agents view the same structured task state. The discovery graph, contract, evidence map, plan, review, and output are all replayable artifacts. The UI is a view, not another source of truth.
- **Evidence anchor**: Paper p1–4, p17–19; Video `02:05–03:19`.
- **Problem addressed**: Prevents the final answer and chat from becoming the only record. Supports source drill-down and local correction.
- **Evidence strength**: Medium-strong. The paper and video UI demonstration agree; this is not an A/B production-effect experiment.
- **A/B decision**: **Adapt / Adapt**. The new state must connect metric, runtime, deploy, and typed change evidence. Store only tool calls, stage decisions, receipts, citations, and brief explanations; do not depend on hidden chain-of-thought.

#### T1286-2. Human gate: humans make judgments, not evidence

- **Practice**: An ambiguity wall provides bounded options, a recommended default, evidence refs, and a fallback. A human choice must still pass evidence, validation, and publication gates.
- **Evidence anchor**: Paper p2, p13–14; Video `04:06–04:53,06:12–06:25`.
- **Problem addressed**: Prevents the agent from guessing when metric definitions, question interpretation, or risk posture are genuinely ambiguous.
- **Observed**: Video visual-only `04:14` shows the run continuing with a default after five minutes. The tool row says `fallback=continue`, and only the answer is marked provisional.
- **Speaker/Paper claim**: The paper and narration describe the wall as a human-agent control mechanism for ambiguity; they do not show that it improves A/B accuracy.
- **Reviewer inference**: `fallback=continue` is fail-open, not human approval. A material attribution/action gate must fail closed: preserve the best-known state, enter blocked/waiting, and notify an explicit owner/on-call through escalation. Only a preapproved, low-risk read branch may fall back.
- **A/B decision**: **Adapt / Adapt**. In A, use it for material definition ambiguity and change review. In B, use it for decisions such as a rollback packet; it cannot implicitly authorize a rollback, flag change, or deploy.

#### T1286-3. Deterministic control, independent review, bounded repair, and abstention

- **Practice**: Contract, evidence, plan, deterministic code, execute, validate, independent review, then accept/repair/abstain. The runner controls timeouts and the repair cap.
- **Evidence anchor**: Paper p2–4, p19; Video `05:24–06:25`.
- **Problem addressed**: Separates evidence collection, computation, and semantic judgment. Errors are locatable, and retries are bounded.
- **Observed: single-demo hollow-determinism boundary**: In the visual-only portion around `05:30`, Task 29's `solution.py` writes the company and numeric value directly as literals; the screen does not show source data being read. Shape validation and semantic review around `05:58–06:05` still accept the result.
- **Paper claim**: Paper p2–3 states that generated code and published values should be grounded in or derived from current task data. This remains in unexplained tension with the single demo screen.
- **Reviewer inference**: The demo establishes only that runtime derivation was not demonstrated. It cannot be generalized into a claim that all Team 1286 solutions are hardcoded. Deterministic code, a shape validator, and a reviewer are insufficient to prove source derivation.
- **A/B decision**: **Adapt / Adapt**. For A, replace the flow with experiment validation, recomputation, and system mapping. For B, replace it with signal, breakpoint, deployed-change, and disconfirmation. Numeric execution requires a source-read derivation receipt listing actual source reads, query/locator, snapshot/version, and input/output digest. An empty numeric read set fails. Do not copy the KDD answer flow.

#### T1286-4. Claim-gated publication and focused continuation

- **Practice**: The publisher releases only output whose evidence status is supported. If feedback affects an earlier answer, rebuild only the affected contract, evidence, plan, and code, then pass the same gate again.
- **Evidence anchor**: Contract gate: Paper p3, p17, p19. Focused continuation: Paper p5, p13, **paper-only**. Video `03:19–04:00,04:20–04:53` summarizes memory and feedback but does not fully demonstrate continuation.
- **Problem addressed**: Prevents unsupported claims from being published and prevents direct human edits to the final artifact from bypassing the audit.
- **Evidence strength**: Medium. The authors explicitly state that the gate cannot prove an answer correct; focused continuation is not demonstrated on video.
- **A/B decision**: **Adapt / Adapt**. An A proposal requires both metric evidence and exact code evidence. A B attribution requires effective time, scope, mechanism, contradicting evidence, and a falsifier. Recompute when the metric definition, window, or runtime identity changes. Open HIGH risk, contradiction, zero source reads, or a material gate timeout must propagate to the publication gate and block publication, not merely display a badge.

#### T1286-5. Memory for navigation only; least privilege; complete traces and hard budgets

- **Practice**: Memory is scoped and requires explicit pin/edit; it only directs where to look. Generated execution is constrained by allowlists and isolation. Traces store tokens, runtime, and failures, with phase timeouts, repair caps, and abstention.
- **Evidence anchor**: Memory: Paper p2–3, p13; Video `03:19–04:00,04:20–04:53`. Permissions: Paper p2, p5, p9, **paper-only**. Budgets/traces: Paper p4–6, p10–11, p16, p20–23, **paper-only**.
- **Problem addressed**: Prevents memory from posing as fact, generated code from exceeding authority, and failures or costs from remaining invisible.
- **Evidence strength**: Medium-strong. The mechanisms and author-reported trace statistics are checkable; they are not an A/B SLA. The video's claim that memory improves performance has no controlled experiment and cannot support a causal conclusion.
- **A/B decision**: Memory **Adapt / Adapt**; least privilege and traces/budgets **Adopt / Adopt**. Production uses scoped, read-only metric/SCM/deploy/flag APIs, not a general shell or filesystem.

#### T1286-6. Explicit rejections

- **Automatically apply benchmark gold learning to live diagnosis: Reject / Reject.** The mechanism appears only in Paper p3, p6, **paper-only**. Live A/B has no clean gold; this is limited to offline, human-gated policy evaluation.
- **Use KDD coverage or a seeded demo to prove production reliability: Reject / Reject.** Paper p4–6, p10–12; Video `00:59–07:21`. Input coverage and a UI demo do not establish diagnostic correctness.
- **Treat 17 skills as requirements: Reject / Reject.** Paper p3–4, p14; Video narration `06:48–07:14`; "17 open Markdown skill files" appears only on screen at `06:50–07:20` and is **visual-only**. The failure-mode policy may inform the design; the catalog is not copied.

#### T1286-7. Critical capability gap

PiTrace's evidence graph targets an uploaded workspace and benchmark answers. It lacks production telemetry, experiment validity, a deploy/config/flag/model/data timeline, an exact deployed SHA, and rollback evidence.

- **Evidence anchor**: Paper p1–6, p17–19; the source-to-answer flow shown in Video `01:30–06:40`. See [`creative-team1286-practices.md`](creative-team1286-practices.md) for the research report's complete boundary analysis.
- **Evidence strength**: Strong. Neither source supplies the required production evidence plane. Its absence does not show that the authors' system can never have this capability, but the current materials do not support claiming that it does.
- **Design conclusion**: Adopt only the principles of a shared evidence state, human gate, deterministic control, and tracing. The greenfield design still requires an independently designed code/runtime evidence plane. It is not a PiTrace compatibility layer.

### 4.4 Creative Track Team 1401: Data Agent Studio

The only primary source is the complete `08:32.48` video, SHA-256 `b50c79b6be38c8344e890eefac7f7c15d2bb946dbc471c4f38ed082bd07fbf34`. There is no Team 1401 paper. This entire section is `video-only`. The video UI can establish what the interface displays; without source code, a server receipt, or a benchmark record, it cannot establish backend enforcement, accuracy, or production readiness.

#### T1401-1. Inspectability: visible plan, action, raw input, result, and evidence

- **Practice**: The UI displays a structured plan, tool activity, raw input, results, and exact SQL evidence.
- **Evidence anchor**: Video `01:07.54–01:23.54,06:00.78–06:21.18,06:37.46–06:44.22`.
- **Problem addressed**: Allows analysts and incident commanders to inspect what the agent did, where values came from, and which step failed.
- **Observed**: The UI displays a plan, Event Log, result, and SQL. The first user prompt already specifies `shop.db`, `order_items JOIN products`, `qty * price`, the output columns, and sorting; the Event Log shows only one `execute_context_sql` call.
- **Speaker claim**: The narration says Autopilot independently decomposes, writes, and runs the join.
- **Reviewer inference**: This run does not establish autonomous decomposition, join discovery, or a four-table execution path. A and B may adopt inspectability, but the plan UI is not proof of agent capability or complete chain-of-thought.
- **A/B decision**: **Adopt principle / Adopt principle**. A displays experiment validation, recomputation, segment loss, production path, and deployed diff. B displays the signal, changepoint, change timeline, deploy proof, and contradicting evidence.

#### T1401-2. Exact query and independent validator

- **Practice**: Preserve the exact SQL beside a numeric answer. The narration says the result agrees with a direct SQL check.
- **Evidence anchor**: Video `06:12.02–06:21.18,07:41.94–07:54.14`.
- **Problem addressed**: Prevents the LLM from rewriting values and makes joins, filters, and parameters reviewable.
- **Observed**: Exact SQL is visible beside the result; the specific run shows only one SQL execution.
- **Speaker claim**: The narration says the result agrees with a direct SQL check; the summary separately says "4 tables." There is no independent check query or receipt, and the specific prompt requires only a two-table join.
- **Reviewer inference**: One reviewable SQL statement does not establish autonomous decomposition, a four-table path, or independent validation. Code must store the query, parameters, result digest, row count, truncation, metric-definition version, and independent validation receipt. Correct SQL also cannot establish causality.
- **A/B decision**: **Adapt / Adapt**.

#### T1401-3. Server-side tool capability and risk-tiered approval

- **Practice**: The UI can enable or disable tools individually, and a custom tool can be marked `Requires approval`. Co-pilot can display raw input and request approval before an action.
- **Evidence anchor**: Video `03:15.22–03:53.22,06:21.18–06:54.98`.
- **Problem addressed**: Restricts irrelevant or high-risk tools and allows a human to inspect the target and input before a sensitive action.
- **Observed**: The UI and approval dialog are visible. The Tools panel also shows `execute_python` enabled by default and describes it as executing arbitrary Python in the task context directory.
- **Speaker claim**: The narration says the agent cannot call a disabled tool; server-side denial, authorization, schema enforcement, expiry, and replay protection are not shown.
- **Reviewer inference**: Tool registration must bind a server-side capability, read/write class, source allowlist, schema, timeout, budget, and authorization identity. Ordinary read-only queries run automatically; only access across sensitive sources, large scans, and production actions pause. B should not require approval for every safe read.
- **A/B decision**: Explicit tool control **Adapt / Adapt**; arbitrary Python by default **Reject / Reject**. If isolated analysis requires Python, it may run only without production credentials or network access, with read-only mounts, bounded resources, a short lifetime, and a complete receipt.

#### T1401-4. Session isolation and diff-before-write

- **Practice**: Each session has its own files, conversation, and settings. Before writing a clean copy, Data Doctor shows the code and before/after diff and waits for approval.
- **Evidence anchor**: Session: Video `00:54.14–01:07.54`. Diff-before-write: Video `04:05.50–04:32.30`.
- **Problem addressed**: Prevents experiment and incident contexts from crossing and makes the effect of an automated source change visible.
- **Evidence strength**: Medium/weak. UI isolation and the workflow are visible; storage/tenant isolation, repair correctness, and rollback are unverified.
- **A/B decision**: Session isolation **Adopt principle / Adopt principle**. Freeze identity, source manifest, authorization, time range, and tool/model versions for each case. Diff-before-write is **Adapt** only for a separate action lane; the diagnostic core remains read-only and does not directly clean production data.

#### T1401-5. Deterministic profiling and a document-evidence adapter

- **Practice**: Display column distributions, correlations, and missingness first. The PDF graph displays entities, relations, pages, and an evidence panel.
- **Evidence anchor**: Profile: Video `02:07.94–02:36.10,04:09.14–04:24.26`. PDF graph: Video `05:10.34–05:27.58`.
- **Problem addressed**: Finds data-quality problems before LLM interpretation and lets document extraction return to a source locator.
- **Observed**: The profile, KG, page pointer, and evidence panel are visible. The screen does not clearly establish a complete verbatim quote.
- **Speaker claim**: The narration says the profile uses no LLM and every relation includes a source-page quotation from the original text.
- **Reviewer inference**: A page pointer establishes only a location on a page; it does not establish quote completeness or that the source text supports the relation. An extracted relation must be marked inferred and cannot override the canonical source.
- **A/B decision**: **Adapt / Adapt**. A adds exposure, SRM, sample, window, and metric version. B adds freshness, logging, schema drift, and changepoint. Correlation can only generate a candidate. The document graph is auxiliary evidence and cannot override canonical metric/deploy/SCM sources.

#### T1401-6. Explicit rejections

- **Uploaded-files-only: Reject as-is / Reject as-is.** Video `01:47.18–01:52.56,08:24.34–08:28.32`. A and B require live metric/runtime/SCM/deploy/flag/model/data sources. Preserve least privilege but use allowlisted read-only adapters.
- **Use a column-name heuristic join as evidence: Reject / Reject.** Video `04:43.50–05:01.84,08:18.10–08:24.34`. At most, it is a candidate generator; validate it with a catalog, lineage, a type/uniqueness test, or owner confirmation.
- **Use a fixture built to join as proof that the heuristic generalizes: Reject / Reject.** **Observed**: The demo fixture was built for the ER demonstration and shares `customer_id`. **Speaker claim**: The narration says the system detected a cross-database link and acknowledges that it relies on a naming heuristic. **Reviewer inference**: A successful link is circular evidence and does not support generalization to unusual schemas or production lineage.
- **Use four competition routes—ReAct / DRAGIN / Multi-agent / Hybrid-B—as a design conclusion: Reject / Reject.** Video `02:59.50–03:15.22`. There is no route rule, A/B ablation, failure-recovery evidence, or cost evidence.
- **Arbitrary Python by default: Reject / Reject.** Video `03:15.22–03:33.54` visual-only. The UI shows it enabled by default but provides no isolation or escape proof. It cannot enter a diagnostic lane with production credentials or network access.
- **Treat polished UI, accounts, theme, or layout as core capabilities: Reject / Reject.** Video `00:33.44–01:37.14,03:55.60–04:05.50,06:54.98–07:33.10`. These may be peripheral product requirements, but they do not answer the causal questions in A or B.

#### T1401-7. Critical capability gap

The video demonstrates only two small data-analysis tasks with known answers. It includes no production repo, deployed SHA, deploy/config/flag/model/data timeline, experiment-validity analysis, SEV changepoint, counterfactual, or incident replay.

- **Evidence anchor**: Complete video timeline and limitations page `07:41.94–08:28.32`; see [`creative-team1401-practices.md`](creative-team1401-practices.md) for the complete evaluation.
- **Evidence strength**: Strong. The current video does not support a claim of A/B production diagnosis. The absence of a paper is not contradicting evidence, nor can material from other teams fill the gap by inference.
- **Design conclusion**: Adopt inspectability and controllability. Production provenance and causal discipline still come from the greenfield code/runtime evidence plane.

### 4.5 Old SMA evidence

Only specific practices are evaluated here. Legacy stages, modules, capsules, and contracts do not define the target architecture boundary.

#### S1. Validate the metric before attribution

- **Practice**: Check freshness and completeness. Detect a step change. Decompose segment contributions and mix shift.
- **Code anchor**: `.agents/skills/sma/scripts/anomaly.py:169,176-197,231`, symbols `check_data_quality`, `detect_step_change`; `.agents/skills/sma/scripts/decompose.py:136,182,222-239,266`, symbols `compute_aggregate_delta`, `decompose_by_dimension`, `compute_mix_shift`. SMA audit repo HEAD was `28cbbda6e4d4d7f08134952d38433e52d3ee8768`.
- **Problem addressed**: Prevents attribution from bad data, bounds the suspect window for B, and distinguishes mechanism change from traffic-composition change.
- **Evidence strength**: Medium-strong. Implementation plus unit tests, not proof of a production effect.
- **Conditions**: A uses treatment/control, query type, and population. B uses tenant, platform, and query class. Missing quality fields must be unknown, not trusted by default.

#### S2. Check holdout, SRM, and same-window controls first

- **Practice**: The experiment-diagnosis playbook checks exposure and comparison validity first.
- **Code anchor**: `.agents/skills/sma/references/playbooks/patterns/experiment_diagnosis.md:21,26-41`. A synthetic scenario is not production-effect evidence.
- **Problem addressed**: Prevents experiment-setup errors from being presented as product causes.
- **Evidence strength**: Medium. Verified playbook plus synthetic fixture; no real experiment result establishes the effect.
- **Conditions**: The greenfield design must connect to real experiment metadata and a metric receipt.

#### S3. Temporal-order gate

- **Practice**: Check whether a candidate cause precedes the metric effect.
- **Code anchor**: `.agents/skills/sma/scripts/diagnose.py:208,226-244`, symbol `check_temporal_precedence`.
- **Problem addressed**: Rules out impossible changes.
- **Evidence strength**: Medium-strong. Implementation plus unit tests; the old implementation parses dates from free text and can still pass when a date is missing.
- **Conditions**: Replace it with the structured comparison `deployed_at <= breakpoint`. An unknown result is inconclusive.

#### S4. Evidence, confidence, falsifier, and action contract

- **Practice**: Diagnostic output includes a probable cause, evidence, confidence/falsifier, and action.
- **Code anchor**: `.agents/skills/sma/SKILL.md:69-75`.
- **Problem addressed**: Makes recommendations reviewable and falsifiable.
- **Evidence strength**: Medium. This is a formal contract, not a production result.
- **Conditions**: An A action must connect to a file, symbol, diff, or test. A B suspect must connect to a commit, affected subsystem, and corroborating metric or log.

#### S5. Read-only queries, bounded post-validation repair, and traces

- **Practice**: Production queries use a read-only allowlist. A stage-validation failure gets one feedback repair. A missing artifact triggers a circuit breaker. The trace records duration, stages, retries, validation, queries, and artifacts.
- **Code anchor**: `.agents/skills/sma/scripts/query.py:104`, symbol `_validate_sql`; `.agents/skills/sma/scripts/pipeline.py:590-601` (bounded retry/circuit breaker), `:301-347` (symbol `_write_stage_trace`).
- **Problem addressed**: Limits production risk, prevents silent omissions, and preserves an execution record.
- **Evidence strength**: Medium-strong for the source implementation; the old trace records zero tokens and lacks a commit, diff, and query hash.
- **Conditions**: Preserve the safety and repair principles. Upgrade the trace into a claim-evidence graph. Do not copy the fixed legacy stage names.

#### S6. Critical capability gap in the old KDD and old SMA

Neither the old KDD nor the old SMA discovers production code/config/flag/model/data changes. At most, the old SMA maps a metric to a layer or event category. The KDD ledger records only the caller-supplied commit/environment; it neither discovers changes nor verifies that the commit is the production runtime. Neither system has a typed change inventory or a mapping from metric segments to production symbols.

- **Evidence anchor**: `KDD_Competition/kdd/trusted_run_ledger.py:31,110-161` (local source, not included), symbols `entry_from_manifest`, `build_entry`; `.agents/skills/sma/scripts/branch.py:87`, symbol `_git`, which serves only its own session branch; legacy tool surface `.agents/skills/sma/SKILL.md:41-75`.
- **Evidence strength**: Strong. The independent source-code audit checked the tool surfaces of both source trees.
- **Design conclusion**: The greenfield design must add a code/runtime evidence plane. It discovers and represents `code | config | flag | model | data` changes in one model, with `stable_id`, `effective_at`, scope, runtime identity, source link, and rollback state. This is a new target capability, not a legacy architecture migration.

## 5. Adopt / Adapt / Reject

`Adopt` means adopting the principle, not copying parameters. `Adapt` means preserving the mechanism while rewriting its inputs, outputs, or gates. `Reject` means excluding it from the target design.

| Candidate practice | A. Post-experiment | B. SEV | Decision, adaptation, and evidence strength |
|---|---|---|---|
| W1/K1 bounded, code-controlled evidence lifecycle | **Adopt** | **Adopt** | Jointly supported by workshop audio `00:45:00–00:48:00` and KDD source code. Shared lifecycle, different scenario policies. Strong. |
| W2/K4 mechanical gate before semantic reviewer | **Adopt** | **Adopt** | Jointly supported by workshop audio `00:48:00–00:51:20` and KDD source code. A checks exposure/SRM/math; B checks the breakpoint and change identity. Strong. |
| W6 typed schema that narrows by stage | **Adopt** | **Adopt** | Workshop audio `01:42:28–01:53:25` supports the mechanism; A/B evidence needs also support adoption. Strong. |
| K3 fail-open context filtering | **Adopt** | **Adopt** | Collapse only the default context; underlying evidence remains retrievable. Strong. |
| K2 fan-out after a structured plan | **Adapt** | **Adapt** | A partitions by mechanism/segment; B by deploy/service/code path. Each unit must be falsifiable. Strong. |
| W4 independent reviewer | **Adapt** | **Adapt** | Workshop audio `01:00:00–01:05:15` supports the mechanism and its instability. Check only claims/evidence; modified output must pass the gate again. Strong/medium. |
| W5/K6 selective fan-out/vote | **Adapt** | **Adapt** | KDD source code supports selective routing; workshop audio supports only selective budgeting within the competition, not A/B lift. |
| W5 broad voting | **Reject** | **Reject** | Workshop audio `01:02:25–01:05:15` and KDD source code both provide negative evidence. Reject as the default path. Strong. |
| K5 layered recovery | **Adopt** | **Adopt** | Bound transport, query, evidence, and reasoning retries separately. Strong. |
| K7 code-serialized evidence and traces | **Adopt** | **Adopt** | The LLM does not write raw values, commits, or diff identities. Strong. |
| W7 difficulty routing, approval, and budgets | **Adapt** | **Adapt** | Workshop audio `01:55:48–02:08:18` supports the mechanism. A prioritizes completeness; B prioritizes time-to-first-safe-action. Requires scenario-specific testing. Strong/medium. |
| W8 eligibility guard-removal ablation | **Adopt principle** | **Adopt principle** | Consensus cannot replace a deterministic guard. Workshop audio-only `01:30:00–01:39:31`. Strong for the demo; production lift unknown. |
| T1286 shared replayable evidence state | **Adapt** | **Adapt** | Add production metric/runtime/change identity. Paper p1–4, p17–19; Video `02:05–03:19`. Medium-strong. |
| T1286 human gate | **Adapt** | **Adapt** | Visual-only `fallback=continue` is fail-open. A material gate must fail closed and escalate. Paper p2, p13–14; Video `04:06–04:53`. Medium-strong. |
| T1286 deterministic control + bounded repair | **Adapt** | **Adapt** | One demo exposes hollow determinism; do not generalize it to all solutions. Numeric execution requires a source-read derivation receipt. Medium-strong, with a single-demo boundary. |
| T1286 claim gate, trace, and hard budget | **Adapt** | **Adapt** | Bind claims to production evidence; propagate HIGH risk, contradiction, zero source reads, and a material timeout to the publication gate. Medium-strong. |
| T1286 live gold learning | **Reject** | **Reject** | Limited to offline, human-gated evaluation. Paper p3, p6, paper-only. Medium. |
| T1286 use KDD coverage/seeded demo to prove reliability | **Reject** | **Reject** | A demo does not establish A/B diagnostic correctness. Paper p4–6, p10–12; Video `00:59–07:21`. Strong. |
| T1401 inspectable plan/action/result/evidence | **Adopt principle** | **Adopt principle** | The prompt specifies the join/formula/output; the UI does not establish autonomous decomposition. Video `05:43.28–06:21.18`. Video-only, medium. |
| T1401 exact query + validator | **Adapt** | **Adapt** | One SQL statement does not establish a four-table path or independent validation; an independent receipt is required. Video `06:12.02–06:21.18,07:41.94–07:54.14`. Medium/weak. |
| T1401 server-side tool capability | **Adapt** | **Adapt** | Replace the UI toggle with a backend capability, authorization, schema, and audit contract. Video `03:15.22–03:53.22`. Medium/weak. |
| T1401 risk-tiered approval | **Adapt** | **Adapt** | Ordinary reads are automatic; only high-risk sources/actions pause. B does not approve every read step by step. Video `06:21.18–06:54.98`. Medium. |
| T1401 case/session isolation | **Adopt principle** | **Adopt principle** | Freeze identity, manifest, authorization, and versions; separate UIs do not establish security isolation. Video `00:54.14–01:07.54`. Medium/weak. |
| T1401 uploaded-files-only | **Reject as-is** | **Reject as-is** | Replace with allowlisted live read-only adapters. Video `01:47.18–01:52.56,08:24.34–08:28.32`. Medium. |
| T1401 heuristic join as evidence | **Reject** | **Reject** | At most, generate a candidate for validation. Video `04:43.50–05:01.84,08:18.10–08:24.34`. Medium. |
| T1401 use a fixture built to join as proof of generalization | **Reject** | **Reject** | The fixture intentionally shares `customer_id`; a successful link does not establish heuristic generalization. Video-only, medium. |
| T1401 KG page pointer as proof of a quote | **Reject** | **Reject** | The page pointer is visible; a complete verbatim quote is only a speaker claim. Video `05:10.34–05:27.58`. Medium/weak. |
| T1401 arbitrary Python by default | **Reject** | **Reject** | Visual-only evidence shows `execute_python` enabled by default; there is no isolation or escape proof. Video `03:15.22–03:33.54`. Medium. |
| T1401 four competition agent routes | **Reject** | **Reject** | No A/B ablation, route rule, cost evidence, or failure evidence. Video `02:59.50–03:15.22`. Weak. |
| T1401 polished UI as a core capability | **Reject** | **Reject** | The UI is a peripheral product surface, not a causal evidence plane. Video-only. Medium. |
| S1 metric gate, step change, and mix shift | **Adapt** | **Adapt** | Adopt the deterministic algorithms, recalibrate thresholds, and do not let unknown pass. Medium-strong. |
| S2 holdout/SRM/same-window controls | **Adopt** | **Conditionally adopt** | Enable for B only when the incident involves an experiment. Medium. |
| S3 cause-before-effect | **Adopt** | **Adopt** | Replace with structured runtime/deploy time. Unknown is inconclusive. Medium-strong. |
| S4 falsifiable action contract | **Adapt** | **Adapt** | Require links to production code and targeted validation. Medium. |
| S5 read-only query and bounded repair | **Adopt** | **Adopt** | Do not copy legacy stage names. Medium-strong. |
| Old SMA trusts missing quality fields by default | **Reject** | **Reject** | Anchor: `.agents/skills/sma/scripts/anomaly.py:176-197`. Missing evidence should be unknown. Strong. |
| Old SMA may pass with a missing date | **Reject** | **Reject** | Anchor: `.agents/skills/sma/scripts/diagnose.py:226-244`. Strong. |
| Fixed requirement for 3 hypotheses | **Reject** | **Reject** | Anchor: `.agents/skills/sma/scripts/validate.py:284-312`. Determine the count dynamically from unresolved causal branches. Strong. |
| Legacy fixed linear stages and 3 PAUSE points | **Reject** | **Reject** | Anchor: `.agents/skills/sma/scripts/pipeline.py:18-27,603-617`. Requirements determine the route. Strong. |
| Treat the old SMA branch helper as production code intelligence | **Reject** | **Reject** | `_git` at `.agents/skills/sma/scripts/branch.py:87` serves only its own session branch. Strong. |
| Make KDD video/ASR/doc-to-SQLite part of the core | **Reject** | **Reject** | Use as an adapter only when the input has the corresponding modality. Strong. |
| KDD `prediction.csv` and scorer | **Reject** | **Reject** | Replace with a claim/evidence/action artifact. Strong. |
| KDD demo-shaped hardcoded fastpath | **Reject** | **Reject** | `KDD_Competition/kdd/runner.py:699-836,1047-1117,2939-3030` (local source, not included). Preserve only rules supported by a formal metric/production contract. Strong. |
| Fixed votes, attempts, requests, and concurrency | **Reject** | **Reject** | Determine from measured quality, coverage, cost, and p95 latency. Strong. |

## 6. Greenfield design

This section states only vendor-neutral logical requirements. It selects no architecture, vendor, language, storage, or agent framework and authorizes no implementation.

### 6.1 Shared evidence-first core

This is neither the old SMA module map nor a KDD clone.

1. **Frame**: Fix the scenario, identity, question, time window, and success criteria.
2. **Collect**: Use server-side, allowlisted, read-only capabilities to retrieve metric, experiment, runtime, and `code | config | flag | model | data` change inventories. Every object includes a source id, stable identity, freshness, authorization, and receipt.
3. **Verify signal**: Deterministically check freshness, completeness, math, exposure, SRM, breakpoint, and identity.
4. **Build evidence map**: Connect metric segments, runtime versions, code, config, flags, models, data, deploys, and dependency changes. Connect code changes to commits, diffs, and code paths.
5. **Generate falsifiable hypotheses**: For each hypothesis, record expected observations, support, contradictions, and gaps.
6. **Route investigation**: Use one path for simple tasks. Fan out only for low confidence or multiple independent evidence paths.
7. **Test and prove derivation**: Run a read-only query, counterfactual slice, targeted test, or rollback/canary evidence check. A numeric execution receipt must list actual source reads, query/locator, snapshot/version, and input/output digest; zero source reads fail immediately.
8. **Review**: Run a deterministic claim gate first, then use a fresh-context reviewer to check whether the explanation exceeds the evidence. Consensus cannot replace eligibility, scope, interval, or runtime-identity guards.
9. **Publish**: Code writes the immutable evidence table. The model writes a cited explanation, confidence, falsifier, and action. Open HIGH risk, contradiction, zero source reads, or a material human-gate timeout must fail closed and enter explicit escalation; a badge alone cannot permit continuation.
10. **Trace and inspect**: Store and display the source manifest, structured plan, raw tool input/result, route, repairs, tokens, cost, wall time, errors, and artifact hash. Redact sensitive raw evidence.

### 6.2 A policy: Post-experiment

Priority order:

1. experiment identity and metric trust;
2. expected mechanism;
3. overall and segment delta;
4. mix shift and within-segment effect;
5. serving path, flag/config, and metric instrumentation;
6. code-backed explanation;
7. change proposal and targeted validation.

Minimum output shape:

```text
finding -> metric evidence -> mechanism -> code evidence
        -> confidence -> falsifier -> proposed change -> validation
```

Without code evidence, the output can only be a "metric-level hypothesis." It cannot claim to be tied to production code.

### 6.3 B policy: SEV

Priority order:

1. confirm the drop and affected population;
2. locate the breakpoint;
3. retrieve the window of code/config/flag/model/data changes around the breakpoint;
4. first eliminate changes that are temporally impossible or do not intersect the affected path;
5. for remaining changes, inspect the diff, runtime reachability, logs, and corroborating metrics;
6. produce a safe action early while continuing to validate causality.

Minimum output shape:

```text
suspect change -> change_type -> effective_at -> affected path -> supporting evidence
               -> contradicting evidence -> confidence -> safe action
```

"Close in time" supports only candidate generation. Confidence may increase only when mechanism, path, and observation all support the change.

### 6.4 Repair, fan-out, cost, and stopping conditions

- Transport failure: Retry the original request a limited number of times. Do not repeat the reasoning.
- Query failure: Repair only the query. Preserve the original error and query receipt.
- Evidence gap: Change the source or request the missing identity. Do not guess.
- Reasoning conflict: Start an independent path only for the unresolved branch.
- Reviewer conflict: Return to the raw evidence for the claim; do not substitute voting for verification.
- A optimizes its budget for a complete, falsifiable explanation.
- B optimizes its budget for time-to-first-safe-action, then increases confidence in the cause.
- When the budget is exhausted, identity is unclear, or evidence conflicts cannot be resolved, stop and return `inconclusive`, the coverage gap, and the smallest next action.

### 6.5 Evaluation before scale-up

Create separate, real, de-identified task sets for A and B. Fixture replay alone is insufficient.

Measure at least:

- metric math correctness;
- correct experiment/runtime/repo/commit identity;
- code-link precision and recall;
- unsupported causal claims;
- action usefulness;
- coverage;
- repair success;
- tokens, cost, median latency, and p95 latency;
- selective fan-out trigger rate and same-batch lift.

Run a single-path baseline first. Then add the reviewer, fan-out, or voting one at a time. Reject any addition with no same-batch quality lift or whose lift does not justify its cost and latency.

## 7. Competition-specific warnings

- The Champion's `VIDEO_RESULT_VOTE_ROUNDS=5`, `SOLVER_REQUEST_LIMIT=80`, `MAX_ATTEMPTS=5`, and task concurrency 16 are competition parameters. Anchor: `zhezh/kddcup2026_champion@bdc874fc4260e3565ae0dce041728fdf5b376709/src/data_agent_baseline/zz_agent_v2.py:116-137`.
- Video, ASR, OCR, hiccup layout, and doc-to-SQLite are input-specific. Structuring and provenance are reusable; the specific media pipeline is not.
- `prediction.csv`, the scorer, and the 12-hour constraint are competition contracts, not contracts for the new agent.
- The local KDD record lacks clean source50/Docker50 evidence for K=3/deliberation; commit `51a712a0b89f88316be9b55a4df1dbc355e7185e` is NO-GO. The presence of source code does not make a practice successful.
- `KDD_Competition/docs/source-map.md:65-123` (local source, not included) records 44 overlay domains. A fixed benchmark fastpath is prone to overfitting.

## 8. Evidence limitations

- `fable-opus-audit.md` is reviewer audit input, not a primary fact source. Its architecture, P0/P1, and selection judgments are reviewer inferences. This refresh synchronizes only evidence corrections that can be checked against the paper, video, or workshop audio.
- The untimestamped low-confidence Mac Voice Memos ASR candidate (raw attachment not included for privacy and source availability) contains obvious recognition errors. It is only an index of candidate terms, not a factual source. During indexing, obvious ASR variants may be normalized to `Qwen3.5`, `DuckDB`, `SQL generation`, `Docker`, `packet-size keyframes`, `record universe`, `solver.py`, `CER/WER`, and `HTML-like layout`; do not copy `Queen`, `dark DB`, `circle`, `talk`, or `WEI`. Values supported only by this ASR, including `0.65/0.69` and `25c/35c`, remain marked `unresolved`.
- Team 1286 is included. Its paper and video establish control mechanisms and a demo path, not A/B production effects.
- Team 1401 is included, but its only primary source is a video. There is no paper, source code, server receipt, or benchmark record. UI displays and speaker claims cannot be extrapolated into backend enforcement, production readiness, or A/B accuracy.
- The Team 1286 and Team 1401 videos are independent Creative Track materials, not part of the workshop meeting audio. They must not be mixed into the meeting transcript, audio-timestamp alignment, or speaker attribution.
- Workshop alignment covers intro, workshop, and aggregate 100%. `meeting-audio-alignment.md` is an ASR-assisted, faithful summary in Chinese, not a transcript, and it has no manual speaker diarization.
- Time mapping and topic-level cross-alignment are complete for 73/73 screenshots. They are only a subset of the slides; topic-level alignment cannot be presented as verbatim speech verification. Missing screenshots are not negative evidence, and audio-only segments are fully preserved.
- Explicitly low-confidence segments remain marked "unconfirmed": workshop `01:07:09–01:07:58`, `01:08:28–01:09:45`, `01:16:59–01:17:11`, `01:24:51–01:25:21`, `01:32:28–01:33:15`, `01:41:03–01:42:21`, `01:46:52–01:47:32`, `02:09:00–02:09:15`, `02:12:18–02:13:15.560`.
- Workshop audio `02:05:20–02:08:18` explicitly discloses limits in external validity, difficulty/modality confounding, and system stability. Competition results cannot be extrapolated directly to production.
- Only the repo README claims the Champion ranking; the official leaderboard was not checked in this research.
- KDD source code establishes that the mechanisms exist, not that they work for A or B.
- The old SMA implementation and unit tests establish deterministic behavior, not production-diagnosis success.
- `.agents/skills/sma_rewrite/evals/tests/test_dry_run.py:1-5` is fixture replay; `.agents/skills/sma_rewrite/evals/fixtures/ablation_llm/README.md:37-47` also explicitly states that a synthetic fixture cannot replace a real LLM signal.
- The final decisions therefore depend on whether a practice meets the evidence needs of A and B and on future same-batch evaluation, not on a reference system's reputation or compatibility cost.

## Top practices

1. Establish the metric before discussing the cause.
2. Control the evidence lifecycle with code. The model handles only uncertain nodes.
3. Create a code/runtime evidence plane that links the metric to code, config, flag, model, and data changes and validation in a shared, replayable evidence state.
4. Put mechanical gates before the semantic reviewer.
5. Filtering narrows only the default context; it does not delete underlying evidence.
6. Repair failures by layer, with a bounded budget for each layer.
7. Fan out only low-confidence, high-value branches. Reject broad voting.
8. Code writes values and identities. The model writes only cited explanations.
9. Humans can inspect the plan, tool inputs/results, and evidence. Approval is risk-triggered; safe reads do not all pause.
10. A optimizes for a complete causal explanation. B optimizes for time-to-first-safe-action. Without code/runtime evidence, state explicitly that the production cause is unconfirmed.
