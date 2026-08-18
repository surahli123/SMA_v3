# M0 Correction Round 2 Receipt

Completed: `2026-08-18T03:13:42-07:00`  
Run boundary: one Owner-authorized local correction run for `IR-M0-01-RR`, `IR-M0-03-RR`, and `IR-M0-TEST-RR` only  
Terminal implementation state: `CORRECTED_LOCAL_FIXTURE_EVIDENCE_READY_FOR_INDEPENDENT_REREVIEW`

## Exact bindings

The pre-edit aggregate was independently recomputed from the sorted repository-relative `.py`, `.json`, and `.md` files below `.agents/skills/kdd_data_agent/`, excluding `__pycache__`, `.pytest_cache`, and `.omc`.

| Binding | SHA-256 | Result |
| --- | --- | --- |
| Input package aggregate | `c9c2d30fe588ce68fa1f45f93b83df768090f3ce7c0992516e8d31b224d4c901` | exact hard-gate match; 59 files; byte-identical to the Round 1 after-manifest |
| Corrected package aggregate | `52d4c82e2a80ffc5a42bc80918165b33ebed0b03256a27c7c7bc78bd8046d2f6` | final 59-file manifest aggregate |
| Frozen M0 packet | `82747da96d66dd8851c03edc837f38597264a07794a2b145cd530ca0a5f07b19` | unchanged |
| Frozen architecture | `9508b42979b5f708d3b0be7016ed414fd0b4c28d531b75fd0a4710eb46df8fc1` | unchanged |
| CE plan | `2b4bbd3583e2f289303b8e47b255e3b53bd0f3307f0b699b33299b57aa9e1daf` | unchanged |
| Sequencing plan | `8fec2f8c3c3d22aa9dc1b762769673789d007fd74dbbed9c34e5ea88fcd4725b` | unchanged |

`source-manifest-before.sha256` preserves the accepted Round 1 package bytes. `source-manifest-after.sha256` binds the corrected package. Eight package files changed; no file was added to or removed from the 59-file aggregate.

## Corrections

### IR-M0-01-RR

`FlightReadinessPacket.deserialize` now verifies the complete serialized identity graph before returning an immutable document view. It validates exact packet schema and outer digest; the frozen packet/architecture binding; contract digest and nested typed schemas; exact core-check inventory and digest; every check result digest, enum, rule source, receipt reference, and check-specific evidence identity; every receipt ID and digest; nested and packet-level Coverage Gap identities; contract-bound source and derivation receipt lineage; and the derived readiness projection.

The regression reproduces the independent bypass exactly: it changes a blocking CHK-05 outcome to `PASS`, leaves the stale `result_digest`, updates readiness fields, recomputes the outer packet digest, and is rejected. Analogous stale/resealed core-set, contract, frozen-binding, receipt-ID, receipt-digest, Coverage-Gap, inventory, and check-rebinding cases are also rejected.

### IR-M0-03-RR

The trusted fixture now contains structured `check_observations`, not boolean-shaped success claims. Nineteen named functions, `validate_chk_01` through `validate_chk_19`, deterministically derive outcomes from those raw observations, the frozen `ExperimentReadContract`, the admitted `ReadResult` lineage, and the typed reported/recomputed outputs. Each check produces its own deterministic validator receipt and evidence identity.

Presence has no success meaning. Missing observations produce `MISSING`; malformed or unadmitted observations produce fail-closed `UNKNOWN` where applicable; contradictions and false claims produce `FAIL`; CHK-19 is `NOT_APPLICABLE` only when the raw observation and versioned `runtime_only` contract agree. SRM is calculated from observed counts, expected proportions, and preregistered alpha; ratio arithmetic is recomputed; source, scope, identity, estimator, CUPED, reconciliation, authorization, comparator, change-revalidation, and closure fields are compared rather than trusted.

### IR-M0-TEST-RR and count reconciliation

The final suite collects `344` tests. The original pre-correction suite collected `314`; Round 1 collected `313` after removing nine semantic cases and adding eight narrower cases. Round 2 adds 31 behavior cases to the Round 1 suite, for net `+30` from the original:

- nineteen public-evaluator contradiction cases cover CHK-01 through CHK-19, including all eight removed per-check material failures;
- one explicit unknown-materiality-ceiling case restores the ninth removed semantic case;
- one arbitrary-present-payload regression and one absent-observation regression cover the independent presence/default bypasses; and
- ten serialized-boundary cases cover the exact stale-check promotion plus nested receipt, core-set, contract, binding, gap, inventory, and lineage identities.

The prior distinct-evidence test was strengthened in place to require nineteen unique evidence identities and nineteen unique validator receipt identities. No semantic test was silently deleted in Round 2.

## Verification

| Evidence | Result |
| --- | --- |
| Repository-root full suite | `344 passed in 0.93s` |
| Package-root full suite | `344 passed in 0.92s` |
| Unrelated `/private/tmp` full suite with explicit `PYTHONPATH` | `344 passed in 0.92s` |
| Capability/import/no-write/no-network test | `61 passed in 0.21s`; no `adapters/production` directory |
| Five hash seeds | seeds `0`, `1`, `42`, `99991`, and `random` reproduced identical canonical evidence |
| Canonical serialized bytes | `44044` |
| Serialized-byte SHA-256 | `cea0119be0588fe5746c2d6bd2da57c577332952c8ec17cf86171d9e8176dc4f` |
| Internal packet content digest | `sha256:4135a724d70e0300d44ee431d1299fcdb9882b67a144b72e7cdaa4f88594c076` |
| Executable sealed corpus | all 19 cases passed through the public evaluator and matched planted truth; trivial baselines, decoys, conflicts, and six hard vetoes remained active |

Fresh disposable copies under `/private/tmp/kdd-m0-round2-probes.fa2dRQ` killed four code mutations: stale nested-check verification bypass (`1 failed`), arbitrary-payload PASS bypass (`20 failed`), unauthorized-admission downgrade (`1 failed`), and forced comparator truth (`1 failed`). A fresh fixture-byte mutation under `/private/tmp/kdd-m0-round2-fixture-probe.kmOE1W` halted collection with `fixture bytes drifted for m0-read-trusted-001`.

## Review and proof boundary

The final five-axis code review found and corrected one boundary-hardening issue: nested records now validate their typed schema, enums, and registered rule sources as well as their hashes. The final suite and boundary scans are green. This is an implementation-owner receipt, not independent acceptance.

The independently verified Phase A behavior remains separate. This run establishes only corrected local fixture-backed M0 evidence ready for independent rereview. It does not establish production authorization or production-backed M0 capability, close P2/P3/P4, authorize or implement M1/M2, deploy, publish, or establish Experiment Review Committee Acceptance. No production access, network read, credential, commit, push, PR, deployment, publication, or external action occurred.
