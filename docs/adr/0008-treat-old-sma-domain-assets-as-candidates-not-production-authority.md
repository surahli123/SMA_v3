---
status: accepted
---

# Treat old SMA domain assets as candidates, not production authority

The new Data Agent may read old SMA metric definitions, schema catalogs, business-table routing, and fixture facts as historical candidates, but it must validate each adopted fact against current production sources and named owners for the Flight's scope and effective time. Transferred contracts and fixtures must retain provenance, validation receipts, and observed drift; old SMA runtime and architecture are not inherited. Direct code reuse requires separate provenance, test, security, and license review. This preserves useful domain discovery work without allowing stale or incorrect SMA knowledge to override production reality.
