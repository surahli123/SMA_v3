# Private-Branch Publication Verification Receipt

- Verified: `2026-08-18T04:59:13-07:00`.
- Scope: the exact include and exclude sets in `share-safe-publication-manifest.md`.
- Terminal pre-Git state: `PUBLICATION_CHECKS_PASS`.

## Repository and Authority Boundary

- Authenticated GitHub account: `surahli123`.
- Target repository: `surahli123/SMA_v2`; GitHub reports it private with default branch `main`.
- Target feature branch: `codex/kdd-data-agent-practices-research`.
- Owner authority covers only a bounded commit and push of the verified include set.
- Pull request creation, public release, production access, M1/M2 implementation, deployment, rollback, external messaging, and Committee Acceptance remain unauthorized or unproven.

## Exact Evidence Bindings

| Evidence | Fresh result |
| --- | --- |
| Round 5 package files | `59` |
| Round 5 aggregate | `sha256:9eea3014cb74acc48e9bbd24a486d2b6a5a4a4f57ae76191f42d037a5988b19a` |
| Stored Round 5 manifest | Byte-identical to the freshly recomputed manifest |
| Frozen M0 packet | `sha256:82747da96d66dd8851c03edc837f38597264a07794a2b145cd530ca0a5f07b19` |
| Frozen architecture | `sha256:9508b42979b5f708d3b0be7016ed414fd0b4c28d531b75fd0a4710eb46df8fc1` |
| CE plan | `sha256:2b4bbd3583e2f289303b8e47b255e3b53bd0f3307f0b699b33299b57aa9e1daf` |
| Sequencing plan | `sha256:8fec2f8c3c3d22aa9dc1b762769673789d007fd74dbbed9c34e5ea88fcd4725b` |
| Independent verdict | `ACCEPT_LOCAL_M0_EVIDENCE` on the exact Round 5 aggregate |

## Reproduction

- Full suite from repository root: `370 passed`.
- Full suite from package root: `370 passed`.
- Full suite from unrelated temporary working directory: `370 passed`.
- Hash seeds `0`, `1`, `42`, `99991`, and `random` produced identical named-builder output.
- Canonical serialized bytes: `47075`.
- Serialized-byte SHA-256: `7327bdb9b280a4b89212bf217b2f6addb40ac8dbd6ba6d46a171ffeb0bfac9cc`.
- Internal packet digest: `sha256:652a3d9f18ff980dbd56059e7d699d6914826847f4d675555137ffa2f5b4caa0`.

## Share-Safe and Mechanical Checks

| Check | Result |
| --- | --- |
| Markdown | `164` files; `804` relative links; zero missing targets; zero unbalanced fences |
| JSON | `64` files parsed; zero errors |
| JavaScript | Prototype source passes `node --check` |
| Secrets | Gitleaks default rules report no leaks across every include path |
| Raw/private media | No audio, video, or PDF file in the include set |
| Oversized files | No file exceeds 10 MB; largest included artifact is approximately 1.49 MB |
| Language | One Owner-requested Chinese six-question collaboration HTML; no other CJK in the include set |
| Protected paths | No change in old SMA runtime or evaluation paths; the unrelated old-SMA workspace remains excluded |
| Runtime state | All `.omc`, `.pytest_cache`, `__pycache__`, bytecode, and other runtime/cache paths remain excluded |
| Diff format | The default staged whitespace check passes over current implementation, plan, ADR, and root-navigation paths. The whole historical bundle flags intentional Markdown hard breaks and exact-byte patch/receipt whitespace; those exceptions are classified and preserved rather than silently rewritten. |

## Historical Path-Literal Classification

Forty-six included files contain inert macOS checkout or disposable scratch-directory literals. They are historical handoffs, reviews, receipts, or status records grouped as follows:

| Historical group | Files |
| --- | ---: |
| Enterprise-plan handover | 1 |
| 2026-08-16 Opus M0 alignment | 10 |
| 2026-08-17 exact-digest review | 9 |
| 2026-08-17 pre-freeze execution | 9 |
| 2026-08-17 Fable architecture finalization | 4 |
| 2026-08-17 Fable adversarial review | 4 |
| 2026-08-17 Phase A independent verification | 2 |
| 2026-08-18 M0 execution and correction rounds | 7 |

These literals are non-executable provenance in a private-repository handoff. Several affected receipts are exact-byte hash-bound, so rewriting them would falsify the freeze history. The exception does not cover secrets, credentials, private attachments, production data, or company data; none were found. Any future public export must omit these originals or create separately labeled redacted copies without changing the immutable historical receipts.

## Proof Boundary

This receipt proves that the declared private-branch publication package passed its pre-Git checks. It does not itself prove that a commit or push occurred. Git branch and remote history are the evidence for any later publication action. It also does not promote local fixture-backed M0 evidence into Phase A readjudication, production authority or capability, P2/P3/P4 closure, M1/M2 completion, deployment, public release, or Experiment Review Committee Acceptance.
