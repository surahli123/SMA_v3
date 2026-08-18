---
status: accepted
---

# Make invalid-experiment diffs a gated M0 capability

The target M0 product may attach a correct, reviewable, unapplied candidate diff to an Invalid Experiment Remediation, but only for validity, instrumentation, or data-quality fixes after exact-target, authority, validation, and no-write delivery gates pass. The first vertical slice produces typed remediation guidance and a reopen condition without a diff. That guidance remains the permanent fallback whenever a diff gate is incomplete; M0 never converts the remediation into a production-cause claim, product-logic recommendation, or applied mutation.
