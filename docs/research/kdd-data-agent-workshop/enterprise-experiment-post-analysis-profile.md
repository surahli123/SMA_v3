# Enterprise Experiment Post-Analysis Operating Profile

Date: 2026-08-14
Status: supporting research profile for the owner-aligned M0-M2 Validation Slice; no implementation receipt is live; fixture, production, review, and evaluation gates remain distinct and open as stated below
Scope: enterprise Scenario A operating profile; research and design only
Authority: the real-work screenshots define the workflow problem; the owner-confirmed planning packet and canonical policy contract define safety and state semantics; KDD and DeepSeek systems are Adopt/Adapt/Reject references only

## 1. Decision Summary

The greenfield Data Agent should not begin as a general autonomous analyst or a graph-first UI. The screenshots support a packet-centered, milestone-gated operating model:

1. **M0 — Flight Readiness:** establish whether the Experiment setup and decision-metric read are trustworthy.
2. **M1 — Metric Movement and Production Grounding:** explain a valid neutral, mixed, positive, or negative result; preserve alternatives and contradictions; and map supported mechanisms to the exact deployed production state.
3. **M2 — Win/Loss Evidence:** find concrete query-level examples, replay what can be replayed, and collect human `win | loss | unclear | not_comparable` judgments.
4. **M3+ — Self-serve Productization:** begin only after the required earlier packets have been accepted on multiple real flights and a separate product, security, cost, and operating decision has been made.

On 2026-08-16, the Owner confirmed one M0-M2 Validation Slice for one real authorized Flight. Later D1-D8 and S1-S11 decisions clarify that fixtures are pre-production evidence only; M0 capability completion requires one real authorized Flight on the company laptop, a sealed core-check set, an auditable packet, and independent adjudication. No implementation receipt is currently live. This profile grants no production access, implementation authority, or P2/P3/P4 closure.

The Agent remains read-only. It may narrow evidence, rank claims and production candidates, and generate an unapplied candidate diff. It never makes the final qualitative launch decision, applies a change, deploys, rolls back, or expands access.

## 2. Evidence Boundary and Screenshot Receipt

Eight HEIC screenshots were supplied through a user-controlled Google Drive folder and inspected directly by the main orchestration task. The raw images are not included in this research package. The hashes identify the inspected bytes without publishing the source material.

| Source ID | SHA-256 | Directly observed topic |
| --- | --- | --- |
| `IMG_3687.HEIC` | `00a786fe79580deaac97a85aec2bff4c8c1a35ba48aeec49290eafc238351568` | Product purpose and four outcome classes |
| `IMG_3689.HEIC` | `e5e4a620de1608b0ba6050f412e7f370123d54555f393da1823dfb060805b5f7` | M0–M3+ roadmap, entry gates, outputs, and exit authority |
| `IMG_3690.HEIC` | `5d24cd3a3d22aa47fb7ceb599bc77f7e44571dc4e0402d65bd1d758bb172dcf2` | M0 exit, M0 exclusions, and M1 packet |
| `IMG_3691.HEIC` | `40f2e1748e846764c161bfa048fbdfb9adcc2cd867ed7da4ef47b9ab593ea7b3` | M2 query evidence and M3+ productization |
| `IMG_3692.HEIC` | `c6147e9f128fb24d5e9bbf5ecf0ef934e81c769a06076d3cc2e691f2b78e1e0d` | Cross-milestone principles |
| `IMG_3693.HEIC` | `75c984a354ab520519174607dd96a51f17b145abc9a40be5e88eb68f6fae4fc5` | Guardrails and blocked shortcuts |
| `IMG_3694.HEIC` | `5382b114d9a8243f9b56caa780c5b955d6e42f9dc64840a3adff3c984987645c` | Proposed read, validate, categorize, rank, and verdict flow |
| `IMG_3695.HEIC` | `b5faceca7ecb40e7dc6d61c97e93eb425fe78248a296314eb62f7619c41d395f` | Statsig WHN and basis-table source contract |

Evidence labels in this document are intentionally separate:

- **Screenshot observed:** visible in the eight inspected images.
- **Repo source observed:** anchored to a fixed repository SHA and exact source location.
- **Paper author claim:** stated by authors but not independently established by source code.
- **Video observed:** visible in the recorded demonstration at the cited timestamp or frame.
- **Reviewer inference:** a proposed enterprise adaptation.
- **Unknown:** cropped, absent, unavailable, or not established by the available evidence.

The screenshots are product/design evidence, not proof that the proposed pipeline is already implemented or production-correct.

## 3. Product Question and Outcome Classes

The Agent answers two questions in order:

1. Can the team trust the Flight and its decision-metric read?
2. If yes, what explains the result and which examples make the explanation concrete?

| Observed outcome | Required investigation |
| --- | --- |
| All lead metrics positive | Confirm the read and whether the movement matches the experiment intent. |
| All lead metrics negative | Confirm the read; stop or iterate unless the result was expected. |
| Decision metrics neutral | Distinguish true null, low power, offsetting wins and losses, or a segment-specific effect. |
| Some metrics positive and some negative | Determine whether the trade-off is real, whether related metrics are coherent, and which users or queries gained or lost. |

The Agent must not force one dominant explanation. A valid result may require multiple contributing factors, and an invalid or materially unknown experiment blocks system-level causal claims.

The screenshots show positive, negative, neutral, mixed, and trade-off outcomes. Expanding canonical Scenario A from a metric miss to every experiment outcome requires an explicit owner decision.

## 4. Milestone Contract

| Milestone | Question | Entry gate | Output | Exit authority | Explicit failure behavior |
| --- | --- | --- | --- | --- | --- |
| **M0 — Flight Readiness** | Can the setup and decision-metric read be trusted? | Metric policy, source owners, one authorized Flight, Experiment Owner, Independent DS Consultant, and Experiment Review Committee route are named. | `FlightReadinessPacket` | The Experiment Review Committee alone decides whether a real Flight may proceed, change, or remain blocked. | Every failed, missing, conflicting, stale, or unsupported prerequisite stays visible. Unsupported state is `UNKNOWN`. |
| **M1 — Metric Movement and Production Grounding** | Why did the result move, remain neutral, or split across metrics and segments? Which deployed state could implement the mechanism? | A separate M1 authorization and applicable production gates exist. A blocked Flight may be investigated, but each dependent claim inherits the applicable M0 publication ceiling. | `MetricMovementPacket` plus append-only `FlightAdvisoryRevision` | The Independent DS Consultant challenges the evidence; the Experiment Review Committee makes the production Flight decision. | Material alternatives, contradictions, missing production mapping, or invalidated M0 evidence cap claims and block exact recommendations. |
| **M2 — Win/Loss Evidence** | Which real queries make the change concrete? | M1 is review-ready; candidate-query method, replay/SBS integration, surface coverage, staffing, and query/trace join are authorized. | `WinLossEvidencePacket` | Human reviewers own example judgments; the Experiment Review Committee owns the production Flight decision. | Missing counterfactual, coverage, replay, or comparability becomes `UNKNOWN` or `not_comparable`, never an inferred win/loss. |
| **M3+ — Self-serve Productization** | Can validated checks run without depending on one analyst? | Earlier packets accepted on more than one real flight; product owner, UI owner, security scope, cost model, logging, support, and surface scope accepted. | A separately approved UI and operating workflow | Separate productization decision | A polished prototype, one successful fixture, or a competition score cannot close this gate. |

Product milestone state must remain separate from Case lifecycle, Stage state, Evidence state, Claim state, Cause Verdict, Recommendation Readiness, Action Approval, and Incident State.

These milestone outputs should be typed payloads or projections of the existing immutable `ReviewPacketRevision`, not three independent sources of truth. The physical choice between separate schemas and one shared envelope remains an engineering decision.

`PASS | FAIL | MISSING | UNKNOWN | NOT_APPLICABLE` are proposed milestone-check outcomes. Canonical lowercase `unknown` used by scope, mapping, or gate contracts remains a different typed value. `directional_only` is proposed experiment-read eligibility, not a Cause Verdict, Claim state, or Stage state.

## 5. M0 — Flight Readiness

### 5.1 Required input contract

`ExperimentReadContract` must include at least:

- experiment ID, owner, hypothesis, treatment intent, and affected product surface;
- assignment unit, layer, region, tenant or cohort scope, and exposure semantics;
- preregistered start, end, and fixed-horizon analysis time;
- a decision-metric set and versioned decision policy; the first M0 defaults to one decision metric, while approved preregistered co-primary metrics are supported by the target contract;
- separately labeled monitoring and diagnostic metrics;
- metric definition version, numerator, denominator, unit, grain, exclusions, attribution, owner, and interpretation;
- primary experiment-read source, source owner, source revision, and freshness;
- `use_cuped`, estimator version, covariate window, and adjusted/unadjusted label;
- arm identity and join key;
- allowlisted basis-table derivations for metrics not registered in the primary source;
- configuration, flag, scorecard, and layer receipts needed to interpret the read;
- independent recomputation contract and validator identity;
- known layer, region, surface, coverage, and calibration limits;
- named Experiment Owner, Independent DS Consultant, and Experiment Review Committee route.

### 5.2 Required deterministic checks

M0 must perform or explicitly mark unavailable:

- experiment identity and assignment reconciliation;
- preregistered runtime completion;
- primary decision-metric registration and presence;
- CUPED-mode identity and non-interchangeability;
- exposure count, allocation, sample-ratio, and duplicate checks;
- arm, layer, region, surface, tenant, and time-scope checks;
- primary-source versus UI or scorecard reconciliation;
- independent basis-table recomputation;
- numerator, denominator, unit, ratio, relative-percent, and percentage-point checks;
- metric-definition and source-owner validation;
- missing-data, freshness, late-arrival, and attribution checks;
- source-change revalidation for meaning, coverage, and attribution;
- disagreement preservation with both values, receipts, and validator outcomes.

### 5.3 M0 ceilings

- Before the preregistered runtime completes, the result is `directional_only` and cannot pass the decision metric.
- CUPED-adjusted and unadjusted reads must never be silently substituted.
- A power result cannot be called Search-calibrated while the calibration population, layer, region, or surface is unresolved.
- A critically invalid experiment permits only `validity_fix | instrumentation_fix | data_quality_fix` recommendations.
- An invalid experiment may produce a correct, exact, unapplied remediation diff only after exact-target, authority, validation, capability-isolation, and human-only delivery gates pass. Typed guidance plus a reopen condition is the first path and permanent fallback. This artifact is an `InvalidExperimentRemediation`, not a product-logic production-change recommendation.
- M0 cannot produce metric-movement explanations, win/loss judgments, autonomous launch decisions, or product-logic production-change proposals.

## 6. M1 — Metric Movement and Production Grounding

M1 begins only after M0 acceptance. Its output is a ranked set of falsifiable explanations, not a single story.

### 6.1 Required diagnostic planes

Each case must evaluate at least:

1. instrumentation and logging;
2. assignment, exposure, and attribution;
3. statistical validity and estimator identity;
4. power and uncertainty;
5. confounding and concurrent change;
6. segment or query-mix heterogeneity;
7. product adoption and interaction behavior;
8. search corpus, ACL, connector, index, ranking, reranking, presentation, latency, fallback, and cache behavior;
9. runtime, deployment, code, configuration, flag, model, and data state;
10. product-hypothesis failure with no implementation defect.

### 6.2 Claim contract

Every ranked explanation must include:

- a falsifiable claim;
- affected metric, population, window, layer, region, surface, component, and segment;
- observed and derived facts;
- supporting and contradicting Evidence IDs;
- material alternatives and coverage gaps;
- expected mechanism and observable predictions;
- cheapest safe falsifier;
- runtime and deployed-state reachability status;
- typed production candidates with exact source locators when available;
- Cause Verdict and Recommendation Readiness as independent axes;
- invalidation dependencies and recomputation boundary;
- named human questions that cannot be answered from evidence.

### 6.3 Production-grounding lane

The production-grounding lane is part of M1 because the user's required deliverable extends beyond aggregate metric explanation. It maps a supported mechanism through:

```text
metric movement
  -> product surface and component
  -> affected segment or query family
  -> query/result and ACL/corpus evidence
  -> pipeline and runtime identity
  -> rollout, interval, and reachable dependency path
  -> typed code/config/flag/model/data candidate
  -> exact deployed SHA or artifact version
  -> file/symbol/line or exact artifact locator
  -> falsifiable causal claim
  -> validation, candidate diff, or recommendation
```

Repository proximity, keyword similarity, a commit timestamp, or a graph edge is not a production tie. When mapping is unavailable, the packet may contain ranked suspected directions, but exact recommendations remain `blocked`.

## 7. M2 — Win/Loss Evidence

M2 makes aggregate explanations concrete without pretending that examples alone prove the aggregate cause.

### 7.1 Candidate sources

Candidate queries may come from:

- known dissatisfied-query sets and validity sets;
- experiment-owner hypotheses;
- segment or metric decomposition;
- top-position treatment examples replayable in control;
- observed query/trace changes that match the M1 mechanism;
- deliberately sampled counterexamples.

### 7.2 Required packet fields

Each example requires:

- stable query or trace identity;
- candidate origin and sampling reason;
- tenant, role, locale, surface, and ACL-safe scope;
- treatment and control runtime identity;
- replay configuration and data/index/corpus snapshot;
- exact query, parameters, source, and result digest;
- side-by-side artifact or explicit counterfactual gap;
- result comparability checks;
- linked M1 claim and predicted direction;
- named human reviewer;
- `win | loss | unclear | not_comparable` judgment and rationale;
- immutable source locator and packet digest.

The Agent may select and organize examples. The domain expert owns the qualitative judgment. Ranking examples never authorizes a launch decision.

## 8. KDD Source Disposition

### 8.1 Champion repository

Fixed source: `zhezh/kddcup2026_champion@bdc874fc4260e3565ae0dce041728fdf5b376709`.

| Mechanism | Decision | Enterprise use or rejection reason |
| --- | --- | --- |
| Python-owned bounded top-level orchestration | **Adapt** | Use typed M0/M1/M2 transitions, persisted gate receipts, and crash-safe resume. Do not copy competition stages. |
| Recoverable source preparation and source-line localization | **Adapt** | Preserve source locators and recoverable extraction artifacts as Evidence candidates. Add authority, freshness, ACL, digest, and claim linkage. |
| Shared structured-data runtime | **Adapt** | A common query receipt reduces accidental drift. Independent M0 recomputation must not share every failure mode with the primary read. |
| Fixed-file write boundaries and tool narrowing | **Adopt the principle** | Replace local competition file tools with server-side, allowlisted, read-only enterprise capabilities. |
| Non-terminal preflight and best-effort fallback | **Reject** | Environment checks are not experiment validity, and material failures must remain blockers or `UNKNOWN`. |
| Relevance voting that can remove recoverable evidence | **Reject** | A relevance judgment cannot erase source evidence or turn uncertainty into absence. |
| Structural solver validation as semantic validity | **Reject** | Shape, non-null, and execution success do not prove statistical, metric, or causal correctness. |
| Retry by deleting and rebuilding output | **Reject** | Corrections must be append-only, dependency-invalidating, and partially recomputable. |
| Fan-out or voting as truth | **Reject** | Correlated agents can amplify the same error; consensus is not independent evidence. |

### 8.2 Fourth-place repository

Fixed sources: `kekshibata/kddcup2026-data-agents-4th-place-solution@ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a` and Phase 2 image commit `13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65`.

| Mechanism | Decision | Enterprise use or rejection reason |
| --- | --- | --- |
| Code-controlled phases and phase-specific tool allowlists | **Adopt the principle** | Enforce adjacent transitions and server-side capability denial. Forward skips must not be possible. |
| Run-by-task matrix and experiment lineage | **Adopt for evaluation** | Use for regression, failure comparison, and repeated-run stability; never present it as a case Evidence Graph. |
| Unified structured query plane | **Adapt** | Require parameterized reads, AST allowlists, row/byte/time limits, source authority, result digests, and no general write capability. |
| Source roles such as primary and support | **Adapt** | Replace advisory routing with authoritative evidence-role contracts and explicit conflict rules. |
| Ordered step trace and trace viewer | **Adapt as Trace only** | Preserve execution order and failure visibility. Do not admit the Trace as claim evidence without an independent Evidence admission step. |
| Forward stage skip, `except: pass`, advisory hard gates | **Reject** | Material gates must fail closed and persist the blocker. |
| Forced terminal commit after budget exhaustion | **Reject** | Exhaustion preserves best-known state and abstains; it does not establish validity. |
| Model self-confirmation and model-judged material validation | **Reject as a gate** | Model judgments may draft candidates; deterministic validators and independent review decide material gates. |
| Adaptive vote or union fallback | **Reject as causal evidence** | Agreement, subset overlap, and union increase coverage but cannot confirm a cause. |
| Runtime identity without fixed Git SHA or image digest | **Reject** | Evidence must bind to the exact deployed runtime, configuration, model, and data snapshot. |

### 8.3 Team 1286

| Mechanism | Evidence class | Decision | Enterprise use or rejection reason |
| --- | --- | --- | --- |
| Source graph, node/group detail, and question-specific answer path | Video observed; paper author claim for generation design | **Adapt** | Use for source orientation and recruited-artifact review only after adding authority, typed edges, production identities, contradictions, falsifiers, freshness, and invalidation. |
| Source locator and click-through detail | Video observed | **Adopt the interaction principle** | Reviewers need a short path from a claim to source grain, owner, freshness, query, result, and receipt. |
| Separate source graph and Trace-like thread | Video observed | **Adopt the separation principle** | They answer different questions. The observed surfaces do not prove a canonical evidence ledger. |
| Human ambiguity wall | Video observed; paper author claim | **Adapt** | Use fail-closed human gates for material ambiguity. Reject the observed timeout fallback as approval. |
| Human-reviewed immutable milestone packet | Reviewer inference; target-system requirement | **Adopt as target design** | PiTrace did not prove this production packet. The deliverable should be a reviewed packet rather than chat, layout, or narration. |
| Plan, thought, thread, or narration as evidence | Video observed as UI; reviewer rejection | **Reject** | These are proposal or Trace artifacts. Claims require independent evidence and falsifiers. |

### 8.4 Team 1401

| Mechanism | Evidence class | Decision | Enterprise use or rejection reason |
| --- | --- | --- | --- |
| Schema/KG search, clusters, filters, collapse/expand, and click detail | Video observed | **Adapt** | Navigation is useful, but extracted and heuristic edges remain assertions until verified. |
| Exact SQL, result, and event-log receipt | Video observed | **Adopt the exact-receipt principle** | It supports M0 recomputation, M2 replay, and independent review. The demonstrated prompt already supplied the join and formula. |
| Co-pilot interaction and tool controls | Video observed; server enforcement unknown | **Adapt** | Use risk-tiered approval for sensitive reads, permission expansion, generated diffs, or action lanes. Do not interrupt every safe read. |
| Uploaded-files-only evidence boundary | Video observed | **Reject** | It cannot establish current experiment, warehouse, deployment, flag, config, model, data, or runtime identity. |
| Heuristic or fixture-built join as evidence | Video observed; reviewer inference about generalization | **Reject** | Same-name joins are mapping candidates, not observed facts. |
| Default-on arbitrary Python | Video observed | **Reject** | Arbitrary Python with production credentials creates a HIGH blast radius. |
| Decorative or untyped graph edges | Video observed | **Reject** | Layout, proximity, grouping, or color cannot silently represent lineage or causality. |

Neither team proves an immutable production review packet or the complete production causal chain.

## 9. DeepSeek Harness and Plugin Disposition

Initial report import receipt: `432bc905b73c8cdd507af5304a53cb7beb4584fc3545f106d9578dfa9945e109`. The ongoing cross-host trajectory audit may supersede the Trace-specific conclusions below; it cannot silently change the canonical Evidence, policy, or authority contracts.

Fixed sources:

- `deepseek-ai/deepseek-harness@47f943859bef60e4160492346772ded9b24f765a`;
- `alchaincyf/deepseek-harness-orange-book@25ef10eddeae4924f43037f9b5896e9cc41e03b5`;
- `icesixgod/codex-trajectory@2f10022557bbc4ffefce1eb656ab2e09dd55ff0e`;
- `cordiverse/paper@948a07b369c62adb3b12e102458be5c18dfb69b9`;
- source-reviewed plugin snapshots listed in [DeepSeek Harness practices](deepseek-harness-practices.md).

| Mechanism | Evidence class | Decision | Enterprise use or rejection reason |
| --- | --- | --- | --- |
| Durable turn, step, tool, retry, and terminal lifecycle events | Official source fact | **Adapt** | Use for bounded execution and debugging. Bind every admitted source read to authorization, tenant, snapshot, redaction, result digest, and Evidence admission. A logged event is not Evidence. |
| Monotonic tool guards | Official source fact | **Adopt the invariant; adapt the implementation** | A later policy layer must never convert deny to allow. Put the hard source and authorization broker outside the replaceable harness/plugin tree. |
| Fail-closed one-shot approval | Official source fact | **Adapt for bounded reads only** | Missing or invalid approval must deny. Keep it separate from causal ruling, packet acknowledgement, Recommendation Readiness, Action Approval, and incident authority. |
| Crash-tail repair with explicit unknown outcome | Official source fact | **Adopt the invariant; adapt the implementation** | Interrupted reads become `unknown`, never success. Resume requires unchanged bundle, policy, source snapshot, authority, and idempotency receipts; no blind retry. |
| Explicit retry events and bounded budgets | Official source fact | **Adapt** | Preserve attempt and fallback receipts under case, source, time, cost, and retry ceilings. Reject unbounded `always` retry and retries after authorization, ACL, or unknown-side-effect failure. |
| Context compaction | Official source fact | **Adapt for model context only** | Evidence, contradiction, authority, invalidation, and gate records remain outside compaction and re-addressable by digest. |
| Effect-bound lifecycle cleanup and quiescence | Official source fact plus paper author claim | **Adapt** | Use for reviewed adapter unload and resource hygiene. It is not malicious-plugin containment and cannot retract external emissions or Evidence writes. |
| Read-only trajectory projection | Third-party source fact | **Adapt as Trace only** | Learn from safe summaries, opt-in detail, stable raw-event indices, path confinement, and parser warnings. Cross-host Codex, Claude Code, and Cursor normalization remains under active review. |
| Structured search results with source and uncertainty | Third-party plugin source fact | **Adapt the contract idea only** | Replace community execution and CLI fallback with enterprise-owned, ACL-aware, snapshot-bound read adapters and per-attempt receipts. |
| Dynamic or model-authored plugins, Code Runtime, shell, Python, and marketplace install | Official and third-party source facts | **Reject** | These surfaces violate the Agent's read-only, least-privilege, fixed-bundle, and supply-chain boundaries. Official `node:vm` and isolation labels are not security boundaries. |
| Persistent model-supervised memory and workspace rewind | Third-party plugin source facts | **Reject** | Cross-case writeback, forgetting, restore, deletion, and workspace mutation cannot enter the canonical Case Workspace or Evidence path. |

The smallest safe harness subset is a SHA-pinned reviewed bundle of allowlisted read-only adapters, a bounded execution loop, a non-replaceable enterprise source/policy broker, deterministic crash/resume handling, and a separate read-only Trace projection. Framework, vendor, runtime, plugin API, and serialization choices remain unfrozen until a cross-host conformance spike passes the required controls.

## 10. Minimum Safe Architecture

The operating profile fits the canonical greenfield architecture through the following logical capabilities. This list does not require one deployable service per item:

1. **Replaceable Host and Execution Adapter capability** lets Codex, Claude Code, Cursor, or a future harness run the same typed workflow without becoming architecture authority. Every host must pass one conformance contract for lifecycle, budgets, cancellation, redaction, failure propagation, and Trace separation.
2. **Experiment Contract Registry capability** extends the existing Case and contract schemas with experiment identity, decision policy, preregistered runtime, layer, scope, estimator mode, owners, and source contracts.
3. **Read-only Experiment Adapter** retrieves the authoritative experiment read and emits a source receipt.
4. **Independent Metric Validator** recomputes allowlisted metrics through a separately versioned path and emits reconciliation receipts.
5. **Milestone-policy capability** extends the existing Gate and Policy Engine with product-milestone entry and exit contracts without conflating them with Cause Verdict or Recommendation Readiness.
6. **Append-only Evidence and Derivation capability** uses the existing Case Workspace and Derivation Engine to preserve sources, queries, results, digests, failures, conflicts, invalidations, and dependencies.
7. **Metric Movement Analyzer** generates typed, falsifiable candidate explanations and material alternatives after M0 acceptance.
8. **Production Identity and Change Mapper** resolves runtime, deploy, code, config, flag, model, and data identities with `scope × interval × rollout` receipts.
9. **Query Example and Replay capability** fits the existing adapter SDK and discovers candidate examples while producing exact query, replay, and comparability receipts.
10. **Claim Registry and Gate 0–7 Evaluator** keeps claim state, Cause Verdict, Recommendation Readiness, contradictions, and reviewer rulings explicit.
11. **Immutable Packet Builder** builds M0, M1, and M2 packet revisions bound to source and policy digests.
12. **Review Surface** projects packet state, Evidence Graph, tables, timelines, exact queries, code, diff, receipts, and Trace without becoming a source of truth.
13. **Host Trace Adapter capability** normalizes host events into a noncanonical, read-only Trace projection with raw-event locators, parser warnings, redaction, and explicit heuristic fields. Its final cross-host envelope remains pending the active trajectory audit.
14. **Evaluation Harness** runs blind cases, invalid experiments, drift cases, missing-source cases, cross-host conformance cases, and repeated-run tests under sealed policies.

No component receives production write, SCM write, deployment, rollback, messaging, or publication authority.

## 11. Review-Surface Information Architecture

The first screen should be milestone and packet centered.

### 11.1 Case header

- experiment ID and intent;
- decision metric and `use_cuped` mode;
- preregistered runtime state;
- layer, region, surface, and population;
- source freshness and authority;
- current milestone and gate status;
- packet revision and digest;
- strongest blocker and next safe action.

### 11.2 M0 workspace

- checklist grouped by experiment, assignment, metric, source, estimator, recomputation, and scope;
- explicit `PASS | FAIL | MISSING | UNKNOWN | NOT_APPLICABLE`;
- primary-versus-recomputed result comparison;
- disagreements shown before explanations;
- source owner, query, result digest, and receipt detail;
- named approver and acceptance receipt.

### 11.3 M1 workspace

- ranked claims with supporting and contradicting evidence side by side;
- metric and segment decomposition;
- material alternatives and open questions;
- production candidate table with runtime reachability and exact target status;
- cheapest falsifier and expected observation;
- Cause Verdict and Recommendation Readiness as independent fields;
- optional unapplied candidate diff only after exact target and action evidence gates.

### 11.4 M2 workspace

- candidate-query queue and discovery origin;
- treatment/control or replay comparison;
- exact query, result digest, runtime, corpus, and ACL-safe locators;
- SBS view and coverage limitation;
- human `win | loss | unclear | not_comparable` judgment;
- links back to the M1 claim and predicted mechanism.

### 11.5 Secondary views

- **Evidence Graph:** typed relationships among admitted evidence, derived facts, mappings, claims, contradictions, verifications, invalidations, and recommendations.
- **Trace:** host-normalized tool calls, retries, errors, budgets, execution order, raw-event locators, parser warnings, redaction status, and explicit heuristic fields. Trace remains operational context and never satisfies an Evidence or causal gate.
- **Timeline:** experiment, exposure, data, deploy, flag, config, model, index, and evidence effective times.
- **Exact proof:** source receipt, query, result digest, code locator, deployed SHA, diff, or packet digest.

Graphs should be used only when relationships are easier to inspect than in a checklist, table, timeline, diff, or receipt.

## 12. Acceptance Evidence

The operating profile is not acceptable without at least these cases:

1. valid positive flight with matching intent;
2. valid negative flight;
3. true-null neutral flight;
4. underpowered neutral flight;
5. offsetting aggregate effects;
6. segment-specific effect hidden by aggregate movement;
7. coherent metric trade-off;
8. unrelated coincident metric movement;
9. preregistered runtime not completed;
10. CUPED/unadjusted mode mismatch;
11. decision metric absent from the registered metric set;
12. primary-source versus independent-recomputation disagreement;
13. metric definition or denominator drift;
14. source migration with changed meaning or coverage;
15. layer, region, tenant, surface, or calibration mismatch;
16. missing counterfactual or replay data;
17. query not comparable across treatment and control;
18. repository commit never deployed to the flight;
19. deployed config, flag, model, or data change with no code commit;
20. concurrent changes requiring a multi-cause explanation;
21. exact target unknown, requiring abstention;
22. material source timeout, partial page, stale receipt, or permission denial;
23. adversarial prompt requesting autonomous ship, write, deploy, or rollback;
24. repeated identical evidence replay proving deterministic policy and packet output;
25. model variation proving that live semantic divergence remains visible rather than being hidden as deterministic.
Hard NO-GO failures remain false `confirmed`, a wrong exact target, or a security, ACL, tenant, or authorization violation.

If the owner later approves an agent-agnostic cross-host conformance spike, that engineering spike—not the product operating profile as a whole—must additionally test:

- the same sealed fixture through each selected host, proving equivalent policy receipts and packet semantics while host-specific Trace differences remain visible;
- malformed, truncated, unknown-version, or unauthorized host logs producing parser warnings and Coverage Gaps without changing Evidence, Claim, Verdict, or packet truth;
- a replaceable plugin or host adapter attempting to bypass a deny decision, read another tenant, expose a secret, write memory, mutate a workspace, or promote Trace to Evidence.

## 13. Open Decisions and Required Human Evidence

### Owner-confirmed M0 and advisory contract

The following decisions are closed product semantics, not open implementation choices:

- Every packet and receipt declares `evidence_class = fixture | production_authorized`. Fixture evidence can prove deterministic behavior but cannot establish production-backed M0 capability.
- A production start receipt seals a versioned `core_check_set`. Its fixed floor is CHK-01, CHK-03, the core assignment/exposure part of CHK-05, CHK-06, CHK-08, CHK-12, CHK-14, CHK-19, and CHK-16. The parity part of CHK-05 and CHK-11 enter the core only if their production sources were declared available before unblinding. Missing or unknown core outcomes leave capability unproven.
- `m0_capability_state = not_demonstrated | demonstrated` is a program state separate from the Flight's stored `analysis_use`. One correctly blocked real authorized Flight may demonstrate capability after independent adjudication, but it remains non-decision-grade and carries the typed Coverage Gap `positive_production_path_unverified`.
- The first real Flight uses the D8 laptop boundary unless a stricter company policy requires full P2: existing Owner read-only entitlement, write-denial attestation, named existing sources and owners, laptop-local raw evidence, a stated local retention period, and exports limited to the packet, receipts, and a redaction manifest with digests. Every such packet carries `authorization_scope = laptop_owner_entitlement`; this never means P2 closure.
- Authorization and redaction are orthogonal typed axes. An authorized read may still be non-exportable or redaction-blocked; a successfully redacted artifact does not establish source authorization. Any new Coverage Gap kind requires an explicit versioned registry decision; Phase A code enums do not silently define product policy.
- Production metric definitions, tables, schemas, routing, owners, ACLs, retention, thresholds, and timers remain `PRODUCTION_BINDING_REQUIRED`. Query Success is the union `TraditionalResultSuccess OR AIAnswerSuccess`; its components are diagnostic, share the Flight's frozen grain/population/window/overlap policy, and cannot acquire hidden post-hoc guardrails.
- Check 14 records `independence_class = independent_source | independent_transform | same_pipeline`; M0 requires at least `independent_transform`. Primary and recomputed reads bind the same immutable source snapshot, interval, scope, and receipt; the resulting limitation is the typed Coverage Gap `shared_source_snapshot`.

M1 publishes an append-only `FlightAdvisoryRevision`, never a mutable advisory flag. It records the official Query Success result; advisory value `recommend_pass | recommend_change | recommend_block | insufficient_evidence`; evidence IDs and lineage classes; counterevidence; falsifier and execution state; `query_evidence_state`; selection timing; tested-analysis inventory; independent-confirmation receipt; Independent DS challenge record; and supersession. It is separate from Cause Verdict, Recommendation Readiness, Action Approval, and Incident State.

Challenge lineage is exactly `independent_instrumentation | shared_logs_independent_definition | derived_from_decision_metric_inputs`; the third class is not independent. Human judgment is decision-bearing only under a preregistered blind rubric and applicable P4 authority; otherwise it remains exploratory. A post-unblinding stream may trigger `urgent_investigation`, but until an independent confirmation receipt exists it cannot carry `recommend_change` or `recommend_block` and the advisory remains `insufficient_evidence`.

Advisory publication and candidate-diff generation are separate. `candidate_diff_eligibility` requires exact deployed artifact/SHA, reliable file/symbol attribution, runtime/scope reachability, supported mechanism, material-alternative and counterevidence challenge, independent code-domain review, and LOW or MEDIUM risk. HIGH risk or large blast radius fails closed. M2 corroboration is mandatory for relevance, ranking, AI-answer, result-presentation, or other user-visible search semantics; only a versioned applicability rule may mark it not applicable for a deterministic technical correction whose evidence does not depend on query-level user value. Every diff remains syntactically valid, `not_applied`, generated outside a source worktree, human-only, and unreachable by automation or apply/commit/PR/deploy/rollback interfaces.

This profile does not close the existing open gates.

### Production authority and access

Production Owner, Engineering, and security/privacy must identify:

- authoritative experiment, metric, scorecard, configuration, flag, deployment, SCM, model, data, index, query/trace, and replay sources;
- source owners and semantic versioning authority;
- tenant, role, locale, region, layer, and surface boundaries;
- raw query, result, screenshot, and side-by-side evidence policy;
- retention, redaction, deletion, and packet-sharing rules;
- read budgets, freshness, fallback, and load ceilings;
- exact runtime-to-repo and experiment-assignment-to-runtime mapping ownership.

### Review-surface acceptance

The owner and real reviewers must confirm that the M0/M1/M2 workflow:

- exposes blockers before explanations;
- reduces time to inspect exact proof;
- makes `UNKNOWN`, contradiction, stale evidence, and human authority obvious;
- does not confuse Trace, narration, or graph layout with Evidence;
- supports the actual review meeting and handoff process.

### Evaluation and calibration

Experiment owners, code/domain reviewers, the Evaluation Owner, Engineering, and security/privacy must provide sealed historical cases, blind adjudication, replay or archival authority, and pilot measurements before numeric top-k, stability, latency, cost, token, SLA, or shadow-read gates are set.

### Owner-aligned validation program and remaining product decisions

**Resolved:** one Flight is one A/B Experiment; M0 is the first gate and main deliverable; M1 and M2 belong to the same one-Flight, four-to-six-active-week validation program; the first M0 defaults to one decision metric while the target supports approved co-primary metrics; invalid Flights may receive a gated unapplied validity/instrumentation/data-quality remediation diff; production responsibilities are split among the Experiment Owner, Independent DS Consultant, and Experiment Review Committee; the primary builder leave from 2026-08-24 through 2026-09-14 is excluded from active time; and old SMA facts are candidates rather than production authority.

No implementation scope is currently authorized. Fixture work, the D8 laptop run or P2 production path, M1/M2 implementation, live review acceptance, and Committee Acceptance remain separately gated.

The Owner alignment record resolves Flight identity, decision-metric cardinality policy, invalid-Experiment remediation, production responsibility split, program sizing, and legacy-asset authority. The owner and named domain authorities must still decide:

1. whether later milestones expand Scenario A beyond metric misses to every positive, negative, neutral, mixed, and trade-off outcome;
2. which P2-authorized source inventory and owners can satisfy the closed D4/D6 recomputation contract and who owns its production binding;
3. who owns semantic revalidation when a metric source, table, join, estimator, or event definition migrates;
4. which exact production values bind the closed sufficiency and comparison rules; the single stored `analysis_use` and derived eligibility mapping are no longer open;
5. which packet-centered M0 hierarchy and interactions real reviewers accept through P3;
6. whether an M1 packet may be review-ready while Recommendation Readiness remains `blocked`;
7. for M2, which raw query, result, screenshot, side-by-side, and Trace fields may enter the packet and which must remain redacted or linked only by digest;
8. for M2, who owns labels, disagreement adjudication, reviewer conflict, and unresolved `not_comparable` cases; and
9. which host runtimes and versions are in scope for any later agent-agnostic conformance spike, and who owns their log/hook access, redaction, retention, and parser-version policy.

Until decided, these remain explicit product or authority gaps and cannot be inferred from KDD, DeepSeek Harness, Codex Trajectory, a prototype, or fixture success.

## 14. Canonical Reconciliation Status

The 2026-08-16 reconciliation is complete for the Owner-aligned program boundary:

1. `ExperimentReadContract` and `FlightReadinessPacket` are canonical M0 entities;
2. M0 is the first gate and main deliverable and ends before production-cause analysis;
3. M1 Metric Movement and M2 Win/Loss are planned in the same one-Flight validation program after M0 and their named gates;
4. implementation sequencing and the CE plan define `M0-F0`-`M0-F5` as a planned local pre-production backlog requiring a new exact-digest start receipt;
5. the evaluation plan includes a threshold-free M0 fixture contract and false-readiness hard veto; and
6. P2 production authority, P3 M0 packet-surface acceptance, and P4 evaluation/calibration remain open.

`MetricMovementPacket`, `WinLossEvidencePacket`, M1/M2 source authority, causal ranking, query replay/SBS, cross-host collection, and the existing M1 Evidence Room are planned validation-program capabilities and remain unimplemented and unauthorized. Any M0 remediation or M1 product candidate diff must pass its distinct evidence/change-type eligibility gate; neither advisory publication nor fixture success grants diff eligibility.

## 15. Completion Claim Boundaries

- P1, the closed canonical domain and policy contract, remains current authority. M0/M1/M2 does not replace its lifecycle, Stage, Evidence, Claim, Cause Verdict, Recommendation Readiness, Action Approval, Incident State, or runtime G0-G7 contracts.
- No M0 implementation start is currently authorized. Fixture execution, the first real-Flight laptop run, M1/M2 implementation, production access, and formal decision use require their named receipts and gates.
- U8 proves only a fixture-backed Scenario A workflow and immutable packet shape. It cannot establish authoritative production reads, production fidelity, exact deployed mapping, or real M1 completion.
- Real M1 production grounding requires P2 closure and U11's one authorized production-evidence path, or a narrower case-specific archival-snapshot authority receipt with the exact permitted scope. A no-identity case cannot count as exact-target acceptance.
- P2 production authority, P3 live review-surface acceptance, and P4 evaluation/adjudication/calibration remain open. Neither this profile, the imported DeepSeek report, nor the active trajectory research closes them.
- The DeepSeek report supports a future harness conformance spike; it does not select a framework, plugin system, runtime, provider, or Trace schema.

## 16. References

- [Planning decision packet](planning-decision-packet.md)
- [Owner alignment record](reviews/2026-08-16-opus5-m0-alignment/owner-alignment-record.md)
- [Canonical architecture specification](final-architecture-spec.md)
- [Canonical domain and policy contract](wayfinder/freeze-canonical-domain-policy-contracts.md)
- [Champion repository reverse audit](champion-repo-reverse-audit.md)
- [Fourth-place repository reverse audit](fourth-place-repo-reverse-audit.md)
- [Team 1286 practices](creative-team1286-practices.md)
- [Team 1401 practices](creative-team1401-practices.md)
- [DeepSeek Harness practices](deepseek-harness-practices.md)
- [Enterprise search experiment failure practices](enterprise-search-experiment-failure-practices.md)
- [Experiment-analysis evaluation practices](experiment-analysis-agent-evaluation-practices.md)
