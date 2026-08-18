# Greenfield Data Agent Deliverable Index

Status: continuation index; artifact status is explicit and does not imply implementation or production approval

## State as Exported to SMA v3 on 2026-08-18

- The canonical freeze record governs the exact M0 packet and architecture bindings; historical status text inside the frozen files is not current state.
- Round 5 independently accepted local fixture-backed M0 aggregate `9eea3014…b19a`; it did not establish production capability or authorization.
- The recovered Fable 5 v3 architecture artifacts are labelled drafts. Their stale state statements, Coverage Gap registry mismatch, `VAL-*` ownership conflict, terminology drift, and proposed extensions are catalogued in `reviews/2026-08-17-fable5-architecture-finalization/deliverable-alignment-review.md`.
- `.agents/skills/kdd_data_agent/README.md` describes the Phase A foundation; the shipped `m0/` package is the frozen-bound fixture evaluator. Correcting that accepted-package documentation requires a new aggregate and independent review.
- `share-safe-publication-manifest.md` and `publication-verification-receipt.md` record the historical SMA v2 publication. The current repository export is governed by the top-level `PROVENANCE.md`, `COMPLETION_LEDGER.md`, and Git history in `surahli123/SMA_v3`.

## Recommended Reading Order

1. [README](README.md) — scope, status, and package entry point.
2. [Planning decision packet](planning-decision-packet.md) — owner-confirmed product destination and boundaries.
3. [Owner alignment record](reviews/2026-08-16-opus5-m0-alignment/owner-alignment-record.md) — O1-O6 product authority for the one-Flight M0-M2 validation program.
4. [Frozen M0-M2 alignment packet](reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md) and [canonical freeze record](reviews/2026-08-18-m0-canonical-freeze/m0-canonical-freeze-record.md) — exact revision and SHA-256 authority for the bounded local M0 build.
5. [Round 5 independent review](reviews/2026-08-18-m0-f1-f5-correction-round5/independent-review.md) — accepts the exact local fixture-backed M0 package aggregate; external gates remain open.
6. [Final architecture specification](final-architecture-spec.md) — canonical target design.
7. [Implementation sequencing](implementation-sequencing.md) — bounded build order and gates.
8. [Evaluation and acceptance plan](eval-acceptance-plan.md) — threshold-free acceptance, pilots, and hard vetoes.
9. [CE implementation plan](../../plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md) — concrete engineering units and tests.
10. [Wayfinder map](wayfinder/map.md) — resolved contract and remaining human-gated frontier.
11. [Enterprise experiment post-analysis profile](enterprise-experiment-post-analysis-profile.md) — supporting requirements profile; Owner alignment overrides its older scope drift.
12. [DeepSeek harness practices](deepseek-harness-practices.md) — supporting fixed-artifact research on safe reuse and diagnostic Trace boundaries.
13. [Opus 5 enterprise-plan review bundle](reviews/2026-08-15-opus5-enterprise-plan-review/README.md), [Codex disposition](reviews/2026-08-15-opus5-enterprise-plan-review/03-codex-disposition.md), and [M0 alignment review](reviews/2026-08-16-opus5-m0-alignment/opus5-review.md) — review findings, evidence receipts, and reconciliation evidence; reviewer text is not product authority.
14. [Research synthesis](research-synthesis.md) — Adopt/Adapt/Reject conclusions, with material claims routed to primary audits.
15. [Source manifest](source-manifest.md) — source identity, coverage, provenance, and availability boundaries.
16. [Cloud/internal-agent handoff](cloud-agent-handoff.md) — exact continuation rules and safe next steps.
17. [Fable 5 final adversarial review](reviews/2026-08-17-fable5-m0-adversarial-review/fable5-final-adversarial-review.md) — completed historical review that failed closed on changed bytes; its verdict is not transferred to the later frozen revision.
18. [Share-safe publication manifest](share-safe-publication-manifest.md) and [verification receipt](publication-verification-receipt.md) — exact include/exclude set and passed pre-push checks; subsequent publication state belongs to Git history.

## Status Labels

- **Canonical:** current product or delivery authority for its stated concern.
- **Supporting:** evidence or analysis that grounds canonical artifacts but cannot override owner decisions.
- **Operational:** current tracker, prototype, or handoff used to continue work.
- **Historical / non-canonical:** retained for provenance; must not direct implementation.
- **Open gate:** prepared work exists, but named human or pilot evidence is required before closure.
- **Availability-blocked review:** the authorized attempt reached its live gate but no reviewer session ran; the blocker receipt, not an imagined verdict, is authoritative.

## Canonical Product and Delivery Artifacts

| Artifact | Status | Purpose and authority |
| --- | --- | --- |
| [Planning decision packet](planning-decision-packet.md) | Canonical | Owner-confirmed product destination, current fixture-backed M0 boundary, M0-M2 validation program, success criteria, vocabulary, safety boundaries, and open gates. |
| [Owner alignment record](reviews/2026-08-16-opus5-m0-alignment/owner-alignment-record.md) | Canonical product authority | O1-O6: Flight identity, decision-metric policy, invalid-Experiment remediation, production role separation, active-time program boundary, and legacy-asset authority. |
| [M0-M2 alignment packet](reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md) | Canonical, frozen | Exact M0 contract, checks, outcomes, fixture controls, gate map, stop conditions, M1/M2 boundary, and continuity rules. Revision `m0-alignment-v1` is bound by the canonical freeze record at SHA-256 `82747da9…b19`. |
| [Canonical freeze record](reviews/2026-08-18-m0-canonical-freeze/m0-canonical-freeze-record.md) | Canonical execution binding | Binds the packet and architecture revisions plus supporting CE-plan and sequencing hashes for the bounded local M0 build. |
| [Local fixture-backed M0 package](../../../.agents/skills/kdd_data_agent/README.md) | Independently accepted local implementation evidence | Exact 59-file aggregate `9eea3014…b19a`; `370` tests from three working directories; fixture-only, no production adapter or authority. |
| [Round 5 independent review](reviews/2026-08-18-m0-f1-f5-correction-round5/independent-review.md) | Independent local acceptance | Verdict `ACCEPT_LOCAL_M0_EVIDENCE` on the exact aggregate. It does not readjudicate Phase A or promote any production, P2/P3/P4, M1/M2, deployment, publication, or Committee state. |
| [Final architecture specification](final-architecture-spec.md) | Canonical | M0 contract plus planned M1/M2 target components, flows, failure behavior, and product invariants. |
| [Implementation sequencing](implementation-sequencing.md) | Canonical | Current authorized `M0-F0`-`M0-F5` order, exit evidence, and separately gated M1/M2 continuation. |
| [Evaluation and acceptance plan](eval-acceptance-plan.md) | Canonical, threshold-free | Fixture, blind historical, replay, and shadow-read contracts; adjudication, metrics, hard vetoes, and pilot calibration. Numeric thresholds remain open. |
| [CE implementation plan](../../plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md) | Canonical M0 engineering plan | Concrete authorized `M0-F0`-`M0-F5` plan and verification. R1-R37/U1-U13 define the separately gated M1/M2 continuation. Engineering choices remain proposals where the product contract leaves them open. |
| [Closed canonical domain and policy contract](wayfinder/freeze-canonical-domain-policy-contracts.md) | Canonical, closed | Eight orthogonal state dimensions, dual axes, deterministic policy matrix, `G0-G7`, invalidation/recompute, and human responsibilities. |

## Wayfinder and Prepared Gate Assets

| Artifact | Status | Purpose and remaining authority |
| --- | --- | --- |
| [Wayfinder map](wayfinder/map.md) | Operational | Routes resolved decisions and the remaining frontier. |
| [Production evidence authority ticket](wayfinder/establish-production-evidence-authority.md) | Open gate | Cannot close without production owner, Engineering, security/privacy, experiment owner, and relevant on-call/IC evidence-backed input. |
| [Production evidence authority intake](wayfinder/production-evidence-authority-intake.md) | Prepared supporting asset | Inventory template and exact human acknowledgements; it is not an authority decision. |
| [Observability prototype ticket](wayfinder/prototype-observability-first-review-surface.md) | Open gate | Current priority is an M0 packet-centered Flight Readiness review surface. Live owner/reviewer validation is required before interaction behavior or UI framework is accepted. |
| [Evidence Room observability prototype](prototypes/observability-review-surface/README.md) | M1 research prototype | Replaces the owner-rejected A/B/C, Evidence Dossier, and Case Ledger iterations. Its synthetic `Review | Claims | Verify | Trace` workbench remains useful M1 research, but it is not the M0 review artifact and cannot close P3 without an M0 packet-centered prototype and live review. |
| [Prototype HTML](prototypes/observability-review-surface/index.html), [styles](prototypes/observability-review-surface/styles.css), and [interactions](prototypes/observability-review-surface/app.js) | Operational prototype sources | Static synthetic rendering only. Exactly four unified image references cover Review, Claims, Verify, and Trace. The latest owner review panel scored the prototype `2.1` with `convergence.passed=false`. Earlier `3.6/5`, `4.1/5`, and `4.5/5` agent critiques are superseded history, not acceptance evidence. Physical `F1-F4` shortcuts select the four modes. These results do not define canonical state, accepted interactions, review efficiency, or a production UI stack. |
| [Prototype build/test receipt](prototypes/observability-review-surface/build-test.json) | Supporting verification receipt | Static build and equivalent browser, route, responsive, asset, keyboard, syntax, and safety checks passed. Project tests were skipped with the explicit reason that this dependency-free static prototype has no package manifest, build script, or project test runner. This is not P3 closure evidence. |
| [Evaluation gold and calibration ticket](wayfinder/freeze-evaluation-gold-and-calibration.md) | Open gate | Requires blind-case adjudication and pilot evidence before final case set or numeric thresholds. |
| [Evaluation gold and calibration contract](wayfinder/evaluation-gold-calibration-contract.md) | Prepared supporting asset | Threshold-free set-valued gold, adjudication, evaluation ladder, and calibration protocol; not yet adjudicated. |

## Original KDD Workshop and Award-Work Research

| Artifact | Status | Coverage |
| --- | --- | --- |
| [Meeting audio alignment](meeting-audio-alignment.md) | Supporting primary-source audit | Both recordings covered completely; preserves audio-only material and unresolved ASR conflicts. Stored SHA, duration, and 100% alignment receipts remain authoritative for that completed audit, but the expired Voice Memos item-provider paths are not currently available for a live re-read. |
| [Screenshot index](screenshot-index.md) | Supporting primary-source audit | All 73 partial screenshots indexed and aligned at topic level; not a complete deck or verbatim transcript. |
| [Qwen/Whisper ASR comparison](qwen-whisper-asr-comparison.md) | Supporting failed-run audit | Records the OpenRouter HTTP 400 and zero Qwen transcripts; prohibits fabricated dual-ASR corroboration. |
| [KDD source practices](kdd-source-practices.md) | Supporting research | Workshop-level practice extraction and production applicability. |
| [Team 1286 / PiTrace practices](creative-team1286-practices.md) | Supporting primary-source audit | Complete paper/video study, including observed source graph and answer-path interactions. |
| [Team 1401 / Data Agent Studio practices](creative-team1401-practices.md) | Supporting primary-source audit | Complete video study, including observed schema/PDF graph and trace affordances. |
| [Champion repository reverse audit](champion-repo-reverse-audit.md) | Supporting fixed-SHA audit | Bounded flow, tools, validation, retry, and fallback; no interactive evidence graph observed. |
| [Fourth-place repository reverse audit](fourth-place-repo-reverse-audit.md) | Supporting fixed-SHA audit | Phase tooling, lineage, run matrix, and trace viewer; no node-edge evidence graph observed. |
| [Local KDD and Old SMA primary-source audit](primary-source-audit.md) | Supporting source audit | Useful mechanisms and gaps; both are references, not architecture or compatibility constraints. |

## External Practice Research

| Artifact | Status | Coverage |
| --- | --- | --- |
| [RCA/SEV causal-confirmation practices](rca-sev-causal-confirmation-practices.md) | Supporting research | Falsifiability, counterevidence, multi-cause analysis, recovery, rollback, and human review. |
| [Enterprise-search experiment-failure practices](enterprise-search-experiment-failure-practices.md) | Supporting research | Query mix, ACL/corpus/index, retrieval/ranking/rendering, sessions, latency, fallback, and cache evidence planes. |
| [Experiment-analysis Agent evaluation practices](experiment-analysis-agent-evaluation-practices.md) | Supporting research | Blind adjudication, hard risk, abstention, stability, human utility, efficiency, and shadow-read evaluation. |

## Synthesis, Audit, and Review Artifacts

| Artifact | Status | Purpose |
| --- | --- | --- |
| [Research synthesis](research-synthesis.md) | Supporting navigation | Unified Adopt/Adapt/Reject conclusions. It routes material claims to primary audits. |
| [Cross-research consistency audit](cross-research-consistency-audit.md) | Supporting audit | Separates source facts, author claims, owner decisions, reviewer inferences, conflicts, and unknowns. |
| [Source manifest](source-manifest.md) | Supporting provenance authority | Compact source identity, coverage, revision, hash, and availability boundaries. Machine-local paths have been replaced by non-sensitive labels. |
| [Enterprise experiment post-analysis profile](enterprise-experiment-post-analysis-profile.md) | Supporting requirements profile | M0/M1/M2 framing and enterprise cases. Its addendum is unresolved and cannot override the planning packet or canonical specification. |
| [DeepSeek harness practices](deepseek-harness-practices.md) | Supporting fixed-artifact research | Safe-reuse, collector, redaction, and diagnostic Trace evidence. The verified source hash is recorded in the Opus disposition; this report is not product authority. |
| [Opus 5 enterprise-plan review bundle](reviews/2026-08-15-opus5-enterprise-plan-review/README.md) | Supporting adversarial review | Findings from 8 review agents plus 1 image-extraction agent, with evidence receipts. Reviewer proposals are not authority. |
| [Codex disposition](reviews/2026-08-15-opus5-enterprise-plan-review/03-codex-disposition.md) | Operational reconciliation ledger | All 38 B/M findings, specialist-scoped decisions, intended canonical actions, receipts, and remaining owner/external gates. |
| [M0 owner alignment record](reviews/2026-08-16-opus5-m0-alignment/owner-alignment-record.md) | Canonical product authority | Resolves the Owner questions that supersede older reviewer assumptions and scope language. |
| [M0 Opus alignment review](reviews/2026-08-16-opus5-m0-alignment/opus5-review.md) | Supporting adversarial review | Finds C1-C9 and proposes freeze mechanics. Its proposals require Codex reconciliation and Owner authority; it is not itself the frozen packet. |
| [Prior Fable/Opus audit](fable-opus-audit.md) | Supporting historical review | Prior adversarial review and owner-decision ledger; not a primary fact source or terminal review. |
| [Fable terminal-review availability receipt](fable-terminal-review-availability-receipt.md) | Historical availability receipt | Records an early blocked attempt. A later authorized Fable session did run; therefore this receipt must not be used as the current Fable status. |
| [Fable 5 final adversarial review](reviews/2026-08-17-fable5-m0-adversarial-review/fable5-final-adversarial-review.md) | Historical adversarial review | Completed against earlier candidate bytes and returned `BLOCKED` after the review object changed. Its findings informed later corrections, but its verdict does not transfer to the frozen packet or accepted Round 5 package. |
| [Deliverable readiness matrix](deliverable-readiness-matrix.md) | Operational tracker | Final package-readiness and terminal-attempt status, refreshed after the live availability gate. Read its timestamp and current artifacts before trusting its verdict. |
| [Completion matrix](completion-matrix.md) | Operational tracker | Requirement-by-requirement completion audit, refreshed after the blocked terminal attempt. |
| `fable-final-review.md` | Superseded expected filename | The durable later output is the dated `fable5-final-adversarial-review.md` linked above; do not infer absence of a Fable review from this filename. |

## Historical, Non-Canonical Artifact

| Artifact | Status | Rule |
| --- | --- | --- |
| [Greenfield requirements draft](greenfield-requirements.md) | Historical / non-canonical | Retained for provenance only. Do not use it instead of the planning packet, closed policy contract, final spec, sequencing, or CE plan. |

## Continuation and Publication Artifacts

| Artifact | Status | Purpose |
| --- | --- | --- |
| [README](README.md) | Operational | Human and Agent landing page for the package. |
| [Cloud/internal-agent handoff](cloud-agent-handoff.md) | Operational | Branch, scope, read-first order, source boundaries, open gates, and next safe steps. |
| [Deliverable index](deliverable-index.md) | Operational | This complete artifact inventory and reading order. |

## Package-Wide Rules

- M0 Flight Readiness is the first gate and main deliverable. M1/M2 continue the same one-Flight validation program after separate gates and implementation-start receipts; Scenario B is deferred and reuses the shared substrate.
- The Agent is read-only. No verdict, readiness state, approval, evaluation result, or handoff authorizes mutation.
- Award systems and old code are reference evidence only. They impose no compatibility or migration requirement.
- Evidence Graph is a packet projection. Trace is a separate, cross-linked diagnostic store; neither may invent source truth, and Trace is never Evidence.
- Unknown production authority, interaction acceptance, and numeric thresholds remain explicit open gates.
- P2 production authority, P3 live interaction acceptance, and P4 evaluation/calibration remain open; static prototype evidence and local M0 acceptance close none of them.
- Raw private audio, workshop screenshots, private video, credentials, private attachments, and company data are not part of this repository scaffold. Public paper source files may be included only with recorded provenance and redistribution basis.
- Expired temporary source paths create a Coverage Gap for any new live source revalidation. They do not retroactively invalidate the stored fixed hashes, duration receipts, or completed alignment audit.
