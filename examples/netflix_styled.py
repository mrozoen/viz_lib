"""A stylized, Netflix-branded overview of the Netflix titles dataset.

This is the "poster" companion to ``netflix_analysis.py``: same data, same
story, but with a dark theme, a red sequential ramp for magnitude panels,
and direct value labels instead of busy axes.

    python examples/netflix_styled.py path/to/netflix_titles.csv

Saves ``netflix_poster.png`` and shows it on screen.
"""

import sys

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap

# --- Theme -----------------------------------------------------------------
BG = "#0b0b0b"          # near-black surface
INK = "#f5f5f5"         # primary text
INK_MUTED = "#8c8c8c"   # secondary text
GRID = "#262626"        # recessive gridlines
RED = "#E50914"         # Netflix red
SILVER = "#b3b3b3"      # second identity color (TV Shows)

# Sequential red ramp: deep -> bright. Larger magnitude reads brighter.
RAMP = LinearSegmentedColormap.from_list("nflx", ["#5c0a10", "#E50914", "#ff6b72"])

plt.rcParams.update({
    "figure.facecolor": BG, "axes.facecolor": BG, "savefig.facecolor": BG,
    "text.color": INK, "axes.labelcolor": INK_MUTED,
    "xtick.color": INK_MUTED, "ytick.color": INK_MUTED,
    "font.family": "DejaVu Sans", "font.size": 11,
})


def load(path):
    df = pd.read_csv(path)
    df["year_added"] = pd.to_datetime(df["date_added"], errors="coerce").dt.year
    movies = df["type"] == "Movie"
    df.loc[movies, "duration_min"] = (
        df.loc[movies, "duration"].str.replace(" min", "", regex=False).astype(float)
    )
    return df


def _clean(ax, title):
    """Strip chart junk and set a left-aligned panel title."""
    for side in ax.spines.values():
        side.set_visible(False)
    ax.set_title(title, color=INK, fontsize=13, fontweight="bold", loc="left", pad=12)
    ax.tick_params(length=0)


def ranked_barh(ax, counts, title):
    """Horizontal bars, largest on top, colored by magnitude with labels."""
    counts = counts[::-1]  # so largest ends up on top after barh
    norm = counts.values / counts.values.max()
    colors = RAMP(0.35 + 0.6 * norm)
    ax.barh(counts.index.astype(str), counts.values, color=colors)
    for y, v in enumerate(counts.values):
        ax.text(v + counts.values.max() * 0.01, y, f"{v:,}", va="center",
                color=INK, fontsize=9)
    ax.set_xlim(0, counts.values.max() * 1.15)
    ax.set_xticks([])
    _clean(ax, title)


def histogram(ax, series, title, bins, unit=""):
    ax.hist(series.dropna(), bins=bins, color=RED, alpha=0.9, edgecolor=BG, linewidth=0.6)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    med = series.median()
    ax.axvline(med, color=SILVER, linestyle="--", linewidth=1.2)
    ax.text(med, ax.get_ylim()[1] * 0.92, f" median {med:.0f}{unit}",
            color=SILVER, fontsize=9)
    _clean(ax, title)


def main(path="netflix_titles.csv"):
    df = load(path)
    total = len(df)

    fig = plt.figure(figsize=(20, 13))
    gs = fig.add_gridspec(2, 3, top=0.80, bottom=0.08, left=0.13, right=0.97,
                          hspace=0.42, wspace=0.28)

    # Header band
    fig.text(0.05, 0.92, "NETFLIX", color=RED, fontsize=52, fontweight="bold",
             fontfamily="DejaVu Sans")
    fig.text(0.052, 0.86, "A DATA PORTRAIT OF THE CATALOG", color=INK,
             fontsize=16, fontweight="bold")
    fig.text(0.052, 0.835, f"{total:,} titles · 2019 snapshot · built with viz_lib",
             color=INK_MUTED, fontsize=11)

    # Panel 1 — Movies vs TV Shows (identity: two distinct colors)
    ax = fig.add_subplot(gs[0, 0])
    tc = df["type"].value_counts()
    bars = ax.bar(tc.index, tc.values, color=[RED, SILVER], width=0.6)
    for b, v in zip(bars, tc.values):
        pct = v / total * 100
        ax.text(b.get_x() + b.get_width() / 2, v, f"{v:,}\n{pct:.0f}%",
                ha="center", va="bottom", color=INK, fontsize=10, fontweight="bold")
    ax.set_ylim(0, tc.values.max() * 1.18)
    ax.set_yticks([])
    _clean(ax, "Movies dominate the catalog")

    # Panel 2 & 3 — time distributions
    histogram(fig.add_subplot(gs[0, 1]), df["release_year"],
              "When titles were released", bins=30)
    histogram(fig.add_subplot(gs[0, 2]), df["year_added"],
              "When Netflix added them", bins=15)

    # Panel 4 & 5 — ranked magnitude
    genres = df["listed_in"].dropna().str.split(",").explode().str.strip().value_counts().head(10)
    ranked_barh(fig.add_subplot(gs[1, 0]), genres, "Top genres")
    countries = df["country"].dropna().str.split(",").explode().str.strip().value_counts().head(10)
    ranked_barh(fig.add_subplot(gs[1, 1]), countries, "Top producing countries")

    # Panel 6 — movie runtimes
    histogram(fig.add_subplot(gs[1, 2]), df["duration_min"],
              "Movie runtimes", bins=30, unit=" min")

    fig.text(0.05, 0.03, "Source: Netflix titles dataset (Kaggle / TidyTuesday mirror)",
             color=INK_MUTED, fontsize=9)
    fig.savefig("netflix_poster.png", dpi=150)
    print("Saved netflix_poster.png")
    plt.show()


if __name__ == "__main__":
    main(*sys.argv[1:])
