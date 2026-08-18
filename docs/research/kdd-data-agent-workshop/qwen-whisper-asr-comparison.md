# Qwen / Whisper ASR comparison

## Status

**NO-GO for a Qwen-versus-Whisper comparison.**

**Later status note (2026-08-11):** The Whisper coverage table in this report is a historical snapshot from the time of the Qwen smoke test, not current overall progress. Local Whisper later completed `intro` and workshop `chunk-00..08`; `meeting-audio-alignment.md` reports `8345.429334 / 8345.429334s` (100%) across both recordings and topic-level cross-alignment for 73/73 screenshots. Qwen still has zero transcripts, so the Qwen-versus-Whisper verdict remains NO-GO.

OpenRouter's live catalog does declare one dedicated Qwen STT model, but its
OpenRouter smoke request for the supplied audio returned a scrubbed HTTP 400
provider error and no transcript. There is therefore no Qwen text, usage,
generation receipt, or timestamp data to compare with Whisper. This is a
failed comparison run, not evidence that the recording is empty or that
Whisper is correct.

This document is the only repo artifact from this review. It does not edit the
main audio alignment, the Whisper outputs, implementation code, or skills.

## Scope and evidence rules

- The two audio files are the meeting record. The `workshop.m4a` main recording
  is about 2:13:17; `intro.m4a` is a separate 5:48 opening/award segment.
  Both remain in scope through their full duration.
- The 73 screenshots are sparse presentation-slide observations, not the full
  deck and not a transcript. Missing screenshots are never negative evidence.
- An interval without a verified screenshot link is labelled **audio-only**.
  It must remain in the main Whisper transcript/alignment with timestamps,
  speaker/topic evidence, and a faithful excerpt or summary. This Qwen report
  neither deletes nor shortens it.
- A screenshot may correct an ASR reading only when the audio actually says the
  item and the interval is aligned. Slide-only text must not be inserted as a
  speaker quote.
- No API key, audio base64, or authorization header is stored here. Qwen smoke
  artifacts are local review material and are not included because of privacy
  and source availability.

## Source inventory

| Recording | SHA-256 verified | Duration | Role |
| --- | --- | ---: | --- |
| `intro.m4a` | `2adf77325cec0f5a78ccc784794c2744bdb7f1a0ff34aff2e36696075332a9a2` | 348.330667 s | opening / awards; must be retained |
| `workshop.m4a` | `24b5fd98fb9dc426039ea3eac3cc18ce8ba9dbe7074db4ba0e3b6c8ac7718929` | 7,997.098667 s | complete workshop mainline; must be retained |

The source files themselves give **100% audio-source availability**. That is
different from having a completed ASR transcript.

## Live OpenRouter model proof

### Correct discovery path

OpenRouter's official STT documentation says to discover transcription models
with `output_modalities=transcription` and to use the dedicated
`POST /api/v1/audio/transcriptions` endpoint, rather than treating a general
chat model's video input as audio support.

- [OpenRouter STT documentation](https://openrouter.ai/docs/guides/overview/multimodal/stt)
- [OpenRouter Models API documentation](https://openrouter.ai/docs/api-reference/models/get-models)
- Live catalog query: `GET https://openrouter.ai/api/v1/models?output_modalities=transcription&model_authors=qwen`
- Live endpoint record: `GET https://openrouter.ai/api/v1/models/qwen/qwen3-asr-flash-2026-02-10/endpoints`

The catalog/endpoint receipts were read at **2026-08-12T03:58:11Z**. The
catalog receipt was cacheable; the endpoint record was `no-store` at the same
response time.

| Field | Observed value |
| --- | --- |
| Exact model id | `qwen/qwen3-asr-flash-2026-02-10` |
| Model name | `Qwen: Qwen3 ASR Flash` |
| Catalog modality | `audio->transcription` |
| Input modality | `audio` |
| Output modality | `transcription` |
| OpenRouter endpoint used for smoke | `/api/v1/audio/transcriptions` |
| Catalog route record | one listed route, provider name `Alibaba`, status `0`; this is OpenRouter routing metadata, **not** a direct provider call |
| Timestamp promise | none established for this route; no successful response exists to assess timestamp quality |

This supersedes an earlier broad, cached general-model listing that showed only
regular Qwen chat/VL entries. That listing had 49 entries: 26 `text`, 9
`text,image` (including two with the order `image,text`), and 14
`text,image,video`. It showed no ordinary chat model with `audio` input. The
14 video-capable models are **not** treated as audio/ASR models. The filtered
STT query above is the relevant, official discovery method and found the
dedicated Qwen transcription declaration.

## OpenRouter smoke: failed

All requests below were sent to the OpenRouter endpoint above. No direct
Alibaba call, Novita call, or alternate provider/model substitution was made.
The source was `intro.m4a` (or its local WAV derivative for a format probe),
whose original SHA-256 is listed above.

| UTC start | OpenRouter request form | Result |
| --- | --- | --- |
| 2026-08-12T03:59:13.103Z | base64 JSON, `m4a`, language `en`, temperature `0`, response format `json` | HTTP 400; no text or usage |
| 2026-08-12T04:00:32.194Z | multipart, `m4a`, same explicit options | HTTP 400; no text or usage |
| 2026-08-12T04:01:20.311Z | minimal multipart, `m4a` | HTTP 400; no text or usage |
| 2026-08-12T04:02:41.224Z | minimal base64 JSON, local WAV derivative | HTTP 400; no text or usage |
| 2026-08-12T04:03:05.024Z | multipart WAV derivative, response format `json` | HTTP 400; no text or usage |

The repeated, scrubbed OpenRouter response was:

```json
{"error":{"message":"Provider returned 400","code":400}}
```

None of those receipts has `X-Generation-Id`, `X-Provider-Name`, transcript
text, usage, or timestamps. The API can list a model and still fail an actual
audio request; this run does not establish callable transcription support for
these recordings. Per the stop instruction, no more format/provider debugging
or live calls were made after this result.

## Coverage snapshot

This is a historical snapshot of files available while the separate local Whisper
task was still producing chunks. It has been superseded for current Whisper progress
by `meeting-audio-alignment.md`; it remains here only to document what was available
at the time of the failed Qwen comparison.

| Coverage dimension | Evidence and current result |
| --- | --- |
| Audio source coverage | 2/2 recordings present and hash-verified: 8,345.429334 s total (100% source availability). |
| Local Whisper transcript coverage | `intro`: 348.320 s / 348.330667 s (99.997%). `workshop`: chunks 00–02 cover global 00:00–45:00, 2,700 s / 7,997.098667 s (33.762%). Combined local-Whisper coverage at this snapshot: 3,048.320 s / 8,345.429334 s (36.526%). |
| Screenshot coverage | 73 sparse screenshots, timestamped 6:04:15 PM–8:09:39 PM in [screenshot-index.md](screenshot-index.md). They are not a complete-deck denominator, so a percentage is not knowable. |
| Qwen ↔ Whisper cross-aligned coverage | **0 s**. No Qwen transcript was returned. |
| Screenshot ↔ audio cross-aligned coverage in this report | **0 verified s**. This comparison run did not establish a recording-to-slide-clock offset; unlinked content remains `audio-only`, not absent. |

### Global audio intervals

Whisper chunk times below are global workshop intervals, not per-file local
offsets. `audio-only (alignment pending)` means no screenshot relation is
claimed here; it does not mean the content is unimportant.

| Source / global interval | Local Whisper snapshot | Qwen result | Evidence label / topic status |
| --- | --- | --- | --- |
| `intro` 00:00–05:48.331 | `intro.json` present through 05:48.320 | none | audio-only (alignment pending); opening, scale/agenda, awards are Whisper-derived leads only |
| workshop 00:00–15:00 | `chunk-00.json` present | none | audio-only (alignment pending); first-place presentation lead |
| workshop 15:00–30:00 | `chunk-01.json` present | none | audio-only (alignment pending); Q&A / next-presentation transition lead |
| workshop 30:00–45:00 | `chunk-02.json` present | none | audio-only (alignment pending); ensemble/coding-agent material, then next presentation lead |
| workshop 45:00–60:00 | WAV `chunk-03.wav` existed; no Whisper JSON in this snapshot | none | audio-only; local Whisper still pending |
| workshop 60:00–75:00 | pending | none | audio-only; local Whisper still pending |
| workshop 75:00–90:00 | pending | none | audio-only; local Whisper still pending |
| workshop 90:00–105:00 | pending | none | audio-only; local Whisper still pending |
| workshop 105:00–120:00 | pending | none | audio-only; local Whisper still pending |
| workshop 120:00–133:17.099 | pending | none | audio-only; local Whisper still pending |

## Chunk comparison and adjudication

There is no Qwen column to compare. Accordingly, every current interval has
the same evidence-grade outcome: **not comparable**.

| Category requested for review | Result |
| --- | --- |
| Proper nouns, team/model/tool names | No Qwen candidate; no comparison or correction. |
| Numbers, percentages, ranks, attempts, votes | No Qwen candidate; no comparison or correction. |
| Negations and limiting statements | No Qwen candidate; no comparison or correction. |
| Speaker/topic boundaries | No Qwen timestamps or transcript; no comparison or correction. |
| Direct ASR agreement | 0 items. Agreement is not ground truth in any event. |
| Screenshot-supported correction | 0 items. No slide text was promoted into a spoken transcript. |
| Unresolved | All Qwen-side wording, timestamps, boundaries, and quality. |

Some local-Whisper strings are visibly risky (for example, model/team names and
terms such as `DuckDB`, `Qwen`, or `KDD Cup`). They remain **review flags**,
not silent repairs. A future correction needs either direct ASR agreement or a
time-aligned screenshot that confirms a term the speaker actually says.

## Supplemental Mac Voice Memos ASR evidence

An additional `Mac Voice Memos ASR candidate` source was read. It is a third
ASR candidate, not ground truth and not a Qwen result. Its raw text is not
included because of privacy and source availability. It has no
usable timestamps, contains systematic phonetic/proper-noun errors (for example
`Queen`, `dark DB`, and `circle`), and cannot establish or overwrite Whisper's
global timestamps, speaker/topic boundaries, or the slide-alignment clock.

It also cannot turn slide-only text into a spoken quote. The classifications
below are a review aid only: direct ASR agreement is not ground truth, and a
screenshot-supported correction applies only where the corresponding audio was
actually spoken and independently aligned.

### Direct ASR agreement

| Candidate agreement | Status and permitted use |
| --- | --- |
| Broad presentation order: first-place lightweight-model harness, NV Data Explorer, Leverages/Team 1418, skill-driven material, Team 1688, Data Agent Studio/Team 1401, then closing remarks | The Mac and local Whisper outputs support this **order-level** sequence. Because the Mac output has no timestamps, it does not refine any boundary or name a speaker. |
| `Data Agent Studio` and the base `Autopilot` mode | Both local ASRs independently contain these phrases near the final presentation. This is a corroborating candidate only; it does not by itself correct wording or timing. |
| Schema-oriented wording in the late workshop material | Both ASRs repeatedly suggest a schema-first/schema-aware theme. Treat it as topic corroboration, not a reliable quotation or a numerical claim. |

No transcript line was silently edited from direct ASR agreement alone.

### Screenshot-supported correction

The following normalizations are supported by a screenshot term and a matching
spoken-audio context. They correct only the ASR token/phrase, not the speaker's
full wording.

| ASR risk | Normalized review term | Support and boundary |
| --- | --- | --- |
| `DuckDDB` / phonetic `deducted be` | `DuckDB` | The aligned first-place architecture slide labels the unified runtime `DuckDB`; use only for the corresponding spoken database term. |
| `circle generation` | `SQL generation` | The aligned first-place overview explicitly calls the task a `SQL generation problem`; do not import surrounding slide text as speech. |
| `recorded universe` | `record universe` | The aligned document fan-out slide uses `record_universe`; normalize only the spoken identifier/concept. |
| Second final-presentation mode transcribed as another `Autopilot` | `Co-pilot` | [screenshot-index.md](screenshot-index.md) Topic 6, item 70 names the two modes `Autopilot` and `Co-pilot`; the Mac candidate also hears the latter. This corrects the mode label only, not a speaker boundary. |

### Unresolved

| Item | Why it remains unresolved |
| --- | --- |
| Exact Qwen model spelling/variant in the opening | The ASRs variously produce `Qn`, `Queen`, and an unclear `3.5 A3B` form. Do not promote an exact variant without an aligned primary source. |
| First presenter's personal name and organization | The two ASRs disagree materially (`Zhang Zhe Zhang`/`Meitan` versus phonetic alternatives). No correction is made from ASR alone. |
| Opening performance number | Local Whisper reads `0.65`; the Mac output can be read as `0.69`. This is a conflict, not a corrected score. |
| Data Agent Studio model and cost figures | `GPT-40`/`GPT-40 mini` and roughly `25c`/`35c` source-cost readings are ASR-ambiguous. They require an aligned slide or primary artifact before use. |
| `word-level timestamps`, `CER`, and `WER` wording/values | The Mac system output corrupts these terms and the local Whisper wording is imperfect; retain as terminology review flags rather than exact claims. |
| Speaker and topic boundaries | The Mac transcript has no timestamps. It must never override Whisper boundaries or infer a missing/extra speaker from a screenshot gap. |

## Conclusion and handoff

- **Model proof:** `qwen/qwen3-asr-flash-2026-02-10` is a real OpenRouter
  catalog declaration for `audio->transcription`.
- **Run verdict:** **NO-GO.** The OpenRouter smoke for the supplied recording
  returned only HTTP 400 provider errors, so no fair Qwen/Whisper transcript
  comparison can be made.
- **Completed reliable path:** local Whisper subsequently reached full coverage for
  both recordings. `meeting-audio-alignment.md` preserves both recordings and all
  screenshot-free sections as `audio-only`.
- **Do not infer:** no Qwen failure proves anything about the speaker's words;
  no screenshot proves a missing slide or statement; no ASR agreement proves
  ground truth.

If this review is reopened, first obtain a successful OpenRouter Qwen receipt
for the same audio under newly authorized scope. Only then create Qwen chunks,
compare them with the matching Whisper global intervals, and record corrections
as `direct ASR agreement`, `screenshot-supported correction`, or `unresolved`.
