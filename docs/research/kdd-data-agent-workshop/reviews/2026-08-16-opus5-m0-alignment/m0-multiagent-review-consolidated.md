---
review_id: m0-multiagent-deep-review-20260817
scope: .agents/skills/kdd_data_agent (M0 pre-alignment foundation)
method: two dynamic workflows, 97 agents, 4.95M subagent tokens, 1253 tool calls
status: consolidated by hand - both workflow synthesis agents died on session limit
---

# M0 Foundation - Consolidated Multi-Agent Review

## Verdict

**CONCERN-ONLY, with one methodological caveat that matters more than any single finding.**

Nothing found makes Phase A wrong to have built. Several things make its *evidence
documents* overstate what is enforced. The package's semantic drift against the CLOSED
P1 contract is the substantive issue, and it is still live.

## 0. Methodological defect in this review - disclosed first

Both workflows classified a finding as "killed" when `total > 0 && upheld*2 >= total`
was false. When every refuter for a finding **failed** (session limit), `total == 0`,
so the finding was silently counted as killed rather than as unverified.

Consequence: WF#1 reported "30 raised, 4 confirmed, 26 killed" and WF#2 "12 raised,
1 confirmed, 11 killed". In reality **42 findings were raised and only 5 were ever
adversarially verified**. The verify agents for the determinism, invented-semantics,
test-quality, doc-fidelity, and audit-fidelity lenses all died on the session limit.

This is the same class of error the workflow guidance warns about - a silent cap that
reads as coverage. The findings below are therefore labelled by **verification status**,
not by the workflow's own confirmed/killed split.

## 1. LIVE - verified by hand against the current tree

Re-checked after the parallel session's edits (package is now 225 tests / 19 modules).

| # | Location | Defect | Evidence |
|---|---|---|---|
| L1 | `core/coverage_gap.py` materiality gate | The package's **single named gate** is bypassable by any non-sentinel string. The guard is `is_sentinel(rule_source)` only. | `CoverageGap(..., materiality=MATERIAL, rule_source="")` -> constructs. `rule_source="reviewer said fine"` -> constructs. Sibling `reason` IS strip-checked; `identity.py` strip-checks every other MaybeStr field. |
| L2 | `core/coverage_gap.py` `CoverageGapKind` | 9 members against P1's frozen 5. `partial_read`, `stale_read`, `conflicting_sources`, `redaction_failure` are additions to a **CLOSED** contract. P1 assigns `stale` to `evidence_state` and contradiction to `contradicts`, so two of the four re-label other frozen dimensions. | Enum dump: 9 members. `freeze-canonical-domain-policy-contracts.md:61` names exactly 5. All 8 fixtures depend on the extended set. |
| L3 | `adapters/outcomes.py` `DEFAULT_GAP_KIND_BY_OUTCOME` | Guesses a gap kind when the fixture leaves it UNKNOWN - inference the handoff forbids and the package elsewhere claims never to perform. | Map still present. |
| L4 | `core/canonical_json.py` sentinel smuggling | `{"__kdd__":"UNKNOWN"}` inside free-form fixture JSON decodes to a live `Sentinel` and can enter a receipt body. The reserved-key guard is one-sided: rejected on encode, accepted on decode. | `canonical_loads('{"body":{"__kdd__":"UNKNOWN"}}')["body"]` -> `Sentinel`. |
| L5 | `core/canonical_json.py` float emission | Second undocumented RFC 8785 deviation, larger than the key-sort one that IS documented. Python `repr` != JCS `ToString`. | `{"v":1.0}` -> `{"v":1.0}` (JCS: `1`); `{"v":-0.0}` -> `{"v":-0.0}` (JCS: `0`). |
| L6 | `core/canonical_json.py` lone surrogate | `canonical_encode` is not total over what `canonical_loads` accepts: a JSON-escaped lone surrogate decodes, then raises a **bare `UnicodeEncodeError`** on re-encode rather than a typed rejection. | `canonical_loads('{"k":"\ud800"}')` then encode -> `UnicodeEncodeError`. |
| L7 | `core/identity.py` `AuthorizationState` | Folds `redaction_failed` into the authorization axis, collapsing two facts the package itself models as separate receipt kinds and P1 keeps independent. | Enum contains `redaction_failed` alongside `authorized`/`unauthorized`. |

## 2. The most damaging single finding

**The "two independent sources agree" justification for the no-retained-body invariant
rests on the C1 identifier collision the package's own seam registry declares unresolved.**

`m0-prealignment-foundation-receipt.md` justifies three implemented invariants by citing
the alignment packet draft and the CE plan as two agreeing independent sources. For the
no-body rule both citations are `M0-SEC-001` / `M0-READ-001` - and `SEAM-M0-06-ACCEPTANCE-IDS`
exists precisely because those identifiers are **the same strings naming different
scenarios** in the two documents. Two documents using a colliding ID are not two
independent agreeing sources.

The invariant itself is almost certainly right and fails closed. The **argument** for it
is circular and must be restated, or the invariant re-grounded on non-colliding text.

## 3. ALREADY FIXED by the parallel session

- Duplicate JSON object keys now raise `CanonicalJSONError` (was: silent last-wins, two
  byte-different fixtures -> identical digest).
- The `__builtins__` / reflection scanner holes: `FORBIDDEN_GLOBAL_REFERENCES` and
  `FORBIDDEN_ATTRIBUTE_REFERENCES` now cover `__builtins__`, `__subclasses__`, `__mro__`,
  `__globals__`, `modules`. Planted violations grew 15 -> 46.
- `tmp_path` removed, so "never writes a file" is literally true.

## 4. UNVERIFIED but credible - raised, never adversarially checked

Ordered by how cheap they are to confirm. None has been re-tested against the current tree.

**Test quality (3 BLOCKER-rated, from mutation attempts):**
- `Receipt._identity_payload` unverified: source, actor, authorization_state,
  observed_interval, detail, coverage_gaps each individually removable from receipt
  identity with the whole suite still green -> two materially different receipts collide.
- `_parse_authorization_state` can be mutated to **fail open** (return `AUTHORIZED` for any
  unrecognised string) with the suite still green; no test feeds an invalid state.
- `_require_exact_keys` can be made a total no-op; the strict fixture-integrity layer is
  untested for rejection.
- `test_the_build_receipt_binds_the_input_digest_and_the_log` asserts **inequality**, so a
  constant satisfies it - the test named "binds the log" proves no binding.

**Package vs P1 (WF#2):**
- A `trusted` read that returned **zero rows** is accepted with no Coverage Gap, and
  attaching one is mechanically rejected - direct contradiction of P1's frozen
  "zero reads create a Coverage Gap" rule.
- `Receipt.outcome` is an unconstrained free string, so a receipt can carry P1-forbidden
  canonical vocabulary (e.g. `confirmed`) produced by an actor of kind `AGENT`.
- `Revision` omits two fields P1 names as required on every transition: `reason` and
  `policy_version`. `Receipt` carries no schema/version field.
- P1's own kind `timeout` is unreachable through the outcome mapping.

**Doc fidelity:**
- The capability allowlist is described as a runtime control; it is a source-level lint.
- Negative control covers 4 of the scanner's 6 finding kinds.
- "Nine mutations, all caught" - there were ten, and M7 was not caught. The receipt's own
  section 9 is honest; the toolchain receipt's one-line summary is not.
- Every LOC/module/test count in all four documents is stale.

## 5. The audits misdescribe the local implementation

This matters because `TOOLCHAIN_RECEIPT.md` was written from the audits, not from source.

- **`primary-source-audit.md:164-167` (P10) and `kdd-source-practices.md:250` (K7) present
  the KDD trace subsystem (`emit`, `emit_seam`, `agent_context_for`) as a working retained
  mechanism graded "Strong; directly implemented in source code". In the real repo the
  entire emission path is dead - no callers.** A dead subsystem was being offered as the
  donor for this package's G-3 Trace gap.
- `TraceSpan` does not contain the fields K7 attributes to it.
- `latency_governor` is presented as a budget/concurrency control plane; the real bounds
  differ from the claim.
- P5 **understates** the local DuckDB backend: it describes read-only enforcement as a
  first-token allowlist plus SQLite `mode=ro` and calls it insufficient, but the DuckDB
  backend implements a genuine runtime capability lockdown. The real code is stronger than
  its own audit says.

## 6. Owner decisions vs engineering

**Engineering can fix now, no Owner input:** L1 (one-line strip check), L4 (reject the
reserved key on decode too), L5/L6 (document or normalise float emission; type the
surrogate rejection), the four test-quality gaps, the doc-fidelity corrections, and the
restatement in section 2.

**Blocked on the frozen packet / Owner:** L2 and L3 - reducing `CoverageGapKind` to P1's
five and deleting the default map means the four read conditions need a home, and deciding
which canonical kind covers a partial, stale, conflicting, or redaction-failed read is
materiality/taxonomy policy. Recommended: reduce to five, allow `kind=UNKNOWN`, and
register a new seam rather than mapping them by hand. L7 likewise.

## 7. What this review cost and what it did not cover

97 agents, 4.95M subagent tokens, 1253 tool calls, ~29 min wall clock across two
workflows. 50 of 97 agents died on the session limit, including both synthesis agents and
every verifier for four of seven lenses.

Not covered: no finding from the determinism, invented-semantics, test-quality, or
doc-fidelity lenses received adversarial refutation, so their severities are the
proposing agent's own and should be treated as unreviewed claims until checked.
