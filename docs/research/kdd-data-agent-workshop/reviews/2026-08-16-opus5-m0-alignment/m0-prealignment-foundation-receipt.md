---
handoff_id: m0-prealignment-foundation-20260816
phase: A
status: complete, blocked at the alignment gate
package_root: .agents/skills/kdd_data_agent/
---

# M0 Pre-Alignment Foundation — Build Receipt (Phase A)

Phase A is complete. Phase B has not started and will not start until the main
session supplies the exact frozen M0 Build Alignment Packet path and SHA-256.

A green Phase A is progress, not proof that M0 is finished.

## 1. Owned files

Everything below is new. Nothing outside this list was created, edited, or
deleted by this session.

**Runtime source — 2,138 lines across 17 modules**

```
.agents/skills/kdd_data_agent/
  README.md
  ENGINEERING_DECISIONS.md          # M0-F0 decision record
  TOOLCHAIN_RECEIPT.md              # keep-or-replace assessment
  __init__.py
  alignment/__init__.py
  alignment/seams.py                # 10 registered seams, all raising
  core/__init__.py
  core/unknown.py                   # UNKNOWN / MISSING / ALIGNMENT_PENDING
  core/canonical_json.py            # canonical serialization seam
  core/digest.py                    # sha256 content digests, content-addressed ids
  core/identity.py                  # source, actor, authorization, interval
  core/coverage_gap.py              # Coverage Gaps, materiality gated
  core/revisions.py                 # append-only revision log
  core/receipts.py                  # receipt primitive
  core/capabilities.py              # positive capability + import allowlist
  adapters/__init__.py
  adapters/outcomes.py              # 8 typed read outcomes
  adapters/base.py                  # ReadAdapter / ReadRequest / ReadResult
  adapters/fixture.py               # fixture-only read adapter
  runner/__init__.py
  runner/hermetic.py                # deterministic foundation run
```

**Fixtures — 9 files**

```
  evals/fixtures/m0/manifest.json
  evals/fixtures/m0/m0-read-trusted-001.json
  evals/fixtures/m0/m0-read-blocked-001.json
  evals/fixtures/m0/m0-read-partial-001.json
  evals/fixtures/m0/m0-read-stale-001.json
  evals/fixtures/m0/m0-read-conflicting-001.json
  evals/fixtures/m0/m0-read-unauthorized-001.json
  evals/fixtures/m0/m0-read-unavailable-001.json
  evals/fixtures/m0/m0-read-redaction-failure-001.json
```

All fixture content is synthetic. No real, production, or de-identified company
data, and no content derived from protected domain assets (that derivation
question is an open Owner decision, registered as `SEAM-M0-08`).

**Tests — 1,315 lines, 168 cases**

```
  tests/__init__.py
  tests/conftest.py
  tests/_import_graph.py            # AST capability scanner (test-only)
  tests/test_canonical_json.py      # 28
  tests/test_digest.py              # 15
  tests/test_revisions.py           # 14
  tests/test_receipts_and_gaps.py   # 13
  tests/test_fixture_adapter.py     # 36
  tests/test_capability_allowlist.py# 26
  tests/test_deterministic_replay.py#  9
  tests/test_alignment_seams.py     # 27
```

**Outside the package**

```
  docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/
    m0-prealignment-foundation-receipt.md      # this file
    m0-prealignment-foundation-status.json     # status writeback (pre-existing path)
```

## 2. Toolchain decision and replacement boundary

Full record: `.agents/skills/kdd_data_agent/ENGINEERING_DECISIONS.md`.

**Keep-or-replace assessment: KEEP.** Full receipt at
`.agents/skills/kdd_data_agent/TOOLCHAIN_RECEIPT.md`, scored against the
Champion (`champion-repo-reverse-audit.md`), Fourth-place
(`fourth-place-repo-reverse-audit.md`), and DeepSeek Harness
(`deepseek-harness-practices.md`) audits on production integration,
deterministic behavior, capability isolation, testability, UI integration,
license, and migration cost. Summary: the three references are strongest where
M0 does not yet need them (orchestration under real workloads) and weakest
where M0 is load-bearing — none has an append-only evidence ledger with
source-read receipts, and two fail open on the decisive paths. Each audit says
so in its own words: the champion is "GO as a bounded-mechanism reference;
NO-GO as the greenfield architecture base"; the fourth-place audit is "not a
suitable production foundation" and sequences its own rebuild as "P0: Build the
trust boundary first"; the DeepSeek Harness "is not an enterprise evidence
system". Phase A is that P0 substrate. The sharpest single lesson taken from
the references is a fourth-place finding: its default tool registry exposes no
shell or Python, yet the shipped image still contains 114 dormant
`python_exec.py` files that `exec()` arbitrary Python, selected by an
environment variable — which is why the capability check here scans everything
present rather than asserting something about the intended entry point.
Fourteen named
mechanisms are reused, including six from the TypeScript DeepSeek Harness
(interrupted work closes as `unknown` and is never blindly retried; monotonic
deny in a non-replaceable boundary; fail-closed approval where only an explicit
grant counts; byte-identical receipts under fixed inputs; append-only ledger
that is never summarized away; `Trace ≠ Evidence`). Four gaps are named rather
than hidden (no crash/resume semantics, no budget accounting, no Trace
projection, static-only capability scanning), and four explicit replace-triggers
are recorded. Python remains a **provisional** M0-F0 engineering choice.

| Item | Choice | Replacement boundary |
| --- | --- | --- |
| Package root | `.agents/skills/kdd_data_agent/` — the root both the sequencing document and the CE plan propose, and a directory that did not previously exist | Directory rename plus one `sys.path` line in `tests/conftest.py` |
| Language | Python 3.14, standard library only, zero dependencies, no frameworks — **provisional M0-F0 engineering choice, not an Owner-frozen architecture decision** | Semantics live in enums, frozen records, and canonical JSON, all language-independent; a port replaces implementations, not meanings |
| Test command | `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider .agents/skills/kdd_data_agent/tests -q` | Tests are plain functions and `assert`; only `pytest.raises` and `parametrize` are framework-specific |
| Schema boundary | Code-defined frozen dataclasses, canonical JSON on the wire; no schema DSL, no codegen, no validation library | JSON Schema or protobuf can be layered later without changing any stored digest, provided canonical bytes are preserved |
| Canonicalization | Sorted-key, separator-tight, UTF-8, sentinel-aware, idempotent | `core/canonical_json.py` is the single seam; swapping in RFC 8785 (JCS) means replacing one module and re-pinning the golden vectors |
| Digest | `sha256:<hex>`, algorithm carried in the string | A second algorithm is additive, never ambiguous |
| Persistence | In-memory append-only log; no database, no file write | `RevisionLog` (append / head / history / verify_chain) is the seam |
| Read source | `ReadAdapter`, one method | A P2-authorized production adapter implements the same protocol; the interface already carries authorization state and Coverage Gaps |

Known, documented deviation: canonical JSON sorts object keys by Unicode code
point rather than RFC 8785's UTF-16 code unit. The two orders agree for every
ASCII key, which is every key in the M0 schema boundary, and
`require_ascii_keys()` can make the difference structurally impossible.

## 3. Commands run and exact outcomes

```
$ PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider .agents/skills/kdd_data_agent/tests -q
168 passed in 0.17s
```

Run from three different working directories to prove the documented command is
not path-dependent:

```
$ cd <repo root>            && … pytest … .agents/…/tests -q  -> 168 passed in 0.17s
$ cd .agents/skills/kdd_data_agent && … pytest … tests -q     -> 168 passed in 0.15s
$ cd /Users/surahli         && … pytest … <absolute path> -q  -> 168 passed in 0.18s
```

Environment: Python 3.14.4 (Clang 17.0.0), pytest 9.0.2 — both already present
in the repository. No package was installed and no global setting was changed.

## 4. Capability and import evidence

The check is mechanical, not prose. `tests/_import_graph.py` parses the AST of
every `.py` file in the package and reports disallowed imports, forbidden
imports, legacy-path imports, forbidden builtin calls, and mutation/subprocess
call shapes. `tests/test_capability_allowlist.py` runs it over the runtime
package and over the tests, and asserts zero findings.

Positive allowlists (`core/capabilities.py`):

- Capabilities: exactly three — `fixture_read`, `local_deterministic_compute`,
  `in_memory_append`. Nothing else has a representation, so no component can
  request one. `assert_capabilities()` runs in `ReadAdapter.__init__`.
- Runtime imports: twelve standard library modules
  (`__future__`, `collections`, `dataclasses`, `datetime`, `enum`, `hashlib`,
  `hmac`, `json`, `math`, `pathlib`, `re`, `typing`). No third party.
- Tests add exactly `ast`, `importlib`, `itertools`, `pytest`, `sys`.

Explicitly unreachable and asserted:

- `socket`, `ssl`, `urllib`, `http`, `requests`, `subprocess`, `multiprocessing`,
  `os`, `shutil`, `tempfile`, `pickle`, `ctypes`, `smtplib`, `webbrowser`, and
  the rest of `FORBIDDEN_IMPORTS` — imported nowhere in runtime or tests.
- `sma` and `sma_rewrite` — imported nowhere. `git status --short` on
  `.agents/skills/sma` and `.agents/skills/sma_rewrite/evals` is empty.
- `open`, `eval`, `exec`, `compile`, `__import__`, `breakpoint`, `input`,
  `globals`, `locals`, `vars` — called nowhere. `Path.read_text` is the single
  file-read shape in the package.
- `write_text`, `write_bytes`, `mkdir`, `unlink`, `rmdir`, `rename`, `replace`,
  `chmod`, `touch`, `rmtree`, `system`, `popen`, `run` — called nowhere. The
  package and its tests never write a file, which is why fixture-integrity
  failures are exercised by calling validators directly rather than by writing
  temporary fixtures, and why the suite uses no `tmp_path` fixture (requesting
  it would have pytest create a directory and make this claim false).

  Verified empirically, not only by reading the source: a full test run creates
  and removes zero files.

  ```
  $ find .agents/skills/kdd_data_agent -type f | sort > before.txt
  $ PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider … -q
  $ find .agents/skills/kdd_data_agent -type f | sort > after.txt
  $ diff before.txt after.txt
  (no output — zero files created or removed)
  ```
- `adapters/production/` — asserted not to exist
  (`test_production_adapter_path_does_not_exist`).

Negative control: `test_the_scanner_detects_planted_violations` feeds the
scanner 15 planted violations (`import socket`, `import subprocess`,
`from urllib.request import urlopen`, `import os`, `from sma.scripts import
pipeline`, `from kdd_data_agent.adapters.production import client`,
`import numpy`, `open('f','w')`, `eval`, `exec`, `__import__`, `.write_text()`,
`.unlink()`, `.run()`, `.system()`) and requires the expected finding kind for
each. A scanner that always returned zero findings would also report a clean
package; this is the test that makes the clean result mean something.

Known scanner limits, stated rather than hidden: the scan is static and matches
call shapes syntactically. A dynamic `importlib.import_module("socket")`, an
attribute call reached through `getattr`, or an import performed inside an
`exec`'d string would evade it. `exec`, `compile`, and `__import__` are
themselves forbidden call shapes, and `importlib` is allowed only in tests, so
the residual bypass surface is a deliberate dynamic import written in a test
file. That is a knowing-insider bypass, not an accidental capability leak.

## 5. Deterministic replay evidence

In-process, `tests/test_deterministic_replay.py`:

- two independent runs over identical frozen inputs produce identical
  `serialize()` bytes, identical run digest, identical revision-log digest, and
  identical build-receipt digest;
- receipt ids repeat across runs (ids are truncated content digests, never
  random);
- `canonical_encode(canonical_loads(serialized)) == serialized`;
- a different input, or the same cases in a different order, produces a
  different digest — so the digest is sensitive, not constant;
- sets and frozensets are rejected by the canonicalizer, which is the mechanism
  that makes the output immune to `PYTHONHASHSEED`.

Cross-process, two clean runs with different hash seeds:

```
$ PYTHONHASHSEED=0     python3 scratchpad/digest_probe.py
$ PYTHONHASHSEED=12345 python3 scratchpad/digest_probe.py

run_digest      : sha256:b8ccb52f167c20ac5ff3891ffa50e6a1da624bfa6b089afe583a0b72ea31c7dc
log_digest      : sha256:d903603cb39d610683a3f8e174a61683b8929c472fade10cac8418a49e940cb0
build_receipt   : sha256:3b448c2961d3677912ac5d8bc5242033e7e105390ee7d94436c29a7b2011570e
serialized_bytes: 47030
sha256_of_bytes : b8ccb52f167c20ac5ff3891ffa50e6a1da624bfa6b089afe583a0b72ea31c7dc
outcome_counts  : {'blocked': 1, 'conflicting': 1, 'partial': 1, 'redaction_failure': 1,
                   'stale': 1, 'trusted': 1, 'unauthorized': 1, 'unavailable': 1}
```

Byte-identical in both processes. This satisfies the "byte-stable across two
clean runs" condition proposed as stop condition 4 in the review's C8.

Sources of nondeterminism closed by construction: no wall-clock read
(`datetime.now` appears nowhere; timestamps are inputs), no random or UUID ids,
no `id()` in output, no set iteration in serialization, no filesystem-glob
ordering in the run (case order comes from the input, and the input's order
comes from the manifest).

The digest anchors in `tests/test_digest.py` are SHA-256 values of literal byte
strings computed outside this package with stdlib `hashlib`, not values captured
from the code under test.

## 6. Completed Phase A work

Mapped to the handoff's eight items.

| # | Handoff item | Where | Evidence |
| --- | --- | --- | --- |
| 1 | Minimum toolchain, package boundary, test command, schema boundary, replacement seam | `ENGINEERING_DECISIONS.md` (D-1…D-12) | Repository's existing Python + pytest; zero new dependencies |
| 2 | Canonical JSON and deterministic content digests | `core/canonical_json.py`, `core/digest.py` | 28 + 15 tests, hand-written golden byte vectors, externally computed digest anchors |
| 3 | Generic append-only revision and receipt primitives with source identity, authorization state, timestamp/interval, derivation inputs, Coverage Gap support | `core/revisions.py`, `core/receipts.py`, `core/identity.py`, `core/coverage_gap.py` | 14 + 13 tests; no update or delete path exists; `verify_chain` detects a forged chain |
| 4 | Fixture-only read-adapter interface and local implementation, with no production credential, network, subprocess, publication, source-worktree write, or arbitrary execution capability | `adapters/base.py`, `adapters/fixture.py` | Section 4; adapter's public surface is exactly `{capabilities, case_ids, load_manifest, load_raw, read, root}` |
| 5 | Typed fixture read outcomes: trusted, blocked, partial, stale, conflicting, unauthorized, unavailable, redaction failure; `UNKNOWN` preserved | `adapters/outcomes.py`, 8 fixtures | All eight exercised end to end; unknown outcome strings fail closed with no alias handling; `UNKNOWN`/`MISSING` are singletons whose `bool()` raises |
| 6 | Hermetic local runner and deterministic replay test | `runner/hermetic.py`, `tests/test_deterministic_replay.py` | Section 5 |
| 7 | Positive capability allowlist plus tests/import-graph evidence that legacy runtime, production network, external publication, and mutation paths are unreachable | `core/capabilities.py`, `tests/_import_graph.py`, `tests/test_capability_allowlist.py` | Section 4, including the 15 planted-violation negative control |
| 8 | Test-fixture infrastructure and representative raw fixture inputs, readiness marked `alignment_pending` | `evals/fixtures/m0/`, `adapters/fixture.py` manifest loader | Every fixture and every manifest entry must record `expected_final_readiness: "alignment_pending"`; the loader rejects any other value |

### What was deliberately not built

No readiness decision, no check inventory, no materiality rule, no
`ExperimentReadContract` or `FlightReadinessPacket` schema, no acceptance-ID
registry, no review projection. No M1 or M2 concept exists anywhere in the
package: no Cause Claim, production candidate, ranking, Recommendation,
candidate diff, Win/Loss label, SEV object, or Trace-as-Evidence path.

Three invariants were implemented that could look like product decisions, so
each is named with the independent sources that agree on it:

1. **No body is retained for `blocked | unauthorized | unavailable |
   redaction_failure`.** Alignment packet draft `M0-SEC-001` ("no body retained
   or rendered") and CE plan `M0-READ-001` / `M0-SEC-001` ("typed receipts with
   no raw leakage") state this independently. Security invariant, not a
   readiness rule.
2. **Every non-trusted read must record a Coverage Gap.** P1
   (`freeze-canonical-domain-policy-contracts.md`): timeout, no authority, and
   zero reads create a Coverage Gap, not observed Evidence. It records the gap;
   it does not classify its materiality.
3. **A Coverage Gap cannot be labelled material or non-material without a named
   versioned `rule_source`.** This is the mechanical refusal to invent
   materiality policy, which is `SEAM-M0-03`.

## 7. Phase B seams awaiting alignment

Registered in `alignment/seams.py`. Each raises `AlignmentPendingError` naming
the decision, the authority, and the Phase B unit.
`tests/test_alignment_seams.py` asserts all ten still raise, so Phase A cannot
silently acquire one of these decisions.

| Seam | Decision blocked | Authority | Phase B unit |
| --- | --- | --- | --- |
| `SEAM-M0-01-READINESS-OUTCOME` | Two outcomes or three (`ready \| directional_only \| blocked`), and the promotion rules between them | packet §3; review C2; Owner decision 1 | M0-F3 |
| `SEAM-M0-02-CHECK-INVENTORY` | The final required-check set (draft has 14; C3 adds four owner-named checks) | packet §5; review C3 | M0-F3 |
| `SEAM-M0-03-MATERIALITY-POLICY` | Which failures and gaps are material by product policy | packet §5; open Owner decision | M0-F3 |
| `SEAM-M0-04-CONTRACT-FIELDS` | The exact `ExperimentReadContract` field set, including the `directional_only` permission field and the flight definition | packet §4; review C2, C9 | M0-F1 |
| `SEAM-M0-05-PACKET-FIELDS` | The exact `FlightReadinessPacket` field set and the typed next-safe-action kind | packet §6; review C4 | M0-F1, M0-F4 |
| `SEAM-M0-06-ACCEPTANCE-IDS` | One acceptance-ID registry with one meaning per id (packet §9 vs CE plan collision) | packet §9; CE plan; review C1, C5 | M0-F5 |
| `SEAM-M0-07-FIRST-SCREEN` | First-screen information hierarchy and reviewer interaction (P3-gated) | packet §7; sequencing P3 row | M0-F4 |
| `SEAM-M0-08-FIXTURE-BASELINES` | Always-ready / always-blocked baseline arms, fixture-author independence receipt, and whether fixtures may derive from protected domain assets | review C6, B3; open Owner decision | M0-F5 |
| `SEAM-M0-09-OWNER-DECISIONS` | Flight definition, one-vs-co-primary decision metric, invalid-experiment fix scope, reviewer/approver roles and overlap, M0 sizing | packet §11; review C9 | M0-F1…M0-F5 |
| `SEAM-M0-10-STOP-CONDITIONS` | The six deterministic halt triggers and the budget cap | packet §8; review C8; Owner sizing | M0-F0 exit re-check, M0-F5 |

### What Phase B needs from the main session

1. The exact frozen packet **path**.
2. The exact frozen packet **SHA-256**. The digest is the contract; a path alone
   is not a binding, because the file can change under the same name.
3. The **revision label** (`m0-alignment-vN`).

`alignment.seams.FrozenPacketBinding` validates all three and refuses a
malformed digest. Each `M0-F*` unit will record the binding in its exit
evidence, so a drift between the implemented digest and the current packet halts
that unit.

Any conflict between the frozen packet and an older planning document will stop
as a typed alignment blocker. This session will not silently choose one.

## 8. Dirty-worktree preservation statement

The worktree was dirty on entry and is dirty on exit, with the user's and the
parallel Codex session's changes untouched.

- Branch unchanged: `codex/kdd-data-agent-practices-research`.
- No `git add`, `commit`, `push`, `stash`, `checkout`, `restore`, `clean`,
  `reset`, branch change, or worktree operation was run.
- Pre-existing modified files left exactly as found: `.omc/project-memory.json`,
  `BACKLOG.md`, `CHANGELOG.md`, `CONTEXT.md`.
- Pre-existing untracked paths left exactly as found:
  `.agents/skills/sma_rewrite/workspace/`, `.gstack/`, `.workflow/`,
  `critique.json`, `designs/`, `docs/plans/`, `docs/research/`, `docs/adr/`,
  `docs/handover-2026-08-15-kdd-enterprise-plan-review.md`,
  `docs/session-logs/2026-08-15-kdd-enterprise-plan-review-wrapup.md`.
  (`CONTEXT.md` and the `docs/adr/*.md` files — 0004 through 0008 as of this
  writing, and still arriving — appeared *during* this session from the parallel
  Codex session, not from this one. They were observed and left alone.)
- No canonical research, planning, architecture, Wayfinder, alignment, or review
  document was modified. The two files written under
  `reviews/2026-08-16-opus5-m0-alignment/` are this receipt and the status
  writeback, both required by the handoff.
- `.agents/skills/sma/` and `.agents/skills/sma_rewrite/evals/` are unmodified:
  `git status --short` on both paths returns empty.
- No software installed, no global setting changed, no network access.

## 9. Test-quality evidence: mutation testing

A green suite proves nothing unless it can go red. Nine mutations were applied
to a scratch copy of the package (never to the repository) and the suite was run
against each. The unmutated copy and the restored copy both return 168 passed,
so the harness is not simply always-red.

| # | Mutation | Result |
| --- | --- | --- |
| M1 | Canonical JSON stops sorting object keys | 5 failed |
| M2 | Coverage Gap materiality can be set without a named `rule_source` | 2 failed |
| M3 | Fixture-level no-body guard removed | 1 failed |
| M3b | Both no-body guards removed (fixture layer and `ReadResult` layer) | 2 failed — each layer has its own failing test |
| M4 | `stable_id` becomes an incrementing counter instead of a content digest | 6 failed |
| M5 | Capability scanner always reports clean | 15 failed |
| M6 | An alignment seam returns `"ready"` instead of raising | 11 failed |
| M8 | Non-trusted reads no longer required to record a Coverage Gap | 1 failed |
| M9 | Coverage-gap builder unwired from `read()` | 2 failed |

### One real gap this found, and the fix

**M7 — the body-policy guard left intact but no longer called from `read()` —
originally passed 165/165.** Every test for that invariant either called the
validator directly or constructed a `ReadResult` directly, so all of them proved
the guard *rejects* and none proved the guard is *reached*. Deleting a control
was caught; silently unwiring it was not.

Fixed by adding three tests that drive a tampered fixture document through the
real `read()` path — retained body on a no-body outcome, a body under a
non-authorized state, and a non-trusted read with its Coverage Gaps stripped.
The tampering happens in memory via `monkeypatch` on the loader, so no hostile
fixture is ever written to disk and the never-writes property is preserved.

After the fix, M7 fails 2 tests and the equivalent M9 unwiring fails 2 tests.
Suite: 165 → 168 cases.

## 10. Verification status

**Self-verification: done.** Sections 3-5 and 9 are this session's own evidence:
suite output from three working directories, cross-process digest equality, the
zero-files-written diff, the planted-violation negative control, and the nine
mutations above.

**Independent verification: NOT COMPLETED.** An independent adversarial
reviewer was dispatched in a separate context with the handoff as its
specification and did substantial work — it re-ran the suite, copied the package
to a scratch directory, probed for bypasses, and checked citations in this
receipt and in `TOOLCHAIN_RECEIPT.md` against their sources. It then went idle
without delivering a report, and did not deliver one when asked a second time.
Per this project's circuit-breaker rule, an external tool gets two attempts
before the work is done by hand; that is what section 9 is. No finding from that
reviewer is recorded here, because none was received.

This matters for how Phase A should be read: the mutation evidence is real, but
it was designed by the same session that wrote the code. An adversarial pass
from a fresh context has repeatedly caught things an in-context pass missed on
this project, and it has not happened yet for this package. Recommend one before
Phase B binds anything to the frozen digest.
