# Independent Rereview — M0 IR-M0-01 through IR-M0-06 Correction

## Verdict

`REJECT_LOCAL_M0_EVIDENCE`

The required package aggregate and all frozen/supporting bindings reproduce exactly. The correction closes direct `dataclasses.replace` readiness promotion, rejects the real unauthorized/no-body fixture, executes the sealed nineteen-case corpus through the public evaluator, compares typed reported/recomputed outputs internally, reproduces the canonical packet under five hash seeds, and retains the declared local-only capability boundary.

The corrected package is nevertheless not correct local M0 evidence. First, `FlightReadinessPacket.deserialize` verifies only the outer digest and derived readiness fields; it does not verify the sealed per-check `result_digest`. A blocked packet was promoted to `decision_grade` by changing CHK-02 from `FAIL` to `PASS`, leaving the stale check digest in place, updating the three readiness fields, and recomputing only the public outer digest. Second, the evaluator treats the presence of arbitrary fixture-authored `check_evidence` payloads as successful validation. Replacing all nineteen payloads with explicit `validator_executed: false`, `result: FAIL`, and garbage still produced eighteen `PASS` outcomes, CHK-19 `NOT_APPLICABLE`, and `decision_grade`.

This verdict rejects only the corrected local fixture-backed M0 evidence claim. It does not alter the separately bounded Phase A evidence and grants no production authorization or capability, P2/P3/P4 closure, M1/M2 authority, deployment, publication, or Committee Acceptance.

## Independence and scope

- The reviewer did not author the implementation or correction bytes and treated every receipt, planted truth, and pass count as an unverified claim.
- No subagent or second reviewer was started. No production or external system, credential, network source, Git mutation, commit, push, publication, or deployment was used.
- Disposable mutations ran only under `/private/tmp/kdd-m0-rereview.fqnExp`.
- The only repository outputs written are this report and `independent-rereview-status.json`.

## Exact-byte binding

| Item | Independently recomputed SHA-256 | Result |
| --- | --- | --- |
| Rereview handoff | `885784ad9df9550641e8b7322b1c35bb281ca4511e4a4b949a2a8356b2c4e10a` | observed current handoff |
| Sorted corrected package aggregate | `c9c2d30fe588ce68fa1f45f93b83df768090f3ce7c0992516e8d31b224d4c901` | exact required match; 59 files; recomputed manifest byte-identical to `source-manifest-after.sha256` |
| Frozen packet | `82747da96d66dd8851c03edc837f38597264a07794a2b145cd530ca0a5f07b19` | exact match |
| Frozen architecture | `9508b42979b5f708d3b0be7016ed414fd0b4c28d531b75fd0a4710eb46df8fc1` | exact match |
| CE plan | `2b4bbd3583e2f289303b8e47b255e3b53bd0f3307f0b699b33299b57aa9e1daf` | exact match |
| Sequencing plan | `8fec2f8c3c3d22aa9dc1b762769673789d007fd74dbbed9c34e5ea88fcd4725b` | exact match |

The aggregate was computed from sorted repository-relative `.py`, `.json`, and `.md` paths below `.agents/skills/kdd_data_agent/`, excluding `__pycache__`, `.pytest_cache`, and `.omc`, then SHA-256 hashing the generated manifest. No drift block applies.

## Required fresh reproduction

### 1–2. Aggregate and frozen/supporting bindings

The aggregate and four receipt bindings above all match. `source-manifest-before.sha256` was also independently checked against the retained exact pre-correction disposable package: its aggregate is `30d6b47ca55f1444ef8ba596aedabd90db5f21af58e60d53ad2320a5fc94c196`.

### 3. Full suite from three working directories

The same suite was executed with `PYTHONDONTWRITEBYTECODE=1`, `-p no:cacheprovider`, and explicit `PYTHONPATH`:

| Working directory | Result |
| --- | --- |
| Repository root | `313 passed in 0.50s` |
| Package root | `313 passed in 0.49s` |
| Unrelated `/private/tmp` | `313 passed in 0.48s` |

### 4. Named canonical builder under five seeds

Command form:

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=.agents/skills PYTHONHASHSEED=<seed> python3 -m kdd_data_agent.tests.canonical_packet_builder
```

Seeds `0`, `1`, `42`, `99991`, and `random` produced identical results:

```text
serialized_byte_count: 20018
serialized_byte_sha256: 0c4ffe715eb18055cbeeec0e88ec3fcf180cc7307fa0298b0d7c6aaaf93e30d1
internal_content_digest: sha256:364ef4e04c8b440e6097f69179d8869fe98dcbf3c0336cdc6f75d808339ab828
```

The builder correctly distinguishes raw serialized-byte SHA-256 from the packet's internal identity digest.

### 5. Previously demonstrated regressions

- Direct reconstruction is closed: `dataclasses.replace(blocked_packet, analysis_use=DECISION_GRADE)` raises `PacketError: analysis_use must be derived exactly from the sealed checks`.
- The real `m0-read-unauthorized-001` no-body result is not admitted; public evaluation emits CHK-16 `FAIL` and `not_permitted`.
- A related sealed-deserialization promotion remains open: changing CHK-02 `FAIL` to `PASS`, retaining its stale `result_digest`, updating readiness fields, and recomputing only `packet_digest` is accepted as `decision_grade`. This is finding `IR-M0-01-RR` below.

### 6. All nineteen validator/evidence bindings

Removing each `check_evidence` key separately and running the public evaluator produced `MISSING + not_permitted` for CHK-01 through CHK-18. Removing CHK-19's key produced its contract-derived `NOT_APPLICABLE` under the versioned `runtime_only` rule; it did not produce `PASS`. Thus an absent key does not become `PASS`.

Presence is not genuine evidence, however. Replacing every payload with contradictory garbage still produced:

```text
CHK-01..CHK-18: PASS
CHK-19: NOT_APPLICABLE
analysis_use: decision_grade
```

The implementation hashes the payload without validating its check-specific claims. This is finding `IR-M0-03-RR` below.

### 7. Versioned reported/recomputed comparison

The public `build_recomputation_evidence` signature has no caller-controlled `comparison_matches` parameter. A typed output disagreement is compared internally under `m0-comparison-rule/v1`, produces CHK-14 `FAIL`, remains visible in `disagreements`, and yields `not_permitted`. Receipt details bind reported and recomputed output digests plus the comparator digest.

### 8. Corpus, baselines, decoys, conflicts, vetoes, and drift

All nineteen sealed corpus cases ran through `kdd_data_agent.m0.evaluator.evaluate_flight`. Observed results matched planted truth: one `decision_grade`, one `directional_only`, and seventeen `not_permitted`, including all three decoys, reviewer conflict, and all six typed hard-veto routes. Both always-ready and always-blocked baselines were contradicted.

Disposable byte/truth probes were killed independently:

- Mutating the trusted fixture byte without updating its pin raises `ValidationError: fixture bytes drifted for m0-read-trusted-001` during corpus load.
- Mutating only `m0-trusted.expected_analysis_use` to `not_permitted` loads but is contradicted by the public evaluator; baseline validation raises `ValidationError: real evaluator contradicted planted truth for m0-trusted`.

The corpus therefore binds raw fixture bytes and detects independently changed planted truth. It does not repair the false semantic acceptance of arbitrary present `check_evidence` payloads.

### 9. Public API split and local-only capability boundary

The public module `.agents/skills/kdd_data_agent/m0/evaluator.py` exports only the typed evaluator API and delegates to the internal implementation. The package declares only `fixture_read`, `local_deterministic_compute`, and `in_memory_append`; the runtime/test import and capability scans pass, planted forbidden-import/write/reflection mutations are detected, and `adapters/production` does not exist. No production adapter or external-action surface was found. This is local capability evidence only, not production authorization or capability.

## 314 to 313 suite-count reconciliation

The exact pre-correction package collected 314 tests; the corrected package collects 313. Normalized node-ID comparison shows:

- Three decoy cases changed only parameter labels and retained their semantics.
- Nine semantic cases disappeared: eight parameterized material-failure checks for CHK-03, CHK-05, CHK-06, CHK-08, CHK-11, CHK-12, CHK-15, and CHK-16, plus the unknown-materiality ceiling case.
- Eight new cases were added: absent-validator and distinct-evidence-ID checks; canonical-builder and deserialization round trips; reconstruction and serialized-readiness tamper checks; unauthorized-fixture rejection; and removal of the caller comparison boolean.

This explains the net `-1`. The old caller-override mechanism was correctly removed, so the old tests could not remain unchanged. But their named semantic coverage was not replaced through the public evaluator. In particular, the new distinct-evidence test checks uniqueness only, and the serialized tamper test changes readiness without changing a sealed check. The count reduction therefore includes real coverage weakening, not merely consolidation.

## Findings

### IR-M0-01-RR — BLOCKER: deserialization does not verify sealed check digests

**Current anchors:** `.agents/skills/kdd_data_agent/m0/packet.py:295-320`; `.agents/skills/kdd_data_agent/m0/packet.py:321-355`; `.agents/skills/kdd_data_agent/tests/test_m0_packet.py:53-61`; `.agents/skills/kdd_data_agent/tests/test_m0_corrections.py:20-22`.

`deserialize` verifies the outer packet digest and recomputes readiness from raw check dictionaries, but it never recomputes each check's `result_digest`, validates the core-check-set digest, or reconstructs typed `CheckResult` objects. The existing tamper test changes only `analysis_use`; the round-trip test checks only an unmodified packet. A blocked packet with a stale sealed check digest was promoted to `decision_grade` and accepted.

**Impact:** a caller can rewrite failed/missing/unknown check outcomes and mint a digest-valid serialized decision-grade document. The correction does not close false readiness across the deserialization boundary.

**Minimal correction:** deserialize by reconstructing and validating the typed contract, core set, checks, receipts, gaps, and packet, or at minimum recompute every nested content digest and exact inventory binding before deriving readiness; add a regression that mutates a blocking check outcome while retaining its stale `result_digest`.

### IR-M0-03-RR — BLOCKER: arbitrary present payloads are accepted as check-specific validator evidence

**Current anchors:** `.agents/skills/kdd_data_agent/m0/corrected_evaluator.py:208-220`; `.agents/skills/kdd_data_agent/m0/corrected_evaluator.py:231-263`; `.agents/skills/kdd_data_agent/evals/fixtures/m0/m0-read-trusted-001.json:39-50`; `.agents/skills/kdd_data_agent/tests/test_m0_checks.py:92-102`.

For every declared key, `_validators` creates `PASS` from a digest of the fixture payload and labels it “named validator accepted,” without executing a named check-specific validator or interpreting the payload. Only a small subset has explicit failure logic, and that logic does not invalidate contradictory declared evidence on a passing path. The test asserts only that evidence IDs are distinct.

**Impact:** SRM/compositional SRM, population/scope, arithmetic/join, completeness/pagination/late arrival, estimator, scorecard reconciliation, source-change revalidation, cross-read attribution/freshness/scope, disagreement closure, and other named checks can be decision-grade even when their alleged evidence explicitly says validation failed.

**Minimal correction:** define a typed input/result contract and deterministic validator for every check; validate the relevant fields and receipt lineage, derive `PASS` only from the validator's successful output, and make malformed, false, absent, or unproven evidence `FAIL`, `MISSING`, or `UNKNOWN` as applicable.

### IR-M0-TEST-RR — MAJOR: prior named failure semantics were removed without equivalent public-evaluator coverage

**Current anchors:** `.agents/skills/kdd_data_agent/tests/test_m0_checks.py:92-102`; `.agents/skills/kdd_data_agent/tests/test_m0_packet.py:47-61`; `.agents/skills/kdd_data_agent/tests/test_m0_reads.py:75-86`; `docs/research/kdd-data-agent-workshop/reviews/2026-08-18-m0-f1-f5-correction/source-manifest-before.sha256:38-50`; `docs/research/kdd-data-agent-workshop/reviews/2026-08-18-m0-f1-f5-correction/source-manifest-after.sha256:40-54`.

The correction removes eight per-check material-failure cases and the unknown-materiality ceiling case, while the replacements test missing-key behavior, evidence-ID uniqueness, and narrower regression surfaces. There is no public-evaluator failure case for several removed check classes, including CHK-06, CHK-08, and CHK-15.

**Impact:** the green 313-test suite cannot detect the arbitrary-evidence acceptance above and no longer proves the previous named failure ceilings across all affected checks.

**Minimal correction:** restore equivalent behavior-driven tests through the public evaluator for every material check and unknown-materiality ceiling, including contradictory/malformed evidence and nested check-digest tampering; document the expected collection-count change after semantic parity is restored.

## IR-M0-01 through IR-M0-06 disposition

| Original finding | Independent rereview disposition | Basis |
| --- | --- | --- |
| `IR-M0-01` | `REJECTED` | direct reconstruction is closed, but digest-valid sealed-check deserialization still promotes blocked packets |
| `IR-M0-02` | `CORRECTED` | typed contract-bound admission rejects the real unauthorized/no-body fixture |
| `IR-M0-03` | `REJECTED` | absence fails closed, but arbitrary present payloads still mint PASS without genuine validators |
| `IR-M0-04` | `CORRECTED` | typed outputs are compared internally under the versioned rule; no public comparison boolean |
| `IR-M0-05` | `CORRECTED_WITH_REJECTING_DEPENDENCY` | byte-bound executable corpus, baselines, decoys, conflicts, and vetoes run correctly, but depend on the unsound evaluator |
| `IR-M0-06` | `CORRECTED` | named five-seed builder truthfully reports both digest namespaces |

## Preserved proof boundaries

- The exact aggregate and frozen/supporting bindings are verified.
- The three-directory suite, five-seed invariance, unauthorized admission closure, internal comparison, executable corpus plumbing, fixture/truth drift checks, and local-only capability boundary remain valid evidence for their narrow claims.
- The 313 green tests are not independent semantic acceptance and do not overcome the reproduced blockers.
- Phase A evidence remains separate and was not re-adjudicated or promoted by this rereview.
- Production authorization/capability, P2/P3/P4, M1/M2, deployment, publication, and Committee Acceptance remain unestablished or unauthorized.
