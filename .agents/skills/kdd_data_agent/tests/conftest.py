"""Test wiring.

Puts `.agents/skills` on `sys.path` so `kdd_data_agent` imports as a package no
matter which directory the suite is invoked from, and exposes the shared
fixture root and a frozen run input.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

PACKAGE_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = PACKAGE_ROOT.parent

if str(SKILLS_ROOT) not in sys.path:
    sys.path.insert(0, str(SKILLS_ROOT))

from kdd_data_agent.adapters.fixture import FixtureReadAdapter  # noqa: E402
from kdd_data_agent.runner.hermetic import FoundationRunInput  # noqa: E402

M0_FIXTURE_ROOT = PACKAGE_ROOT / "evals" / "fixtures" / "m0"
FIXTURE_SOURCE_ID = "fixture-metric-store"

FROZEN_RUN_TIMESTAMP = "2026-08-16T00:00:00+00:00"
"""Every timestamp in the suite is frozen. Nothing reads a clock."""


@pytest.fixture
def package_root() -> Path:
    return PACKAGE_ROOT


@pytest.fixture
def fixture_root() -> Path:
    return M0_FIXTURE_ROOT


@pytest.fixture
def adapter() -> FixtureReadAdapter:
    return FixtureReadAdapter(M0_FIXTURE_ROOT)


@pytest.fixture
def frozen_run_input(adapter: FixtureReadAdapter) -> FoundationRunInput:
    return FoundationRunInput(
        run_id="m0-foundation-run-0001",
        recorded_at=FROZEN_RUN_TIMESTAMP,
        source_id=FIXTURE_SOURCE_ID,
        case_ids=adapter.case_ids(),
    )
