# M0-F0 Engineering Decision Record

Status: engineering proposal, not an Owner-frozen architecture decision.
Scope: the isolated package boundary and local toolchain for the M0 Flight
Readiness slice. This record selects no production source, credential, vendor,
UI framework, threshold, or SLA. Rejecting any proposal below returns to M0-F0;
it does not revise the product contract.

## 1. Decisions

| # | Decision | Choice | Class | Cheapest proof | Replacement boundary |
| --- | --- | --- | --- | --- | --- |
| D-1 | Package root | `.agents/skills/kdd_data_agent/` | `engineering_proposal` | The directory did not exist; nothing outside it changed. | Moving the root is a directory rename plus one `sys.path` line in `tests/conftest.py`. |
| D-2 | Implementation language | Python 3.14, standard library only | `engineering_proposal` (**provisional**) | The suite runs on the interpreter already used by this repository, with zero installed dependencies. | Section 3. Every contract, adapter, receipt, validator, and presenter sits behind an explicit interface so a port replaces implementations, not semantics. |
| D-3 | Test runner | `pytest`, already present in the repo | `engineering_proposal` | `python3 -m pytest … -q` -> 225 passed after independent hardening. | Tests use plain functions and `assert`; only `pytest.raises` and `pytest.mark.parametrize` are framework-specific. A port to `unittest` is mechanical. |
| D-4 | Hermetic command | `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider .agents/skills/kdd_data_agent/tests -q` | `engineering_proposal` | Matches the invocation convention already used by `.agents/skills/sma_rewrite`. | Any runner that executes the same test bodies. |
| D-5 | Schema boundary | Code-defined frozen dataclasses plus canonical JSON on the wire; **no** schema DSL, no code generation, no validation library | `engineering_proposal` | `core/canonical_json.py` + golden byte vectors in `tests/test_canonical_json.py`. | JSON is the interchange format, so a JSON Schema or protobuf encoding can be introduced later without changing any stored digest, provided canonical bytes are preserved. |
| D-6 | Canonicalization | Sorted-key, separator-tight, UTF-8, sentinel-aware, idempotent | `engineering_proposal` | Hand-written golden vectors, not code-derived expectations. | `core/canonical_json.py` is the single seam. Swapping in RFC 8785 (JCS) means replacing one module and re-pinning the vectors. |
| D-7 | Digest algorithm | SHA-256, carried in the string as `sha256:<hex>` | `engineering_proposal` | Pinned against SHA-256 of literal byte strings computed outside the package. | The algorithm prefix makes a second algorithm additive rather than ambiguous. |
| D-8 | Identifiers | Truncated content digests (`rev-…`, `rcpt-…`, `gap-…`) | `engineering_proposal` | `test_stable_id_is_deterministic_and_content_addressed`. | Random UUIDs are excluded by design: they would make replay non-deterministic. |
| D-9 | Time | Every timestamp is an input; no wall-clock read anywhere in the package | `engineering_proposal` | `datetime.now` appears nowhere; the import-graph scan enforces the allowlist. | A clock becomes an injected parameter if one is ever needed, never an ambient call. |
| D-10 | Persistence | In-memory append-only log; no database, no file writes | `engineering_proposal` | `test_log_exposes_no_update_or_delete_path`; `write_text`/`unlink`/`mkdir` are forbidden call shapes. | `RevisionLog` is the seam. A durable store implements append/head/history/verify_chain. |
| D-11 | Capability model | Positive allowlist of capabilities **and** imports, enforced by an AST scan over the package's own source | `engineering_proposal` | `tests/test_capability_allowlist.py`, including 46 planted violations that the scanner must catch. | The allowlist is data in `core/capabilities.py`; the scanner is test-only and never enters the runtime import graph. |
| D-12 | Absence handling | `UNKNOWN` / `MISSING` / `ALIGNMENT_PENDING` singletons whose `bool()` raises | `engineering_proposal` | `test_the_alignment_pending_sentinel_has_no_truth_value`. | The reserved wire key `__kdd__` is the only coupling to the encoding. |

## 2. Boundary

Owned by this package:

- `.agents/skills/kdd_data_agent/**` — source, fixtures, tests, and these docs.

Never touched:

- `.agents/skills/sma/`, `.agents/skills/sma_rewrite/` — read-only references,
  not migration targets. No import, no copied stage, schema, or threshold.
- Any canonical research, planning, architecture, Wayfinder, alignment, or
  review document.
- `adapters/production/` — must not exist before P2 closes.

## 3. Why Python is provisional, and what a port would cost

Python is chosen because it is what the repository already runs, which makes the
foundation testable today at zero setup cost. It is **not** an Owner-frozen
architecture decision, and nothing in the design leans on it:

- **No frameworks and no dependencies.** Runtime imports are thirteen standard
  library modules, enforced by allowlist. There is no ORM, no pydantic, no
  serialization library, no async runtime, no web framework.
- **Semantics live in data, not in language features.** Outcomes, capabilities,
  gap kinds, authorization states, and seams are enumerations; contracts are
  frozen records; the wire format is canonical JSON. Every one of those
  transfers unchanged to another language.
- **The digest contract is language-independent.** Byte-stability is a property
  of `core/canonical_json.py`, not of Python. The one documented deviation from
  RFC 8785 (code-point rather than UTF-16 key ordering) is unobservable for
  ASCII keys, and `require_ascii_keys` can make it structurally impossible.
- **Interfaces are the seam, implementations are not.** `ReadAdapter` is one
  method. `RevisionLog` is four. `Receipt` is a record. A port replaces bodies,
  not meanings.

Concrete port cost, measured against what exists today: 2,365 lines of runtime
source (docstrings included) across 19 modules, of which the canonicalizer, the
digest helpers, deep-freeze helper, and append-only log are the only non-trivial algorithms.
The 1,769 lines of tests port as behavioral specifications -- 225 cases, all
expressed as inputs and expected outcomes rather than as Python internals.

## 4. Reference-harness comparison

See `TOOLCHAIN_RECEIPT.md` for the keep-or-replace assessment against the
Champion, Fourth-place, and DeepSeek Harness implementation practices, scored on
production integration, deterministic behavior, capability isolation,
testability, UI integration, license, and migration cost.

## 5. What this record does not decide

Readiness semantics, the check inventory, materiality policy, contract and
packet field sets, acceptance identifiers, the review surface, and every open
Owner decision. Those are registered in `alignment/seams.py` and remain blocked
until the frozen M0 Build Alignment Packet digest is supplied.
