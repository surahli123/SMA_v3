# Data Agent redesign: primary-source audit

## Conclusion first

The goal is neither to patch old SMA nor to copy the KDD pipeline. Both real tasks require a primary path that the old system does not have:

`metric facts -> suspect window -> production change inventory -> file/symbol/diff -> falsifiable cause -> targeted validation`

What is worth retaining from the existing source code is its mechanisms: deterministic metric gates, segment/mix decomposition, read-only queries, selective escalation, layered retries, and rerunnable ledgers and traces. What the existing source code lacks is discovery of production code/config/flag/model/data changes. This gap means the redesign must add a code/runtime evidence plane.

This document treats only the current local source code as primary evidence. The workshop, older research documents, and screenshots were not used to prove that practices are effective; screenshots were not used as substitutes for recordings, and no audio transcription was performed.

## Two real requirements

- **A — post-experiment metric miss**: The experiment did not meet its target. First verify the experiment/metric facts, then locate mechanisms in production code that may have caused the miss, and propose a change supported by `file + symbol + diff/commit + targeted test`.
- **B — SEV metric drop**: An online metric suddenly declined. First confirm the drop and time window, then audit code, config, feature flag, model, and data changes in the same window; produce a suspect list with temporal order, impact paths, and falsification conditions.

## Audit scope and source identity

- Local KDD iteration source: `KDD_Competition` (local source, not included), at audit HEAD `7270e3bcc24a039ac458e45caeab7a283c62eca8`.
- Old SMA source: `.agents/skills/sma` (repository-relative source), at audit repo HEAD `28cbbda6e4d4d7f08134952d38433e52d3ee8768`.
- The KDD canonical/mirror boundary is documented in `KDD_Competition/docs/source-map.md` (local source, not included); this audit cites canonical Python files and does not treat the `main.py` mirror, temporary directories, or submission tarballs as design source code.
- `Adopt` means adopt the principle, not copy old parameters; `Adapt` means retain the mechanism but rewrite the contract; `Reject` means exclude it from the default target design.

## Primary-source audit

### P1. Metric credibility must first pass a deterministic gate

**Source evidence**

- `.agents/skills/sma/scripts/anomaly.py:169`, symbol `check_data_quality`: checks completeness and freshness before analysis.
- `.agents/skills/sma/scripts/anomaly.py:231`, symbol `detect_step_change`: finds the largest day-over-day change and checks whether the change persists.
- `KDD_Competition/kdd/sanity_checker.py:33` (local source, not included), symbol `check_sanity`: runs mechanical checks for zero rows, numeric ranges, filter effect, count type, row count, and other conditions before the LLM reviewer.

**Migration judgment**

- A: First verify exposure, SRM, treatment/control window, and metric freshness/completeness; otherwise the process cannot proceed to code root-cause analysis.
- B: First verify the drop, breakpoint, data latency, and instrumentation completeness; otherwise the SEV may only be an observability failure.
- Limitation: When fields are missing, old SMA defaults completeness to `1.0` and freshness to `0.0` (`anomaly.py:176-197`), which can misclassify unknown data as trustworthy.
- **Decision: Adapt**. Retain the gate, but missing fields must produce `unknown/inconclusive` and cannot automatically pass; thresholds must be calibrated against production metrics.

### P2. Perform contribution decomposition before searching production changes

**Source evidence**

- `.agents/skills/sma/scripts/decompose.py:136`, symbol `compute_aggregate_delta`: records baseline/current values, absolute and relative changes, and sample sizes.
- `.agents/skills/sma/scripts/decompose.py:182`, symbol `decompose_by_dimension`: calculates rate change, traffic weight, and contribution by segment.
- `.agents/skills/sma/scripts/decompose.py:266`, symbol `compute_mix_shift`: distinguishes behavioral change from traffic-composition change.

**Migration judgment**

- A: Find where the miss is concentrated by treatment/control, query type, surface, and population, then map those segments to code paths.
- B: Find the blast radius by tenant, platform, region, query class, and model route, then narrow the change inventory.
- Limitation: The current implementation uses row count as traffic weight (`decompose.py:222-239`); a real system may need exposure, request, or user weighting and must handle variance and missing segments.
- **Decision: Adapt**. Retain the decomposition sequence, rewrite the weighting and statistical contract, and require the decomposition result to directly generate the scope for subsequent code/runtime search.

### P3. Experiment diagnosis must use a concurrent control, not only pre/post comparison

**Source evidence**

- `.agents/skills/sma/references/playbooks/patterns/experiment_diagnosis.md:21`: requires confirmation of ramp, treatment/control ratio, and SRM.
- The same file at `:26-36`: when the control also changes, the change cannot be attributed to the experiment; the true experiment effect is concurrent `treatment - control`, not `treatment - pre-period`.
- The same file at `:38-41`: requires checking other concurrent experiments, model updates, infrastructure changes, and seasonal factors.

**Migration judgment**

- A: This is a hard gate before production-code investigation; experiment metadata, assignment receipt, and metric-query receipt must each have a stable ID.
- B: Enable this only when the SEV overlaps an experiment/rollout; an ordinary incident is not required to follow the experiment process.
- Limitation: This is a verified old-SMA playbook, not an implementation connected to real Statsig/deploy data and not proof of production effectiveness.
- **Decision: A Adopt; B conditional Adapt**. Convert the textual checks into structured connectors and recomputable receipts.

### P4. Cause-before-effect is hard logic, but unknown cannot count as a pass

**Source evidence**

- `.agents/skills/sma/scripts/diagnose.py:208`, symbol `check_temporal_precedence`: compares the metric step date with dates in the diagnosis.
- The same file at `:226-244`: when there is no step date or diagnosis date, it still returns `passed: True`, while the detail says skipped/inconclusive.

**Migration judgment**

- A: A candidate code/config/model change must satisfy `effective_at <= experiment observation window` and cover the treatment code path.
- B: A candidate must satisfy `effective_at <= breakpoint`; a deployment after the drop should be excluded immediately.
- Limitation: The current implementation extracts dates from free text with regex and compares only date strings, so it cannot handle deployment completion time, flag ramp, rollback, time zones, or gradual rollout.
- **Decision: Adapt**. Use typed timestamps/event intervals; unknown is `inconclusive` and cannot pass.

### P5. Production queries are read-only by default, with safety enforced by code rather than prompts

**Source evidence**

- `.agents/skills/sma/scripts/query.py:104`, symbol `_validate_sql`: allows only `SELECT` or a CTE whose final main statement is `SELECT`, and checks for multi-statement and comment bypasses.
- `KDD_Competition/core/sql_executor.py:99-113` (local source, not included), symbol `execute_sql`: validates data-source exclusivity and the write block before selecting a backend.
- The same file at `:148-177`, symbols `_check_write_block` and `_run_sqlite`: allowlists the first token and uses SQLite `mode=ro` as a second layer of read-only protection.

**Migration judgment**

- A: Reading experiment, metric, log, and repository metadata is allowed; changing code or flags and performing a rollout are outside the default diagnostic authority.
- B: Read first during an incident; rollback/flag mutation is a separate approval action and cannot execute automatically because an SEV exists.
- Limitation: KDD's first-token check is explicitly a simplified version for a trusted agent (`sql_executor.py:148-157`) and is insufficient against untrusted SQL; SMA's parser is also not a substitute for database-level permissions.
- **Decision: Adopt the principle, Adapt the implementation**. Tools should use read-only credentials, query timeouts, row/byte caps, and audit logs; side effects must use a separate authorization plane.

### P6. Mechanical gates should precede the semantic reviewer

**Source evidence**

- `KDD_Competition/kdd/sanity_checker.py:1-13` (local source, not included) explicitly requires deterministic checks to run before the LLM reviewer to reduce cost and stochastic misclassification.
- The same file at `:87-106`, symbol `_check_zero_rows`: turns an empty result into specific suggestions to check filters, JOINs, and dates.
- The same file at `:109-181`, symbol `_check_magnitude`: checks ranges for counts, percentages, and negative values.

**Migration judgment**

- A: Mechanically check exposure/SRM, query receipt, metric math, diff applicability, and targeted-test results; the reviewer should judge only the remaining semantic causal chain.
- B: Mechanically check breakpoint, change ID, effective time, affected service/path, and rollback state; the reviewer should not rewrite factual fields.
- Limitation: KDD thresholds such as `10000` reflect competition data shapes and cannot be carried into production; `FILTER_NO_EFFECT` currently works only when the caller provides total rows (`sanity_checker.py:185-205`).
- **Decision: Adopt the ordering, Adapt the check set**.

### P7. Fan-out/vote should be enabled only selectively

**Source evidence**

- `KDD_Competition/kdd/submission_loop.py:34-47` (local source, not included), constant `SQL_FLIPPER_TASKS`: comments explicitly state that majority voting amplifies the dominant-wrong pattern and enable it only for validated flippers.
- The same file at `:195-218`, symbol `run_one_task`: the stable route uses a single run by default; only hybrid/flipper routes vote, and the skeptic is not stacked on the voting route.
- The same file at `:256-290`: deterministic route conditions select source-derived, voting, or stable SQL.

**Migration judgment**

- A: Fan out by mechanism/segment only when multiple independent causal branches remain unresolved; do not have three agents vote on the same thin evidence.
- B: Evidence collection can run in parallel across the code, config/flag, model, and data planes; merge by evidence coverage, not answer count.
- Limitation: The KDD allowlist consists of task IDs and competition heuristics and cannot be migrated; its `n_votes=3` is not a general parameter either.
- **Decision: Adapt selective routing; Reject broad voting**.

### P8. Retry must be layered by failure type and have stopping conditions

**Source evidence**

- `KDD_Competition/kdd/submission_loop.py:121-151` (local source, not included), symbols `_is_retryable_stable_sql_empty_answer` and `_is_retryable_stable_sql_transient_failure`: distinguishes empty/provider-transient failures from local-cap exhaustion; the latter cannot be retried blindly.
- The same file at `:291-316`: a stable run gets only one fresh replay; it selectively escalates to a vote fallback only after consecutive empty results.
- `.agents/skills/sma/scripts/pipeline.py:590-601`: allows at most one retry per pause and sets a circuit breaker.

**Migration judgment**

- A/B: Handle transport, permission, query syntax, empty evidence, schema mismatch, and causal uncertainty separately; failure in an earlier layer cannot be hidden by additional reasoning calls.
- Limitation: Old SMA's fixed pause count and KDD's fixed voting fallback do not match the new tasks.
- **Decision: Adopt the layered/bounded principle; Reject the fixed retry graph**.

### P9. Every conclusion must trace back to a run, commit, environment, and artifact

**Source evidence**

- `KDD_Competition/kdd/trusted_run_ledger.py:31` (local source, not included), symbol `entry_from_manifest`: builds a run entry from a retained manifest and includes the head commit, branch, and artifact root.
- The same file at `:110-161`, symbol `build_entry`: records run ID, timestamp, git commit/branch, candidate behavior change, verdict, rerun command/environment, metrics, baseline comparison, and evidence paths.
- The same file at `:164-176`, symbol `write_ledger_entry`: writes a new file according to a naming contract and does not overwrite an existing entry.

**Migration judgment**

- A: Bind each proposed fix to an experiment receipt, metric-query hash, repository/commit, file/symbol, patch, targeted test, and expected metric movement.
- B: Bind each suspect to a breakpoint, deploy/flag/model/data event ID, commit/config version, affected path, corroborating logs/metrics, and rollback status.
- Limitation: The ledger accepts caller-provided commit/environment values; it does not itself discover a change or verify that the commit is the live production runtime.
- **Decision: Adapt**. Retain the artifact-driven ledger and add runtime-identity verification and typed claim-evidence links.

### P10. Traces must be complete while controlling downstream context

**Source evidence**

- `KDD_Competition/trace/span.py:17-50` (local source, not included), type `TraceSpan`: records stage, tool, decision, whether it is code-enforced, inputs/outputs, alternatives, constraints, and duration.
- `KDD_Competition/trace/collector.py:44-79` (local source, not included), symbols `emit` and `emit_seam`: consistently adds trace/span/timestamp identity and records stage-boundary validation.
- The same file at `:93-153`, symbol `agent_context_for`: gives downstream agents a token-budgeted summary, retains decision/evidence count, and excludes raw payloads.
- `.agents/skills/sma/scripts/pipeline.py:301-347`, symbol `_write_stage_trace`: old SMA stores stage traces in the session directory, but trace-write failures are non-fatal.

**Migration judgment**

- A/B: Retain complete evidence in the artifact store; agent context should contain only IDs, summaries, and location pointers. This preserves auditability without putting large diffs/logs into prompts.
- Limitation: The current KDD trace schema has no repository URL, commit/diff identity, query hash, or deploy/flag/model/data event; old SMA does not block on trace failure, allowing conclusions without evidence.
- **Decision: Adapt**. Low-risk intermediate traces can be best-effort; a final causal claim missing a required evidence link must fail closed.

### P11. Budget and concurrency belong in the control plane, not hardcoded in agent prompts

**Source evidence**

- `KDD_Competition/kdd/latency_governor.py:61-85` (local source, not included), symbols `configured_cap` and `budget_fuse_active`: the global concurrency cap is configurable; when the remaining budget approaches task timeout plus reserve, it stops optional heavy work and retains the best result.
- The same file at `:144-228`, type `LLMInflightSlot`: provides cross-process tokens, locks, wait timeouts, and stale-token cleanup.
- The same file at `:259-279`, symbol `_emit`: records task, stage, model, provider host, cap, wait, elapsed time, and success/error.

**Migration judgment**

- A: Prioritize complete, verifiable fix evidence; when budget is insufficient, return a coverage gap rather than manufacturing a conclusion.
- B: Prioritize time-to-first-safe-action; first investigate changes with high coverage, easy rollback, and close proximity to the breakpoint, then expand to the long tail.
- Limitation: KDD uses environment variables and competition wall-clock parameters; the new system needs budgets based on data sensitivity, incident severity, and repository/query cost.
- **Decision: Adapt**.

### P12. Single-variable changes plus baseline comparison can serve as a validation skeleton for proposed changes

**Source evidence**

- `KDD_Competition/kdd/autorefine.py:53-64` (local source, not included): each mutation changes only one prompt aspect, avoiding combinatorial explosion and unclear attribution.
- The same file at `:134-210`, symbol `_compute_verdict`: compares baseline/current, lists per-task regressions and improvements, then returns keep/discard/investigate.
- The same file at `:217-267`, symbol `run_autorefine`: runs a baseline first, then each mutation, and resets configuration after each round.

**Migration judgment**

- A: A proposed code fix should form a minimal patch and be compared with the same fixture/replay baseline; results must report improvements, regressions, and coverage.
- B: Incident mitigation can be validated as a single-variable change in shadow/canary/targeted replay; without authorization, the system can only generate a validation plan and cannot directly change production.
- Limitation: A KDD canary is a fixed competition task and cannot prove a production causal effect; prompt reset is also not equivalent to safe code/config rollback.
- **Decision: Adapt**. Adopt minimal intervention and paired comparison, and replace the validation set with replay/canary cases generated from the affected production path.

## Explicitly rejected candidate practices

| Candidate | A | B | Primary evidence and rationale |
|---|---|---|---|
| Treat missing quality fields as trustworthy by default | Reject | Reject | `.agents/skills/sma/scripts/anomaly.py:176-197` defaults missing values to good data. Unknown must be presented explicitly. |
| Pass the causality gate despite missing temporal evidence | Reject | Reject | `.agents/skills/sma/scripts/diagnose.py:226-244` returns `passed: True`. It should be inconclusive. |
| Require at least three hypotheses | Reject | Reject | `.agents/skills/sma/scripts/validate.py:284-312` hardcodes C5. The number of hypotheses should be determined by unresolved causal branches. |
| Fixed linear stages and three PAUSEs | Reject | Reject | `.agents/skills/sma/scripts/pipeline.py:18-27,603-617` provides only a fixed linear sequence and retry branch, which cannot express the different evidence graphs for A and B. |
| Broad voting by default | Reject | Reject | `KDD_Competition/kdd/submission_loop.py:34-47` (local source, not included) already states that majority voting amplifies the dominant-wrong pattern. |
| Reuse KDD task-ID routes and fixed `n_votes=3` | Reject | Reject | `KDD_Competition/kdd/submission_loop.py:195-218,256-290` (local source, not included) is competition task routing, not production diagnosis policy. |
| Reuse KDD numeric thresholds and output/scorer contract | Reject | Reject | The range heuristics in `KDD_Competition/kdd/sanity_checker.py:109-181` (local source, not included) come from competition task shapes; the target artifact should be claim/evidence/action, not a prediction score. |
| Treat old SMA's branch helper as production code intelligence | Reject | Reject | `_git` in `.agents/skills/sma/scripts/branch.py:87` serves only session branch/commit/push operations; the file has no contract for production repository search, log/diff/blame, or deployment correlation. |

## Critical capability gaps

A search across the Python/Markdown tool surfaces of both source trees confirms:

1. **Old SMA has no production change discovery.** It can say "check ranking/model/config changes" and has a helper for managing its own session branch, but it cannot read `log/show/diff/blame` from the target production repository and has no symbol ownership, deploy-to-commit mapping, feature-flag history, model-registry history, or data-lineage change history.
2. **The KDD ledger records commits but does not discover or verify live changes.** `trusted_run_ledger.build_entry` accepts caller-provided commit/environment values; it cannot prove that the commit is running in production.
3. **Neither has a typed change inventory.** A/B need a unified representation of `code | config | flag | model | data` changes with `effective_at`, scope, runtime identity, source link, and rollback state.
4. **Neither maps metric segments to symbols.** A service/route/metric ownership catalog is needed to find code paths from affected segments/query classes rather than searching the entire repository loosely.
5. **Neither has a code-backed action gate.** "Recommend checking/rolling back" is insufficient; A needs at least a file/symbol/diff, mechanism explanation, and targeted test. B needs at least a suspect event ID, impact path, corroborating evidence, falsifier, and safe mitigation plan.

Therefore, the old architectures provide only partial practices and do not define the redesign boundary.

## Recommended minimal greenfield target

The shared core should retain only the evidence lifecycle; A and B should use different policies:

1. **Metric intake**: metric definition, window, population, experiment/incident ID, and query receipt.
2. **Deterministic metric gate**: freshness, completeness, SRM/control or breakpoint/step, and segment/mix.
3. **Typed change inventory**: collect code, config, flag, model, and data events within the suspect window; each item carries a stable ID and effective interval.
4. **Scope mapping**: map affected metric segments to service/route/repository/file/symbol; filtering can reduce default context but cannot delete underlying evidence.
5. **Causal tests**: temporal precedence, affected-path overlap, counterfactual/control, corroborating metric/log, and falsifier.
6. **Action artifact**:
   - A produces a minimal proposed diff, targeted test/replay, expected metric mechanism, and regression risk.
   - B produces ranked suspects, immediate safe checks, reversible mitigation options, and actions requiring authorization; it does not execute mutations by default.
7. **Claim-evidence ledger**: stores runtime identity, commit/config/model/data versions, query hash, artifact links, coverage gaps, cost, and a rerunnable recipe.

## Final adopt / adapt / reject summary

| Practice | A | B |
|---|---|---|
| metric/data quality gate | Adapt | Adapt |
| segment contribution + mix shift | Adapt | Adapt |
| SRM, holdout, concurrent treatment/control | Adopt | Conditional |
| typed cause-before-effect | Adopt | Adopt |
| read-only evidence tools | Adopt | Adopt |
| deterministic gate before semantic review | Adopt | Adopt |
| selective fan-out by unresolved branch | Adapt | Adapt |
| broad voting | Reject | Reject |
| failure-typed bounded retry | Adopt | Adopt |
| run/commit/environment/artifact ledger | Adapt | Adapt |
| complete trace + budgeted agent context | Adapt | Adapt |
| budget/concurrency control plane | Adapt | Adapt |
| minimal change + paired validation | Adapt | Adapt |
| old SMA fixed stages/three hypotheses | Reject | Reject |
| KDD task/scorer/output architecture | Reject | Reject |

The acceptance criterion is not "can generate a diagnosis." A must be able to move from a metric miss to a production symbol and a verifiable patch; B must be able to move from a breakpoint to a code/config/flag/model/data change inventory and clearly identify what is evidence and what remains a coverage gap.
