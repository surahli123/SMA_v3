# Phase A Independent Verification — Q11 and Q12

Verdict: **`PASS_WITH_GAPS`**

## 1. Reviewer identity and conflict of interest

| Field | Value |
| --- | --- |
| Reviewer | Fresh Claude Code session, third reviewer for Q11/Q12 |
| Model | `claude-opus-5[1m]` (Opus 5, 1M context), high effort |
| Session ID | `session_011PvYucF3moQ4oPFenZ2N5M` |
| Review window (UTC) | 2026-08-18T02:52:02Z to 2026-08-18T07:33:01Z |
| Repository | `/Users/surahli/Documents/projects/SMA_v2` |
| Branch | `codex/kdd-data-agent-practices-research` |
| HEAD | `28cbbda6e4d4d7f08134952d38433e52d3ee8768` |
| Python | 3.14.4 (Clang 17.0.0), `/opt/homebrew/Cellar/python@3.14/3.14.4` |

**Conflict-of-interest statement.** This session did not author the Phase A package, the
Codex continuation, any Phase A receipt, the earlier Opus freeze review, or the alignment
packet. It read the prior review and the prior receipts only as claims to test. Every
conclusion below rests on a command this session ran against the bytes named in section 2.
Where a prior claim is repeated here it is marked as confirmed or falsified by this
session's own evidence, never adopted.

This session did not read the product-steelman handoffs, to preserve independence on the
Q11/Q12 question as scoped.

## 2. Reviewed artifact binding

Recomputed at the start and at the end of the review. No historical digest was reused.

| Artifact | Expected (handoff) | Observed | Match |
| --- | --- | --- | --- |
| `reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md` | `67c844d1…6b15dfcfa` | `67c844d10dcafcf2637388bf579dfcd9866d7d69ea6f4d3b456fd6b6b15dfcfa` | yes |
| `final-architecture-spec.md` | `3b20c938…1ba8706b8` | `3b20c93859b78074b653d375fc29f60bd40993b3f3bcb4ee2ff481e8ba8706b8` | yes |
| `.agents/skills/kdd_data_agent/` aggregate | `2f1001b9…9f15bf7d1e` | `2f1001b93b19b2318c4c6419205ed2f7778ac23c02533e78a0c0899f15bf7d1e` | yes |

Aggregate method, reproduced from `m0-freeze-opus5-adversarial-review.md:21-24`: every
`.py`, `.json`, and `.md` file under the package, excluding `__pycache__`,
`.pytest_cache`, and `.omc` harness state; 42 files; per-file `shasum -a 256` over a
sorted path list, then a digest of that listing.

```text
find .agents/skills/kdd_data_agent -type f \( -name '*.py' -o -name '*.json' -o -name '*.md' \) \
  -not -path '*/__pycache__/*' -not -path '*/.pytest_cache/*' -not -path '*/.omc/*' \
  | sort | xargs shasum -a 256 | shasum -a 256
-> 2f1001b93b19b2318c4c6419205ed2f7778ac23c02533e78a0c0899f15bf7d1e   (42 files)
```

The sort is load-bearing: the same file set in raw `find` order digests to
`8a4bfaddc792edd9d8654c49abd474dda582e133afb1df8769ec842ed7959524`. Any future receipt
citing this aggregate must also cite the ordering rule.

**No drift.** A per-file manifest captured at 02:52Z and re-captured at 07:16Z is
byte-identical across all 42 files (`diff` empty). All findings below bind to these bytes.

## 3. Authority state I did not assume

- The packet is a **post-review candidate, not frozen** (`m0-m2-build-alignment-packet.md:3`;
  `m0-freeze-codex-disposition.md:7`).
- The Phase A package aggregate is **unchanged since the continuation receipt**, while the
  packet moved from `40c7234f…` to `67c844d1…`. Eight adjudicated edits plus three
  additional corrections landed in the packet; **nothing landed in the code.** Most Q11
  staleness below is a direct consequence of that one-sided movement.
- No freeze record exists. Nothing in this report creates one.

## 4. Commands actually run

All read-only against the repository. Every mutation and fault injection ran on an
isolated byte-identical copy under `/private/tmp/phaseA-indep-2026-08-18/`.

```text
# bindings and drift
shasum -a 256 <packet, spec>
find … | sort | xargs shasum -a 256 | shasum -a 256          (start and end, identical)
diff baseline-manifest.txt recheck-manifest.txt              (empty)

# full suite, caches and bytecode disabled, four working directories
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider .agents/skills/kdd_data_agent/tests
  -> 225 passed in 0.24s     (cwd = repository root)
  -> 225 passed in 0.23s     (cwd = package root)
  -> 225 passed in 0.23s     (cwd = /private/tmp, PYTHONPATH=.agents/skills)
  -> 225 passed in 0.25s     (cwd = /private/tmp/phaseA-indep-2026-08-18, PYTHONPATH=.agents/skills)

# determinism: 9 fresh processes x 6 PYTHONHASHSEED values, live bytes and isolated copy
PYTHONHASHSEED={0,1,42,99991,4294967295,random,12345} python3 probe_determinism.py
  -> identical 47274-byte serialization, sha256 7837c3e6…c044375, in all 9 runs

# object-level fault injection (canonical JSON, coverage gaps, identity, append-only, seams)
python3 probe_objects.py ; python3 probe_objects2.py ; python3 probe_chain.py

# fixture / manifest / fail-closed parsing (57 probes on disposable fixture-root copies)
python3 probe_fixture.py

# static capability scanner reachability and non-vacuity (68 probes)
python3 probe_scanner.py

# runtime audit hook over the exercised hermetic path
python3 probe_runtime_audit.py

# mutation battery: 78 defined, 77 applied, each on a fresh isolated copy, suite re-run per probe
python3 mutate.py
# follow-ups + minimal-correction validation
python3 mutate2.py
```

Code read in full: `__init__.py`, `core/{canonical_json,digest,immutability,unknown,identity,coverage_gap,revisions,receipts,capabilities}.py`,
`adapters/{base,outcomes,fixture}.py`, `alignment/seams.py`, `runner/hermetic.py`,
`tests/{conftest,_import_graph,test_capability_allowlist,test_alignment_seams}.py`, the
nine fixture files, and the current packet sections 1–12.

## 5. Q11 — semantic independence

### 5.1 Headline

**Phase A has not pre-decided the readiness contract.** None of the post-edit packet's
decision vocabulary appears anywhere in the package: `post_analysis_eligibility`,
`analysis_use`, `decision_grade`, `not_permitted`, `eligible`, power/MDE, arm parity, and
the legal-combination policy return **zero** hits across all `.py` and `.json` files.
`directional_only` appears twice, both inside seam `blocked_reason` prose describing an
option under discussion, never as a code path. All ten seams raise. `decide_readiness()`
raises. Every fixture and manifest entry is locked to `expected_final_readiness =
"alignment_pending"`, and both locks are test-reachable (mutation F08 caught).

**What Phase A did quietly decide** is a *vocabulary*, not a decision rule: a 9-member
Coverage Gap taxonomy against a closed contract that enumerates 5, and a 5-member
`AuthorizationState` that folds redaction failure into the authorization axis. Both are
locked by tests, so Phase B inherits them as contracts rather than proposals.

**What has gone stale** is every authority citation in the package. Eight of ten seams
cite `alignment packet §N`; all eight resolve against the **superseded** draft's numbering,
and six of them point at wholly unrelated sections of the current packet. Two comments cite
acceptance IDs that no longer exist in any document. No test detects any of this: mutating
a seam's `packet_reference` to `"TOTALLY WRONG AUTHORITY"` passes 225/225.

### 5.2 Classification table

| # | Seam / surface examined | Observation | Evidence | Classification |
| --- | --- | --- | --- | --- |
| Q11-1 | Readiness seam | `SEAM-M0-01` raises; `decide_readiness()` raises; no eligibility/use field exists | `alignment/seams.py:104-114`, `runner/hermetic.py:207-209`; probe `seam.decide_readiness` | `semantics_independent` |
| Q11-2 | Readiness seam wording | `blocked_reason` still describes "two outcomes (ready \| blocked) or three (ready \| directional_only \| blocked)"; the packet now specifies two coordinated fields with three legal pairs | `alignment/seams.py:107-111` vs `packet:115-133` | `stale_reference_only` |
| Q11-3 | Check-inventory seam | Raises; no check type exists in code. `blocked_reason` says "the draft lists 14 checks"; the current packet lists 19 | `alignment/seams.py:119-121` vs `packet:88-108` | `stale_reference_only` |
| Q11-4 | Materiality seam | Raises; `Materiality` defaults to `UNKNOWN`; no unknown→material ceiling is implemented anywhere (correct — the ceiling is Phase B's) | `core/coverage_gap.py:59`, `alignment/seams.py:126-135`; grep for any ceiling mapping returns none | `semantics_independent` |
| Q11-5 | Materiality rule-source guard | Guard admits `""`, `"   "`, `"because I said so"`, `7`, `{"id":"x"}` as a "named versioned rule_source"; only a sentinel is rejected | `core/coverage_gap.py:71-75`; probes `gap.nonmaterial_EMPTY_rule`, `gap.nonmaterial_ARBITRARY_rule`, `gap.nonmaterial_INT_rule` | `unratified_semantic_choice` (BLOCKER-1) |
| Q11-6 | `CoverageGapKind` taxonomy | 9 kinds; the closed canonical contract enumerates 5. `PARTIAL_READ`, `STALE_READ`, `CONFLICTING_SOURCES`, `REDACTION_FAILURE` are Phase A additions, and unknown kinds are rejected, so the extension is already binding | `core/coverage_gap.py:26-37` vs `wayfinder/freeze-canonical-domain-policy-contracts.md:61`; mutation F10 caught | `requires_owner_or_policy_ruling` (MAJOR-1) |
| Q11-7 | `AuthorizationState` vs redaction failure | `REDACTION_FAILED` is a member of the authorization enum, so a redaction-failed read cannot also record whether it was authorized. Fixture `m0-read-redaction-failure-001` stores `state:"redaction_failed"` and carries the real redaction fact only as untyped `detail["redaction"]` | `core/identity.py:53-65`; `evals/fixtures/m0/m0-read-redaction-failure-001.json`; canonical contract's orthogonality resolution at `freeze:37-39` | `unratified_semantic_choice` (MAJOR-2) |
| Q11-8 | Seam `packet_reference` values | 8 of 10 cite `alignment packet §N`. §3→`Canonical Flight…` (should be §5.3), §4→`Human Responsibility Contract` (should be §5.1), §6→`M1` (should be §5.4), §7→`M2` (should be P3-gated, no §), §9→`Build Envelope` (should be §11), §8→`Production Authority` (should be §12). All eight match the **superseded** draft's outline | `alignment/seams.py:112,122,133,143,153,163,173,195,205`; `packet` outline vs `m0-build-alignment-packet-draft.md` outline (that file is titled "Superseded Historical Draft") | `stale_reference_only` (MAJOR-3) |
| Q11-9 | Removed acceptance IDs cited as authority | `outcomes.py` and `identity.py` say the no-body rule is stated "independently" by "the alignment packet draft (`M0-SEC-001`)" and "the CE plan (`M0-READ-001`, `M0-SEC-001`)". Repository-wide grep: those IDs survive **only** in these two comments, the superseded draft, and prior review prose. The current registry is `VAL-*`, and the two cited "independent" sources were the same colliding strings | `adapters/outcomes.py:44-46`, `core/identity.py:71-75`; `packet:230-263` | `stale_reference_only` (MAJOR-4) |
| Q11-10 | Seam authority is untested | `test_every_seam_names_its_reason_authority_and_phase_b_unit` asserts only `.strip()` truthiness. Replacing a `packet_reference` with garbage, or a `blocked_reason` with `"stale text nobody checks"`, passes 225/225. The test's own example binding names the superseded draft | `tests/test_alignment_seams.py:52-57,81`; mutations E05, E06 SURVIVED | `stale_reference_only` (MAJOR-3, mechanism) |
| Q11-11 | Packet / UI / acceptance-ID / fixture-baseline / budget seams | `SEAM-M0-05/07/06/08/10` all raise; no packet field set, first-screen hierarchy, VAL registry, baseline arm, or budget cap exists in code | probe `seam.*`, all 10 raise `AlignmentPendingError` | `semantics_independent` |
| Q11-12 | Post-edit coordinated fields, legal pairs, power/MDE, arm parity | Zero occurrences in the package; blocked by absence plus seams 01/02/04 | grep across `*.py`/`*.json`: 0 hits for each term | `semantics_independent` |
| Q11-13 | Provisional mechanism as accidental contract — fixture schema | `_REQUIRED_FIXTURE_KEYS` is an exact-key contract and rejects both extra and missing keys. It carries `m0-fixture-read/v0` and a version check, so it is replaceable by design | `adapters/fixture.py:52-67,145-149`; probes `fixture.EXTRA_key`, `fixture.SCHEMA_version_drift` | `semantics_independent` |
| Q11-14 | Provisional mechanism as accidental contract — `ReadOutcome` | 8 outcomes with no mapping to readiness; the mapping is explicitly deferred to `SEAM-M0-01` | `adapters/outcomes.py:9-11,21-31` | `semantics_independent` |
| Q11-15 | `DEFAULT_GAP_KIND_BY_OUTCOME` | `BLOCKED → MISSING_AUTHORITY` while the `blocked` fixture records `state:"not_evaluated"` (no authorization check ran). Naming that "missing authority" is a small inference beyond the recorded fact | `adapters/outcomes.py:68`; `evals/fixtures/m0/m0-read-blocked-001.json` | `unratified_semantic_choice` (MINOR-5) |
| Q11-16 | Canonical-JSON deviations | The module documents only the key-sort deviation from RFC 8785. It also emits `1e-07` (JCS requires `1e-7`) and `-0.0` (JCS requires `0`), and `1` vs `1.0` are distinct digests | `core/canonical_json.py:21-24`; probes `cj.smallfloat_encode`, `cj.float_neg0_encode`, `cj.int_vs_float_collision` | `stale_reference_only` (MINOR-3) — documented deviation list is incomplete, not a bug |

**Q11 answer.** Phase A remains semantics-independent and replaceable on every decision the
packet owns. It has not silently selected a readiness, check, packet, or UI meaning. It has
silently selected two *vocabularies* (Coverage Gap kinds, authorization states) that exceed
or reshape the closed canonical contract, and its authority citations have gone
comprehensively stale against the post-edit packet with no mechanical detection.

## 6. Q12 — independent mechanical verification

### 6.1 Claim / probe / result table

| # | Claim under test | Probe | Result | Evidence |
| --- | --- | --- | --- | --- |
| 1 | Suite is green from any working directory | Full suite from repository root, package root, `/private/tmp`, and an unrelated tmp dir; `PYTHONDONTWRITEBYTECODE=1 -p no:cacheprovider` | **CONFIRMED** 225 passed × 4 | §4 |
| 2 | Deterministic bytes across processes and hash seeds | 9 fresh processes, `PYTHONHASHSEED` ∈ {0,1,42,99991,4294967295,random,12345}, live bytes and isolated copy | **CONFIRMED** identical 47 274 bytes, `sha256 7837c3e6…c044375`, identical run/log digests and receipt ids in all 9 | probe_determinism |
| 3a | Deep immutability | Mutate the source dict after construction; write to top-level and nested `detail` | **CONFIRMED** digest unchanged; nested writes raise `TypeError: 'mappingproxy' object does not support item assignment`; nested lists become tuples | probe_objects2 |
| 3b | Append-only, seal, chain | Same-entity reorder / drop-middle / duplicate; append, `setattr`, private-list append after seal | **CONFIRMED** all raise `AppendOnlyViolation` (or `AttributeError` on the frozen storage) | probe_chain, probe_objects2 |
| 3c | Duplicate-receipt handling | `record_receipt(log, same_receipt)` twice | **PARTIAL** the core store accepts it and records revision 1 superseding revision 0 — an identical receipt logged as its own correction. Only `runner/hermetic.py:148-150` rejects it | probe_objects2 `log.append_DUPLICATE_receipt` → index 1 (MINOR-1) |
| 3d | Seal-chain verification depth | Tamper `payload_digest` / `revision_digest` / `payload` on a recorded revision, then `verify_chain()` and `seal()` | **FALSIFIED as "verification"** both pass. `verify_chain` checks index monotonicity and `supersedes` linkage only; it never recomputes a digest, and no `Revision`/`Receipt` exposes a verify entry point | probe_chain `digest.tampered_seal` → ok; `dir()` verify methods → `[]` (MAJOR-5) |
| 3e | Build-receipt binding | Mutations H07/H08/H09 remove `input_digest`, `revision_log_digest`, `effective_capabilities` from the build receipt | **CONFIRMED** each caught by the suite | mutate.py |
| 4 | Receipt identity sensitivity | Vary source, actor, actor_kind, authorization state, interval, recorded_at, outcome, detail, derivation inputs, Coverage Gaps, body, body-absence, receipt kind | **CONFIRMED at object level** — every one changes both `digest` and `receipt_id`. Identical derivation inputs correctly produce an identical digest | probe_objects2 identity.* |
| 4b | …is that sensitivity test-reachable? | Delete each field from `Receipt._identity_payload()` on an isolated copy | **FALSIFIED** 9 of 10 deletions pass 225/225. Only `body_digest` is locked | mutations R01–R09 SURVIVED (BLOCKER-2) |
| 5a | Fail-closed authorization parsing | 11 malformed strings (case, spacing, British spelling, zero-width char, empty) and 5 wrong types | **CONFIRMED at object level** — all raise `FixtureIntegrityError`; no alias, no default branch | probe_fixture auth.* |
| 5b | …is that fail-closed behavior test-reachable? | Make the parser return `AUTHORIZED` on any unrecognised value | **FALSIFIED** passes 225/225. The analogous guard for read outcomes (A03) *is* locked | mutation A01 SURVIVED (BLOCKER-3) |
| 5c | Exact-key fixture / manifest validation | Extra and missing keys at fixture, `source`, `authorization`, `observed_interval`, coverage-gap, manifest, and manifest-case level; schema drift; case-id mismatch; unlisted case; outcome mismatch; duplicate case; pre-decided readiness | **CONFIRMED** every one raises `FixtureIntegrityError` with a precise message. A `materiality` key planted in a fixture gap is rejected as unrecognised — fixtures cannot inject a materiality classification | probe_fixture (22 probes) |
| 6a | Canonical JSON — duplicate keys, non-finite, sets, bytes, non-string keys | Encode and decode probes | **CONFIRMED** all raise `CanonicalJSONError` | probe_objects |
| 6b | Reserved-sentinel smuggling on **encode** | `{"__kdd__": "UNKNOWN"}` as application data, top-level and nested | **CONFIRMED** rejected: "key '__kdd__' is reserved for absence sentinels" | probe_objects |
| 6c | Reserved-sentinel smuggling on **decode** | `canonical_loads('{"x":{"__kdd__":"ALIGNMENT_PENDING"}}')`; and a fixture file with a smuggled sentinel | **ASYMMETRY CONFIRMED, by design** decode reconstitutes the real singleton. This is the intended fixture mechanism for expressing absence, and a fixture can place a sentinel anywhere the schema permits (`notes`, `recorded_at`). Unregistered names and non-string names are rejected | probe_objects `cj.reserved_key_decode_SMUGGLE`; probe_fixture `fixture.SENTINEL_smuggled_into_notes` (MINOR-2) |
| 6d | Floats `1.0`, `-0.0`, lone surrogates | Encode/decode probes | **DOCUMENTED-DEVIATION + one untyped failure** `1.0`→`1.0`, `-0.0`→`-0.0`, `1e-7`→`1e-07`; a lone surrogate `dumps()` fine but `canonical_encode` raises `UnicodeEncodeError`, not `CanonicalJSONError` — fails closed at the byte layer but escapes the typed-error contract | probe_objects cj.* (MINOR-3, MINOR-4) |
| 6e | Cross-process byte stability | See row 2 | **CONFIRMED** | probe_determinism |
| 7 | Coverage-Gap materiality rule-source validation | `rule_source` ∈ {sentinel `UNKNOWN`/`MISSING`/`ALIGNMENT_PENDING`, `""`, `"   "`, `"\t\n"`, arbitrary prose, `7`, `{"id":"x"}`, versioned URI}; and the default mapping | **FALSIFIED** only sentinels are rejected. Empty, whitespace-only, arbitrary, integer, and dict rule sources all construct a classified gap. Default mapping is correct: `materiality=unknown`, `rule_source=UNKNOWN`, and no unknown→material ceiling is implemented (correctly deferred) | probe_objects gap.* (BLOCKER-1) |
| 8a | Scanner catches planted violations | 57 evasion shapes at a runtime label: aliased imports, from-imports, dead-code / function-local / class-body / `TYPE_CHECKING` imports, `io.open`, `builtins.open`, lambda and comprehension `__import__`, string-built builtin via `globals()`, `Path.open`, clock calls and clock aliases, reflection dunders, `sys.modules` writes | **CONFIRMED** 54 of 57 flagged; `delattr` with a safe literal and a string-only annotation correctly produce nothing | probe_scanner |
| 8b | Forbidden production path is unreachable | `from . import production`, `from .production import client`, `from ..adapters.production import c` | **FALSIFIED** all three produce **zero** findings. The relative-import branch compares against absolute prefixes, so `kdd_data_agent.adapters.production` is inexpressible relatively. The parallel legacy case `from ...sma import runtime` *is* caught | `tests/_import_graph.py:71-88` vs `core/capabilities.py:104-109` (MAJOR-6) |
| 8c | Scanner non-vacuity over the file set | `test_the_package_contains_no_python_files_outside_the_scanned_set` | **VACUOUS FOR SYMLINKS** both `python_files()` and the test's `on_disk` set use `rglob`, which does not recurse symlinked directories. A symlinked dir holding `evil.py` with `socket` + `subprocess` + `open` yields 0 scanner findings **and** the non-vacuity assertion still evaluates `True` | probe_scanner symlink section; `tests/_import_graph.py:50`, `tests/test_capability_allowlist.py:69-76` (MAJOR-7) |
| 8d | Scanner is genuinely reached | Plant `import socket` at the top of `core/digest.py`; empty each allowlist; unwire each scanner branch | **CONFIRMED** planted import flagged at `core/digest.py:1`; mutations C01–C11 all caught | probe_scanner, mutate.py |
| 8e | Test-file exemptions | Aliased forms under a `tests/` label | **GAP** `clock = datetime.now; clock()` and `writer = p.write_text; writer('x')` produce **no** findings in test files; the direct call forms are caught | probe_scanner tests/ section (MINOR-6) |
| 9 | Runtime audit over the exercised hermetic path | `sys.addaudithook` across import and run phases | **CONFIRMED** run phase: 17 audit events, all `open`, **all read-mode**, all 9 distinct paths inside `evals/fixtures/m0/`. Zero network, zero subprocess, zero credential/env, zero exec/compile, zero filesystem-mutation events. Zero write-mode opens. No clock or random reference in any runtime module (AST sweep) | probe_runtime_audit |
| 9b | Proof boundary | — | **This is not an OS sandbox proof.** `sys.addaudithook` observes only CPython audit events raised by the interpreter and stdlib. Native code, direct syscalls, or any capability reached without raising an audit event would not appear. It covers exactly the path this run exercised | stated, not inferred |
| 10 | Test reachability of the guards | 78 single-guard mutations, 77 applied, each on a fresh isolated copy | **20 SURVIVORS** — see §7 | mutate.py, mutate2.py |

### 6.2 One efficiency observation

`FixtureReadAdapter.read()` calls `load_manifest()` on every read
(`adapters/fixture.py:208-211`), so an 8-case run performs 9 manifest reads. The audit hook
counted 17 opens for 8 cases. Correct but O(n²) in file reads; worth noting because the
audited read surface grows with case count.

## 7. Mutation and fault-injection matrix

Baseline on the isolated copy: `225 passed`. Each probe: fresh copy, exactly one textual
mutation, anchor asserted unique and byte change asserted, full suite re-run.

| Class | Defined | Applied | Caught | Survived |
| --- | --- | --- | --- | --- |
| Receipt identity (R01–R11) | 11 | 11 | 1 | **10** |
| Fail-closed parsing (A01–A03) | 3 | 3 | 1 | **2** |
| Seal / append-only (S01–S08) | 8 | 8 (S08 re-run) | 6 | **2** |
| Capability allowlist + scanner (C01–C11) | 11 | 11 | 11 | 0 |
| Fixture guards (F01–F10) | 10 | 10 | 9 | **1** |
| Read/receipt binding (B01–B05) | 5 | 5 | 5 | 0 |
| Runner / build receipt (H01–H10) | 10 | 10 | 7 | **3** |
| Core semantics (K01–K17) | 17 | 17 | 15 | **2** |
| Seams (E01–E06) | 6 | 5 valid | 3 | **2** |
| **Total** | **81** | **80** | **60** | **20** |

E04 (delete a seam entry) is reported as an **invalid probe**: my textual splice broke the
module and pytest exited with a usage error rather than a test failure. It is not counted
as caught. E03 (rename a seam id) *is* valid and was caught by two tests.

### Survivors

| ID | Mutation | File | Suite result | Why it matters |
| --- | --- | --- | --- | --- |
| R01 | drop `source` from receipt identity | `core/receipts.py:102` | 225 passed | BLOCKER-2 |
| R02 | drop `actor` | `core/receipts.py:103` | 225 passed | BLOCKER-2 |
| R03 | drop `authorization_state` | `core/receipts.py:104` | 225 passed | BLOCKER-2 |
| R04 | drop `observed_interval` | `core/receipts.py:105` | 225 passed | BLOCKER-2 |
| R05 | drop `recorded_at` | `core/receipts.py:106` | 225 passed | BLOCKER-2 |
| R06 | drop `outcome` | `core/receipts.py:107` | 225 passed | BLOCKER-2 |
| R07 | drop `derivation_inputs` | `core/receipts.py:108` | 225 passed | BLOCKER-2 |
| R08 | drop `coverage_gaps` | `core/receipts.py:109` | 225 passed | BLOCKER-2 |
| R09 | drop `detail` | `core/receipts.py:110` | 225 passed | BLOCKER-2 |
| R11 | remove the `coverage_gaps` sequence-type guard | `core/receipts.py:82-83` | 225 passed | MINOR-7 |
| A01 | authorization parse fails **open** to `authorized` | `adapters/fixture.py:292-298` | 225 passed | BLOCKER-3 |
| A02 | non-string authorization coerced with `str()` | `adapters/fixture.py:290-291` | 225 passed | **near-equivalent mutant** — `str(x)` still hits the enum lookup and still rejects. Not counted as a real gap |
| S01 | `seal()` no longer calls `verify_chain()` | `core/revisions.py:184` | 225 passed | MAJOR-5 |
| S05 | remove the immutable-storage guard in `append` | `core/revisions.py:128-129` | 225 passed | MINOR-8 (S04 covers the same path) |
| F09 | remove the fixture-root containment check | `adapters/fixture.py:134-135` | 225 passed | MAJOR-8 |
| H02 | remove the duplicate-receipt guard | `runner/hermetic.py:148-150` | 225 passed | MINOR-1 |
| H04 | remove the pre-seal `verify_chain()` call | `runner/hermetic.py:156` | 225 passed | MAJOR-5 |
| H06 | remove the sealed-log requirement from the run result | `runner/hermetic.py:101-102` | 225 passed | MAJOR-5 |
| K10 | unregistered sentinel name silently becomes `UNKNOWN` | `core/unknown.py:77-78` | 225 passed | MINOR-9 — the prior status JSON lists "unregistered sentinel decode" as a blocked injection; it *is* blocked at object level but nothing locks it |
| K11 | `require_known` no longer raises | `core/unknown.py:96-97` | 225 passed | MINOR-10 — `require_known` and `is_known` have **zero call sites** in the package |
| E05 | seam `packet_reference` → `"TOTALLY WRONG AUTHORITY"` | `alignment/seams.py:205` | 225 passed | MAJOR-3 mechanism |
| E06 | seam `blocked_reason` → `"stale text nobody checks"` | `alignment/seams.py:107-111` | 225 passed | MAJOR-3 mechanism |

### Minimal corrections, validated by re-running the mutations

I did not only propose fixes; I applied them to isolated copies and re-ran the battery.

| Correction | Clean run | Kills |
| --- | --- | --- |
| One golden byte vector: `assert sha256(run_foundation(frozen_run_input, adapter).serialize()) == "7837c3e6…c044375"` added to `tests/test_deterministic_replay.py` | **226 passed** | R01, R02, R03, R05, R09 — each now `1 failed, 225 passed` |
| One fail-closed parsing test asserting `FixtureIntegrityError` for 5 malformed strings and 4 wrong types | **226 passed** | A01 — now `1 failed, 225 passed` |

Both satisfy the revert test in both directions: the new test passes on unmutated bytes and
fails on the mutated bytes. Two small tests close nine of the twenty survivors.

**Root cause of the R-class survival.** The suite contains exactly **two** hard-coded
digest constants, both in `tests/test_digest.py:25-26`, both over trivial values (`{"a":1}`
and the `UNKNOWN` sentinel). No golden vector pins any `Receipt`, `Revision`, `ReadResult`,
or `FoundationRunResult`. The determinism tests compare run *N* against run *N+1*, which is
self-referential: a mutation that changes every run identically is invisible to them. The
guard is correct; the lock is tautological.

## 8. Findings

### BLOCKER

**BLOCKER-1 — the materiality rule-source guard does not require a named versioned rule, and three documents claim it does.**
`core/coverage_gap.py:71-75` rejects only a *sentinel* `rule_source`. Constructing
`CoverageGap(kind=TIMEOUT, reason="r", materiality=Materiality.NON_MATERIAL, rule_source="")`
succeeds, as do `"   "`, `"\t\n"`, `"because I said so"`, `7`, and `{"id":"x"}`.
The module docstring at `core/coverage_gap.py:7-11` states this "makes an invented policy
fail at construction time instead of quietly shipping";
`m0-prealignment-foundation-receipt.md:302` and `m0-freeze-opus5-adversarial-review.md:421`
both assert that classification "without a versioned `rule_source`" raises. All three claims
are false as written.
*Consequence.* `non_material` is the classification that suppresses a blocker. The one
mechanical control standing between "the Owner has not frozen materiality policy" and "a gap
was quietly declared immaterial" accepts an empty string. This is packet Stop Condition 1
(`packet:288`) — a fail-closed default bypassed by a permissive branch — in the exact place
`SEAM-M0-03` promises to hold open.
*Minimal correction.* Require a non-empty string matching a versioned shape, e.g. reject
unless `isinstance(rule_source, str) and rule_source.strip()` and it matches a
`rule://…/v<N>` or equivalent pattern the Owner names; add the empty/whitespace/arbitrary
cases to `tests/test_receipts_and_gaps.py`. Mutation K01 already proves the guard's
existence is test-reachable, so only its strictness needs the new cases.

**BLOCKER-2 — receipt identity is not test-reachable: 9 of 10 identity fields can be deleted with the suite still green.**
`core/receipts.py:100-112`. Deleting `source`, `actor`, `authorization_state`,
`observed_interval`, `recorded_at`, `outcome`, `derivation_inputs`, `coverage_gaps`, or
`detail` from `_identity_payload()` each leaves 225/225 passing. Only `body_digest` (R10)
is locked.
*Consequence.* "Every visible conclusion in M0 must resolve to a receipt" is the package's
central claim, and receipt identity is what makes a receipt quotable. Today the behavior is
correct — my object-level probes confirm all fourteen field variations change both `digest`
and `receipt_id` — but nothing prevents the next change from silently collapsing two
different reads onto one receipt id. This is one of the defects the handoff names as
previously reported; the package aggregate is unchanged since the continuation receipt, so
it was never addressed.
*Minimal correction.* Add the golden byte vector validated in §7. One assertion, verified
here to kill R01/R02/R03/R05/R09 while passing on unmutated bytes.

**BLOCKER-3 — fail-open authorization parsing is not test-reachable.**
`adapters/fixture.py:288-298`. Replacing the `except ValueError` branch with
`return AuthorizationState.AUTHORIZED` passes 225/225.
*Consequence.* `AUTHORIZATION_STATES_PERMITTING_BODY = {AUTHORIZED}`
(`core/identity.py:68`) is the sole gate on retaining a source body. A fail-open parse would
let a fixture declaring `state: "totally-bogus"` be treated as authorized and keep its body,
which is the no-raw-leakage invariant the package calls a security invariant rather than a
product decision. The analogous guard next door, `parse_read_outcome` (A03), *is* locked by
6 tests — the asymmetry reads as an oversight, not a decision.
*Minimal correction.* Add the fail-closed parsing test validated in §7.

### MAJOR

**MAJOR-1 — `CoverageGapKind` extends a closed canonical enumeration by four kinds, and the extension is already binding.**
`core/coverage_gap.py:26-37` defines 9 kinds. `freeze-canonical-domain-policy-contracts.md:61`
enumerates 5: missing authority, timeout, unavailable source, unknown mapping, unchecked
evidence plane. `PARTIAL_READ`, `STALE_READ`, `CONFLICTING_SOURCES`, and `REDACTION_FAILURE`
are Phase A additions. The docstring says "Extending this enum is a Phase B decision"; Phase A
extended it, and `adapters/fixture.py:345-351` rejects any kind outside the 9 (mutation F10
caught), so Phase B inherits a locked taxonomy.
*Consequence.* Four gap kinds enter the M0 vocabulary without a policy ruling, and a Phase B
kind the Owner does want is rejected at fixture load.
*Minimal correction.* Owner or policy ruling on whether the canonical five are exhaustive.
If they are, map the four additions onto them and record the mapping; if not, amend the
canonical contract. Do not resolve this in code.

**MAJOR-2 — `AuthorizationState` folds redaction failure into the authorization axis, destroying the authorization fact.**
`core/identity.py:53-65`. `REDACTION_FAILED` is a member of the enum, so a read cannot record
both "the principal was authorized" and "redaction failed". Fixture
`m0-read-redaction-failure-001.json` demonstrates the loss: `state: "redaction_failed"`, with
the actual redaction fact (`"required_but_not_applied"`) surviving only as untyped
`receipt.detail["redaction"]`. Packet check 16 (`packet:105`) treats authorization and
redaction as separate items, and the canonical contract's headline resolution is "orthogonal
state dimensions … No field implicitly changes another field" (`freeze:37-39`).
*Consequence.* A redaction-failed read is indistinguishable from an authorization-unknown
read on the typed axis, and the fact that governs body retention is decided by an enum that
conflates two questions.
*Minimal correction.* Separate `redaction_state` from `authorization_state` as its own typed
field, and make `AUTHORIZATION_STATES_PERMITTING_BODY` consult both. This changes a Phase A
vocabulary, so it needs the Owner's ruling before the code moves.

**MAJOR-3 — every seam authority citation is stale, and nothing detects it.**
`alignment/seams.py:112,122,133,143,153,163,173,195,205`. Eight seams cite
`alignment packet §N`. Against the current packet: §3 is *Canonical Flight and Decision
Metric Contract* (readiness outcome is §5.3), §4 is *Human Responsibility Contract* (required
input is §5.1), §6 is *M1* (M0 output is §5.4), §7 is *M2* (first screen has no section), §9
is *Build Envelope and Continuity* (acceptance scenarios are §11), §8 is *Production
Authority and Old SMA* (stop conditions are §12). All eight match the outline of
`m0-build-alignment-packet-draft.md`, whose own first line reads "Superseded Historical
Draft". `SEAM-M0-01`'s `blocked_reason` still describes a two-vs-three-outcome question the
packet replaced with coordinated fields; `SEAM-M0-02` still says "the draft lists 14 checks"
against a 19-check inventory. `AlignmentPendingError` prints
`Authority: {packet_reference}` (`alignment/seams.py:46`), so a Phase B implementer is
actively directed to the wrong section at the moment they hit the seam.
`tests/test_alignment_seams.py:52-57` asserts only that these strings are non-empty; mutations
E05 and E06 confirm arbitrary garbage passes 225/225. The test's own example binding at
`tests/test_alignment_seams.py:81` names the superseded draft.
*Consequence.* The seam registry is the checklist Phase B is supposed to work from. It
currently points at a document the corpus marks as not-an-implementation-contract.
*Minimal correction.* Repoint all ten `packet_reference` values at the current packet's
sections, refresh the two stale `blocked_reason` texts, and add a test that each
`packet_reference` names a section heading that exists in the bound packet.

**MAJOR-4 — two comments cite removed acceptance IDs as independent agreeing authority.**
`adapters/outcomes.py:44-46` and `core/identity.py:71-75` justify the no-retained-body rule
by "the alignment packet draft (`M0-SEC-001`)" and "the CE plan (`M0-READ-001`,
`M0-SEC-001`)" stating it "independently". Repository-wide grep: those identifiers survive
only in these two comments, in the superseded draft, and in prior review prose. The current
registry is `VAL-*` (`packet:230-263`), and the two "independent" sources were the same
colliding strings that `SEAM-M0-06` exists to resolve.
*Consequence.* A security invariant is justified by a corroboration that does not exist. The
rule itself is sound and locked (mutations B05, F01, K14 all caught) — the *warrant* is
false.
*Minimal correction.* Recite `VAL-SEC-001` and packet §5.4, and drop the independence claim
or name two genuinely distinct current sources.

**MAJOR-5 — "seal-chain verification" is weaker than its name, and its wiring is untested.**
Three findings in one mechanism. (a) `RevisionLog.verify_chain()`
(`core/revisions.py:189-207`) checks only revision-index monotonicity and `supersedes`
linkage; it never recomputes `payload_digest` or `revision_digest`. Tampering both on a
recorded revision and then calling `verify_chain()` and `seal()` — both pass. No `Revision`
or `Receipt` exposes any verify entry point (`dir()` yields no verify method), so a
content-addressed record has no way to check its own address. (b) Removing
`self.verify_chain()` from `seal()` (`core/revisions.py:184`) passes 225/225 — S01. (c)
Removing `log.verify_chain()` from the runner (`runner/hermetic.py:156`) — H04 — and removing
the sealed-log requirement from `FoundationRunResult` (`runner/hermetic.py:101-102`) — H06 —
both pass 225/225.
*Consequence.* The suite proves `verify_chain` rejects a broken chain (S02 caught) but never
proves it is *reached*, and "seal" implies an integrity check it does not perform.
*Minimal correction.* Have `verify_chain` also recompute each revision's digest, add a test
asserting `seal()` raises on a broken chain (not only that `verify_chain()` does), and assert
`FoundationRunResult` rejects an unsealed log.

**MAJOR-6 — the forbidden production-adapter path is reachable by relative import and the scanner cannot express it.**
`core/capabilities.py:104-109` declares `kdd_data_agent.adapters.production` unreachable.
`tests/_import_graph.py:71-88` handles relative imports by testing the relative module string
against the same *absolute* prefixes, so `from . import production`,
`from .production import client`, and `from ..adapters.production import c` all produce zero
findings. The parallel legacy case works — `from ...sma import runtime` is caught, because
`"sma"` is both the prefix and the relative name.
*Consequence.* The runtime package uses relative imports throughout, so this is exactly how
an implementer would write the forbidden import. The only surviving control is
`test_production_adapter_path_does_not_exist`, a directory-existence check — one layer where
the design intends two.
*Minimal correction.* In the relative branch, reconstruct the absolute module name from the
importing file's package position before comparing, or add `"production"` and
`"adapters.production"` to a relative-prefix denylist. Add the three shapes to
`PLANTED_VIOLATIONS`.

**MAJOR-7 — the scanner's non-vacuity test is vacuous for symlinked directories.**
`tests/test_capability_allowlist.py:69-76` compares `python_files()` against an on-disk
`rglob` set. `tests/_import_graph.py:50` also uses `rglob`. Neither recurses symlinked
directories, so both sides miss the same files and the assertion still evaluates `True`.
Demonstrated: a symlinked directory inside the package containing `evil.py` with `import
socket`, `import subprocess`, and `open('x','w')` produced **0** scanner findings, was absent
from both sets, and left the non-vacuity assertion satisfied. `import
kdd_data_agent.linked.evil` would nonetheless work at runtime.
*Consequence.* The one test whose stated job is "a scanner that always returns zero findings
would also report a clean package" can be defeated without any assertion firing. Exploiting
it requires write access to the package tree, so this is a hole in the mechanical control,
not a live escape.
*Minimal correction.* Enumerate with `rglob("*.py", recurse_symlinks=True)` (Python 3.13+) or
walk explicitly, and assert no symlinked directory exists under the package root.

**MAJOR-8 — the fixture-root containment backstop is untested.**
`adapters/fixture.py:134-135`. Removing the `is_relative_to(self._root)` check passes
225/225 — F09. The check does work today: a symlink inside the fixture root pointing at
`/etc/hosts` is refused with "resolves outside the fixture root". No test reaches it, and no
test mentions containment at all.
This composes with a second weakness: `CASE_ID_PATTERN`
(`adapters/fixture.py:50`) is applied with `re.match` and `$`, so `$` matches before a
trailing newline and `validate_case_id("m0-read-trusted-001\n")` **passes**. Today that id
simply fails at `is_file()`, so there is no live traversal — but the docstring's claim that
path traversal "has no expressible form" (`adapters/fixture.py:6-7`) rests on a pattern that
is one metacharacter from strict while its backstop is unlocked.
*Minimal correction.* Use `fullmatch` or `\Z` in `CASE_ID_PATTERN`, and add a symlink-escape
test against a temporary fixture root.

### MINOR

| ID | Finding | Evidence | Minimal correction |
| --- | --- | --- | --- |
| MINOR-1 | Recording the *same* receipt twice is accepted by the core store and logged as revision 1 superseding revision 0 — an identical receipt recorded as its own correction. Only the runner rejects it, and that guard is untested (H02 survived) | `core/revisions.py:114-155`, `runner/hermetic.py:148-150`; probe `log.append_DUPLICATE_receipt` → index 1 | Reject an append whose payload digest equals the current head's, or add a test for the runner guard |
| MINOR-2 | `canonical_loads` reconstitutes a sentinel from any `{"__kdd__": name}` object while `canonical_dumps` rejects the same shape as application data. Intended for fixtures, but any future caller decoding untrusted JSON inherits sentinel injection | `core/canonical_json.py:124-132` vs `:76-89`; probe `fixture.SENTINEL_smuggled_into_notes` → `<ALIGNMENT_PENDING>` | Document the asymmetry in the module docstring and gate reconstitution behind an explicit `trusted=` flag |
| MINOR-3 | The documented RFC 8785 deviation list covers only key sorting. Number formatting also deviates: `1e-07` (JCS: `1e-7`), `-0.0` (JCS: `0`), and `1` vs `1.0` digest differently | `core/canonical_json.py:21-24`; probes `cj.smallfloat_encode`, `cj.float_neg0_encode`, `cj.int_vs_float_collision` | Extend the deviation note; it is a documentation gap, not a bug |
| MINOR-4 | A lone surrogate raises `UnicodeEncodeError` from `canonical_encode`, not `CanonicalJSONError`, escaping the typed-error contract. It still fails closed | `core/canonical_json.py:119-121`; probe `cj.lone_surrogate_encode` | Catch and re-raise as `CanonicalJSONError` |
| MINOR-5 | `DEFAULT_GAP_KIND_BY_OUTCOME[BLOCKED] = MISSING_AUTHORITY`, but the `blocked` fixture records `state: "not_evaluated"` — no authorization check ran, which is not the same as missing authority | `adapters/outcomes.py:68`; `m0-read-blocked-001.json` | Map `blocked` to `UNCHECKED_PLANE`, or state the inference in the docstring |
| MINOR-6 | Test files may reach the wall clock and the filesystem through an alias: `clock = datetime.now; clock()` and `writer = p.write_text; writer('x')` produce no findings under a `tests/` label; the direct call forms are caught | `tests/_import_graph.py:107`; probe_scanner tests/ section | Exempt only `read_text`/`read_bytes` references in tests, not clock and write shapes |
| MINOR-7 | The `coverage_gaps` sequence-type guard is untested (R11 survived) | `core/receipts.py:82-83` | Add a test passing a bare `CoverageGap` and a non-sequence |
| MINOR-8 | The immutable-storage guard in `append` is untested (S05 survived); S04 covers the same path, so impact is low | `core/revisions.py:128-129` | Fold into the seal test |
| MINOR-9 | `sentinel_from_name` rejecting an unregistered name is untested (K10 survived), although `m0-freeze-opus5-review-status.json:138` lists "unregistered sentinel decode" among blocked injections | `core/unknown.py:77-78` | Add the case to `tests/test_canonical_json.py` |
| MINOR-10 | `require_known` and `is_known` have **zero call sites** in the package, and removing the raise passes 225/225 (K11) | `core/unknown.py:85-98`; grep for call sites returns none | Either wire them at the boundary they were written for or delete them |
| MINOR-11 | Nested `tests` directories (e.g. `core/tests/x.py`) receive the permissive test import allowlist because `is_test` matches any path part, while the call-shape exemptions match only a leading `tests/`. Inconsistent scoping | `tests/_import_graph.py:54` vs `:107,195` | Use the same leading-segment rule in both places |
| MINOR-12 | `read()` re-reads and re-validates `manifest.json` once per case: 9 manifest opens for 8 cases | `adapters/fixture.py:208-211`; audit hook counted 17 opens | Load the manifest once per adapter instance |

## 9. Untested boundaries

Reported as untested rather than inferred as passing.

1. **OS-level sandboxing.** The runtime evidence is a CPython audit hook, which observes only
   interpreter- and stdlib-raised audit events. Native extensions, direct syscalls, or
   capabilities reached without an audit event are outside it. No `seccomp`, container, or
   network-namespace proof was attempted.
2. **Any path the run did not exercise.** The audit evidence covers the eight fixture cases in
   the shipped manifest. Error paths, alternative adapters, and unexercised branches carry no
   runtime evidence.
3. **Cross-language digest agreement.** Verified identical across CPython 3.14.4 processes
   only. No second Python version, implementation, or language was tested; per MINOR-3 the
   number formatting would not match a JCS implementation.
4. **Concurrency.** `RevisionLog` was exercised single-threaded only. No claim is made about
   concurrent append or seal.
5. **Equivalent-mutant census.** 80 mutations were applied. A02 is identified as a
   near-equivalent mutant; the remaining 19 survivors were each traced to a specific missing
   assertion, but I did not prove that none of the 60 caught mutations is caught for an
   incidental reason.
6. **The `.pytest_cache` and `.omc` directories** were excluded from the aggregate by the
   receipted method and were not reviewed as package content.
7. **Fixture semantic realism.** I verified fixture *integrity* and *schema*, not whether the
   eight cases are representative of real experiment reads. `SEAM-M0-08` holds that open.
8. **Prior review's 22-probe battery.** I did not attempt to reproduce it probe-for-probe; I
   ran an independent 80-probe battery instead. Where the two disagree — notably on receipt
   identity and authorization parsing — my results are bound to the commands in §4.
9. **The packet itself.** This review verifies Phase A against the packet. It does not review
   the packet's product content, and it records no verdict on the freeze candidate.

## 10. Verdict and separated proof states

### Phase A verdict: `PASS_WITH_GAPS`

Every material *runtime* claim I could test independently holds against the live bytes:
determinism to the byte across 9 processes and 6 hash seeds, deep immutability, append-only
and seal enforcement, receipt identity sensitivity across all fourteen field variations,
fail-closed parsing on 16 malformed authorization inputs and 7 malformed outcomes, exact-key
fixture and manifest validation across 22 shapes, canonical-JSON rejection of duplicate keys,
non-finite numbers, sets, bytes, non-string keys and reserved-key smuggling on encode, path
traversal refused in 15 shapes, all ten seams raising, and zero network, subprocess,
credential, exec, write, or out-of-surface read events on the exercised path.

No unratified *decision* remains: Phase A has not chosen a readiness, check-inventory,
packet, acceptance-ID, or UI meaning.

It is `PASS_WITH_GAPS` rather than `PASS` because three material claims made *about* the
package are false — the materiality rule-source guard (BLOCKER-1), and the receipted
sufficiency of the suite over receipt identity (BLOCKER-2) and authorization parsing
(BLOCKER-3) — and because two vocabularies were chosen without a ruling (MAJOR-1, MAJOR-2)
while every authority citation went stale (MAJOR-3, MAJOR-4).

It is not `FAIL` because no guard I tested behaves incorrectly on the live bytes, no seam is
open, and the foundation is replaceable exactly where it promises to be. The defects are in
the proof apparatus and the citations, and §7 demonstrates that two small tests close nine of
the twenty survivors.

**Gaps that block M0-F0 acceptance:** BLOCKER-1, BLOCKER-2, BLOCKER-3, MAJOR-5, MAJOR-6,
MAJOR-7, MAJOR-8. These are all mechanical and all have validated minimal corrections.

**Gaps that require an Owner or policy ruling before Phase B consumes the vocabulary:**
MAJOR-1 (Coverage Gap taxonomy) and MAJOR-2 (authorization vs redaction). Codex should not
resolve these in code.

**Gaps that must close before the seam registry is used as the Phase B checklist:** MAJOR-3
and MAJOR-4.

### The four proofs, kept separate

| Proof | State | Basis |
| --- | --- | --- |
| 1. Phase A foundation verification | **`PASS_WITH_GAPS`** | This review, bound to aggregate `2f1001b9…9f15bf7d1e` |
| 2. Local fixture-backed M0 MVP completion | **NOT PROVEN, and not in scope here** | Phase A implements no check, no contract, no packet, and no readiness decision. All ten seams raise. Eight synthetic fixture cases exercise a read path, nothing more |
| 3. Production authorization | **NOT GRANTED** | No production adapter exists; `adapters/production/` is absent and asserted absent. P2 is not closed. Nothing in this review touches production access |
| 4. Experiment Review Committee acceptance | **NOT APPLICABLE** | An external human ruling. No technical result substitutes for it |

### May M0-F1 start on this evidence alone?

**No.** A Phase A pass verifies that the foundation is sound and semantically independent. It
does not freeze the packet, does not authorize `M0-F1` through `M0-F5`, does not prove the
local M0 MVP, does not authorize production access, and does not stand in for Committee
acceptance.

`M0-F1` requires, separately from this review: an accepted freeze binding recording the
packet path, revision label, and SHA-256 together with the independently bound
`final-architecture-spec.md` digest; and a fresh Owner authorization and start receipt naming
the active-time cap, run/read/tool cap, expiry, and halt owner. The packet states this itself
at line 7, and the continuation authorization `m0-codex-continuation-20260817` is recorded as
exhausted. Neither exists today.

## 11. Boundaries observed

- No Phase A source, test, or fixture was modified: the package aggregate is
  `2f1001b93b19b2318c4c6419205ed2f7778ac23c02533e78a0c0899f15bf7d1e` at the end of the review,
  identical to the start, with a byte-identical 42-file manifest.
- No canonical document, packet, plan, ADR, receipt, or prior review was edited.
- No freeze record and no implementation handoff was written.
- Nothing was committed, pushed, or opened as a PR. No dependency was installed. No production
  system, external service, or message channel was touched.
- The dirty worktree was preserved: `git status` shows the same four modified tracked files
  and the same untracked set as at session start.
- Every mutation and fault injection ran on an isolated copy under
  `/private/tmp/phaseA-indep-2026-08-18/`, which is removed when this review ends. The live
  package was imported read-only with `PYTHONDONTWRITEBYTECODE=1` throughout.
- Only the two authorized output files were written.

## 12. Output-file digests

Computed with `shasum -a 256` after writing. A file cannot contain its own digest, so this
report's digest is recorded in the companion status JSON, and the JSON's digest is reported in
the session summary rather than inside either file.

| File | Digest location |
| --- | --- |
| `phase-a-independent-review.md` | `phase_a_independent_status.json` → `output_files.markdown_sha256` |
| `phase-a-independent-status.json` | reported in the session summary; self-excluding |
