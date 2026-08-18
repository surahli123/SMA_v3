# Greenfield Data Agent: Current Research Routing and Synthesis

Date: 2026-08-12

Status: Current supporting synthesis of the research record. It routes source observations, author claims, reviewer inferences, and owner-confirmed decisions into the canonical package, but it does not override the [planning decision packet](planning-decision-packet.md), the closed [domain and policy contract](wayfinder/freeze-canonical-domain-policy-contracts.md), or the [final architecture specification](final-architecture-spec.md). Production authority (P2), live interaction and visual acceptance (P3), and evaluation gold and calibration (P4) remain open. The single authorized terminal Fable attempt failed closed at the live availability gate; no terminal review occurred.

Current entry point: use the [deliverable index](deliverable-index.md) for reading order and status, then the [final architecture specification](final-architecture-spec.md) and [implementation sequencing](implementation-sequencing.md) as the current design and delivery authorities. Earlier drafts and the prior Fable audit remain historical inputs, not current authority.

## 1. Executive Conclusion

The design starts from only two real problems.

- **A — Post-experiment:** Determine whether the experiment is valid, then explain why the metric missed expectations. Narrow the cause to ranked production `code | config | flag | model | data` candidates. The system may generate an unapplied candidate diff.
- **B — SEV:** Confirm the drop, onset, and affected scope, then identify changes that actually reached that production scope. Produce deployed-SHA-bound candidates and a rollback-ready packet.

A/B should share one evidence core: frozen cases, read-only evidence collection, reproducible numbers, runtime identity, typed change inventory, metric-to-symbol mapping, falsifiable claims, counterevidence, review, and immutable handoff. A emphasizes experiment validity, a complete causal chain, and why lift did not occur. B emphasizes time-to-first-safe-action, the change window, blast radius, rollback readiness, and continuing RCA.[`greenfield-requirements.md:73-185`](greenfield-requirements.md) [`primary-source-audit.md:218-242`](primary-source-audit.md)

Old SMA, the KDD workshop, Champion, Fourth-place, and Creative Track works are references only. They show mechanisms worth testing; they do not determine the new system's modules, framework, vendor, or UI.[`greenfield-requirements.md:8-17`](greenfield-requirements.md)

The central finding is that award-winning solutions are strong at bounded orchestration, narrow tools, traces, repair, and multimodal extraction, but none implements our complete production causal chain. The new design must not be migrated from old code; it must add a production evidence plane.[`champion-repo-reverse-audit.md:180-210`](champion-repo-reverse-audit.md) [`fourth-place-repo-reverse-audit.md:272-311`](fourth-place-repo-reverse-audit.md) [`primary-source-audit.md:218-242`](primary-source-audit.md)

## 2. Source Inventory and Evidence Levels

### 2.1 Inputs Checked Item by Item

| Input | Primary use | Evidence level and boundary |
|---|---|---|
| [`meeting-audio-alignment.md`](meeting-audio-alignment.md) | Complete timeline for both recordings and screenshot-assisted corrections | Stored hash, duration, ASR, and alignment receipts support 100% duration coverage; this is not a verbatim transcript. The original Voice Memo temporary paths are no longer available, so no current audio re-read is claimed. Missing screenshots are not negative evidence.[`:6-38`](meeting-audio-alignment.md) |
| [`screenshot-index.md`](screenshot-index.md) | Visual index of 73/73 partial slides | Direct visual observation. Corrects aligned terminology only; slide text cannot be reported as spoken words.[`:3-13`](screenshot-index.md) |
| [`qwen-whisper-asr-comparison.md`](qwen-whisper-asr-comparison.md) | Third-ASR attempt and conflict register | OpenRouter Qwen smoke is NO-GO; not a second valid transcript.[`:202-230`](qwen-whisper-asr-comparison.md) |
| [`creative-team1286-practices.md`](creative-team1286-practices.md) | PiTrace paper/video, graph UI, and control mechanisms | Separates Video observed, paper author claim, and reviewer inference. No confirmed official repo.[`:192-244`](creative-team1286-practices.md) |
| [`creative-team1401-practices.md`](creative-team1401-practices.md) | Data Agent Studio video, schema/PDF graphs, and trace | Video only. No paper/repo/server receipt; UI does not prove backend enforcement.[`:363-404`](creative-team1401-practices.md) |
| [`champion-repo-reverse-audit.md`](champion-repo-reverse-audit.md) | Fixed-source reverse audit and Fable-claim verification | Fixed SHA `bdc874fc4260e3565ae0dce041728fdf5b376709`; source facts are strong, README/HTML claims separate.[`:19-34`](champion-repo-reverse-audit.md) |
| [`fourth-place-repo-reverse-audit.md`](fourth-place-repo-reverse-audit.md) | Reverse audit of the Fourth-place release and Phase 2 image | Release SHA `ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a`; Phase 2 commit `13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65`. Competition tag and later release are separate.[`:55-69`](fourth-place-repo-reverse-audit.md) |
| [`primary-source-audit.md`](primary-source-audit.md) | Source facts and capability gaps in old SMA and local KDD | Direct source observation. Proves mechanisms exist, not production diagnosis success.[`:18-25`](primary-source-audit.md) |
| [`kdd-source-practices.md`](kdd-source-practices.md) | Candidate practices across workshop, Champion, local KDD, and old SMA | Mixes source facts and reviewer recommendations; Adopt/Adapt/Reject is not an owner decision.[`:438-487`](kdd-source-practices.md) |
| [`rca-sev-causal-confirmation-practices.md`](rca-sev-causal-confirmation-practices.md) | RCA, causal confirmation, and complex SEV | Official SRE/experimentation sources plus project inference. Gate details are not an industry-wide standard.[`:155-171,278-304`](rca-sev-causal-confirmation-practices.md) |
| [`enterprise-search-experiment-failure-practices.md`](enterprise-search-experiment-failure-practices.md) | Enterprise-search-specific failure planes | Official vendor documentation and primary research. Product contracts are reasoned deductions, not vendor requirements.[`:20-29`](enterprise-search-experiment-failure-practices.md) |
| [`experiment-analysis-agent-evaluation-practices.md`](experiment-analysis-agent-evaluation-practices.md) | Gold, scoring, abstention, stability, and shadow-read | Official evaluation principles plus a project rubric. Numerical thresholds are not frozen.[`:23-45,326-353`](experiment-analysis-agent-evaluation-practices.md) |
| [`fable-opus-audit.md`](fable-opus-audit.md) | Historical adversarial review and owner-decision input | Prior reviewer input, not a primary fact source, terminal review, or current architecture authority.[`:136-179`](fable-opus-audit.md) |
| [`greenfield-requirements.md`](greenfield-requirements.md) | Historical requirements draft | Research-era draft superseded where it conflicts with the current planning packet, closed policy contract, or final specification.[`:1-17`](greenfield-requirements.md) |
| [`planning-decision-packet.md`](planning-decision-packet.md) | Owner-confirmed product destination and boundaries | Current product authority above research interpretations. |
| [`wayfinder/freeze-canonical-domain-policy-contracts.md`](wayfinder/freeze-canonical-domain-policy-contracts.md) | Canonical state, policy, and Gate contract | Closed Wayfinder resolution; freezes orthogonal states, dual axes, `G0`–`G7`, failure ceilings, and human boundaries. |
| [`final-architecture-spec.md`](final-architecture-spec.md) | Logical architecture and implementation-ready contract | Current canonical design authority; open P2/P3/P4 gates remain explicit. |

### 2.2 Unified Evidence Labels

- **Confirmed source fact:** Directly supported by fixed-SHA source, original visual material, or a reproducible query/fixture.
- **Author claim:** README, paper, or speaker statement not independently reproduced.
- **Reviewer inference:** Product recommendation or risk judgment derived from multiple sources.
- **Owner-confirmed decision:** Product boundary explicitly decided by the owner.
- **Unknown / unresolved:** Missing or conflicting evidence, or an undecided owner choice.

Temporal proximity only creates a candidate. A visible line in a UI does not automatically become causality.[`rca-sev-causal-confirmation-practices.md:155-170`](rca-sev-causal-confirmation-practices.md)

## 3. Findings Organized by Problem

### 3.1 Experiment Validity and Metric Diagnosis

A must pass validity first. At minimum, inspect assignment, SRM, exposure, triggering, ramp, sample/power, window, join/completeness/freshness, interference, metric definition, and guardrails. If SRM or a material data-quality failure remains unresolved, output only validity, instrumentation, and data-quality fixes. Preserve system hypotheses as blocked and produce no production change proposal.[`rca-sev-causal-confirmation-practices.md:89-121`](rca-sev-causal-confirmation-practices.md) [`experiment-analysis-agent-evaluation-practices.md:116-128`](experiment-analysis-agent-evaluation-practices.md)

Even a valid experiment cannot jump from aggregate delta to code. Recompute the metric, then decompose by component, segment, time, and mix. “No significant change” and “insufficient evidence” must remain valid outcomes. Old SMA's deterministic gates, same-window control, and mix decomposition are useful references; defaults that treat missing fields as trustworthy or pass missing temporal evidence must be rejected.[`primary-source-audit.md:27-84`](primary-source-audit.md) [`primary-source-audit.md:205-216`](primary-source-audit.md)

A's cause space must not default to a code bug. It must cover at least treatment/exposure, population/mix, measurement, corpus/ACL/freshness, retrieval/ranking/rendering, user behavior, runtime/reliability, and concurrent production changes.[`champion-repo-reverse-audit.md:214-221`](champion-repo-reverse-audit.md)

### 3.2 Enterprise-Search Causal Chain

The actual enterprise-search chain is:

```text
intended treatment
  -> eligible and permission-trimmed corpus
  -> retrieved candidates
  -> fusion / rerank / rendered results
  -> user and session interaction
  -> metric
```

Freeze query context, tenant/role/locale/surface, ACL/identity, connector/index generation, schema/parser/chunker, lexical/vector/hybrid lane, fusion/rerank, fallback/cache, render, and telemetry version. The same query string does not necessarily search the same corpus for different users.[`enterprise-search-experiment-failure-practices.md:6-18`](enterprise-search-experiment-failure-practices.md)

Key diagnostic planes include head/tail and tenant heterogeneity, ACL synchronization, connector/index freshness, query rewrite, embedding compatibility, candidate recall, fusion/rerank, snippet/presentation, zero results, click-position bias, session success, and latency/timeout/fallback/cache.[`enterprise-search-experiment-failure-practices.md:31-46`](enterprise-search-experiment-failure-practices.md) [`enterprise-search-experiment-failure-practices.md:54-96`](enterprise-search-experiment-failure-practices.md) [`enterprise-search-experiment-failure-practices.md:126-142`](enterprise-search-experiment-failure-practices.md) [`enterprise-search-experiment-failure-practices.md:171-212`](enterprise-search-experiment-failure-practices.md)

CTR alone is not relevance. Aggregate lift cannot hide tenant, tail, locale, or ACL regressions. A security regression is a failure even if CTR rises.[`enterprise-search-experiment-failure-practices.md:54-70`](enterprise-search-experiment-failure-practices.md) [`enterprise-search-experiment-failure-practices.md:171-197`](enterprise-search-experiment-failure-practices.md)

### 3.3 Runtime Identity and Change Discovery

All reference systems lack complete production change discovery. The target must represent `code | config | flag | model | data` uniformly and record, for each item, a stable ID, effective interval, rollout scope, environment, owner, source receipt, runtime identity, rollback state, and type-specific identity.[`primary-source-audit.md:218-242`](primary-source-audit.md) [`greenfield-requirements.md:206-225`](greenfield-requirements.md)

A commit existing in SCM does not prove production runs it. B candidates must bind to the SHA/config/flag/model/data version actually running in the affected environment. A proposals must also resolve to exact owner/repo, deployed revision, and file/symbol. Missing mapping stays unknown; broad repository keyword search cannot masquerade as a production path.[`greenfield-requirements.md:219-225`](greenfield-requirements.md)

Docker audits reinforce that image, repo, tag, runtime selection, dependency lock, and exit status may drift. Champion's entrypoint pipeline may hide main-process failure. Fourth-place's Phase 2 image allows `EXPERIMENT_NAME` to be overridden and copies a much larger code surface than its default path.[`champion-repo-reverse-audit.md:117-140`](champion-repo-reverse-audit.md) [`fourth-place-repo-reverse-audit.md:95-114`](fourth-place-repo-reverse-audit.md)

### 3.4 Evidence Graph and Review UI

The four focused studies must not be collapsed incorrectly:

- **Team 1286 has real graph UI.** Video shows source nodes, multiple line styles, translucent groups, node/group detail, `Re-layout`, findings walk, and answer-path graph. Filter, edge detail, group expand/collapse, manual edge editing, and graph timeline replay were not observed.[`creative-team1286-practices.md:196-214`](creative-team1286-practices.md)
- **Team 1401 has real graph UI.** The schema graph shows table/column/key, solid FK, and dashed heuristic joins. The PDF KG shows typed relations, clusters, node detail, page locator, collapse/expand, type filter, zoom, and fit. Event Log is an execution/debug trace, not an evidence graph.[`creative-team1401-practices.md:365-394`](creative-team1401-practices.md)
- **Champion graph UI not observed.** The Fable HTML is a static architecture SVG. The repo contains logs, trajectories, timings, votes, and `__src_line`, but no graph builder, claim registry, or interactive evidence graph.[`champion-repo-reverse-audit.md:285-326`](champion-repo-reverse-audit.md)
- **Fourth-place graph UI not observed.** The repo has Mermaid diagrams, a run × task matrix, a click-through trace viewer, and a static dashboard. They support process explanation, evaluation, and debugging, not a node-edge evidence graph.[`fourth-place-repo-reverse-audit.md:228-258`](fourth-place-repo-reverse-audit.md)

Useful ideas are node click-through, source locators, group/filter/navigation, exact query/result receipts, and separate debug-trace and final-evidence panes. Proximity, group membership, step order, model thought, `rests on` chips, page pointers, and arbitrary arrows are not causal evidence.[`creative-team1286-practices.md:223-244`](creative-team1286-practices.md) [`creative-team1401-practices.md:406-450`](creative-team1401-practices.md)

The canonical contract now freezes the typed Evidence Graph substrate, its separation from Trace, required node and edge trust detail, local-first entry with access to full coverage and competing claims, and the rule that another projection must be used when it is clearer. Evidence Graph and Trace are separate, cross-linked read-only projections; neither is the source of truth.

The current static synthetic prototype is the **Evidence Room** workspace with `Review | Claims | Verify | Trace`; it replaces the owner-rejected A/B/C, Evidence Dossier, and Case Ledger iterations. It is M1 research, not the current M0 packet-centered review surface. The latest owner-requested structural redo makes Review a decision header, blocker-first support/contradiction comparison, direct exact-proof action, and inline authority trail. Claims uses a typed, question-oriented Evidence Graph; Verify separates observed deployment from the literal `not_applied` candidate; Trace stays visibly separate from Evidence. On mobile, Claims becomes a complete vertical typed path rather than a squeezed graph, while the 390x844 Review first viewport includes the strongest contradiction and direct proof action. Browser checks are design and mechanical evidence only. The current owner review panel scored the prototype `2.1` with `convergence.passed=false`; earlier `3.6/5`, `4.1/5`, and `4.5/5` agent critiques are superseded history.[`prototypes/observability-review-surface/README.md`](prototypes/observability-review-surface/README.md)

P3 does not reopen the logical contract and remains open. Screenshots, browser checks, or agent critique cannot substitute for live owner/reviewer acceptance that the hierarchy, interactions, and visual treatment improve observability and review efficiency.[`wayfinder/prototype-observability-first-review-surface.md`](wayfinder/prototype-observability-first-review-surface.md)

### 3.5 Deterministic Gates and Semantic Reasoning

The strongest source-level pattern is code-controlled stages, schemas, budgets, and mechanical gates, with models handling uncertain semantics. Champion's bounded stages, narrow tools, soft relevance, and shape/syntax checks are useful. Fourth-place's phase tool allowlist, executable SQL answers, answer review, and bounded repair also have value.[`champion-repo-reverse-audit.md:194-210`](champion-repo-reverse-audit.md) [`fourth-place-repo-reverse-audit.md:313-320`](fourth-place-repo-reverse-audit.md)

Mechanical gates must precede semantic review. Code writes numbers, identity, scope, interval, rollout, and query-result digests. Models may generate candidate mechanisms and explanations, but every material claim needs a source, falsifier, counterevidence, and verdict ceiling.[`primary-source-audit.md:86-116`](primary-source-audit.md) [`experiment-analysis-agent-evaluation-practices.md:142-167`](experiment-analysis-agent-evaluation-practices.md)

The closed policy contract freezes `G0`–`G7`, their required inputs and executor boundaries, GateReceipt fields, outcomes, ceilings, and reopen behavior. A failed hard gate limits the independent Cause Verdict and Recommendation Readiness axes according to that contract. Pilot-calibrated numeric thresholds remain open under P4 and must not be presented as an industry standard.[`wayfinder/freeze-canonical-domain-policy-contracts.md`](wayfinder/freeze-canonical-domain-policy-contracts.md) [`rca-sev-causal-confirmation-practices.md:296-304`](rca-sev-causal-confirmation-practices.md)

### 3.6 Failure, Retry, and Trace

Retries must be failure-typed: transport retries only the request; query repair only repairs the query; an evidence gap changes source or reports the gap; a reasoning conflict fans out only the unresolved branch. Every layer has a bounded budget, and original errors and evidence remain visible.[`primary-source-audit.md:131-173`](primary-source-audit.md)

Broad voting is not validation. The same model, prompt, and missing evidence can create correlated errors; majority voting may also selectively ignore timeout/parse failures. Use selective fan-out only at calibrated high-variance nodes, and use independent evidence challenges rather than vote count to promote a verdict.[`champion-repo-reverse-audit.md:142-155`](champion-repo-reverse-audit.md)

Trace should retain stage, tool input/result, errors, repairs, source reads, tokens, cost, latency, and artifact digest. Trace is a debug/provenance surface, not automatically evidence. Missing material source reads, risks, contradictions, or human timeouts must propagate to the publication gate.[`fable-opus-audit.md:90-123`](fable-opus-audit.md)

### 3.7 Causal Confirmation and Complex SEV

Temporal order, runtime identity, scope overlap, and plausible mechanism are necessary but insufficient. Stronger evidence includes controlled replay, valid holdout/control, negative control, paired rollback/re-enable observation, or a test that distinguishes competing hypotheses.[`rca-sev-causal-confirmation-practices.md:155-169,215-237`](rca-sev-causal-confirmation-practices.md)

Recovery after rollback is strong but rebuttable evidence, not automatic confirmation. It may coincide with another change, auto-healing, traffic shift, or natural recovery. Operational recovery and continuing RCA should proceed in parallel.[`rca-sev-causal-confirmation-practices.md:239-247,261-276`](rca-sev-causal-confirmation-practices.md)

Complex SEVs must not be compressed into one root cause. The owner confirmed `trigger | proximate mechanism | contributing factor | systemic condition`. A candidate may be a group and need not pretend that one file/line is sufficient.[`fable-opus-audit.md:166-179`](fable-opus-audit.md)

### 3.8 Human Gates and Handoff

Humans may rule on metric definitions, investigation scope, semantics, risk, incident state, and action ownership. “I agree” cannot replace runtime, metric, or counterfactual evidence.[`rca-sev-causal-confirmation-practices.md:133-145`](rca-sev-causal-confirmation-practices.md)

The owner confirmed separation of cause verdict and recommendation readiness. The former asks how strong the causal evidence is; the latter asks whether evidence supports an exact patch or rollback-ready packet. Neither authorizes mutation. The earlier “dual axis unconfirmed” language in `cross-research-consistency-audit.md:31-41,197` was stale and has since been corrected.

Case lifecycle, cause verdict, recommendation readiness, action approval, and incident operational state must remain separate. Handoff packets use immutable revisions with named recipient, acknowledgment, expiry, escalation, close, and reopen; reopen creates a new generation rather than overwriting the old packet.[`fable-opus-audit.md:72-102,166-179`](fable-opus-audit.md)

High-risk or large-blast-radius recommendations cannot become ready and must escalate to IC + code owner. Material human gates fail closed.[`fable-opus-audit.md:166-177`](fable-opus-audit.md)

### 3.9 Evaluation

Evaluation cannot compare final prose only. Gold must include validity, required/acceptable/forbidden candidates, cause roles, support/contradiction, runtime identity, verdict ceiling, acceptable abstentions, and action constraints.[`experiment-analysis-agent-evaluation-practices.md:49-86`](experiment-analysis-agent-evaluation-practices.md)

Measure validity-defect recall, candidate recall/precision/top-k, cause-role correctness, claim entailment, provenance completeness, unsupported claims, false-confirmed, false-ready, justified/excessive abstention, security vetoes, patch-target correctness, repeated-run stability, human time, latency, tokens, source load, and cost.[`experiment-analysis-agent-evaluation-practices.md:114-216`](experiment-analysis-agent-evaluation-practices.md) [`experiment-analysis-agent-evaluation-practices.md:255-286`](experiment-analysis-agent-evaluation-practices.md)

The order should be synthetic/planted fixtures → blind historical cases → production-like replay → narrow shadow-read. Shadow output is visible only to designated reviewers and does not enter formal decisions, Slack, documents, commits, PRs, or action workflows.[`experiment-analysis-agent-evaluation-practices.md:288-299`](experiment-analysis-agent-evaluation-practices.md)

N, top-k, risk weights, case count, latency/cost/SLA, and shadow-exit thresholds remain unknown. Pilot first, then freeze them with the owner, Engineering, and security/privacy reviewer.[`experiment-analysis-agent-evaluation-practices.md:326-353`](experiment-analysis-agent-evaluation-practices.md)

## 4. Adopt / Adapt / Reject Matrix

All entries below are **reviewer recommendations**, not owner adoption decisions.

| Candidate practice | Judgment | A/B | Source | Why | Cheapest falsifier |
|---|---|---|---|---|---|
| Code-owned bounded lifecycle | Adopt principle | A/B | Champion, workshop [`champion-repo-reverse-audit.md:194-210`](champion-repo-reverse-audit.md) | Replayable stages and explicit failure points | The same frozen case skips stages or drifts state without explanation |
| Mechanical gate before semantic review | Adopt | A/B | Old SMA, Champion [`primary-source-audit.md:86-116`](primary-source-audit.md) | Prevents model rewriting of numbers and identity | Plant an SRM/scope/SHA error; promotion must fail |
| Soft relevance with recoverable underlying evidence | Adopt | A/B | Champion [`champion-repo-reverse-audit.md:198-206`](champion-repo-reverse-audit.md) | Controls context without deleting evidence | Hide a candidate; reviewer cannot click through to the original receipt |
| Hard evidence deletion | Reject | A/B | Champion [`champion-repo-reverse-audit.md:149-155`](champion-repo-reverse-audit.md) | False negatives permanently truncate the causal chain | Put the true cause only in a “low relevance” document and see whether it disappears |
| Narrow, server-side read-only tools | Adapt | A/B | Champion, old SMA, Team 1401 [`greenfield-requirements.md:227-249`](greenfield-requirements.md) | Permissions, schema, and receipts become mechanically enforceable | Bypass the UI toggle; backend must reject an unauthorized source |
| Failure-typed bounded retry | Adopt | A/B | Old SMA, award repos [`primary-source-audit.md:131-143`](primary-source-audit.md) | Avoids full reruns and bad-state accumulation | Inject a query error; rerunning metric/source collection is failure |
| Broad self-consistency voting | Reject by default | A/B | Champion [`champion-repo-reverse-audit.md:142-148`](champion-repo-reverse-audit.md) | Correlated error, cost, and selection bias | Under one wrong source, multiple votes repeatedly output the same wrong cause |
| Selective independent fan-out | Adapt | A/B | Workshop/Champion [`kdd-source-practices.md:448-455`](kdd-source-practices.md) | Restricts cost to valuable unresolved branches | Same-batch baseline shows no correctness gain or unacceptable cost/p95 |
| Typed change inventory + runtime identity | Adopt as target requirement | A/B | Primary audit [`primary-source-audit.md:218-242`](primary-source-audit.md) | Required to tie findings to production | SCM lists one commit while runtime uses another; matching must fail |
| Metric-segment → symbol mapping | Adapt and validate | A/B | Primary audit, requirements [`greenfield-requirements.md:219-225`](greenfield-requirements.md) | Narrows to an inspectable production target | Conflicting mappings are overwritten or keyword hits are treated as verified mapping |
| Team 1286 shared replayable state | Adapt | A/B | Paper/video [`creative-team1286-practices.md:51-69`](creative-team1286-practices.md) | Humans and agents share source topology and answer path | A claim cannot open its query/source-read/runtime receipt |
| Team 1286 fail-open human timer | Reject | A/B; stricter for B | Video/paper [`creative-team1286-practices.md:82-90`](creative-team1286-practices.md) | Timeout is not approval | Ignore a material gate; continuing to publish is failure |
| Team 1401 node detail/navigation | Adapt | A/B review UI | Video [`creative-team1401-practices.md:365-419`](creative-team1401-practices.md) | Reduces source-inspection cost | Graph is visible but source digest/edge basis cannot be verified |
| Team 1401 heuristic dashed join as evidence | Reject | A/B | Video [`creative-team1401-practices.md:367-386`](creative-team1401-practices.md) | Same field name does not prove lineage | Use same-named fields with different meaning; a verified edge must not form |
| Champion/Fourth-place trace UI as evidence graph | Reject | A/B | Repo audits [`champion-repo-reverse-audit.md:285-326`](champion-repo-reverse-audit.md) [`fourth-place-repo-reverse-audit.md:228-258`](fourth-place-repo-reverse-audit.md) | Step order and debug logs are not claim evidence | Delete source receipt but retain trace; verdict must weaken |
| Append-only evidence + invalidation | Adapt | A/B | Fable audit [`fable-opus-audit.md:90-102`](fable-opus-audit.md) | New evidence does not erase audit history | Change metric definition; old claim fails to become stale/invalidated |
| Candidate diff / rollback packet, never applied | Adopt contract | A / B | Owner packet [`fable-opus-audit.md:166-177`](fable-opus-audit.md) | Makes recommendations executable without crossing authority | Repo/deploy/flag state changes after a run |
| Competition constants and hardcoded fast paths | Reject | A/B | Champion, local KDD [`kdd-source-practices.md:480-487`](kdd-source-practices.md) | Competition parameters do not represent production complexity | Change tenant/query/domain; quality or safety gates collapse |
| Uploaded-files-only substrate | Reject as target | A/B | Team 1401 [`creative-team1401-practices.md:421-441`](creative-team1401-practices.md) | Cannot prove runtime/change/ACL | Historical file conflicts with live runtime and causes misattribution |
| Blind, repeated, selective-risk evaluation | Adopt | A/B | Evaluation research [`experiment-analysis-agent-evaluation-practices.md:218-299`](experiment-analysis-agent-evaluation-practices.md) | Controls leakage, nondeterminism, and abstention risk | One demo passes but repeated verdicts flip or blind cases fail |

## 5. Competition Practice vs Production Contract Gap

| Competition practice | What it proves | What it does not prove; production must add |
|---|---|---|
| Docker + fixed repo snapshot | One public build/runtime path | Actual competition image identity, deployed production identity, config/flag/model/data state |
| DuckDB / SQL answer | Some inputs can share a query surface and produce an answer | Authoritative metric definition, independent recomputation, tenant ACL, live corpus, production lineage |
| PLAN/EXPLORE/ANSWER/VERIFY | Bounded flow and repair points | Experiment validity, SEV changepoint, causal confirmation, action risk |
| Vote/fan-out | Multiple sampled outputs | Independent evidence, causal correctness, stability, or cost-benefit |
| Trace/log/timing | Execution-debug process | Immutable claim-evidence link, freshness, authorization, invalidation |
| Source/schema graph | Source navigation and candidate joins | Production runtime/change chain, verified mapping, causal edge |
| Benchmark score/demo | Performance on a specified benchmark | A/B production external validity, false-confirmation, security, SLA |

The workshop itself discloses that external validity, difficulty/modality confounding, and run-to-run stability were not sufficiently validated.[`meeting-audio-alignment.md:168-171`](meeting-audio-alignment.md)

## 6. Authority Ledger

### 6.1 Confirmed Source Facts

- Stored hash, duration, ASR, and alignment receipts cover both meeting recordings in full; the 73 screenshots are only partial slides, so audio-only content remains represented. The original Voice Memo temporary paths are no longer available, and this synthesis makes no current re-read claim.[`meeting-audio-alignment.md:6-38`](meeting-audio-alignment.md)
- Champion fixed SHA is `bdc874...`; Fourth release is `ae0f2...`, and Phase 2 commit is `13b17...`.[`champion-repo-reverse-audit.md:19-34`](champion-repo-reverse-audit.md) [`fourth-place-repo-reverse-audit.md:55-69`](fourth-place-repo-reverse-audit.md)
- Team 1286/1401 have observed graph UI; Champion/Fourth-place interactive evidence graph was not observed. See Section 3.4.
- Existing source lacks complete production change discovery, runtime identity, typed change inventory, and metric-to-symbol mapping.[`primary-source-audit.md:218-242`](primary-source-audit.md)

### 6.2 Author Claims

- Ranking, competition score, cost, model effects, and some validation claims come from READMEs, speakers, or papers. Without organizer/runtime receipts they are not independent facts.
- Team 1286's paper describes typed discovery events and a compiler; no official repo was found for direct verification.[`creative-team1286-practices.md:216-221`](creative-team1286-practices.md)
- Team 1401's speaker claims PDF relations include verbatim quotes; the video directly proves only a page pointer.[`creative-team1401-practices.md:377-386`](creative-team1401-practices.md)

### 6.3 Reviewer Inferences

- Typed evidence substrate, append-only invalidation, runtime matcher, mapping catalog, and graph edge taxonomy are strong research recommendations, not observed award-system capabilities.
- The Adopt/Adapt/Reject matrix is planning input. It cannot freeze architecture, framework, storage, UI, or thresholds for the owner.

### 6.4 Owner-Confirmed Decisions

- Output ranked production `code | config | flag | model | data` candidates, complete evidence, and an auditable path.
- A may generate an unapplied candidate diff; B may generate a rollback-ready packet. Never mutate/deploy/rollback.
- Separate cause verdict and recommendation readiness. No state authorizes mutation.
- Invalid experiments produce validity/instrumentation/data-quality fixes only and block system hypotheses and production proposals.
- High-risk/large-blast-radius items cannot become ready; escalate to IC + code owner.
- Human rulings do not replace evidence. Material gates fail closed.
- Confirmation follows the strict Gate 0–7 principle. Complex SEV uses multi-role cause modeling.
- Handoff uses immutable revisions plus named recipient/acknowledgment/expiry/escalation/close/reopen.
- Recovery verification and continuing RCA run after rollback; human on-call/IC decides recovered/stable/close.
- A/B SLA waits for a real production-complexity benchmark.

The current authority for these decisions is the [planning decision packet](planning-decision-packet.md) and the closed [canonical policy contract](wayfinder/freeze-canonical-domain-policy-contracts.md). The earlier packet in [`fable-opus-audit.md:166-179`](fable-opus-audit.md) is retained only as historical reviewer and decision provenance.

### 6.5 Open Prerequisites and Unknowns

- **P2 — Production evidence authority:** authoritative production sources, mapping ownership, tenant/ACL boundaries, raw-evidence handling, retention/redaction, credentials, and safe read limits require named production owner, Engineering, and security/privacy decisions.
- **P3 — Observability-first review surface:** the logical Evidence Graph/Trace and view-selection contracts are frozen. The static synthetic Evidence Room prototype is M1 research and has recorded browser/mechanical checks, but the current owner review panel scored it `2.1` with `convergence.passed=false`. The current M0 slice still lacks a packet-centered review surface, and live owner/reviewer interaction and visual acceptance remain open; these artifacts cannot close P3.
- **P4 — Evaluation gold and calibration:** blind historical adjudication, code/domain and production Evidence, pilot distributions, human baseline, dispute receipts, and numeric decisions for risk weights, N, top-k, case count, stability, shadow exit, latency, source load, token use, and cost remain open.
- **Terminal adversarial review:** the single authorized attempt failed closed because the live Claude Code runtime explicitly blocked unavailable `claude-fable-5`. No session, substitute review, or findings exist; the [availability receipt](fable-terminal-review-availability-receipt.md) is the current execution authority. Any future attempt requires fresh owner authorization.
- Language, storage, vendor, agent framework, and concrete adapter implementation remain engineering selections constrained by the final logical specification, not missing product-contract decisions.

## 7. Unresolved Research Provenance

- Opening final score: `0.65` vs `0.69`; select neither.[`meeting-audio-alignment.md:78-83`](meeting-audio-alignment.md)
- Data Agent Studio per-task cost: `25c` vs `35c`; select neither.[`meeting-audio-alignment.md:168-171`](meeting-audio-alignment.md)
- Exact Qwen3.5 suffix in the opening talk: unconfirmed. `Qwen3.5-35B-A3B` appears on a different NV slide and cannot be projected backward.[`screenshot-index.md:59-66`](screenshot-index.md) [`qwen-whisper-asr-comparison.md:202-210`](qwen-whisper-asr-comparison.md)
- OpenRouter lists a Qwen STT model, but the smoke request returned HTTP 400. No valid Qwen transcript supports a fair comparison with Whisper.[`qwen-whisper-asr-comparison.md:213-230`](qwen-whisper-asr-comparison.md)
- Champion: Sol lead review completed and independently verified material anchors. Terra extractor was interrupted and produced no usable packet. Do not claim Terra double confirmation.
- Fourth-place: Terra extraction completed; it mistakenly spawned a derivative agent, which was stopped. That derivative chain adds no independent evidence level.

The last two items are orchestration provenance, not repository capabilities. They do not weaken fixed-SHA evidence, but they limit claims about multi-model confirmation.

## 8. Research Conclusions Reflected in the Current Specification

The final architecture specification incorporates these research constraints. If a later closed authority changes one, it must record the reason, evidence, and affected acceptance behavior:

1. A/B needs are the only architecture source. Old systems impose no compatibility obligation.
2. Read-only by default; the agent never deploys, rolls back, commits, pushes, or changes incident state.
3. Invalid experiments fail closed and produce no production proposal.
4. Numbers, runtime identity, scope/interval/rollout, and source receipts require mechanical verification.
5. All five production-change types enter one inventory; coverage gaps are first-class outputs.
6. Keep claim, evidence, mapping, cause role, cause verdict, recommendation readiness, case lifecycle, and action approval separate.
7. Material claims must be falsifiable and preserve support, contradiction, gaps, and alternatives.
8. High-risk ceilings, human escalation, immutable handoff, and reopen generations cannot be omitted.
9. Debug traces cannot masquerade as evidence. Graph edges cannot all be causal.
10. Evaluation must cover false-confirmed, false-ready, abstention, security, stability, human utility, latency, and cost.

## 9. Research Context Only

The following must not be frozen directly into the final spec:

- Champion/Fourth-place stage names, tool names, and attempt/vote/request/concurrency constants.
- DuckDB, Qwen, a specific ASR/OCR/video/document pipeline, Mermaid, LlamaIndex, or a UI framework.
- Team 1286 event taxonomy, 17 skills, and paper module/file names.
- Team 1401 ReAct/DRAGIN/Multi-agent/Hybrid-B routes, uploaded-files sandbox, and heuristic joins.
- Competition scores, rankings, costs, demo success, and README reliability claims.
- Old SMA pipeline, artifact names, fixed hypothesis count, thresholds, and pause points.
- Exact visual styling and interaction implementation for the review surface. P3 requires live owner/reviewer acceptance; it does not reopen the frozen logical Evidence Graph/Trace contract.

## 10. Delivery Boundary

This source-linked research synthesis distinguishes evidence, author claims, reviewer recommendations, owner decisions, and open prerequisites, and routes readers to the current authority.

The canonical [final architecture specification](final-architecture-spec.md), [implementation sequencing](implementation-sequencing.md), [planning decision packet](planning-decision-packet.md), and [Wayfinder map](wayfinder/map.md) now exist. This synthesis does not replace them and does not authorize implementation, production access, mutation, commit, push, PR, deploy, or rollback.
