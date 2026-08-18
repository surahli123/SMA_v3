"""Greenfield KDD Data Agent package (M0 Flight Readiness slice).

This package is isolated on purpose. It does not import, extend, or migrate
`.agents/skills/sma/` or `.agents/skills/sma_rewrite/`, and it holds no
production, network, subprocess, publication, or mutation capability.

Only the pre-alignment foundation is implemented. Every part of M0 whose
meaning depends on the frozen M0 Build Alignment Packet is represented as an
explicit seam in `kdd_data_agent.alignment.seams` and raises rather than
guessing a product decision.
"""

from __future__ import annotations

PACKAGE_NAME = "kdd_data_agent"
MILESTONE = "M0"
PHASE = "pre-alignment-foundation"

__all__ = ["PACKAGE_NAME", "MILESTONE", "PHASE"]
