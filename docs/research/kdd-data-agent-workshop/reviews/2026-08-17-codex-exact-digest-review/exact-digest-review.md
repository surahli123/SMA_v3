# Exact-Digest M0 Document Review

Date: 2026-08-17  
Handoff: `kdd-m0-exact-digest-review-20260817`  
Branch / HEAD observed at review start: `codex/kdd-data-agent-practices-research` / `28cbbda6e4d4d7f08134952d38433e52d3ee8768`

## Verdict and authority boundary

**REJECT — CODEX_ADVISORY_ONLY.**

The current document candidate is not internally safe to freeze or implement. Owner decisions D1 and D3 are not propagated, D2 is only partially propagated, stale text still presents exhausted M0 authority as live, and most shared `VAL-*` acceptance IDs lack implementation-unit ownership. These are current-byte contract defects, not requests for stylistic improvement.

This verdict is advisory only. It is not an Opus or Fable freeze decision, an Owner authorization, a Phase A independent-review result, production authority, P2/P3/P4 closure, M1/M2 implementation approval, or Committee Acceptance. No canonical document, Phase A artifact, Git state, code, test, fixture, external system, or prior review was modified.

## Scope and source-path correction

The handoff names `reviews/2026-08-16-opus5-m0-alignment/00-final-review.md`, which does not exist. Before adopting any prior conclusion, this review located the single document containing exactly the requested 38 identifiers (`B1`-`B14`, `M1`-`M24`):

`docs/research/kdd-data-agent-workshop/reviews/2026-08-15-opus5-enterprise-plan-review/00-final-review.md`

Its SHA-256 is `802b82a25f7163d4a4e6ccf36687cf2fa4e341d17bb62b9f9f80910aa24d803c`. The substitution is recorded as a coverage correction, not silently treated as the handoff's literal path.

## Exact-digest binding

| Reviewed artifact | Start SHA-256 | End SHA-256 | Result |
| --- | --- | --- | --- |
| `reviews/2026-08-15-opus5-enterprise-plan-review/00-final-review.md` | `802b82a25f7163d4a4e6ccf36687cf2fa4e341d17bb62b9f9f80910aa24d803c` | `802b82a25f7163d4a4e6ccf36687cf2fa4e341d17bb62b9f9f80910aa24d803c` | stable |
| `reviews/2026-08-16-opus5-m0-alignment/m0-freeze-opus5-adversarial-review.md` | `aa0a3b5dd4bc59aede5f9f109cca48384e62dd8905ae9b61170a78691e048ad8` | `aa0a3b5dd4bc59aede5f9f109cca48384e62dd8905ae9b61170a78691e048ad8` | stable |
| `reviews/2026-08-16-opus5-m0-alignment/m0-freeze-codex-fix-handoff.md` | `e55b7273f6d5464a0ab5813128d1a9b3b917be94a16401c17b882d659f42becb` | `e55b7273f6d5464a0ab5813128d1a9b3b917be94a16401c17b882d659f42becb` | stable |
| `reviews/2026-08-16-opus5-m0-alignment/m0-freeze-codex-disposition.md` | `5801c035aa13d912c8adce840f262e84b36523d41f9646e436b3cac1ecf869d5` | `5801c035aa13d912c8adce840f262e84b36523d41f9646e436b3cac1ecf869d5` | stable |
| `reviews/2026-08-17-fable5-architecture-finalization/architecture-decision-ledger.md` | `e3b830da95b8ec1d8c4401ba75e1b130beaa5148d3d4da1c471fb876ec4c27b7` | `e3b830da95b8ec1d8c4401ba75e1b130beaa5148d3d4da1c471fb876ec4c27b7` | stable |
| `reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md` | `67c844d10dcafcf2637388bf579dfcd9866d7d69ea6f4d3b456fd6b6b15dfcfa` | `67c844d10dcafcf2637388bf579dfcd9866d7d69ea6f4d3b456fd6b6b15dfcfa` | stable |
| `final-architecture-spec.md` | `3b20c93859b78074b653d375fc29f60bd40993b3f3bcb4ee2ff481e8ba8706b8` | `3b20c93859b78074b653d375fc29f60bd40993b3f3bcb4ee2ff481e8ba8706b8` | stable |
| `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md` | `52ce2763a365eb35ea884dfbc7f19b8b3d012b85edac544a21b356638126499c` | `52ce2763a365eb35ea884dfbc7f19b8b3d012b85edac544a21b356638126499c` | stable |
| `implementation-sequencing.md` | `1d42e67c0ba5e2a1799960a3e151b12fa847a419f13b7a9f63362366dc3a29ee` | `1d42e67c0ba5e2a1799960a3e151b12fa847a419f13b7a9f63362366dc3a29ee` | stable |
| `eval-acceptance-plan.md` | `5dce10ca451f7ccbbf5d86896cefed2b8dd8a5b5cae480da4d3ea030d5603194` | `5dce10ca451f7ccbbf5d86896cefed2b8dd8a5b5cae480da4d3ea030d5603194` | stable |
| `reviews/2026-08-17-codex-exact-digest-review/handoff.md` | `08b94aa85cf041e177ca1793bb3fdb2bef7347bb2dcc6919ec5b5827dccdd0b4` | `08b94aa85cf041e177ca1793bb3fdb2bef7347bb2dcc6919ec5b5827dccdd0b4` | stable |

No reviewed input changed during the bounded run.

## Critical current-byte findings

### P0 — D3 is directly contradicted

The Owner ledger makes `analysis_use` the only stored M0 readiness state and makes `post_analysis_eligibility` a non-settable render-time projection (`architecture-decision-ledger.md:60`). The packet still says M0 stores two coordinated fields and rejects invalid stored pairs (`m0-m2-build-alignment-packet.md:117-132`). The same two-stored-field contract appears in `final-architecture-spec.md:36,199,274`, the CE plan at `:32,198`, sequencing at `:56,59`, and evaluation at `:212,221`.

**Consequence:** conforming implementations would persist a state model the Owner explicitly rejected.  
**Minimal correction:** store only `analysis_use`; derive eligibility deterministically at render time; make the projection non-settable; retain pair-shaped wording only as derived scenario language.

### P0 — D1 is not propagated

The ledger requires exactly `sufficiency_rule = runtime_only | runtime_and_sample`, preregistered inputs only, no achieved/post-hoc power, check 19 `NOT_APPLICABLE` for `runtime_only`, and a declared-missing-input result of `MISSING`, `blocked + not_permitted`, `contract_correction` (`architecture-decision-ledger.md:58`). The packet, spec, plan, sequencing, and evaluation retain generic power/MDE wording; `final-architecture-spec.md:469` still delegates directional use to an undefined permission.

**Consequence:** two builders can compute different readiness, including an outcome-aware achieved-power path forbidden by D1.  
**Minimal correction:** propagate the closed rule enum, inputs, state transitions, and prohibition verbatim through all five implementation surfaces and their fixtures.

### P0 — Exhausted authority is still presented as live

The packet correctly says the prior continuation authorization is exhausted and requires a new Owner authorization and digest-bound start receipt (`m0-m2-build-alignment-packet.md:7,19`). In conflict, the CE plan says the Owner separately authorized `M0-F0`-`M0-F5` (`:20`), sequencing says the local slice is authorized and may proceed (`:74,83-84`), evaluation describes it as separately authorized (`:4`), and the spec claims current authorization (`:890,940`). The packet itself also repeats the exhausted handoff as the current execution budget at `:200`.

**Consequence:** a builder can incorrectly start work without live authority.  
**Minimal correction:** replace every live-authorization claim with the exhausted-state rule and require one new bounded start receipt binding path, revision, digest, caps, expiry, and halt owner.

### P1 — D2 is only partially propagated

The four arm-parity fields and a divergence check exist, but the exact Owner branches do not. The ledger requires missing inputs to yield material `MISSING`, `blocked + not_permitted`, and `evidence_collection`; permits `NOT_APPLICABLE` only through a versioned policy; and makes divergence a material `FAIL` (`architecture-decision-ledger.md:59`). Those branches are absent from the packet, spec, plan, sequencing, and evaluation.

**Consequence:** incomplete or non-applicable Flights can receive implementation-dependent outcomes.  
**Minimal correction:** copy the three D2 branches and required per-arm source identities into each implementation and acceptance surface.

### P1 — `VAL-*` ownership is incomplete

The packet contains 26 exact `VAL-*` IDs. The CE plan shares 22 and the packet adds four M1/M2 IDs. Sequencing explicitly names only `VAL-UI-001` and `VAL-UI-101` (`implementation-sequencing.md:59`); neither the spec nor evaluation plan names any `VAL-*` ID. Packet family-to-gate rows (`m0-m2-build-alignment-packet.md:273-282`) govern claim authority but do not assign implementation ownership.

**Consequence:** unit completion cannot be reconciled mechanically against the acceptance registry.  
**Minimal correction:** add one authoritative table mapping every active ID to exactly one `M0-F*`, later `U*`, or explicit external gate, plus its proving test or receipt.

## Reconciliation of all 38 Opus findings

States describe current document bytes, not implementation or production proof. “Implemented” means the requested document contract is present. “Open” and “partial” remain required actions or gates.

| ID | Severity | Current state | Exact current-byte evidence | Consequence | Minimal correction |
| --- | --- | --- | --- | --- | --- |
| B1 | BLOCKER | IMPLEMENTED | `final-architecture-spec.md:201,225,874` defines the attribution resolver, admissible provenance, and file-only `G2=inconclusive` case. | No remaining document gap for the original attribution-port finding. | None; preserve this contract. |
| B2 | BLOCKER | IMPLEMENTED | `m0-m2-build-alignment-packet.md:22-33,194-200` makes M0 the first deliverable and prices the M0-M2 slice at 4-6 active engineering weeks. | The delivery target and active-time envelope are explicit. | None; preserve this contract. |
| B3 | BLOCKER | OPEN / INTENTIONALLY GATED | `final-architecture-spec.md:926` permits direct reuse only after interface, provenance, test, security, license, source, owner, and access evidence; no per-asset inventory exists. | Builders cannot determine which named assets are adopt/adapt/reject candidates. | Produce the per-asset reuse inventory before direct reuse or `M0-F1`. |
| B4 | BLOCKER | IMPLEMENTED | `final-architecture-spec.md:183-184,209,597` defines Trace as a separate diagnostic store whose divergence never overrides Evidence. | The original competing-truth ambiguity is closed in the document contract. | None; preserve this contract. |
| B5 | BLOCKER | IMPLEMENTED | `final-architecture-spec.md:209,232,726-728` gives Trace an owner/port and removes Trace navigation from the digested manifest. | Packet immutability no longer depends on an unfrozen Trace schema. | None; preserve this contract. |
| B6 | BLOCKER | IMPLEMENTED | `final-architecture-spec.md:232,648,673-681` and `implementation-sequencing.md:335` define typed no-body redaction failure, dependent blocking, intake controls, and no raw persistence. | Redaction failure is fail-closed rather than an unowned raw-transcript path. | None; preserve this contract. |
| B7 | BLOCKER | IMPLEMENTED | `final-architecture-spec.md:149,194-195,608` and `implementation-sequencing.md:451-453` require a constrained broker, write-incapable source credentials, and real write-denial proof behind P2. | “Read-only” has a credential and broker enforcement boundary. | None; preserve this contract. |
| B8 | BLOCKER | IMPLEMENTED | `final-architecture-spec.md:145,205,245-246,609` defines role separation, permission intersection, synthetic allow/deny probes, and per-render authorization. | Cross-user ACL diagnosis no longer implies a broad service identity over bodies. | None; preserve this contract. |
| B9 | BLOCKER | IMPLEMENTED | `final-architecture-spec.md:243,613-618` defines predecessor digests, tiered retention, keyed stores, tombstones, and crypto-shredding for erasure-eligible content. | Append-only audit history and erasure obligations have a compatible path. | None; preserve this contract. |
| B10 | BLOCKER | IMPLEMENTED | `final-architecture-spec.md:264,270,414` defines segment-bearing claims and a preregistered segmentation/multiplicity contract. | Segment claims can be reproduced without uncontrolled multiple comparisons. | None; preserve this contract. |
| B11 | BLOCKER | IMPLEMENTED AS DOCUMENT REQUIREMENT | `m0-m2-build-alignment-packet.md:260-269` and `eval-acceptance-plan.md:224-226,244` require trivial baselines, adversarial decoys, and author/evaluator independence or conflicts. | The evaluation-power contract is explicit; fixture existence remains implementation evidence, not a document-freeze claim. | None in the documents; produce fixtures only under a valid start. |
| B12 | BLOCKER | IMPLEMENTED | `implementation-sequencing.md:414,421` makes `UI-001` synthetic before P3 and leaves final interaction acceptance open. | U9 is no longer required to pass a P3-approved interaction contract before P3. | None; preserve this contract. |
| B13 | BLOCKER | IMPLEMENTED | `deliverable-index.md:16-17,90-91`, `README.md:23-24`, and `cloud-agent-handoff.md:30-31` link both the experiment profile and harness-practices document; the controlling content is present in the main worktree. | The reviewed package is reachable without relying on a transient alternate worktree. | None; preserve indexed authority order. |
| B14 | BLOCKER | IMPLEMENTED | `implementation-sequencing.md:451-463,496` and `eval-acceptance-plan.md:91-93` require read/load ceilings, abort behavior, and a named halt authority. | Production-like and shadow paths have bounded operational stops. | None; preserve this contract. |
| M1 | MAJOR | IMPLEMENTED | `final-architecture-spec.md:155,422` allows current-generation correction through superseding Claim/VerdictEvent revisions and requires a new generation after sealed closure. | False confirmation has a legal, auditable exit path. | None; preserve this contract. |
| M2 | MAJOR | IMPLEMENTED | `final-architecture-spec.md:269,509-515` types human citations and legal relationship triples so Trace cannot support a claim. | Trace cannot enter `confirmed` through an unconstrained human citation. | None; preserve this contract. |
| M3 | MAJOR | IMPLEMENTED | `final-architecture-spec.md:450-458,587` requires a non-applicable fragment/sentinel and a human-review-only publish barrier. | The `not_applied` state has a delivery mechanism, not only a label. | None; preserve this contract. |
| M4 | MAJOR | IMPLEMENTED | `final-architecture-spec.md:366-367,510` requires G4 evidence to be disjoint from G3 support unless it is a preregistered counterfactual. | One observation cannot satisfy both support and challenge. | None; preserve this contract. |
| M5 | MAJOR | IMPLEMENTED | `implementation-sequencing.md:260` and `final-architecture-spec.md:513` make missing replay authority/coverage/budget `inconclusive`, never `not_applicable`. | The G6 escape cannot be emptied by missing authority. | None; preserve this contract. |
| M6 | MAJOR | IMPLEMENTED | `final-architecture-spec.md:272,484-499` deterministically classifies material validity failures and treats unclassified materiality as material at the ceiling. | Invalid-experiment blocking no longer hinges on undefined materiality. | None; preserve this contract. |
| M7 | MAJOR | PARTIAL / SUPERSEDED BY D1 GAP | `final-architecture-spec.md:253,469` names neutral/mixed outcomes and directional use, but D1's closed sufficiency state machine is absent. | Neutral or underpowered reads can still receive builder-dependent treatment. | Propagate D1 exactly; then verify neutral/mixed scenario coverage. |
| M8 | MAJOR | IMPLEMENTED | `final-architecture-spec.md:106,277` and `m0-m2-build-alignment-packet.md:168-181` give Win/Loss a canonical M2 packet and query-evidence fields. | Win/loss evidence has an explicit home and stage boundary. | None; preserve this contract. |
| M9 | MAJOR | PARTIAL / D2 BRANCHES MISSING | `final-architecture-spec.md:271-272` and `implementation-sequencing.md:58` name parity fields and divergence, but omit D2's exact MISSING/N/A/FAIL branches. | Arm-parity failures can be classified inconsistently. | Propagate D2's exact outcome and next-action branches. |
| M10 | MAJOR | IMPLEMENTED | `implementation-sequencing.md:58,356` and `eval-acceptance-plan.md:150` require compositional SRM and zero-result shift checks. | Query-mix confounding is part of validity evaluation. | None; preserve this contract. |
| M11 | MAJOR | IMPLEMENTED | `final-architecture-spec.md:417` and `eval-acceptance-plan.md:150,254` require position-bias correction or interleaving before click-derived support. | Click evidence cannot silently stand in for relevance. | None; preserve this contract. |
| M12 | MAJOR | IMPLEMENTED | `final-architecture-spec.md:277` defines judgment/offline-eval evidence; the M1 plane list includes offline-online divergence. | Relevance judgments and offline/online reconciliation have a typed evidence class. | None; preserve this contract. |
| M13 | MAJOR | IMPLEMENTED AS GATED PROPOSAL | `final-architecture-spec.md:262` and `implementation-sequencing.md:343` define proposed index/connector/permission/presentation/telemetry subtypes while retaining owner gates. | Search-specific changes can be typed without pretending the subtype authority is already settled. | None; preserve the gate. |
| M14 | MAJOR | IMPLEMENTED | `implementation-sequencing.md:358` and CE plan `:698` define a reviewer-recomputable `uncalibrated_fixture` ordering with gate ceilings and stable IDs. | Fixture ranking is reproducible rather than merely byte-stable. | None; preserve this contract. |
| M15 | MAJOR | IMPLEMENTED | `eval-acceptance-plan.md:181,289-290` and `final-architecture-spec.md:850` require every veto to name a deterministic, human, or not-yet-implemented detector. | Missing detector coverage remains visible instead of masquerading as a pass. | None; preserve this contract. |
| M16 | MAJOR | IMPLEMENTED | `eval-acceptance-plan.md:57,244,287` and `final-architecture-spec.md:851` define leakage detectors, prompt freeze, conflict handling, and widely-published-case exclusion. | Blind-case contamination controls are concrete and auditable. | None; preserve this contract. |
| M17 | MAJOR | IMPLEMENTED AS PRE-P3 BOUNDARY | `implementation-sequencing.md:404-421` replaces prototype-specific acceptance with a synthetic state/interaction contract and leaves live P3 acceptance open. | The old misleading prototype behavior cannot be treated as accepted review evidence. | None in the candidate docs; preserve P3 as open. |
| M18 | MAJOR | OPEN / OUT-OF-M0 EXTERNAL-SHARING ACTION | `final-architecture-spec.md:690-692` and CE plan `:339` prohibit bare hashes for low-entropy/confidential values but do not complete the external-sharing inventory/action. | Digest-based membership or confirmation leakage remains possible if later sharing ignores the rule. | Complete the named sharing/security action before any affected external distribution. |
| M19 | MAJOR | OPEN / DIRECTION-ONLY ACTION | `final-architecture-spec.md:709-713` and CE plan `:745` acknowledge employee-endpoint collection as a separate privacy/labor authority decision, but no DPIA/works-council/query-authority receipt exists. | A collector fleet cannot be authorized from the current package. | Keep collection off; obtain the separate privacy/labor and query-authority decisions if pursued. |
| M20 | MAJOR | OPEN / NO-POST-HOC-NARROWING RULE INCOMPLETE | `final-architecture-spec.md:709-713` defines dependent Trace blocking, while the complete adapter-pin/capture-receipt barrier remains an action to verify in implementation. | Unsupported host capture can still be narrowed after outcome unless the receipt rule is enforced end to end. | Freeze the required capture/pin predicate and test fail-closed unsupported-host behavior before dependent publication. |
| M21 | MAJOR | IMPLEMENTED | `final-architecture-spec.md:243,278,849` requires predecessor digests and packet manifests of `(revision_id, content_digest)` pairs. | Historical revision substitution becomes detectable. | None; preserve this contract. |
| M22 | MAJOR | IMPLEMENTED | `implementation-sequencing.md:214-216` restates the universal negative as an enumerated capability allowlist, denied-write receipts, and reachability/import assertions. | Read-only verification has deterministic pass/fail evidence. | None; preserve this contract. |
| M23 | MAJOR | IMPLEMENTED | `implementation-sequencing.md:343,451-453` limits pre-P2 work to interfaces, fixture algorithms, and unknown-authority paths; source-specific fidelity waits for P2/U11. | Fixture shapes are not represented as proven production grounding. | None; preserve this boundary. |
| M24 | MAJOR | IMPLEMENTED | `m0-m2-build-alignment-packet.md:69,92`, CE plan `:132,197`, and `eval-acceptance-plan.md:150` require assignment/analysis units and a named valid ratio variance estimator. | Unit mismatch is a material validity failure. | None; preserve this contract. |

Count check: 14 `B*` rows + 24 `M*` rows = **38**.

## D1-D3 cross-document consistency

| Decision | Owner-selected contract | Packet | Architecture spec | CE plan | Sequencing | Evaluation | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D1 | Closed `runtime_only | runtime_and_sample`; preregistered inputs only; no achieved/post-hoc power; exact N/A and missing-input branches (`architecture-decision-ledger.md:58`) | Generic power/MDE at `:75,107,138` | Generic policy at `:271-272`; stale permission at `:469` | Generic power/MDE at `:32,129,198` | Generic power/MDE at `:56,58` | Generic checks at `:150,212-214` | **CONTRADICTED / NOT PROPAGATED** |
| D2 | Missing = material `MISSING` + `blocked/not_permitted` + `evidence_collection`; versioned N/A; divergence = material `FAIL` (`:59`) | Fields/check exist at `:74,93`; branches absent | Fields at `:271`; branches absent | Divergence named at `:34,197`; branches absent | Divergence named at `:58`; branches absent | Parity named at `:150,214`; branches absent | **PARTIAL** |
| D3 | Store only `analysis_use`; derive non-settable eligibility at render time (`:60`) | Stores both and validates pair at `:117-132` | Stores both at `:36,199,274` | Stores both at `:32,198` | Stores both at `:56,59` | Requires both at `:212,221` | **DIRECTLY CONTRADICTED** |

## `VAL-*` namespace and ownership audit

- Packet registry: 26 exact IDs (`m0-m2-build-alignment-packet.md:234-269`).
- CE plan registry: 22 shared IDs (`docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md:123-150`).
- Packet-only planned IDs: `VAL-M1-001`, `VAL-M1-002`, `VAL-M2-001`, `VAL-M2-002` (`m0-m2-build-alignment-packet.md:249-252`).
- Sequencing names only `VAL-UI-001` and `VAL-UI-101`; the spec and evaluation plan name no `VAL-*` IDs.
- The packet's family gate table (`:273-282`) is useful but is not a one-ID-to-one-unit ownership map.

Required freeze correction: one authoritative registry must map every active ID to exactly one implementation unit (`M0-F*` or later `U*`) or one explicitly gate-only owner, with the exact proving test/receipt and prerequisites. No ID may remain implied by family membership alone.

## Gate and non-authorization ledger

| Gate or authority | Current state | What this review does not establish |
| --- | --- | --- |
| New Owner start receipt for `M0-F1`-`M0-F5` | OPEN | No implementation start authorization |
| D1-D3 propagation and byte reconciliation | OPEN | No packet/spec freeze |
| B3 reuse inventory | OPEN | No direct component reuse approval |
| M18/M19/M20 actions | OPEN / deferred | No external sharing, endpoint collection, or capture-pipeline approval |
| Phase A Q11/Q12 independent review | OPEN | This review did not inspect Phase A as a substitute |
| Opus exact-digest freeze gate | OPEN | Codex advice cannot substitute |
| Fable architecture-finalization gate | OPEN | Codex advice cannot substitute |
| P2 production authority | OPEN | No production reads, credentials, or mapping authority |
| P3 interaction acceptance | OPEN | No live UI acceptance |
| P4 evaluation/gold/calibration | OPEN | No numeric GO or production-readiness claim |
| M1/M2 implementation | NOT AUTHORIZED | Packet planning is not execution authority |
| Committee Acceptance | EXTERNAL / OPEN | No experiment decision approval |

## Review coverage and reviewer roster

The bounded run used five adopted reviewer lanes: feasibility, scope-guardian, coherence, security, and adversarial-document review. They independently converged on D1, D2, D3, stale execution authority, and incomplete `VAL-*` unit mapping. Cross-model review was intentionally not used because it would not replace Opus/Fable and this task required a fresh Codex advisory.

An initial orchestration error dispatched a sixth `product_lens`. After the Owner coordination correction, that lane was interrupted while running. Its output was not read, cited, merged, or adopted. No replacement reviewer was started. The final and cumulative adopted roster is therefore exactly five lanes.

| Adopted lane | Coverage used |
| --- | --- |
| feasibility | Implementability of D1-D3, authority, and acceptance ownership |
| scope-guardian | Scope inflation, exhausted authority, D1-D3, `VAL-*` ownership |
| coherence | Cross-document contradictions and missing state-machine branches |
| security | Unauthorized-start path and redundant readiness authority state |
| adversarial-document | Outcome-aware sufficiency and deterministic projection risks |

This is one bounded report-only run. The next lawful step is canonical correction by an authorized owner/editor, followed by new exact-digest Codex verification and the required Opus/Fable/Owner gates. This report itself authorizes none of those actions.
