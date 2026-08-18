# Agent report — `image-extractor` (Sonnet 5)

Role: extraction only, not interpretation. Converted the eight authorized read-only HEIC
screenshots and transcribed what is literally visible.

Provenance note: this report was delivered through the agent message channel rather than
persisted as an assistant message in the agent transcript, so it is reproduced here from the
received message. The lead reviewer independently opened all eight converted images and
verified the transcription; see `../01-evidence-receipts.md` section 3.

Privacy: the raw images are NOT copied into this repository. Only the text observations the
review depends on are recorded here.

---

## CONVERSION REPORT

Method: `sips -s format jpeg -Z 1600 <in>.HEIC --out <out>.jpg` succeeded on all 8 files on
the first attempt (no fallback needed). Output written to the ephemeral job scratch dir.
Originals untouched.

Note on content: these are screenshots of a Google Doc / planning artifact for a "Search
Experiment Deep-Dive Analyzer" — an internal DS tooling proposal (milestone/roadmap doc plus
an architecture flowchart), not a live dashboard or chat thread. No PII, no real experiment
IDs, no secrets visible. Table names and a couple of internal doc titles are legible.

---

## IMG_3687.HEIC

Kind: Doc slide — proposal section, titled "The proposal — what we're building and why".

Text: "The agent answers two questions for a Search experiment, in order: 1. Can we trust
this flight and its metric read? (Flight Readiness — M0) 2. If we can, what explains the
outcome and which examples make it concrete? (Metric Movement — M1; Win/Loss Evidence — M2)."

Body: "Every flight lands in one of four states. The analyzer earns its keep on neutral and
mixed flights — those require the most investigation labor, carry the highest decision risk,
and are the most common source of delayed launches."

Table (2 cols: "Outcome" | "What the team needs"):

- All lead metrics positive | Confirm the read and whether movement matches the experiment's intent.
- All lead metrics negative | Confirm the read; stop or iterate unless the result was expected.
- Metrics neutral (highlighted yellow) | Decide: true null, underpowered flight, offsetting wins/losses, or a segment-specific effect.
- Some positive, some negative (highlighted yellow) | Decide: is the trade-off real, are related metrics coherent, which users/queries gained or lost.

Trailing (cut off): "Today people [manually] checks setup, validates the statistical read,
compares metrics for coherence, inspects slices, forms hypotheses about movement, and hunts
for representative queries to co[nfirm...]"

No IDs / SHAs / tenants / PII visible.

---

## IMG_3689.HEIC

Kind: Doc slide — "Roadmap & milestone contract" table, Google Docs UI visible.

Table columns: M0 — Flight readiness | M1 — Metric-movement | M2 — Win/loss evidence | M3+ — Self-serve

Rows:

- **Question answered**: "Can we trust the setup and primary read?" | "Why neutral/mixed; which trade-offs/segments?" | "Which real queries demonstrate the change?" | "Run it without depending on one analyst?"
- **Output**: Flight Readiness Report | Metric Movement Analysis Packet | Win/Loss Evidence Packet | UI + workflow over validated checks
- **Approval requested**: Build + staffing | Direction only | Direction only | No build approval
- **Status** (status chips): M0 = "CURRENT TARGET" (green); M1 = "BLOCKED ON M0" (yellow); M2 = "BLOCKED ON M1" (yellow); M3+ = "NOT REQUESTED" (gray)
- **Entry gate**: M0 = "Allowlist, source owners, validation flight, Approver named"; M1 = "M0 accepted; metric/data/interpretation contracts confirmed"; M2 = "M1 accepted; query-discovery, SBS, coverage, staffing closed"; M3+ = "Earlier packets accepted on >1 flight; UI owner/cost/scope confirmed"
- **Exit authority**: M0 = "Approver accepts one reviewed report"; M1 = "Approver accepts one reviewed packet"; M2 = "Approver accepts one human-reviewed packet"; M3+ = "Separate productization decision"

Footer text: "The [linked doc] Search Experiment Deep-Dive Analyzer — Metric & Tech Spec owns
the build detail for each milestone."

---

## IMG_3690.HEIC

Kind: Doc slide — continuation, header cut off.

"Exit:" bullets —

- one real flight runs end to end (experiment id -> reviewed report)
- a DS + experiment owner review every prerequisite
- disagreements become explicit failed/missing checks
- unsupported state stays `UNKNOWN`; the Approver accepts it as sufficient to start or block post-analysis.

"Not in M0:" — metric-movement explanation, win/loss evidence, side-by-side, scorecard
replacement, UI, peeking corrections (the M0 report is generated at flight conclusion, not
mid-flight), or multiple-testing adjustments across the allowlist (one decision metric gates
ship/kill; the rest are monitoring metrics that inform but don't gate).

"Milestone 1 — metric-movement explanation (conditional on M0)"

"Explains a neutral/mixed flight across related metrics, defined slices, and named trade-offs
(QSR vs 3P authorized clicks; latency vs relevance)."

Output: a Metric Movement Analysis Packet with ranked explanations, supporting/contradicting
evidence, and open questions for the experiment owner.

Key blockers: freeze metric definitions; ML-UGC table access; join contract; trade-off
contract; slice readability; domain expertise; human-evaluation method.

Bottom cut off: "Milestone 2 — win/loss evidence (conditional on M1)"

---

## IMG_3691.HEIC

Kind: Doc slide (photographed rotated 180 degrees; transcribed correctly below), continuing
Milestone 2/3 detail.

"Milestone 2 — win/loss evidence (conditional on M1)"

"Finds candidate win/loss queries (DSATs incl. the existing validity set; owner hypotheses;
top-position replayed in control) and validates them via the existing SBS surface (Hello
only; trace id or query; links). **The hard part is discovery — Search has no general
counterfactual logs.**"

Output: a Win/Loss Evidence Packet with a human win/loss/unclear/not-comparable judgement.

Key blockers: candidate-query method; counterfactual gap; SBS integration contract; surface
coverage; query/trace join; artifact durability; human reviewer; MLE support.

"Milestone 3+ — productization (directional only)"

"After M0-M2 outputs are accepted on more than one flight, decide whether to fund a
self-serve UI/workflow. Adding Chat requires a separate metric, attribution, and ownership
decision."

Key blockers: repeated validation; product owner; cost/token model; logging; surface scope;
Chat contract.

---

## IMG_3692.HEIC

Kind: Doc slide — "Principles that don't change across milestones" (full list) plus the start
of "Cross-milestone guardrails".

1. **Evidence before explanation** — later analysis never hides a prerequisite warning or blocker.
2. **Incremental metric coverage** — add a metric only when its definition, source, and interpretation check are explicit.
3. **Human-reviewed examples** — the agent narrows and preserves evidence; a domain expert makes the final qualitative call.
4. **Revalidate source changes** — if the source moves from Statsig to the in-house scorecard, recheck metric meaning, coverage, and attribution first.
5. **`UNKNOWN` is a valid result** — missing config, metrics, replay support, or query evidence stays visible.
6. **One decision metric per flight** — if the allowlist contains multiple primary metrics, the report identifies which one gates the ship/kill decision and which are monitoring. Multiple-testing corrections apply only if more than one metric gates.
7. **No mid-flight statistical conclusions** — if the report is invoked before the pre-registered runtime completes, significance verdicts carry a "directional only" label and cannot return PASS on a primary metric.

"Cross-milestone guardrails" section begins, first bullet visible: "Don't start a milestone
because it's on the roadmap; start it only after its entry gate clo[ses...]"

---

## IMG_3693.HEIC

Kind: Doc slide — continuation of "Cross-milestone guardrails" plus start of "Reversal and
rescoping conditions".

Guardrail bullets (full):

- Don't start a milestone because it's on the roadmap; start it only after its entry gate closes.
- Don't hide a prerequisite warning or blocker in a later explanation.
- Don't treat a power result as Search-calibrated while layer/region limits are unresolved.
- Don't turn example ranking or metric trade-offs into an autonomous launch decision.
- Preserve `UNKNOWN` when configuration, data, replay, ownership, or evidence is missing.
- Don't report a fixed-horizon significance result from a flight that hasn't reached its pre-registered runtime.
- Don't treat CUPED-adjusted and unadjusted reads as interchangeable — the report always labels which mode is being presented (per the Tech Spec `use_cuped` flag).

"Reversal and rescoping conditions" table begins (columns: Condition | Response):

- Row 1: "An existing artifact already meets a milestone" | "Add missing checks to it instead of building a [new one...]" (cut off)

---

## IMG_3694.HEIC

Kind: Architecture/flowchart diagram, titled "Search Experiment Deep-Dive Analyzer" —
subtitle: "One pass over a flight: read -> validate -> categorize the root cause -> hand off".

Flow (top to bottom):

1. "Experiment flight" (surfaces: FPS, QF, Jira, Chat (later))
2. "Read the metric" — user-level ratio, per surface (section 1)
3. "Validate the read" — metric present? counts sane? recompute matches? else insufficient-evidence (section 2). Side inputs: "in-house scorecard" (labeled "read not trustworthy") and "Switcheroo config" (labeled "read").
4. "Categorize the root cause" — which kind of problem is it? each = a check -> fired? / strength / evidence. Six check-type chips: Instrumentation, Attribution, Validity, Power, Confounding, Segment, plus a 7th chip "AI-adoption". Caption: "Validity reads Switcheroo. none fires -> log a new-check candidate." Side box "Log + learn / grows checks" feeds back into this step.
5. "Verdict allowed?" — validity ok / result clear / one category dominant; else -> insufficient-evidence.
   - "yes" branch -> "**Ranking-diagnostics RCA**" (**REUSED**) — where ranking moved: connector / rank / region / 1P/3P
   - -> "**Verdict framework**" (**REUSED**) — ship / caveat / extend / iterate / hold
   - -> branches to "ship / iterate / kill" or (on "no / can't validate") "insufficient-evidence"
   - The "insufficient-evidence" terminal node also loops back (dashed line) into "Categorize the root cause".

Footer: "**Steps 1-3 are the DS layer. Ranking RCA and the verdict framework are reused from
the existing skill.**"

Numbered circles "1" and "2" label the "Read the metric" and "Validate the read" boxes.

---

## IMG_3695.HEIC

Kind: Doc slide — technical spec section "1. Data sources", continuing the "One pass per
flight" framing.

Intro: "One pass per flight: read -> validate -> categorize is the new layer (sections 1-3);
the ranking RCA and verdict framework are reused from `search-relevance-experiment-analysis`.
Chat runs the same pipeline once its metric catalog is defined."

**1. Data sources**

"Primary read — Statsig Warehouse Native (WHN)." Table
`production.experimentation_statsig.statsig_daily_results` on Socrates — the official Statsig
read, matching the Statsig UI. Arm rows are keyed by `layer_id`; `use_cuped` selects the
CUPED / non-CUPED read; exposure is per-user (every event from an enrolled user). Refs
(linked text): "WHN training guide", "scorecard<->WHN reconciliation".

"Caveat, encoded as a check: WHN only returns metrics the flight *registered* for — a flight
with QSRv5 but not pd QSRv5 returns only QSRv5; compute the rest from the basis tables below."

"Basis-table catalog (verified)." Relevance metrics are user-level ratios
(`sum(n_u)/sum(d_u)`); tables live under `production.ai_search_analytics.*`, **verified
against live Databricks + Statsig in the sma playbook — reuse that routing.**

Table (Surface | Verified primary table | Arm join | Watch-out):

- Confluence FPS (QSR/SAIN) | `experimentation_events_confluence_search_qsr_v2` | `first_exposure_report` on `unit_id` | "Statsig shows relative %, convert to pp; SAIN needs coverage-vs-success check first"
- Cross-product OKR | `experimentation_even[...]` | same | (row cut off at bottom)

---

## Synthesis (extractor's own, labeled as such)

This is an internal DS/eng planning doc for building a "Search Experiment Deep-Dive Analyzer"
agent — a tool that automates root-cause analysis of Search A/B test (experiment) flights,
replacing manual metric validation and win/loss investigation. The author is proposing a
milestoned build (M0 Flight Readiness -> M1 Metric Movement -> M2 Win/Loss Evidence -> M3+
Self-serve UI) and seeking approval to build **M0 first**, with M1-M3 as "direction only". It
explicitly reuses a component called `search-relevance-experiment-analysis` for ranking
diagnostics and the verdict framework. Data sources reference Statsig, a Databricks-backed
warehouse, and named internal tables/configs. No names of individuals, no live metric values
or p-values, no deploy SHAs, and no tenant/locale specifics beyond the named surface labels.
