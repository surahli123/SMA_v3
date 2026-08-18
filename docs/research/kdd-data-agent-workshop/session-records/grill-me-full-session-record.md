# Grill Me and Wayfinder Session Record

## Record contract

This is a faithful English export of the substantive Grill Me and Wayfinder discussion available in the Planning task. It preserves chronological order and speaker roles while consolidating repeated prompts that asked the same unresolved question. Owner statements are translated into English. Research coordination is included only when it corrected evidence or changed the decision context.

This is not a byte-for-byte system transcript. It is the complete substantive discussion record recoverable from the consolidated Planning-task skeleton, overlapping continuation records, and the visible task history supplied to this task. It excludes hidden reasoning, tool internals, secrets, machine-local paths, raw media paths, and unrelated orchestration. A coverage marker appears wherever a source records that a decision was accepted but does not preserve the intervening Owner wording or does not allow a short acknowledgement to be paired safely with one exact question.

Time is UTC on 2026-08-12 unless stated otherwise.

## 1. Destination and problem definition

### 03:39 - What must the planning deliver?

**Grill Facilitator:** Asked whether the destination should be an Owner-confirmed redesign specification for Scenarios A and B, defining inputs, outputs, evidence standards, success criteria, agent autonomy, and human gates, without implementation code. Recommended this destination so references would not dictate the design.

**Owner:** Asked whether the question concerned how to plan or the final deliverable, because the distinction was unclear.

**Grill Facilitator:** Clarified that the question concerned the final deliverable. Initially recommended a specification that an engineering team could use to create an implementation plan, while deferring the concrete technical architecture.

**Owner:** Rejected that depth. The design must allow Codex or Claude Code to implement directly, or directly build the implementation plan. The Owner challenged why the plan should not choose a concrete technical architecture.

**Grill Facilitator:** Corrected the destination: the final package should include concrete architecture, component boundaries, data models, interfaces, agent workflow, human gates, implementation sequencing, and acceptance criteria. It should stop short of writing implementation code but require no second architecture-design round.

**Owner:** Agreed, with a further requirement: the design must be deep and clear like a specification, explain the real problem, and derive every design choice from that problem rather than becoming an unsupported architecture.

**Decision:** The destination is a deep, problem-driven, implementation-ready greenfield redesign specification. It may and should choose a concrete architecture.

### 03:55-04:02 - What problem must the agent solve?

**Grill Facilitator:** Proposed a common problem statement: when a search metric misses expectations or drops, engineers cannot quickly connect the metric phenomenon to production code, configuration, flag, model, or data changes through verifiable evidence, and therefore cannot confidently decide what to verify or change.

**Delegated Research Input:** Reaffirmed that the complete meeting audio was the workshop narrative and screenshots covered only part of it. KDD winners, workshop materials, and old SMA code were rejectable references, not compatibility or migration constraints. Scenario A was post-experiment analysis; Scenario B was SEV change discovery.

**Owner:** Said the framing was broadly correct, but the practical deliverable must narrow the production code or configuration that engineers need to inspect so they can determine what to change.

**Grill Facilitator:** Refined the output to a ranked set of production candidates of type `code | config | flag | model | data`, each with relevance, required verification, and likely change location.

**Grill Facilitator:** Asked whether insufficient evidence should still produce ranked suspected directions without presenting them as a confirmed answer. Recommended yes, because pure refusal is not useful but false certainty is dangerous.

**Owner:** Agreed and required all evidence plus a clear reasoning path.

**Grill Facilitator:** Defined that path as an auditable evidence chain: metric phenomenon -> observed facts -> typed production change -> relationship and source -> confidence and gaps -> verification or falsification -> location to inspect or change. It explicitly excluded hidden chain-of-thought.

**Delegated Research Input:** Corrected repeated questioning and recorded the Owner's answer as confirmation of the evidence-chain definition and the suspected-versus-confirmed boundary.

**Delegated Research Input:** Added a primary-source correction: old KDD and SMA could inform evidence lifecycle, but neither supplied production-change discovery. Therefore the code and runtime evidence plane was a greenfield capability to design, not a migration task.

**Delegated Research Input:** Added Team 1286 and Team 1401 as independent, rejectable research inputs. Team 1286 supported shared evidence state, human gates, deterministic stages, bounded repair, and trace. Team 1401 supported inspectability, controllability, exact-query receipts, independent validation, and risk-tier approval. Neither demonstrated production telemetry, deployed-runtime identity, or production-change attribution. Uploaded-files-only operation, heuristic joins treated as evidence, and competition routing were not accepted as target architecture.

**Decision:** The agent narrows a broad metric problem to ranked, precisely grounded production candidates. It publishes complete evidence and an auditable reasoning path. It may publish suspected directions when evidence is incomplete, but never as a confirmed cause.

## 2. Actionable outputs and independent status axes

### 04:29-04:58 - How concrete must recommendations be?

**Grill Facilitator:** Asked whether Scenario A recommendations must be patch-ready: exact repository, file, symbol, configuration key or flag; a delta specification; expected metric effect; risk; verification; and optionally an unapplied candidate diff. Recommended yes, with no automatic modification or deployment.

**Delegated Research Input:** Added a clean architecture candidate for later design: case state machine, append-only evidence graph, read-only adapters, deterministic validators, falsifiable semantic claims, policy gates, immutable handoff packets, and partial recomputation. It did not answer the product question.

**Owner:** Confirmed the patch-ready boundary.

[Coverage note: The consolidated skeleton does not preserve the Owner's short patch-ready acknowledgement as a timestamped event. The visible task history contains a short confirmation in this position, and all later facilitator summaries treat the boundary as Owner-confirmed. No longer quotation is reconstructed.]

**Grill Facilitator:** Asked whether Scenario B must be rollback-ready, including exact service, environment, deployed SHA, config key, flag, model or data version, target version, and affected scope, while never executing rollback.

**Owner:** Confirmed and preferred precision down to the code file and line.

**Decision:** Scenario A produces a patch-ready, unapplied proposal. Scenario B produces a rollback-ready packet. Grounding binds to the deployed revision and should reach repository, file, symbol, and line or an exact configuration or artifact identifier. The agent never mutates production.

### 04:58-05:03 - Early verdict model and invalid experiments

**Grill Facilitator:** Initially proposed one user-visible ladder: `observed`, `suspected`, `action-ready`, `confirmed`, with no state granting mutation authority.

**Owner:** Confirmed the proposal in the available exchange.

**Grill Facilitator:** Asked what should happen when experiment validity fails, such as SRM, exposure contamination, or missing data. Recommended only validity, instrumentation, or data-quality repair; system hypotheses may remain blocked; no production-change proposal or candidate diff.

**Owner:** Added that every failed check must clearly explain why it failed.

**Grill Facilitator:** Expanded the contract: every failure reports what was checked, the data and threshold, actual result, reason for failure, invalidated conclusions, repair, and revalidation method.

**Decision:** An invalid experiment cannot support a production-change proposal. The output is limited to validity, instrumentation, or data-quality repair, with detailed failure receipts. Other hypotheses may remain visible only as blocked.

### 06:17-06:50 - The single ladder is replaced by two evidence-backed axes

**Grill Facilitator:** Noted a flaw in the single ladder: a safe mitigation may be actionable while the cause is still suspected, and a confirmed cause may still have no safe patch. Proposed independent cause and recommendation axes.

**Owner:** Confirmed that cause verdict and recommendation readiness must be separate. The Owner also required exact code-line, config, or proof grounding and challenged any readiness label that lacked independent evidence.

**Grill Facilitator:** Refined the rule: cause evidence controls Cause Verdict; action-specific evidence controls Recommendation Readiness. A mitigation with an unconfirmed cause may become action-ready only when the target is exact, blast radius is bounded, the action is recoverable, independent operational evidence supports it, monitoring exists, and stop conditions are explicit.

**Owner:** Confirmed both the separation and the action-specific evidence requirement.

**Grill Facilitator:** Later proposed final canonical enums and explained why every label requires evidence, counterevidence, failed checks, scope, and policy-matrix rationale.

**Owner:** Accepted the proposed final vocabulary and policy-evidence requirement.

**Decision:** The final Owner-confirmed enums are:

- Cause Verdict: `unassessed | suspected | confirmed | ruled_out | inconclusive`
- Recommendation Readiness: `not_applicable | blocked | proposal_ready | action_ready | rejected`

`observed` is an evidence or claim state, not a Cause Verdict. No state authorizes mutation.

**Policy consequence discussed and accepted:** A legal cause/readiness combination must be justified by a deterministic policy matrix. A Cause Verdict carries supporting evidence, counterevidence, failed checks, scope, and promotion or demotion rationale. Recommendation Readiness separately carries action-specific evidence and its failure ceiling. An exceptional human override cannot erase source history and must cite concrete, code-grounded evidence.

## 3. Risk, human rulings, incident recovery, and handoff

### 05:03-05:10 - High risk and the scope of human ruling

**Grill Facilitator:** Proposed that multi-service, full-traffic, shared-config, core-ranking or model changes, non-recoverable actions, and actions likely to enlarge a SEV be marked high risk, withheld from action-ready status, and escalated to accountable humans.

**Owner:** Confirmed.

**Grill Facilitator:** Initially framed human ruling around conflicting evidence that changes candidate ranking, verdict, action, or risk.

**Owner:** Asked for a broader model because real cases are more complex than three or four listed situations, and asked what truly requires human ruling.

**Grill Facilitator:** Expanded the model to seven areas: definition, evidence conflict, investigation scope, causal ambiguity, action and risk, incident state, and responsibility or delivery. Deterministic read-only collection, validation, candidate retention, and bounded ranking remained agent responsibilities.

**Owner:** Confirmed the broader boundary.

**Grill Facilitator:** Asked what happens when a required human gate does not respond. Recommended fail-closed behavior with recorded escalation receipts rather than a timeout default that silently continues.

**Owner:** Accepted the fail-closed recommendation.

**Decision:** Human ruling is required when a decision changes product meaning, evidence authority, authorized scope, causal promotion, material risk, operational state, or accountability. A material conflict is retained and causes fail-closed promotion rather than silent selection.

### 05:07-05:17 - Rollback, monitoring, SLA, dependency expansion, and immutable handoff

**Grill Facilitator:** Asked whether a completed rollback should lead to recovery verification, continuing RCA, or both. Recommended both: verify recovery while checking whether the rollback's time, scope, and mechanism support the causal claim.

**Owner:** Confirmed and added that humans must monitor overall system health after rollback.

**Grill Facilitator:** Proposed that the agent continuously collect read-only health evidence, while the human incident commander or on-call owns `recovered`, `stable`, and `close`. Monitoring must cover the primary metric, guardrails, errors, latency, availability, traffic and rollout scope, adjacent slices, data freshness, dependencies, and new regressions.

**Owner:** Confirmed this as the current operating model.

**Grill Facilitator:** Proposed a five-minute first-safe-check target for Scenario B.

**Owner:** Challenged the feasibility because production repositories and dependencies are complex, direct reading is token-expensive, and strong models add latency.

**Grill Facilitator:** Tried to condition the five-minute target on prebuilt mappings and indexes.

**Owner:** Rejected that claim too: even precise retrieval and scanning still require evidence, so five minutes was not established.

**Grill Facilitator:** Withdrew the target as unsupported. Recommended benchmarking intake, evidence acquisition, candidate ranking, and rollback-ready stages on realistic production-complexity fixtures before setting any SLA. Recommended the same evidence-first calibration for Scenario A.

**Decision:** Neither A nor B has a fixed deadline yet. Latency, token use, coverage, and accuracy must be measured on realistic fixtures before an SLA is set. Progress and coverage gaps remain visible during a run.

**Grill Facilitator:** Asked whether, when no direct deployed change is plausible, the agent may expand one dependency layer within authorized read-only scope, with human ruling required for cross-team, sensitive, or unbounded expansion.

**Owner:** Confirmed.

**Grill Facilitator:** Asked whether a handoff packet should be an immutable revision with named recipient, expiry, explicit acknowledgement, escalation on expiry, human-only closure, and a superseding revision on reopen.

**Owner:** Confirmed.

**Decision:** Investigation expands gradually within an authorized dependency graph. Handoff is an immutable revision with explicit recipient, acknowledgement, expiry, escalation, closure, and superseding reopen semantics.

## 4. Causal discipline and enterprise-search-specific analysis

### 05:17-05:30 - What can become confirmed?

**Grill Facilitator:** Proposed that `confirmed` require temporal order, deployed runtime and scope match, a mechanism that explains the effect, at least one independent validation, and checked counterevidence. Human agreement alone would not create causal evidence.

**Owner:** Confirmed but requested stricter standards and asked whether the proposal had been derived from external RCA and SEV success practices.

**Grill Facilitator:** Disclosed that the initial standard came from local evidence discipline, not fresh web research. A read-only external review then added falsifiable predictions, reliable validity and runtime identity, direction and segment fit, independent validation, counterfactual evidence, search for contradictory evidence, and explicit residual uncertainty. Google SRE, postmortem, Microsoft experimentation, Netflix experimentation, Cloudflare incident, and NIST RCA practices were used as research evidence rather than as Owner decisions.

**Owner:** Confirmed using the stricter Gate 0-7 approach.

**Research evidence and proposed Gate 0-7 discipline:**

1. State a falsifiable causal claim, its prediction, and a result that would disprove it.
2. Establish experiment or incident data validity before causal interpretation.
3. Prove deployed runtime identity, temporal order, rollout overlap, affected scope, and mapping cardinality.
4. Show a mechanism that explains the direction, shape, and affected segments of the metric change.
5. Seek independent validation such as reproduction, targeted replay, holdout, rollback or re-enable evidence, or an unaffected comparison.
6. Test competing explanations and retain material counterevidence.
7. Check recovery, regression, recurrence, guardrails, and monitoring when applicable; an unapplied Scenario A proposal uses applicable pre-action replay and regression evidence rather than pretending recovery occurred.
8. Require a named human causal ruling only after all applicable deterministic gates pass.

**Boundary:** These gate contents combined external research evidence and planner contract design. The Owner confirmed the stricter discipline, not every future source-specific threshold or validator implementation.

**Grill Facilitator:** Asked whether complex SEVs should avoid forcing a single root cause and instead represent trigger, proximate mechanism, contributing factor, and systemic condition independently.

**Owner:** Confirmed that complex SEVs must not output a unique failure reason.

**Owner:** Asked whether the same reasoning could be used to find experiment-analysis failure causes.

**Grill Facilitator:** Proposed an eight-part experiment failure taxonomy: invalid experiment; treatment not delivered; implementation diverged from design; expected mechanism did not occur; metric or statistical power failure; offsetting or segment-specific effects; product hypothesis failure; and external or concurrent interference. Each candidate remains falsifiable and separately evidenced.

**Owner:** Accepted the layered causal chain and eight categories, and requested enterprise-search-specific research.

**Decision:** Cause confirmation follows strict Gate 0-7 causal discipline. Complex SEV analysis represents multiple causal roles rather than one forced root cause. Scenario A uses a layered experiment causal model and an enterprise-search extension.

### 05:30-05:50 - Enterprise search evidence planes and impact scope

**Delegated Research Input:** External research identified enterprise-search-specific risks: ACL and permission synchronization, eligible and permission-trimmed corpora, connector and index freshness, lexical and vector retrieval, filtering, fusion, reranking, rendering, latency, tenant and role segmentation, and proxy-metric bias. It recommended an explicit chain from eligible corpus to interaction metric.

**Delegated Research Input:** A completed evidence audit also recommended, as engineering input rather than an Owner answer, separate lifecycle and verdict state, a new generation on reopen, append-only evidence with dependency invalidation and partial recompute, deterministic scope-by-interval-by-rollout matching with `in | partial | out | unknown`, numeric derivation receipts that enumerate source reads, fail-closed material human gates, propagation of open HIGH risk to publish gates, deterministic stable ranking, and immutable closed packets. It explicitly rated immediate final-spec freezing as NO-GO while allowing contract design to continue.

**Grill Facilitator:** Proposed eight evidence planes: cohort, permission, content/index, query understanding, retrieval, ranking, serving, and experience/measurement. Every case reports coverage, while deep investigation follows evidence rather than scanning everything.

**Owner:** Confirmed the coverage approach and asked what else should be considered.

**Grill Facilitator:** Added search-task interpretation, security and privacy, temporal state, external dependencies, evidence readiness, efficiency, and evaluation as horizontal concerns.

**Owner:** Corrected the task model: enterprise search cannot reliably label a user's search task from a query. Observable dimensions are whether a change affects Quick Find/navigation or SERP, and within SERP whether it affects traditional results or AI search.

**Grill Facilitator:** Proposed mandatory production-grounded fields `search_surface` and `serp_component`, derived from exposure, UI events, routing, and code rather than inferred intent.

**Owner:** Confirmed, with the requirement that final names and boundaries be determined by production code.

**Grill Facilitator:** Asked whether analysis should focus on the exposed component but still check the entire search journey and guardrails, analyzing cross-component changes separately before aggregation.

**Owner:** Confirmed and gave an interleaver example: a change aimed at Confluence can reorder Jira or other third-party results and indirectly change their metrics.

**Grill Facilitator:** Distinguished declared target, reachable impact, and observed impact, and proposed a cross-component impact graph from change through shared pipeline stages to affected sources, positions, impressions, clicks, success, and guardrails.

**Owner:** Confirmed.

**Decision:** The design does not require inferred query-intent labels. It uses production-grounded surface and component mappings, reports coverage over eight evidence planes, and models declared, reachable, and observed cross-component impact. A reachable component is not automatically a valid unaffected control.

**Owner:** Asked the main task to be told that the Grill was not yet finished, while allowing preliminary research findings to be shared.

**Grill Facilitator:** Reported the still-open Grill status and preliminary findings without claiming that the final specification was frozen.

## 5. Human responsibility and security boundaries

### 05:50-06:02 - Agent work versus human accountability

**Owner:** Asked what remained before ending the Grill and allowed questions in same-topic batches.

**Grill Facilitator:** Asked whether a recovered incident may close operationally while RCA remains open. Recommended independent operational and causal lifecycles.

**Owner:** Agreed and corrected the questioning rule: multiple questions are allowed when they share a topic.

**Grill Facilitator:** Proposed separate human roles for evidence review, action approval, A ownership, B ownership, and escalation.

**Owner:** Required review and approval to remain separate even for low risk, except for the distinction between a human and an agent, and asked whether the listed roles were subagents or real people.

**Grill Facilitator:** Clarified that they were human organizational roles. It then proposed two hard boundaries: a named human causal reviewer is required for `confirmed`, and a different named human action approver is required for production action.

**Owner:** Confirmed both boundaries but objected that too many human roles made the system redundant and asked where the agent's output was.

**Grill Facilitator:** Reduced the product model: the agent performs evidence collection, deterministic validation, production mapping, candidate ranking, counterevidence and gap reporting, Scenario A proposal, Scenario B rollback packet, monitoring, immutable packet generation, and partial recomputation. Humans retain only causal confirmation, action approval, and accountable operational closure.

**Owner:** Confirmed agent-led investigation and the two human gates, and required at least a real human action or incident owner for closure.

**Decision:** The agent performs the investigative work. A named human causal reviewer alone may promote a cause to confirmed. A different named human action approver controls production action. A human action or incident owner controls operational closure.

### 06:02-06:07 - Security, permissions, and sensitive evidence

**Grill Facilitator:** Asked about security veto, over-filtering, least-privilege reads, packet content, and source retention.

**Owner:** Confirmed unauthorized exposure, cross-tenant leakage, and ACL bypass as high-risk security regressions. The Owner also treated over-filtering as critical and potentially launch-blocking. Scenario A must be read-only and limited to authorized tenant data; access expansion for sensitive sources requires human approval. In explicitly approved cases, internal queries, document results, and even screenshots may enter the packet because win-versus-loss analysis may require them. The Owner preferred a graph, not only prose. Raw sensitive evidence should otherwise stay at the source.

**Grill Facilitator:** Proposed that packets store summary, locator, digest, and permission label by default. Case-scoped human approval can include named internal queries, results, snippets, or screenshots with defined recipients and expiry. Packet access cannot exceed the most sensitive source; wider sharing creates a redacted revision.

**Owner:** Confirmed the default-summary and approval model, but said the proposed graph description was unclear and requested learning from the winning-team videos.

**Decision:** Unauthorized exposure and critical over-filtering can block launch. Access is allowlisted, read-only, tenant-scoped, and least-privilege. Sensitive raw evidence remains in its source by default; explicit case-scoped approval can embed selected internal evidence. Packet authorization inherits the strictest source.

## 6. MVP, evaluation, and resource autonomy

### 06:08-06:11 - Which scenario comes first?

**Grill Facilitator:** Initially recommended building a shared evidence core followed by thin walking skeletons for both A and B.

**Owner:** Rejected that sequence. MVP must first complete Scenario A from a real experiment miss through a patch-ready proposal, or at least a complete post-experiment-analysis loop. Scenario B can follow. A and B may share evidence graph, runtime mapping, typed change analysis, and later infrastructure. The first production case should have high evidence readiness or a narrow search-surface change. Shadow-read gates require Engineering alignment. A read-only web app is acceptable; the agent must not send Slack messages or write formal documents automatically.

**Grill Facilitator:** Asked whether MVP requires a real historical case, blind review, and a read-only review surface that might be a web service or artifacts inspected by the user's coding agent.

**Owner:** Confirmed: use a real historical experiment miss, run blind review, and have the experiment owner provide the final true judgment of why the analysis was right or wrong. The review surface may be a web service or schema and artifacts inspected by another coding agent.

**Decision:** MVP completes Scenario A first. It uses a real, blind historical experiment miss and multiple de-identified fixtures. Scenario B follows on shared infrastructure. The review surface is read-only and does not grant outbound or mutation powers.

### 06:11-06:17 - Evaluation and agent resource policy

**Grill Facilitator:** Proposed that gold be an experiment-owner adjudication packet rather than an old RCA document, that false confirmation and wrong patches be highest-priority failures, that security and evidence failures be hard NO-GO conditions, and that latency and cost be independent gates.

**Owner:** Requested separate research because the group discussion could not fully align evaluation design. The Owner proposed deriving labels from experiment-owner review, experimentation triage documents, discussions, and production evidence. The Owner confirmed false confirmed causes and wrong patch proposals as highest priority, provisionally accepted hard NO-GO conditions, and accepted latency and cost as separate gates.

**Delegated Research Input:** Evaluation research supported immutable adjudication packets, separate scoring of causal result, evidence, patch, abstention, safety, stability, and cost, and local pilot calibration rather than imported numeric thresholds.

**Grill Facilitator:** Asked about tool autonomy, bounded workers, deterministic-first processing, strong-model escalation, budget exhaustion, and scope expansion.

**Owner:** Allowed the agent to choose and repeat allowlisted read-only tools. It may start multiple analysis workers, but count, concurrency, scope, tokens, cost, and timeout must be strictly bounded, and every worker must submit evidence. Deterministic code should narrow the problem before strong-model reasoning. Functionality should be proven first while measuring compute and cost; budget-exhaustion policy is a later decision. Bounded scope expansion was accepted.

**Decision:** Evaluation uses multiple cases and human adjudication, with false confirmation, wrong target, and security failures as top risks. Numeric thresholds wait for pilot distributions. Agent autonomy is read-only and bounded; deterministic narrowing precedes expensive semantic reasoning; costs are measured without weakening evidence gates.

## 7. Observability and evidence-graph product decisions

### 06:06-06:28 - Research correction: graphs were observed in Creative Track

**Delegated Research Input:** Four research tracks were asked to separate video observations, repository observations, author claims, and reviewer inference. Champion and fourth-place materials showed trace or static diagrams but no evidence-graph UI. Team 1286 showed a PiTrace source graph and question-specific answer path. Team 1401 showed a schema relationship graph and PDF knowledge graph.

**Delegated Research Input:** The source audits added important negative and boundary evidence. Champion exposed batch, CLI, Docker, logs, voting, timing, and source-line artifacts but no stable evidence-node identities, typed causal edges, contradiction or invalidation model, or interactive evidence graph. Fourth place exposed Mermaid diagrams, run-by-task matrices, a trace viewer, and a static dashboard; those were workflow or debug views, not an evidence graph. Its nominal four stages were not a strict mandatory path because forward stage skipping was possible. Both audits supported adopting trace visibility and bounded controls while rejecting self-confirmation, consensus-as-proof, receipt-free numbers, forced submission, and debug trace presented as causal evidence.

**Grill Facilitator:** Incorrectly generalized that winning solutions lacked an evidence graph, while intending to say they lacked a full production causal evidence graph.

**Owner:** Corrected the claim: Team 1286 and Team 1401 were Creative Track teams and at least one had an evidence graph. An ASR ambiguity initially sounded like a request to contact a PI or adviser.

**Grill Facilitator:** Corrected the evidence statement and paused external contact because no contact or authorization existed.

**Owner:** Clarified the ASR ambiguity: do not contact teams or advisers. Understand the designs from their MP4 files, paper, screenshots, and meeting notes.

**Delegated Research Input:** A separate ASR correction established that automatic speech recognition was routing evidence, not truth. Final research had to distinguish direct ASR agreement, screenshot-supported correction, and unresolved wording. The observed workshop naming correction was `Autopilot / Co-pilot`, not two Autopilot modes. Conflicting numeric transcriptions were not to be published as facts.

**Decision:** Learn directly from the observed Team 1286 and Team 1401 UI patterns. Do not contact external people. Their graphs are real design references, but no studied work demonstrates the full metric-to-production-change causal chain required here.

### 06:28-06:45 - What should the review surface optimize?

**Grill Facilitator:** Asked a batch of seven graph questions.

**Owner:** Asked for smaller batches and stated the central rule: nodes and graphs exist to increase observability and allow people to review the agent's process, not to chase a visually impressive image.

**Grill Facilitator:** Proposed a conclusion-centered first screen with metric phenomenon, cause verdict, recommendation readiness, key evidence, gaps, failed checks, and drill-downs.

**Owner:** Broadly agreed but said the first screen may use a graph or the two winning teams' UI patterns to show the measurement phenomenon, cause verdict, recommendation, and first-level evidence.

**Grill Facilitator:** Recommended a hybrid: conclusion summary plus local evidence graph, with full graph, timeline, code, receipt, and trace available.

**Owner:** Agreed.

**Grill Facilitator:** Asked whether every verdict- or readiness-affecting edge must be typed and expandable.

**Owner:** Agreed and asked why the system could not directly learn from the teams' MP4 UI.

**Grill Facilitator:** Confirmed that it should directly learn Team 1286's node and group detail, answer path, relayout, and references, and Team 1401's typed edges, clusters, filters, collapse and expand, locators, and relationship detail. These patterns require production semantics for metric, runtime, deployed change, code line, claim, falsifier, and recommendation.

**Grill Facilitator:** Asked whether clicking a node or edge must expose source, read time, scope, authorization, query or read receipt, validation, and failure or invalidation reason. The available record next states that this was confirmed.

[Coverage gap: The available session record does not contain the Owner's intervening reply. The following facilitator turn records this decision as confirmed.]

**Grill Facilitator:** Asked whether conflicting evidence must remain simultaneously visible instead of being hidden by an agent selection.

**Owner:** Confirmed. The Owner also allowed up to four same-topic questions in a batch.

**Decision:** The review UI is observability-first. The first screen combines conclusions with a local evidence graph. Every material node and edge exposes trust receipts. Conflicts remain visible and can block promotion.

### 06:40-06:47 - Graph scope, Trace, invalidation, and correction

**Grill Facilitator:** Asked four related questions: local versus full graph; evidence graph versus execution trace; deletion versus retention of invalidated evidence; and shared A/B graph substrate with different default views.

**Owner:** Requested the original questions and recommendation reasons, not only a list of recommendations.

**Grill Facilitator:** Restated each question and rationale in full.

**Owner:** Confirmed a local default graph with coverage and competing-claim access; allowed separate tabs or a Trace view; confirmed retained invalidated evidence; and accepted a shared graph substrate with A-specific and B-specific views.

**Grill Facilitator:** Asked whether human correction may overwrite prior evidence, whether rulings require cited reasons, and whether reviewers may restart investigation from a selected node.

**Owner:** Said direct modification is normally disallowed, except that a human may explicitly require a specific evidence item to override another when supported by concrete code-grounded evidence. Human rulings require reasons. Targeted reinvestigation is allowed.

**Grill Facilitator:** Clarified that override means a new current version linked by `supersedes` or `invalidates`, never deletion or destructive replacement of history.

**Owner:** Confirmed and requested faster Grill progress.

**Decision:** Evidence Graph and Trace are separate but linked views. Invalidated and superseded history remains visible. Human correction is append-only, scoped, evidence-grounded, and causes affected claims and recommendations to recompute. Reviewers may initiate a new investigation revision from a selected point.

## 8. Final Grill closure

### 06:47-06:50 - Final product vocabulary and MVP acceptance

**Grill Facilitator:** Compressed the remaining product questions into two short same-topic batches. It presented the final Cause Verdict and Recommendation Readiness enums, required policy evidence for each state, and illegal combinations.

**Owner:** Confirmed the recommended vocabulary. The Owner also confirmed that any exceptional human override must carry evidence and that the final policy matrix must include its evidence.

**Grill Facilitator:** Asked whether one real historical miss was sufficient for MVP, whether the old RCA could be the sole gold, and whether false confirmation, wrong patch target, and security or ACL violations should be hard NO-GO conditions.

**Owner:** Required multiple cases, required the experiment owner's real judgment, and confirmed the recommended hard gates.

**Hard-gate examples discussed:** a security miss; an invalid experiment that still receives a production patch; a proposed target not grounded to the deployed revision; an evidence-free confirmed cause; unauthorized sensitive-data use; unstable repeated ranking; or a conclusion that cannot be traced to source reads. Numeric thresholds remained a pilot-calibration question rather than a Grill decision.

**Grill Facilitator:** Summarized shared understanding: implementation-ready greenfield spec; Scenario A first; multiple cases and blind review; production-grounded evidence; separate verdict and readiness axes; invalid-experiment ceilings; exact action grounding; strict causal gates; bounded read-only autonomy; human causal and action gates; enterprise-search scope and cross-component impact; observability-first evidence graph; immutable append-only revision; calibrated evaluation; and no fixed SLA without benchmark evidence.

**Owner:** "I agree. Please confirm the Grill is finished."

[Coverage note: This exact Owner wording is available in the visible task history provided to the Planning task, but it is absent from the consolidated JSONL skeleton. It is therefore preserved without inventing a timestamp.]

**Grill Facilitator:** "The Grill is formally finished; shared understanding is confirmed."

## 9. Wayfinder follow-through

### 06:50-06:56 - Chart the map

**Wayfinder Planner:** Entered Wayfinder `Chart the map` mode. It committed to local Markdown only, no implementation, no ADR, no commit, push, or PR, and no same-session ticket resolution. It created a breadth-first map, the planning decision packet, and four immediately visible frontier tickets while leaving architecture, Scenario A, evaluation release gates, final specification, and sequencing in fog.

**Wayfinder Planner:** The four visible frontier tickets were: freeze canonical domain and policy contracts; establish production evidence authority and access boundaries; prototype the observability-first review surface; and freeze evaluation gold, adjudication, and calibration. Tickets beyond this breadth-first frontier stayed in fog rather than being created preemptively.

**Wayfinder Planner:** Reported the next frontier as `Freeze the Canonical Domain and Policy Contracts` and asked the main task to choose whether it should run in this task, the main task, or a new task.

### 06:56-07:06 - Resolve one canonical-contract ticket

**Delegated Research Input:** Directed this task to claim and resolve only `Freeze the Canonical Domain and Policy Contracts`, preserving the other three frontier tickets.

**Wayfinder Planner:** Claimed the ticket to the current Planning task before research or editing. It identified a key conflict: older material mixed `observed`, `action-ready`, and `confirmed` on one axis, and Gate 6 needed explicit handling for an unapplied Scenario A proposal.

**Delegated Research Input:** Required all durable final documents to be English. Translation of the map, packet, and open tickets did not count as resolving those tickets.

**Wayfinder Planner:** Resolved the canonical contract with independent lifecycle, stage, evidence, claim, Cause Verdict, Recommendation Readiness, approval, and incident states; a deterministic policy matrix; Gate 0-7 inputs, executors, receipts, ceilings, and reopen rules; append-only invalidation and partial recompute; separate human causal, action, and incident responsibilities; and fail-closed behavior for invalid experiments, HIGH risk, material contradiction, and timeout. The ticket closed; the other three remained open and unclaimed at that time.

### 07:08-07:31 - Route the remaining frontier

**Owner:** Asked the planner to report to the main task and determine whether new tickets should run here, in new tasks, or wait for human input or review.

**Wayfinder Planner:** Classified the remaining work:

- Production evidence authority can prepare an intake but needs real Production Owner, Engineering, Security/Privacy, Experiment Owner, and on-call evidence before closure.
- The observability-first review surface can be prototyped independently but needs live Owner or reviewer feedback before closure.
- Evaluation gold and calibration can draft a threshold-free contract but need blind-case adjudication, pilot distributions, and Engineering and Security/Privacy decisions for numeric gates.

**Delegated Research Input:** Reported that each remaining frontier was assigned to a dedicated task and retained open status. Prototype live review was the next actionable human gate. This Planning task did not reclaim or close them.

## Coverage limitations

- The available session skeleton contains 69 Owner or delegated-input events and 120 facilitator or planner text events through the export request. It excludes hidden reasoning and tool results by design.
- Session inventory found eight files carrying the same Planning task identity. The main consolidated file contains the broadest chronological record. Seven continuation files were checked and were substantially overlapping replays or bounded continuations; they did not provide a safe, complete replacement timeline.
- Some short Owner acknowledgements are absent from the consolidated skeleton even though the visible task history or immediately following facilitator text records the decision as confirmed. Material cases are marked as coverage notes or phrased as recorded confirmation rather than assigned invented wording or timestamps.
- Repeated prompts caused by research messages interrupting an unresolved question were consolidated. The question, recommendation, Owner correction or answer, and final ruling remain represented.
- Time stamps are available at event level, not as a formal turn-number ledger. No audio timing or raw transcript path is included.
- This record ends its full transcript treatment at explicit Grill closure. Later Wayfinder activity is summarized only where it established the map, resolved the canonical contract, or routed the remaining frontier.
