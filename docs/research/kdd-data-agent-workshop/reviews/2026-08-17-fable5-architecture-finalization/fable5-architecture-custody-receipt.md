# Fable 5 Architecture Artifact Custody Receipt

Status: `PRESERVED_DRAFTS_RATE_LIMITED`

Recorded by: Codex main orchestrator  
Recorded at: `2026-08-18T00:36:51-07:00`  
Reason: the Fable 5 architecture session reached its rate limit before it could finish its requested closeout.

## Preserved artifacts

| Artifact | Lines | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `architecture-design-draft.md` | 497 | 53,416 | `70a4fd230f5ce41137fb5d2c266098c6bf37a948a8739031cd0c03d077097f4e` |
| `architecture-decision-ledger.md` | 142 | 33,069 | `8c156cbce9a6b2e262fbcebf30a4c29b13867848ccc8e3041b3320cdb47db03f` |
| `architecture-overview-draft.html` | 226 | 20,836 | `fd2cfc6d463556355221f88bc9890e5133392ac5ea4a093eb2849ef27b3e9935` |
| `m0-review-flow-draft.html` | 204 | 17,594 | `a612663070f1d778bbd150b7ee25b220625f91ab2a13650cc02c3772ba402f8a` |
| `architecture-finalization-status.json` | n/a | n/a | `ebbeadb2b3217801855abd2e30c5c64692eb3b175943c2c454af172e054eee40` |
| `steelman-owner-alignment-handoff.md` | n/a | n/a | `be360517fdd4beb5d0f76782d8372078c2b16ad940ac843447434122f842f8d3` |

The four primary design artifacts total 1,069 lines and 124,915 bytes.

## Integrity observations

- All four primary artifacts are present and non-empty.
- Both HTML files contain complete `</body>` and `</html>` terminators.
- The primary artifacts contain no Chinese prose; durable technical content remains English.
- The architecture design identifies itself as `DRAFT v2`; both visual artifacts visibly identify themselves as `DRAFT`.
- The decision ledger contains Owner records through D8 and S8. Its F-series rows are facilitator rulings or proposals unless separately confirmed by the Owner.
- The existing `architecture-finalization-status.json` is preserved as historical Fable output, but it is stale relative to the artifact bytes: it still describes the design as v1 with S1-S8 integration pending, while the preserved Markdown identifies itself as v2 and includes later decisions.
- The requested `steelman-owner-alignment-status.json` was not written before rate exhaustion.
- A strict legacy HTML parser reports warnings for inline SVG elements and unescaped ampersands in Google Fonts URLs. These warnings do not establish browser failure, but the HTML has not yet passed final visual/browser acceptance.

## Authority boundary

This receipt proves only that the Fable-authored drafts were preserved at the exact digests above. It does not:

- convert any draft into a frozen architecture specification;
- transfer a review verdict across changed bytes;
- approve facilitator proposals that the Owner has not confirmed;
- clear the exact-digest architecture review, Phase A independent verification, production authorization, or Committee Acceptance;
- authorize M0-F1 through M0-F5 implementation.

## Lawful continuation

Codex may continue the Owner steelman discussion, reconcile confirmed Owner decisions and evidence-backed review findings into a new candidate, and arrange independent exact-byte review. The Fable drafts must remain attributable to their preserved digests; any Codex revision must use a new path or explicit superseding revision and a new digest.
