# KDD Data-Agent Workshop: Audio and Screenshot Alignment

Date: 2026-08-11 (America/Los_Angeles)  
Scope: two user-provided recordings and 73 same-day workshop screenshots. Research only; no agent implementation changes. Raw media and ASR outputs are not included because of size, privacy, and source availability.

## Evidence Boundaries

- The recordings are the complete meeting timeline. `workshop` covers `00:00:00–02:13:17.099`; `intro` covers `00:00:00–00:05:48.331`.
- Screenshots are sparse slide samples, not a complete deck. Audio without a matching screenshot remains included and is labeled **audio-only**.
- This is a faithful English summary, not a verbatim transcript. Unclear terms, names, and numbers are marked **unconfirmed**.
- “Directly heard (audio + ASR)” means locally transcribed content located on the audio timeline; recognition errors remain possible.
- “Screenshot support” means visible slide evidence. It is not treated as spoken content. It corrects ASR only when a term, name, number, or topic clearly matches contemporaneous audio.
- “Inference” is based only on temporal proximity or topic continuity and is never presented as fact.

## Evidence Legend

| Label | Meaning |
|---|---|
| Directly heard (audio + ASR) | Supported by the local Whisper transcript for that interval; the summary does not expand unrecognized content. |
| Screenshot support | Supported by direct visual review in `screenshot-index.md`. |
| Inference | A weak conclusion based only on timing or topic continuity. |
| audio-only | No screenshot aligns with this interval, or the screenshot cannot correct its content. This is not negative evidence. |

A third ASR candidate is the `Mac Voice Memos ASR candidate` source label. It has no timestamps and systematically mishears proper terms as `Queen`, `dark DB`, `circle`, `recorded universe`, and `WEI`. It only proposes candidates; it neither resets the clock nor overrides Whisper. Corrections use only `direct ASR agreement`, `screenshot-supported correction`, or `unresolved`. The raw ASR is not included because of privacy and source availability.

## Audio Sources, Integrity, and Transcription

| Audio | Stable source label | SHA-256 | Key `ffprobe` metadata |
|---|---|---|---|
| intro | `Workshop intro recording` (raw media not included) | `2adf77325cec0f5a78ccc784794c2744bdb7f1a0ff34aff2e36696075332a9a2` | AAC LC; 48 kHz; mono; `348.330667 s`; `creation_time=2026-08-12T00:50:45Z` |
| workshop | `Workshop main recording` (raw media not included) | `24b5fd98fb9dc426039ea3eac3cc18ce8ba9dbe7074db4ba0e3b6c8ac7718929` | AAC LC; 48 kHz; mono; `7997.098667 s`; `creation_time=2026-08-12T01:02:14Z` |

- Transcription used `whisper-cli`; input was converted to 16 kHz mono WAV. WAV, model, and JSON/VTT/TXT outputs are local review material and are not included because of size, privacy, and source availability.
- Model: `ggml-large-v3-turbo-q5_0.bin`; official URL: `https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo-q5_0.bin`; downloaded SHA-256: `394221709cd5ad1f40c46e6031ca61bce88931e6e088c188294c6d5a55ffa7e2`.
- Smoke test: `intro` was detected as English with probability `0.997755`; it was intelligible and matched the KDD Cup opening. The same model was used for final transcription.
- Runtime constraint: Metal initialization once failed while allocating 7.33 MiB. Later runs used CPU/BLAS with the same model and no downgrade.
- Raw ASR files: `intro.{txt,vtt,json}` and `workshop/chunk-00..08.{txt,vtt,json}`. These are local review inputs, not repository deliverables, and are not included because of size, privacy, and source availability.
- The main task verified the assets, SHA values, `ffprobe` output, and coverage against local originals. The independent Fable review packet did not re-verify those originals; that limits its review scope but does not imply the assets are absent.

## Time Baseline and Screenshot Index

- Screenshot index: [screenshot-index.md](screenshot-index.md). All 73 workshop screenshot basenames were independently verified.
- `workshop` creation time `2026-08-12T01:02:14Z` converts to `2026-08-11 18:02:14 PDT`.
- Alignment formula: `local wall clock ≈ 18:02:14 + workshop global audio timestamp`. This is the metadata anchor; each screenshot-aligned interval also uses contemporaneous topic evidence.
- Example: screenshot 01 at `18:04:15` maps to approximately `00:02:01` in the workshop audio.

## Chunks and Raw Outputs

| Chunk | Workshop global interval | Raw output basename |
|---|---:|---|
| 00 | `00:00:00–00:15:00` | `transcripts/workshop/chunk-00` |
| 01 | `00:15:00–00:30:00` | `transcripts/workshop/chunk-01` |
| 02 | `00:30:00–00:45:00` | `transcripts/workshop/chunk-02` |
| 03 | `00:45:00–01:00:00` | `transcripts/workshop/chunk-03` |
| 04 | `01:00:00–01:15:00` | `transcripts/workshop/chunk-04` |
| 05 | `01:15:00–01:30:00` | `transcripts/workshop/chunk-05` |
| 06 | `01:30:00–01:45:00` | `transcripts/workshop/chunk-06` |
| 07 | `01:45:00–02:00:00` | `transcripts/workshop/chunk-07` |
| 08 | `02:00:00–02:13:17.099` | `transcripts/workshop/chunk-08` |

## Complete Intro Timeline

| Relative timestamp | Faithful summary of directly heard audio + ASR | Screenshot / correction | Inference | Confidence |
|---|---|---|---|---|
| `00:00:00–00:01:17` | Award-team certificates are presented or handed over; the host transitions to the next section. Names are unclear and unconfirmed. | audio-only. | Ceremony/transition before the formal workshop talks. | Medium |
| `00:01:17–00:02:34` | The agenda covers the competition, findings, winning-team talks, future ideas for data agents, and open resources. The task is more than answering questions: an agent must understand an unfamiliar workspace, connect evidence, compute, and verify exact and complete answers. | audio-only. | None. | High |
| `00:02:34–00:04:32` | The speaker reports 703 valid teams and 1,307 participants, plus leaderboard movement; public-leaderboard feedback does not equal generalization, and hidden evaluation changed rankings. | audio-only. | Numbers come from ASR and lack screenshot verification. | Medium |
| `00:04:32–00:05:48.331` | Phase 2 tasks were larger and more complex: about 20 files across five data types, often requiring structured and unstructured evidence together. The first-place team is then introduced. | audio-only. | None. | High |

## Complete Workshop Timeline

Rows follow workshop global time. Wall clock is `18:02:14 PDT + audio timestamp`. Screenshot corrections apply only to contemporaneous spoken terms, team/work names, or numbers; slide-only detail is not written as speech.

### 00 · `00:00:00–00:15:00`

| Audio timestamp / wall clock (PDT) | Speaker / topic; faithful summary of directly heard audio + ASR | Screenshot number and basename | Screenshot-supported ASR correction | Inference | Confidence |
|---|---|---|---|---|---|
| `00:00:00–00:02:00` / `18:02:14–18:04:14` | First winning-team speaker; name unconfirmed. Introduces the first-place KDD Cup Data Agents Challenge solution, restricted to a small `Qwen3.5` model, Docker, and two hours. The model suffix is unconfirmed. | audio-only. | `direct ASR agreement`: Whisper and Mac ASR support `Qwen3.5`, Docker, and two hours; neither reliably identifies the suffix. | None. | Medium |
| `00:02:00–00:04:30` / `18:04:14–18:06:44` | Why the task is hard and how to unify querying: inconsistent field names, formats, and units; entity attributes scattered through documents; redundant video frames and ASR term errors; and small-model tool-call or SQL failures. Sources are converted to tables, registered in DuckDB, and reduced to SQL generation. | 01 `Screenshot 2026-08-11 at 6.04.15 PM.png`; 02 `Screenshot 2026-08-11 at 6.06.12 PM.png`. | `screenshot-supported correction`: `docdb/dark DB` and `circle` become `DuckDB` and `SQL generation`; screenshots support the challenge-to-unified-query topic. | None. | High |
| `00:04:30–00:06:20` / `18:06:44–18:08:34` | Bounded harness: the solver agent has four explore/read/edit/run tools, completes a scaffolded `solver.py`, mainly writes SQL, and produces the final CSV. Other constraints normalize names/units, expose details only for relevant tables, vote on key decisions, and return short error context. | 03 `Screenshot 2026-08-11 at 6.08.08 PM.png`. | `screenshot-supported correction`: `solver.python` and `circle` become `solver.py` and `SQL`; the slide supports `Scaffold`, `Normalize`, and `Vote`. | None. | High |
| `00:06:20–00:08:35` / `18:08:34–18:10:49` | Document extraction first fixes the complete entity/ID set, then divides extraction by attributes. Code checks columns, row counts, and ID coverage, retries missing records, outer-joins results, and normalizes units and formats. | 04 `Screenshot 2026-08-11 at 6.10.18 PM.png`. | The slide supports `record universe`, `outer join`, and each worker covering every ID. | None. | High |
| `00:08:35–00:12:30` / `18:10:49–18:14:44` | Video and ASR: video-encoding packet size selects keyframes without decoding every frame; ASR detects language, uses a domain vocabulary prompt, and aligns frames, text, and HTML-like layout by word-level timestamps. The speaker reports Chinese CER below 2% and English WER below 1%. | audio-only. | `direct ASR agreement`: both ASRs support packet-size keyframes, word-level timestamps, CER/WER, and HTML-like layout; Mac's `WEI` is rejected. | These are speaker-reported results; this report did not reproduce them. | Medium |
| `00:12:30–00:14:30` / `18:14:44–18:16:44` | Results and limits: the solution ranked first and is compared with a general frontier agent. The claim is that a strong harness can make a lightweight model more reliable on a specific task. The first talk's final score conflicts across ASRs as `0.65` vs `0.69`; neither is selected. Other model names and comparison numbers are unclear. | audio-only. | `unresolved`: no clear contemporaneous screenshot resolves `0.65` vs `0.69`. | None. | Medium |
| `00:14:30–00:15:00` / `18:16:44–18:17:14` | Thanks, host transition, and brief room noise. | audio-only. | — | None. | High |

### 01 · `00:15:00–00:30:00`

| Audio timestamp / wall clock (PDT) | Speaker / topic; faithful summary of directly heard audio + ASR | Screenshot number and basename | Screenshot-supported ASR correction | Inference | Confidence |
|---|---|---|---|---|---|
| `00:15:00–00:18:05` / `18:17:14–18:20:19` | Q&A and transition. The speaker says a harness matters when the model is constrained; further gains may require model improvements tailored to specific problems. Some names and wording are unconfirmed. | audio-only. | — | None. | Medium |
| `00:18:05–00:21:20` / `18:20:19–18:23:34` | NVIDIA Data Explorer speaker; name unconfirmed by ASR. The goal is to run fast and preserve time for repeated attempts that improve stability. Inputs include CSV, JSON, PDF, and video. | 05 `Screenshot 2026-08-11 at 6.21.09 PM.png`. | The slide corrects the work name to `NV DATA EXPLORER` and supports “one SQL surface, two tools.” | None. | High |
| `00:21:20–00:24:20` / `18:23:34–18:26:34` | Preprocessing: structured data enters one SQL database, PDFs become Markdown, and videos become captioned images. This reduces entry points while complex modalities are processed asynchronously. | 06 `Screenshot 2026-08-11 at 6.23.45 PM.png`; 07 `Screenshot 2026-08-11 at 6.25.05 PM.png`. | Slides support `context.db`, `schema-scout`, and `prose_helper`; small slide text is not treated as speech. | None. | High |
| `00:24:20–00:26:45` / `18:26:34–18:28:59` | Document and video interfaces: `prose_helper` has QA and table-extraction modes. Video keyframes use audio pauses or visual changes; schema, question, and context help correct Whisper transcription. | 08 `Screenshot 2026-08-11 at 6.26.18 PM.png`; 09 `Screenshot 2026-08-11 at 6.28.05 PM.png`. | `pros/process helper` becomes `prose_helper`; `AST card` becomes `AST guard`. | None. | High |
| `00:26:45–00:30:00` / `18:28:59–18:32:14` | Bounded stateful Python and ensemble: preload helpers, restrict free file/interpreter access, adapt prompts to task language, run multiple attempts, and prioritize disputed predictions. | 10 `Screenshot 2026-08-11 at 6.30.52 PM.png`. | Slide supports `stateful Python`, `answer.csv`, and coverage-first ensemble/retry. | None. | High |

### 02 · `00:30:00–00:45:00`

| Audio timestamp / wall clock (PDT) | Speaker / topic; faithful summary of directly heard audio + ASR | Screenshot number and basename | Screenshot-supported ASR correction | Inference | Confidence |
|---|---|---|---|---|---|
| `00:30:00–00:33:10` / `18:32:14–18:35:24` | NVIDIA speaker: first ensure every task has a prediction, then spend budget on disputed tasks; merge candidates by column set, remove unnecessary columns, and preserve name columns. | audio-only. | — | None. | High |
| `00:33:10–00:37:20` / `18:35:24–18:39:34` | A coding agent makes a minimal “surgery-style” fix for one misprediction without harming other tasks. Q&A notes that schema, sample values, and `knowledge.md` help explain columns, while cross-modal links remain harder. | audio-only. | — | None. | Medium |
| `00:37:20–00:41:35` / `18:39:34–18:43:49` | Host closes the segment and prepares the next team; substantial room and device-transition noise. | audio-only. | — | None. | Medium |
| `00:41:35–00:45:00` / `18:43:49–18:47:14` | Leverages Team 1418 speaker; name unconfirmed. The team placed first in Phase 1 and fourth in Phase 2 and received a Merit Award. Introduces `Phase-Gated ReAct` and three problems: large search space, long multimodal context, and tool/SQL stability. | 11 `Screenshot 2026-08-11 at 6.44.25 PM.png`. | `direct ASR agreement`: both ASRs support Team 1418, Phase 1 first, and Phase 2 fourth; the slide corrects `Leverages` and `Phase-Gated ReAct`. | None. | High |

### 03 · `00:45:00–01:00:00`

| Audio timestamp / wall clock (PDT) | Speaker / topic; faithful summary of directly heard audio + ASR | Screenshot number and basename | Screenshot-supported ASR correction | Inference | Confidence |
|---|---|---|---|---|---|
| `00:45:00–00:48:00` / `18:47:14–18:50:14` | Four phases: `PLAN → EXPLORE → ANSWER → VERIFY`. Define the required answer, inspect data, form executable SQL, then independently re-query; a failed check may return to ANSWER a limited number of times. | 12 `Screenshot 2026-08-11 at 6.47.30 PM.png`; 13 `Screenshot 2026-08-11 at 6.48.32 PM.png`; 14 `Screenshot 2026-08-11 at 6.49.02 PM.png`. | `answer CSP` becomes `answer.csv`; slide supports `answer_from_sql`. | None. | High |
| `00:48:00–00:51:20` / `18:50:14–18:53:34` | Validation and domain guidance: inspect SQL before execution, then check empty results and output shape; an independent reviewer checks evidence path, columns, and values. Domain classification determines entity grain, aggregation, and deduplication. | 15 `Screenshot 2026-08-11 at 6.49.30 PM.png`; 16 `Screenshot 2026-08-11 at 6.50.26 PM.png`; 17 `Screenshot 2026-08-11 at 6.51.04 PM.png`. | Slides support `domain-aware guidance` and `row grain`. | None. | High |
| `00:51:20–00:54:20` / `18:53:34–18:56:34` | The phase-gated system scored higher locally and left fewer tasks unanswered. A fully automated improvement loop failed because of a leakage prompt, so humans proposed hypotheses while the agent implemented and ran experiments. Exact statistics were not all spoken. | 18 `Screenshot 2026-08-11 at 6.52.28 PM.png`; 19 `Screenshot 2026-08-11 at 6.53.21 PM.png`. | Slides qualify the ablation: end-to-end gains cannot all be attributed to phase gating. | None. | High |
| `00:54:20–00:55:25` / `18:56:34–18:57:39` | Thanks, short Q&A, and transition. | audio-only. | — | None. | Medium |
| `00:55:25–00:57:30` / `18:57:39–18:59:44` | Team Degas speaker; name unconfirmed. Rather than build a custom pipeline, the team encoded reusable rules in `SKILL.md` and ran them on a general coding agent. | 20 `Screenshot 2026-08-11 at 6.56.57 PM.png`; 21 `Screenshot 2026-08-11 at 6.57.54 PM.png`. | `codec/QuenCode` becomes `coding agent` / `qwen-code`. | None. | High |
| `00:57:30–01:00:00` / `18:59:44–19:02:14` | Skill rules and Phase 2 updates: unattended tasks must not stop to ask users; tools continue until `prediction.csv` is written and verified. Large files should not enter the main context. The talk then turns to document and video readers. | 22 `Screenshot 2026-08-11 at 7.01.02 PM.png`; 23 `Screenshot 2026-08-11 at 7.02.02 PM.png`. | Slides support `doc-reader`, `video-reader`, `whisper.cpp`, and `PaddleOCR`. | None. | High |

### 04 · `01:00:00–01:15:00`

| Audio timestamp / wall clock (PDT) | Speaker / topic; faithful summary of directly heard audio + ASR | Screenshot number and basename | Screenshot-supported ASR correction | Inference | Confidence |
|---|---|---|---|---|---|
| `01:00:00–01:02:25` / `19:02:14–19:04:39` | Team Degas finishes the video reader: combine frames, captions, and OCR so the main agent does not carry long-video detail. An independent reviewer then treats executor output as a possibly wrong hypothesis. | 24 `Screenshot 2026-08-11 at 7.03.14 PM.png`. | Slide supports `reviewer agent` and “Treat executor's analysis only as a hypothesis. It may be wrong.” | None. | High |
| `01:02:25–01:05:15` / `19:04:39–19:07:29` | Attempts without reliable gains: demonstration playbooks, two executors plus a reviewer, and three-executor majority voting showed no clear stable benefit. | 25 `Screenshot 2026-08-11 at 7.04.50 PM.png`. | Slide supports “what did not work”; extra slide experiment detail is not treated as speech. | None. | High |
| `01:05:15–01:07:55` / `19:07:29–19:10:09` | Unconfirmed ideas and difficulties: shorter prompts, worked examples, and reasoning mode showed signals but were not confirmed. Agents still ignore skills, local scores fluctuate, and hand-written skills may omit critical rules. | 26 `Screenshot 2026-08-11 at 7.05.51 PM.png`; 27 `Screenshot 2026-08-11 at 7.07.37 PM.png`; 28 `Screenshot 2026-08-11 at 7.08.29 PM.png`. | Slides correct `thinking`/`skill` and explicitly distinguish “couldn't confirm.” | None. | High |
| `01:07:55–01:09:50` / `19:10:09–19:12:04` | Talk close and room Q&A. ASR repeats at `01:07:09–01:07:58` and `01:08:28–01:09:45`; content is unconfirmed, so only the Q&A/transition is retained. | audio-only. | — | None. | Low (ASR repetition degeneration) |
| `01:09:50–01:12:20` / `19:12:04–19:14:34` | Team Null Hypothesis speaker; audio sounds like Atif Khan, retained as audio-derived. Introduces the team, multimodal tasks, and a skill/agent-harness approach. | audio-only. | — | None. | Medium |
| `01:12:20–01:15:00` / `19:14:34–19:17:14` | Bounded phases: one runtime uses different skills, artifacts, and gates for discovery, solver, and learner. The agent loop explores, but each phase emits an inspectable artifact and a deterministic gate decides whether to continue or publish. | 29 `Screenshot 2026-08-11 at 7.14.51 PM.png`; 30 `Screenshot 2026-08-11 at 7.15.14 PM.png`; 31 `Screenshot 2026-08-11 at 7.16.49 PM.png`. | Slides support `discover / solve / review`, `repair / learn`, and `execute / validate / publish`. | None. | High |

### 05 · `01:15:00–01:30:00`

| Audio timestamp / wall clock (PDT) | Speaker / topic; faithful summary of directly heard audio + ASR | Screenshot number and basename | Screenshot-supported ASR correction | Inference | Confidence |
|---|---|---|---|---|---|
| `01:15:00–01:17:20` / `19:17:14–19:19:34` | Skills emerge iteratively from task feedback; the central rule is to generalize and not overfit one task. `01:16:59–01:17:11` contains an incomplete repetition; exact wording is unconfirmed. | 32 `Screenshot 2026-08-11 at 7.17.55 PM.png`. | Slide supports `Skills Development` and `always generalize, never overfit`. | None. | Medium |
| `01:17:20–01:19:30` / `19:19:34–19:21:44` | Solver loop and human involvement: trace interpretation, evidence, and planning into code; after feedback, repair, revalidate, and republish. Human participation varies with risk. | 33 `Screenshot 2026-08-11 at 7.19.36 PM.png`; 34 `Screenshot 2026-08-11 at 7.20.23 PM.png`. | Slides support `Interpretation → Contract → Evidence → Plan → Code` and `Feedback → Repair → Revalidate → Republish`. | None. | High |
| `01:19:30–01:21:55` / `19:21:44–19:24:09` | Multimodal purchase-price walkthrough: CSV, an image discount memorandum, and knowledge rules contribute different facts before calculation. Negative result: normalizing everything to SQL made hard joins work poorly, so the team switched to just-in-time discovery and generated Python; validation follows and low-evidence answers may abstain. | 35 `Screenshot 2026-08-11 at 7.21.26 PM.png`; 36 `Screenshot 2026-08-11 at 7.21.51 PM.png`; 37 `Screenshot 2026-08-11 at 7.22.06 PM.png`; 38 `Screenshot 2026-08-11 at 7.22.21 PM.png`; 39 `Screenshot 2026-08-11 at 7.22.27 PM.png`; 40 `Screenshot 2026-08-11 at 7.22.41 PM.png`; 41 `Screenshot 2026-08-11 at 7.22.54 PM.png`; 42 `Screenshot 2026-08-11 at 7.23.05 PM.png`; 43 `Screenshot 2026-08-11 at 7.23.51 PM.png`. | Slides correct `Beacon` and `discount memorandum` and support artifact names such as `answer-contract.yaml`, `evidence-map.md`, and `validation.md`; this does not mean each was spoken. Prices and discounts remain screenshot evidence. | Hard-join failure and the Python switch are speaker claims about this team; no universal Python-over-SQL claim is inferred. | High |
| `01:21:55–01:23:40` / `19:24:09–19:25:54` | Software-engineering lessons: test-driven development, service-oriented architecture, component modularization, and known interfaces. Negative result: the initial attempt to pre-index everything was too costly and the first submitted run did not finish; the team switched to just-in-time evidence search. Modular memory can turn human feedback into question or workspace/long-term memory. | 44 `Screenshot 2026-08-11 at 7.24.02 PM.png`; 45 `Screenshot 2026-08-11 at 7.25.32 PM.png`. | Slides support `memory ... never as task evidence` and `Bounded Agents, Deterministic Answers`; these slide-only points are not added as speech. | The unfinished pre-indexing run and switch are speaker claims about this team, not universal conclusions. | High |
| `01:23:40–01:25:45` / `19:25:54–19:27:59` | The talk has ended and room Q&A begins. The speaker says the approach is used in insurtech so brokers can ask questions over reports and insurance policies while speaking with users. Long ASR repetition later in the interval makes exact speech unconfirmed. | 46 `Screenshot 2026-08-11 at 7.26.34 PM.png`. | Screenshot 46 is time-anchored here but only shows a slide still on screen; it does not prove its text was spoken during Q&A. | None. | Medium (later ASR repetition) |
| `01:25:45–01:26:42` / `19:27:59–19:28:56` | Room Q&A and equipment handoff; no method evidence. | audio-only. | — | None. | Medium |
| `01:26:42–01:30:00` / `19:28:56–19:32:14` | Team Olympus / Astrolabe speaker; personal name unconfirmed. Introduces real-world evidence: the agent may explore freely, but numbers pass deterministic checks; describes the drug, patient, follow-up, and counting problem. | 47 `Screenshot 2026-08-11 at 7.29.50 PM.png`; 48 `Screenshot 2026-08-11 at 7.30.42 PM.png`; 49 `Screenshot 2026-08-11 at 7.31.09 PM.png`. | Slides correct the work name to `Astrolabe` and support `real-world evidence` and `plausible wrong number`. | None. | High |

### 06 · `01:30:00–01:45:00`

| Audio timestamp / wall clock (PDT) | Speaker / topic; faithful summary of directly heard audio + ASR | Screenshot number and basename | Screenshot-supported ASR correction | Inference | Confidence |
|---|---|---|---|---|---|
| `01:30:00–01:31:25` / `19:32:14–19:33:39` | Errors often concern who counts, observation start, and sufficient follow-up—not SQL syntax. Three agreeing computation paths may share the same study-design error. | 50 `Screenshot 2026-08-11 at 7.33.27 PM.png`. | Slide corrects `three paths agree` and `eligibility`; exact numbers are not treated as audio-only speech. | None. | High |
| `01:31:25–01:34:30` / `19:33:39–19:36:44` | Live demo: asks the one-year GI-bleed incidence after a common painkiller. The system maps language to medical concepts and writes a study plan, inclusion criteria, outcome, follow-up window, and checklist. Live self-correction at `01:32:28–01:33:15` makes exact wording unconfirmed. | 51 `Screenshot 2026-08-11 at 7.34.06 PM.png`; 52 `Screenshot 2026-08-11 at 7.35.08 PM.png`. | Slides support `GI bleed`, `celecoxib`, and `gastrointestinal hemorrhage`; visible IDs are not treated as speech. | None. | Medium |
| `01:34:30–01:37:20` / `19:36:44–19:39:34` | SQL, Python, and an eligibility ledger independently compute the question. They initially agree, yet validation rejects the result because some patients lack pre-index data or full follow-up. Criteria are revised, then recomputed and reviewed. | 53 `Screenshot 2026-08-11 at 7.36.32 PM.png`; 54 `Screenshot 2026-08-11 at 7.38.24 PM.png`. | `0.1908`, `1,745`, and `333` are screenshot-visible ASR corrections; this row does not claim they were spoken verbatim. | None. | High |
| `01:37:20–01:39:11` / `19:39:34–19:41:25` | Second run and cautious interpretation: a new question may follow different paths; even after checks pass, a reviewer warns against strong conclusions from a small cohort/few events. Names, drugs, and some numbers are unconfirmed. | 55 `Screenshot 2026-08-11 at 7.40.47 PM.png`. | Slide supports “verified ≠ safe to read” and the small-sample warning; numbers such as `8/15` are screenshot corrections only. | None. | Medium |
| `01:39:11–01:39:31` / `19:41:25–19:41:45` | audio-only negative result: removing guards one at a time showed that removing the eligibility check made the system accept a biased answer. All three paths still agreed, so consensus did not object. The speaker concludes consensus cannot replace that guard. `01:39:22–01:39:31` repeats, but the result is clear before the repetition. | audio-only. | — | “Consensus cannot replace the guard” is the speaker's ablation conclusion, not this report's extrapolation. | High |
| `01:39:31–01:40:13` / `19:41:45–19:42:27` | The same unchanged agent ran on three datasets, including real de-identified hospital data. The speaker concludes that healthcare research agents must be cautious and smart, and architecture can combine autonomy and verification. | audio-only. | — | None. | High |
| `01:40:13–01:42:28` / `19:42:27–19:44:42` | Astrolabe ends; the host introduces remote teams and handles screen sharing. Overlap, silence, and setup at `01:41:03–01:42:21` cannot be reliably recovered. | audio-only. | — | None. | Low (room setup) |
| `01:42:28–01:45:00` / `19:44:42–19:47:14` | Team 1688 remote speaker; name unconfirmed. The team placed fifth. Phase 2 is a multifile workspace, not single-table QA; incremental changes produced little gain, so the team rebuilt around explicit schemas and controlled execution. Continues in the next chunk. | audio-only. | `direct ASR agreement`: both ASRs support Team 1688 and fifth place. | None. | High |

### 07 · `01:45:00–02:00:00`

| Audio timestamp / wall clock (PDT) | Speaker / topic; faithful summary of directly heard audio + ASR | Screenshot number and basename | Screenshot-supported ASR correction | Inference | Confidence |
|---|---|---|---|---|---|
| `01:45:00–01:46:50` / `19:47:14–19:49:04` | Each modality has a role: video may supply rules, documents mappings, and databases exact values. A task-level schema connects source, entity, rule, and output. | 56 `Screenshot 2026-08-11 at 7.48.30 PM.png`; 57 `Screenshot 2026-08-11 at 7.49.21 PM.png`. | Slides correct `schema control plane` and `typed workspace map`. | None. | High |
| `01:46:52–01:47:32` / `19:49:06–19:49:46` | ASR repetition degeneration prevents reliable recovery; only the timestamp and continuation of Team 1688's talk are retained. | audio-only. | — | None. | Low (repetition degeneration) |
| `01:47:32–01:50:20` / `19:49:46–19:52:34` | Route by source role and use bounded tools: unstructured evidence supplies rules/mappings, structured sources exact values; inspect schema and samples before bounded SQL, Python, document, and video operations. | 58 `Screenshot 2026-08-11 at 7.50.10 PM.png`; 59 `Screenshot 2026-08-11 at 7.51.02 PM.png`; 60 `Screenshot 2026-08-11 at 7.52.18 PM.png`. | Slides support `canonical structured source`, `bounded tools`, and `read-only`. | None. | High |
| `01:50:20–01:53:25` / `19:52:34–19:55:39` | Validation, clock, and delivery: answer schema covers columns, grain, nulls/duplicates, and units; reject empty output; limit fresh-context reviewer repairs; use concurrency, fallback, and atomic writes to avoid missing files at deadline. | 61 `Screenshot 2026-08-11 at 7.53.06 PM.png`; 62 `Screenshot 2026-08-11 at 7.53.58 PM.png`; 63 `Screenshot 2026-08-11 at 7.55.06 PM.png`. | Slides support `schema-aware validation`, `wall clock`, and `atomic write`; chart scores remain visual corrections only. | None. | High |
| `01:53:25–01:55:48` / `19:55:39–19:58:02` | Explicit schemas and bounded execution improved deliverability, but run-to-run variance remained. Thanks and handoff around `01:54:40`. | 64 `Screenshot 2026-08-11 at 7.57.40 PM.png`. | Screenshot 64 is the next team's `Data Agent Studio` cover and marks a nearby transition/name only; its text is not inserted into Team 1688 speech. | Timing shows the next cover; audio starts that talk around `01:55:48`. | Medium |
| `01:55:48–01:57:57` / `19:58:02–20:00:11` | Data Agent Studio speaker. Audio clearly has the host announce Team 1401; a personal name is not confirmed from ASR alone. Data-agent execution is hard to observe or interrupt; the goal is visible intermediate state and control before actions. | 64 `Screenshot 2026-08-11 at 7.57.40 PM.png`; 65 `Screenshot 2026-08-11 at 7.59.26 PM.png`; 66 `Screenshot 2026-08-11 at 8.00.11 PM.png`. | `screenshot-supported correction`: screenshot 64 supports `UITNLP · VNU-HCM`, Team ID 1401, presenter `Ha Huu Phat`, and Creative Track Top 3; these identity strings are not treated as speech. Slides also correct `Limited Observability` and `Step-Level Intervention`. | None. | High |
| `01:57:57–02:00:00` / `20:00:11–20:02:14` | Begins three design elements: multi-step orchestration, strategy selection by task characteristics, and observable/controllable execution. Continues in the next chunk. | audio-only. | — | None. | High |

### 08 · `02:00:00–02:13:17.099`

| Audio timestamp / wall clock (PDT) | Speaker / topic; faithful summary of directly heard audio + ASR | Screenshot number and basename | Screenshot-supported ASR correction | Inference | Confidence |
|---|---|---|---|---|---|
| `02:00:00–02:01:20` / `20:02:14–20:03:34` | Completes the three elements and architecture: interface renders traces; gateway handles sessions/events; orchestration handles routing, execution, self-correction, and interaction control; lower layers call SQL, Python, documents, and models. | 67 `Screenshot 2026-08-11 at 8.02.15 PM.png`; 68 `Screenshot 2026-08-11 at 8.03.03 PM.png`. | Slides support `Multi-Step Orchestration`, `Adaptive Strategy Selection`, and `Interaction / Orchestration / Execution`. | None. | High |
| `02:01:20–02:03:30` / `20:03:34–20:05:44` | Difficulty-aware routing and recovery: easy/medium use ReAct; hard tasks use signals such as multiple sources and long documents to choose planner/analyst, multi-agent, or dynamic retrieval. Errors, stagnation, and exhausted budgets have recovery/return policies. | 69 `Screenshot 2026-08-11 at 8.03.51 PM.png`. | Slide corrects router name to `Hybrid-B`; not every slide detail is treated as speech. | None. | High |
| `02:03:30–02:05:20` / `20:05:44–20:07:34` | Human control has two interaction modes. Whisper repeats Autopilot for the second; the contemporaneous slide identifies Co-pilot. Autopilot runs continuously and pauses only for approval-required calls. Co-pilot waits before a proposed tool call so the user can approve, edit, reject, or guide. | 70 `Screenshot 2026-08-11 at 8.05.31 PM.png`. | `screenshot-supported correction`: second mode is `Co-pilot`; slide also supports `Autopilot` and `AWAITING_USER`. This is not corrected from Mac ASR alone. | None. | High |
| `02:05:20–02:08:18` / `20:07:34–20:10:32` | Cross-modal workflows, evaluation, and limits: cross-source joins, document relation extraction, human-approved data correction, and traceable output. The speaker compares backbone scores, cost, and latency and states that external validity, difficulty/modality confounding, and system-level stability remain insufficiently tested. Per-task cost conflicts across ASRs as `25c` vs `35c`; neither is selected. | 71 `Screenshot 2026-08-11 at 8.06.11 PM.png`; 72 `Screenshot 2026-08-11 at 8.08.47 PM.png`; 73 `Screenshot 2026-08-11 at 8.09.39 PM.png`. | Slides correct `ground-truth files`, `permission checks`, `external validity`, and `run-to-run stability`. `unresolved`: current screenshots do not clearly show per-task cost and cannot resolve `25c` vs `35c`; other latency figures are screenshot support only. | None. | High (except cost) |
| `02:08:18–02:08:52` / `20:10:32–20:11:06` | Talk ends; host thanks the final presenter and transitions to closing. | audio-only. | — | None. | High |
| `02:08:52–02:12:18` / `20:11:06–20:14:32` | Host explicitly invites Professor Tang for closing remarks. The remarks say real-world data agents must understand task and data, align information across sources, and keep verifying answers; a group photo follows. Other names/dialogue at `02:09:00–02:09:15` are unconfirmed. | audio-only. | `direct ASR agreement`: both ASRs support `Professor Tang` closing remarks. | None. | High (except other room names) |
| `02:12:18–02:13:15.560` / `20:14:32–20:15:29.560` | Photos, informal conversation, and thanks. Room audio after `02:12:18` is low confidence and individual statements are unconfirmed; its place in the meeting close is retained. | audio-only. | — | None. | Low (informal/distant speech) |
| `02:13:15.560–02:13:17.099` / `20:15:29.560–20:15:31.099` | No-speech tail; recording ends naturally. | audio-only. | — | None. | High |

## Coverage and Blockers

### Audio Coverage and Continuity

| Scope | Covered / original duration | Coverage | Continuity evidence |
|---|---:|---:|---|
| intro | `348.330667 / 348.330667 s` | **100%** | `intro.{txt,vtt,json}` are nonempty; timeline covers `00:00:00–00:05:48.331`. |
| workshop | `7997.098667 / 7997.098667 s` | **100%** | `chunk-00..08.{txt,vtt,json}` are nonempty; nominal boundaries continuously cover `00:00:00–02:13:17.099`. |
| aggregate | `8345.429334 / 8345.429334 s` | **100%** | Both recordings are fully included. |

- Chunk boundaries were checked. Chunks 00, 01, 02, 04, 05, and 07 cover their full 15 minutes. Chunk 03's last speech is at local `14:59.920` with about `80 ms` of silence. Chunk 06 ASR ends at `15:00.120`, 120 ms beyond its WAV, and is clamped to nominal `01:45:00`. Chunk 08's last speech is at `02:13:15.560`; the final `1.539 s` of silence is included.
- The recording ends naturally: talks end around `02:08:18`, followed by closing, the group photo, and room audio; the final no-speech tail reaches the media endpoint.

### Screenshot Coverage and Cross-Alignment

| Metric | Result | Meaning |
|---|---:|---|
| screenshot time mapping | **73/73** | Every Desktop basename maps by `18:02:14 PDT + audio timestamp`; screenshot number, basename, and contemporaneous interval are listed above. |
| screenshot coverage | **73/73** | All 73 real files in the index are referenced. This registers sparse slide samples, not a complete deck. |
| cross-aligned coverage | **73/73 (topic-level)** | Every screenshot was cross-checked with its contemporaneous audio topic to correct terms, team/work names, numbers, or processes. This is not verbatim-speech verification; unspoken slide content was not added to directly heard summaries. |
| audio-only coverage | **fully retained** | Every interval without a useful screenshot remains in the timeline as `audio-only`; none was removed for lacking a screenshot. |

### Limitations / Blockers

- **Coverage blocker: none.** Both audio files and all nine workshop chunks are readable, so intro, workshop, and aggregate coverage are each 100%.
- **Evidence limitation, not a coverage blocker:** no manual speaker diarization. This is a faithful ASR-assisted summary, not a verbatim transcript. Distant Q&A, room names, proper nouns, and identified repetition-degeneration intervals remain unconfirmed.
- **Explicit low-confidence intervals:** workshop `01:07:09–01:07:58`, `01:08:28–01:09:45`, `01:16:59–01:17:11`, `01:24:51–01:25:21`, `01:32:28–01:33:15`, `01:41:03–01:42:21`, `01:46:52–01:47:32`, `02:09:00–02:09:15`, and `02:12:18–02:13:15.560`. No speculative verbatim content is used for these intervals.
