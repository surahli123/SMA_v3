# Toolchain Decision Receipt — keep or replace

Scope: the M0-F0 engineering choice recorded in `ENGINEERING_DECISIONS.md`,
assessed against the three reference implementations already audited in this
repository. This receipt decides engineering, not product meaning.

Sources, all local audits at their stated fixed SHAs:

| Reference | Local audit | Upstream fixed identity |
| --- | --- | --- |
| Champion | `docs/research/kdd-data-agent-workshop/champion-repo-reverse-audit.md` | `zhezh/kddcup2026_champion@bdc874fc4260e3565ae0dce041728fdf5b376709` |
| Fourth place | `docs/research/kdd-data-agent-workshop/fourth-place-repo-reverse-audit.md` | `kekshibata/kddcup2026-data-agents-4th-place-solution@ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a` |
| DeepSeek Harness | `docs/research/kdd-data-agent-workshop/deepseek-harness-practices.md` | `deepseek-ai/deepseek-harness@47f943859bef60e4160492346772ded9b24f765a` |

Every claim below cites the local audit. Independent continuation review also
read the pre-existing pinned local checkouts at the three SHAs above. No
upstream repository was fetched, cloned, or executed, and no upstream code was
copied.

## Recommendation

**KEEP** the current approach. Continue the current implementation; do not start
a second one.

The three references are strongest exactly where M0 is weakest — orchestration
under real workloads — and weakest exactly where M0 is load-bearing: none of
them has an append-only evidence ledger with source-read receipts, and two of
them fail open on the paths that matter most. The current foundation is not
competing with them on capability; it is supplying the substrate all three
audits say has to be built greenfield (`champion-repo-reverse-audit.md:202-214`,
`fourth-place-repo-reverse-audit.md:46`).

Each audit reaches this conclusion in its own words:

- Champion: "**GO as a bounded-mechanism reference; NO-GO as the greenfield
  architecture base.**" `champion-repo-reverse-audit.md:439`
- Fourth place: "not a suitable production foundation," and its own rebuild
  sequence puts **"P0: Build the trust boundary first"** — case schema,
  append-only evidence ledger, capability-enforced read-only tools,
  receipts/digests/freshness/authorization, policy ceilings — ahead of every
  competition mechanism. `fourth-place-repo-reverse-audit.md:44, 556-558, 594`
- DeepSeek Harness: "useful reference … **it is not an enterprise evidence
  system**." `deepseek-harness-practices.md:9`

Phase A *is* that P0 substrate, minus the parts that are alignment-blocked. So
the decision is not "our approach versus theirs"; it is whether to build the
trust boundary in the toolchain we already have, or to port a competition or
harness runtime first and build the same boundary afterwards. The audits argue
for the former.

Replace-triggers are listed in section 3. None fires today.

## 1. Axis-by-axis

### Production integration

| | Assessment |
| --- | --- |
| Champion | Docker is a real execution contract, but it establishes no production runtime identity, artifact attestation, hard readiness gate, or least privilege. Preflight failure does not stop the task; images run under mutable tags, not digests; the runner hardcodes host paths and model URL and emits no runtime receipt. `champion-repo-reverse-audit.md:151-162` |
| Fourth place | The Dockerfile selects the experiment, flags, worker count, step limit, timeout, and retry default that actually ship — a genuinely useful pattern of putting the execution contract in one reviewable place. Still no deployed-identity contract and no production change discovery. `fourth-place-repo-reverse-audit.md:57, 46` |
| DeepSeek Harness | Designed for production agent hosting, but the audit is explicit that it is not an enterprise evidence system: its session log records execution facts, not experiment facts, and its plugin system establishes no tenant authorization or source authority. It is also self-labelled developer preview with breaking changes. `deepseek-harness-practices.md:9, 85` |
| **Current** | Zero production integration by design. `adapters/production/` must not exist before P2 closes and a test asserts its absence. The `ReadAdapter` interface already carries authorization state and Coverage Gaps, so a P2-authorized adapter implements the same protocol rather than widening it. |
| **Verdict** | **Keep.** Production integration is P2-gated, not a toolchain property. Adopting any of the three would import an execution surface we are forbidden to use and would not close a single P2 question. |

### Deterministic behavior

| | Assessment |
| --- | --- |
| Champion | Actively hostile to replay. The attempt loop overwrites `solver.py` and deletes `_schema_shown.flag` and `prediction.csv`; per-attempt messages are logged but there is no append-only evidence. Numeric provenance is model-extracted (`__src_line`), which the audit classes as candidate provenance, not a source-read receipt. `champion-repo-reverse-audit.md:171-181` |
| Fourth place | Has real deterministic portions — no backward stage transitions, tool allowlist, SQL prefix allowlist, shape rules, step/timeout budgets — but retry is coverage retry, not evidence-aware repair, with no failure classification or input invalidation. `fourth-place-repo-reverse-audit.md:348-356, 387` |
| DeepSeek Harness | The strongest of the three, and the source of two mechanisms worth taking. Crash-tail repair deterministically closes an interrupted tool as `TOOL_OUTCOME_UNKNOWN` and never blindly redispatches it. Its own required-test list demands that a fixed ledger plus validator/policy versions produce byte-identical receipts. Against that, compaction shadows the model-visible projection, and `always` retry mode has no attempt ceiling. `deepseek-harness-practices.md:99, 101, 251` |
| **Current** | Byte-stable by construction, and proven: two clean processes under `PYTHONHASHSEED=0` and `12345` produce identical run, log, and build-receipt digests. No clock read, no random identifier, no set iteration reaching serialization, no filesystem-order dependence. Ids are truncated content digests. |
| **Verdict** | **Keep, and adopt two Harness invariants in Phase B** (section 2). The Harness determinism *requirement* is right and already satisfied; its *implementation* carries a compaction-shadowing risk M0 must not inherit. |

### Capability isolation

| | Assessment |
| --- | --- |
| Champion | Narrow solver tools are a good principle, but the audit states plainly that they are not container capability isolation: no non-root `USER`, no read-only root filesystem, no `--network none`, no capability drop, no resource limit, no security profile, and `/logs` at mode 777. `champion-repo-reverse-audit.md:158-159` |
| Fourth place | The default registry exposes no shell or Python tool, and the tool allowlist plus SQL prefix allowlist are real controls the audit says to move server-side with read/write class and auth identity. But the shipped `src` tree contains **114 `python_exec.py` files** — 113 under `src/experiments` plus the baseline copy — that call `exec(code, namespace, namespace)` with full `__builtins__`; the entry point selects the experiment package from the `EXPERIMENT_NAME` environment variable. The audit records that it cannot prove whether a dormant executor was reachable, which is itself the finding: the default path is narrow, the image is not. Also note the SQL control is a string-prefix allowlist only — DuckDB has no per-query read-only mode. `fourth-place-repo-reverse-audit.md:108, 116-117, 120, 343, 353-354, 442` |
| DeepSeek Harness | Rich vocabulary, weak boundary. Monotonic tool guards hold only within one live `ToolRuntime` and the tool service is itself a replaceable plugin, so the audit calls it defense-in-depth, not a security boundary. The sandbox governs filesystem effects only, not network or process visibility; `danger-full-access` bypasses it. Code Runtime and dynamic Cordis packages are explicitly equivalent to Bash access and are rejected outright. `deepseek-harness-practices.md:89, 107, 111` |
| **Current** | Positive allowlist of exactly three capabilities, checked at adapter construction; positive allowlist of thirteen stdlib imports; forbidden builtin, write, dynamic-import, reflection, module-table, ambient environment, wall-clock, network, subprocess, legacy-import, arbitrary-execution, and non-fixture filesystem-read shapes; all enforced by an AST scan over the package's own source, with 46 planted violations proving the scanner fails when it should. `open` is forbidden even for reading, and direct or aliased content reads outside the fixture adapter are rejected. The scanner is static assurance, not a runtime sandbox. |
| **Verdict** | **Keep.** This is the axis where the current approach is strongest, and it is strong for a structural reason: with zero dependencies and zero dynamic execution, there is no plugin tree to escape from and no dormant executor to ship. The fourth-place finding is the sharpest lesson here — a narrow *default path* is not isolation when the *artifact* still contains an arbitrary-code executor selected by an environment variable. That is exactly why the check in this package is an allowlist scan over everything present, not an assertion about the intended entry point. The Harness's own conclusion — put source authorization in a non-replaceable broker outside the plugin composition — is what a dependency-free package gets for free. |

### Testability

| | Assessment |
| --- | --- |
| Champion | No conventional `tests/` suite. `asr/test_remote_whisper.py` is a manual script; `run_compare_to_gt.py` is a scorer, not regression proof. No frozen fixtures for stage transitions, retry/fallback, numeric derivation, read-only bypass, or append-only evidence. `champion-repo-reverse-audit.md:196-200` |
| Fourth place | Top-level `tests/` covers the CSV scorer and CLI evaluation well, and the audit names that coupling — output contract shapes agent behavior — as worth adopting. But no tests were found for stage transition, source routing, forced commit, prose extraction, adaptive vote, or timeout cleanup, so architecture-contract coverage is far weaker than scorer coverage. `fourth-place-repo-reverse-audit.md:409-411, 423` |
| DeepSeek Harness | Tool schemas, guards, and lifecycle invariants are tested, and the local audit adds a 15-item required-test list before any adoption — bundle lock, read-only capability, ACL/tenant, Trace separation, retry/fallback, crash/resume, determinism, compaction, plugin lifecycle, fixtures, host conformance, observational no-op, capture coverage, ordering, cross-host privacy. That list is a better artifact than any of the three codebases. `deepseek-harness-practices.md:245-259` |
| **Current** | 225 cases over 1,769 lines, running in 0.22s with no network, no filesystem writes, and no external service. Digest anchors are SHA-256 of literal byte strings computed outside the package. The suite rejects duplicate JSON keys, reserved-sentinel collisions, and non-finite decode constants; binds every fixture outcome to its manifest; deeply freezes content-addressed inputs and completed results; hard-seals completed logs; correlates adapter results to issued requests; receipts the effective capability envelope; and carries 46 planted capability violations. The earlier nine-mutation self-check remains historical self-authored evidence; this continuation independently reproduced and expanded the adversarial suite. |
| **Verdict** | **Keep, and inherit the Harness required-test list as the Phase B checklist.** Items 2, 4, 7, and 10 of that list already have M0 analogues here; items 1, 3, 5, 6, 8, 9, and 11-15 are either not applicable to a dependency-free fixture-only slice or belong to later milestones. |

### UI integration

| | Assessment |
| --- | --- |
| Champion | No UI in the repository at all. The `L0-L6` graph is a static architecture SVG in an external HTML report that sits outside the audited commit; node click, group/expand/filter, and any timeline or trace renderer are all recorded as **not observed**. The audit also warns that table-schema soft collapse must not be presented as graph UI, and that the edge taxonomy must not be flattened. `champion-repo-reverse-audit.md:316-320, 369-383` |
| Fourth place | Better than the champion, and better than a first pass suggests: `scripts/trace_viewer_v2.py` is a read-only run × task matrix with filters by run id, status, tag, lever, and configuration text; clicking a run opens detail; clicking a task opens `overview \| input \| trace \| output \| raw` tabs; the trace tab lists steps in attempt order with phase, action, `ok`, input, and observation, plus a toggle for thought display and a live auto-refreshing step log. What is absent is a node-edge evidence graph. Note also that none of this ships in the Docker image. `fourth-place-repo-reverse-audit.md:236, 246-250` |
| DeepSeek Harness | The best available reference, via Codex Trajectory: read-only projection, privacy-reduced summary by default, full detail opt-in, no network calls, symlink and path confinement, stable original indices, and a warning channel for parse damage. Its interaction patterns (turn grouping, filters, keyboard-accessible inspector, timeline selection) are explicitly reusable. Two hard constraints: the projection is never the canonical evidence schema, and reuse must retain the MIT copyright notice. `deepseek-harness-practices.md:155-161` |
| **Current** | No UI at all, deliberately. The first-screen hierarchy is `SEAM-M0-07` and live review acceptance is P3-gated. |
| **Verdict** | **Keep (no change now), and take the fourth-place trace viewer as the reference shape for a later Trace surface** — filterable matrix, click-through detail, per-step attempt order — alongside the Codex Trajectory pattern of safe default, opt-in detail, path confinement, and explicit parse warnings. Both are *Trace*, strictly separate from the packet projection. The M0 review surface is packet-centered and is not a trajectory viewer, and no reviewer conclusion may resolve to a trace record. |

### License

| | Assessment |
| --- | --- |
| Champion | Unestablished. The word "license" does not appear anywhere in the 455-line audit — an absence, not an oversight. Do not reuse its code. |
| Fourth place | MIT. The fixed release commit message is `Public release: results README, MIT license`. `fourth-place-repo-reverse-audit.md:66` |
| DeepSeek Harness | Not established in the local audit for the harness itself. Codex Trajectory is MIT (`LICENSE:1-21`), so its source may be copied and modified rather than only imitated — but because its UI already adapts parts of DeepSeek's trajectory component, substantial reuse must retain **three** things: the Codex Trajectory copyright/license, its `NOTICE`, and the bundled DeepSeek MIT notice. The audit's required method is to fork from the fixed SHA, record copied-file provenance, and carry local changes as an auditable patch series. `deepseek-harness-practices.md:161, 345` |
| **Current** | Zero third-party code and zero dependencies, so nothing is inherited and nothing must be attributed. Python and pytest were already present in the repository. |
| **Verdict** | **Keep.** The controlling rule is `implementation-sequencing.md:45`: any direct component reuse requires an explicit interface, provenance, test, security, and license review, and local visibility is not copying authority. This receipt reuses *mechanisms described in our own audits*, never upstream source, which keeps the license surface empty. |

### Migration cost

| | Assessment |
| --- | --- |
| Champion | Migrating its video and document heuristics would invite overfitting; its contest constants reflect leaderboard tuning, not A/B risk policy. Its own verdict is unambiguous: **"GO as a bounded-mechanism reference; NO-GO as the greenfield architecture base."** Its build is the more reproducible of the two competition entries — `uv sync --frozen --no-dev --no-install-project` — but the image still runs under mutable tags rather than digests. `champion-repo-reverse-audit.md:129, 145, 156, 231, 439` |
| Fourth place | Its 181-package experiment lineage is valuable as *research* input for sequencing and evaluation design, not as code to import. Its build is less reproducible than the champion's: the base image is not digest-pinned, apt packages are unpinned, and although `uv.lock` is copied, installation uses `uv pip install --system -e .` against `>=`/unconstrained dependency ranges rather than `uv sync --frozen`. Most usefully, its own section 15 sequences the rebuild as **"P0: Build the trust boundary first"** — case schema, append-only evidence ledger, capability-enforced read-only tools, receipts/digests/freshness/authorization, and the policy-ceiling engine — before competition voting, domain prompt cards, or heuristics. `fourth-place-repo-reverse-audit.md:124, 424, 556-558, 594` |
| DeepSeek Harness | Adopting it means a TypeScript/Node runtime, a plugin tree, and a developer-preview API the audit says must not become a stable enterprise contract without a compatibility adapter and pinned conformance suite. That is a large cost paid before the first M0 check exists. `deepseek-harness-practices.md:85` |
| **Current** | Cost of leaving: 2,365 lines of runtime source across 19 modules; the canonicalizer, digest helpers, deep-freeze helper, and append-only log are the only non-trivial algorithms; the 1,769 lines of tests port as behavioral specifications. Cost of staying: none paid up front, and the language commitment stays reversible because semantics live in enums, frozen records, and canonical JSON. |
| **Verdict** | **Keep.** Replacing now would spend the entire M0 budget on a runtime port while the product semantics are still unfrozen — the exact failure the alignment gate exists to prevent. |

## 2. Winning mechanisms reused, including across languages

| Mechanism | Source | Original language | Status here |
| --- | --- | --- | --- |
| Orchestration owns stage order in code, not the model | Champion `:220`; Fourth place `:441` | Python | **Reused.** `runner/hermetic.py` fixes the order; no model participates. The full stage machine is Phase B (M0-F3), and it must not repeat the fourth-place defect: rejecting only *backward* transitions lets a forward skip bypass the gate it was meant to pass (`fourth-place-repo-reverse-audit.md:372`). Phase B allows explicitly named adjacent transitions only. |
| Narrow, explicitly scoped tool surface | Champion `:221`; Fourth place `:442` | Python | **Reused and hardened.** Three capabilities total, checked at construction; the adapter's public surface is six names. |
| Deterministic structural checks, extended beyond shape | Champion `:225` | Python | **Reused.** Fixture validation is strict and fail-closed; unknown fields, unknown enum values, and contradictory states are errors. |
| Retry isolates the failed unit and preserves history | Champion `:227` | Python | **Partially reused.** History is append-only and corrections supersede rather than overwrite. There is no retry loop yet — see gap G-1. |
| Output contract shapes behavior; one shared scorer | Fourth place `:423` | Python | **Deferred.** Which contract, and which baselines, are `SEAM-M0-05` and `SEAM-M0-08`. |
| Preserve failed experiments and compare them with one scorer | Fourth place `:42, :424` | Python | **Deferred to Phase B**, and named so it is not lost. |
| Interrupted work closes as `unknown` and is never blindly retried | DeepSeek Harness `:99, :186` | TypeScript | **Adopted as a rule now, mechanised in Phase B.** `UNKNOWN` is a first-class singleton whose `bool()` raises, so an interrupted or unestablished value cannot be silently defaulted. Crash-tail resume itself is gap G-1. |
| Monotonic deny in a non-replaceable boundary | DeepSeek Harness `:183` | TypeScript | **Adopted structurally.** With no plugin tree and no dynamic import, the allowlist has nothing to be replaced by. |
| Fail-closed approval: only an explicit grant counts; missing, throwing, or invalid answers deny | DeepSeek Harness `:89, :184` | TypeScript | **Adopted at the read layer.** Only `AuthorizationState.AUTHORIZED` may carry a body; `unknown` and `not_evaluated` are distinct and neither is a pass. |
| Fixed ledger plus versioned validators produce byte-identical receipts | DeepSeek Harness `:251` | TypeScript | **Adopted and demonstrated.** Cross-process digest equality under two hash seeds. |
| Append-only canonical ledger, never summarized or shadowed | DeepSeek Harness `:97, :196` | TypeScript | **Adopted.** `RevisionLog` exposes no update or delete path; corrections append and supersede. |
| Trace ≠ Evidence | DeepSeek Harness `:234, :248` | TypeScript | **Adopted by omission.** No trace store exists, and nothing narrative can reach a receipt: a receipt requires a source identity, an authorization state, and an interval. |
| Read-only projection with safe default and explicit parse warnings | Codex Trajectory, via DeepSeek Harness `:155-161` | Python | **Deferred to `SEAM-M0-07`**, with the MIT attribution requirement recorded now rather than discovered later. |
| Reject dynamic/model-authored code, ambient credentials, cross-case memory, workspace rewind | DeepSeek Harness `:193-195, :263-267` | TypeScript | **Adopted.** `eval`, `exec`, `compile`, `__import__`, `open`, and every mutation call shape are forbidden and mechanically checked. |

## 3. Gaps and replace-triggers

Named gaps, stated rather than hidden:

- **G-1 — no crash/resume semantics.** The runner is single-shot and in-memory,
  so there is no interrupted-run repair, no idempotency class, and no resume
  gate. The Harness rule (close as `unknown`, never blindly retry) is adopted in
  vocabulary but not yet mechanised. Owner: Phase B, after `SEAM-M0-05`.
- **G-2 — no budget or ceiling accounting.** Per-case token, cost, wall-clock,
  source-read, and retry budgets do not exist. Blocked on the Owner's M0 sizing
  answer (`SEAM-M0-10`), which is also what makes "the slice exceeds its budget"
  a real stop condition rather than a wish.
- **G-3 — no Trace projection and no review surface.** Deliberate; `SEAM-M0-07`.
- **G-4 — static capability assurance only.** The continuation hardening removed
  `importlib` from both runtime and test allowlists and added alias, reflection,
  module-table, ambient-home, clock/reference, relative-legacy-import, and
  filesystem-read probes. The scanner now rejects the ordinary and aliased
  bypass corpus, including builtin recovery through allowed modules, but it
  remains source analysis rather than an OS/runtime sandbox. A future
  generated-code or extension mechanism would require a separate
  non-replaceable runtime boundary; none exists or is authorized in this
  fixture-only package.

Replace the current toolchain if, and only if, one of these fires:

1. The frozen packet requires a runtime capability the standard library cannot
   provide without adding a dependency — and the dependency cannot be replaced
   by a fixture at the adapter seam.
2. Cross-language digest agreement becomes a requirement, *and* replacing
   `core/canonical_json.py` with an RFC 8785 implementation is insufficient.
3. The accepted review surface (P3) forces a runtime that cannot call into a
   Python packet producer.
4. A named Owner or Engineering decision selects a different implementation
   language for the funded slice.

Absent one of those, the standing instruction holds: continue the current
implementation, and do not begin a second one unless the alignment session
explicitly rejects this approach.
