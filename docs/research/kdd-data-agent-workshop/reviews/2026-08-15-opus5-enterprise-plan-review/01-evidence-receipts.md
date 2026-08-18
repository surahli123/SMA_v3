# Evidence receipts — 2026-08-15 Opus 5 enterprise plan review

Every load-bearing claim in `00-final-review.md` traces to one of the receipts below. All
commands are read-only. Re-run them to reproduce or refute the finding.

Environment note: this session ran under a restrictive Bash policy for part of its life.
`shasum`, `openssl`, `sips`, `python3`, and `git -C` were denied at the time the hash claims
would have been checked, which is why sections 4 and 8 record **coverage gaps** rather than
hash receipts.

**Post-review receipt correction.** The main orchestration task independently verified that all eight screenshot SHA-256 values match the enterprise profile. The raw images and their rehash command are no longer available in this workspace, so no path or command is invented. The final DeepSeek source was verified from the `cd68` worktree with `shasum -a 256` and digest `81feaa5e1c2514732707fa542a283162faafa435611f768e6887c8421bb64f52`; the machine-local absolute path is intentionally omitted from this share-safe artifact.

---

## 1. Repository state at review time

```
git status --short --branch
## codex/kdd-data-agent-practices-research
 M .omc/project-memory.json
?? .agents/skills/sma_rewrite/workspace/
?? .gstack/
?? .workflow/
?? critique.json
?? designs/
?? docs/plans/
?? docs/research/

git log --oneline -1
28cbbda chore: session wrap-up 2026-05-30 — promotion gate slice
```

Consequence for every finding below: **the entire review object is untracked working-tree
content.** `docs/research/` and `docs/plans/` are not represented by HEAD. Document existence
is current-worktree evidence, not committed or published evidence.

Relevant worktrees:

```
git worktree list
<primary-worktree>                 28cbbda [codex/kdd-data-agent-practices-research]
<review-worktree-cd68>             28cbbda (detached HEAD)
<review-worktree-e9b9>             28cbbda (detached HEAD)
<review-worktree-eb76>             28cbbda (detached HEAD)
```

---

## 2. R3 — M0/M1/M2 vocabulary has no downstream presence

```
grep -c -E "M0|M1|M2|FlightReadinessPacket|MetricMovementPacket|WinLossEvidencePacket|ExperimentReadContract" \
  docs/research/kdd-data-agent-workshop/final-architecture-spec.md \
  docs/research/kdd-data-agent-workshop/implementation-sequencing.md \
  docs/research/kdd-data-agent-workshop/eval-acceptance-plan.md \
  docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md

final-architecture-spec.md:0
implementation-sequencing.md:2
eval-acceptance-plan.md:0
2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md:0
```

The two hits in sequencing are an unrelated mermaid node, not milestone coverage:

```
grep -n -E "M0|M1|M2" docs/research/kdd-data-agent-workshop/implementation-sequencing.md
105:  P4C --> M1["Scenario A MVP decision"]
106:  M1 --> B0["Separate Scenario B plan"]
```

This is also an identifier **collision** (finding m8): bare `M1` means "Scenario A MVP
decision" here and "Metric Movement" in the profile.

---

## 3. R4 — win/loss evidence has no architectural home

```
grep -n -i -E "win/loss|win \| loss|side-by-side|\bSBS\b|not_comparable|replay" \
  docs/research/kdd-data-agent-workshop/final-architecture-spec.md
```

Hits exist only for `replay` (lines 103, 167, 366, 367, 369, 372, 531, 618, 669, 671, 704, 710,
712, 740, 770, 787). **Zero** hits for `win/loss`, `side-by-side`, `SBS`, or `not_comparable`.
The `D-search` agent independently confirmed that synonyms
(`query-level|query evidence|winners|losers|regression example`) also return zero.

---

## 4. R5 — the reuse contract is absent, and the assets are protected

```
grep -rn -i "search-relevance-experiment-analysis" docs/
; exit status 1  (no matches)

ls .agents/skills/
sma
sma_rewrite

ls .agents/skills/sma/references/metric_registry/
ai_metrics.md  click_quality.md  search_success_rate.md

ls .agents/skills/sma/references/schema_catalog/
connector_schema.md  search_success_rate_schema.md  templates
```

Against the owner's tech spec (IMG_3695): "the ranking RCA and verdict framework are reused
from `search-relevance-experiment-analysis`" and basis tables are "verified against live
Databricks + Statsig in the sma playbook — reuse that routing."

The `H-verifier` agent additionally found that the plan does not merely omit the reuse — it
prohibits it: `implementation-sequencing.md:151` ("The future implementation must not edit
`.agents/skills/sma/` … These paths are protected references, not migration targets") and
`:167`.

---

## 5. R6 — both newest documents are orphans

```
grep -rln "enterprise-experiment-post-analysis-profile" docs/
; exit status 1  (no inbound references anywhere)

grep -rln "deepseek-harness-practices" docs/
docs/research/kdd-data-agent-workshop/enterprise-experiment-post-analysis-profile.md
```

Confirmed absent from the package's own navigation surfaces:

```
grep -rn -i "post-analysis-profile\|Operating Profile\|post analysis profile" \
  docs/research/kdd-data-agent-workshop/deliverable-index.md \
  docs/research/kdd-data-agent-workshop/README.md \
  docs/research/kdd-data-agent-workshop/wayfinder/map.md \
  docs/research/kdd-data-agent-workshop/cloud-agent-handoff.md \
  docs/research/kdd-data-agent-workshop/source-manifest.md
(no output)
```

**Important fairness note:** the profile declares this itself. Its section 14 states "This
addendum should be reconciled into the canonical package only after review" and lists the nine
required edits; section 15 retracts a prior completeness claim. The legitimate finding is not
"they forgot" — it is that **the reconciliation is unmerged, so the approval object is the
unreconciled package.**

---

## 6. R7 — the trajectory increment exists only in the Codex worktree

```
ls -la <worktree>/docs/research/kdd-data-agent-workshop/deepseek-harness-practices.md
-rw-r--r--  80869  Aug 14 23:03

ls -la <main-tree>/docs/research/kdd-data-agent-workshop/deepseek-harness-practices.md
-rw-r--r--  53020  Aug 14 22:48
```

`diff` of the two copies shows the worktree version is a strict superset apart from trailing
whitespace. The decisive hunks:

```
269c286
< ## 16. Bottom line                                          <- main tree
---
> ## 16. Agent-agnostic Trace across Codex, Claude Code, and Cursor   <- worktree
271c288,390
  (+102 lines: sections 16.1 decision/host boundary, 16.2 TraceEnvelope field table,
   16.3 direct source reuse plan, 16.4 scenario use, 16.5 threat controls and unknowns,
   then section 17 Bottom line)
```

Additional worktree-only content earlier in the file: the dynamic-documentation evidence class,
the three pinned host repository SHAs, the reusable-test paragraph, two mechanism-matrix rows,
and required tests 11-15.

Consequence: the strongest privacy analysis in the package is not present in the tree a
reviewer or implementer would read, and lives in a transient Codex worktree.

---

## 7. R8 — the evaluation plan is blind to M0

```
grep -c -i -E "cuped|sample ratio|sample-ratio|srm|preregistered|underpowered|co-primary|directional_only" \
  docs/research/kdd-data-agent-workshop/eval-acceptance-plan.md                        -> 0
  docs/research/kdd-data-agent-workshop/final-architecture-spec.md                     -> 2
  docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md                     -> 6
  docs/research/kdd-data-agent-workshop/enterprise-experiment-post-analysis-profile.md -> 18
```

The `E-eval` agent additionally found that **no fixture files exist on disk**
(`find docs/research/kdd-data-agent-workshop -iname "*fixture*"` returns zero), so the
evaluation substrate is specified but unbuilt.

Correction carried into the final review: an earlier draft claimed the profile's 25 acceptance
cases had *no* overlap with the eval plan's case classes. The verifier refuted that — cases
#18, #21, #22, #23, #24 do map. The accurate claim is that the **M0-validity and
M2-comparability subset** has no home.

---

## 8. Named production sources are absent from the canonical package

```
grep -rc -i -E "search-relevance-experiment-analysis|Statsig|WHN|Socrates|Switcheroo|QSR|SAIN|Confluence|Databricks|basis.table|layer_id|use_cuped|first_exposure" \
  final-architecture-spec.md            -> 0
  implementation-sequencing.md          -> 0
  eval-acceptance-plan.md               -> 0
  2026-08-12-001-...-greenfield-plan.md -> 0
  wayfinder/production-evidence-authority-intake.md -> 1
  enterprise-experiment-post-analysis-profile.md    -> 6
```

Every one of those source identities is legible in the owner's own tech-spec screenshot
(IMG_3695). P2 is modelled as "all real answers remain unknown"
(`final-architecture-spec.md:669`) while a large part of the source inventory already exists —
hence finding B2b / the P2a-versus-P2b split recommended in section 7 of the review.

---

## 9. Search-domain vocabulary distribution

```
grep -c -i -E "\bACL\b|tenant|corpus|permission-trim|index freshness|connector|click bias|position bias|interleav|zero result|zero-result|query mix|query-mix|offline-online|rerank" \
  final-architecture-spec.md                      -> 31
  implementation-sequencing.md                    -> 10
  eval-acceptance-plan.md                         -> 10
  2026-08-12-001-...-greenfield-plan.md           -> 26
  enterprise-search-experiment-failure-practices.md -> 74
```

The concepts are present in the canonical spec, which is why the `D-search` agent graded most
of them **NAMED-ONLY** rather than ABSENT: named as evidence planes, but with no diagnostic,
no adapter wiring, and no owning implementation unit. Genuinely ABSENT: interleaving,
offline-online gap, per-query win/loss.

---

## 10. P3 prototype receipt — what it does and does not prove

`prototypes/observability-review-surface/build-test.json`:

```
"artifact": "PROTOTYPE / THROWAWAY"
"status":   "pass_with_owner_gate"
"tests": {
  "project_build":  {"status": "skipped", ...},
  "project_lint":   {"status": "skipped", ...},
  "project_tests":  {"status": "skipped", ...},
  ... 17 passing render / interaction / overflow / console / scan checks ...
  "git_diff_check": "pass"          <- unexplained, carries no verifiable meaning
}
"remaining_gate": "Owner live acceptance is pending. ..."
```

Proves: JavaScript parses; four routes render at two viewports; four specific real
clicks/keypresses change `?view=`; no console errors; no CJK or machine-local paths in durable
artifact text. Does not prove: content correctness, reviewer outcome, accessibility, or any
regression guard.

The `E-eval` agent read the prototype source and found a defect the receipt does not cover:
`app.js:124` falls back to `EV-DEP-17` for any non-`EV-` node, so inspecting competing claims
C-09 or C-22 displays validated support belonging to C-17 (finding M17).

Score correction (finding m13): `deliverable-index.md:49` cites "3.6/5, 4.1/5, 4.5/5". The
actual files show baseline 1.8-2.0 (`critique-before.json`), cycle 1 3.7-4.1, cycle 2 4.0-4.5,
**all superseded** by `critique-owner-ai-slop-2026-08-12.json` scoring 2.1 with
`"convergence": {"passed": false, "threshold": 4.0}` and
`"supersedes": "All prior 4.x agent self-scores"`.

---

## 11. Image evidence

Eight authorized read-only HEIC screenshots were supplied outside the repository and were
**not** copied into it. They were converted to JPEG in an ephemeral job scratch directory with
`sips -s format jpeg -Z 1600`, and all eight were opened and read directly by the lead
reviewer, independently of the extraction agent. Transcriptions:
`agent-reports/image-extractor.md`.

| File | Topic (directly observed) |
| --- | --- |
| IMG_3687 | Proposal; two ordered questions; four outcome classes, neutral and mixed highlighted |
| IMG_3689 | Roadmap and milestone contract: question / output / **approval requested** / **status** / entry gate / exit authority |
| IMG_3690 | M0 exit criteria; explicit "Not in M0" exclusions; M1 definition and blockers |
| IMG_3691 | M2 win/loss and the counterfactual-log constraint; M3+ productization (rotated 180 degrees) |
| IMG_3692 | Seven cross-milestone principles |
| IMG_3693 | Seven cross-milestone guardrails; reversal and rescoping table |
| IMG_3694 | Architecture flowchart; check-type chips; two stages labelled **REUSED**; Log + learn loop |
| IMG_3695 | Data sources: WHN primary read, arm join, `use_cuped`, registered-metric caveat, verified basis-table catalog |

**Post-review receipt correction:** the main orchestration task independently verified that the eight SHA-256 values recorded at `enterprise-experiment-post-analysis-profile.md:27-34` match the screenshots. Raw image paths and the rehash command are no longer available in this workspace; the original review-time tool denial is preserved above.

---

## 12. Agent transcript recovery

The reports from 8 review agents plus 1 image-extraction agent in `agent-reports/` were recovered from
`~/.claude/projects/<project>/<session>/subagents/agent-*.jsonl` by extracting each
transcript's longest assistant text message. Verbatim, unedited apart from the provenance
header on `image-extractor.md`, whose report arrived via the message channel rather than its
transcript.
