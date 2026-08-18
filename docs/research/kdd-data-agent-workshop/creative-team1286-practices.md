# Team 1286 PiTrace: Practices to Adopt and Avoid for the Greenfield Data Agent

Date: 2026-08-11
Scope: research-only. No production access; no agent implementation, deployment, or modification.

## 1. Conclusion First

What is most worth learning from PiTrace is not the KDD task flow, but three control principles:

1. Humans and the agent see the same structured, replayable task state;
2. Deterministic gates control numerical execution, validation, and publication, while only points of semantic uncertainty go to a model or human;
3. Human feedback and memory may guide an investigation, but cannot masquerade as evidence or bypass a gate.

These principles are valuable for both A (post-experiment) and B (SEV), but nearly all require **Adapt**. PiTrace's evidence graph is designed for an uploaded workspace and benchmark answers; it does not contain production telemetry, an experiment-validity layer, a deploy/config/flag/model/data timeline, an exact deployed SHA, or rollback evidence. Adopting it unchanged would conflict with the current greenfield requirements.

This report presents 14 judgments: `Adopt 3 / Adapt 8 / Adopt the principle but Adapt the implementation 1 / Reject 2`. Even `Adopt` refers only to a principle; it does not mean adopting the authors' modules, filenames, 17 skills, or competition parameters.

## 2. Evidence Coverage

Fresh source audit: 2026-08-11. Conclusion status is divided into four categories:

- **Paper claim**: A claim made by the authors in the Team 1286 report. Page numbers refer to physical pages in the PDF.
- **Speaker claim**: Content explicitly stated by the speaker in the video's audio track. Timestamps come from a fresh Whisper transcription cross-checked against the embedded subtitles.
- **Visual-only**: Visible only in the video image, with no corresponding spoken statement.
- **This report's inference**: An adaptation judgment made by applying the A/B requirements to the materials. It is not a Team 1286 claim.

Evidence strength is also kept separate: agreement among paper + speaker + visual is **stronger corroboration within these materials**; paper alone or demo visuals alone are **single-source**; effects in A/B production are always **unknown**, because the materials contain no production evaluation.

### Paper

- Source label: `Team 1286 paper` (raw PDF not included because of size, privacy, and source availability)
- SHA-256: `1114180be5df7c6a00217518b4602c18e51e5cd882bf4f559521819c56b0a572`, matching the value provided in the task.
- Fresh coverage: all text was re-extracted first, then all 23/23 pages were re-rendered and inspected page by page. The visual review covered the main-text architecture diagrams (PDF p1–2), main-text claims/limitations (p3–6), evidence/dependency/skill/config tables (p7–16), the complete architecture and two loop diagrams (p17–19), and token/runtime tables and charts (p20–23). There were no unreadable pages. All page numbers refer to physical pages in the PDF.

### Video

- Correct Drive source: file ID `10hlBEPLNNRKmeW7t-oAB1yzkLew8SdXU`, URL `https://drive.google.com/file/d/10hlBEPLNNRKmeW7t-oAB1yzkLew8SdXU/view?usp=sharing`. Fresh metadata gives the name `creative_team1286_video.mp4` and duration `07:58`. The source download is `35,858,783 bytes`; SHA-256 `492976a5e113b9d7aa15f5dca262c9add5986b3d16d102adfeba48348c29b15b`. It is byte-for-byte identical to the previous local Team 1286 file.
- Container: 1920×1080 H.264 at 25 fps; 48 kHz stereo AAC; English `mov_text` subtitle stream; format duration `478.000s`.
- Fresh audio coverage: the complete audio track was re-extracted as mono 16 kHz WAV and independently transcribed from `00:00:00–00:07:58.04` with `whisper.cpp small.en`, CPU-only, with 0 fallback. The first run with the default backend crashed; the CPU-only rerun succeeded, so this did not create a coverage gap. The embedded subtitles cover `00:00:00.579–00:07:57.695`; they omit narration around `01:41.88–02:00.28` and `05:11.68–05:24.48`, which the fresh Whisper transcript filled in.
- Fresh visual coverage: 48 frames were sampled every 10 seconds across `00:00–07:50`, and UI frames at claim transitions and subtitle gaps were also reviewed. The ending from `07:50–07:58` was checked separately with keyframes and audio. There were no uncovered intervals.
- Confidence: the principal claims in the two transcriptions agree; minor punctuation differences and slips of the tongue do not affect the practices below. The video is a demonstration and a set of author statements, not an experiment on A/B production effects.

### Rejected Incorrect Candidate URL

- Fresh Drive metadata for file ID `1ev10EJT5_yAVItYGCl1wdPRex798Mzng` identifies it as `creative_team1401_video.mp4`, not Team 1286.
- Receipt: `41,147,647 bytes`; SHA-256 `b50c79b6be38c8344e890eefac7f7c15d2bb946dbc471c4f38ed082bd07fbf34`; duration `512.480s`; 1920×1200 H.264 + AAC; no subtitle stream.
- **Reject attribution**: this report did not inspect or use its content and did not attribute any Team 1401 claim to Team 1286.

## 3. Adopt / Adapt / Reject

### P1 — Shared, Replayable Evidence State: **Adapt**

- **Problem addressed**: Looking only at the final answer or chat history does not allow reviewers to verify what the agent saw, what it missed, or how it reached a conclusion.
- **Mechanism**: Question-blind discovery first writes sources, relationships, and concerns into a graph/artifact; the answer loop then writes the contract, evidence map, plan, code, review, and output. The paper explicitly states that the app renders solver artifacts/events. **This report's inference**: in greenfield, the UI can only be a view of this state; it cannot become another source of truth.
- **Primary evidence**: Paper p1–4, p17–19; Video `02:05–03:19` shows the discovery graph, source drill-down, thread, and solution graph.
- **Applicable to**: A + B.
- **Requires**: metric/source registry, typed discovery/query tools, immutable event log, stable IDs, digest/freshness/auth; humans can review without having to approve every step.
- **Risks/failures**: The authors acknowledge that discovery labels/grouping vary across runs and shallow parsing can miss evidence (Paper p5); a cited frame in the UI is only a provenance aid, not formal lineage (p6). Video `02:54–03:19` calls the thread the reasoning/entire loop; production audit should not save or depend on hidden chain-of-thought, only tool calls, stage decisions, receipts, citations, and brief explanations.
- **Greenfield comparison**: The current requirement is a graph from metric → runtime → repo/symbol → deployed change → hypothesis. PiTrace covers only workspace source → answer and lacks experiment/deploy/config/flag/model/data planes, so it cannot be adopted unchanged.

### P2 — Separate Discovery from the Specific Diagnosis: **Adapt**

- **Problem addressed**: Re-scanning all materials for every question, or allowing the current question to distort the source inventory too early.
- **Mechanism**: First build a question-blind profile/discovery and save reusable state; after the question arrives, recruit evidence under a contract.
- **Primary evidence**: Paper p2, p4, p18–19; Video `01:30–02:50` demonstrates uploading, completing discovery, and viewing sources/relationships before a question is introduced.
- **Applicable to**: A + B.
- **Requires**: source topology/ownership cache, targeted refresh, incident/experiment window, freshness receipt; no default human gate is required.
- **Risks/failures**: Unbounded discovery is expensive and becomes stale; for a SEV, scanning the entire corpus first may miss the incident latency target. The authors also state that cheap orientation under-parses (Paper p5).
- **Greenfield comparison**: Adapt this into a "reusable registry + targeted refresh around the experiment/incident." Otherwise, it conflicts with freshness, exact affected scope, and B's timeliness requirements.

### P3 — Deterministic Stages, Independent Review, Bounded Repair, and the Ability to Abstain: **Adopt the Principle, Adapt the Stages**

- **Problem addressed**: One-shot execution mixes understanding, evidence gathering, computation, and validation; errors are difficult to localize, and retries may loop indefinitely.
- **Mechanism**: contract → evidence → plan → deterministic code → execute → validate → independent review → accept/repair/abstain; the runner manages timeouts and a repair cap.
- **Primary evidence**: Paper p2–4, p19; Video `05:24–06:25` explains contract, evidence, plan, code, execute, validate, and then accept or another loop, step by step.
- **Applicable to**: A + B.
- **Requires**: frozen inputs, deterministic metric/changepoint/deploy validators, phase state, error class, repair budget; an execution receipt must list actual source reads, query/locator, digest/version, and output binding; only material ambiguity enters the human wall.
- **HIGH risk — hollow determinism / unproven derivation**: Visual-only `05:30` shows that this Task 29 demo's `solution.py` directly constructs `result_df`, with a Chinese company-name literal translated as `Hengbao Co., Ltd.` and `bonus_share_ratio=6.0` written as literals; the image does not show the code reading source data. The validation at `05:58` mainly confirms execution, header/shape, and publishability, with `Warnings: None`; the semantic review at `06:05` emphasizes “no hardcoded paths” and then accepts. The weak conclusion is limited to this demo: deterministic code + a shape validator + a semantic reviewer can still allow constants that were not derived from the source at execution time; this does not establish that every solve is hard-coded. Paper p2–3 instead claims that generated code and published values must be grounded/derived from current task data, so there is an unexplained tension between the paper claim and the demo visual.
- **Other risks/failures**: Paper p6 reports that 6 task roots reached the solution cycle but still did not publish. The authors observed about 6 minutes for a clean solve and about 11 minutes with one repair (p5); this cannot be extrapolated into a production SLA.
- **Greenfield comparison**: Adopt the control pattern; replace the stages with A's experiment validation/recompute/system mapping or B's signal/changepoint/deployed-change/disconfirmation. If a numerical derivation's execution receipt has zero source reads, fail it immediately; risks/contradictions must propagate to the review and publication gates. Do not copy the KDD answer flow, and do not give generated code general production/SCM access.

### P4 — Human Wall: Humans Make Judgments, but Do Not Serve as Evidence: **Adopt**

- **Problem addressed**: Metric definitions, question interpretation, and risk posture contain genuine ambiguity; the agent should neither guess nor let one human opinion bypass validation.
- **Mechanism**: The wall presents 2–3 bounded choices, a recommended default, evidence references, and a fallback for no response; the human choice is guidance, and the result must still pass evidence, validation, and publication gates. Paper p2 makes the mechanism claim; the video image further shows a typed tool row including `request_type=interpretation`, `review_gate=question_understanding`, `severity=material`, `agent_default`, `fallback`, and `context_refs`.
- **Primary evidence**: Paper p2, p13–14; Video `04:06–04:53` shows the ambiguity wall, and `06:12–06:25` says the agent can ask the user whenever there is a contradiction/ambiguity. Visual-only `04:14` shows “fallback in 5:00 · applies the default, marks the answer provisional,” with `fallback=continue` in the tool row.
- **Applicable to**: A + B.
- **Requires**: the current contract/evidence, request-human tool, durable ruling artifact; use human gates for material ambiguity, A's change review, and B's rollback packet.
- **HIGH risk — fail-open human-gate timer**: The five-minute timeout at `04:14` automatically applies the default and continues, merely marking the answer provisional. This is not human approval. It must not be copied into A/B, especially a SEV: a material ambiguity, attribution, or action gate should fail closed, preserve the best-known state, explicitly notify the owner/on-call, and follow a time-bounded escalation; only a pre-approved low-risk query branch may fall back.
- **Other risks/failures**: Humans can also be wrong, and the wall can block progress; a human response cannot become causal proof.
- **Greenfield comparison**: This aligns with the human-control principle in Gates 0–3, but continuing by default conflicts with a material gate. In B, the wall may only request a human decision; it cannot implicitly authorize a rollback, flag change, or deploy.

> **Current-authority terminology note (2026-08-12; not Team 1286 evidence):** “Gates 0–3” above records the pre-contract research vocabulary. It is superseded for the logical Data Agent contract by the [planning decision packet](planning-decision-packet.md), the closed [canonical domain and policy ticket](wayfinder/freeze-canonical-domain-policy-contracts.md), and the [final architecture specification](final-architecture-spec.md). The canonical gate set is `G0`–`G7`; it separately defines Cause Verdict (`unassessed | suspected | confirmed | ruled_out | inconclusive`) and Recommendation Readiness (`not_applicable | blocked | proposal_ready | action_ready | rejected`). The later shorthand in this report—such as “Gate 0 runs before any query” and `Observed / Heuristic/Inferred`—remains a useful research warning, not a complete canonical schema: `observed` is evidence or an observed-fact claim state, never a Cause Verdict. No gate or state authorizes mutation.

### P5 — Contract-Gated Publication: **Adapt**

- **Problem addressed**: Model output may contain columns, values, or conclusions unsupported by evidence.
- **Mechanism**: The contract fixes row grain, binding, predicate, projection, and per-column status; the publisher emits only `supported` content and abstains if there is no supported output.
- **Primary evidence**: Paper p3, p17, p19. The authors explicitly state that the gate does not prove the answer correct; it only prevents an unsupported column from becoming part of the final answer. Video `05:24–06:12` shows `answer-contract.yaml`, validation, review, and publication artifacts; at `06:12–06:20`, the published answer and contract/validation references are visible. This is a UI affordance/visual evidence, not proof of gate enforcement or derivation correctness.
- **Applicable to**: A + B.
- **Requires**: typed claim/hypothesis/change schemas, validator, publication/review report, source-read execution receipt, open-risk register; final actionability can have a human gate.
- **Risks/failures**: If the evidence/status itself is wrong, the error can still be labeled supported; checking only columns/headers creates a hollow gate; KDD's extra-column penalty is not proof of production safety.
- **Greenfield comparison**: Adapt this into a claim gate: A's change proposal must have both metric and exact code evidence; B's attribution must have deploy proof, timing/scope/mechanism, counterevidence, and a falsifier. Numerical conclusions must have nonzero source reads and a derivation receipt; an unresolved HIGH risk must fail publication. This is not simply "remove columns."

### P6 — Focused Feedback Continuation: **Adapt**

- **Problem addressed**: Restarting the entire run after an existing answer is found to contain an interpretation error loses context; directly editing the final artifact bypasses auditability.
- **Mechanism**: Save the feedback, branch from the existing solve state, rebuild only the affected contract/evidence/plan/code, and pass through the same review/publication gate again.
- **Primary evidence**: Paper p5, p13 describes the continuation mechanism. The video does not fully demonstrate a correction run; however, at `06:12–06:20`, the image clearly shows a `Refine` affordance and “focused repair revision runs on the same workspace.” The entry point is therefore **visual evidence**, while the actual branching, partial rebuild, and republication remain a **paper claim**.
- **Applicable to**: A + B, more commonly A.
- **Requires**: immutable prior run, feedback artifact, dependency/invalidation map, repair diff, human correction gate.
- **Risks/failures**: Stale or incorrect old state can be inherited; the authors' example concerns benchmark semantic correction, not production incident attribution.
- **Greenfield comparison**: Allow local continuation, but if the metric definition/window/deployed SHA changes, freeze and recompute again; do not reuse the old evidence.

### P7 — Scope-Separated Memory, with Memory Not Equal to Evidence: **Adapt**

- **Problem addressed**: Organizational rules, workspace conventions, and resolved ambiguities are repeatedly debated.
- **Mechanism**: Three layers of memory—instance/workspace/question—are injected according to context; only explicit pin/edit actions persist; memory may only guide where to investigate and cannot supply an unsupported value or bypass validation.
- **Primary evidence**: Paper p2–3, p13; Video `03:19–04:00` introduces the three memory scopes, and `04:20–04:53` shows that a wall ruling can enter future memory.
- **Applicable to**: A + B.
- **Requires**: author, scope, approval, source refs, validity window, expiry, version; pin/edit is a human gate.
- **Risks/failures**: Old rules can contaminate a new run, content can leak across scopes, and memory can be treated as a source. The video links memory with “getting better over time” (`03:46–04:00`), but presents no controlled experiment, so it cannot be described as a causal improvement.
- **Greenfield comparison**: This is consistent with separating observed from inferred, but provenance/freshness/auth must be added. During a live SEV, memory is navigation only, not current truth.

### P8 — Reusable Failure-Mode Skills + Profile Routing: **Adapt**

- **Problem addressed**: Rewriting the pipeline for every task; recurring errors in row grain, joins, metrics, normalization, and evidence.
- **Mechanism**: 17 task-agnostic Markdown skills encode procedures/checklists; skills are selected by source profile, phase, and human/repair mode, not by task-ID fastpaths.
- **Primary evidence**: Paper p3–4, p14; Video narration at `06:48–07:14` names discovery orientation, operator escalation, and video context, and says new skills can extend capabilities. The image at `06:50–07:20` separately states “17 open Markdown skill files” and “organized by phase—not compiled pipeline code”; this is a **visual-only claim**, not a spoken statement.
- **Applicable to**: A + B.
- **Requires**: versioned policies, deterministic routing receipt, evaluation regression, human-reviewed promotion.
- **Risks/failures**: Skill prose is not a correctness guarantee; a wrong profile can omit rules; the video's “lift” is an author claim without an independent ablation and cannot be treated as a causal effect.
- **Greenfield comparison**: Adapt this into a small set of A/B diagnosis policies: experiment validity, decomposition, changepoint, deployed-change resolution, disconfirmation, and escalation. The authors' 17 skills are not requirements.

### P9 — Apply Benchmark Gold Learning or Automatic Growth Directly to Live Diagnosis: **Reject**

- **Problem addressed**: The authors want to turn failures into rules usable in the future; in live A/B, however, ex post outcomes are usually not clean gold, and automatic absorption would contaminate the system.
- **Mechanism (authors' system)**: Gold is unlocked only after a no-gold solve/publish; the system generates a reflection and skill proposal according to a failure taxonomy; a human decides whether to promote it. Video `06:48–07:21` shows only the skill library and does not show gold learning; the full mechanism is **paper-only** (Paper p3, p6).
- **Applicable to**: Do not include in live A/B. It may exist only as a separate governance process for offline evaluation / closed incident review.
- **Requires**: frozen run, reliable ground truth, reviewer, versioned diff, regression suite, explicit human approval.
- **Risks/failures**: Benchmark gold ≠ production truth; reviewer bias, narrow task distribution, and ex post overfitting; automatically changing policy during a live SEV can amplify errors.
- **Greenfield comparison**: The current requirements prohibit online writes to production/policy. “Offline, human-gated, no task-specific leakage” may separately be **Adapted** into the evaluation process, but reject it as a live-diagnosis practice.

### P10 — Convert Multimodal Inputs into Inspectable Artifacts First: **Adapt (Conditional)**

- **Problem addressed**: Metric definitions, configuration instructions, or runbooks may be hidden in a PDF/video/image; raw media is difficult to search and audit.
- **Mechanism**: Frame sampling, deduplication, OCR, and timestamped STT produce frame/text/table/transcript artifacts that then enter the same evidence loop. The authors explicitly state that this is not general native video reasoning.
- **Primary evidence**: Paper p3, p5–6, p8–9; Video `06:28–06:40` shows video frames and extracted data but does not discuss extraction failure.
- **Applicable to**: A + B, only when the authoritative input actually includes media.
- **Requires**: ffmpeg/OCR/STT/document parser, timestamps, extraction coverage/status, original-file locator; critical content can require human review.
- **Risks/failures**: OCR/STT/shallow parsing can miss evidence; a cited frame is not formal lineage; the prototype fails open on media-extraction errors (Paper p16).
- **Greenfield comparison**: Media can provide definitions/mapping/context; exact metric/deploy facts must return to an authoritative structured source. Failure on critical media should yield `insufficient_evidence`, not silently continue.

### P11 — Least Privilege, Isolation, and Allowlists: **Adopt**

- **Problem addressed**: Generated code uses the network, shell, installer, or the wrong session/source.
- **Mechanism**: Generated Python is restricted to local deterministic libraries; forbidden access is checked before execution; the preview route uses a folder/filename allowlist and bounded responses; answer roots are isolated.
- **Primary evidence**: Paper p2, p5, p9 claims library restrictions, forbidden-pattern scanning, answer-root isolation, and a preview allowlist. The reviewer prose in Video `06:05` says `solution.py reads from CONTEXT_DIR (no hardcoded paths)` and uses only the permitted `pandas+os`; this is only a textual claim in a review artifact. The image does not show sandbox/IAM, interception tests, or actual enforcement, so it cannot be upgraded into permissions proof.
- **Applicable to**: A + B.
- **Requires**: dedicated read-only adapters, underlying IAM, isolated state, redaction/secret policy; Gate 0 runs before any query.
- **Risks/failures**: Pattern scans can be bypassed; local files may still contain secrets/PII; malicious code may still read credentials from environment variables.
- **Greenfield comparison**: Adopt the least-privilege principle, but do not copy “arbitrary generated `solution.py` + local files.” Use scoped read-only APIs for metrics/SCM/deploy/flags instead, with no general shell/filesystem access.

### P12 — Hard Budgets, Traces, and Failure Disclosure: **Adopt**

- **Problem addressed**: Agent-loop latency/cost is unbounded, and only successful demos are shown.
- **Mechanism**: Phase timeout, repair cap, token/runtime receipt, durable/replayable trace; seeded snapshots are explicitly labeled as not being proof of live execution; the trace bundle preserves failures. The paper does not prove cryptographic immutability; an immutable event log is an additional greenfield requirement.
- **Primary evidence**: Paper p4–6, p10–11, p16, p20–23 provides complete token/runtime/failure accounting: 13 counted logs, 123 phase calls, 7 failed calls, 427 minutes; repair/feedback accounts for 32.5% of reported total tokens. The video does not show complete token or failure accounting, but the UI displays durations such as `8.2m` and `3.9m` beside phase headings at `05:30`, `06:05`, and elsewhere. Per-phase duration is therefore **visual evidence**; the complete cost/failure receipt remains **paper-only**. These are author trace audits, not A/B SLAs.
- **Applicable to**: A + B.
- **Requires**: per-stage budget/timeout, cost/runtime/error receipt, best-known state, redacted replay archive; human review or abstention after the budget is exhausted.
- **Risks/failures**: Of 99.7M total tokens, 94.8% are cache reads; the sample mixes Phase 1/2, seeded/custom; approximately 6/11 minutes is an observation on one machine and cannot support production capacity planning.
- **Greenfield comparison**: This aligns with existing hard-budget/trace requirements; quality, p95, cost, false-cause rate, and abstention must be re-measured on A/B fixtures.

### P13 — Use KDD Coverage / Seeded Demos to Prove Production Reliability: **Reject**

- **Problem addressed**: These materials can show that a UI, modality, and artifact path are demonstrable, but cannot prove A/B diagnostic correctness.
- **Mechanism (authors' evaluation)**: The report claims coverage of 111 KDD-provided input roots and separately provides a representative trace subset, seeded workspaces, and scenario cases; it explicitly makes no leaderboard claim.
- **Primary evidence**: Paper p4–6, p10–12; Video `00:59–07:21` shows product paths for tasks 29, 163, and 11, with no A/B production case.
- **Applicable to**: Not a live A/B practice; only the presentation of offline fixtures may serve as a reference.
- **Requires**: If used for evaluation, replace these with the frozen A/B cases and ground-truth/review receipts in greenfield requirements §9.
- **Risks/failures**: Input coverage does not equal correct outputs; representative traces are not a full validation archive; medical PBL is explicitly not clinical validation.
- **Greenfield comparison**: Reject this as reliability evidence. Testing must cover SRM/definition drift, undeployed commits, flag/config/model/data changes, scope overlap, counterfactuals, and measurement incidents.

### P14 — Typed Narration, Event Taxonomy, and a Current-Risk Register: **Adapt**

- **Problem addressed**: A natural-language timeline mixes observations, heuristics, risks, decisions, and actions; reviewers cannot tell which risks remain unresolved.
- **Mechanism**: Paper p3–4 describes `kdd_discovery_emit` as a typed graph update and lists relationship, group, concern, and synthesis events; the Narration visible in Video `02:05–02:50` explicitly labels items `CONCERN`, `BACKBONE`, `SYNTHESIS`, and `HYPOTHESIS`. These are a paper claim + visual evidence. **This report's inference**: greenfield can borrow the typed-narration form, but should separate facts into `Observed` and `Heuristic/Inferred` and maintain a separate current-risks register; it cannot inherit the demo labels as a production schema.
- **Primary evidence**: Paper p2–4, p17–18; Video `02:05–02:50`. For the typed wall request, also see Visual-only `04:14` and Paper p2.
- **Applicable to**: A + B.
- **Requires**: typed event schema, stable IDs, source refs, event producer, severity/status/owner, created/updated time, falsifier, risk-to-gate linkage; the UI is only a view of event state.
- **Risks/failures**: Labels do not prove their contents correct; `HYPOTHESIS` may still be read as fact; an old concern may remain in the UI without entering the final decision.
- **Greenfield comparison**: Adopt typed state, not the KDD taxonomy. Every claim must be labeled `Observed` or `Heuristic/Inferred`; the current-risks register must record open/mitigated/accepted status, owner, and evidence. Any unresolved material risk must propagate to the human/publication gate.

## 4. Graph-Specific Evidence Packet

This section provides research judgment only. The owner has not confirmed the evidence-graph product contract; the content below does not freeze the final spec.

> **Current-authority note (2026-08-12; not a revision of the source audit):** The preceding sentence is historically accurate for this research phase. The logical Evidence Graph and Trace contract has since been owner-confirmed in the [planning decision packet](planning-decision-packet.md), the closed [canonical domain and policy ticket](wayfinder/freeze-canonical-domain-policy-contracts.md), and the [final architecture specification](final-architecture-spec.md). The video, paper, timestamps, and research inferences below remain evidence about Team 1286 only; they do not prove or approve the new product. Live interaction and visual acceptance are still open in the [Observability-First Review Surface ticket](wayfinder/prototype-observability-first-review-surface.md). Any sensitive production display remains blocked pending the [Production Evidence Authority and Access Boundaries ticket](wayfinder/establish-production-evidence-authority.md), including its production-owner and security/privacy decisions.

### 4.1 UI and Actions Actually Seen in the Video

| Capability | Evidence level | Observation |
| --- | --- | --- |
| workspace graph preview | Video observed | Workspace cards at `01:30–01:40` show small node/edge previews; this proves only that a thumbnail exists, not its semantics or interaction. |
| source nodes | Video observed | Source nodes with different icons for CSV, JSON, document, video, and other types are visible at `02:05–02:50`. |
| edges | Video observed | Solid, dashed, and differently colored lines are visible at `02:05–02:50`. The image contains no edge legend and does not show relation types; line styles cannot be interpreted as causal. |
| source groups | Video observed | Translucent group boxes such as `CSV CORPORATE ACTIONS TABLES` and `DOCUMENT & REFERENCE SOURCES` are visible at `02:05–02:50`. |
| click node → detail | Video observed | Different source nodes are clicked in sequence at `02:22–02:48`; the card on the left shows source kind, grain, rows, key fields, a summary, and `Explore <file>`. |
| click group → detail | Video observed | At about `02:35`, a group is clicked; the card on the left shows cluster members and a group summary. |
| relayout | Video observed | `Re-layout` appears at the top right at `02:20–02:50`. The image does not prove that the layout algorithm or edge semantics change. |
| findings walk | Video observed | At `02:20–02:50`, the top shows “agent flagged 3 findings” and `Walk them in order`; Narration on the right displays entries labeled `CONCERN / BACKBONE / SYNTHESIS / HYPOTHESIS`. |
| answer path graph | Video observed | At `03:07–03:19` and `06:12–06:20`, a solution/answer graph is visible, placing recruited sources into a question-specific path; the final card has “rests on” artifact references. It is a provenance affordance, not derivation proof. |
| phase timeline / trace | Video observed | The Thread at `03:00–03:19` has a phase timeline, tool calls, and artifacts; `05:24–06:12` shows contract/evidence/plan/code/validation/review/publication stages. It is an execution/debug trace, not the same thing as a source-to-claim evidence graph. |
| graph filter | Not observed | The video shows no graph control that filters by source/type/status/time/filter. The paper also does not describe a concrete filtering UI. |
| expand/collapse group | Not observed | Only clicking a group to show a detail card is visible; group expansion/collapse or hidden members are not shown. |
| edge click/detail | Not observed | No edge click, relation receipt, direction, confidence, or source locator is shown. |
| manual add/edit edge | Not observed | No user creating, modifying, confirming, or rejecting an edge is shown. |
| graph timeline replay | Not observed | The Thread has a replay bar, but the graph is not shown replaying over event time, and no historical edge supersession/invalidation is shown. |

### 4.2 How the Graph Is Generated: Keep Evidence Levels Separate

- **Video observed**: `01:40–02:05` shows discovery running while continuously emitting findings/drawing connections; `02:05–02:50` shows the completed nodes, edges, groups, concerns, and narration. The image does not show compiler code or prove the derivation of each edge.
- **Author claim (Paper p2–4, p17–18)**: Source profiling/extraction first produces inventories, schemas, samples, and media text; the agent writes relationships, groups, concerns, and synthesis to `discovery/stream.jsonl` through typed `kdd_discovery_emit`; the compiler replays the event stream and generates `discovery-summary.md`, `discovery/graph.yaml`, `discovery/passages.jsonl`, `discovery/media-tables.jsonl`, and canonical `discovery-map.json`; the answer loop recruits nodes through typed queries. The paper also says stable node IDs connect discovery with the answer overlay.
- **Repo observed**: `not observed`. As of 2026-08-11, no verifiable official public GitHub repo for Team 1286 / PiTrace was found. Public GitHub searches for `PiTrace KDD`, `Team 1286`, `kdd_discovery_emit`, `discovery-map.json`, `graph.yaml`, and related terms returned no attributable project. Therefore, no Team 1286 file/symbol/line, commit SHA, or fixed-SHA permalink can be provided. Paths such as `app/src/server.js` from the paper can only be labeled author claims, not direct source-code implementation.
- **Reviewer inference**: Source extraction → typed discovery events → a compiled source graph has paper-level design evidence, and the UI is superficially consistent with it. But claim/evidence links, execution receipt → claim, edge validation, and invalidation have no source-code or UI proof. They cannot be filled in as implemented capabilities.

### 4.3 What the Graph Actually Helps With

- **Adopt (research judgment)**: Node details and groups can help users answer “what sources exist, what is each source's grain/schema/size, and which sources are grouped together.” There is direct UI evidence at `02:22–02:48`.
- **Adapt (research judgment)**: A question-specific answer path can help answer “which sources/artifacts did the agent recruit for this question?” But query/result, execution-read, and claim-level receipts must be added before it becomes an A/B evidence graph.
- **Adapt (research judgment)**: Typed concern/hypothesis narration can help users identify uncertainty and current risks. But `CONCERN / BACKBONE / SYNTHESIS / HYPOTHESIS` is a narration taxonomy, not a set of evidence levels; production needs explicit `Observed / Derived / Heuristic / Assertion` labels.
- **Reject (research judgment)**: Treating source proximity, group membership, arbitrary connections, or Narration as causal evidence. The current image provides neither edge semantics nor causal validation.
- **Reject (research judgment)**: Treating Thread tool logs, the phase timeline, replay bar, or “rests on” chips directly as an evidence graph. They are, respectively, a debug/execution trace and a provenance affordance; the Task 29 hollow-determinism visual demonstrates that these surfaces can coexist with a derivation gap.

### 4.4 Edge Types Must Not Be Collapsed into “Causal”

The following semantics need to be distinguished in a production graph. They are **reviewer inference / research recommendation**, not implemented Team 1286 capabilities:

| Edge type | Meaning | Minimum evidence |
| --- | --- | --- |
| observed fact | The relationship between the two endpoints is directly provided by an authoritative record | source locator, query/result, version/digest |
| derived fact | The relationship is produced by a join, aggregation, or deterministic transform | input reads, code/query, parameters, output receipt |
| mapping assertion | A human or agent asserts that a metric/surface/symbol corresponds to another entity | author, scope, confidence, supporting refs, review status |
| causal claim | A claim that a change caused a metric effect | mechanism, timing, scope, counterevidence, falsifier; correlation cannot be promoted to causation |
| contradiction | Two pieces of evidence or claims disagree | both refs, conflicting field, resolution status |
| supersedes / invalidation | A new version/window/ruling invalidates an old node/edge | prior ID, new ID, reason, effective time, owner/gate |

Only the visual appearance of connections was observed in the Team 1286 video; the typed edge schema, legend, and receipts above were not observed.

### 4.5 Gaps in a Production A/B Evidence Graph

The target chain is assessed below. `not observed` means there is insufficient evidence across the paper, video, and any verifiable public repo; it is not proof of a negative effect.

| Chain link | Team 1286 evidence | A/B gap |
| --- | --- | --- |
| metric | Not observed | metric definition/version, window, segment, numerator/denominator, SRM/missingness |
| surface/component | Not observed | product surface → service/component/owner mapping |
| query/result | Partial author claim | The paper has a workspace query/evidence map; it lacks production query text, result digest, and warehouse/runtime receipt |
| ACL/corpus | Not observed | principal, authorization decision, row/field policy, corpus snapshot/freshness |
| pipeline/runtime | Not observed | job/service/deploy runtime identity, environment, region/cohort, effective time |
| typed production change | Not observed | code/config/flag/model/data change type, deployed SHA/version, rollout scope, parent/change receipt |
| claim | Partial | The answer contract/status targets output columns; it lacks an A/B hypothesis/attribution schema and uncertainty |
| verification/falsifier | Partial author claim | Validation/review/repair exists; counter-metric, holdout/recompute, disconfirmation, and causal falsifier are missing |
| recommendation | Not observed | action owner, expected effect, risk, approval status |
| not-applied diff | Not observed | proposed code/config/flag/model/data diff, explicitly marked `not applied` |
| rollback-ready packet | Not observed | rollback target, preconditions, blast radius, verification, incident-commander gate |

Net judgment: The Team 1286 graph can serve as a reference for source orientation and a shared review surface. It cannot become a production A/B evidence graph unchanged. Whether to adopt it, and how to define the final product contract, remains an owner decision.

> **Current status (2026-08-12; not a retroactive change to the judgment):** The owner has now selected the logical product contract in the linked current-authority documents above. What remains open is the review-surface interaction and visual acceptance, plus production source/ACL/redaction authority for any sensitive display; neither is settled by this Team 1286 research.

## 5. Paper and Video Alignment

| Practice | Video | Paper | Alignment conclusion |
| --- | --- | --- | --- |
| shared discovery/solution state | `01:30–03:19`, `06:26–06:40` | p1–4, p17–19 | They align; the video is a UI demonstration, while the paper provides artifact/loop details |
| contract/evidence/plan/code/review loop | `05:24–06:12` | p2–4, p19 | The stages and UI artifacts align; the Task 29 image exposes hollow determinism, so pipeline presence cannot be treated as derivation proof |
| human wall | `04:06–04:53`, `06:12–06:25` | p2, p13–14 | Typed requests align; `fallback=continue` at `04:14` is visual-only fail-open behavior |
| three-scope memory | `03:19–04:00`, `04:20–04:53` | p2–3, p13 | The mechanism aligns; the video's performance-improves claim lacks a control and is not accepted as causal |
| reusable skills | Narration `06:48–07:14`; visual-only `06:50–07:20` | p3–4, p14 | The mechanism aligns; “17 open Markdown files” appears only in the image; effectiveness is only an author claim |
| focused post-answer feedback | `06:12–06:20` has a `Refine` entry point, but no complete correction run | p5, p13 | The affordance is visual; the continuation mechanism is a paper claim |
| gold-after-publish learning | Not demonstrated | p3, p6 | Paper-only; do not extrapolate to live production |
| permissions/restrictions | `06:05` reviewer prose | p2, p5, p9 | The video shows only a reviewer claim, not enforcement proof |
| token/runtime/failure accounting | Phase durations are visible; no complete token/failure UI | p5–6, p20–23 | Durations are visual; complete statistics are paper-only; neither is A/B effectiveness evidence |
| typed narration/current risks | `02:05–02:50` has event labels | p2–4, p17–18 | The taxonomy can be adapted; separating Observed/Heuristic and risk propagation is this report's adaptation |

## 6. Conclusions the Materials Do Not Support

- They do not support saying that PiTrace can explain a post-experiment metric miss or locate a SEV root cause; the materials are not connected to production code/change timelines.
- They do not support saying that memory, skills, or the human wall **cause** quality improvement; the video is a demonstration, and the paper contains no rigorous A/B ablation that isolates these components.
- At `00:50–00:59`, the video says human judgment + agent precision produces “trustworthy, grounded answers.” This is a speaker claim / product framing, not proof of production trust.
- “Coverage of 111 KDD input tasks” cannot be written as all 111 tasks being correct. The paper explicitly makes no leaderboard claim, the released traces are only a representative subset, and failures are included.
- The most recent change, graph adjacency, or a human choice cannot be presented as causal. A/B still requires timing, scope, mechanism, counterevidence, and deployed proof.
- Local-file privacy, forbidden-pattern scanning, or a contract-gated CSV cannot be equated directly with production auth, security, or rollback control.
- The appearance of a literal in the Task 29 demo does not support inferring that every `solution.py` is hard-coded; what can be confirmed is only that the image does not prove runtime derivation and that the existing validation/review still accepts it.

## 7. Net Effect on the Current Requirements

The objectives of the two scenarios do not need to change, and no PiTrace-compatible architecture should be added. The design pressures worth preserving are:

1. The evidence graph must become a shared working surface for humans and the agent;
2. The human wall, feedback, and memory must be separated, each with a different safety contract;
3. The output gate must check evidence completeness for each claim, not only formatting;
4. Reusable diagnosis policies may be promoted only through an offline, versioned, human-gated process;
5. The execution receipt must list source reads; a numerical derivation with zero source reads fails immediately; current risks must propagate to the publication gate;
6. A material human wall fails closed by default and has explicit escalation;
7. Typed narration must separate `Observed` from `Heuristic/Inferred`;
8. All KDD-specific artifacts, the 17-skill catalog, generated `solution.py`, `prediction.csv`, and the competition flow remain outside the greenfield compatibility contract.

### Production Evidence Plane That A/B Must Build Separately

| Gap | A — Post-experiment | B — SEV | Minimum requirement |
| --- | --- | --- | --- |
| production telemetry | experiment exposure, metric rows, component/segment, trace | alert, changepoint, affected scope, logging freshness | frozen query/window, metric-definition version, source receipt |
| runtime identity | actual treatment/control service versions, config, flag, model, data dependency | service/config/flag/model/data versions actually in effect during the incident window | environment, region/cohort, effective time, owner |
| code identity | exact `owner/repo`, deployed SHA, file/symbol, serving path | deployed SHA/parent, PR/commit, rollout scope, diff | deploy proof; an undeployed commit must not be listed as a production candidate |
| typed change attribution | candidate mechanism, expected effect, counter-metric, test, rollback | timing, scope, mechanism, supporting/contradicting/missing evidence, falsifier | separate `observed` from `inferred`; correlation must not be promoted to causation |
| execution derivation | metric query/source reads, code path, input/output digest | telemetry/change queries, source reads, candidate derivation | numerical derivation with zero source reads fails; receipt binds source, query, version, and result |
| current risks | SRM, definition drift, missingness, counterevidence | telemetry staleness, scope mismatch, undeployed change, counterevidence | typed risk register; a material open risk blocks publication |
| decision gate | recommend a change only after experiment validity, SRM, missingness, and guardrails pass | one of rollback/holdout/independent validation, plus incident-commander approval | read-only by default; the agent does not execute production actions |

PiTrace's graph, wall, contract, and trace provide only a control shell for these capabilities. Neither the paper nor the video shows the production inputs or adapters above. These gaps are therefore **unknown / not evaluated**, not negative evidence that Team 1286 has failed and not something a UI demo can fill.

Overall judgment: PiTrace directly informs “how to make an investigation reviewable, correctable, and able to abstain”; for “how to connect a metric to a production change and validate the cause,” it provides only the shell, not the required evidence plane.
