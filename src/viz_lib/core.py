"""World Cup player-stat visualizations, built on matplotlib.

Every chart function takes a tidy DataFrame from :func:`load` and returns a
matplotlib ``Axes``. Pass ``save_path=`` to write the figure straight to disk.
The whole library shares one "stadium night" look defined at the top.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ── Palette ────────────────────────────────────────────────────────────
# A dark "stadium night" theme. Position hues are the colorblind-safe
# Okabe-Ito set, assigned in a fixed order and never cycled.
BG, INK, MUTED, GOLD, GRID = "#0f1a17", "#f4f1e8", "#8b968f", "#f2c14e", "#26332c"
POS_COLORS = {"FW": "#e69f00", "MF": "#009e73", "DF": "#56b4e9", "GK": "#cc79a7"}


def _ax(figsize, polar=False):
    """Make a styled figure + axes in the shared dark theme."""
    fig, ax = plt.subplots(figsize=figsize, subplot_kw={"polar": polar})
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(colors=MUTED, labelsize=9)
    return ax


def _finish(ax, title, subtitle=None, save_path=None):
    """Add the gold title (+ optional subtitle), then save/return the axes."""
    ax.set_title(title, color=GOLD, fontsize=17, fontweight="bold",
                 loc="left", pad=26)
    if subtitle:
        ax.annotate(subtitle, xy=(0, 1), xytext=(0, 8), va="bottom",
                    xycoords="axes fraction", textcoords="offset points",
                    color=MUTED, fontsize=10)
    if save_path:
        ax.figure.savefig(save_path, dpi=150, bbox_inches="tight",
                          facecolor=ax.figure.get_facecolor())
    return ax


def load(path):
    """Read a World Cup player-stats CSV into a tidy DataFrame.

    Turns the ``"fr France"`` style ``Squad`` codes into a clean ``Country``
    column and coerces the stat columns to numbers.
    """
    df = pd.read_csv(path)
    df["Country"] = df["Squad"].astype(str).str.replace(
        r"^[a-z]{2,3}\s+", "", regex=True)
    for col in ["Gls", "Ast", "Min", "90s", "Age", "MP", "CrdY", "CrdR"]:
        if col in df:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def golden_boot(df, n=12, save_path=None):
    """The Golden Boot race: a lollipop chart of the top ``n`` goalscorers."""
    top = (df.sort_values("Gls", ascending=False)
             .head(n)[["Player", "Country", "Gls"]].iloc[::-1])
    m = float(top["Gls"].max())
    ax = _ax((9, 7))
    y = np.arange(len(top))
    ax.hlines(y, 0, top["Gls"], color=GOLD, alpha=0.35, lw=2.5)
    ax.scatter(top["Gls"], y, s=470, color=GOLD, zorder=3,
               edgecolor=BG, linewidth=1.5)
    for yi, (_, r) in zip(y, top.iterrows()):
        ax.text(r["Gls"], yi, int(r["Gls"]), ha="center", va="center",
                color=BG, fontsize=10, fontweight="bold", zorder=4)
        ax.text(-m * 0.04, yi, f"{r['Player']}  ·  {r['Country']}", ha="right",
                va="center", color=INK, fontsize=10)
    ax.set_xlim(-m * 0.5, m * 1.12)
    ax.set_yticks([])
    ax.set_xticks([])
    return _finish(ax, "The Golden Boot Race",
                   f"Top {n} goalscorers  ·  goals in the tournament", save_path)


def finishers_vs_playmakers(df, min_90s=1.5, annotate=6, save_path=None):
    """Scatter every attacking contributor as goals (x) vs assists (y).

    Bubble size scales with minutes played and colour marks the position, so
    pure finishers sit to the right, creators sit high, and the complete
    forwards land up in the top-right corner.
    """
    d = df[(df["90s"] >= min_90s) & (df["Gls"] + df["Ast"] > 0)].copy()
    d["GA"] = d["Gls"] + d["Ast"]
    ax = _ax((9, 7.5))
    for pos, color in POS_COLORS.items():
        s = d[d["Pos"] == pos]
        ax.scatter(s["Gls"], s["Ast"], s=s["Min"] / 3 + 25, color=color,
                   alpha=0.75, edgecolor=BG, linewidth=0.6, label=pos)
    ax.axvline(d["Gls"].median(), color=GRID, lw=1, zorder=0)
    ax.axhline(d["Ast"].median(), color=GRID, lw=1, zorder=0)
    for i, (_, r) in enumerate(d.nlargest(annotate, "GA").iterrows()):
        dy = 7 if i % 2 == 0 else -15  # stagger so adjacent labels don't collide
        ax.annotate(r["Player"], (r["Gls"], r["Ast"]), xytext=(8, dy),
                    textcoords="offset points", color=INK, fontsize=9)
    ax.set_xlabel("Goals", color=MUTED)
    ax.set_ylabel("Assists", color=MUTED)
    ax.set_xlim(right=d["Gls"].max() * 1.28)
    ax.grid(True, color=GRID, lw=0.6, alpha=0.5)
    leg = ax.legend(title="Position", frameon=False, labelcolor=INK,
                    loc="upper right")
    leg.get_title().set_color(MUTED)
    return _finish(ax, "Finishers vs. Playmakers",
                   "Each bubble is a player  ·  size = minutes played", save_path)


def nation_firepower(df, n=12, save_path=None):
    """Radial bar chart of total goals scored by the top ``n`` nations."""
    g = df.groupby("Country")["Gls"].sum().sort_values(ascending=False).head(n)
    ax = _ax((8.5, 8.5), polar=True)
    theta = np.linspace(0, 2 * np.pi, len(g), endpoint=False)
    width = 2 * np.pi / len(g) * 0.86
    colors = plt.cm.YlOrRd(0.35 + 0.6 * g.values / g.values.max())
    ax.bar(theta, g.values, width=width, color=colors, edgecolor=BG,
           linewidth=1.5, zorder=3)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(theta)
    ax.set_xticklabels([])
    ax.set_yticks([])
    ax.set_ylim(0, g.values.max() * 1.18)
    ax.spines["polar"].set_visible(False)
    ax.grid(color=GRID, lw=0.6, alpha=0.6)
    for t, (name, val) in zip(theta, g.items()):
        ax.text(t, val + g.values.max() * 0.05, f"{name}\n{int(val)}",
                ha="center", va="center", color=INK, fontsize=8.5,
                fontweight="bold")
    return _finish(ax, "National Firepower",
                   "Total goals scored by nation", save_path)


def tournament_trend(by_year, stat="Gls", save_path=None):
    """Line chart of a summed ``stat`` across tournaments.

    ``by_year`` maps a tournament label (e.g. ``2018``) to its DataFrame.
    """
    years = sorted(by_year)
    totals = [float(by_year[y][stat].sum()) for y in years]
    ax = _ax((9, 5))
    ax.plot(years, totals, color=GOLD, lw=2.5, marker="o", ms=10,
            mec=BG, mew=1.5, zorder=3)
    ax.fill_between(years, totals, color=GOLD, alpha=0.12)
    for x, yv in zip(years, totals):
        ax.text(x, yv + max(totals) * 0.04, int(yv), ha="center",
                color=INK, fontsize=10, fontweight="bold")
    ax.set_xticks(years)
    ax.set_xticklabels(years, color=MUTED)
    ax.set_yticks([])
    ax.margins(y=0.2)
    ax.grid(True, axis="x", color=GRID, lw=0.6, alpha=0.4)
    return _finish(ax, f"World Cup Pulse  ·  total {stat}",
                   "Summed across every player each tournament", save_path)
