# Architecture Review — Truth-Store Separation and the Trajectory Increment

Report complete. Anchors: `spec` = `final-architecture-spec.md`, `dh` = worktree `deepseek-harness-practices.md`, `freeze` = `wayfinder/freeze-canonical-domain-policy-contracts.md`.

---

## ITEM 2 (priority) — TRACE→EVIDENCE LEAK: ENFORCED vs ASSERTED

**Exactly one enforced boundary exists.** `spec:183`: `EvidenceAdmission.evaluate(SourceRead, AdmissionPolicy) -> EvidenceRevision | CoverageGap`. The admission port's input type is `SourceRead`, not a trace event. Backed by `spec:161` ("Tool success alone cannot admit Evidence; zero reads never becomes `observed`") and invariant `spec:118` ("a successful tool call is Trace until evidence admission validates its identity, scope, authorization, freshness, digest, and receipt"). This is a genuine type boundary — but only if nothing else can construct a `SourceRead`. Who may construct one is **ABSENT** — searched §6.1, §6.2, §7.2 (`SourceRead` row, `spec:215`), §14.3.

Every other claimed control is prose:

| Mechanism | Anchor | ENFORCED / ASSERTED |
|---|---|---|
| "a tool trace ... [is not] evidence" | `spec:93` | ASSERTED — non-goal text |
| "A Trace event affects a verdict only through separately admitted Evidence and typed dependencies" | `spec:582` | ASSERTED — states the outcome, names no validator |
| `trace_event --cross_links_to--> source_read\|stage\|failure` | `spec:243` | ASSERTED — `spec:246` requires provenance on `supports`/`contradicts`/`explains` but **never enumerates legal source node types**. Nothing schema-level forbids `trace_event --supports--> claim`. ABSENT — searched §7.2, §7.3, §14.2 |
| "Schema and UI enforce `Trace != Evidence`; gates accept only evidence IDs with source-read receipts" | `dh:234` | ASSERTED — `spec:188` `GateEngine.evaluate(ClaimRevision, DependencySnapshot)` places no membership constraint on `DependencySnapshot` |
| Test 4: "a Trace event without an Evidence receipt cannot satisfy any gate or support edge" | `dh:248` | Test of an unspecified mechanism — and its phrasing leaks: a Trace event *with* an Evidence receipt evidently can. Nothing defines how a receipt attaches to a trace event |
| Trace UI header "Execution Trace — not Evidence" | `dh:357` | ASSERTED — a label |

**The unguarded path is human-mediated, and it reaches Cause=`confirmed`.** `spec:653` places Trace cross-links inside the immutable packet. `spec:547` places a Trace entry point on the fixed first screen. `spec:227` requires `HumanRuling` to carry "evidence citations"; `spec:370` requires the G7 reviewer to "cite Evidence in an explicit ruling." **Nothing constrains a citation to resolve to an `EvidenceRevision` ID.** ABSENT — searched §7.2 (`HumanRuling` row), §8.6, §9 G7. A Causal Reviewer who sees a Trace timeline showing the ranking stage inspecting the right artifact can cite that trace record; the ruling then satisfies `spec:372`'s single path to `Cause=confirmed`. `spec:111` ("Human rulings MUST cite visible evidence") does not help — a Trace record in the packet *is* visible.

Model-narration path is adequately gated: `spec:166` ("model text is a draft until linked and validated") plus G0 (`spec:363`) and G3 (`spec:366`) require Evidence linkage before a claim becomes testable.

**Severity: MAJOR.** **Correction:** (1) Enumerate in §7.3 the legal `(source_type, edge_type, target_type)` triples, with `trace_event` legal only for `cross_links_to`. (2) Type `HumanRuling.evidence_citations` as `EvidenceRevision[] | DerivedFactRevision[] | GateReceipt[]`, validated at submission, rejecting Trace IDs. (3) Add both to the `spec:825` conformance checklist.

---

## ITEM 3 (priority) — COMPETING TRUTH STORE

### 3a. Yes — and the two documents define Trace incompatibly. **BLOCKER.**

`spec:539`: "Evidence Graph, table, timeline, diff, receipt, and **Trace are read-only projections over the same immutable packet**." `spec:840`: "Evidence Graph and Trace are separate, cross-linked **projections over the same canonical workspace**."

Against this, `dh:297` terminates the collector seam in an "**append-only diagnostic Trace store**"; `dh:17` places it "outside the canonical Case Workspace"; `dh:302` feeds it from host hooks, never from the workspace.

A projection *derived* from canonical state cannot contain a fact the workspace lacks. An *independently collected* store structurally can, and the increment's is fed from a completely disjoint source (host lifecycle hooks). `dh:29` cites the spec as governing authority while silently changing its Trace ontology.

### 3b. Precedence on disagreement: **ABSENT.**

Searched `spec` §12 (invalidation), §14, §18 (failure table) — `spec:683` covers "Conflicting identity/mapping/source", i.e. conflicts *between sources*, not Trace-vs-Evidence; `dh` §12, §16.1–16.5 — `dh:375` ("Never infer completion from absence") governs Trace's own gaps only.

**Production consequence:** a reviewer opens a packet where the Trace tab shows a completed query/result retrieval with timing and token counts, and the Evidence tab shows a Coverage Gap reading "zero reads, authority missing." No rule says which governs. The Trace record is the more concrete-looking artifact and carries no "this is not evidence" enforcement beyond a tab label (`dh:357`). This is precisely the failure `spec:680` forbids ("Treat absence as proof") running in reverse.

**Correction:** amend `spec:539`/`spec:840` to state Trace is an independently collected diagnostic store, not a projection; add a §18 row — "Trace and canonical Evidence disagree → canonical Evidence controls; Trace divergence is recorded as a diagnostic anomaly, never as evidence or counterevidence."

### 3c. Unfrozen schema with live downstream dependents: **BLOCKER.**

`dh:386`: "`TraceEnvelope`, its serialization, adapter API, capability-manifest schema, and the observability UI acceptance gate remain unfrozen. The field table is a proposal and cannot be treated as a canonical contract."

Dependents that exist **now**, in frozen documents:

1. `spec:214` — `RunAttempt` carries "Trace references." A canonical workspace entity dereferences into the unfrozen store.
2. `spec:653` — the immutable packet binds "projection manifest and **Trace cross-links**."
3. `spec:655` — "content digest over the immutable manifest."
4. `dh:332` — `case_id`, `case_generation_id`, `run_attempt_id`, `stage_id`, `gate_id` are placed **inside** `TraceEnvelope`, with the doc's own note: "their placement in Trace remains unfrozen." The canonical ID space is shared bidirectionally into an unfrozen schema.

**What breaks.** `event_id` is derived from "pseudonymous source identity, epoch, sequence/offset" (`dh:322`) under a versioned scheme, and pseudonyms come from a keyed transform with its own `pseudonymization_key_version` (`dh:327`). A schema version bump or key rotation re-keys every cross-link. Packet manifests sealed before the bump then reference IDs that no longer resolve — so either every historical packet digest becomes unverifiable, or every packet requires supersession and re-acknowledgement under `spec:493`. Additionally `dh:377` states outright: "Trace retention may be shorter than Evidence retention. **Deleting or rebuilding a Trace projection** cannot delete, change, or invalidate canonical Evidence." So a packet's Trace half can legally vanish while its digest still claims immutability (`spec:841`).

Compounding this: `spec` §6.1 (`spec:156-173`) and §6.2 (`spec:179-193`) assign Trace **no owning component and no port**. The only §6.1 mention is `spec:172`, the *renderer*. An unowned store holds canonical identifiers.

**Corrections.** (1) Either exclude Trace cross-links from the digested manifest and carry them in a separately versioned non-digested annex, **or** freeze `event_id` and require Trace retention ≥ packet retention. Until one is chosen, no packet may be described as immutable. (2) Add a `TraceStore` row to §6.1 with boundary "holds no canonical truth; retains canonical IDs as opaque, unresolvable-tolerant references," and a `TraceStore.append(TraceEnvelope) -> AppendReceipt` port in §6.2, distinct from `Workspace.append`.

---

## REMAINING FINDINGS, SEVERITY-ORDERED

### BLOCKER — Redaction failure has no defined behavior; the collector holds raw transcripts (Q4)

`dh:302` specifies actor, layer, and rule: "The collector/adapter may decode a native event only ephemerally; it must not log or persist the raw object, and prompt/tool/result/path/reasoning bodies are **dropped before `TraceEnvelope` construction**." What is redacted is a deny list (`dh:333`). Verification is canary-based (`dh:259`, test 15). `dh:353` proposes "a strict envelope with closed fields" — a real enforcement shape, but unwritten and unfrozen.

**What happens on redaction failure: ABSENT** — searched `dh` §12 (`dh:230` mandates "structured redaction before log/Trace/packet; secret scanner and deletion proof" with no failure path), §13, §16.1, §16.2, §16.5. Drop / quarantine / halt have opposite consequences: a silent drop manufactures an unexplained gap, which `dh:334` forbids conflating with absence.

**Exact raw-content path:** host hook → collector process → `transcript_path` (Claude Code and Cursor payloads, `dh:307-308`; Codex rollout files, `dh:310`) → collector reads the file (this is the reused `sessions.py` slice, `dh:349`) → raw prompts and tool bodies in collector memory. Controls at `dh:372` bound environment, shell, and output — **not filesystem retention**. `dh:337` then adds a "secured pre-envelope intake receipt" retaining "an authorized integrity digest outside Trace" plus a path where "separately authorized troubleshooting may re-open the original host source under its own ACL and retention policy" — a *third* store and a raw re-open route, both with no named owner, ACL, retention, or approver. Directly in tension with `spec:612`: raw content "MUST NOT enter model context, Trace, logs, packets, errors, caches, **or this repository** unless an explicit future policy authorizes the exact field and path."

**Correction.** (1) Redaction failure fails closed: emit a typed `redaction_failure` envelope with no body, `coverage_status=blocked`, dependent publish gate blocks. (2) Give the secured pre-envelope intake an owner, ACL, retention, and approver, or remove it. (3) Add a collector no-disk-write assertion to §16.5 and a matching §13 test.

### MAJOR — Transcript backfill is fail-open (Q5)

Pinning specified: `dh:306` "Pin the adapter to observed host version"; `dh:310` "source-version-pinned Codex backfill adapter"; `dh:328` collector/adapter digests observed.

Upgrade detection is weak by the doc's own admission — `dh:326`: `host_artifact_digest` is "observed only from a trusted install manifest, **otherwise null**," and "version text is not an artifact digest." On an ordinary developer machine, detection reduces to a self-reported version string.

**Mismatch fail behavior: ABSENT** — searched `dh` §16.1, §16.2, §13 items 11/13/14. The inherited parser is explicitly lossy: `dh:157` "unknown events are ignored, malformed complete lines are skipped with warnings, and an unfinished tail is silently deferred"; `dh:349` requires only "explicit unknown-record **warnings**." `dh:314` claims closure — "absence of a mandatory capture receipt fails closed at the applicable Data Agent workflow or publication gate" — but the publish barrier at `spec:628-638` lists **no** capture receipt among its nine conditions. Composite behavior today: mismatched pin → warnings → packet publishes.

**Correction.** Add "required capture receipts present and adapter pin matches observed host version" to the `spec:628` barrier; specify pin mismatch → adapter emits no envelopes, `coverage_status=unsupported`, dependent gate blocks.

### MAJOR — "Append-only" is API-enforced, not cryptographically enforced (Q7)

Sound and real: `spec:162` "No mutable update/delete API"; `spec:202` every revision records a content digest; `spec:486-493` and `freeze:289-295` give a complete supersession / invalidation / dependency-closure algorithm; `freeze:290` "Human override requires new code-grounded Evidence and a `supersedes` or `invalidated_by` relation. Old records remain"; `spec:227` `HumanRuling` "cannot replace hard Evidence"; `freeze:295` "Closed packets remain immutable. Recomputation creates a new packet with `supersedes_packet_id`." Corrections, invalidation, supersession, and human override are all represented without rewriting history.

Missing: a **digest chain**. Revisions link by ID (`spec:236` `new_revision --supersedes--> old_revision`), not by predecessor digest. `spec:644-655` says the packet binds "included revisions" — identifiers — with digests listed separately only for question/input/policy/schema/authorization/redaction. If the manifest carries IDs rather than `(revision_id, content_digest)` pairs, the packet digest does not cover revision content, and an operator with store access can alter a historical revision's bytes undetected except by that record's own self-digest.

**Correction.** §16.2: the manifest enumerates `(revision_id, content_digest)` pairs. §7.1: each revision records `prev_digest` for its logical ID.

### MAJOR — Licensed reuse: license anchored, "safe" undefined, chain incomplete (Q6)

Verifiable and above average for this class: MIT at a fixed SHA (`dh:343`, `LICENSE:1-21`), `NOTICE:1-18` covering the bundled DeepSeek notice, per-file/line slice boundaries (`dh:345-353`), fork-from-SHA plus auditable patch series.

Absent: (i) **"safe" is never defined** — appears at `dh:17`, `dh:355`, `dh:390` with no test; searched §8, §16.3. (ii) Upstream-of-upstream unanchored: `dh:343` says the UI "already adapts portions of DeepSeek's trajectory component" but names no DeepSeek file, line, or SHA. (iii) No contributor-provenance check on a single-author third-party repo. (iv) No SBOM or dependency license scan for the `protocol.py`/MCP-bridge slice (`dh:352`); `dh:276` acknowledges the missing "signed npm tarballs, package integrity digests, SBOMs" gap for plugins but does not extend it to reused slices. (v) No statement of the Data Agent's outbound license or distribution posture.

**Correction.** Define "safe" as a testable predicate (no network egress, no filesystem write, no reasoning ingestion, no host-steering return value — each mapped to a §13 test); add an attribution manifest listing every copied file with upstream path, SHA, license, and the DeepSeek-derived sub-portion.

### MINOR — Pseudonymization key custody

`dh:325`/`dh:327` require a "tenant-scoped keyed transform" executed at the collector — meaning key material sits inside a hook-launched process on a developer machine. Custody, rotation, and re-identification risk unspecified. `spec:613` defers credentials, secret store, and rotation to the production-authority OPEN GATE, but that ticket's intake does not name a collector-held key. **Correction:** add collector key custody to `establish-production-evidence-authority` before any collector ships.

---

## Q1 — SEPARATION SCORECARD

| Concern | Owner | Schema/contract | Lifecycle | Mutability rule | Verdict |
|---|---|---|---|---|---|
| (a) Trace | **NONE** — `spec:172` names only the renderer; `dh:297` names a store with no owner | Unfrozen (`dh:386`) | Undefined; retention "may be shorter" (`dh:377`) | "append-only" (`dh:297`) but deletable/rebuildable (`dh:377`) | **FAILS all four** |
| (b) Evidence Graph | Projection Renderer, `spec:172` | §14.2, `spec:552-578` | Rebuilt on renderer invalidation, `spec:499` | "Maintains no truth" (`spec:172`); `spec:761` renderer defect changes nothing | **PASSES** |
| (c) Case Workspace | Append-only Case Workspace, `spec:162` | `Workspace.append`/`resolve`, `spec:181-182` | §8.4 case/stage transitions | "No mutable update/delete API" (`spec:162`) | **PASSES** |
| (d) canonical Evidence | Evidence Admission, `spec:161` | `EvidenceRevision`, `spec:217`; states `spec:256` | §8.5, `spec:339-347` | Append-only (`freeze:289`); supersede/invalidate only | **PASSES** |
| (e) deterministic receipts | Gate/Policy Engine + Derivation Engine, `spec:163`,`spec:168` | `GateReceipt` fields `freeze:249`; `spec:223` | Per-gate, §9 | Append-only; `spec:684` no waiver | **PASSES** |
| (f) human packet | Packet and Handoff Service, `spec:171` | §16.2 `spec:644-655` | §16.3 `spec:657-661` | Immutable + supersession | **PASSES structurally, FAILS in fact** — `spec:653` binds Trace cross-links into a deletable, unfrozen store (BLOCKER 2) |

**Shared stores / ID spaces / write paths that permit one to become the other's truth:**
1. Packet ↔ Trace: `spec:653` (cross-links inside the digested manifest).
2. Workspace ↔ Trace: `spec:214` `RunAttempt` "Trace references."
3. Canonical ID space ↔ TraceEnvelope: `dh:332` places five canonical IDs inside the unfrozen envelope.
4. Human ruling ↔ Trace: unconstrained `evidence_citations` (item 2 above).

---

## Q8 — FAIL-CLOSED ENUMERATION

**Closed behavior defined:** missing authority `spec:679`; zero reads `spec:680`; pagination/partition `spec:681`; stale evidence `spec:682`; source conflict `spec:683`; validator failure `spec:684`; permanent authz failure `spec:687`; worker/model timeout `spec:688`; budget exhaustion `spec:689`; material contradiction `spec:690`; human timeout `spec:691`; HIGH risk `spec:692`; security violation `spec:693`; G7 reviewer missing/conflicted `spec:370`; approval expiry on material revision `spec:351`; denial non-disclosure `spec:611`; unknown policy rule `spec:168`; publish barrier `spec:640`; unauthorized/replayed/cross-tenant access `spec:618`.

**Left open:** redaction/secret-scan failure (BLOCKER above); transcript pin mismatch (MAJOR above); missing capture receipt — asserted at `dh:314`, absent from `spec:628`; Trace-vs-Evidence disagreement (BLOCKER, item 3b); pseudonymization key unavailable/rotated; `TraceEnvelope` version mismatch when re-rendering an archived packet (BLOCKER, item 3c).

**Correctly fail-open by design, worth stating so it is not mistaken for a gap:** the host-side collector. `dh:308` records Cursor's `failClosed: false` default; `dh:314` requires the collector to be a neutral no-op that "cannot approve, deny, rewrite a tool call, add model context, stop a turn, or auto-submit another prompt." That is the right choice — a collector that can block the host is a policy boundary, which `dh:314` explicitly refuses. The compensating fail-closed must therefore be the Data Agent capture receipt, which is exactly the control the MAJOR above finds missing from `spec:628`.

---

**Reviewer inference (labeled as such).** The increment's intent is coherent and its per-host limits are unusually well anchored — the Codex/Claude/Cursor coverage caveats at `dh:306-312` are more honest than most vendor-integration designs. The defect is uniform, not scattered: the document consistently specifies *what should be true* and *what to test*, and consistently omits *what happens when the check fires*. All three BLOCKERs are instances of that single omission, and all three are closable by adding failure semantics rather than by redesigning the seam.
