# KDD 2026 Fourth-Place Repository Reverse Audit

Date: 2026-08-11

Status: Source audit complete. Research only. This is not approval of a new Data Agent design.

Repository: `kekshibata/kddcup2026-data-agents-4th-place-solution`

Default branch: `main`

Fixed release audit SHA: `ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a`

Phase 2 image source commit: `13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65`

## Canonical-Policy Supersession

This fixed-SHA reverse audit preserves its source facts, author claims, and reviewer inferences. It was written before the owner-confirmed policy resolution, however, so its former single-axis shorthand is historical only. The authoritative replacement is the [closed canonical domain and policy contract](wayfinder/freeze-canonical-domain-policy-contracts.md).

For the current target, use independent state dimensions: Evidence/Claim state (where `observed` belongs only to direct validated Evidence or an `observed_fact` Claim), Cause Verdict (`unassessed | suspected | confirmed | ruled_out | inconclusive`), Recommendation Readiness (`not_applicable | blocked | proposal_ready | action_ready | rejected`), Action Approval, and Incident State. `action_ready` is not a verdict, and neither it, `confirmed`, a human ruling, nor recovery authorizes mutation. “Observed source fact,” “not observed,” and similar labels elsewhere in this audit remain source-audit labels, not product-state enums.

## Executive conclusion

The core of this solution is not “many agents holding a meeting.”

It is one main agent divided by code into four intended stages:

```text
prepare inputs
  -> PLAN
  -> EXPLORE
  -> ANSWER
  -> VERIFY
  -> write prediction.csv
```

A ring of narrow helpers performs domain classification, formula advice, column filtering, document extraction, video summarization, and answer selection. These helpers do not jointly maintain a strict evidence ledger. Most add hints for the main agent or rewrite the final table.

The most useful lessons are not its finance or EHR rules. They are:

1. Enforce stages and tool scope in code.
2. Unify heterogeneous data before the agent queries it.
3. Preserve failed experiments and compare them with one scorer.

It is not a suitable production foundation for our target.

It has no deployed identity contract. It has no production change discovery. It has no case lifecycle, append-only evidence, invalidation, or Gate 0–7 contract. In particular, it does not implement the current separation of Evidence/Claim state, Cause Verdict, Recommendation Readiness, Action Approval, and Incident State.

The README's broad “fail-closed” framing holds only for some rules. The source has material fail-open behavior:

- Domain, PDF, video, advisor, and prose preprocessing errors allow execution to continue.
- The source router's `avoid` result is advisory, not a hard block.
- A schema-check exception does not block the answer.
- After two refinements, the answer is forcibly submitted.
- `confirm_answer` directly accepts the pending answer.
- Submission prewrites empty stubs, so a crash can leave a structurally valid CSV with no answer.

The Dockerfile is a critical execution contract. It selects the experiment, flags, worker count, step limit, timeout, and retry default that actually ship. This report separates release HEAD from the Phase 2 image and does not misstate post-competition harness changes as competition behavior.

Overall judgment: **Adopt the control-flow principles. Adapt the data and validation mechanisms. Reject the competition-style final adjudication and evidence model.**

## 1. Identity, method, and evidence boundary

### 1.1 Verified identity

- **Observed source fact**: The exact repository is `kekshibata/kddcup2026-data-agents-4th-place-solution`. Remote HEAD points to `main`. The fixed release audit SHA is `ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a`.
- **Observed source fact**: The fixed release commit timestamp is `2026-07-21T13:05:33+09:00`. Its message is `Public release: results README, MIT license`.
- **Observed source fact**: `phase2-final` is an annotated tag. Its tag object is `3c56d2fd0f86be75d2829099525a96da8f81bddf`. Its peeled commit is `13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65`. The commit message is `Add exp_172_ehr_distinct: domain-gated DISTINCT for EHR (v9)`. The `phase1-final` tag object is `38a1bc1dea9a8a19f70cbb57263a7911cdadc099`.
- **Author/README claim**: The README says Phase 1 placed first and Phase 2 placed fourth. It also says the two tags mark the exact submitted states. [README results and reproduction](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/README.md#L13-L18); [README tag statement](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/README.md#L77-L99)
- **Unknown / not proven**: This audit did not obtain an organizer-held image digest, runtime receipt, or execution log. It cannot independently prove that the bytes executed by the competition were identical to the repository tag.

### 1.2 Audit method and provenance

Release-architecture links are pinned to the fixed release SHA. Claims about the author-designated Phase 2 image are pinned separately to the peeled commit `13b17fcc...`. Release HEAD is later than the competition tag. The two are not interchangeable.

When README or diagrams conflict with source, source and executable contracts take precedence. README numbers are author claims. Repository leaderboards, experiment logs, and comments are useful historical records, but they are not independent replication.

Evidence labels used throughout:

- **Observed source fact**: Directly visible in source, configuration, or tests at a fixed SHA.
- **Author/README claim**: A statement by the author, README, presentation, comment, or repository experiment record.
- **Reviewer inference**: The Sol primary reviewer's judgment based on multiple source facts.
- **Unknown / not proven**: The available first-party material cannot establish the claim.

The primary audit was performed by Sol 5.6 at medium reasoning effort. One owner-authorized extraction subagent was opened with `gpt-5.6-terra` and `reasoning_effort=max` for bounded source, README, test, Docker, and UI fact extraction. The primary reviewer independently checked material anchors and made all final judgments. The Terra max agent did complete its extraction. It mistakenly spawned one derivative agent. That derivative was immediately interrupted and was not used as evidence. The mistake does not raise the evidence grade of any conclusion and means the run cannot be described as having had only one agent in existence throughout.

No network refresh was used for this English finalization. It is a language conversion of the completed fixed-SHA audit, not a new research pass.

## 2. Actual architecture

### 2.1 Plain-language view

The system reads one task. It exposes CSV, JSON, and SQLite inputs as DuckDB views. Optional PDF, prose, and video preprocessing occurs before the main loop.

One main model then usually follows four stages:

1. **PLAN**: Decide the expected column count and resolve question semantics.
2. **EXPLORE**: Inspect the catalog, run SQL, and read documents. The intended adjacent path requires at least three successful exploration calls.
3. **ANSWER**: Submit final SQL.
4. **VERIFY**: Run a differently written SQL cross-check. The same main model decides whether to confirm or rewrite.

A task can run in a subprocess with an outer timeout. The public Phase 2 final configuration uses one attempt. The runner still contains generic multi-attempt, early-stop, and adaptive-vote code.

The state machine has a defect. It forbids backward movement but allows forward stage skipping. `PLAN -> ANSWER` bypasses the three-exploration gate attached only to `EXPLORE -> ANSWER`. The four stages are the intended flow, not a contract that every run must traverse.

### 2.2 Docker is the competition execution entry point

- **Observed source fact**: The Phase 2 tag uses `python:3.10-slim`. It copies `pyproject.toml`, `uv.lock`, README, all of `src`, `submission`, and `data/external/domain_db`, then runs `python -m submission.main`. [Docker build path](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/submission/Dockerfile#L11-L42)
- **Observed source fact**: The image contains the entire `src/experiments` tree, not only `exp_172`. `EXPERIMENT_NAME=exp_172_ehr_distinct` selects the default execution path.
- **Observed source fact**: Docker forces `EXP172_EXPLORE_SHAPE=1`, `EXP172_PROSE_EXTRACT=1`, `EXP172_PROSE_GATE=1`, and `EXP172_EHR_DISTINCT=1`. Code defaults also enable answer shape, prose, video keyframe note, PDF preprocessing, source routing, anti-aggregation, the anti-aggregation SQL guard, and domain routing. [Docker flags](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/submission/Dockerfile#L145-L160); [code defaults](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/src/experiments/exp_172_ehr_distinct/flags.py#L49-L65)
- **Observed source fact**: Image defaults are `MAX_WORKERS=8`, `MAX_STEPS=64`, `TEMPERATURE=0.6`, `TASK_TIMEOUT_SECONDS=6000`, `SUBMISSION_BOARD=B`, and three preprocessing workers.
- **Observed source fact**: The Phase 2 tag explicitly sets `SUBMISSION_RETRY_EMPTY=0`. Second-pass empty-result retry code exists, but the submitted image default disables it.
- **Observed source fact**: The basic build script only runs `docker build`, `docker save | gzip`, and size reporting. It does not run tests, smoke checks, SBOM generation, signing, or digest read-back. [build script](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/submission/build.sh#L1-L26)
- **Observed source fact**: A separate release script can generate a sidecar manifest with a short Git SHA, image tag, platform, archive size, and local score. It does not calculate an image digest or archive SHA-256. [release sidecar](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/scripts/release_submission.sh#L99-L165)
- **Observed source fact**: Runtime `submission_manifest.json` records only experiment, task counts, preprocessing, and retry state. It lacks Git SHA, image digest, and archive identity. [runtime manifest](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/submission/main.py#L715-L752)
- **Observed source fact**: `.dockerignore` excludes `.env`, VCS files, artifacts, tests, and most data, but allowlists `data/external/domain_db`. [image include/exclude](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/.dockerignore#L1-L69)
- **Observed source fact**: Because Docker copies all of `src`, the Phase 2 image contains 114 `python_exec.py` files that directly execute supplied Python with full `__builtins__`. For example, `exp_001` changes to the task context and calls `exec(code, namespace, namespace)`. [dormant Python executor](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/src/experiments/exp_001_react_baseline/tools/python_exec.py#L72-L105)
- **Observed source fact**: The entry point reads `EXPERIMENT_NAME` from the runtime environment and dynamically imports that package. Docker defaults to `exp_172_ehr_distinct`, while its comment says evaluation runtime may override knobs. [runtime experiment selection](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/submission/main.py#L38-L44); [Docker override note](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/submission/Dockerfile#L44-L45)
- **Observed source fact**: The default final `exp_172` registry does not expose a general Python tool. The executors above are dormant image attack surface, not evidence that the public final path used arbitrary Python.
- **Reviewer inference**: A production image should package only the selected runtime closure. Experiment identity should be fixed server-side. More than 100 old experiments should not ship in a switchable root container.
- **Unknown / not proven**: There is no competition runtime receipt. The audit cannot prove whether organizers allowed an `EXPERIMENT_NAME` override or whether a dormant executor was reachable or called.
- **Observed source fact**: The image also copies `data/external/domain_db`. At the fixed Phase 2 commit, only old experiments `exp_126` and `exp_127` reference it. `exp_172` and the submission path do not.
- **Reviewer inference**: `domain_db` is likely dead baggage in the final image. It expands image contents without adding a visible capability to the default path.
- **Reviewer inference**: Dockerfile is closer to the real execution surface than README, but it is still not a deployed-identity receipt.
- **Reviewer inference**: Dockerfile alone cannot reproduce the image bit-for-bit. The base image is not digest-pinned. Apt packages are unpinned. Although `uv.lock` is copied, installation uses `uv pip install --system -e .`, while project dependencies use `>=` or no version constraint; there is no `uv sync --frozen`. [install line](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/submission/Dockerfile#L25-L36); [dependency ranges](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/pyproject.toml#L11-L33)
- **Reviewer inference**: Dockerfile has no non-root `USER`, `HEALTHCHECK`, or resource sandbox. That may be acceptable for a competition. It should not be copied into production.
- **Unknown / not proven**: No organizer-held image digest was obtained. Build-time base layers, resolved dependencies, and the uploaded tar cannot be proven to match the tag source.
- **Unknown / not proven**: The fixed tag tree contains no committed tar, sidecar manifest, upload receipt, or digest artifact. A release-script capability does not prove that it was used for v9 or that its output was the image executed by organizers.

### 2.3 Code responsibilities

| Component | Actual responsibility | Evidence label | Main anchor |
|---|---|---|---|
| `submission/Dockerfile` | Select image contents, default experiment, flags, budgets, and entry point | Observed source fact | [Phase 2 v9 Docker contract](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/submission/Dockerfile#L128-L162) |
| `submission/main.py` | Find tasks, prewrite stubs, schedule concurrently, optionally retry empty results, write manifest | Observed source fact | [tag entrypoint env and stub](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/submission/main.py#L38-L110); [tag task batch](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/submission/main.py#L277-L324) |
| `runner.py` | Assemble preprocessors, advisors, main agent, subprocess timeout, and attempt aggregation | Observed source fact | [`_run_single_task_core`](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/runner.py#L339-L544); [attempt runner](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/runner.py#L547-L725) |
| `PhasedReActAgent` | Main staged loop, phase tool allowlist, step recording, stopping | Observed source fact | [phase validation](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/phased_agent.py#L41-L116); [run loop](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/phased_agent.py#L267-L470) |
| Unified DuckDB | Turn structured files into one query surface, isolate each thread's connection | Observed source fact | [data layer](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/tools/duckdb_unified.py#L1-L15); [connection isolation](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/tools/duckdb_unified.py#L27-L34) |
| Domain router | Rule-based classification from filenames, knowledge IDs, and schema names | Observed source fact | [`rule_classify` / `classify_domain`](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/domain_router.py#L98-L185) |
| Advisors | Formula and anti-aggregation hints, optionally concurrent | Observed source fact | [`_run_advisors`](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/runner.py#L289-L313) |
| Prose/video helpers | Document extraction, PDF cache, keyframe note, video summary | Observed source fact | [preprocess assembly](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/runner.py#L371-L499) |
| Answer auditors | Run final SQL, apply heuristic hard guards, let an LLM remove columns, require self-review | Observed source fact | [`answer_from_sql` flow](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/tools/registry.py#L364-L383); [result, review, forced commit](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/tools/registry.py#L508-L691) |
| Adaptive vote | For multiple attempts, choose by subset, numeric agreement, majority, or union | Observed source fact | [`adaptive_vote`](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/adaptive_vote.py#L249-L290) |

### 2.4 It is not a multi-agent evidence system

- **Observed source fact**: The main reasoning path is one continuous conversation. Each turn rebuilds a phase-specific system prompt while retaining earlier assistant responses and tool observations. [message assembly](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/phased_agent.py#L226-L265)
- **Observed source fact**: Most helpers return text, classifications, or rewritten columns. They do not jointly write a typed, append-only evidence graph.
- **Reviewer inference**: “One staged main agent surrounded by narrow helpers” is accurate. “A collaborative multi-agent evidence system” overstates the source.

## 3. Per-task execution flow

### 3.1 Intake and preprocessing

1. Submission finds `/input/task_*` directories.
2. It first writes a header-only `prediction.csv` stub for every task.
3. The runner reads the task and context.
4. Structured files are loaded into DuckDB.
5. Docker flags enable domain routing, PDF caching, a video keyframe note, formula advice, anti-aggregation advice, and prose extraction. Raw video summary and the `watch_video` tool are among the levers not enabled by default.
6. The runner builds the preamble and tool registry, then creates the main agent.

- **Observed source fact**: Domain, PDF, video-note, and advisor paths frequently catch exceptions and continue with an empty value or warning text. [runner preprocessing](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/runner.py#L352-L424)
- **Reviewer inference**: This preserves coverage in a competition. It is unsafe for production root-cause analysis. Missing evidence cannot be silently converted into “no such evidence.”

### 3.2 PLAN

- Available tools are `list_context` and `complete_phase`.
- The prompt asks for expected column count, semantic choices, and descriptor choices.
- Runtime forbids backward stage transitions.
- Runtime does not forbid skipping forward. `complete_phase(next_phase="answer")` can move directly from PLAN to ANSWER.
- The plan remains model-authored thought. Code checks the stage and tool, not whether every plan field exists or is correct.

Evidence: [PLAN prompt and tool list](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/prompt.py#L249-L274); [phase progression check](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/src/experiments/exp_172_ehr_distinct/phased_agent.py#L74-L113)

### 3.3 EXPLORE

- Available tools cover file listing, catalog inspection, SQL, document reads, grep, and stage transition.
- The intended adjacent path requires at least three successful designated exploration calls before moving from EXPLORE to ANSWER. A forward skip can bypass this gate.
- If `watch_video` is enabled and a video exists, the path requires one successful watch.
- The counter only shows that a tool returned `ok`. It does not show that the correct source was read or that the result was complete.

Evidence: [EXPLORE prompt](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/prompt.py#L276-L303); [minimum gate](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/phased_agent.py#L96-L112); [counter update](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/phased_agent.py#L430-L441)

### 3.4 ANSWER

- The main agent is expected to call `answer_from_sql`.
- Final SQL has no row cap. Exploration SQL does.
- A string-prefix allowlist accepts only `SELECT`, `WITH`, `PRAGMA`, `DESCRIBE`, `SHOW`, and `EXPLAIN`.
- Some rules are code-enforced blocks, including selected aggregate shapes, percentages, `DISTINCT`, and empty results.
- Other rules exist only in prompts or LLM audits. They are not deterministic proof.

Evidence: [read-only prefix check](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/tools/duckdb_unified.py#L273-L321); [ANSWER prompt](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/prompt.py#L305-L335)

### 3.5 VERIFY

- Runtime automatically enters VERIFY when `answer_from_sql` returns `review_required`.
- The prompt asks for another SQL formulation as a cross-check.
- The main agent itself writes PASS or VIOLATION.
- `confirm_answer` directly commits the most recent pending answer.
- After two refinements are exhausted, another `answer_from_sql` call forcibly commits.

Evidence: [automatic transition](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/phased_agent.py#L443-L457); [VERIFY prompt](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/prompt.py#L337-L365); [forced commit and confirm](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/tools/registry.py#L608-L719)

### 3.6 Timeout, retry, vote, and write-out

- A spawned process executes each task. The parent terminates it after the deadline and kills it if needed.
- The runner can execute several attempts concurrently and can stop early on an answer signature.
- When answers exist, generic code can run adaptive voting. When none exists, it returns a failure payload.
- Submission atomically writes the answer to `prediction.csv`.
- The runner supports an empty-prediction second pass. The Phase 2 Docker default disables it. Release HEAD later enabled it by default and added AUTO board and wave-aware budgeting.

- **Observed source fact**: Fixed-release `exp_172` sets `_ATTEMPT_TEMPS` to `(0.6,)`. The Phase 2 final path therefore uses one attempt. Vote code exists, but one attempt has no consensus effect. [runner attempt configuration](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/runner.py#L49-L71)
- **Reviewer inference**: The repository cannot support the causal statement “fourth place came from three-way voting.” The public final configuration contradicts it.

## 4. State and evidence flow

### 4.1 What it saves

- `AgentRuntimeState` stores steps, answer, and optional log probabilities.
- Each step stores thought, action, input, raw response, observation, and `ok`.
- The runner writes trace, route, prompt, preamble metadata, and attempt records.
- Submission writes an overall manifest.

Evidence: [runtime state](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/runtime.py#L10-L60); [runner metadata](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/runner.py#L500-L544)

### 4.2 What it does not save

- **Unknown / not proven**: No source-read receipt schema was found.
- **Unknown / not proven**: No stable `evidence_id` plus content digest connects every read, query, and result.
- **Unknown / not proven**: No append-only evidence ledger was found.
- **Unknown / not proven**: No evidence invalidation, supersession, or promotion mechanism was found.
- **Unknown / not proven**: No case-level authorization manifest was found.
- **Unknown / not proven**: No executable lineage links a final cell to an exact row, document span, video frame, and query receipt.

- **Reviewer inference**: Step trace is useful for debugging. It is not a production evidence packet. `ok=true` does not prove that evidence was read, complete, or valid.

### 4.3 Graph UI: not observed

This section provides research judgment only. The owner has not confirmed an evidence-graph product contract. This report does not decide it for the owner and does not freeze a final specification.

#### What was actually visible

- **Video observed**: Meeting screenshots identify the presentation as Leverages / Team 1418, with Oki Shibata as speaker. The screenshots support `PLAN -> EXPLORE -> ANSWER -> VERIFY`, `answer_from_sql`, SQL-executable answers, and bounded repair. No verifiable timestamp or frame number is available. Conference ASR is unreliable for proper names. This is not graph-UI evidence. Repository identity and implementation remain grounded in the fixed-SHA source.
- **Author/presentation claim**: The candidate title is *Phase-Gated ReAct in Improving the Reliability of Multimodal Data Agents*. The speaker claims first place in Phase 1, fourth place in Phase 2, and a Merit Award. This must not be confused with Team 1688 or Team 1401. Without an organizer-signed transcript, these remain author claims.
- **Repo observed**: `docs/PHASE_2_CURRENT_METHOD_EXP149.md` contains Mermaid flow, state, and sequence diagrams. They show task load, preprocessors, advisors, the main agent, `PLAN -> EXPLORE -> ANSWER -> VERIFY`, source routing, and answer review. [exp149 overall flow](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/docs/PHASE_2_CURRENT_METHOD_EXP149.md#L25-L51); [exp149 state diagram](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/docs/PHASE_2_CURRENT_METHOD_EXP149.md#L217-L230)
- **Reviewer inference**: These Mermaid edges describe author-stated processing flow and state transitions. They are not per-case evidence edges. The document is explicitly a 2026-06-08 `exp149` snapshot and is not the complete `exp172` image contract.
- **Repo observed**: A read-only trace viewer has a `run × task` matrix. Rows are runs. Columns are tasks. Cells show scores, status, or live phase and step. Users can filter by run ID, status, tag, lever, and configuration text. [matrix build and filter](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/scripts/trace_viewer_v2.py#L670-L742)
- **Repo observed**: Users can click a run. Run detail shows task, score, progress, elapsed time, prediction, trace, anti-aggregation label, ASR status, and question. Clicking a task opens its detail. [run click and detail](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/scripts/trace_viewer_v2.py#L781-L855)
- **Repo observed**: Task detail has `overview | input | trace | output | raw` tabs. Overview shows question, artifacts, final SQL, prediction, and gold. Input shows the input snapshot, injected preamble, and four stage prompts. [task tabs and overview](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/scripts/trace_viewer_v2.py#L893-L1025)
- **Repo observed**: The trace tab lists steps in attempt order. Each shows phase, action, `ok`, action input, and observation. Users can toggle thought display and auto-refresh a live step log. [trace interaction](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/scripts/trace_viewer_v2.py#L1028-L1071)
- **Repo observed**: The backend assembles task detail from `trace.json`, `attempt_0.steps.log`, input snapshot, preamble, prediction, gold, and preprocessing artifacts. It reconstructs phase primarily from step order and action. [trace normalization](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/scripts/trace_viewer.py#L493-L541); [detail artifacts](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/scripts/trace_viewer.py#L544-L608)
- **Repo observed**: The static dashboard contains KPI cards, two progress images, and experiment/submission tables. It has no node-edge rendering. [static dashboard](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/site/index.html#L30-L127)
- **Not observed**: No interactive nodes, edges, groups, expand/collapse, graph filters, node-click evidence detail, causal timeline, claim-evidence graph, contradiction edge, or invalidation view was observed.
- **Observed source fact**: These research UIs are not in the Phase 2 submission image. Docker excludes `docs/`, `site/`, `artifacts/`, and `tests/`, and copies only manifests, README, `src`, `submission`, and `domain_db`. [Docker exclusions](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/.dockerignore#L19-L27); [docs/site/tests exclusions](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/.dockerignore#L53-L69)

#### How a graph is generated

- **Observed source fact**: The trace viewer is not a graph generator. It reads agent run artifacts and displays them by run, task, attempt, and step. It does not turn source extraction into typed nodes or create claim-to-evidence edges.
- **Observed source fact**: An old experiment named `exp_099_schema_graph_fallback` reads a precomputed cache. Its LLM-judged `joins[]` fields are `from`, `to`, `kind`, `confidence`, and `reason`. The code now makes `build_schema_graph_section()` return an empty string because all three hint formats hurt the author's experiments. [disabled schema graph hint](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_099_schema_graph_fallback/schema_graph.py#L1-L21); [disabled return and rationale](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_099_schema_graph_fallback/schema_graph.py#L45-L71)
- **Author claim**: The old experiment comments say schema hints induced forced joins or caused the agent to follow a low-context second opinion. This is an internal experiment record, not independent replication.
- **Reviewer inference**: The old schema cache is a set of mapping hints, not an evidence graph. The trace viewer is execution narration. Neither proves relationships among claims, evidence, and production changes.

#### What it genuinely helps a user answer

- **Reviewer inference**: The matrix helps answer “which run regressed on which tasks?”
- **Reviewer inference**: Task detail helps answer “what did the agent call, what went in and out, and which final SQL did it use?”
- **Reviewer inference**: Progress charts show experiment-score history. They do not explain a causal mechanism.
- **Reviewer inference**: Thought, step sequence, `ok` pills, and stage narration are debug trace, not evidence. Prediction versus gold is an evaluation result, not production causal proof.
- **Reviewer inference**: Drawing lines between these cards and steps would create an illusion of lineage. Without edge types, sources, and falsification conditions, the lines are decoration.

#### Research judgment for our Data Agent

| Practice | Judgment | Boundary |
|---|---|---|
| `run × task` matrix | **Adopt** | Use as an evaluation-regression view, not a case evidence graph |
| Click-through task detail | **Adapt** | Detail should show source receipt, query/result, ACL, runtime identity, typed change, claim, contradiction, falsifier, and the applicable Cause-Verdict / Recommendation-Readiness ceiling |
| Ordered step trace | **Adapt** | Keep as a debug pane. Do not put it in the evidence ledger by default or let it promote a Cause Verdict or Recommendation Readiness |
| Show model thought | **Reject** as evidence | Thought is narration. It may help debugging but is neither fact nor causal proof |
| Progress score charts | **Adopt** as a research dashboard | They show evaluation trajectory, not component causality |
| Disabled LLM schema-graph hints | **Reject** direct transfer | A mapping assertion must not pose as an observed relationship. The author's record also shows anchoring risk |
| Node-edge evidence-graph product contract | **Unknown / not proven** | This repository supplies no implementation to adopt. Whether to build it and how to present it remain owner decisions |

#### Missing production A/B evidence-graph chain

The repository does not implement this production chain. Every segment is a gap and must not be inferred from an adjacent capability:

```text
metric
  -> surface / component
  -> query / result
  -> ACL / corpus
  -> pipeline / runtime
  -> typed production change: code | config | flag | model | data
  -> claim
  -> verification / falsifier
  -> recommendation / not-applied diff / rollback-ready packet
```

- **Unknown / not proven**: Metric-node version, window, segment, and definition.
- **Unknown / not proven**: Owner-backed mapping from metric to surface/component.
- **Unknown / not proven**: Query text, parameters, result digest, data snapshot, and independent validator receipt.
- **Unknown / not proven**: ACL decision, caller identity, allowed corpus, and denied sources.
- **Unknown / not proven**: Pipeline job, runtime instance, deployed SHA, configuration, flag, model, and data versions.
- **Unknown / not proven**: Typed production-change inventory and file/symbol/line mapping.
- **Unknown / not proven**: Supporting, contradicting, and missing evidence for a claim.
- **Unknown / not proven**: Verification outcome, cheapest falsifier, invalidation, and supersession.
- **Unknown / not proven**: Executable lineage from recommendation to a `not_applied` candidate diff or rollback-ready packet.

#### Not every edge is causal

If the owner later selects a graph product shape, it should at least distinguish these meanings. The table is **Reviewer inference**, not a contract implemented by this repository.

| Edge type | Meaning | Minimum requirement |
|---|---|---|
| Observed fact | A source directly reports a relationship between A and B | Source receipt, scope, time, digest |
| Derived fact | B is computed from A by a defined method | Transform version, inputs, recomputation receipt |
| Mapping assertion | A is mapped to B | Mapper, basis, confidence, owner or authority |
| Causal claim | A caused or contributed to B | Timing, scope, mechanism, disconfirmation |
| Contradiction | Two material items disagree | Preserve both original receipts; do not overwrite either |
| Supersedes / invalidation | New evidence replaces or invalidates an older conclusion | Actor, reason, timestamp; old node remains auditable |

In trace, `step N -> step N+1` means only execution order. `SQL -> prediction` can be a derived-fact edge only when the result receipt is complete. Neither is automatically causal.

## 5. Tools, retrieval, SQL, and document reasoning

### 5.1 Useful boundaries

- **Observed source fact**: Each phase has a runtime tool allowlist. An out-of-phase tool request is not executed.
- **Observed source fact**: Structured data is exposed through one DuckDB query surface. SQLite is attached with `READ_ONLY`.
- **Observed source fact**: Each task or thread has an isolated DuckDB connection, avoiding unsafe concurrent connection sharing.
- **Observed source fact**: Document reading and SQL querying are separate. Markdown is not treated as a table.

Evidence: [tool allowlist](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/prompt.py#L375-L394); [SQLite read-only attach](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/tools/duckdb_unified.py#L66-L89)

### 5.2 Production risks

- **Observed source fact**: SQL read-only enforcement relies mainly on a string-prefix check. The code notes that DuckDB has no per-query read-only mode. [prefix contract](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/tools/duckdb_unified.py#L273-L290)
- **Reviewer inference**: Allowing `PRAGMA` under a prefix check is not a production SQL capability sandbox. Production needs a parser or AST allowlist, underlying read-only connections, a source allowlist, and row, byte, and time budgets.
- **Observed source fact**: The final answer path can call unbounded `fetchall()`. [unbounded final fetch](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/tools/duckdb_unified.py#L302-L321)
- **Reviewer inference**: A competition requires the full CSV. In production this can cause memory exhaustion. Use artifact streaming and a hard byte limit.
- **Observed source fact**: The prose extractor has a model generate SQL table definitions and rows, then executes them and exports CSV. [prose extractor contract](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/prose_extractor.py#L1-L15)
- **Reviewer inference**: This is model-generated structured transcription. A linked Cause Claim cannot reach `Cause Verdict=confirmed` without a source-span receipt for each material cell; Recommendation Readiness remains a separate assessment.
- **Observed source fact**: The final `exp_172` registry does not expose a general Python or shell tool to the agent. Its default surface is primarily DuckDB, filesystem reads, and model calls.
- **Observed source fact**: The image nevertheless contains 114 old `python_exec.py` files that can execute arbitrary Python. Default path and image attack surface must be audited separately. See Section 2.2.
- **Reviewer inference**: Production security cannot inspect only the default registry. It must also inspect dormant code that can be selected, imported, or dynamically loaded from the image.

## 6. Validation, retry, fallback, and stopping

### 6.1 Deterministic portions

- No backward stage transitions.
- Exploration minimum on the intended adjacent transition.
- Selected video-consumption gates.
- Tool allowlist.
- SQL prefix allowlist.
- Empty-column, empty-row, shape, and selected `DISTINCT` or aggregation rules.
- Maximum steps, task timeout, and wall budget.

### 6.2 Model-judged portions

- Whether the plan understood the task.
- The source router's model route.
- Whether the column auditor removed the right columns.
- Whether alternative SQL is genuinely independent.
- Whether PASS or VIOLATION is truthful.
- Whether confirmation is justified.
- Whether document-extracted numbers match the source.

### 6.3 Explicit fail-open behavior

| Behavior | Source fact | Judgment for our target |
|---|---|---|
| Forward stage skip | Only backward or same-stage transitions are rejected; intermediate stages may be skipped | Reject. A hard state machine must allow only explicitly named adjacent transitions |
| Domain or preprocessing error | Several exceptions become empty values or continued execution | Reject. Missing material input must hard-fail or impose the relevant Cause-Verdict / Recommendation-Readiness ceiling |
| Source-router model failure | Falls back to deterministic routing | Adapt only for navigation. It cannot prove a material gate |
| Source role `avoid` | Source comment makes it advisory | Reject for material source gating |
| Schema full-name check error | Uses `except: pass` | Reject. A hard gate cannot fail open |
| Refinement budget exhausted | Forces terminal commit | Reject. Budget exhaustion does not establish validity |
| Direct confirm | Pending answer becomes terminal | Reject. Human or model ruling cannot replace evidence |
| Empty stub | A crash can leave a valid empty CSV | Acceptable for competition coverage. Production must expose `blocked`, not false success |

Source-router fallback evidence: [router fallback](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/source_router.py#L229-L278). `avoid` advisory evidence: [registry comment](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/src/experiments/exp_172_ehr_distinct/tools/registry.py#L386-L411).

### 6.4 Retry semantics

- **Observed source fact**: Model-adapter retry, task-subprocess retry, and an empty-prediction second pass are different retry capabilities.
- **Observed source fact**: Submission retry checks only whether the prediction is empty. The Phase 2 image disables it by default. A later release-HEAD version enables it and budgets it from remaining time.
- **Reviewer inference**: This is coverage retry, not evidence-aware repair. It has no persistent failure classification, input invalidation, source refresh, or same-failure stop contract.

## 7. README claims versus source

| Statement | Classification | Audit judgment |
|---|---|---|
| Phase 1 first; Phase 2 fourth | Author/README claim | Clearly stated by the repository. Not independently checked against an organizer-signed result |
| 181 experiment packages and 139 commits | Author/README claim | Repository structure and history are consistent with many experiments. Exact counts are not used as architectural causality |
| Four-stage phased ReAct | Author/README claim plus Observed source fact | Source supports the intended stages, but forward skips mean they are not all mandatory |
| Phase transition is not left to the model | Partially supported | Code enforces direction and tools. The model calls `complete_phase`, and the runtime permits forward skips |
| Minimum exploration and scoped tools | Observed source fact | Source supports the adjacent-transition gate and tool scoping, with the bypass noted above |
| Video evidence is mandatory | Conditional support | True only when relevant flags are enabled. It is not unconditional across all video paths |
| Domain routing generalizes to about 10,000 external questions | Author/README claim | No independent final-contract test was found. This cannot be stated as proven causality |
| Deterministic prose-needed gate | Observed source fact plus Unknown impact | The flag and gate exist. Production correctness is unproven |
| Fail-closed output guards | Partially supported; too broad | Some hard guards fail closed. The overall answer path does not |
| Hidden-final success was caused by these guards | Author/README claim | Ranking alone cannot establish component causality |
| One scorer prevents experiments from self-promoting | Author claim plus source support | A shared scorer exists, but cannot remove selection bias, hidden tuning, or infrastructure confounds |

README anchor: [architecture and component claims](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/README.md#L38-L75).

## 8. What tests establish

- **Observed source fact**: Top-level `tests/` mainly covers the CSV scorer and CLI evaluation flow. [scorer tests](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/tests/test_eval_csv_compare.py); [CLI tests](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a/tests/test_cli_evaluate_run.py)
- **Unknown / not proven**: No formal unit or integration tests were found for final `exp_172` stage transition, source routing, forced commit, prose extraction, adaptive vote, or timeout cleanup.
- **Reviewer inference**: Test strength for the README's architecture contract is much lower than for the scorer contract. Demo or leaderboard results are not comprehensive validation of these controllers.

## 9. Comparison with the champion solution

This comparison is limited to our Scenario A and B goals. It is not a general ranking.

Champion-audit fixed SHA: `bdc874fc4260e3565ae0dce041728fdf5b376709`. The separately verified local champion audit identified a more explicit Python orchestration path, narrow tools, structural checks, layered recovery, and recoverable underlying evidence. The fourth-place repository adds different useful practices.

| Different fourth-place practice | Value for our target | Addition relative to champion audit | Judgment |
|---|---|---|---|
| Phase-specific prompt plus runtime tool allowlist | Reduces drift in a long loop | Shows how one continuous agent conversation can change phase contracts | Adapt |
| Unified DuckDB data plane | Gives CSV, JSON, and SQLite one query language | Easier to build one query receipt than a separate agent per source | Adapt; production needs a controlled connector/query plane |
| Tight coupling of final shape and scorer | Shows that output contracts shape agent behavior | Makes evaluator-agent coupling especially visible | Adopt the principle; reject the competition rule itself |
| Complete experiment lineage and failure notes | Useful for implementation sequencing and evaluation design | Provides negative results, not only the final architecture | Adopt the research practice |
| Source-modality routing | Separates sources that hold final values from sources that supply conditions | Useful for roles of metric, trace, code, and config evidence | Adapt into a typed evidence-role contract |
| Layered advisor, task, and attempt concurrency | Shows that concurrency is not one switch | SEV can parallelize independent source reads, but not material gates | Adapt |
| Visible failure surface of adaptive vote and union fallback | Demonstrates that agreement is not proof | Reinforces consensus risk | Reject as a Cause-Verdict gate |

### 9.1 What the comparison cannot establish

- **Unknown / not proven**: It cannot establish that this architecture is worse than the champion architecture.
- **Unknown / not proven**: It cannot attribute rank differences to stages, voting, guards, or a model component.
- **Unknown / not proven**: Task mix, submission state, infrastructure, and variance are insufficient for a fair architecture A/B test.

## 10. Adopt / Adapt / Reject for our target

“Cheapest falsifier” means the fastest test that could disprove the proposed value.

| Practice | Decision | Reason | Required production contract | Cheapest falsifier |
|---|---|---|---|---|
| Code-controlled stages | **Adopt** | Both scenarios need replay and explicit hard stops | `case_state_machine`; stage inputs, outputs, gate receipt, allowed transition | Ten invalid-experiment fixtures must never reach system-hypothesis stages |
| Phase tool allowlist | **Adopt** | Limits overreach and wrong-tool use | Server-side capabilities, read/write class, source allowlist, auth identity | Ask for deploy and flag writes in every stage; server must reject 100% |
| At least N exploration calls | **Reject the number / Adapt the intent** | Call count is not evidence coverage | `required_evidence_types` and receipt coverage, not tool count | Three successful calls all read the wrong source; gate must fail |
| Unified query plane | **Adapt** | Unified structured evidence is useful | Parameterized query, AST allowlist, underlying read-only access, row/byte/time cap, receipt and digest | Malicious SQL corpus plus 100M-row result must neither write nor exhaust memory |
| Extract prose/video before querying | **Adapt** | Search also uses documents, dashboards, logs, and video | Bind every extracted cell or claim to source span/frame, extractor version, and confidence | Conflicting OCR/table numbers; no source span means Cause Verdict cannot exceed `suspected` |
| Domain router | **Reject current heuristic / Adapt routing concept** | Our routing follows scenario and evidence plane, not finance/EHR names | Typed scenario router, unknown lane, route receipt | Unseen query class must enter unknown, not silently use a template |
| Formula and anti-aggregation advisor | **Reject direct answer influence / Adapt as hypothesis helper** | Hints can anchor the result | Advisor output creates candidates only; it cannot alter values or pass a gate | Wrong advisor hint must be overturned by deterministic recomputation |
| LLM column auditor | **Reject as material guard** | It may remove correct columns or preserve wrong ones | Output schema from metric/spec; LLM only explains schema conflicts | Adversarial multi-metric fixture; schema validator decides completeness |
| Source role `primary/support/avoid` | **Adapt** | Useful for production evidence | `evidence_role`, source authority, materiality, conflict rule | Trace and document conflict must remain visible; router cannot overwrite either |
| Source-router fallback | **Reject for hard gates** | Fallback can disguise missing evidence as a route | Material routing fails closed; navigation may fail open | Router unavailable means neither `Cause Verdict=confirmed` nor `Recommendation Readiness=action_ready` is available |
| Self-review plus alternate SQL | **Adapt** | Independent validation is the right direction | Independent implementation and receipt with frozen input | Mutation test where main query and validator share the same bug must fail |
| Two refinements then forced submit | **Reject** | Budget exhaustion does not establish truth | Exhaustion preserves Evidence and creates the applicable Case/Stage/Readiness block or Cause-Verdict ceiling | Three consecutive wrong answers must never force acceptance |
| Consensus or adaptive vote | **Reject as a Cause-Verdict gate** | Correlated models can agree on the same error | Vote is triage only; hard gates accept evidence | Three attempts read the wrong deployed SHA; Cause Verdict must not rise |
| Subprocess timeout and kill | **Adopt** | Prevents hangs | Stage deadline, cleanup receipt, partial-output invalidation | Hung connector must leave a replayable case and no partial evidence in graph |
| Empty-output retry capability | **Adapt** | Transient failures may be retried; competition image disabled it | Typed errors, bounded retry, same-error stop, freshness check | Permanent auth failure must not keep consuming budget |
| Prewritten stub | **Reject production semantics** | Empty CSV hides failure | Explicit `case_status=blocked/failed`; no silent success | Crash before first task must alert as failure, not a valid empty result |
| One scorer across experiments | **Adopt** | Prevents metric drift | Versioned evaluation contract, frozen fixtures, invalid-run ledger | Per-experiment scorer modification must be rejected by CI |
| Experiment package per idea | **Adapt** | Supports isolation and archaeology | Immutable evaluation run, config digest, base SHA; avoid code-tree copies | Two runs differing only in package name must be identified as equivalent |
| Full experiment history and negative results | **Adopt** | Improves evaluation and sequencing | Decision ledger with claims, run IDs, confounds, invalidations | Audit 20 conclusions; each must resolve to raw run receipt |
| Arbitrary model-generated code or literals | **Reject** | Production RCA does not need general execution | No shell, no arbitrary Python, candidate diff only as unapplied artifact | Prompt injection requesting execution or writes must be rejected completely |

## 11. Mapping to Scenario A: post-experiment analysis

### 11.1 Adopt directly

- Use a state machine to separate `freeze -> validity -> recompute -> decompose -> map -> hypothesize -> test -> review`.
- Give each stage its own tool allowlist.
- Give metric, trace, document, and code-diff evidence distinct roles.
- Parallelize independent source reads. Join only before material gates.
- Preserve trace and error class for every failure.

### 11.2 Rewrite

- Replace `3 successful queries` with required receipts for metric definition, assignment, exposure, query result, validator, and runtime identity.
- Replace final-SQL self-review with deterministic metric recomputation and an independent validator.
- Replace the answer table with an evidence packet.
- Turn formula advice into competing-hypothesis assistance.
- Replace the source router with source-authority and conflict resolution.

### 11.3 Reject

- Continuing to system hypotheses after an invalid experiment.
- Using majority vote to confirm why a metric missed.
- Producing a candidate diff with `Recommendation Readiness=action_ready` without a deployed SHA.
- Letting the model assign `Cause Verdict=confirmed` directly.
- Applying any candidate diff automatically.

## 12. Mapping to Scenario B: SEV metric drop

### 12.1 Adopt directly

- Bounded stages and timeout.
- Concurrent independent source adapters.
- Runtime-enforced tool scope.
- Strict final-packet shape.
- Preservation of every attempt and failure reason.

### 12.2 Add

- Deployed runtime identity.
- `code | config | flag | model | data` change inventory.
- Affected segment to service/route/job to repo/file/symbol mapping.
- Changepoint and rollout overlap.
- Trigger, proximate mechanism, contributing factor, and systemic condition.
- Counterfactual, rollback, holdout, and unaffected cohort.
- IC and code-owner escalation.

### 12.3 Current dual-axis ceilings

The former sentence “the highest possible verdict is `action-ready`” is superseded. `action_ready` is Recommendation Readiness, not a Cause Verdict. A material gate result constrains the two axes independently under the [closed canonical domain and policy contract](wayfinder/freeze-canonical-domain-policy-contracts.md): for example, missing runtime identity normally caps Cause Verdict at `suspected` and blocks the linked Recommendation; an invalid experiment makes a production Recommendation `not_applicable`; HIGH risk blocks the Recommendation even if a Cause Claim is `confirmed`.

The following conditions cannot support `Recommendation Readiness=action_ready` for a production Recommendation:

- High risk or large blast radius without IC and code owner.
- Conflicting runtime identity.
- Unclear affected scope.
- Timing proximity alone.
- Consensus alone.
- README, demo, prompt, or heuristic alone.

## 13. Conclusions for the final specification

1. `case_state_machine` must be code-controlled.
2. Every stage needs a server-side capability allowlist.
3. Tool-call count cannot substitute for evidence coverage.
4. Every material evidence item needs a receipt, digest, freshness, scope, and authorization.
5. The validator must be independently implemented, not the same model thinking again.
6. Budget exhaustion must preserve Evidence and produce an explicit Case/Stage block, Recommendation-Readiness block, or Cause-Verdict ceiling; forced acceptance is forbidden.
7. Source roles must be typed. Conflicts must remain visible.
8. Final output needs a strict schema including Evidence/Claim state, Cause Verdict, Recommendation Readiness, support, contradiction, missing evidence, falsifier, owner, and risk.
9. No state authorizes mutation.
10. A candidate diff is always `not_applied`.
11. Retry must be divided by typed failure.
12. An invalid experiment may produce only validity, instrumentation, or data-quality fixes.

## 14. Conclusions for evaluation

1. Out-of-phase capability request.
2. Three successful calls that read the wrong source.
3. Unavailable source router.
4. Validator and main query share one bug.
5. Numeric document extraction lacks a source span.
6. Three attempts agree while using the wrong deployed SHA.
7. Retry encounters permanent authorization failure.
8. Partial evidence leaks into the final packet after timeout.
9. Invalid experiment still produces a system hypothesis.
10. High-risk candidate does not escalate to IC and code owner.
11. Runtime SHA, config, and flag snapshot conflict.
12. Complex SEV has multiple causal roles and must not be forced into one root cause.
13. Human ruling attempts to skip a material gate.
14. Any tool applies a candidate diff.
15. Forward skips such as `PLAN -> ANSWER` and `PLAN -> VERIFY` must all be rejected.
16. Registry contains a tool but the phase allowlist omits it; a reachability test must detect this.
17. A module or tool description claims a guard, but the active call graph does not wire it; the test must fail.

## 15. Implementation sequencing

### P0: Build the trust boundary first

- Case schema.
- Append-only evidence ledger.
- Capability-enforced read-only tools.
- Receipts, digests, freshness, authorization.
- Dual-axis policy ceilings and Gate 0–7 engine.

### P1: Fixed search-metric scenario

- Metric definition, query, and independent validator.
- Experiment validity.
- Segment decomposition.
- Search-pipeline identity.

### P2: Production mapping

- Runtime identity.
- Typed change inventory.
- Segment to runtime to repo/file/symbol mapping.
- Owner and blast radius.

### P3: SEV

- Changepoint.
- Timeline.
- Competing causal roles.
- Rollback-ready packet.

### P4: Add model enhancements last

- Hypothesis generation.
- Source-role suggestion.
- Prose and code summary.
- Unapplied candidate diff.

Competition voting, domain prompt cards, finance/EHR heuristics, and prose-to-SQL literals should not precede the trust boundary.

## 16. Research context only

- Phase 1 and Phase 2 leaderboard numbers.
- Generalization claim about “approximately 10,000 external questions.”
- Causal claim that a selected guard caused hidden-board success.
- Finance/EHR rules for `DISTINCT`, names, and superlatives.
- Three exploration calls, 64 steps, 6,000 seconds, and eight workers.
- Single-attempt and multi-attempt temperatures.
- Task-specific comments and demo-rescue anecdotes.
- Author's best-of-N bias analysis, unless raw runs and statistical method are independently checked.
- Package count and commit count by themselves.

These items can inspire evaluations. They cannot directly become production contracts.

## 17. Blind spots exposed by this repository

### 17.1 “There is a gate” is too vague

The source demonstrates three different gate types:

1. A true hard gate.
2. A prompt instruction.
3. A fallback after error.

The final specification must name each gate's executor, failure semantics, and the relevant Cause-Verdict and Recommendation-Readiness ceilings. Merely saying “Gate 0–7 exists” is insufficient.

### 17.2 Validator independence needs an executable definition

“Run another SQL query” can reproduce the same semantic error. Independence must specify a separate implementation, query plan, or frozen oracle. Evaluation must include correlated-error tests.

### 17.3 Call count is not evidence coverage

Three `ok` results are only three successful calls. They may repeatedly read the same wrong source. A final specification should gate on evidence type, source authority, and scope coverage.

### 17.4 Answer shape changes agent behavior

Many repository decisions follow the scorer's column rules. Our packet schema will also shape reasoning. A schema with only `root_cause` will force one cause. It should natively support four causal roles and competing hypotheses.

### 17.5 Fail-open policy needs materiality levels

The champion audit supported fail-open relevance filtering because underlying evidence remained recoverable. This repository shows how easily that principle can expand into source routing, schema checks, and final answers. A final specification should state:

- Navigation failure may fail open.
- Material evidence, authorization, identity, and validation must fail closed.

### 17.6 Selection strategy is its own risk

Even if every attempt has a trace, vote or union can merge different errors into a new error. The final specification should audit the selection algorithm as a component, not treat it as transparent glue.

### 17.7 A preprocessor is an evidence producer

PDF cache, video summary, and prose extraction are often called preparation. They change evidence. Each needs a version, source span, digest, error, and invalidation rule.

### 17.8 Empty output is not explicit blocked state

The competition stub is a reasonable coverage defense. In production, merging unknown, empty, and blocked creates false success. Case status must be first-class.

### 17.9 Test the architecture contract, not only the scorer

The repository's scorer tests are materially stronger than tests for the final stage controller. Our sequencing should reverse that priority: test trust boundaries, gates, and failure semantics before model quality.

### 17.10 State names do not prove mandatory traversal

The repository encodes stage names and phase tool allowlists. That is useful. But transition checking permits forward skips, so `PLAN -> ANSWER` avoids the exploration gate. A final specification must enumerate the only legal edges, each edge guard, illegal-transition tests, and recovery semantics.

### 17.11 A registered tool is not necessarily reachable

The document-only path registers direct `answer`, but no phase allowlist contains `answer`, so the phased agent rejects it. [document-only registration](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/src/experiments/exp_172_ehr_distinct/tools/registry.py#L786-L813); [phase allowlist](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/src/experiments/exp_172_ehr_distinct/prompt.py#L375-L401)

This exposes a planning blind spot: capability inventory, registry, phase allowlist, image packaging, and runtime reachability must be tested together. Source existence does not prove runtime reachability.

### 17.12 Filenames and descriptions can overstate active validation

`filter_auditor.py` exists, and a tool description mentions column and filter audits. The fixed tag's active call site calls only `audit_columns`; no active filter-auditor call was observed. [active audit call](https://github.com/kekshibata/kddcup2026-data-agents-4th-place-solution/blob/13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65/src/experiments/exp_172_ehr_distinct/tools/registry.py#L578-L600)

A final specification and evaluation cannot use module names, README, or tool descriptions as proof that a guard is wired. They require a runtime reachability test and gate receipt.

## 18. Historical Gate 0–7 Critique (Superseded as Policy)

The fourth-place solution does not supply these gates. It supplies only stage-control inspiration. The table below is retained as a pre-resolution reviewer critique, not an implementation contract. Its numbering, conditions, and single-axis shorthand are superseded by the [closed canonical domain and policy contract](wayfinder/freeze-canonical-domain-policy-contracts.md), which defines the current Gate 0–7 receipt inputs, executors, pass/fail/inconclusive behavior, reopen rules, and independent axes.

| Historical gate | Historical proposed condition | Historical shorthand ceiling |
|---|---|---|
| Gate 0 Authorization | Case scope, read-only capability, source allowlist | `blocked` |
| Gate 1 Identity | Experiment or incident, metric version, time window | `suspected` |
| Gate 2 Validity | SRM, instrumentation, freshness, data quality | Invalid case permits only validity fixes |
| Gate 3 Runtime | Deployed SHA, configuration, flag, model, data identity | `suspected` |
| Gate 4 Evidence | Required receipts, coverage, lineage, conflict | `suspected` |
| Gate 5 Mechanism | Timing, scope, mechanism, disconfirmation | `action-ready` ceiling |
| Gate 6 Risk | Blast radius, rollback, owner, IC, code owner | High risk cannot reach `action-ready` |
| Gate 7 Confirmation | Independent or counterfactual evidence plus human review | `confirmed` |

The retained historical direction remains compatible with the current policy: a human ruling cannot replace material Evidence, and no state authorizes mutation. For current behavior, use the closed canonical contract rather than this historical table.

## 19. Final recommendation

Do not reproduce this solution.

Take its exoskeleton: stages, tool boundaries, unified query surface, timeout, shared scorer, and failed-experiment ledger.

Replace its internals: competition heuristics, self-confirmation, forced submission, advisory source guards, vote-as-answer, and prose numbers without receipts.

The clean target state is:

```text
read-only case
  -> fix identity and authorization
  -> independently validate metric / incident signal
  -> build typed evidence graph
  -> connect real runtime and deployed changes
  -> rank competing causes
  -> pass Gate 0-7
  -> produce evidence packet / not-applied candidate diff
  -> human decision
```

This adds the critical production requirement missing from “connect the KDD agent to GitHub”: prove what is actually deployed now and why the recommendation points to that change.

## 20. Unknowns and blockers

- No organizer-held image digest or runtime receipt was obtained.
- Private competition data is unavailable, so the hidden board cannot be reproduced locally.
- README leaderboard results and component causality were not independently verified.
- The final architecture lacks direct tests. Conclusions rely on source contracts and repository experiment records.
- Release HEAD is later than `phase2-final`. The annotated-tag object is `3c56d2fd...`; the peeled commit is `13b17fcc...`. This report audits snapshot architecture and image-source identity separately.
- Dockerfile and build scripts cannot prove byte identity of the uploaded tar. No organizer image digest was found.
- No evidence proves transfer to production search or SEV workflows. All transfer statements are Reviewer inference and have falsifiers.
- Docker environment variables are defaults and may be overridden. Actual competition runtime knobs remain unproven.
- No active-path source contract was observed for human approval, deployed reachability, production identity, change discovery, or general evidence invalidation.
- The active default path does not expose arbitrary Python, but the image contains dormant arbitrary executors. Competition reachability is unknown.
- Graph UI was not observed. The run-by-task matrix, trace viewer, static dashboard, and Mermaid diagrams are adjacent capabilities, not an evidence graph.
- The owner has not approved an evidence-graph product contract. This audit does not freeze one.

These unknowns do not block completion of the reverse audit. They block stronger claims. The repository does not prove production suitability, the causal contribution of one component to fourth place, or the identity of the exact binary executed by organizers.
