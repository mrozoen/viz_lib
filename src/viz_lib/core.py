"""Core plotting functions for viz_lib.

Each function takes a pandas DataFrame and produces a matplotlib chart.
Functions return the matplotlib Axes so you can tweak the result, and
accept an optional ``save_path`` to write the figure to disk.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd


def _finish(ax, save_path):
    """Shared helper: save the figure if asked, then return the Axes."""
    if save_path is not None:
        ax.figure.savefig(save_path, bbox_inches="tight", dpi=150)
    return ax


def plot_histogram(df, column, bins=20, ax=None, save_path=None):
    """Plot the distribution of a single numeric column."""
    if ax is None:
        _, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df[column].dropna(), bins=bins, color="#4c72b0", edgecolor="white")
    ax.set_title(f"Distribution of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    return _finish(ax, save_path)


def plot_bar(df, column, top=None, ax=None, save_path=None):
    """Plot value counts of a categorical column as a bar chart.

    ``top`` limits the chart to the N most common categories.
    """
    counts = df[column].value_counts()
    if top is not None:
        counts = counts.head(top)
    if ax is None:
        _, ax = plt.subplots(figsize=(8, 5))
    ax.bar(counts.index.astype(str), counts.values, color="#55a868")
    ax.set_title(f"Counts of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    ax.tick_params(axis="x", rotation=45)
    return _finish(ax, save_path)


def plot_multi_value_bar(df, column, sep=",", top=None, ax=None, save_path=None):
    """Plot counts for a column whose cells hold several values.

    Handy for fields like ``"Dramas, Comedies"`` or ``"United States, India"``
    where each cell lists multiple values separated by ``sep``. Every value is
    counted on its own. ``top`` keeps only the N most common values.
    """
    exploded = (
        df[column].dropna().astype(str).str.split(sep).explode().str.strip()
    )
    counts = exploded.value_counts()
    if top is not None:
        counts = counts.head(top)
    if ax is None:
        _, ax = plt.subplots(figsize=(8, 5))
    ax.barh(counts.index.astype(str), counts.values, color="#c44e52")
    ax.invert_yaxis()
    ax.set_title(f"Top values in {column}")
    ax.set_xlabel("Count")
    return _finish(ax, save_path)


def plot_scatter(df, x, y, ax=None, save_path=None):
    """Plot the relationship between two numeric columns."""
    if ax is None:
        _, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(df[x], df[y], alpha=0.6, color="#c44e52", edgecolor="white")
    ax.set_title(f"{y} vs {x}")
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    return _finish(ax, save_path)


def plot_correlation(df, ax=None, save_path=None):
    """Plot a correlation heatmap of all numeric columns."""
    corr = df.select_dtypes(include="number").corr()
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 6))
    im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_xticks(range(len(corr.columns)))
    ax.set_yticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=45, ha="right")
    ax.set_yticklabels(corr.columns)
    for i in range(len(corr.columns)):
        for j in range(len(corr.columns)):
            ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center",
                    color="black", fontsize=8)
    ax.figure.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    ax.set_title("Correlation heatmap")
    return _finish(ax, save_path)


def plot_missing(df, ax=None, save_path=None):
    """Plot the number of missing values in each column."""
    missing = df.isna().sum()
    missing = missing[missing > 0].sort_values(ascending=False)
    if ax is None:
        _, ax = plt.subplots(figsize=(8, 5))
    if missing.empty:
        ax.text(0.5, 0.5, "No missing values", ha="center", va="center",
                transform=ax.transAxes)
        ax.set_axis_off()
        return _finish(ax, save_path)
    ax.barh(missing.index.astype(str), missing.values, color="#8172b3")
    ax.invert_yaxis()
    ax.set_title("Missing values per column")
    ax.set_xlabel("Count")
    return _finish(ax, save_path)
