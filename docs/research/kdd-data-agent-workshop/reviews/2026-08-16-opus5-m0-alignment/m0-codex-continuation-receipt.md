# M0 Codex Continuation Receipt

Handoff: `m0-codex-continuation-20260817`  
Updated at: `2026-08-17T07:07:31Z`  
Repository: `/Users/surahli/Documents/projects/SMA_v2`  
Branch: `codex/kdd-data-agent-practices-research`  
HEAD inspected and preserved: `28cbbda6e4d4d7f08134952d38433e52d3ee8768`  
Phase A verdict: **PASS_WITH_GAPS**  
Phase B status: **BLOCKED AT FROZEN-PACKET GATE**

This receipt exhausts the handoff's `One-Run Execution Cap`. This task must not
resume, start M0-F1 through M0-F5, or extend scope without a new Owner
authorization and handoff.

## 1. Scope and authority

This continuation modified only:

- `.agents/skills/kdd_data_agent/`
- this continuation receipt
- `m0-codex-continuation-status.json`

The existing dirty worktree was preserved. No canonical plan, freeze document,
protected legacy path, production source, external service, global setting, or
dependency was modified. No commit, push, pull request, deployment,
publication, package installation, production access, product network call,
product write capability, or external message occurred.

The internal progress message required by the handoff is addressed to the
source Codex task after this receipt is written. The explicitly prohibited
external cross-model peer pass was not run; six local fresh-context review
personas and one independent findings validator were used instead.

No Opus 5 review started: the main orchestrator reported that Claude quota was
exhausted. Therefore no Opus 5 verdict exists, and this receipt does not infer
or substitute one.

## 2. Fresh Phase A reproduction

The continuation independently reproduced the original 168-case baseline from
the repository root, package root, and `/private/tmp`, then expanded the suite
during adversarial hardening. The final exact invocations were:

```text
cd /Users/surahli/Documents/projects/SMA_v2
PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider .agents/skills/kdd_data_agent/tests
225 passed in 0.25s

cd /Users/surahli/Documents/projects/SMA_v2/.agents/skills/kdd_data_agent
PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider
225 passed in 0.24s

cd /private/tmp
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/Users/surahli/Documents/projects/SMA_v2/.agents/skills pytest -q -p no:cacheprovider /Users/surahli/Documents/projects/SMA_v2/.agents/skills/kdd_data_agent/tests
225 passed in 0.25s
```

The package file-set aggregate SHA-256 was identical immediately before and
after those three runs:

```text
2f1001b93b19b2318c4c6419205ed2f7778ac23c02533e78a0c0899f15bf7d1e
```

This proves the final verification did not write or mutate a tracked package
artifact. `PYTHONDONTWRITEBYTECODE=1` and `-p no:cacheprovider` also disabled
Python bytecode and pytest cache writes.

### Full-suite invocation count under the one-run cap

Twelve full-suite invocations are evidenced for this continuation run:

1. Three required initial reproductions: repository root, package root, and
   `/private/tmp`, each at 168 passed.
2. One package-root checkpoint at 197 passed after the first independent
   hardening set.
3. Five package-root review/hardening checkpoints: 213 cases with one scanner
   failure, 213 passed after that correction, 217 cases with 20 request-binding
   and scanner-test failures, 217 passed after those corrections, and 225
   passed after capability-receipt and malformed-fixture coverage landed.
4. Three required final acceptance invocations: repository root, package root,
   and `/private/tmp`, each at 225 passed.

The five additional package-root invocations were focused regression gates for
evidenced review defects. The two failing gates changed the implementation
direction immediately; the three passing gates verified the corresponding
minimal correction before the next review batch. No additional full suite is
authorized after this receipt.

## 3. Deterministic replay

Three clean external processes used the same frozen input under
`PYTHONHASHSEED=0`, `1`, and `12345`. All three produced identical values:

```text
run digest       sha256:7837c3e6819052870299c7e0f82362680834562fb6d2e8c0f69310721c044375
revision log     sha256:7221d8a458fb810839706a95e59d4004baa3d4048e4ac068a114bca8e8579ce2
build receipt    sha256:63ba40745a6caca6f24bc7d20b29e38a18cc385c1976173c90ead7a1a6be95b1
serialized bytes 47274
```

The new digests intentionally differ from the earlier receipt because the
build receipt now records the adapter identity and sorted effective capability
set. Equality across processes and hash seeds is the determinism claim.

## 4. Defects proved and corrected

Fresh local reviewers found 13 actionable semantics-independent defects or
verification gaps. `findings-mechanics.py` accepted all reviewer returns with
`malformed_returns=0`, `malformed_findings=0`, and no confidence suppression.
The independent validator re-inspected the pre-fix addition snapshot and the
current code and validated all eight P1 scenarios. All 13 were corrected:

1. Completed run outcome counts and sealed `RevisionLog` storage remained mutable.
2. Mutable objects exposing `to_canonical()` survived `deep_freeze` by reference.
3. Mutable or non-string `SourceIdentity` fields could invalidate a fixed receipt identity.
4. `ReadResult` could contradict its proving receipt's request, outcome, body digest, or Coverage Gaps.
5. `CoverageGap.gap_id` could be caller supplied rather than content derived.
6. A caller could construct a Phase A result with a readiness value other than `ALIGNMENT_PENDING`.
7. The runner did not correlate adapter results to issued requests or reject repeated receipt identities.
8. Runtime reads did not bind fixture `declared_outcome` to manifest `expected_read_outcome`.
9. A plain application object equal to `{"__kdd__":"UNKNOWN"}` decoded as the reserved sentinel.
10. The AST scanner missed builtin recovery through allowed modules, literal reflected attributes, and `from ... import sma`.
11. The scanner missed direct and aliased non-fixture filesystem reads such as `read_bytes`, `cwd`, `iterdir`, and `stat`.
12. Fixture and manifest fail-closed schema guards lacked real-loader negative wiring tests.
13. Executed runner capabilities were not represented in the build receipt.

Regression coverage now includes 46 planted scanner violations, deeply frozen
completed outputs, hard-sealed logs, manifest/outcome binding, strict reserved
sentinel provenance, direct ReadResult/receipt consistency, derived-only gap
identities, readiness-seam construction blocking, adapter request correlation,
fixture/manifest tampering, and receipted effective capabilities.

The scanner claim remains deliberately narrow: it is static source assurance
over every Python file present in this package. It is not an OS or interpreter
runtime sandbox.

## 5. Package and toolchain evidence

Current measured package size:

- 19 runtime modules, 2,365 lines including docstrings
- 11 test files, 1,769 lines
- 225 collected cases
- 13 allowed runtime standard-library import roots
- 46 planted capability violations
- nine synthetic fixture files: eight read cases plus one manifest

Pinned-source identities were rechecked without network access or execution:

- Champion: `bdc874fc4260e3565ae0dce041728fdf5b376709`
- Fourth place: `ae0f2baa9b6533c23cd4db6bbcc09f4fcf791c1a`
- DeepSeek Harness: `47f943859bef60e4160492346772ded9b24f765a`

The provisional Python `KEEP` conclusion still holds. The Fourth-place
toolchain claim was corrected to 114 `python_exec.py` files under `src`: 113
under `src/experiments` plus one baseline copy. No upstream code was copied.

## 6. Remaining gaps

Phase A receives `PASS_WITH_GAPS`, not an unconditional production acceptance,
because:

- static AST enforcement is not a runtime sandbox;
- fixture-directory symlink replacement has an environment-dependent TOCTOU
  residual if an attacker controls the synthetic fixture directory;
- no production adapter, live company data, external service, host sandbox,
  cross-language digest implementation, UI, or M1/M2 path was authorized or
  tested; and
- all product-semantic implementation remains blocked.

The external peer review required by the default CE workflow was skipped to
honor the explicit no-egress/no-external-message boundary. Local reviewers were
correctness, testing, maintainability, security, agent-native, and adversarial.

## 7. Frozen-packet gate

No authoritative Phase B binding was found. The current packet remains an
Owner-aligned freeze candidate. Opus 5 review did not start because Claude
quota was exhausted, so no Opus verdict exists. No accepted digest-bound freeze
record supplies all three required values:

1. exact frozen packet path;
2. exact `sha256:<64 lowercase hex>` digest; and
3. exact revision label.

The following ten seams remain present and blocking:

- `SEAM-M0-01-READINESS-OUTCOME`
- `SEAM-M0-02-CHECK-INVENTORY`
- `SEAM-M0-03-MATERIALITY-POLICY`
- `SEAM-M0-04-CONTRACT-FIELDS`
- `SEAM-M0-05-PACKET-FIELDS`
- `SEAM-M0-06-ACCEPTANCE-IDS`
- `SEAM-M0-07-FIRST-SCREEN`
- `SEAM-M0-08-FIXTURE-BASELINES`
- `SEAM-M0-09-OWNER-DECISIONS`
- `SEAM-M0-10-STOP-CONDITIONS`

Next authorized action: the main orchestrator supplies the exact frozen packet
path, revision label, and SHA-256 together. Until then, this implementation
stops cleanly at the gate and must not infer product meaning from drafts.
