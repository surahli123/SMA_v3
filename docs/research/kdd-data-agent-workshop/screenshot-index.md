# KDD Data-Agent Workshop Screenshot Evidence Index

## Scope and reading guide

- **Source**: 73 workshop PNG screenshots from the same date. Filename times run from `6.04.15 PM` to `8.09.39 PM`, sorted by filename time; no other date is included. Raw screenshots are not included because of size, privacy, and source availability.
- **Method**: each image was read visually. “Excerpt” means visible original wording or a faithful short extract; “visual meaning” describes only visible relationships; “plain-language explanation” explains that image directly, not an overall design.
- **Sparse-sampling caveat**: these 73 images are only a partial sample of the presentation slides, not the complete deck. A missing screenshot must not be used to infer that a time segment, page, or spoken point did not exist or was not said. This file proves only what is visible in the screenshots.
- **Audio boundary**: the complete meeting recording (about 2 hours 13 minutes) is an independent primary line. The audio index must cover the full duration; segments without a matching screenshot must still be transcribed, segmented, summarized, and marked `audio-only`, not removed or downgraded as irrelevant.
- **Cross-alignment boundary**: audio segments that align to screenshots are the priority cross-check area. Slide images may correct ASR terms, numbers, flow, and speaker/topic labels; text visible only on a screenshot must not be inserted into the transcript unless spoken. Report coverage separately as `audio coverage`, `screenshot coverage`, and `cross-aligned coverage`.
- **Evidence boundary**: screenshots are observational evidence from workshop/demo material. They do not prove online performance, causality, generality, or adoption value. Speaker names are usually not visible; when a name is not explicit, write “unable to confirm.”
- **Third ASR boundary**: the `Mac Voice Memos ASR candidate` has no timestamps, cannot override Whisper, and cannot add content that is not visible in a screenshot. Its raw text is not included because of privacy and source availability. The correction log below uses only three statuses: `direct ASR agreement`, `screenshot-supported correction`, and `unresolved`.
- **Direction boundary**: this index is not organized around legacy SMA modules, old contracts, migration cost, or compatibility. A later requirements-first review may compare these screenshot practices with the two real scenarios, KDD works, and legacy SMA separately; this file does not make adopt/adapt/reject decisions.
- **Confidence**: high = title and key text are clear; medium = the main thread is readable but small text/cropping affects details; unable to confirm = the image does not support the conclusion.

## Topic 1 — Challenges, unified querying, and lightweight-model guardrails (01–10)

### 01 · 2026-08-11 6:04:15 PM

- **File**: `Screenshot 2026-08-11 at 6.04.15 PM.png`
- **Visible title**: `02 · WHY IT IS HARD` / **The Challenges**.
- **Key excerpt**: `No shared schema.` The same column has different names across sources; units can change from `100 million CNY` to `millions`, with no mapping. `Documents are prose, not tables.` Fields are scattered across paragraphs and pages, and chunk-and-merge can silently drop rows. `Video frames deceive.` The on-screen answer may be a decoy, and ASR can corrupt domain terms. `3B parameters` may hallucinate columns, write unparseable SQL, and loop on tool calls.
- **Visual meaning**: Four colored bullets summarize failure sources in heterogeneous inputs, documents, video, and model/tool calls.
- **Plain-language explanation**: Inputs differ, long documents are hard to join, video can mislead, and the model can write nonsense or loop.
- **Confidence / ambiguity**: High; the full text is clear.
- **Speaker/topic transition clue**: speaker unable to confirm; this starts the challenge segment (“why it is hard”); the next slide moves to the overall design.

### 02 · 2026-08-11 6:06:12 PM

- **File**: `Screenshot 2026-08-11 at 6.06.12 PM.png`
- **Visible title**: `04 · THE OVERALL DESIGN` / **Unify, Then Query**.
- **Key excerpt**: Models the full challenge as **SQL generation problem**: structured `CSV / JSON / SQLite`, unstructured `Markdown / PDF`, and video `MP4 slide recordings` are preprocessed separately; `Multi-format registration → DuckDB`, `PDF reflow + fan-out`, and video `Packet-size keyframes`, `word-level timestamps`, and `ASR + layout, time-aligned`; unified `DuckDB` runtime; `Table-relevance filter` gives relevant table schemas + sample rows and only table names for the rest (`median 93%`); solver tools are `explore_data / read_solver / edit_solver / run_solver`, outputting `prediction.csv`.
- **Correction note**: `screenshot-supported correction`: the image shows `SQL generation`, `DuckDB`, `Packet-size keyframes`, and `word-level timestamps`; these only correct the concurrent audio candidate and do not expand into an unshown speaker claim.
- **Visual meaning**: Three input types pass through modality preprocessing, a unified database, relevant-table filtering, and a bounded solver to produce one CSV per task.
- **Plain-language explanation**: Convert different materials into one queryable table set, then let the agent write SQL.
- **Confidence / ambiguity**: High; the bottom tool/output text is small, but the main flow is clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from the challenge to the overall design: “unify, then query.”

### 03 · 2026-08-11 6:08:08 PM

- **File**: `Screenshot 2026-08-11 at 6.08.08 PM.png`
- **Visible title**: `05 · THE HARNESS` / **Six Constraints That Make a Lightweight Model Reliable**; the upper-right sentence reads “Correctness comes from narrowing the search space, not from more freedom.”
- **Key excerpt**: `Scaffold`: I/O is prewritten; the model only fills the SQL template. `Four Tools`: explore / read / edit / run; no shell, filesystem, or sub-agents. `Normalize`: the execution boundary fixes names and quoting, including Chinese field names translated as “net value” and “manager (new).” `Collapse`: relevant tables get schema + samples; the rest get names only (`93% of tables → bare name`). `Vote`: irreversible calls run concurrently for multiple rounds; `3 rounds → majority`, with ties favoring retention. `Truncate`: returns only the nearby error, `3 frames + message`, to the model.
- **Visual meaning**: Six cards narrow inputs, tools, context, calls, and error feedback.
- **Plain-language explanation**: Restricting what the model can do, see, and receive after an error makes it more stable.
- **Confidence / ambiguity**: High; the full text is clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from the overall design to harness reliability constraints.

### 04 · 2026-08-11 6:10:18 PM

- **File**: `Screenshot 2026-08-11 at 6.10.18 PM.png`
- **Visible title**: **Doc fan-out: turning a narrative document into a queryable table**.
- **Key excerpt**: `task_5/patient.md` has `322` prose lines and becomes `50 rows × 27 cols`; the planner emits one JSON plan and freezes `record_universe = 50`, schema, and a normalize spec; `6 workers` run in parallel, each owning an attribute group and scanning all 50 entities (not pages); a structural-check example has only 47 rows in attempt 0, missing IDs `786542 / 912034 / 556781`; it is returned to worker #2 and attempt 1 restores 50 rows; then outer-join, column normalization, sandboxing, and revision follow.
- **Correction note**: `screenshot-supported correction`: the image shows `record_universe` (with an underscore). Mac ASR’s `recorded universe` is only a candidate and does not replace the visible wording.
- **Visual meaning**: Fan-out splits by attribute group rather than page, checks omissions against a fixed row universe, then reruns.
- **Plain-language explanation**: Each attribute group scans the full record set; missing entities are recovered rather than silently dropped.
- **Confidence / ambiguity**: High; the lower code and ending are cropped, but the key numbers and flow are readable.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from constraints to prose extraction and validation retries.

### 05 · 2026-08-11 6:21:09 PM

- **File**: `Screenshot 2026-08-11 at 6.21.09 PM.png`
- **Visible title**: **Solution architecture — one SQL surface, two tools** (NV DATA EXPLORER · V15).
- **Key excerpt**: Heterogeneous sources are preprocessed behind one interface; the agent has only two tools; canonical `answer.csv` feeds the ensemble. A background async thread pool converts PDF→`.md` (pypdf) and Video→transcript + keyframes (faster-whisper + ffmpeg) without blocking structured inputs; SQLite is authoritative; CSV/JSON, Prose/PDF, and MP4 map to `context.db` (one table per file, conflicts skipped); `schema-scout / schema-preempt` provide schema at turn 0; `prose_helper` handles QA or table extraction; video keyframes + transcript are caption-aligned in the first message; stateful Python preloads `sql() / schema() / write_answer()`; `answer.csv` is written atomically, followed by `5–10 attempts` majority, col-trim/kAN, and finally `prediction.csv`; scheduling is A structured → B prose → C video → D video+prose; `knowledge.md` injects units, answer grain, and allowed columns.
- **Correction note**: `screenshot-supported correction`: the upper right shows `NV DATA EXPLORER · V15`, and the visible model name is `Qwen3.5-35B-A3B`. This is the model name on this NV slide and cannot determine the first talk’s Qwen3.5 suffix.
- **Visual meaning**: One SQL surface, asynchronous media preprocessing, few tools, parallel attempts, and final voting.
- **Plain-language explanation**: Prepare one unified database, route the model through fixed entry points, and merge multiple answers.
- **Confidence / ambiguity**: High; some small text needs magnification, but the main flow is clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from the extraction example to the full solution architecture.

### 06 · 2026-08-11 6:23:45 PM

- **File**: `Screenshot 2026-08-11 at 6.23.45 PM.png`
- **Visible title**: **Preprocessing — build one uniform SQL surface**.
- **Key excerpt**: CSV uses pandas→`to_sql` (one table per file, using the filename stem); JSON records or bare lists→table; the authoritative DB is copied as-is; same-named CSV/JSON files are skipped rather than merged; all results in `context.db` are accessed through `schema()` / `sql()`; `schema-scout` reports duplicate columns, look-alikes `AnnRet` vs `FundReturn`, and the inference `manager_id → manager.id`; `schema-preempt` provides the full schema first at turn 0; structure and values are normalized, including a Chinese unit conversion from “ten-thousand yuan” to “million yuan”; the system prompt hard-codes DISTINCT entity lists, NULL rules, rows-vs-entities grain, units/precision, and requested columns only.
- **Visual meaning**: Input formats, table names, column ambiguities, units, and answer grain are handled and exposed before execution.
- **Plain-language explanation**: Fix formats, names, units, and row grain first to reduce model guessing.
- **Confidence / ambiguity**: High; the full text is clear.
- **Speaker/topic transition clue**: speaker unable to confirm; continues the schema/preprocessing details of the unified SQL surface.

### 07 · 2026-08-11 6:25:05 PM

- **File**: `Screenshot 2026-08-11 at 6.25.05 PM.png`
- **Visible title**: **prose_helper — two modes over a large document**.
- **Key excerpt**: `mode=answer`: QA over the full document, returning plain text for threshold/eligibility/filter decisions (for example, `minimum holding period → ≥90 days`); `mode=table`: extract repeated records from the full document and register a real SQLite table for later SQL (for example, `prose_extraction_1`); table mode uses one full-document LLM call, temp 0, thinking off, and compact JSON, with no shard/coalesce/multi-turn stitch; shared error handling uses 1+2 attempts and transient retry; when `finish_reason=length`, truncate deterministically and record `too big`; timeout and endpoint saturation are counted separately, with helper and outer-tool timeouts decoupled.
- **Visual meaning**: Large documents take either a “ask for one value” or “materialize as a table” path.
- **Plain-language explanation**: Ask directly for a single value; materialize repeated records into a table before SQL instead of stitching fragments.
- **Confidence / ambiguity**: High; bottom text is slightly blurry, but the key rules are clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from general preprocessing to the document helper’s two modes and stability.

### 08 · 2026-08-11 6:26:18 PM

- **File**: `Screenshot 2026-08-11 at 6.26.18 PM.png`
- **Visible title**: **Video — captioned frames, read the right slide**.
- **Key excerpt**: Video is converted to caption-aligned keyframes + transcript and inlined; frames prioritize audio pauses, with ffmpeg scene fallback, RMSE deduplication, and 1024px output; audio uses faster-whisper small (int8, VAD) + an LLM homophone fix; alignment buckets each transcript segment to a keyframe and renders a caption strip below the image; the first message contains the full transcript + each captioned keyframe (≤50); captions bind spoken constraints to the corresponding slide; exact terms/values prioritize on-screen text; video-anchor values are treated as truth and not recomputed from the DB.
- **Visual meaning**: Speech, the corresponding slide, and on-screen values are bound to one time point to reduce decoy misreads.
- **Plain-language explanation**: Tell the model which slide a sentence belongs to; slide values take priority.
- **Confidence / ambiguity**: High; the Chinese homophone-fix example and bottom text are slightly blurry.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from the document helper to multimodal video alignment.

### 09 · 2026-08-11 6:28:05 PM

- **File**: `Screenshot 2026-08-11 at 6.28.05 PM.png`
- **Visible title**: **Everything is SQL, and there is only one way in**.
- **Key excerpt**: One stateful Python tool + preloaded helpers; an AST guard blocks alternate paths. Run SQL only through `sql()` (no `sqlite3.connect`); structured files are already tables and use `schema()` / `sql()` (no `pd.read_csv`); documents use `list_docs / preview_doc / search_doc / prose_helper` (no `open / read_text`); answers can only use `write_answer()`→atomic `answer.csv`; Python can only use stateful `python()` (no shell); helpers are preloaded globals (no import); the namespace persists across turns; middleware redirects wrong tool names, plain-text tool calls, and wrong channels to the correct entry point.
- **Visual meaning**: All data reads, SQL computation, and answer writes use the prescribed entry points.
- **Plain-language explanation**: Do not let the model choose files, the interpreter, or the output path; correct bad calls where possible so the whole run does not fail.
- **Confidence / ambiguity**: High; the full text is clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from modality preprocessing to the single execution path and AST guard.

### 10 · 2026-08-11 6:30:52 PM

- **File**: `Screenshot 2026-08-11 at 6.30.52 PM.png`
- **Visible title**: **Ensemble & retry — coverage first, then vote+kAN**.
- **Key excerpt**: In long runs, each task gets at most 10 attempts; the scheduler is coverage-first (every task gets attempt 1 before any task gets attempt 2), with the most-contested tasks upgraded first; four consistent votes settle a task, contested tasks rise to 10, and never-valid tasks are abandoned after at most 5 tries; full parallel width; A structured → B prose → C video → D video+prose; the example clusters by column sets, keeps the column superset, uses col-trim to remove auxiliary code, and kAN keeps multiple name forms; `5× @temp0.4` gives per-column majority, and never trims name, abbreviation, or label fields, including their Chinese equivalents.
- **Visual meaning**: Give every task at least one attempt, then spend compute on contested tasks; merge by column-set and value consensus.
- **Plain-language explanation**: Ensure coverage first, then give unstable tasks more chances; do not casually remove key name columns when merging.
- **Confidence / ambiguity**: High; the lower-right is cropped, but scheduling and voting rules are readable.
- **Speaker/topic transition clue**: speaker unable to confirm; completes the unified SQL/execution-guardrail segment and moves to external workshop leverage/evaluation evidence.

## Topic 2 — Phase-gated ReAct, SQL result interface, and evaluation caution (11–18)

### 11 · 2026-08-11 6:44:25 PM

- **File**: `Screenshot 2026-08-11 at 6.44.25 PM.png`
- **Visible title**: **Challenges** (upper-right `Leverages`).
- **Key excerpt**: Three failure classes: `Evidence acquisition`: the search space is large, the agent stops too early, and it misses the needed source; `Huge Context`: multimodal observations create a long history and relevant evidence is hard to find (lost in middle); `Stability`: tool calls/queries may be invalid and the trajectory is stochastic.
- **Visual meaning**: Three columns cover evidence acquisition, context retrieval, and execution stability.
- **Plain-language explanation**: The agent may miss evidence, miss the key context, or make unstable calls.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from the previous solution details to another group’s “Leverages” failure modes.

### 12 · 2026-08-11 6:47:30 PM

- **File**: `Screenshot 2026-08-11 at 6.47.30 PM.png`
- **Visible title**: **Main Workflow: Phase-Gated ReAct Agent** (Leverages).
- **Key excerpt**: Four phases each have a goal, tools, and completion gate: `PLAN(list_context)` reads the question, schema metadata, and domain context; it passes only when the agent declares completion. `EXPLORE(describe_data · execute_sql · read_doc · grep)` checks schema/query/docs and ends only when the agent declares finished and 3 inspection calls succeed. `ANSWER(answer_from_sql)` is the single SQL exit and ends only after deterministic checks pass. `VERIFY(execute_sql · confirm_answer)` independently verifies; `confirm_answer` ends the phase or returns to ANSWER at most twice. Results are written to an answer table.
- **Visual meaning**: Phase gates, a tool allowlist, and at most two ANSWER↔VERIFY fallbacks.
- **Plain-language explanation**: Plan first, explore, submit, then verify independently; failures trigger bounded revision.
- **Confidence / ambiguity**: High; the bottom caption is readable.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from failure modes to the phase-gated workflow.

### 13 · 2026-08-11 6:48:32 PM

- **File**: `Screenshot 2026-08-11 at 6.48.32 PM.png`
- **Visible title**: **SQL as the Common Interface for Final Answers** (Leverages).
- **Key excerpt**: The agent cannot return free text; every answer goes through `answer_from_sql`, and scoring executes the result. Table evidence example: `SELECT ChiNameAbbr, ManagementFeeRatio FROM mf_fundarchives WHERE ManagementFeeRatio > 1.0`; document/video evidence is materialized as SQL literals, such as `SELECT '2023-11-04' AS launch_date UNION ALL SELECT '2024-02-17'`.
- **Visual meaning**: Database, document, and video evidence all become executable SQL results.
- **Plain-language explanation**: Do not submit text that merely looks like an answer; submit a result that machines can execute and check.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from the main workflow to the final-answer interface.

### 14 · 2026-08-11 6:49:02 PM

- **File**: `Screenshot 2026-08-11 at 6.49.02 PM.png`
- **Visible title**: **SQL as the Common Interface for Final Answers** (substantially repeats 13).
- **Key excerpt**: Repeats the `free-text ban`, `answer_from_sql`, table `SELECT`, and document/video literal examples.
- **Visual meaning**: Same as 13; emphasizes a modality-independent executable answer surface.
- **Plain-language explanation**: Same as 13: the final answer form is fixed as an executable result.
- **Confidence / ambiguity**: High; this is a duplicate screenshot with no new information.
- **Speaker/topic transition clue**: speaker unable to confirm; likely the same page held on screen or captured twice; the next image moves to verification.

### 15 · 2026-08-11 6:49:30 PM

- **File**: `Screenshot 2026-08-11 at 6.49.30 PM.png`
- **Visible title**: **Verification of the Agent’s Output** (Leverages).
- **Key excerpt**: Four checks sit between the submitted query and committed answer: (1) pre-execution structural constraints (percent must divide + scale; use DISTINCT only when requested); (2) post-execution rejection of empty/zero-column/schema-violating outputs and a full_name concatenation check; (3) independent LLM verification selects output columns and judges whether SQL follows the right evidence path; (4) self-verification + independent regeneration, where VERIFY gives a rule-level verdict and regenerates independently. On failure, repair SQL and commit after at most two tries rather than losing the result.
- **Visual meaning**: Static rules, execution-result checks, independent model review, and bounded retry are chained together.
- **Plain-language explanation**: Review SQL structure, then review the result, then have another checker review it; allow at most two edits.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from the answer interface to output verification.

### 16 · 2026-08-11 6:50:26 PM

- **File**: `Screenshot 2026-08-11 at 6.50.26 PM.png`
- **Visible title**: **Auxiliary Components** (Leverages).
- **Key excerpt**: The main workflow controls the flow; auxiliary components improve what the agent sees, its reasoning, and output checks: `Evidence preparation` classifies the domain, adds modality context, and turns text into queryable tables; `Reasoning support` provides schema/value profiles, numerical checks, and query feedback; `Output validation` selects requested columns, preserves value formats, and applies domain-specific row constraints.
- **Visual meaning**: Evidence preparation, reasoning support, and output validation support the main workflow.
- **Plain-language explanation**: Add one support layer for input, understanding, and acceptance so the main workflow does not carry everything alone.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from output verification to auxiliary components.

### 17 · 2026-08-11 6:51:04 PM

- **File**: `Screenshot 2026-08-11 at 6.51.04 PM.png`
- **Visible title**: **Auxiliary Components: Domain-Aware Guidance** (Leverages).
- **Key excerpt**: The detected domain changes both query instructions and expected row grain: `Classify the domain` infers clinical/financial/macroeconomic from schema metadata; `Set query conventions` (entity grain/aggregation/time reference); `Set output conventions` (row grain/deduplication; one row/entity vs repeated records); for example, patient-level means one row per person, while visit-level retains repeated visits.
- **Visual meaning**: Domain identification → query conventions → output row grain/deduplication rules.
- **Plain-language explanation**: Identify the business domain first, then decide how to aggregate, deduplicate, and output.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; narrows the general auxiliary components to domain-aware row grain.

### 18 · 2026-08-11 6:52:28 PM

- **File**: `Screenshot 2026-08-11 at 6.52.28 PM.png`
- **Visible title**: **Is the Phase Structure Worth It?** (Leverages · `5 ABLATION`).
- **Key excerpt**: Under the same evaluation setting (Phase 1 Local), baseline ReAct vs phase-gated shows `Score (λ = 0.5) 0.431 → 0.720 (+0.289)`; exact-match tasks `20 → 36/50 (+16)`; no final answer `34% → 6% (-28 pt)`; `n=50, iterations=10, SE≈0.01–0.02`. The footer explicitly warns that the end-to-end gain cannot all be attributed to phase gating (proposed system n=10 vs Starter-Kit ReAct n=3).
- **Visual meaning**: The table shows the phase-gated configuration doing better in this setting, while the footnote limits causal attribution.
- **Plain-language explanation**: The full configuration is clearly better here, but the slide does not show that phase gating caused all of the gain.
- **Confidence / ambiguity**: High; the numbers and cautionary footnote are clear.
- **Speaker/topic transition clue**: speaker unable to confirm; closes the Leverages segment with ablation and causal caution.

## Topic 3 — Human-guided work, skills, deterministic phases, and inspectable artifacts (19–34)

### 19 · 2026-08-11 6:53:21 PM

- **File**: `Screenshot 2026-08-11 at 6.53.21 PM.png`
- **Visible title**: **Autonomous Way Failed in Our Setting** (the upper-right Leverage title is cropped).
- **Key excerpt**: `automatic loop failed` (local fixes / leakage prompts); `Human-guided loop worked`: hypothesis → implementation → validate → report, with the agent running and monitored in the background. The chart shows kobushi λ0.5 score/experiment + best-so-far envelope, `N=107`; the blue line is leakage-excluded rep_mean best-so-far, green circles are n=3 mean±std, and red diamonds are LB v1/v2/v5/v11 submissions.
- **Visual meaning**: Local iteration scores and leaderboard submissions are overlaid, showing variance and gaps; a person proposes hypotheses while the agent executes and reports.
- **Plain-language explanation**: Fully automatic patching was unstable; human direction plus agent validation worked better.
- **Confidence / ambiguity**: High; the upper-right text is cropped and some legends are small.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from phase-gated evaluation to another practice report: automatic loop failure versus human-guided success.

### 20 · 2026-08-11 6:56:57 PM

- **File**: `Screenshot 2026-08-11 at 6.56.57 PM.png`
- **Visible title**:**Our core approach**.
- **Key excerpt**: `We wrote a skill and ran it on a coding agent`; qwen-code already provides the agent loop, tools, and subagents; the skill is reusable plain-language Markdown loaded per task; example command `/kdd-cup-data-analysis task_xxx`.
- **Visual meaning**: A task process is written as a loadable skill and handed to an existing coding-agent harness.
- **Plain-language explanation**: A reusable instruction sheet drives the general-purpose agent.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; starts the skill-based coding-agent approach.

### 21 · 2026-08-11 6:57:54 PM

- **File**: `Screenshot 2026-08-11 at 6.57.54 PM.png`
- **Visible title**:**Our SKILL.md in a nutshell**.
- **Key excerpt**: Critical Rules: `Never ask user anything` (a question means task failure); keep calling tools until `prediction.csv` is written and verified; do not load large context beyond `knowledge.md`. Workflow: read `task.json` → EDA (read `knowledge.md` first, hand docs/video to reader subagents) → write `approach.md` → write/run Python and save `prediction.csv` → reload with pandas to check content and format.
- **Visual meaning**: Cards for rules and a linear workflow.
- **Plain-language explanation**: The agent must finish the run itself, isolate large materials, and reload the file to confirm format.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from what a skill is to its concrete rules.

### 22 · 2026-08-11 7:01:02 PM

- **File**: `Screenshot 2026-08-11 at 7.01.02 PM.png`
- **Visible title**:`PHASE-2 IMPROVEMENTS` / **Handling documents (PDF / Markdown) v2**.
- **Key excerpt**: Loading a large document into the main context overflows it; public data documents are essentially prose records; a new `doc-reader` reads the full text and stores CSV; the main agent uses Python as if handling a table and consumes less context; estimated A-Board gain `≈ +0.06` (mixed with the skill rewrite).
- **Visual meaning**: A dedicated reader structures the long document first; the main agent consumes only the result.
- **Plain-language explanation**: Turn long documents into tables first so the main agent is not filled by the full text.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from skill rules to the phase-2 document improvement.

### 23 · 2026-08-11 7:02:02 PM

- **File**: `Screenshot 2026-08-11 at 7.02.02 PM.png`
- **Visible title**:`PHASE-2 IMPROVEMENTS` / **Handling video (MP4) SRT v7 · OCR v10**.
- **Key excerpt**: Qwen3.5 can view video but cannot hear it and often misreads on-screen characters/numbers; a new `video-reader` combines video frames, whisper.cpp-generated SRT, and scene-based PaddleOCR, while an LLM labels scene changes; estimated gains are SRT `≈ +0.065` and OCR `≈ +0.04`.
- **Visual meaning**: Convert video to subtitles and screen-reading text before handing it to the main agent.
- **Plain-language explanation**: Turn hard-to-hear or misread content into text and scene information first.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from the document reader to video preprocessing.

### 24 · 2026-08-11 7:03:14 PM

- **File**: `Screenshot 2026-08-11 at 7.03.14 PM.png`
- **Visible title**:`PHASE-2 IMPROVEMENTS` / **Adding a reviewer agent v9**.
- **Key excerpt**: On the same task, one round is right and the next is wrong; a second agent runs after the executor and must `criticize`, not `approve`, and redo when needed; `Treat executor's analysis only as a hypothesis. It may be wrong.` The independent reviewer sometimes breaks a correct answer but more often fixes an error; estimated A-Board gain `≈ +0.045`.
- **Visual meaning**: An executor is chained to an independent critic that can trigger a redo.
- **Plain-language explanation**: Do not let the executor prove itself; give another role the job of finding errors.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from input preprocessing to output review.

### 25 · 2026-08-11 7:04:50 PM

- **File**: `Screenshot 2026-08-11 at 7.04.50 PM.png`
- **Visible title**: `WHAT WE LEARNED` / **What didn’t work**.
- **Key excerpt**: Playbooks had a frontier model inspect correct answers and write an ideal `approach.md` for each public task, to improve the skill and let the executor read a similar domain, but showed no clear gain; answer merging with 2 executors → reviewer often choosing wrong, while 3 executors → majority vote helped locally but showed no clear A-Board effect.
- **Visual meaning**: Lists negative or unstable results from exemplar playbooks and simple multi-executor/vote schemes.
- **Plain-language explanation**: Plausible demonstrations and simple voting did not produce reliable end-to-end gains.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; enters the reflection segment with practices that did not work.

### 26 · 2026-08-11 7:05:51 PM

- **File**: `Screenshot 2026-08-11 at 7.05.51 PM.png`
- **Visible title**: `WHAT WE LEARNED` / **What we couldn’t confirm**.
- **Key excerpt**: Promising but unconfirmed: fork qwen-code; shorten system prompts/tool descriptions/unused tools; an agent following a `knowledge.md` worked exemplar, but too infrequently; enabling `<think>` was clearly better locally, but its A-Board effect could not be attributed (only v14 enabled it and other changes were present).
- **Visual meaning**: Marks changes with signal but confounded variables as unconfirmed.
- **Plain-language explanation**: The experiment showed possible gains but did not isolate their causes.
- **Confidence / ambiguity**: High; the “unconfirmed” qualification is clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from failed practices to practices that could not be confirmed.

### 27 · 2026-08-11 7:07:37 PM

- **File**: `Screenshot 2026-08-11 at 7.07.37 PM.png`
- **Visible title**: `WHAT WE LEARNED` / **What was hard**.
- **Key excerpt**: The agent often ignored the skill (for example, loading a huge file into context); repeating the same rule in different wording helped somewhat but hit model limits; local scores varied widely across runs under the same configuration, while averaging many runs was compute-limited; phase 1 used an LLM to polish the skill, while phase 2 was mostly hand-written because the LLM made it verbose or omitted key rows.
- **Visual meaning**: Summarizes compliance, reproducible measurement, skill maintenance, and compute-budget difficulties.
- **Plain-language explanation**: Writing a rule does not make the agent follow it; the same setup can vary, and maintaining the prompt can introduce problems.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from experimental conclusions to operating difficulties.

### 28 · 2026-08-11 7:08:29 PM

- **File**: `Screenshot 2026-08-11 at 7.08.29 PM.png`
- **Visible title**: **Where our approach fits**.
- **Key excerpt**: The trend is `ReAct → orchestration frameworks → coding agent + skills`; ReAct is think/act/observe with no preset workflow; frameworks plan the structure ahead of time (LangGraph/CrewAI); coding agent + skills is a ReAct loop with a general harness, with skills/subagents handling complex work (Claude Code/Codex); the bottom note says the last option uses only skills + subagents on qwen-code and does not hand-write the workflow.
- **Visual meaning**: An arrow positions three forms of agent organization.
- **Plain-language explanation**: Put more flow control in reusable skills and a general harness instead of hard-coding every task.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; closes the reflection and enters method positioning.

### 29 · 2026-08-11 7:14:51 PM

- **File**: `Screenshot 2026-08-11 at 7.14.51 PM.png`
- **Visible title**: **Our Approach**.
- **Key excerpt**: `Deterministic orchestration through bounded phases`; input `task question + all-modalities data` → bounded phase; current state enters a semantic phase agentic loop (observe/reason/act) → inspectable artifact; a deterministic gate decides the next phase; output `validated answer · published.csv · audit trail`.
- **Visual meaning**: Input, bounded phases, an in-phase agent loop, inspectable artifacts, deterministic gates, and published output.
- **Plain-language explanation**: Exploration can be flexible inside a phase, but phase boundaries and publishing conditions are fixed.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from method positioning to the bounded-phase claim.

### 30 · 2026-08-11 7:15:14 PM

- **File**: `Screenshot 2026-08-11 at 7.15.14 PM.png`
- **Visible title**: **Our Approach**.
- **Key excerpt**: `Core agentic = discover / solve / review`; `Conditional agentic = repair / learn`; `Deterministic gates = execute / validate / publish`; the right diagram remains input → bounded phase (agent loop + artifact) → gate → output.
- **Visual meaning**: Separates open-ended reasoning, conditional branches, and repeatable execute/validate/publish steps.
- **Plain-language explanation**: Flexible work and hard guarantees have different jobs.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; continues 29 and adds the three responsibilities.

### 31 · 2026-08-11 7:16:49 PM

- **File**: `Screenshot 2026-08-11 at 7.16.49 PM.png`
- **Visible title**: **One Runtime, Three Workflows**.
- **Key excerpt**: `01 Question-blind data discovery`; `02 Task solver`; `03 Task learner`; `Same runtime; different skills, artifacts, and gates.`
- **Visual meaning**: One runtime supports discovery, solving, and learning through different skills, artifacts, and gates.
- **Plain-language explanation**: The runtime can be shared, but different tasks need different rules and outputs.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from responsibility separation to workflow separation.

### 32 · 2026-08-11 7:17:55 PM

- **File**: `Screenshot 2026-08-11 at 7.17.55 PM.png`
- **Visible title**: **Skills Development**.
- **Key excerpt**: `Iterative Refinement`: the Task Learner produces answers and iterates against a gold standard; `Skill Progression`: develop new emergent skills and keep tightening old capabilities; `Generalization Rule`: `always generalize, never overfit to a task result`; the right-side skill list includes aggregation-and-ties, answer-contracts, discovery-orientation, document-evidence, evidence-mapping, join-planning, learning-reflection, no-gold-review, operator-escalation, question-interpretation, structured-data-analysis, value-normalization, and video-context.
- **Visual meaning**: Skills improve through task learning, but a cross-task generalization rule is required.
- **Plain-language explanation**: Skill changes should learn a class of problems, not just solve one task.
- **Confidence / ambiguity**: High; the small skill list is readable, but individual spellings should follow the image.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from three workflows to the skill lifecycle.

### 33 · 2026-08-11 7:19:36 PM

- **File**: `Screenshot 2026-08-11 at 7.19.36 PM.png`
- **Visible title**: **Solver Loop**.
- **Key excerpt**: Reasoning trail `How the question becomes a program`: `Interpretation` (reading question) → `Contract` (the promise made) → `Evidence` (sources that feed it) → `Plan` (deterministic steps) → `Code` (reasoning as a program); the scratchpad shows execution_date `2026-08-10`, year `2026`, and `Which event bought the lowest-cost item?`.
- **Visual meaning**: Turns a question step by step into an executable program and leaves a reasoning trail.
- **Plain-language explanation**: State the question and output promise, then choose evidence, steps, and code.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from the skill lifecycle into a single-task solver loop.

### 34 · 2026-08-11 7:20:23 PM

- **File**: `Screenshot 2026-08-11 at 7.20.23 PM.png`
- **Visible title**: **Operator Interaction**.
- **Key excerpt**: `Iterative Feedback Cycle`: `1 Feedback → 2 Repair → 3 Revalidate → 4 Republish`; `REQUIRED`: force a human at every critical node; `AUTO`: act autonomously and ask only when materially blocked; `OFF`: solve fully automatically and independently.
- **Visual meaning**: Feedback does not publish directly; it is repaired, revalidated, and republished. Human involvement has three levels.
- **Plain-language explanation**: After feedback, repair, recheck, and republish; choose the intervention level by risk.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from the solver loop to operator interaction and the repair loop.

## Topic 4 — Cross-modal walkthrough, evidence chains, validation, and memory governance (35–45)

### 35 · 2026-08-11 7:21:26 PM

- **File**: `Screenshot 2026-08-11 at 7.21.26 PM.png`
- **Visible title / interface**: Purchases Discovery; the top says `agent flagged 2 findings`.
- **Key excerpt**: Three-source discount-pricing task: a 3-row CSV, a PNG discount memorandum, and 4-line procedural knowledge; the CSV supplies list prices, the image supplies two discounts, and the knowledge requires post-discount pricing with `include ties`; main risks are no discount for Beacon and dollar-string parsing; the diagram connects `Discount memorandum`, `Purchase transactions`, and `Operating Procedures`.
- **Visual meaning**: Establishes cross-modal relationships and a risk list before solving.
- **Plain-language explanation**: Identify each source’s role and ambiguities before calculating.
- **Confidence / ambiguity**: High; side-panel text is small.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from operator interaction to a concrete data-orientation walkthrough.

### 36 · 2026-08-11 7:21:51 PM

- **File**: `Screenshot 2026-08-11 at 7.21.51 PM.png`
- **Visible title / interface**: Purchases Discovery, with CSV `Purchase transactions` expanded.
- **Key excerpt**: `Key fields Event`, 3 rows; the table shows `Aurora $12`, `Beacon $9`, `Cedar $15`; button `Explore purchases.csv`.
- **Visual meaning**: Inspects source fields, row count, and raw values first.
- **Plain-language explanation**: Confirm what the data actually looks like before calculating.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; the relationship map in 35 moves into structured-table inspection.

### 37 · 2026-08-11 7:22:06 PM

- **File**: `Screenshot 2026-08-11 at 7.22.06 PM.png`
- **Visible title / interface**: `Attention` popup on the Discovery graph.
- **Key excerpt**: `Beacon has no approved discount in the memorandum`; its post-discount price therefore equals the CSV raw price `$9`, but whether “missing discount” means no discount or an incomplete memo materially affects correctness; source is `image/discount_memo.png`.
- **Visual meaning**: Promotes the semantic ambiguity of a missing value to an explicit finding.
- **Plain-language explanation**: A blank does not necessarily mean zero; confirm its meaning first.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from table inspection to semantic-ambiguity audit.

### 38 · 2026-08-11 7:22:21 PM

- **File**: `Screenshot 2026-08-11 at 7.22.21 PM.png`
- **Visible title / interface**: `Load-bearing` popup on the Discovery graph.
- **Key excerpt**: `Prices in the CSV are stored as dollar-formatted strings ($12, $9, $15) rather than raw numbers, requiring parsing before any arithmetic comparison`; source `csv/purchases.csv`.
- **Visual meaning**: Marks a type issue as a load-bearing finding for later computation.
- **Plain-language explanation**: Strip `$` and convert to numbers before comparing prices.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from missing-value semantics to data typing/normalization.

### 39 · 2026-08-11 7:22:27 PM

- **File**: `Screenshot 2026-08-11 at 7.22.27 PM.png`
- **Visible title / interface**: Thread `Which event bought the lowest-cost item?`.
- **Key excerpt**: The right side shows `Provenance artifacts grouped by phase`, including `context-profile.md`, `scratchpad.md`, `answer-contract.yaml`, `evidence-map.md`, `plan.md`, `solution.py`, `run-output.md`, `predicted.csv`, `validation.md`, `solution-review.md`, a review decision log, `artifacts.yaml`, `publish-report.md`, and `published.csv`.
- **Visual meaning**: Each phase leaves inspectable artifacts, with provenance grouped in the side panel.
- **Plain-language explanation**: The final answer is not the only record; evidence, plans, runs, and reviews remain available.
- **Confidence / ambiguity**: High; the bottom and some paths are cropped by the interface.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from finding issues to inspectable artifact/provenance.

### 40 · 2026-08-11 7:22:41 PM

- **File**: `Screenshot 2026-08-11 at 7.22.41 PM.png`
- **Visible title / interface**: Solve-stage reasoning trail (Interpretation → Contract → Evidence → Plan → Code).
- **Key excerpt**: Source Data table: `csv/purchases.csv` has 3 rows, Event/Price `Aurora $12`, `Beacon $9`, `Cedar $15`; `image/discount_memo.png` gives Aurora `$4/item` and Cedar `$7/item`, while Beacon is absent; the knowledge document remains below but is partly cropped.
- **Visual meaning**: Combines facts from each modality into a sourced fact table.
- **Plain-language explanation**: Keep list price, discount, and omission separate so later code has a basis.
- **Confidence / ambiguity**: High; the lower knowledge-document rows are cropped.
- **Speaker/topic transition clue**: speaker unable to confirm; provenance moves into evidence mapping.

### 41 · 2026-08-11 7:22:54 PM

- **File**: `Screenshot 2026-08-11 at 7.22.54 PM.png`
- **Visible title / interface**: Plan stage.
- **Key excerpt**: Step 1 loads the CSV and strips `$` to float; Step 2 applies image-approved discounts, defaults an event absent from the memo to discount 0, and computes `discounted_price = Price - discount`; Step 3 takes `min(discounted_price)`; Step 4 keeps all ties equal to the minimum under knowledge rule 2.
- **Visual meaning**: Type conversion → source-rule application → minimum → contract-defined tie handling.
- **Plain-language explanation**: Make values computable first, then define missing-discount and tie behavior.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; evidence mapping moves into a deterministic plan.

### 42 · 2026-08-11 7:23:05 PM

- **File**: `Screenshot 2026-08-11 at 7.23.05 PM.png`
- **Visible title / interface**: Run solution / Draft prediction.
- **Key excerpt**: `solution/cycle-001/predicted.csv` outputs Event values Aurora and Cedar; Validate prediction shows `run_ok:true`, `validation_ok:true`, `publishable:true`, an empty `failure_class`, and a `failure_note` saying the columns match the contract; Warnings `None`.
- **Visual meaning**: Code execution, result format, and publishability are displayed as separate fields.
- **Plain-language explanation**: Producing a result is not enough; format and contract must pass before publishing.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; plan moves into execution and the publishability gate.

### 43 · 2026-08-11 7:23:51 PM

- **File**: `Screenshot 2026-08-11 at 7.23.51 PM.png`
- **Visible title / interface**: Review solution.
- **Key excerpt**: `solution-review.md` Decision=`accept`; Human Gate `final_prediction: status=passed`; the task is an unambiguous singleton extremum with an explicit tie policy; two audits confirm grounding for literal cues (lowest-cost, price-after-discount, include ties), with Event sourced from `purchases.csv`; implementation has no gold paths/network/shell; OCR discounts are Aurora `$4`, Cedar `$7`, and Beacon absent → `$0`.
- **Visual meaning**: Independent semantic and implementation reviews jointly accept the result.
- **Plain-language explanation**: Check both whether the question was interpreted correctly and whether the code avoided forbidden paths.
- **Confidence / ambiguity**: High; lower calculation details are small/partly cropped.
- **Speaker/topic transition clue**: speaker unable to confirm; after execution passes, enters dual semantic and implementation review.

### 44 · 2026-08-11 7:24:02 PM

- **File**: `Screenshot 2026-08-11 at 7.24.02 PM.png`
- **Visible title**: **Lessons Learned**.
- **Key excerpt**: `01 Distill · Explore · Measure`: distill compiled knowledge, explore in parallel, and measure end to end; `02 Proven Engineering Foundations`: TDD/SOA/modularity and protected boundaries; `03 Orient Broadly · Search Just in Time`: orient at a high level, then retrieve/parse/normalize as needed; `04 Agents Interpret · Code Integrates`: agents interpret cross-modal meaning, deterministic code connects accepted evidence, and each phase boundary iterates validation; `05 Artifacts as Learning Substrate`: runtime artifacts close the review/verification/feedback loop, building bounded persistent memory/reusable skills, with humans as high-level guides.
- **Visual meaning**: Compresses experience into five practice groups, emphasizing flexible exploration/interpretation and deterministic evidence connection/validation/publishing.
- **Plain-language explanation**: Let agents understand and explore; let code connect evidence and recheck it, leaving a reviewable record at every step.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; summarizes the walkthrough as lessons learned.

### 45 · 2026-08-11 7:25:32 PM

- **File**: `Screenshot 2026-08-11 at 7.25.32 PM.png`
- **Visible title**: **From Feedback to Durable Memory**.
- **Key excerpt**: Operator guidance first asks `Should this affect future answers?`, then a person chooses the scope: `Repo memory` (broadest, shared across all workspaces, EDIT), `Workspace memory` (one corpus, EDIT), or `Question memory` (one thread and follow-ups, PIN); each task compiles `effective-memory.md` in repo→workspace→question order (broadest first · local last); memory guides interpretation only and never becomes task evidence; task data still grounds the answer, and deterministic validation/publishing gates still apply; principle: `Persist deliberately`.
- **Visual meaning**: Feedback is scope-selected, then compiled into guidance for the next run; evidence and memory stay separate.
- **Plain-language explanation**: Persist only human-approved feedback, and never let memory impersonate current-task evidence.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; closes the walkthrough with memory governance and moves to real-world evidence/RWE.

## Topic 5 — Real-world evidence, validation loops, and schema-first rebuild (46–63)

### 46 · 2026-08-11 7:26:34 PM

- **File**: `Screenshot 2026-08-11 at 7.26.34 PM.png`
- **Visible title**: **Bounded Agents, Deterministic Answers**.
- **Key excerpt**: `Phase 01 Agents interpret uncertainty`; `Phase 02 Artifacts preserve their decisions`; `Phase 03 Deterministic gates control what gets published`.
- **Visual meaning**: Three horizontal phase cards, with a QR code at the bottom.
- **Plain-language explanation**: The model can handle uncertainty, but must leave decision records; deterministic gates decide what can be published.
- **Confidence / ambiguity**: High; bottom URL/page number is cropped, and QR contents are unable to confirm.
- **Speaker/topic transition clue**: speaker unable to confirm; manifesto slide for the RWE/controlled-agent segment.

### 47 · 2026-08-11 7:29:50 PM

- **File**: `Screenshot 2026-08-11 at 7.29.50 PM.png`
- **Visible title**: **What is real-world evidence?**
- **Key excerpt**: Defines it as studying what happens to patients after a drug using collected records; flow `01 A DRUG → 02 A QUESTION → 03 FIND THE PATIENTS → 04 LOOK FORWARD one year → 05 COUNT`; example `FOLLOWED 1,745 → HAD IT 333 → RATE 19%`.
- **Visual meaning**: Five-step cohort/incidence flow and worked example.
- **Plain-language explanation**: Start with people taking the drug, follow them for a year under the rules, then count events and the total.
- **Confidence / ambiguity**: High; the bottom actor description is small.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from the governance manifesto to the basic RWE definition.

### 48 · 2026-08-11 7:30:42 PM

- **File**: `Screenshot 2026-08-11 at 7.30.42 PM.png`
- **Visible title**: **Step three is easy in a trial. Here it is the whole problem.**
- **Key excerpt**: Trial data are arranged for the question and the eligible group is decided before collection; real records capture everything about everyone; qualifying people must be observable at drug start, have enough follow-up, and be disease-free at start; `selecting qualifying group is the study`.
- **Visual meaning**: Two-row Trial Data vs Real Records comparison emphasizing post-hoc cohort selection.
- **Plain-language explanation**: Trial participants are fixed; real records must first be filtered to comparable, followable people, and that filter shapes the result.
- **Confidence / ambiguity**: High; footer references/numbers are not central, and the main point is clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from the RWE definition to cohort eligibility/selection bias.

### 49 · 2026-08-11 7:31:09 PM

- **File**: `Screenshot 2026-08-11 at 7.31.09 PM.png`
- **Visible title**: **The failure mode**.
- **Key excerpt**: The worst output is not an error but a `plausible wrong number`; `MAP` maps plain words to medical codes (possibly the wrong code); `GROUP` should include only new users but mixes in old users; `WHO COUNTS` does not check observability at start, sufficient follow-up, or prior disease; every step can fail silently, leaving a confident number from “correct SQL.”
- **Visual meaning**: Four-part silent-failure chain MAP → GROUP → WHO COUNTS → COMPUTE.
- **Plain-language explanation**: SQL without an error does not prove the study definition is correct.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from cohort selection to silent semantic failure.

### 50 · 2026-08-11 7:33:27 PM

- **File**: `Screenshot 2026-08-11 at 7.33.27 PM.png`
- **Visible title**: **Run 1: the three paths agree, and the check still says no.**
- **Key excerpt**: `THREE PATHS AGREE 0.1925 → REJECTED`; `44 with no data before they started`, `99 not followed for a full year`; self-fix plan `0.1908`; `The math was fine. The study was not.`
- **Visual meaning**: Three calculation paths agree, but the eligibility gate rejects the result; self-fix then recomputes it.
- **Plain-language explanation**: Agreement across SQL, Python, and a ledger still does not validate study design; eligibility conditions must be fixed first.
- **Confidence / ambiguity**: High; numbers are clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from failure mode into the validation gate and self-correction.

### 51 · 2026-08-11 7:34:06 PM

- **File**: `Screenshot 2026-08-11 at 7.34.06 PM.png`
- **Visible interface**: Astro UI, question `What is the 1-year incidence of GI bleed…`.
- **Key excerpt**: Eunomia GiBleed synthetic, `2,694 persons`; `37` tables, vocabulary OK, incidence-ready yes; `osteoarthritis → Osteoarthritis`, `celecoxib → celecoxib`; `GI bleed → ∅`, `not found in vocabulary`; status `Data exploration in progress`.
- **Visual meaning**: Dataset/table list on the left, timeline in the middle, study board on the right; schema and concept mapping are checked first.
- **Plain-language explanation**: If a natural-language outcome cannot map to the vocabulary, cohort calculation cannot pretend to continue.
- **Confidence / ambiguity**: High; the bottom progress row is faint.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from the RWE concept to actual schema inspection/concept grounding.

### 52 · 2026-08-11 7:35:08 PM

- **File**: `Screenshot 2026-08-11 at 7.35.08 PM.png`
- **Visible interface**: Astro Study board / `Study design`.
- **Key excerpt**: `Incidence`; population `osteoarthritis`; exposure `celecoxib`; outcome `gastrointestinal hemorrhage`; time at risk `365 days`; mapping terms/IDs (osteoarthritis `80180`, celecoxib `1118084`, GI bleed/hemorrhage `192671`); execution checklist `0/7`; bottom button `Approve and run`.
- **Visual meaning**: Fixes the natural-language question into an executable study design, mapping table, and seven-item checklist; it runs only after approval.
- **Plain-language explanation**: Write the study contract first, then obtain human approval to execute.
- **Confidence / ambiguity**: High; small text in the left UI remains readable.
- **Speaker/topic transition clue**: speaker unable to confirm; schema/concept checking enters the study spec and human approval.

### 53 · 2026-08-11 7:36:32 PM

- **File**: `Screenshot 2026-08-11 at 7.36.32 PM.png`
- **Visible interface**: Astro live verification.
- **Key excerpt**: `run_verification ACCEPTED no, FIXABLE yes, CONFIDENCE 0`; `44 index date outside observation_period`; `99 lack complete 365-day follow-up`; `revise_spec` applies `require_index_in_obs / require_full_followup / exclude_prior_outcome`; recomputed denominator `1,745`, numerator `333`, incidence `0.1908`; A_sql_setbased/B_python_interval/C_eligibility_ledger all return `0.1908`; recheck yields `ACCEPTED yes, FIXABLE no, CONFIDENCE 1`.
- **Visual meaning**: Finds eligibility issues, tightens the spec, recomputes, cross-checks three paths, and accepts only at the end.
- **Plain-language explanation**: A failed check is not immediate discard; if fixable, change study conditions, recompute, and validate again.
- **Confidence / ambiguity**: High; playback controls cover a few edge checklist items, but core numbers are clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from the study spec to the eligibility ledger and consensus verification.

### 54 · 2026-08-11 7:38:24 PM

- **File**: `Screenshot 2026-08-11 at 7.38.24 PM.png`
- **Visible title**: **Run 2: same loop, same gate. Different path.**
- **Key excerpt**: `Guidance recalled as advice, never as a value`; helper agent never called; `15 patients, 8 events: verified ≠ safe to read`; Run 1 grounding failed → helper called, Run 2 terms matched → helper never called; Run 1 rejected → revised → recomputed, Run 2 passed first try; reviewer concern is too small to trust; the system did not change, and findings determined the path.
- **Visual meaning**: Run 1 and Run 2 take different branches but share one loop/gate.
- **Plain-language explanation**: The same system can choose different tools and repairs from the evidence; even a passing check should flag small-sample caution.
- **Confidence / ambiguity**: High; bottom text is readable.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from one validation loop to adaptive paths and reviewer caution.

### 55 · 2026-08-11 7:40:47 PM

- **File**: `Screenshot 2026-08-11 at 7.40.47 PM.png`
- **Visible title / interface**: Astro synthetic OMOP, question `What is the 90-day incidence of acute bronchitis in patients initiating acetaminophen?`
- **Key excerpt**: Numerics reviewer `CONCERN 0.5333 (8/15)` (small cohort); Study-Design reviewer `CONCERN` (prior outcomes not excluded, 90-day full follow-up not guaranteed); Data-Quality reviewer `PASS`, with three methods agreeing; Magnitude `53.33%`; Bias `0.0%`; Consensus `3/3`; about `533/1,000`, `8 events/15 eligible`; eligibility adjustment `0.0% change`; checklist `6/6`.
- **Visual meaning**: Multiple reviewer cards, multi-analyst synthesis, and a cohort-age histogram.
- **Plain-language explanation**: Agreement and data quality do not hide small samples or design bias.
- **Confidence / ambiguity**: High; the lower histogram is cropped, but the numeric conclusions are clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from the repair loop to multi-reviewer synthesis and sample-size warnings.

### 56 · 2026-08-11 7:48:30 PM

- **File**: `Screenshot 2026-08-11 at 7.48.30 PM.png`
- **Visible title**: **The rebuild made schema the control plane**.
- **Key excerpt**: Each stage consumes an explicit contract and produces a narrower, more reliable representation: `Ingest` maps files/modalities → `Profile` schema + samples + semantics → `Route` chooses canonical evidence → `Execute` uses bounded tools (SQL/Python/Docs/video) → `Validate` produces schema-valid `prediction.csv`; bottom line: `typed map · bounded tools · retries · atomic writes · logs`.
- **Visual meaning**: A five-stage pipeline puts schema in control from input through publishing.
- **Plain-language explanation**: Organize typed, semantic inputs first, choose evidence and tools, then publish only a schema-valid CSV.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from the RWE walkthrough to the rebuild’s schema-first summary.

### 57 · 2026-08-11 7:49:21 PM

- **File**: `Screenshot 2026-08-11 at 7.49.21 PM.png`
- **Visible title**: **A schema-aware index turns files into a compact data map**.
- **Key excerpt**: `01 Source inventory`: map each logical source to an SQL/CSV/JSON/document/video location; `02 Structural schema`: column names, row count, 3 sample rows, 60-character cell clips; `03 Semantic schema`: ≤20k chars anchored to business terms/units/entities/time windows; `04 Modality cues`: documents are record sources, while video rules are transcribed/cached separately; `LLM reasons over a typed workspace map—not filenames alone.`
- **Visual meaning**: Four steps turn files into a compact map with structure, semantics, and modality cues.
- **Plain-language explanation**: The index does more than list filenames; it tells the agent what is inside and how to use it.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; the five-stage overview moves into index/data-map details.

### 58 · 2026-08-11 7:50:10 PM

- **File**: `Screenshot 2026-08-11 at 7.50.10 PM.png`
- **Visible title**: **Schema determines what each modality contributes**.
- **Key excerpt**: Briefing video → thresholds, field definitions, scope, completeness rules; document records → entity mappings, corrected IDs, scattered attributes; `Route by role`: extract rules/mappings from unstructured evidence, then compute exact values from the canonical structured source.
- **Visual meaning**: Video/documents and structured sources have different roles; unstructured material does not directly produce final exact values.
- **Plain-language explanation**: Video and documents supply rules, mappings, and definitions; compute exact values from canonical tables.
- **Confidence / ambiguity**: High; middle example text and Chinese details are not fully legible, but the main point is clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from the index to modality routing/source authority.

### 59 · 2026-08-11 7:51:02 PM

- **File**: `Screenshot 2026-08-11 at 7.51.02 PM.png`
- **Visible title**: **Each Agent attempt progressively narrows the answer schema**.
- **Key excerpt**: `Infer the contract` (requested attributes, row granularity, canonical sources, schema-values) → `Act through tools` (7 callable ops, schema-first previews, SQL/Python/docs/video, 8k tool-result cap) → `Validate & repair` (schema-shaped CSV, reject empty, fresh-context reviewer, stop after two repairs); bottom budget `≤24 turns / 7 tools / ≤2 repairs`.
- **Visual meaning**: Each attempt infers the output contract, makes bounded calls, then validates/repairs and stops.
- **Plain-language explanation**: Each round narrows the answer scope under a hard budget.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; modality routing moves into the agent loop/budget.

### 60 · 2026-08-11 7:52:18 PM

- **File**: `Screenshot 2026-08-11 at 7.52.18 PM.png`
- **Visible title**: **Tool boundaries preserve schema and source integrity**.
- **Key excerpt**: SQL: read-only database URI, 40-row schema/value preview, 90s query watchdog, 180s schema-exact export; Python+docs: private temp workdir, context via symlinks, 4.5k-character document chunks, 6 parallel extractors; Video: ≤100 MB clips, cached first transcription, captured captions/rules, targeted re-watch.
- **Visual meaning**: Three columns specify minimum permissions and resource caps for SQL, Python/docs, and video.
- **Plain-language explanation**: Give each material only the needed capability, with sandboxing, timeouts, and caching.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from agent budget to tool boundaries and permissions.

### 61 · 2026-08-11 7:53:06 PM

- **File**: `Screenshot 2026-08-11 at 7.53.06 PM.png`
- **Visible title**: **Schema-aware validation protects the CSV at three levels**.
- **Key excerpt**: `01 Before submission`: the contract fixes columns, row granularity, null/duplicate behavior, units, and raw-value fidelity; `02 After submission`: parse CSV, reject empties, check units/shape, use a fresh-context judge, ≤2 repairs; `03 Across attempts`: group by normalized column signature, and if all differ, use a pairwise judge twice with swapped order; `schema is semantics—not post-processing`.
- **Visual meaning**: Schema validation operates before submission, after submission, and across attempts.
- **Plain-language explanation**: Schema is not a final formatting patch; it defines what the answer means from the beginning.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from tool boundaries to output contract/validation.

### 62 · 2026-08-11 7:53:58 PM

- **File**: `Screenshot 2026-08-11 at 7.53.58 PM.png`
- **Visible title**: **A schema-valid answer still has to survive the wall clock**.
- **Key excerpt**: `8 parallel worker processes`; when budget allows, `3× attempts` (add only if the first round leaves 420s); `0 missing output files` (fallback `prediction.csv` before the first model call); `1 atomic final write` (SQL replaces `.tmp`; Python copies after pandas parses the CSV).
- **Visual meaning**: Four large numbers make concurrency, retry budget, fallback files, and atomic writes runtime metrics.
- **Plain-language explanation**: Correct content is not enough; manage timeouts, partial files, and missing outputs too.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from schema validation to wall-clock/runtime delivery.

### 63 · 2026-08-11 7:55:06 PM

- **File**: `Screenshot 2026-08-11 at 7.55.06 PM.png`
- **Visible title**: **The rebuild raised the ceiling—while variance remained**.
- **Key excerpt**: Line chart Run 6 `0.6389`, Run 7 `0.6125`, Run 8 `0.6753`, Run 9 `0.5979`, Run 10 `0.6208`; dashed Final B-board `0.6217`; cards show best local run `0.6753` / final B-board `0.6217`; `schema awareness raised ceiling; controls made result deliverable`; model variance still needs reduction after schema/execution/delivery controls.
- **Visual meaning**: The rebuild raises the best score, but run-to-run variance remains visible.
- **Plain-language explanation**: Engineering controls make results deliverable; they do not prove model performance is stable.
- **Confidence / ambiguity**: High; chart and numbers are clear.
- **Speaker/topic transition clue**: speaker unable to confirm; closes the rebuild with variance and deliverability, then cuts to another team’s cover.

## Topic 6 — Data Agent Studio: interaction control, routing, cost, and evaluation limits (64–73)

### 64 · 2026-08-11 7:57:40 PM

- **File**: `Screenshot 2026-08-11 at 7.57.40 PM.png`
- **Visible title**: **Data Agent Studio — A Transparent and Controllable Chatbot for Data Analysis Agents**.
- **Key excerpt**: `KDD Cup 2026 Data Agents Creative Track`; `UITNLP · University of Information Technology, VNU-HCM`; `Team ID 1401`; `Creative Track, Top 3`; Presenter `Ha Huu Phat`; members `Nguyen Minh Triet / Nguyen Xuan Phuc / Ha Huu Phat / Dang Van Thin`.
- **Visual meaning**: Cover for another team’s product/demo, emphasizing a transparent, controllable data-analysis chatbot.
- **Plain-language explanation**: Context for an external team and work, not evidence of a specific method.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: presenter/team are explicit on screen; cuts from the prior team’s rebuild result to another KDD Creative Track work.

### 65 · 2026-08-11 7:59:26 PM

- **File**: `Screenshot 2026-08-11 at 7.59.26 PM.png`
- **Visible title**: **Output-Only Agent Execution Limits Observability and Intervention**.
- **Key excerpt**: `Limited Observability`: intermediate tool calls, observations, errors, and retries stay inside the execution loop; `No Intervention Point`: actions cannot be inspected/modified before execution; the consequence is diagnosis only after final output; diagram `Task → Agent Execution (hidden state) → Final Output`.
- **Visual meaning**: A batch-style output-only agent hides execution state.
- **Plain-language explanation**: Returning only the final file loses the chance to pause and correct midway.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; after the cover, defines the system-level gap in output-only execution.

### 66 · 2026-08-11 8:00:11 PM

- **File**: `Screenshot 2026-08-11 at 8.00.11 PM.png`
- **Visible title**: **Existing Approaches Leave Two System-Level Gaps**.
- **Key excerpt**: `Single-Call Prompting`: no iterative data interaction, limited recovery; `Tool-Calling Agent`: fixed agent loop, limited adaptation; `KDD Starter Kit`: ReAct + tool registry, one strategy across tasks, no in-loop user intervention; remaining gaps: `Adaptive Strategy Selection` (orchestration by task difficulty) and `Step-Level Intervention` (pause the loop for human control, not CLI-only).
- **Visual meaning**: Compares three existing approaches and proposes task-based strategy selection plus in-loop human intervention.
- **Plain-language explanation**: Existing approaches either do not iterate/recover or use a fixed strategy with no mid-loop human control.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from observability gaps to existing approaches and gap analysis.

### 67 · 2026-08-11 8:02:15 PM

- **File**: `Screenshot 2026-08-11 at 8.02.15 PM.png`
- **Visible title**: **Our Solution: An Interactive Data-Agent Execution Framework**.
- **Key excerpt**: `01 Multi-Step Orchestration` (iterative reasoning/tool interaction); `02 Adaptive Strategy Selection` (choose ReAct/multi-agent/dynamic retrieval by task characteristics); `03 Observable And Controllable Execution` (expose intermediate state and support step-level intervention); `UNIFIED EXECUTION ENGINE`: interactive interface and benchmark evaluation share one orchestration pipeline.
- **Visual meaning**: Three capability cards, with the bottom emphasizing one execution engine for interactive UI and benchmark evaluation.
- **Plain-language explanation**: The core is multi-step execution, difficulty-aware routing, visible/controllable progress, and one flow for tests and interaction.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from gaps to this team’s solution-framework overview.

### 68 · 2026-08-11 8:03:03 PM

- **File**: `Screenshot 2026-08-11 at 8.03.03 PM.png`
- **Visible title**: **System Overview: Interaction, Orchestration, And Execution** (left edge of title slightly cropped).
- **Key excerpt**: `INTERFACE`: Chat UI, Live execution trace, User input; `GATEWAY`: Session management, Event streaming, `run / proceed / edit / stop`; `ORCHESTRATION`: Runner, Strategy router, Agent execution, Self-correction, Interaction controller; lower `TOOLS & ENDPOINTS`: SQL, Python, Document retrieval, Models.
- **Visual meaning**: UI events pass through the Gateway to orchestration, then tools call lower-level capabilities.
- **Plain-language explanation**: The interface emits events, the Gateway manages sessions and streams, and orchestration selects strategy, executes, self-corrects, and pauses.
- **Confidence / ambiguity**: High; the left edge of the title is cropped, but hierarchy text is clear.
- **Speaker/topic transition clue**: speaker unable to confirm; framework capabilities become a system-layer diagram.

### 69 · 2026-08-11 8:03:51 PM

- **File**: `Screenshot 2026-08-11 at 8.03.51 PM.png`
- **Visible title**: **Agent Workflow: Difficulty-Aware Routing With Step-Level Recovery**.
- **Key excerpt**: `Task → Hybrid-B Router → ReAct / Planner–Analyst / Dynamic Retrieval → Agent Execution → Self-Correction`; Easy/Medium → ReAct; Hard → choose from task signals; Extreme → Dynamic Retrieval; error → targeted recovery hint; stagnation → redirect; budget exhausted → best available answer; strategy selection happens before execution, while recovery is shared across strategies.
- **Visual meaning**: Routes different strategies by difficulty and uses one recovery rule set after execution.
- **Plain-language explanation**: Judge difficulty first, then choose a route; when stuck, give a targeted hint, redirect, and still return the best available answer when budget ends.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from system layers to routing and recovery behavior.

### 70 · 2026-08-11 8:05:31 PM

- **File**: `Screenshot 2026-08-11 at 8.05.31 PM.png`
- **Visible title**: **Two Interaction Modes Over A Shared Controller**.
- **Key excerpt**: `Autopilot`: keep running, pausing only for calls that need approval; `Co-pilot`: pause before every proposed tool call so the user can approve/edit/reject/guide; the shared controller’s pause/resume is independent of the underlying strategy; right diagram labels `Co-pilot — AWAITING_USER before tool execution`.
- **Correction note**: `screenshot-supported correction`: the image clearly distinguishes `Autopilot` and `Co-pilot`; do not carry Whisper’s misrecognition of the second mode as `Autopilot`.
- **Visual meaning**: Two interaction modes share one controller and one set of approval buttons.
- **Plain-language explanation**: Let the agent run itself, or have a person check every tool call first.
- **Confidence / ambiguity**: High; right-side code is small, but main labels and buttons are clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from routing/recovery to human-in-the-loop modes.

### 71 · 2026-08-11 8:06:11 PM

- **File**: `Screenshot 2026-08-11 at 8.06.11 PM.png`
- **Visible title**: **Interactive Workflows Across Structured And Unstructured Data**.
- **Key excerpt**: `01 Cross-Source Data Exploration`: schema relationships/join paths across databases; `02 Document Knowledge Extraction`: PDF entity-relation graph; `03 Human-In-The-Loop Data Correction`: review data-quality changes before applying them; `04 Traceable Analytical Output`: link the final result to execution steps; bottom emphasizes one orchestration/tool interface/interaction controller.
- **Visual meaning**: Four workflow screenshot tiles cover databases, PDFs, human data correction, and traceable output.
- **Plain-language explanation**: One orchestration can span structured and unstructured material; review proposed changes and keep the final result traceable.
- **Confidence / ambiguity**: High; thumbnail details are blurry, but titles and explanations are clear.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from interaction modes to cross-modal workflow examples.

### 72 · 2026-08-11 8:08:47 PM

- **File**: `Screenshot 2026-08-11 at 8.08.47 PM.png`
- **Visible title**: **Practical Considerations: Cost, Latency, Safety, And Deployment**.
- **Key excerpt**: Adaptive routing/step budgets limit compute; permission checks protect ground-truth files, and writes/side effects need explicit approval; a single-container setup is for evaluation, while production should split into independently scalable services; average latency table Stronger vs Cheaper: Easy `20.5s / 53.5s`, Medium `34.7s / 46.8s`, Hard `39.1s / 94.8s`, Extreme (`n=1`) `28.3s / 35.7s`; the cheaper backbone is estimated to cost less but is generally slower.
- **Visual meaning**: Three engineering cautions and latency comparisons by difficulty/model.
- **Plain-language explanation**: Use difficulty routing and step budgets to control cost; require approval for sensitive writes; do not treat an evaluation container as production deployment.
- **Confidence / ambiguity**: High; the Extreme `n=1` sample limitation is explicit.
- **Speaker/topic transition clue**: speaker unable to confirm; moves from workflow capabilities to cost, latency, safety, and deployment realities.

### 73 · 2026-08-11 8:09:39 PM

- **File**: `Screenshot 2026-08-11 at 8.09.39 PM.png`
- **Visible title**: **Current Limitations And Evaluation Scope**.
- **Key excerpt**: `Limited External Validity`: only the Phase-1 benchmark split, with no extrapolation test; `Difficulty And Modality Are Confounded`: the current split cannot analyze them independently; `Stability Not Characterized System-Wide`: repeated evaluation covers only one task and run-to-run variance is not sufficiently quantified; next steps: external unseen datasets, controlled difficulty/modality splits, repeated-run stability analysis.
- **Visual meaning**: Three limitation cards plus a next-step evaluation list.
- **Plain-language explanation**: Current scores do not establish cross-dataset, cross-difficulty/modality, or long-term stability; external blind tests, decoupled splits, and repeated runs are needed.
- **Confidence / ambiguity**: High; clear.
- **Speaker/topic transition clue**: speaker unable to confirm; closes the screenshot sequence with limitations and evaluation scope.

## Third-route Mac ASR correction log (screenshot evidence only)

- **Source and limits**: the `Mac Voice Memos ASR candidate` has no timestamps; it can propose candidates but cannot override Whisper or turn unseen screenshot content into a screenshot claim. Its raw text is not included because of privacy and source availability.
- **screenshot-supported correction**:
  - **02**: the image shows `SQL generation`, `DuckDB`, `Packet-size keyframes`, and `word-level timestamps`.
  - **04**: the image shows `record_universe`; Mac ASR’s `recorded universe` is not used as the visible wording.
  - **05**: the image shows `NV DATA EXPLORER · V15` and `Qwen3.5-35B-A3B`; this is the model name on the NV slide and cannot determine the first speaker’s Qwen3.5 suffix.
  - **64**: the image shows `Data Agent Studio`, `UITNLP · VNU-HCM`, Team ID `1401`, `Ha Huu Phat`, and `Creative Track Top 3`.
  - **70**: the image clearly distinguishes `Autopilot` and `Co-pilot`, and shows `AWAITING_USER`; the second mode must not inherit Whisper’s `Autopilot` misrecognition.
- **direct ASR agreement (does not add screenshot content)**: Whisper and Mac ASR both support `Docker`, `CER/WER`, `HTML-like layout`, Team 1418 ranking/Merit, Team 1688 fifth place, and Professor Tang closing. In this index these remain audio-only/audio evidence, not visible screenshot wording.
- **unresolved**: first-talk final score `0.65` vs `0.69`; Data Agent Studio per-task cost `25c` vs `35c`; and the first talk’s `Qwen3.5` suffix. Existing screenshots cannot independently resolve these conflicts, so no value is selected silently.

## High-value observations directly supported by screenshots (not adoption decisions)

The following observations compress the per-image evidence above for later requirements-first review. Each still needs item-by-item comparison with the two real-scenario success criteria, KDD work evidence, and legacy SMA; screenshots alone do not decide adopt/adapt/reject.

1. **Fix problem semantics and the output contract first.** Screenshots repeatedly place schema, row grain, units, allowed columns, and tie/null behavior before execution (06, 17, 41, 51–53, 57–61). A success criterion should at least check what is being computed, what each row represents, and which values are authoritative sources.
2. **“SQL did not error” is not a correctness criterion.** The RWE example shows that mapping, enrollment, observability at start, and follow-up length can fail silently (47–50); three calculation paths can agree and still be rejected by a study-design gate (50, 53).
3. **Route evidence by role instead of letting every modality produce numbers.** Video/documents provide rules, definitions, and mappings; exact values return to the canonical structured source (08, 51, 58). For post-experiment “why miss” and SEV “possibly related change,” this points to source provenance without prescribing an implementation.
4. **Make long documents and video verifiable intermediate representations first.** Prose helpers, doc-readers, caption-aligned frames/transcripts, and schema-aware indexes compress long material into tables, time-aligned segments, or typed maps (04, 07–08, 22–23, 49, 57). The key is not “summary,” but the ability to return to source evidence and check coverage.
5. **Separating open reasoning from deterministic gates is a recurring success candidate.** Bounded phases, phase gates, inspectable artifacts, deterministic execute/validate/publish, and a fresh-context reviewer recur in the material (12, 15, 29–30, 42–46, 59–61). The ablation has positive numbers, but its footnote says not to attribute all end-to-end gain to phase gating (18).
6. **Human intervention should control risk and steps, not be one final switch.** The material shows REQUIRED/AUTO/OFF, feedback→repair→revalidate→republish, Co-pilot pauses before tool calls, and step-level intervention (34, 45, 65–71). Later work should define human-needed points from the two scenarios’ risks rather than copy a UI.
7. **Retry/ensemble value depends on coverage, budget, and dispute handling; simple majority is not automatically useful.** One set proposes coverage-first, extra attempts for contested tasks, and column/name preservation (10); another reports no reliable end-to-end gain from 2/3 executor voting (25). Together they imply measuring when to retry, what a retry repairs, and when to stop—not merely adding calls.
8. **Runtime reliability is itself success evidence.** Atomic writes, fallback outputs, timeouts, permissions, sandboxing, concurrency, and logs recur (09, 42, 53, 60, 62, 72). An agent explaining why or finding a change must leave usable intermediate results, failure classes, and recovery records for the conclusion to be reviewable.
9. **Memory must stay separate from current-task evidence.** Feedback may persist as scoped guidance, but the material states that memory guides interpretation only and cannot become task evidence (45). This is a boundary for later design evaluation, not a reason to copy a memory layer.
10. **Evaluation claims need explicit external-validity and variance bounds.** The workshop itself records local-run variance, confounded variables, insufficient repeated evaluation on one task, and unmeasured external validity (18, 26–27, 55, 63, 73). Later adoption can rely only on repeated runs, external samples, and a failure taxonomy for the corresponding real scenarios.

## Requirements-first cross-reference (index only; not a design)

- **Need A: post-experiment** — explain why the metric missed, tie it to production code, and say what to change. Revisit evidence from interpretation/contract/evidence/provenance/validation/intervention in 33, 39–44, 49–53, 56–61, and 65–71.
- **Need B: SEV** — after a metric drop, find possibly related production-code changes. Revisit evidence on acquisition, time/scope constraints, artifacts/logs, recovery, and runtime boundaries in 11, 19, 27, 34, 46, 59–63, and 65–72.
- **Candidate success criteria**: a sourced conclusion; clear separation of observation, hypothesis, and verified fact; reproducible calculations/checks; explicit uncertainty and failure classes; a readable artifact delivered within budget, permissions, and timeouts; step-level pause/approval when needed.
- **Candidate practices (names only)**: typed workspace map, modality-by-role routing, explicit answer/analysis contract, bounded reasoning with deterministic gates, independent review, repair + revalidate, artifact/provenance trail, step-level intervention, atomic delivery, repeated-run stability analysis.
- **Adopt/adapt/reject**: This index makes no decision. For each candidate, ask whether it directly serves Need A/B, what evidence strength supports it, and how to turn it into a greenfield design. Reject practices that do not fit; do not retain them merely because they came from the workshop, KDD, or legacy SMA.
