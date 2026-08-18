# KDD Data Agent — M0 Flight Readiness (pre-alignment foundation)

This package is the isolated greenfield root for the M0 Flight Readiness slice.
Only the **pre-alignment foundation** is built. Every part of M0 whose meaning
depends on the frozen M0 Build Alignment Packet is an explicit seam that raises.

## Hermetic command

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider .agents/skills/kdd_data_agent/tests -q
```

No network, no credential, no subprocess, no production source, no legacy
runtime, and no filesystem write — in the runtime package or in its tests.

## What exists

| Area | Module | Responsibility |
| --- | --- | --- |
| Absence | `core/unknown.py` | `UNKNOWN` / `MISSING` / `ALIGNMENT_PENDING` singletons. `bool()` raises, so no code can guess past one. |
| Serialization | `core/canonical_json.py` | Canonical, idempotent, sorted-key UTF-8 JSON. The single canonicalization seam. |
| Identity | `core/digest.py` | `sha256:<hex>` content digests and content-addressed ids. No random ids. |
| Provenance | `core/identity.py` | Source identity, actor, authorization state, observation interval. Timestamps are inputs, never clock reads. |
| Absence of coverage | `core/coverage_gap.py` | Coverage Gaps. Materiality stays `UNKNOWN` unless a named versioned rule is supplied. |
| History | `core/revisions.py` | Append-only revision log with chain verification. No update or delete path exists. |
| Audit | `core/receipts.py` | Source-read / derivation / authorization / redaction / build receipts. |
| Capability policy | `core/capabilities.py` | Positive allowlist of capabilities and imports. |
| Reads | `adapters/outcomes.py`, `adapters/base.py`, `adapters/fixture.py` | Eight typed read outcomes and the fixture-only adapter. |
| Run | `runner/hermetic.py` | Deterministic foundation run producing byte-stable receipts. |
| Not yet decided | `alignment/seams.py` | Ten named seams that raise `AlignmentPendingError`. |

## What is deliberately absent

- No readiness decision. `runner.hermetic.decide_readiness()` raises.
- No `ExperimentReadContract` or `FlightReadinessPacket` schema. Their field
  sets are alignment seams.
- No check inventory, no materiality policy, no acceptance-ID registry, no
  first-screen projection.
- No production adapter. `adapters/production/` must not exist before P2 closes;
  a test asserts its absence.
- Nothing from M1 Metric Movement or M2 Win/Loss: no Cause Claim, candidate,
  ranking, Recommendation, diff, or Trace-as-Evidence.

## Boundaries

- Does not import, extend, or migrate `.agents/skills/sma/` or
  `.agents/skills/sma_rewrite/`. They are read-only references.
- Fixtures under `evals/fixtures/m0/` are fully synthetic. No real, production,
  or de-identified company data.
- Every fixture records `expected_final_readiness: "alignment_pending"`.

## Read order

1. `README.md`
2. `ENGINEERING_DECISIONS.md` — the M0-F0 record: toolchain, boundaries,
   replacement seams, and the comparison against the reference harnesses.
3. `alignment/seams.py` — what Phase B must bind to the frozen packet digest.
