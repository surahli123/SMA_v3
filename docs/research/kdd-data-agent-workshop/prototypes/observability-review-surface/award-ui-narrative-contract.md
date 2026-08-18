# Award-UI Narrative Contract

PROTOTYPE / THROWAWAY. This contract applies the observed interaction language of Team 1286 and Team 1401 to Scenario A. It does not attribute production RCA capabilities to either team.

## The review flow

The reviewer starts with a question, not an evidence schema: what happened, what makes that reading doubtful, and where is the deployed proof?

Team 1286 provides the basic shape. Keep the question-specific answer path visible, let the reviewer inspect a source or group beside it, and keep the execution thread separate. Team 1401 supplies the graph operations: typed edges, grouped nodes, collapse and expand, filters, node detail, and a locator back to the source.

We can change the color, type, and domain language. We should keep that interaction grammar.

## Review

The deployed blend weight may explain the web miss. It does not explain why mobile stayed flat.

Cause remains **Suspected**. Recommendation remains **Blocked**.

The mobile result is the point of tension, so it should dominate the page. Deployment timing supports the claim; the stale corpus limits the comparison. Both are secondary. The next action is concrete: check the deployed artifact and the source line used at scoring time.

Evidence IDs stay available for inspection, but they should not lead the prose.

## Claims

The page asks one question: **Which explanation survives the mobile contradiction?**

For the selected “Blend overweight” claim, the deployment timing fits and the cross-surface behavior does not. The default path is:

`web miss → deployed blend v73 → blend application → mobile contradiction → blocked recommendation`

Claims sit on the left, the selected path stays in the center, and source detail opens on the right. Full topology and context remain available, but collapsed. Selecting another claim updates the path, detail, and locator together.

## Verify

Commit `9f71c2e` with `blend_weights.bin v73` was observed in the deployment. The candidate artifact is `not_applied`.

That establishes what ran. It does not resolve the mobile contradiction.

Show this authority distinction first, followed by the exact source locator. Receipts, ACL detail, hashes, and the verification log belong one level deeper. Keep the source and artifact proof visible together, following Team 1401's detail-plus-locator pattern.

## Trace

The deploy lookup failed once, left a gap, then succeeded on retry. Those are the three moments worth seeing first.

Only `EV-ACL-04`, `EV-MET-19`, and `EV-DEP-17` link back to reviewed evidence. The full run and raw output remain available below. The UI should make this boundary visible through linked and unlinked records instead of repeating “Trace is not Evidence.”

## Writing and display rules

Use proportional sans for findings and explanations. Reserve mono for evidence IDs, timestamps, code, hashes, receipts, and locators. Orange marks the blocking contradiction and its consequence; selection stays neutral.

State the consequence instead of naming the mechanism. Do not repeat a fact in the masthead, body, inspector, and footer. Do not turn every contract field into navigation. Preserve uncertainty: cleaner language must not turn “Suspected” into “Confirmed.”

The design passes this narrative gate when the reviewer understands the finding and its strongest objection before learning the graph vocabulary. The selected claim reveals one coherent path. Exact deployed proof remains within two interactions. Trace is distinguishable from Evidence without a warning repeated across the page.
