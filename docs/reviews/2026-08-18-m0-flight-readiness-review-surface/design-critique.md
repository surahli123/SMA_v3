# Design Critique: Skills Applied, Skills Rejected, Risks Remaining

Subject: `prototypes/m0-flight-readiness-review/`
Structured panel: `critique.json` (score 4/5, converged)
Conformance to the owner-selected contract, and the D1–D8 defect log from the
first render pass: `visual-critique.md`

The continuation handoff required five design skills to be read in full before
further surface changes, and required this file to record what was adopted, what
was rejected, and why. All five were read. The frozen product contract overrides
generic marketing-site prescriptions, so a large part of this document is an
explicit, reasoned rejection list rather than a compliance list.

## 1. What this artifact is, for the purposes of design judgement

A local, static, dependency-free, read-only forensic workspace that renders
fixture-class `FlightReadinessPacket` projections for one reviewer at a time. It
has no audience to persuade, no conversion to drive, no brand to launch and no
network to fetch from. On `taste-skill`'s own dials that places it at
`VISUAL_DENSITY 9` (cockpit), `MOTION_INTENSITY 1` (static) and
`DESIGN_VARIANCE 5` (asymmetric but strictly legible) — not at the skills'
defaults of 4, 6 and 8.

## 2. Adopted

| Rule | Source | How it shows up |
| --- | --- | --- |
| Cockpit density: tiny padding, no card boxes, 1px lines separating data, monospace for all numbers | `taste-skill` §6 `VISUAL_DENSITY 8-10` | Every separator is a 1px rule; every number, digest and identifier is monospace |
| Dashboard hardening: generic card containers banned above density 7; group with `border-t` / `divide-y` / negative space | `taste-skill` Rule 4 | The only bordered containers are the collapsible receipt records, where the border marks an expandable boundary rather than decoration |
| One accent, no AI purple/blue, no neon glow, no pure black | `taste-skill` Rule 2 and §7; `imagegen-frontend-web` §8 | Single orange accent; ink is `#1f2326`, never `#000000`; the stylesheet contains zero `box-shadow`, zero gradient and zero keyframe |
| No Inter; no serif on a dashboard; control hierarchy with weight and colour rather than scale | `taste-skill` §7 | A sans/mono pair from the owner-selected contract; the decision value is 21px, not a hero |
| Anti-emoji policy | `taste-skill` §2, `gpt-tasteskill` | No emoji in code, markup, content or alt text |
| Ban cheap meta-labels ("SECTION 01", "QUESTION 05") | `gpt-tasteskill` §7 | No ordinal section labels. The uppercase micro-labels name real packet fields (`PACKET DECISION`, `NEXT SAFE ACTION`, `SUPERSESSION`), which is the owner-selected reference's own language |
| Button text contrast must be legible | `gpt-tasteskill` §3 | Every foreground/background pair is machine-checked against WCAG AA in `tools/verify.py`; twelve pairs, all ≥ 4.7:1 |
| Prevent horizontal page scroll | `gpt-tasteskill` §7 | Measured rather than asserted: 120 checks across four scenarios, five routes and six widths, all passing |
| Viewport stability: `100dvh`, never `h-screen` | `taste-skill` §2 | `min-height: 100dvh` |
| Grid over flexbox percentage math | `taste-skill` §2 | CSS Grid throughout; no `calc` width math |
| Mobile override: asymmetric layouts collapse to a single column below 768px | `taste-skill` §6 | Three breakpoints; label-above-value stacking below 760px |
| Empty and error states are mandatory, not optional | `taste-skill` Rule 5 | Empty: "No check matches this filter. The packet is unchanged." and "No Coverage Gap is recorded on this packet." Error: the fail-closed refusal screen, which names the schema it actually saw |
| Tactile `:active` feedback | `taste-skill` Rule 5 | Adopted as a tone change rather than a transform — see the deviation note below |
| Typography is a primary material: clear size contrast, obvious reading order, brief supporting text | `imagegen-frontend-web` §9 | Four type sizes carry the whole hierarchy; supporting text is one sentence |
| Anti-slop content: no "unleash", "elevate", "seamless", "next-gen", no fake brand names, no invented statistics | `imagegen-frontend-web` §8 | Mechanically checked; zero hits. Every value on screen comes from an emitted packet, so there is no invented data to be slop |
| Five-axis critique panel emitting a 0–5 score, converging at ≥ 4 | `open-design-critique-theater` | `critique.json`, score 4, converged after two passes |
| Prove the build passes; never mark a test skipped without a reason | `open-design-build-test` | `build-test.json` and `build-test.log`: 16 commands, 16 passed, 0 failed, 0 skipped |

## 3. Rejected, with reasons

These are rules from the required skills that this artifact deliberately does
not follow. Each rejection is a consequence of the frozen product contract, the
no-dependency constraint or the no-network constraint.

**Every third-party dependency.** `taste-skill` mandates React or Next.js,
Tailwind, Framer Motion and `@phosphor-icons/react` or `@radix-ui/react-icons`;
`gpt-tasteskill` mandates GSAP and ScrollTrigger. The handoff requires a
dependency-free artifact that opens from `file://` with no build step, and adding
any dependency would require a licence and security decision that is not in
scope. The surface is hand-written HTML, CSS and one ES5-compatible script.

**AIDA page structure, hero architecture and massive section spacing**
(`gpt-tasteskill` §2–§3). There is no hero, no navigation bar in the marketing
sense, no `py-32` chapter rhythm and no call to action. A reviewer opening this
page has already decided to read it; the first screen owes them a decision and
its proof, not an attention funnel. Large section padding would push the exact
receipts below the fold, which is the specific defect D2 fixed.

**All motion.** `gpt-tasteskill` §5 requires scroll pinning, scrubbed text
reveals, card stacking and hover scale physics; `taste-skill` §4 and §9 require
perpetual infinite micro-animations and spring physics so a dashboard "feels
alive". This surface renders forensic evidence for a decision about whether an
experiment may be used at all. Motion competing for attention with an evidence
value is a defect here, not polish, and perpetual animation is directly contrary
to the reduced-motion requirement in the handoff. The stylesheet has no
animation at all.

**Bento grids, the Bento 2.0 paradigm, `rounded-[2.5rem]`, diffusion shadows
and card archetypes** (`gpt-tasteskill` §4, `taste-skill` §9). The owner-selected
contract reserves elevation for a selected record or a permission boundary and
carries hierarchy on thin rules. Card soup is also on the handoff's own
prohibition list.

**Generated and stock imagery.** `gpt-tasteskill` §7 and `taste-skill` §7 both
require `picsum.photos` placeholders; `imagegen-frontend-web` is built around
generating reference imagery. Both need network access, which is prohibited, and
the handoff states that the existing owner-selected screenshots are the visual
source of truth and that no replacement reference is to be generated in this
run. The page loads no image of any kind.

**The prescribed webfont stacks** (`Geist`, `Satoshi`, `Cabinet Grotesk`,
`Outfit`). Each requires a font fetch. The stack is the one named in the
owner-selected design contract, resolved from system fonts, so the page renders
identically offline.

**Python-driven layout randomisation** (`gpt-tasteskill` §1). Layout variety
across generations is the wrong goal for an artifact whose bytes must be
deterministic and independently reproducible. The layout is fixed and derived
from the owner-selected references.

**The Creative Arsenal** — magnetic buttons, gooey menus, glassmorphism,
parallax tilt, marquees, coverflow, text scramble, hover image trails and the
rest (`taste-skill` §8). None is compatible with a read-only evidence surface,
and several would obscure or animate values that must be read exactly.

## 4. Deviations that are neither adoption nor rejection

**Accent saturation.** `taste-skill` Rule 2 caps accent saturation below 80%.
The accent here is `#c3410f`, about 86% saturated in HSL. It is a darkened
derivative of the owner-selected `#ef5a24` (also about 86%), and the darkening
was done to clear WCAG AA on light backgrounds — it measures 4.93:1 on the
workspace ground and 5.14:1 on a panel. The owner-selected contract and the
contrast floor jointly win over the generic ceiling.

**A fourth semantic colour.** The palette is neutral scale plus orange
(blocked, contradiction, selection), green (validated) and amber (`MISSING` and
`UNKNOWN`). That is one more than the one-accent guidance allows. It is kept
because `PASS`, `FAIL` and `MISSING`/`UNKNOWN` are three distinct typed
outcomes in the frozen check contract, and folding the third into either of the
others would misreport a packet state. Amber is confined to the outcome tag; it
is deliberately *not* used for typed absence in field values, which was defect
D4.

**`:active` as tone, not transform.** `taste-skill` Rule 5 suggests
`-translate-y-[1px]` or `scale-[0.98]`. In a dense table where the primary
control is a row expander, a per-click nudge reads as jitter, and a transform is
precisely what a reduced-motion reader asked not to see. The press state is a
background and colour shift instead.

**Uppercase micro-labels.** `imagegen-frontend-web` §8 lists "lazy all-caps
everywhere" as typography slop. Uppercase here is confined to 9.5px letterspaced
monospace field labels, which is the exact register used by the owner-selected
screenshots, and never appears in running text. Treated as a deliberate
typographic register rather than a shortcut.

## 5. Changes made in this pass, before and after

Four issues were found after re-reading the skills and re-reading the captures.
The eight found in the first render pass are logged as D1–D8 in
`visual-critique.md`.

**D9 — orange was spent on every typed absence.** Before: `UNKNOWN` and
`MISSING` field values rendered in the warn colour, so a blocked packet showed
dozens of orange tokens and the accent carried no signal. After: typed absence
is muted monospace with a dotted underline. Orange now appears only on
selection, a blocked or unauthorized state, a stale or incomplete state and a
`FAIL` row.

**D10 — an orange callout on a non-blocked screen.** Before: the receipt-reach
callout used an orange left rule and wash, which appeared on the
`decision_grade` screen where nothing is blocked and read as an alarm. After:
neutral rule and ground.

**D11 — an inset shadow standing in for a rule.** Before: a blocking table row
was marked with `box-shadow: inset 3px 0 0`. After: a 3px `border-left`, so the
stylesheet now contains literally zero `box-shadow` and the "hierarchy by rules,
not elevation" claim is exactly true rather than nearly true.

**D12 — short enums breaking mid-word.** Before: at 390px the receipt index
compressed `derivation` into `deriv` / `ation` and `source_read` into three
fragments, because digest-oriented `overflow-wrap: anywhere` applied to short
enum cells too. After: enum cells are `nowrap`, the table minimum width was
raised, and the table scrolls inside its own container instead of shredding
tokens.

## 6. Residual AI-slop and observability risks

1. **Consequential-row repetition.** A packet whose read was not admitted shows
   eighteen rows restating one cause. It is ordered correctly and explained in
   one sentence above, but it is still a wall of near-identical content, which is
   density slop by `imagegen-frontend-web` §8. Grouping consequential unknowns
   under their originating check would fix it; that is a presentation change and
   was not attempted inside this cap.
2. **Unused right column on the Boundaries route** at desktop width. The
   boundary list is measure-bounded at 82ch, which is deliberate, but the space
   beside it does nothing.
3. **The route tablist scrolls below roughly 620px with no visible affordance.**
   Keyboard arrow navigation still reaches every route; a touch reader sees four
   of five tabs and no hint that a fifth exists.
4. **Coverage Gap identifiers are shown but not cross-linked** to the receipt
   index. Every relationship exists as a table row, as the contract requires, but
   matching a gap's `evidence_refs` to a receipt is manual.
5. **No live reviewer has used this.** Every accessibility property claimed is
   either mechanically measured or structurally implemented, and none of it
   substitutes for P3 live review-surface acceptance, which remains open.

## 7. Proof boundary

This critique covers a local fixture-only prototype. It establishes no
production M0 capability or authorization, closes no part of P2, P3 or P4,
starts no M1 or M2 work, and carries no Experiment Review Committee decision.
`VAL-UI-101` remains an open external gate.
