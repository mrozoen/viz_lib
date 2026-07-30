"""viz_lib: tiny, aesthetic World Cup player-stat visualizations for pandas."""

from viz_lib.core import (
    finishers_vs_playmakers,
    golden_boot,
    load,
    nation_firepower,
    tournament_trend,
)

__version__ = "0.2.0"

__all__ = [
    "load",
    "golden_boot",
    "finishers_vs_playmakers",
    "nation_firepower",
    "tournament_trend",
]
