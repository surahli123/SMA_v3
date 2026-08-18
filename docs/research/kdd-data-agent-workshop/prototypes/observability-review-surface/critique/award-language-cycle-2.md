# Award Interaction-Language Redesign — Cycle 2 Critique

PROTOTYPE / THROWAWAY. This critique follows an explicit owner rejection. It does not replace live owner acceptance.

## What changed

The previous interface exposed the evidence schema as its visual hierarchy. This iteration instead carries over the observed award-interface grammar: a review question, a selected answer path, grouped evidence on demand, adjacent source detail, an exact locator, and a separate execution replay.

The UI narrative was drafted with `comms-draft` and revised with `comms-polish`. The rewrite preserved uncertainty: the blend remains suspected, the recommendation remains blocked, and deployed proof does not resolve the mobile contradiction.

## Five-axis review

- Clarity: the Review screen communicates the current reading, strongest objection, and next action before showing evidence vocabulary. Claims asks one review question.
- Hierarchy: contradiction dominates Review; Claims centers one selected answer path; Verify leads with the proof boundary; Trace foregrounds failure, gap, and validated retry.
- Typography: proportional sans carries findings and explanations. Mono is limited to IDs, timestamps, receipts, locators, and code.
- Motion: interaction feedback is limited to selection, context disclosure, contradiction focus, and re-layout. Reduced-motion support remains explicit.
- Brand consistency: all four routes share the same case header, two independent decision axes, bone/graphite system, and one orange contradiction accent.

## Cycle findings and corrections

Cycle 1 found that the supposedly collapsed evidence context was visible because a component display rule overrode the HTML `hidden` attribute. It also found rotated typed-edge labels on the 390px Claims path. Cycle 2 added a global hidden rule, preserved context disclosure behind an explicit control, rendered the mobile typed path vertically with horizontal edge labels, and added bottom-navigation clearance.

## Remaining human questions

- Does the direct award-interface grammar feel sufficiently learned rather than translated into another internal dashboard?
- Is the Review narrative concise enough for a reviewer who has not read the contract?
- Does the selected path contain enough context before the reviewer chooses “Show context”?
- Does the Verify proof boundary explain deployed-versus-candidate authority without over-explaining it?

P3 remains open pending live owner acceptance.
