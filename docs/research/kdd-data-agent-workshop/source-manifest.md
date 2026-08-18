# Greenfield Data Agent Research Source Manifest

Date: 2026-08-11

Status: Research manifest. This is not the final spec and does not authorize implementation or production mutation.

## 1. Usage Rules

- `direct`: audio, image, video, PDF, or fixed-SHA source read directly during this research.
- `author claim`: a claim made in a README, paper, talk, or slide; it is not promoted without an independent receipt.
- `reviewer inference`: a design judgment derived from multiple sources; it must retain a falsifier.
- `planning input`: an Adopt / Adapt / Reject judgment, engineering proposal, or owner decision; it cannot rewrite primary-source facts.
- Audio segments without matching screenshots remain valid. The screenshots are only a partial slide set, not a complete deck or transcript.
- Visible UI does not prove server-side enforcement, production correctness, or causal attribution.

## 2. Meeting Evidence

| Source | Stable identity | Coverage | Evidence class | Canonical research artifact | Boundary |
|---|---|---:|---|---|---|
| Intro audio | `Workshop intro recording`; SHA-256 `2adf77325cec0f5a78ccc784794c2744bdb7f1a0ff34aff2e36696075332a9a2` | `348.330667 / 348.330667s` | direct audio + ASR | [`meeting-audio-alignment.md`](meeting-audio-alignment.md) | Raw audio and ASR outputs are not included because of size, privacy, and source availability; ASR is not a human-produced verbatim transcript |
| Workshop audio | `Workshop main recording`; SHA-256 `24b5fd98fb9dc426039ea3eac3cc18ce8ba9dbe7074db4ba0e3b6c8ac7718929` | `7997.098667 / 7997.098667s` | direct audio + ASR | [`meeting-audio-alignment.md`](meeting-audio-alignment.md) | Raw audio and ASR outputs are not included because of size, privacy, and source availability; all audio-only content is retained |
| Screenshots | `Workshop screenshot set` (73 PNG basenames; see the index) | `73/73` file index; `73/73` topic-level cross-alignment | direct visual | [`screenshot-index.md`](screenshot-index.md) | Raw screenshots are not included because of size, privacy, and source availability; not a complete deck; topic-level alignment is not verbatim verification |
| Mac Voice Memos ASR | `Mac Voice Memos ASR candidate` | No timestamps | weak ASR candidate | [`meeting-audio-alignment.md`](meeting-audio-alignment.md) | Raw ASR is not included because of privacy and source availability; terminology navigation only; does not override Whisper |
| Qwen OpenRouter STT attempt | `Qwen OpenRouter STT failed-run receipt` | 0 transcripts | failed-run receipt | [`qwen-whisper-asr-comparison.md`](qwen-whisper-asr-comparison.md) | Run artifacts are not included because of privacy and source availability; HTTP 400; cannot be described as successful dual-ASR corroboration |

## 3. Award-Winning Work Evidence

SMA v3 export note (2026-08-18): the Owner-authorized Team 1286 report is now included at [`sources/papers/team-1286-pitrace-report.pdf`](../../../sources/papers/team-1286-pitrace-report.pdf), preserving the audited SHA-256 below. The Team 1286 video, Team 1401 video, workshop recordings, and raw screenshots remain excluded. This private evidence copy asserts no public redistribution right.

| Work | Source identity | Coverage / fixed revision | Observed proof | Not proven | Canonical audit |
|---|---|---|---|---|---|
| Team 1286 / PiTrace | Paper SHA-256 `1114180be5df7c6a00217518b4602c18e51e5cd882bf4f559521819c56b0a572`; Drive ID `10hlBEPLNNRKmeW7t-oAB1yzkLew8SdXU`, video SHA-256 `492976a5e113b9d7aa15f5dca262c9add5986b3d16d102adfeba48348c29b15b` | PDF `23/23`; video `07:58/07:58` | Source graph, groups, node/group detail, `Re-layout`, answer path, and trace | The paper PDF is included in the private SMA v3 export; raw video remains excluded. No confirmed public repo; paper implementation paths are author claims; no complete production causal chain | [`creative-team1286-practices.md`](creative-team1286-practices.md) |
| Team 1401 / Data Agent Studio | Drive ID `1ev10EJT5_yAVItYGCl1wdPRex798Mzng`; SHA-256 `b50c79b6be38c8344e890eefac7f7c15d2bb946dbc471c4f38ed082bd07fbf34` | video `08:32.48/08:32.48`; 0 embedded subtitles | Schema relationship graph, PDF KG, typed edges, clusters, filter, collapse/expand, node detail, page locator, and query/trace UI | No paper/repo/server receipt; page locator is not a verbatim-quote proof; `3-page PDF` vs KG `1 page` remains unresolved | [`creative-team1401-practices.md`](creative-team1401-practices.md) |
| Champion repo | `zhezh/kddcup2026_champion` | fixed SHA `bdc874fc4260e3565ae0dce041728fdf5b376709` | Source behavior for bounded flow, narrow tools, validation/retry/fallback | README `Top1` was not verified against an official leaderboard; interactive graph UI not observed; Terra extractor interrupted | [`champion-repo-reverse-audit.md`](champion-repo-reverse-audit.md) |
| Fourth-place repo | `kekshibata/kddcup2026-data-agents-4th-place-solution` | release SHA `ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a`; Phase 2 commit `13b17fcc7b65d44cd8f8583e2bf6d9497b82cb65` | Phase tools, SQL/validation, experiment lineage, run × task matrix, and trace viewer | Node-edge evidence graph not observed; release and competition image are not identical; the Terra-spawned derivative agent does not count as independent evidence | [`fourth-place-repo-reverse-audit.md`](fourth-place-repo-reverse-audit.md) |

## 4. Local Code References

| Source | Audit identity | Role | Boundary | Canonical audit |
|---|---|---|---|---|
| Local KDD repo | `KDD_Competition` — audit HEAD `7270e3bcc24a039ac458e45caeab7a283c62eca8`; availability: `local source, not included` | Direct source for deterministic checks, bounded retry, selective fan-out, and trace/budget practices | Not the target architecture; lacks complete production change discovery/runtime identity/mapping | [`primary-source-audit.md`](primary-source-audit.md) |
| Old SMA | `.agents/skills/sma/`; audit repo HEAD `28cbbda6e4d4d7f08134952d38433e52d3ee8768` | Read-only oracle/reference | Protected paths are read-only references, not migration targets. Domain assets require independent validation; no legacy runtime import or stage/schema/threshold copy. Direct reuse requires interface, provenance, tests, security, license, source, owner, and access receipts. Self-declared verification metadata is not production authority. | [`primary-source-audit.md`](primary-source-audit.md) |

## 5. External Practice Research

| Area | Canonical artifact | Source families | Planning use |
|---|---|---|---|
| RCA / SEV / causal confirmation | [`rca-sev-causal-confirmation-practices.md`](rca-sev-causal-confirmation-practices.md) | Google SRE, Microsoft ExP, Netflix, Cloudflare, NIST | Candidate contracts for confirmation, counterevidence, multi-cause analysis, rollback/recovery, and human review |
| Enterprise-search experiment failure | [`enterprise-search-experiment-failure-practices.md`](enterprise-search-experiment-failure-practices.md) | Azure AI Search, Google Agent Search, Elastic, OpenSearch, Microsoft/Google IR research | Evidence planes for query mix, ACL/corpus/index, retrieval/rank/render, session, latency/fallback/cache |
| Experiment-analysis agent evaluation | [`experiment-analysis-agent-evaluation-practices.md`](experiment-analysis-agent-evaluation-practices.md) | Microsoft ExP, OpenAI, Anthropic, Google SRE, NIST, agreement/metamorphic-testing research | Blind adjudication, false-cause/patch risk, abstention, stability, latency/cost, and shadow-read evaluation |

Use the `Sources` sections of the three canonical artifacts for complete URLs, access dates, and claim anchors.

## 6. Research Routing Artifacts

| Artifact | Authority |
|---|---|
| [`research-synthesis.md`](research-synthesis.md) | A/B navigation and Adopt/Adapt/Reject synthesis across all research; material claims still route to primary audits |
| [`cross-research-consistency-audit.md`](cross-research-consistency-audit.md) | Conflict audit across facts, author claims, owner decisions, inferences, proposals, and unknowns |
| [`deliverable-readiness-matrix.md`](deliverable-readiness-matrix.md) | Current delivery prerequisite status; not an architecture authority |
| [`greenfield-requirements.md`](greenfield-requirements.md) | Old research draft; not the final spec |
| [`fable-opus-audit.md`](fable-opus-audit.md) | Prior adversarial review and owner-decision ledger; not a fact source |
| [`enterprise-experiment-post-analysis-profile.md`](enterprise-experiment-post-analysis-profile.md) | Supporting requirements profile and enterprise cases; Owner-aligned O1-O6 and the canonical planning packet override older M0-only or M1/M2 direction-only wording, and the profile is not broader product authority |
| [`reviews/2026-08-16-opus5-m0-alignment/owner-alignment-record.md`](reviews/2026-08-16-opus5-m0-alignment/owner-alignment-record.md) | Canonical Owner authority for Flight identity, decision-metric policy, invalid-Experiment remediation, production role separation, the M0-M2 active-time program, and legacy-asset handling |
| [`reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md`](reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md) | Current freeze candidate; becomes implementation-binding only after independent Opus review and a freeze record names its revision and SHA-256 |
| [`deepseek-harness-practices.md`](deepseek-harness-practices.md) | Supporting fixed-artifact research on reuse, collectors, redaction, and diagnostic Trace; verified source SHA-256 `81feaa5e1c2514732707fa542a283162faafa435611f768e6887c8421bb64f52`; not product authority |
| [`reviews/2026-08-15-opus5-enterprise-plan-review/README.md`](reviews/2026-08-15-opus5-enterprise-plan-review/README.md) | Supporting adversarial review bundle from 8 review agents plus 1 image-extraction agent; reviewer proposals are not authority |
| [`reviews/2026-08-15-opus5-enterprise-plan-review/03-codex-disposition.md`](reviews/2026-08-15-opus5-enterprise-plan-review/03-codex-disposition.md) | Reconciliation ledger for all 38 B/M findings, specialist-scoped dispositions, receipt corrections, and remaining gates |
| [`fable-terminal-review-availability-receipt.md`](fable-terminal-review-availability-receipt.md) | Current terminal-review execution receipt; proves the single authorized attempt failed closed before session creation because the runtime blocked Fable; contains no review findings |

## 7. Unresolved Items

- Opening final score: `0.65` vs `0.69`.
- Team 1401 cost: `25c` vs `35c`.
- Exact suffix of the Qwen3.5 model named in the opening talk.
- Team 1401 `3-page PDF` vs KG `1 page`.
- Champion Terra formal extractor was interrupted; this cannot be described as multi-model double confirmation.
- Production authority/access, evaluation adjudication, pilot-calibrated thresholds, and A/B SLA remain owner decisions.
- Live prototype/UI acceptance remains open; it does not reopen the frozen logical Evidence Graph contract, Gate G0–G7 schema, or complete dual-axis enums.

These unresolved items do not prevent use of verified research. They prohibit silently selecting a value or presenting an unknown as fact.
