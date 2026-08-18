## PART 1 — SEQUENCING EXECUTABILITY

### 1. The safe first slice

**Docs observed.** `implementation-sequencing.md:203-218` (U2) — "Traverse frozen intake → one admitted fixture Evidence revision → one scoped Cause Claim → deterministic policy result → immutable partial review packet… Exclude production access, model fan-out, UI framework." Exit: "one hermetic command proves the end-to-end object seam." Plan mirror: `2026-08-12-001…plan.md:435-447`.

Yes — U2 is a genuinely safe, zero-production, fixture-backed slice. Inputs: U1 contract encodings + one fixture Evidence revision. Exit evidence: `SKEL-001`–`SKEL-004`.

**Reviewer inference — checkability is 3-of-4.** `SKEL-001` (digest reproducibility), `SKEL-002` (missing authority → Coverage Gap), `SKEL-003` (Trace ≠ Evidence) are mechanically checkable. `SKEL-004` — "no code path exposes source writes, arbitrary file writes, external publication, or production mutation" (`:216`) — is an unbounded universal negative. **MAJOR.** Consequence: the one test that guards the entire read-only claim is the one that cannot pass or fail deterministically. Correction: restate as a positive capability allowlist — "the capability registry enumerates exactly N read methods; a denied-write attempt per method emits a policy receipt; import-graph assertion that no write/network/subprocess symbol is reachable from the package root." That is testable; the current wording is not.

### 2. Unit table

| Unit | Depends on | Prod access? | Entry specified? | Exit evidence checkable? | Anchor |
|---|---|---|---|---|---|
| D0 | P1 closed | No | Yes | **No — document.** Exit is "a reviewed decision record" | `seq:171-179`; `plan:401-412` |
| U1 | D0 | No | Yes | Yes — `POL-001`…`POL-009` | `seq:181-201` |
| U2 | U1 | No | Yes | Mostly — `SKEL-004` not checkable | `seq:203-218` |
| U3 | U2 | No | Yes | Yes — `EVD-001`…`EVD-005` | `seq:220-236` |
| U4 | U3 | No | Yes | Yes — `REV-001`…`REV-005` | `seq:238-254` |
| U5 | U3 | No (pre-P2) | Yes | Yes — `ADP-001`…`ADP-005` | `seq:256-272` |
| U6 | U3–U5 | No (fixtures) | Yes | Yes mechanically; **fixtures unvalidated** | `seq:274-291` |
| U7 | U1–U6 | No | Yes | Yes — `ORC-001`…`ORC-006` | `seq:293-310` |
| U8 | U1–U7 | No | Yes | Yes — `A-001`…`A-008` | `seq:312-331` |
| U9 | U4, U8 | No | Yes | **Contradictory** — see below | `seq:333-350` |
| U10 | U1–U8 | No | Yes | Yes — `EVAL-001`…`EVAL-008` | `seq:352-371` |
| U11 | **P2** + U3–U8 | **Yes** | Yes, hard, named | Yes — `PROD-001`…`PROD-006`; **no load/abort/halt-authority** | `seq:373-390` |
| U12 | **P3** + U9 | No | Yes | **Prose only** — no test IDs at all | `seq:392-398` |
| U13A | P4-rung + U10 | Archival snapshot | Yes, very hard | Receipts (checkable as artifacts) | `seq:400-406`; `plan:620-639` |
| U13B | **P2** + U11 + P4 | **Yes** | Yes | Receipts | same |
| U13C | **P3** + U12 + P4 | No | Yes | Receipts | same |

**Document-not-test exits — flagged:** D0 (`seq:179`), U12 (`seq:398` — the entire final review contract has zero enumerated test IDs in sequencing, though `plan:612-618` supplies five), and U9's exit "a synthetic prototype and technology-neutral state/interaction matrix are **ready for owner/reviewer review**" (`seq:350`) — readiness for review is not evidence.

**BLOCKER — U9's `UI-001` is unsatisfiable at U9.** `seq:343`: "`UI-001`: the primary Claim reaches exact target proof and validator receipt **through the P3-approved interaction contract**." U9's entry says "P3 may still be open" (`seq:335`) and its exit says "Final interaction acceptance remains open" (`seq:350`). A required test depends on an approval the unit is defined to precede. The CE plan already fixed this — `plan:559` reads "through a technology-neutral synthetic prototype path; final interaction acceptance remains U12 work after P3 closes." **Correction:** replace `seq:343` with the plan's wording; sequencing is stale relative to its own downstream plan.

### 3. Critical path reality

Gate-blocked: U11 (P2), U12 (P3), U13B (P2+P4), U13C (P3+P4). Unblocked: D0, U1–U10, U13A-offline.

**Docs observed — the plan is honest.** `seq:408-421` is an explicit "what can start before P2/P3/P4" table with four `No` rows, and `seq:422`: "No open prerequisite may be closed by repository inference, a model opinion, a prototype screenshot, or a mechanically green test." `cross-research-consistency-audit.md:91-97` enumerates the illegal conflations. This is better gate hygiene than most enterprise plans.

**MAJOR — but the honesty is about authority, not about validity.** The product thesis is "ranking **production-grounded** candidates" (`plan:16`). Every mechanism that delivers that — deployed-SHA binding (`ANA-003`), exact-target blocking (`ANA-004`), `scope × interval × rollout` matching (U6), the eight-stage flow's `production_identity_and_scope` stage (U8) — is built in U6/U8 against fixtures the plan itself forbids validating: "No test or documentation claims production fidelity" (`seq:272`). So U6–U8 are ~60% of the pre-gate build, are byte-stable against invented inputs, and P2 closure can invalidate their input shape wholesale. `seq:433` and `plan:677` acknowledge this ("supersede that engineering proposal before further expansion") but the ordering still invites a team to build the full matcher before knowing what a deploy record looks like. Correction: U6 pre-P2 should be scoped to the *interfaces and the unknown-authority failure paths* (`ANA-004`, `ANA-003` conflict retention), with the matcher's feature set deferred to a post-P2 U6b. Say so explicitly rather than leaving it to a failure-recovery row.

### 4. The one authorized production path

**Docs observed.** Exactly one read path is defined: U11, "one least-privilege read-only adapter and one deployed-target mapping" (`seq:377`), with `adapters/production/` marked "**forbidden before P2 closes**" (`seq:136`). Entry is hard and named: "P2 is closed with named source, mapping, security/privacy, retention/redaction, credential, and incident-handling authority… **This entry gate is mandatory**" (`seq:375`). Exit: "Do not fan out to more sources until this seam passes human and security/privacy review" (`seq:390`). Reads are **not** diffuse across units.

**BLOCKER — the exit side is a correctness contract, not an operational one.** `PROD-001`–`PROD-006` cover identity, secrets, receipts, conflict, authority gaps, and revocation. **ABSENT — searched `implementation-sequencing.md`, the CE plan, `cross-research-consistency-audit.md`:** (a) rate/QPS/byte/row limits on the production adapter; (b) blast-radius limits (max rows, max tenants, max time range per case); (c) runtime abort triggers (what source-side signal stops a run in flight); (d) a **named halt authority** for U11 itself. The nearest text is the development-checkpoint row `seq:435` ("Security, ACL, tenant, or credential leak | Hard stop; revoke affected development access as directed by security/privacy") — that is a post-incident dev-process rule, not a runtime kill switch with an owner. "Source load" appears only as a *measurement* in U13 (`seq:404`) and as a shadow-read authorization field (`plan:624`), never as a U11 ceiling.

Correction: add `PROD-007` (per-case and per-window read ceilings; exceeding one aborts the run and emits a Coverage Gap, never a partial-as-complete Evidence), `PROD-008` (named on-call halt role with a tested disable path that leaves preserved Evidence intact — `PROD-006` tests revocation from the source side, not halt from ours), and a blast-radius clause in the U11 entry criteria alongside the P2 authority list.

Precise note: one **adapter**, three **exposure modes** — U11 authorized read, U13B production-like replay, and narrow shadow-read. Each carries its own authorization (`seq:402`; `plan:386`), which is correct, but the docs never state that the U11 ceilings bind the other two. They should.

### 5. Sizing

**ABSENT — searched both primary docs for `estimat|effort|week|day|sprint|size|person-`: zero hits.** No unit carries a size, and no unit is decomposed into startable tasks. A team could start Monday on **U1 and U2 only**, because their required tests are enumerated and their inputs are internal.

Research projects wearing unit costumes:
- **U6 `mapping.py` / deploy→SHA mapping** (`seq:274-291`; `plan:496-511`). Establishing which system authoritatively answers "what SHA served this tenant at this hour" is an organizational discovery problem gated on P2, not an algorithm. Pre-P2 this unit can only build the *unknown* branch honestly.
- **U3 `EVD-003` transitive authorization** — "the intersection of permissions and the strictest handling label" (`seq:233`). Permission-lattice semantics come from P2. Pre-P2 this is a fixture-defined toy whose real shape is unknown.
- **U9** (`plan:558-568`) — ten scenarios spanning graph/trace projection, a twelve-state matrix, full keyboard/AT accessibility, and eight authorization/anti-enumeration behaviors. That is a product surface, not a unit.
- **U13** — a multi-rung evaluation *program* with sealed authorizations and four named human roles, labeled "one implementation unit" (`seq:109`).
- **U11** — an authorization negotiation plus an adapter.

### 6. Is the first slice the right one? — recommendation

Yes in shape, wrong in size. **U1 as written is the risk**, not U2: `POL-001` requires "every Cause Verdict × Recommendation Readiness pair has one deterministic legal/conditional/illegal result **and rationale**" (`seq:191`) — 25 pairs, each crossed with gate ceilings, reopen rules, and nine `POL-*` obligations, before a single line of the skeleton exists. That is a contract-authoring project in front of the walking skeleton, which inverts the plan's own stated principle ("not a large horizontal build," `seq:39`).

**Recommend as slice 1: D0 + a vertical U1′ + U2.** U1′ encodes only (a) the closed enums as total functions that fail closed on any un-enumerated pair, (b) the exact matrix cells traversed by the skeleton path, and (c) `POL-004` (fail-closed) and `POL-005` (`confirmed` impossible without receipts). The remaining matrix cells land in U1″ alongside U7/U8, when there is a consumer to prove them against. Deliverable: one hermetic command producing a byte-stable packet digest, plus the `SKEL-004` replacement from §1.

**Stop conditions:** (1) the fail-closed default is ever bypassed by an enum alias or a default branch — stop, return to U1′; (2) any file appears under `adapters/production/` — hard stop; (3) any test requires a network socket, a secret, or a path outside the package — hard stop; (4) the packet digest is not byte-stable across two clean runs — stop, no unit advances; (5) the slice exceeds its budget without a green hermetic command — stop and re-scope, do not start U3.

---

## PART 2 — TRANSFER BOUNDARY AUDIT

| Source family | Docs' verdict (anchor) | Evidence identity | Cargo-cult risk | Production control the source cannot supply |
|---|---|---|---|---|
| **KDD workshop practices** | Mixed Adopt/Adapt/Reject; "Adopt/Adapt/Reject is not an owner decision" (`research-synthesis.md:36`); constants **Reject** (`:177`) | Hashed audio (SHA-256 `2adf77…`, `24b5fd…`) + 73 hashed screenshots (`source-manifest.md:20-22`) — **fixed artifacts, author-claim content** (speaker statements, non-verbatim ASR) | Low — the docs pre-emptively reject stage names, constants, scores (`research-synthesis.md:268-272`) | Everything: no ACLs, tenants, deploy identity, on-call |
| **Champion repo** | Adopt principle ×4, Adapt ×4, **Reject** ×5 incl. hard doc-relevance deletion, best-effort fallback, README-as-validation (`champion-repo-reverse-audit.md:216-232`) | **Fixed SHA** `bdc874fc…` (`source-manifest.md:32`) — strongest class | Low. Bounded stages + narrow tools carry an enterprise re-derivation requirement | ACLs, deployed identity, tenants, rollback |
| **Fourth-place repo** | Adopt directly ×5, Rewrite ×5, **Reject** ×5 (`fourth-place-repo-reverse-audit.md:464-486`) | **Fixed SHAs** `ae0f2baa…` release + `13b17fcc…` Phase 2 (`source-manifest.md:33`) | Low. Its own audit documents the prefix-check SQL sandbox and unbounded `fetchall()` as production-unsafe (`:300-340` region) | Same |
| **Team 1286 (PiTrace)** | P1/P2/P5–P8/P10/P14 **Adapt**, P3/P4/P11/P12 **Adopt**, P9/P13 **Reject** (`creative-team1286-practices.md:49-193`) | Hashed PDF + hashed video; **"No confirmed public repo"** (`source-manifest.md:30`) — artifact hashes fix the *file*, not the *system*. Practice claims are **author claim** | **MEDIUM.** P1 "shared replayable evidence state" is Adapted into the U3/U7 substrate, but `seq:220-236` (U3) cites no source and carries no author-claim label | Server-side enforcement, ACL, deploy identity, tenancy |
| **Team 1401 (Data Agent Studio)** | Adopt node-click/locator/collapse/filter/zoom; Adapt navigation; **Reject** KG-as-backbone, dashed joins, page-pointer-as-quote (`creative-team1401-practices.md:419-423`) | **One 8:32 video**, SHA `b50c79b6…`; "No paper/repo/server receipt; UI does not prove backend enforcement" (`source-manifest.md:31`) | **HIGH.** An "Adopt" list of UI affordances derived from a single demo video of a system whose backend is explicitly unproven, feeding U9's ten-scenario surface | ACL enforcement, freshness, runtime identity, validators — its own §7.5 marks all of these "**Not observed**" |
| **DeepSeek Harness** | §10 matrix: Adopt-invariant ×2, Adapt ×7, **Reject** ×3 (`deepseek-harness-practices.md:182-199`); §14 explicit rejections (`:263-271`) | **Fixed SHA** `47f94385…` plus pinned Codex/Claude/Cursor snapshots; hook behavior is **mutable dynamic docs, captured 2026-08-14** (`:59-61`) — correctly labeled | **HIGH — §16 `TraceEnvelope`.** A 15-field envelope + three host adapters + capability manifest + Codex backfill fork, self-labeled "unfrozen engineering proposal" (`:302`) with six open unknowns (`:379-386`). It maps to **no unit ID in D0–U13 and no requirement in R1–R37** | Source authority, tenant ACL, causal correctness — its own gap list says so (`:280`) |
| **Old SMA** | Reject ×8 with `file:line` (`primary-source-audit.md:205-216`); reference-only, protected path (`seq:167`) | **Repo HEAD** `28cbbda…` + line anchors (`source-manifest.md:40`) — locally re-derivable, strongest of all | None. Explicitly not a migration target (`plan:174`, `plan:390`) | n/a — it is the counterexample |
| **Local KDD code** | Reject task routes, `n_votes=3`, thresholds, scorer contract (`primary-source-audit.md:210-213`) | HEAD `7270e3bc…`, **"local source, not included"** (`source-manifest.md:39`) | None | n/a |

**Credit where due:** `plan:168` states as `source_fact` that "**No audited work proves the complete production causal chain**," and `cross-research-consistency-audit.md:142` repeats it. No family is treated as mandatory legacy architecture, and none is used as production proof. The transfer boundary is, in the main, correctly drawn.

### My corrected verdicts (where I disagree)

1. **DeepSeek Harness §16 `TraceEnvelope` → Reject for the Scenario A MVP; defer to a post-P3 proposal.** Docs say Adapt (`deepseek-harness-practices.md:190-191`). A cross-host trace-collection subsystem with no unit, no requirement, no gate, and six self-declared unknowns is scope arriving through a research door. Adopt only the §13 *tests* (Trace≠Evidence, crash-tail unknown, no-blind-retry) into U7/U9, which they already fit.
2. **Team 1401 → Adapt-with-P3-gate, not Adopt.** `creative-team1401-practices.md:419` lists node-click/filters/zoom as **Adopt**. Single-video evidence with unproven backend cannot carry an Adopt label into U9; the docs' own manifest line (`source-manifest.md:31`) contradicts the strength of that verdict.
3. **Team 1286 P1 → keep Adapt, but require the author-claim label to travel.** U3 (`seq:220-236`) inherits shared-replayable-state design from a paper with no confirmed repo and cites no provenance. Add the source label to U3's rationale so a future reader cannot mistake it for a proven mechanism.
4. **Local KDD code → keep the Reject verdicts, downgrade the evidence class.** "Local source, not included" (`source-manifest.md:39`) means no reviewer can re-derive those line anchors. Label it *reviewer-observed, non-reproducible* rather than fixed-source, consistent with how the docs treat unavailable audio (`research-synthesis.md:28`).
