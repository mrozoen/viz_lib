"""viz_lib: a tiny matplotlib-based visualization library for pandas DataFrames."""

from viz_lib.core import (
    plot_bar,
    plot_correlation,
    plot_histogram,
    plot_missing,
    plot_multi_value_bar,
    plot_scatter,
)

__version__ = "0.1.0"

__all__ = [
    "plot_histogram",
    "plot_bar",
    "plot_multi_value_bar",
    "plot_scatter",
    "plot_correlation",
    "plot_missing",
]
