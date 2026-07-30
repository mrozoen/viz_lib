"""Aesthetic 2026 World Cup player-stat visualizations, built on matplotlib.

Two editorial, neon-styled charts share one "midnight pitch" look: a deep
indigo background with a complementary **teal + coral** palette. Each function
takes a tidy DataFrame from :func:`load` and returns a matplotlib ``Axes``;
pass ``save_path=`` to write a PNG straight to disk.
"""

from __future__ import annotations

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ── Palette: complementary teal + coral on a deep indigo night ─────────────
BG, INK, MUTED = "#140a2e", "#ece9f7", "#8b86ad"
TEAL, CORAL, GRID = "#22d3ee", "#ff8a4c", "#2a2050"
TEAL_RAMP = mcolors.LinearSegmentedColormap.from_list(
    "teal", ["#0e5563", "#17a2c4", "#22d3ee", "#a5f3fc"])


def _ax(figsize, polar=False):
    """Make a styled figure + axes in the shared midnight-pitch theme."""
    fig, ax = plt.subplots(figsize=figsize, subplot_kw={"polar": polar})
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(colors=MUTED, labelsize=9)
    return ax


def _finish(ax, title, subtitle=None, save_path=None):
    """Add the editorial headline (+ teal subtitle), then save/return the axes."""
    ax.set_title(title, color=INK, fontsize=17, fontweight="bold",
                 loc="left", pad=30)
    if subtitle:
        ax.annotate(subtitle, xy=(0, 1), xytext=(0, 10), va="bottom",
                    xycoords="axes fraction", textcoords="offset points",
                    color=TEAL, fontsize=10.5)
    if save_path:
        ax.figure.savefig(save_path, dpi=150, bbox_inches="tight",
                          facecolor=ax.figure.get_facecolor())
    return ax


def _glow(ax, x, y, color, core=170, zorder=5):
    """Draw a soft neon bloom by stacking translucent copies of a marker."""
    for size, alpha in ((core * 6, 0.05), (core * 2.6, 0.12), (core, 1.0)):
        ax.scatter(x, y, s=size, color=color, alpha=alpha,
                   edgecolors="none", zorder=zorder)


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


def minutes_vs_goals(df, highlight=8, save_path=None):
    """Scatter every player as minutes played (x) vs goals scored (y).

    The whole tournament forms a faint teal field; the top ``highlight``
    finishers glow coral and are named. A dashed guide marks the elite
    "a goal every 90 minutes" scoring pace.
    """
    d = df[df["Min"] > 0].copy()
    ax = _ax((10, 7.5))
    ax.scatter(d["Min"], d["Gls"], s=26, color=TEAL, alpha=0.28,
               edgecolors="none", zorder=2)

    xmax = float(d["Min"].max())
    ax.plot([0, xmax], [0, xmax / 90], color=MUTED, lw=1, ls="--",
            alpha=0.55, zorder=1)
    ax.annotate("a goal every 90 min", xy=(xmax, xmax / 90), xytext=(-8, 9),
                textcoords="offset points", ha="right", color=MUTED,
                fontsize=9, style="italic")

    top = d.nlargest(highlight, "Gls")
    _glow(ax, top["Min"], top["Gls"], CORAL)
    for i, (_, r) in enumerate(top.iterrows()):
        dy = 8 if i % 2 == 0 else -14  # stagger so adjacent names don't collide
        ax.annotate(r["Player"], (r["Min"], r["Gls"]), xytext=(10, dy),
                    textcoords="offset points", color=INK, fontsize=9.5,
                    fontweight="bold")

    ax.set_xlabel("Minutes played", color=MUTED, fontsize=11)
    ax.set_ylabel("Goals scored", color=MUTED, fontsize=11)
    ax.grid(True, color=GRID, lw=0.7, alpha=0.6)
    ax.margins(0.07)
    ax.set_xlim(right=xmax * 1.2)  # headroom for the rightmost player labels
    return _finish(ax, "WHERE MINUTES BECOME GOALS",
                   "2026 World Cup  ·  every player, and the finishers who beat the pace",
                   save_path)


def nation_firepower(df, n=12, save_path=None):
    """Radial bar chart of total goals scored by the top ``n`` nations.

    Bars run a light-to-deep teal ramp by goals; the leading nation blazes
    coral so the eye lands on it first.
    """
    g = df.groupby("Country")["Gls"].sum().sort_values(ascending=False).head(n)
    vals = g.values
    ax = _ax((8.5, 8.5), polar=True)
    theta = np.linspace(0, 2 * np.pi, len(g), endpoint=False)
    width = 2 * np.pi / len(g) * 0.82
    colors = [mcolors.to_rgba(CORAL) if v == vals.max()  # leader(s) blaze coral
              else mcolors.to_rgba(c)
              for v, c in zip(vals, TEAL_RAMP(0.25 + 0.7 * vals / vals.max()))]
    ax.bar(theta, vals, width=width, color=colors, edgecolor=BG,
           linewidth=2, zorder=3)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim(0, vals.max() * 1.2)
    ax.spines["polar"].set_visible(False)
    ax.grid(color=GRID, lw=0.7, alpha=0.5)
    for t, (name, val) in zip(theta, g.items()):
        color = CORAL if val == vals.max() else INK
        ax.text(t, val + vals.max() * 0.06, f"{name}\n{int(val)}", ha="center",
                va="center", color=color, fontsize=9, fontweight="bold")
    return _finish(ax, "NATIONAL FIREPOWER",
                   "2026 World Cup  ·  total goals scored by nation", save_path)
