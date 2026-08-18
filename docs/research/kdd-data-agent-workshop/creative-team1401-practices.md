# Creative Team 1401: Review of Video Practices and Screenshot-Based Identity

Date: 2026-08-11

Status: research-only; the primary-source video has been reviewed in full, and workshop screenshots were used to verify identity and the interaction contract

Objective: determine only whether the practices demonstrated by Team 1401 should be considered for two greenfield scenarios. This is neither an attempt to reproduce KDD nor an effort to patch the legacy SMA.

## 1. Executive conclusion

Team 1401 presented **Data Agent Studio — A Transparent and Controllable Chatbot for Data Analysis Agents**. The team is `UITNLP` from the `University of Information Technology, VNU-HCM`. Its Team ID is `1401`, and the presenter is `Ha Huu Phat`. The cover identifies the entry as `Creative Track, Top 3`. [workshop Screenshot 64; `screenshot-index.md:654-665`]

Its most valuable contribution is not a particular competition agent. It is an interface that lets users see, constrain, inspect, and approve the agent's work.

Recommendations:

| Candidate practice | A | B | Decision |
| --- | --- | --- | --- |
| Visible plan, tool calls, raw input, results, and evidence | Applicable | Applicable | **Adopt the principle** |
| Preserve exact SQL for numeric answers and verify it with an independent direct SQL check | Applicable | Applicable | **Adapt** |
| Enable or disable tools individually; mark sensitive tools as requiring approval | Applicable | Applicable | **Adapt** |
| Enable arbitrary Python in the task context directory by default | High risk | High risk | **Reject default enablement** |
| Pause for approval before every Co-pilot tool call | Optional | Unsuitable as the default during an emergency | **Adapt** |
| Show code and a before/after diff before a write, then require human approval | Conditionally applicable | Conditionally applicable | **Adapt** |
| Deterministic column profiles, correlations, and missingness analysis | Applicable | Applicable | **Adapt** |
| Isolate files, conversations, and settings by session | Applicable | Applicable | **Adopt the principle** |
| Uploaded-files-only sandbox | Too narrow | Too narrow | **Reject as-is** |
| Infer cross-database links from column names | High risk | High risk | **Reject as evidence** |
| Attach a source-text quotation to every relationship in a PDF knowledge graph | Conditionally applicable | Conditionally applicable | **Adapt** |
| Choose among ReAct / DRAGIN / Multi-agent / Hybrid-B | No A/B evidence | No A/B evidence | **Reject as a design conclusion** |
| Product features such as demo/live switching, accounts, themes, and layout controls | Not core | Not core | **Reject from the diagnostic core** |

The most important evidence gap is that the video demonstrates only two small data-analysis tasks with known answers. The first prompt already specifies the database, join, formula, output columns, and sort order; the sample fixture was also designed for the relationship-graph demonstration. The video provides no production repository, deployed SHA, deploy/config/flag/model/data timeline, experiment-validity check, SEV changepoint, counterfactual check, or incident replay. It therefore cannot establish autonomous task decomposition, general join discovery, a code-backed why/change proposal for A, or production change attribution for B.

## 2. Sources and coverage

### 2.1 Primary sources

- Google Drive: `https://drive.google.com/file/d/1ev10EJT5_yAVItYGCl1wdPRex798Mzng/edit`
- Drive metadata/title: `creative_team1401_video.mp4`
- File ID: `1ev10EJT5_yAVItYGCl1wdPRex798Mzng`
- Downloaded-file SHA-256: `b50c79b6be38c8344e890eefac7f7c15d2bb946dbc471c4f38ed082bd07fbf34`
- Container-reported duration: `08:32.48`
- Video: H.264, `1920x1200`, 25 fps
- Audio: AAC, 24 kHz, mono
- Subtitle tracks: `0`. The video contains no embedded subtitles. The SRT/VTT used below was generated from the complete audio track during this research; it was not supplied by the authors.

Workshop screenshots were also used to verify identity and the interaction contract:

- Screenshot 64, `Screenshot 2026-08-11 at 7.57.40 PM.png`: official title, `UITNLP`, `University of Information Technology, VNU-HCM`, `Team ID 1401`, Presenter `Ha Huu Phat`, and `Creative Track, Top 3`. [`screenshot-index.md:654-665`]
- Screenshot 70, `Screenshot 2026-08-11 at 8.05.31 PM.png`: `Autopilot`, `Co-pilot`, their shared controller, and `Co-pilot — AWAITING_USER before tool execution`. [`screenshot-index.md:716-724`]

**There is no Team 1401 paper.** Operational verification of the practices therefore relies primarily on the full video. The screenshots correct only the identity, terminology, and interaction states that they clearly show. The absence of a paper is not counter-evidence, and it does not permit design details to be filled in from the Team 1286 PDF or materials from any other team. This report did not use the Team 1286 PDF.

### 2.2 Full-coverage method

- `audio_coverage`: segment-by-segment transcription covers `08:32.14 / 08:32.48`. The final approximately `0.34s` is an end frame or container margin with no intelligible speech. No segment was skipped, and the audio review was not sampled.
- `subtitle_coverage`: `ffprobe` detected `0` subtitle streams, so no author-provided subtitles were available for verification. The research-generated SRT/VTT covers all intelligible speech but was used only to check the ASR.
- Transcription: the complete audio track was converted to 16 kHz mono WAV and processed in full with `whisper.cpp small.en`; proper nouns and key claims were then checked against the video frames.
- ASR statistics: 1,466 ordinary tokens; mean token probability approximately `0.941`; 149 below `0.8`, and 36 below `0.5`. ASR probability is therefore not treated below as confidence in a fact; key terms were corrected from the visuals.
- `visual_coverage`: 102 frames sampled across the entire video at five-second intervals, plus original-resolution frames at 47 claim or transition points. The review covered the title slide, the complete operational demonstration, and the final limitations slide.
- `cross_aligned_coverage`: every candidate practice below includes both the speaker timestamp and corresponding visual. None is inferred only from the opening or from sampled excerpts.
- Narrator: the entire video has one English narrator. The video neither shows nor states the narrator's name, so voice identity is `unknown`. The workshop cover confirms that the presenter is `Ha Huu Phat`, but no voice match was performed; the presenter therefore cannot be identified directly as the narrator.

### 2.3 Fresh source audit receipt

- Review date: `2026-08-11`.
- Drive file ID: `1ev10EJT5_yAVItYGCl1wdPRex798Mzng`. Live metadata again returned `creative_team1401_video.mp4` and `video/mp4`.
- Fresh download: `41,147,647 bytes`; SHA-256 remained `b50c79b6be38c8344e890eefac7f7c15d2bb946dbc471c4f38ed082bd07fbf34`, byte-for-byte identical to the first download.
- `ffprobe`: video `512.480s`; audio `512.476s`; subtitle streams `0`.
- The fresh audit again covered the complete ASR from `00:00.00–08:32.14`, all `102/102` five-second frames, and 47 original-resolution close-review frames.
- The re-review used only the Team 1401 video. No Team 1286 PDF, video, or other team material was used to supply details.
- Result: the core A/B judgments did not change. The chronology of the tool count was corrected, the unsupported phrase “auto difficulty routing” was withdrawn, and P12's input, state, and human gate were completed.
- Independent-review correction receipt: `218.jpg`, `375.jpg`, the original KG/cross-DB frames, and their corresponding transcript were rechecked. The review confirmed that the first prompt supplied the join/formula/output, that only one `execute_context_sql` call is visible for the specific run, that `execute_python` is enabled by default, that only the page pointer in the KG is independently confirmed, and that the cross-DB fixture was constructed for the ER demonstration. The claims about autonomy, a four-table path, quotations, join generalization, and tool blast radius were tightened accordingly.
- Name-verification receipt: possible Mac/meeting ASR renderings of `Pat`, `UIDNLB`, and `My 401` are not used as identity evidence. The clear text in Screenshot 64 is the authoritative anchor: Presenter `Ha Huu Phat`, `UITNLP`, `Team ID 1401`. The meeting ASR has no timestamps; numbers such as costs mentioned there remain unverified and are not presented as confirmed facts.

Evidence-state definitions:

- `observed`: directly shown by the narration and visuals.
- `speaker claim`: stated by the narrator but not independently supported by enough material in the video.
- `reviewer inference`: this report's A/B adaptation judgment, not the authors' wording.
- `unknown`: not provided by the video.

## 3. Full timeline transcript summary and visual alignment

The table below is a faithful English rendering of the complete audio transcript summary. Proper nouns, numbers, and tool names are preserved. Each segment includes a visual check so that a speaker claim is not mistaken for a verified mechanism.

| Time | Narration transcript summary | Concurrent visual and evidence status |
| --- | --- | --- |
| 00:00.00–00:14.02 | Analytical questions often come from people who cannot code; LLM data agents that could help them are usually opaque, making intermediate steps difficult to inspect, verify, or correct. | The title slide states the same problem. This is an `observed` product position, not evidence of effectiveness. |
| 00:14.02–00:33.44 | The narrator introduces Data Agent Studio, which wraps a benchmark-evaluated data agent in a transparent, controllable interface; the video will demonstrate it end to end with a live model. | The video title slide says `Transparent, controllable conversational data analysis`. The formal entry title and team identity are corrected from workshop Screenshot 64. “Benchmark-evaluated” and “live” remain `speaker claim`; there is no benchmark receipt or network trace. |
| 00:33.44–00:48.16 | An account is created; this is not a mock login but a real account system with salted password hashing; login succeeds. | The visuals show account creation and login. The hashing implementation is not visible and remains a `speaker claim`. |
| 00:48.16–01:07.54 | First entry triggers a guided tour. A session is an isolated workspace with its own files, conversation, and settings; after creating the workspace, the tour introduces each panel. | The visuals progressively highlight the session/workspace UI. Isolation strength and cross-tenant boundaries are not shown. |
| 01:07.54–01:23.54 | The panels include files, settings/tools chips, Autopilot/Co-pilot, a question box, live activity, a plan that displays agent thinking, results, and Data Doctor. | These regions are visible in the UI. Calling the plan “thinking” does not establish that it is complete or faithful reasoning; it establishes at most that a structured plan/status is displayed. |
| 01:23.54–01:38.66 | This is the product map; data will now be loaded. | The guided tour ends and the upload begins. |
| 01:38.66–01:47.18 | Two files are uploaded: a clean sales CSV and an intentionally messy HR file. | The upload dialog shows two CSV files. |
| 01:47.18–02:07.94 | The agent reasons only over content in the files panel. Files can be previewed, sorted, and filtered in the browser without downloading them or using a spreadsheet. | The visuals demonstrate preview, sort, and filter. The “nothing more” boundary was not subjected to a permission attack test and is a `speaker claim`. |
| 02:07.94–02:26.34 | Explore provides a data scientist's first look at a file: the distribution of each column, a correlation heatmap for numeric columns, and the strongest relationships. | The visuals show Columns and Correlations. Correlation is association only and cannot be reported as cause. |
| 02:26.34–02:36.10 | Missingness shows where values are absent; all of these calculations are deterministic and use no LLM. | The visuals show Missingness. Whether the entire implementation avoids an LLM is only a `speaker claim`; no source code is available. |
| 02:36.10–02:43.98 | Cross-file search accepts one value and searches for it across all uploaded files. | The visual demonstrates a search. It establishes behavior only for the small uploaded files. |
| 02:43.98–02:59.50 | A real model is connected by selecting the Azure OpenAI preset and entering the deployment, endpoint, key, and API version; temperature and the agent step budget are adjustable. | The Settings screen explicitly warns that credentials are stored in browser `localStorage`, persist across sessions, are plaintext, and are “only sent to the local backend.” This is a UI statement, not verification of implementation or transport. Budget enforcement is also not shown. |
| 02:59.50–03:15.22 | Four approaches based on KDD Cup baseline code are available: ReAct, DRAGIN, Multi-agent, and Hybrid-B, each intended for different questions; the demonstration selects ReAct. | The visual shows four choices and short descriptions. It provides no routing evaluation, comparative results, or selection basis. |
| 03:15.22–03:33.54 | The Tools panel exposes the full toolbox. Examples can be viewed by expanding entries. Each tool has a switch; when switched off, the agent cannot call it, and when switched back on, access is restored. | Before custom-tool registration, the visual shows 23 tools, descriptions, and toggles. `218.jpg` also shows that `execute_python` is enabled by default and describes it as `Execute arbitrary Python code with the task context directory as the working directory`. No server-side denial receipt is shown, so “cannot call it when disabled” remains a `speaker claim`. |
| 03:33.54–03:55.60 | Tools are not hard-coded. Fetch Weather is registered live, its use is described, and it is marked as requiring approval before execution; it appears in the toolbox without an engine-code change. | The visual shows the custom-tool form and `Requires approval`. The description is `Current weather for a city`, but the input schema remains the default `{"path":"relative/file.csv"}`; the UI does not prevent this semantic mismatch. Endpoint, authentication, and server-side validation are not visible. |
| 03:55.60–04:05.50 | Users can switch between demo mode, a fully offline scripted replay, and live mode, which uses the real engine; this demonstration remains live. | The UI shows a Live chip. There is no external execution receipt, so this remains a `speaker claim`. |
| 04:05.50–04:16.76 | Data Doctor is a self-contained quality assistant; Analyze is run on the messy HR file. | The visual moves to Data Doctor. |
| 04:16.76–04:32.30 | It profiles every column and proposes a specific fix, each shown as a readable pandas snippet. The user opens the code, previews the exact before/after diff, and approves it. The narrator says approval writes a clean copy. | The visuals directly establish proposal cards, pandas code, a before/after preview, and an `APPROVE` click at approximately `04:29–04:32`. The UI says `pandas · sandboxed (no imports, no I/O)`, but no enforcement or escape test is shown. Before the next section, no clean copy is clearly shown as created or opened, so writing the clean copy remains a `speaker claim`. |
| 04:32.30–04:43.50 | Three connected SQLite databases—shop, CRM, and billing—are added, along with a PDF project brief. | The Files panel shows three databases and one PDF. |
| 04:43.50–05:10.34 | Relationship view inspects schemas and draws a live graph. Within-database foreign keys are solid lines; it also detects a cross-database join between shop and CRM through customer ID and draws it as a dashed line. Users can search, zoom, and inspect columns and keys. | The visual shows 3 databases, 8 tables, 7 links, and solid/dashed lines. The sample fixture was designed for the ER demonstration and deliberately shares `customer_id`; the video later states that cross-database links depend on naming heuristics. This cannot establish general automatic join discovery. |
| 05:10.34–05:27.58 | For the PDF, the model extracts a knowledge graph of people, organizations, places, and dates. The narrator says every relationship has a verbatim quotation from the source page and that users can click an entity to inspect evidence. | The visual shows a PDF graph, page markers, and an entity evidence panel. The close-review frames do not clearly display the complete quotation text, so “every relationship has a verbatim quote” remains a `speaker claim`. Extraction accuracy is `unknown`. |
| 05:27.58–05:43.28 | Graph clusters can be collapsed and expanded; the graph can be filtered by type, zoomed, and fitted to the screen. | The visual demonstrates the UI operations. They primarily establish usability, not diagnostic quality. |
| 05:43.28–06:00.78 | The data is now cleaned and mapped. A nontrivial question is asked: which product category has the highest revenue? The answer requires joining order_items and products in the shop database. | `375.jpg` shows that the user prompt already specifies `shop.db`, `order_items JOIN products`, `qty * price`, the output `category,total_revenue`, and descending order. Task decomposition and the formula come from the prompt, not autonomous agent discovery. This is a small SQLite analysis task, not A or B. |
| 06:00.78–06:21.18 | The narrator says Autopilot decomposes the question, then writes and runs the join itself. The answer is sorted by revenue, and the evidence trail shows the exact SQL. | The visual shows the plan, result, and SQL receipt, but the Event Log shows only one `execute_context_sql` call for this run, followed by `answer`. One inspectable SQL query is therefore confirmed; autonomous decomposition, join discovery, and a multi-step or four-table execution path are not. |
| 06:21.18–06:35.58 | The second question switches to Co-pilot: using only the sales CSV, which region has the highest average order value? In this mode, the system pauses and requests permission before every tool call. | The video UI switches to `Co-pilot` and shows an approval dialog. Workshop Screenshot 70 further establishes the state as `AWAITING_USER before tool execution`. |
| 06:35.58–06:44.22 | The first step is approved. For the next step, the editor is opened so that the proposed action's raw input can be inspected before execution is allowed. | The visual shows approve/edit/cancel controls and raw action input. The approval contract does not show identity, timeout, or replay prevention. |
| 06:44.22–06:54.98 | The user also enters a hint to guide the next step, and the result remains correct. The narrator says this proves that human involvement does not obstruct the result. | The visual shows the hint and answer. The answer explains East's high AOV as “higher spending per order,” which only restates AOV and is not a cause. One successful example also cannot establish that the human layer generally “does not obstruct” results; both are over-strong claims. |
| 06:54.98–07:22.22 | The layout is adjustable and can be reset by double-clicking; dark/light themes and a keyboard-shortcut reference are supported. | The visual demonstrates the UI. It has no direct bearing on the core A/B evidence problem. |
| 07:22.22–07:33.10 | Clearing the conversation and resetting the workspace both require confirmation to prevent accidental data loss. | The visual shows confirmation dialogs. This establishes only the existence of UI confirmation, not complete data recovery. |
| 07:33.10–07:41.94 | The narrator summarizes the product as a complete loop from raw files to verified, evidence-backed answers, then logs out. | “Verified” is supported only for one answer by the later direct-SQL-check claim; it cannot be generalized to all outputs. |
| 07:41.94–07:54.14 | The narrator summarizes the first task as joining `order_items` and `products` and says the result matches a direct SQL check. | The summary slide separately states `593 rows · 4 tables across shop.db`. The Event Log for the specific run shows only one `execute_context_sql` call, and the prompt requires only a two-table join; “4 tables” is therefore a summary claim, not a proven execution path for that run. The direct check also has no query or receipt. |
| 07:54.14–08:03.06 | The second task runs under step-by-step approval; one action is inspected, another is guided with a hint, and the result is also correct. | The summary slide aligns with the narration; this is only one task. |
| 08:03.06–08:08.94 | The Studio and the DataAgent-Bench submission use the same engine. | The summary slide aligns with the narration; no source code, commit, or build identity is provided. |
| 08:08.94–08:28.32 | Known limitations: answer quality depends on the connected LLM; knowledge graphs become slow for large documents; cross-database links rely on naming heuristics and may miss unusual schemas; the sandbox can access only uploaded files. | The summary slide displays the same limitations item by item. These are explicit author disclosures and carry more weight than reviewer speculation, but they remain unquantified. |
| 08:28.32–08:32.14 | Data Agent Studio; thank you for watching. | Closing title. The formal team name is anchored to `UITNLP` in workshop Screenshot 64. |

## 4. Practices: Adopt / Adapt / Reject

### P1. Make the plan, action, input, result, and evidence visible

- **Decision**: **Adopt the principle**; applicable to both A and B.
- **Problem addressed**: analysts and incident commanders cannot work from a conclusion alone. They need to know which inputs the agent used, what it executed, where the numbers came from, and which step failed.
- **Mechanism**: the plan on the left shows task decomposition and progress; Activity/Event Log shows tools; Answer retains the result; the evidence area shows SQL/raw output. [video `01:07.54–01:23.54`, `06:00.78–06:21.18`, `06:37.46–06:44.22`]
- **Visual alignment**: the visuals directly show the Plan stages `Understand question / Explore context / Compute / Validate & answer`, tool actions, code, observations, and exact SQL.
- **A/B adaptation**: A should show experiment validation, metric recomputation, segment loss, production path, and deployed diff. B should show signal checks, changepoints, the change timeline, deploy proof, and supporting/contradicting evidence. Do not display or claim to expose a “complete chain-of-thought.”
- **Input / tool / state**: frozen experiment/incident identity; structured stage state; read-only metric/runtime/SCM/deploy tools; source receipt, freshness, time range, and authorization for every artifact.
- **Human gate**: inspect critical sources and gaps before publishing `actionable/likely/confirmed`; production actions require a separate gate.
- **Risks / failures**: a polished plan may be a retrospective narrative; the event log may omit hidden calls; raw evidence may contain secrets or PII; excessive UI may slow SEV response.
- **Do not copy directly**: the video's four-step plan is a generic analysis UI, not an A/B workflow. Do not use “reveal thinking” as an acceptance criterion. The first prompt already leaks the task decomposition, join, formula, and output shape, so the plan UI cannot establish autonomous planning.
- **Alignment with greenfield requirements**: no conflict; it directly supports the evidence graph, review packet, and replay, but must add fields missing from the video, including exact repository and deployed SHA.
- **Evidence strength**: video-only; medium evidence for the displayed mechanism; effect on A/B is `unknown`.

> **Current-authority terminology note (2026-08-12; not Team 1401 evidence):** `actionable/likely/confirmed` above is pre-contract descriptive wording, not the final product state model. The [planning decision packet](planning-decision-packet.md), closed [canonical domain and policy ticket](wayfinder/freeze-canonical-domain-policy-contracts.md), and [final architecture specification](final-architecture-spec.md) now require independent Cause Verdict (`unassessed | suspected | confirmed | ruled_out | inconclusive`) and Recommendation Readiness (`not_applicable | blocked | proposal_ready | action_ready | rejected`). `observed` remains an evidence or observed-fact claim state, never a Cause Verdict; `G0`–`G7` are the canonical fail-closed gates. No state or gate authorizes a production action.

### P2. Bind numeric answers to the exact query and perform independent mechanical verification

- **Decision**: **Adapt**; applicable to both A and B.
- **Problem addressed**: prevents an LLM from rewriting numbers or presenting an incorrect join or filter as a credible explanation.
- **Mechanism**: the exact SQL that produced the numbers is shown beside the answer. The narrator also says that the first result matches a direct SQL check. [video `06:12.02–06:21.18`, `07:41.94–07:54.14`]
- **Visual alignment**: the result table and `How this answer was computed` SQL are visible; the Event Log shows one `execute_context_sql` call. Neither the final slide's direct-check claim nor its “4 tables” claim has an independent query or receipt, so they cannot be combined with the specific run to create stronger evidence.
- **A/B adaptation**: code should record the query, parameters, result digest, row count, truncation state, and metric-definition version; an independent validator should recompute the result. A must also check SRM/ramp/window; B must also check freshness/changepoint.
- **Input / tool / state**: canonical metric rows, metric definition, parameterized read-only query, validation receipt, and frozen time range.
- **Human gate**: when the validator fails, output is truncated, or the definition has drifted, the result must be `insufficient_evidence`; no ship/revert recommendation is allowed.
- **Risks / failures**: displaying SQL does not prove that the displayed SQL was executed; a direct check may reuse the same faulty logic; the prompt supplied the join/formula and hides decomposition difficulty; the summary may enlarge the path taken by the specific run; correct SQL does not establish causality; production data may be affected by permissions and delay.
- **Do not copy directly**: one correct small SQLite join is not production metric diagnosis. “Matching direct SQL” cannot be presented as root-cause proof.
- **Alignment with greenfield requirements**: aligned, but the requirements are stricter: they require a query receipt, source provenance, deployed-code evidence, and supporting/contradicting evidence.
- **Evidence strength**: medium for the visible UI; weak for the independent check because it is only a `speaker claim`; A/B lift is `unknown`.

### P3. Authorize each tool capability explicitly

- **Decision**: explicit tool controls are **Adapt**; enabling `execute_python` by default is **Reject**. Applicable to both A and B.
- **Problem addressed**: prevents the agent from receiving broad shell access, arbitrary write access, or production permissions unrelated to the task.
- **Mechanism**: the Tools panel lists tools; each can be switched on or off; a custom tool can be marked `Requires approval`. [video `03:15.22–03:53.22`]
- **Visual alignment**: the visual first shows 23 tools, toggles, and the custom-tool registration form; after `Fetch Weather` is registered, the total is 24.
- **A/B adaptation**: tool registration must bind a server-side capability, read/write class, source allowlist, exact target, schema, timeout, budget, and authentication identity. The UI toggle is only a control plane; the tool server must enforce denial and return a receipt.
- **Input / tool / state**: task scope, user identity, source permission, tool manifest, per-call authorization, and audit log.
- **Human gate**: access to a source outside the authorized scope is blocked immediately; write tools do not exist by default. Any future production action requires separate authorization, an exact target, and one-time confirmation.
- **Risks / failures**: **HIGH**: `execute_python` is enabled by default and can run arbitrary Python in the task context directory. If the same session holds production credentials, downloaded evidence, or network access, the blast radius includes credential exfiltration, file access or modification, and arbitrary outbound actions. Front-end toggles may be inconsistent with back-end permissions; a token/session may remain usable after a tool is disabled. In the demonstration, a weather description is clearly inconsistent with the default file-path schema, yet registration still succeeds.
- **Do not copy directly**: **Reject arbitrary Python enabled by default**. A/B should use narrow, read-only, typed tools. If an isolated analysis genuinely needs Python, it must have no production credentials, no network, a read-only mount, resource limits, a short lifetime, and a complete receipt. A user also must not gain an arbitrary live integration by entering only a name and description.
- **Alignment with greenfield requirements**: directionally aligned. Greenfield explicitly forbids a general shell or arbitrary filesystem and requires inheritance of source-system permissions, making it stricter than the video.
- **Evidence strength**: medium for the UI mechanism; server-side enforcement is `unknown`.

### P4. Step-by-step Co-pilot approval and human hints

- **Decision**: **Adapt**; applicable to A. For B, use only for high-risk or low-confidence steps, not as the default for every step.
- **Problem addressed**: before a tool call, the user can inspect raw input, cancel, or redirect the agent, preventing a bad query or incorrect scope from proceeding unchecked.
- **Mechanism**: `Autopilot` continues running and pauses only for calls marked approval-required. `Co-pilot` pauses before each proposed tool call and enters `AWAITING_USER before tool execution`; users can approve/edit/reject/guide. [video `06:21.18–06:54.98`; workshop Screenshot 70; `screenshot-index.md:716-724`]
- **Visual alignment**: the approval dialog, editor, hint, and final answer are all visible.
- **A/B adaptation**: classify by risk. Ordinary read-only queries run automatically; pause for access across sensitive sources, large scans, possible PII exposure, or generation of change/rollback packets. B must prioritize time-to-first-safe-action and cannot wait for a human before every safe read.
- **Input / tool / state**: risk class, expected scope/cost, query preview, diff preview, cancel state, approval identity, and expiry.
- **Human gate**: approval must bind to an immutable action digest; parameter changes require reapproval; approval expires on timeout and cannot be reused by a later call.
- **Risks / failures**: approval fatigue; users may not understand raw input; SEV delays; hints may introduce confirmation bias; one successful demonstration cannot establish that the human layer does not affect results. The demonstration's “higher spending per order” only restates high AOV and is not a causal explanation, showing that successful approval still does not establish explanation quality.
- **Do not copy directly**: reject “pause before every tool call” as a universal policy, and reject the author's general conclusion that human involvement “does not obstruct” results based on one example.
- **Alignment with greenfield requirements**: aligned with the action gate, but the requirements make the MVP read-only by default, so many reads do not require step-by-step approval.
- **Evidence strength**: the video directly demonstrates Co-pilot approval; Screenshot 70 clearly shows both modes and `AWAITING_USER`, providing strong terminology evidence. Quality, latency, and server-side enforcement remain `unknown`.

### P5. Show code and a before/after diff before modifying data, then approve a clean-copy write

- **Decision**: **Adapt**; the investigative phase of A/B does not write to production, but this may be useful for offline repair proposals and a future separate action lane.
- **Problem addressed**: automatic data cleaning may alter the sample, hide an incident, or create a new metric. Users should see the exact transformation and its impact first.
- **Mechanism**: Data Doctor profiles columns and proposes pandas fixes; the user inspects the code and exact before/after diff before approval. The narrator says approval writes a new copy. [video `04:05.50–04:32.30`]
- **Visual alignment**: the visual shows proposals such as imputation and winsorization, pandas code, a before/after preview, and an `APPROVE` click. It also displays `sandboxed (no imports, no I/O)`, which is only a UI/product claim; no server-side enforcement or escape test is shown. No new copy is clearly shown as created or opened, so creation of a clean copy is not an observed result.
- **A/B adaptation**: the diagnostic core generates only an immutable proposal and does not modify the source. The proposal must state affected rows, metric impact, counter-metric, test, owner, and rollback. Entry into an action lane requires an exact target, reviewed diff, fresh precondition, and human approval.
- **Input / tool / state**: source snapshot/digest, quality rule, proposal code, sample/full diff, row counts, validation dataset, and write destination.
- **Human gate**: a data-quality suggestion must never execute automatically; the current agent never cleans a production source directly.
- **Risks / failures**: median imputation or winsorization may change business meaning; a preview sample may not represent the full dataset; downstream users may mistake a clean copy for canonical data; generated code may exceed its boundary.
- **Do not copy directly**: the video presents generic imputation/outlier fixes as too easy. In A/B, anomalies may be the evidence that must be preserved and cannot be removed merely to make data “clean.”
- **Alignment with greenfield requirements**: compatible with a read-only investigative boundary. Adding `FIX` to the MVP would conflict and must remain in a separate, unauthorized production-action lane.
- **Evidence strength**: medium for the UI workflow; correctness and reversibility of the repair are `unknown`.

### P6. Run deterministic data profiles before LLM interpretation

- **Decision**: **Adapt**; applicable to both A and B.
- **Problem addressed**: identify missingness, distribution, correlation, and schema problems before the agent invents explanations for bad data.
- **Mechanism**: the narrator says Columns, Correlations, and Missingness are deterministic and use no LLM; Data Doctor then proposes fixes. [video `02:07.94–02:36.10`, `04:09.14–04:24.26`]
- **Visual alignment**: the visuals show distributions for each column, a heatmap, missingness, and quality cards.
- **A/B adaptation**: A adds exposure/SRM/sample/window/metric-version checks; B adds freshness/logging/schema-drift/changepoint checks. Correlation may generate a candidate but is not a cause.
- **Input / tool / state**: typed rows, schema, time zone, null semantics, baseline, expected range, and deterministic code/version.
- **Human gate**: a missing quality field is `unknown`, not a default pass; definition drift or a stale source blocks a causal recommendation.
- **Risks / failures**: automatic type inference may be wrong; missingness may have legitimate semantics; correlation may encourage false causal claims; sampling large datasets may hide a rare segment.
- **Do not copy directly**: generic EDA tabs are not a diagnostic completion criterion. Scenario-specific validators and source receipts are required.
- **Alignment with greenfield requirements**: aligned; directly supports A's `Validate experiment/Recompute metric` and B's `Verify signal`.
- **Evidence strength**: medium for the displayed feature; weak-to-medium for deterministic implementation because there is no source code; A/B effectiveness is `unknown`.

### P7. Isolate files, conversations, and settings by session

- **Decision**: **Adopt the principle**; applicable to both A and B.
- **Problem addressed**: prevents files, conclusions, permissions, and model settings from different experiments/incidents from crossing cases.
- **Mechanism**: the narrator defines a session as an isolated workspace with its own files, conversation, and settings. [video `00:54.14–01:07.54`]
- **A/B adaptation**: each case freezes identity, source manifest, authorization, time range, model/tool versions, and evidence digest; cross-case memory requires human promotion.
- **Input / tool / state**: case ID, owner, retention, access policy, immutable receipts, and session lifecycle.
- **Human gate**: check permissions and freshness when citing across cases or promoting a learning.
- **Risks / failures**: UI isolation does not establish storage/tenant isolation; caches, vector stores, logs, or the model provider may leak data; reset may not delete backend copies. Settings also warns that credentials are stored as plaintext in browser `localStorage` and persist across sessions, creating exposure through shared machines, XSS, and browser profiles.
- **Do not copy directly**: separate-looking workspaces do not establish security isolation. The narrator says a session has its own settings, while credentials persist across sessions; the scope is ambiguous and must not be guessed.
- **Alignment with greenfield requirements**: aligned and strengthens Freeze input and replay; a formal authorization/redaction/retention contract is still required.
- **Evidence strength**: medium for the UI and `speaker claim`; security isolation is `unknown`.

### P8. Source-cited document knowledge graph

- **Decision**: **Adapt**; use only when A/B genuinely takes a metric definition, runbook, PR, or incident document as input.
- **Problem addressed**: after extracting entities and relations from a document, users can return to a source quotation, reducing unsupported relationships.
- **Mechanism**: a PDF is converted to an entity/relation graph; the narrator says each relation carries a verbatim quotation from its source page. [video `05:10.34–05:27.58`]
- **Visual alignment**: the graph, entity types, page pointer, and evidence panel are visible. A page pointer establishes only that the UI points to a page; it does not establish that the full text on that page supports the relation. The complete verbatim quotation was not independently verified visually.
- **A/B adaptation**: each graph node must include a stable source ID, page/section, digest, observed/retrieved time, and extraction model/version; an extracted relation is `inferred` and cannot override a canonical metric/deploy/SCM source.
- **Input / tool / state**: versioned documents, OCR/text locator, quotation span, document digest, and extraction model/version.
- **Human gate**: critical production identity, metric definition, or causal edges cannot be confirmed only from an extracted graph.
- **Risks / failures**: large documents are slow; entity resolution may be wrong; a quotation that mentions something may not support the relationship; a document may be stale; prompt injection is possible.
- **Do not copy directly**: do not make the PDF graph the core data plane. Production changes should come from canonical deploy/SCM adapters.
- **Alignment with greenfield requirements**: conditionally aligned; it may serve as one evidence-graph adapter but must preserve `observed/reviewer inference/unknown`.
- **Evidence strength**: medium for the UI mechanism; accuracy and performance at scale are `unknown`, and the authors explicitly acknowledge slowdowns on large documents.

### P9. Infer cross-database links from column names

- **Decision**: **Reject as evidence**; at most, retain as a candidate generator that requires verification. Neither A nor B may rely on it for attribution.
- **Problem addressed (author's objective)**: quickly find a possible join path when there is no explicit foreign key. [video `04:43.50–05:01.84`]
- **Mechanism**: within-database foreign keys are shown as solid lines; similar cross-database names such as `customer_id` are shown as dashed lines. The authors state at the end that these links depend on naming heuristics and may miss unusual schemas. [video `08:18.10–08:24.34`]
- **A/B adaptation if candidate generation is retained**: confirm each link with catalog/lineage data, sample uniqueness, type compatibility, an owner, or a validated query; mark an unconfirmed edge `inferred`.
- **Input / tool / state**: schema catalog, lineage, semantic registry, join tests, and data owner.
- **Human gate**: an unverified join cannot enter metric recomputation, scope mapping, or root-cause ranking.
- **Risks / failures**: same name with different meaning, different names with the same meaning, many-to-many explosion, cross-domain PII joins, and missed unusual schemas can directly create wrong numbers and false causal chains. The fixture in this demonstration was built for the ER display and shares `customer_id`; using its successful linkage to establish heuristic effectiveness would be circular, because the fixture was built to join.
- **Do not copy directly**: reject a dashed heuristic edge as fact. Also reject the conclusion that join generalization or a production path has been resolved merely because a purpose-built sample fixture connects in the UI.
- **Alignment with greenfield requirements**: conflicts if treated as evidence, because the requirements call for a stable source ID, an explicit relation basis, confidence, and a falsifier.
- **Evidence strength**: medium, video-only evidence for both the mechanism and its limitation; error rate is `unknown`.

### P10. Uploaded-files-only sandbox

- **Decision**: **Reject as-is**; retain the least-privilege principle.
- **Problem addressed (author's objective)**: restrict the agent to files that the user has placed in the workspace. [video `01:47.18–01:52.56`, `08:24.34–08:28.32`]
- **Why it is unsuitable for A/B**: A needs experiment/metric/runtime/SCM/deploy evidence; B needs alerts, logs, timelines, and flag/config/model/data changes. Uploaded files alone leave critical sources stale and without provenance, and they cannot verify deployed state.
- **Replacement**: allowlisted read-only adapters that return identity, freshness, authorization, and a receipt on every call; lack of permission must be reported as a coverage gap.
- **Input / tool / state**: source allowlist, credential scope, case time range, and redaction policy.
- **Human gate**: a new source or permission increase requires explicit authorization. Users must not be asked to download private production data manually to bypass permissions.
- **Risks / failures**: an uploaded snapshot may be stale, selectively cropped, or missing query/lineage data; the local sandbox may be secure while its conclusion is incomplete.
- **Do not copy directly**: sandbox confinement is not evidence completeness.
- **Alignment with greenfield requirements**: direct conflict if copied as-is; least privilege and read-only-by-default remain aligned.
- **Evidence strength**: medium, based on explicit author disclosure; A/B incompatibility follows directly from the requirements.

### P11. Four agent approaches and recommendation hints

- **Decision**: **Reject as a current design conclusion**; reconsider only if a future same-batch A/B evaluation demonstrates lift.
- **Problem addressed (author's objective)**: select ReAct, DRAGIN, Multi-agent, or Hybrid-B for different questions. [video `02:59.50–03:15.22`]
- **Mechanism**: the UI provides four approaches and a one-line intended use for each; a `classify_question` recommendation hint appears, while the demonstration still has a human select ReAct. The video does not show automatic routing execution or a receipt.
- **Input / tool / state**: route features, train/evaluation split, fallback, budget, and stopping rule are not described and are all `unknown`.
- **Human gate**: in any future trial, the route may affect only the investigation path, not the evidence gate; stop when cost or latency exceeds budget.
- **Risks / failures**: overfitting benchmark routing; multi-agent amplification of shared errors; delay in B; incomparable outputs from different engines.
- **Do not copy directly**: the authors provide no A/B benchmark, ablation, or failure cases. Four approach names are not a production practice.
- **Alignment with greenfield requirements**: direct introduction would violate requirements-first design. It may enter only after a baseline comparison establishes quality lift with acceptable p95 latency/cost.
- **Evidence strength**: only UI and narration, weak; A/B effects are `unknown`.

### P12. Demo/live mode, accounts, and general UI features

- **Decision**: **Reject from the diagnostic core**; these may be discussed separately as peripheral product requirements.
- **A/B applicability**: neither A nor B treats these features as diagnostic evidence. An offline fixture and clear runtime identity have supporting value in both.
- **Content**: demo scripted replay versus live engine, accounts, guided tour, adjustable layout, themes, keyboard shortcuts, and confirmation before clear/reset. [video `00:33.44–01:37.14`, `03:55.60–04:05.50`, `06:54.98–07:33.10`]
- **Actual value**: offline replay helps training and demonstrations; reset confirmation reduces accidental deletion; usable UI supports review.
- **Why reject as a core practice**: these features do not answer A's why/code/change questions or B's suspect-change/timeline questions. Treating them as architecture evidence would allow a polished demonstration to distort the decision.
- **Adaptation that may be retained**: clearly separate offline fixture, shadow read, and live production read, and display a receipt; do not rely on a `Live` chip alone.
- **Input / tool / state**: run mode, fixture ID, engine build, model/tool version, source manifest, authorization, and immutable run receipt. The video shows only UI state and none of this runtime-identity evidence.
- **Human gate**: before switching from offline/demo to a production read, re-confirm the source, permissions, and runtime identity. Reset/delete requires an exact target, impact scope, and recoverability statement.
- **Risks / failures**: scripted replay may be mistaken for real validation; a live label lacks runtime identity; confirmation does not establish recoverability.
- **Do not copy directly**: a `Live` chip, successful login, or confirmation dialog cannot be reported as proof of production runtime, security enforcement, or recoverability.
- **Alignment with greenfield requirements**: no conflict, but not part of the MVP core. The requirements already call for staged proof through offline cases, local adapters, and production shadow reads.
- **Evidence strength**: medium for the UI mechanism; runtime identity and production readiness are `unknown`.

## 5. Combined judgment for the two scenarios

### A — Post-experiment

The inspectability of the investigative process is worth adapting:

1. Use deterministic profiles and metric validators to check data and experiment validity first.
2. Display the original user prompt, plan, query, result, validation, and gaps in a structured form so that steps supplied by the prompt are not misreported as agent discoveries.
3. Bind numbers to an exact query and independent recomputation.
4. Before generating any data/code change proposal, show the exact target, diff, impact, test, and rollback, then require a human gate.
5. Isolate the experiment's evidence by session.

The video lacks A's critical chain:

```text
experiment hypothesis / exposure / SRM
  -> metric component / segment loss
  -> runtime event / service path
  -> exact deployed repo / SHA / file / symbol
  -> proposed change / targeted validation / rollback
```

Team 1401 therefore supplies only interaction/control candidates; it does not establish post-experiment diagnostic capability.

### B — SEV

The time-sensitive review surface is worth adapting:

1. Display signal checks, the current plan, and obtained/missing evidence quickly.
2. Authorize read-only tools by capability; disable arbitrary Python by default; require human approval only for high-risk actions.
3. Preserve raw input, output, and a receipt for every query/action.
4. Make evidence visible so that the incident commander can inspect it.

The video provides none of B's critical chain:

```text
alert / verified drop / changepoint
  -> affected scope
  -> deploy + config + flag + model + data timeline
  -> deployed proof + runtime reachability
  -> supporting / contradicting / missing evidence
  -> next safe check / human rollback packet
```

Co-pilot's “approve every step” behavior could also slow a SEV response. Gates should be selected by risk rather than copied directly.

## 6. Evidence gaps and non-generalizable claims

The video does not provide the following information, which must remain `unknown`:

- Team 1401 paper, complete architecture, source code, fixed commit, dependencies, and deployment manifest;
- Specific DataAgent-Bench tasks, scores, baseline, split, repetitions, error rate, and cost;
- Route rules, ablations, failure recovery, stopping conditions, and tool budgets for the four agent approaches;
- Account isolation, password storage, tenant/security testing, and actual credential storage/transport enforcement. The UI states only that credentials are plaintext in `localStorage`, persist across sessions, and are sent only to the local backend; source code and security testing are unknown;
- Whether tool toggles and approval are enforced server-side;
- OS/container isolation, network egress, credential access, filesystem boundaries, and audit enforcement when `execute_python` is enabled by default;
- SQL read-only enforcement, query timeout, row limit, truncation, transaction behavior, and receipts;
- Validation, rollback, full-dataset impact, and business semantics for Data Doctor fixes. The UI claims that the pandas sandbox forbids imports/I/O, but actual enforcement and escape testing are unknown;
- PDF graph extraction accuracy and quotation-to-relation entailment;
- Integration with production code, SCM, deploys, flags, config, models, and schema/data lineage;
- Experiment validation, metric-definition version, SRM, changepoint, and counterfactual analysis;
- Incident latency, p95, concurrency, and behavior for stale, partial, or unauthorized sources;
- Failure cases beyond the two demonstrated answers;
- Independent decomposition/join-discovery capability for the first demonstration: the prompt already specifies the database, two-table join, formula, output columns, and sort order;
- Whether the first specific run used four tables: the Event Log shows only one `execute_context_sql` call, and the summary's “4 tables” has no execution receipt;
- Generalization of the cross-DB heuristic to a non-purpose-built schema: the demonstration fixture was designed for the ER display and shares `customer_id`.

Words used in the video such as “correct,” “verified,” “live,” “same engine,” “real account,” and “cannot call disabled tool” can be recorded only within the scope actually demonstrated. They are not evidence of production readiness or general accuracy.

## 7. Graph / trace UI: observations and gaps in the production evidence graph

> This section is a research judgment. The owner has not confirmed an evidence-graph product contract. This section does not freeze the final specification.

> **Current-authority note (2026-08-12; not a revision of the source audit):** That statement accurately records the research phase. The logical Evidence Graph and Trace contract is now owner-confirmed in the [planning decision packet](planning-decision-packet.md), the closed [canonical domain and policy ticket](wayfinder/freeze-canonical-domain-policy-contracts.md), and the [final architecture specification](final-architecture-spec.md). The video observations, timestamps, and reviewer inferences below remain Team 1401 evidence only; they do not ratify the new product. Live prototype interaction and visual acceptance remain open in the [Observability-First Review Surface ticket](wayfinder/prototype-observability-first-review-surface.md). Sensitive production display remains blocked pending the [Production Evidence Authority and Access Boundaries ticket](wayfinder/establish-production-evidence-authority.md), including its production-owner and security/privacy decisions.

### 7.1 Observed in the video: specific graphs and operations

#### Schema / relationship graph

- `04:43.52–05:10.36`; frames `288.jpg` (04:48) and `303.jpg` (05:03). The visual shows `3 databases · 8 tables · 7 links`.
- Each node is a table card. The card displays columns, types, PK/FK markers, and row count. Databases are distinguished by color.
- A solid edge represents a within-database foreign key. A dashed edge is labeled `cross-DB join`. The latter is a mapping assertion, not observed lineage and not causality.
- A search box, zoom, and fit/fullscreen are visible. The video shows zoom moving from 69% to 100%, followed by fit. The footer says tables can be dragged and that users can scroll to zoom and pan. These are navigation features.
- **Not observed**: entering a search term; a separate detail panel after clicking a table; edge provenance; edge history; collapse/group/filter; timeline; contradiction, supersedes, or invalidation.
- **Author claim**: Relationship view inspects all database schemas; users can search by table name; solid lines are FKs; the dashed link comes from shop and CRM sharing `customer_id`. [video `04:43.52–05:10.36`]
- **Reviewer inference**: a solid link may come from schema metadata, but there is no source code or receipt. The dashed link depends on a naming heuristic, and the fixture was designed for the ER demonstration and shares `customer_id`. It cannot establish general join discovery.

#### PDF knowledge graph

- `05:10.36–05:43.32`; frames `318.jpg`, `322.jpg`, `325.jpg`, `328.jpg`, `331.jpg`, `333.jpg`, `337.jpg`, `340.jpg`, and `343.jpg`.
- The header shows `29 entities · 8 clusters · 25 relations · LlamaIndex`. Node types include Person, Organisation, Project, Place, Concept, Date, and Other. Edges carry relation labels. Dashed boxes are cluster groups.
- Observed operations: clicking `Project Falcon` shows incoming/outgoing relations and a `p.1` page pointer; `Collapse all` changes `0/8` to `8/8 collapsed`; `Expand all` returns it to `0/8`; filtering switches to `Person` and back to `All`; zoom moves out to 60%; the graph is fitted.
- A search box is visible, but no input is observed. Timeline, trace overlay, edge version/history, contradiction, supersedes, and invalidation are all **not observed**.
- **Author claim**: the model extracts entities/relations from the PDF; every relation has a verbatim quotation from the source page. [video `05:10.36–05:27.62`]
- **Observed fact**: a page pointer and relation list are visible. Complete verbatim quotation text was not independently verified visually. A page pointer is a locator, not entailment proof.
- **Observed contradiction**: the upload UI in `155.jpg` (02:35) labels `project_falcon_brief.pdf` as a `3-page PDF`; from `318.jpg` (05:18), the KG header says `1 page`. The video does not explain the discrepancy. It must remain an unresolved source-identity/parser-coverage gap; full graph coverage of the corpus cannot be assumed.
- **Reviewer inference**: PDF nodes/edges are model-extracted assertions. There is no receipt for source digest, extractor version, ACL, deduplication, completeness, or accuracy.

#### Plan, Event Log, and exact SQL

- `06:00.78–06:21.18`; frame `375.jpg`. Plan, Event Log, Answer, and SQL are visible.
- The Event Log shows `RUN_STARTED`, `KNOWLEDGE_GRAPH`, `AGENT_THOUGHT`, and `TOOL_EXECUTION_START/SUCCESS`. This is a time-ordered execution/debug trace, not a node-edge evidence graph.
- The `KNOWLEDGE_GRAPH` event name and entity JSON do not constitute an auditable evidence graph.
- This run shows only one `execute_context_sql` call followed by `answer`. Exact SQL is a query recipe/receipt UI. It does not automatically create links from claim to evidence, contradiction, falsifier, or production change.
- **Not observed**: proof of trace completeness, immutable event identity, runtime/deploy identity, claim status, edge provenance, timeline, or source freshness.

### 7.2 How the graphs are generated: evidence layers

| Surface | Directly visible | Author claim | Repository/source implementation | Reviewer inference |
| --- | --- | --- | --- | --- |
| Schema graph | Table/column/key/row-count cards; solid/dashed links | Inspects all schemas; shared names create a cross-DB link | **Not observed**. Team 1401 has no paper or repository | A solid link may be derived metadata; a dashed link is a heuristic mapping assertion |
| PDF KG | Entities, typed relations, clusters, page pointer; header says `LlamaIndex` | The model reads the PDF; every relation has a verbatim quotation | **Not observed** | Nodes/edges are extraction assertions; a page pointer does not verify the relation or quotation |
| Plan/Event Log | Run events, tool name, raw input, SQL, result | Displays agent steps and an evidence trail | **Not observed** | An execution trace helps replay/debug but is not a claim/evidence graph |

The Team 1401 video does not show a graph generated jointly from production metrics, agent artifacts, runtime/deploy changes, or formal claim/evidence links. Adjacent capabilities cannot be used to fill in that missing mechanism.

### 7.3 What the UI actually helps answer

- The schema graph helps users see which tables, columns, keys, and candidate join paths exist in the current fixture.
- The PDF KG helps users browse entities/relations and return to a page locator.
- Collapse/expand, filter, search, zoom, fit, and clusters mainly improve navigation and readability. They do not themselves improve evidence quality.
- The Event Log helps users see the run sequence. Exact SQL helps users inspect the computation recipe.
- The Plan is narration. It may repeat the user prompt. It is not independent evidence.
- UI color, layout, clusters, and connecting lines do not automatically establish provenance, accuracy, production reachability, or causality.

### 7.4 Adopt / Adapt / Reject

- **Adopt (research judgment)**: node-click detail; source locator; collapse/expand; type filters; search/zoom/fit; distinct edge styles; exact query/result receipts; faceted presentation of execution trace and final evidence.
- **Adapt (research judgment)**: schema/KG navigation and traces. A production version requires a stable source ID, digest, observed/retrieved time, freshness, ACL, runtime/deploy identity, edge type, status, provenance, and falsifier. Mapping and causal edges require a mechanical or human gate.
- **Reject (research judgment)**: using the PDF KG as the production evidence backbone; treating the fixture's dashed join as verified lineage; treating the `KNOWLEDGE_GRAPH` debug event, Plan, or Event Log as a complete evidence graph; treating a page pointer as quotation proof; drawing every connection as causal.

### 7.5 Production A/B chain: gaps in Team 1401

Target chain, checked item by item:

```text
metric -> surface/component -> query/result -> ACL/corpus
  -> pipeline/runtime
  -> typed production change(code/config/flag/model/data)
  -> claim -> verification/falsifier
  -> recommendation / not-applied diff / rollback-ready packet
```

- `metric`: only a demonstration result. Canonical metric definition/version, baseline/target, cohort/window, experiment validity, and SEV changepoint are all **not observed**.
- `surface/component`: **Not observed**.
- `query/result`: partially observed. Exact SQL and result are visible; parameters, time range, source digest, truncation, a complete row-count guarantee, and an independent validator are not.
- `ACL/corpus`: **Not observed**. Only an uploaded-files UI claim is present. There is no ACL enforcement, manifest, freshness, or completeness; the PDF `3-page` versus KG `1 page` contradiction also remains.
- `pipeline/runtime`: **Not observed**. A `Live` chip and model label are not deployed runtime identity. There is no pipeline job, image, SHA, or deploy receipt.
- `typed production change`: code/config/flag/model/data changes are all **not observed**.
- `claim`: natural-language answers and PDF relations are visible, but there is no formal claim type/status.
- `verification/falsifier`: the direct SQL check is only a `speaker claim` and has no receipt. Contradicting evidence and a falsifier are **not observed**.
- `recommendation / not-applied diff / rollback-ready packet`: **Not observed**. Data Doctor's local preview is not a production change packet.

### 7.6 Edge taxonomy: not every line can be causal

- **Observed fact**: recorded directly by a canonical source. Requires source, digest, scope, and time.
- **Derived fact**: computed from observed facts through a replayable query/recipe. It is not causal.
- **Mapping assertion**: entity resolution, component mapping, or a heuristic cross-DB join. Requires confidence, basis, and owner validation.
- **Causal claim**: requires temporal order, mechanism, alternative explanations, intervention/rollback, or a falsifier. Team 1401 does not establish this.
- **Contradiction**: two pieces of evidence cannot both be true. The PDF `3-page` versus KG `1 page` discrepancy must be retained rather than silently overwritten.
- **Supersedes / invalidation**: old evidence is replaced or invalidated by a new version, expiry, or an erroneous result. This is **not observed** in the Team 1401 UI.

## 8. Final recommendation

The clean target state from Team 1401 that merits greenfield evaluation is:

- **Adopt**: the case/session-isolation principle; let users see the original prompt, plan, tool action, and source-backed result together; bind numbers to an exact query receipt. The video does not establish an independent validator.
- **Adapt**: turn tool switches into a server-side capability contract; trigger approval by risk; keep diff-before-write in a separate action lane; use a document graph's page pointer only as a locator, while quotations and relations still require verification.
- **Reject**: arbitrary Python enabled by default; treating a prompt-specified join as autonomous discovery; expanding one SQL run into a proven four-table path; treating links in a purpose-built fixture as evidence that the heuristic generalizes; treating four competition agents, an uploaded-files-only sandbox, generic Data Doctor fixes, or a polished UI as the production diagnostic architecture for A/B.

Team 1401's strongest practice is **inspectability + controllability**. Its central gap is **production provenance + causal discipline**. The former should be adopted; the latter must be built from the A/B requirements and cannot be inferred from this video.
