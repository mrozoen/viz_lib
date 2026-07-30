"""Aesthetic 2026 World Cup player-stat visualizations, built on matplotlib.
Warm-charcoal theme; charts take a DataFrame from load(), return an Axes, and
accept save_path=. Named players wear their country's flag.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Circle

try:
    import flagpy as _flagpy
except Exception:  # flags degrade gracefully to a plain disc
    _flagpy = None

# ── Palette: coral + gold accents on a warm charcoal ground ────────────────
BG, INK, MUTED = "#211d1b", "#f2ede6", "#9b938a"
CORAL, GOLD, GRID = "#ff8a4c", "#e9b949", "#3a342e"

# Players always named on the minutes-vs-goals chart.
REQUIRED = ["Cristiano Ronaldo", "Kylian Mbappé", "Erling Haaland",
            "Jude Bellingham", "Lamine Yamal", "Neymar"]

# flagpy names a few nations differently from the dataset.
_ALIAS = {"Netherlands": "The Netherlands", "United States": "The United States",
          "Czech Republic": "The Czech Republic", "Korea Republic": "South Korea",
          "IR Iran": "Iran"}


def _finish(ax, title, subtitle=None, save_path=None):
    """Editorial headline + gold subtitle, then save/return the axes."""
    ax.set_title(title, color=INK, fontsize=17, fontweight="bold",
                 loc="left", pad=30)
    if subtitle:
        ax.annotate(subtitle, xy=(0, 1), xytext=(0, 10), va="bottom",
                    xycoords="axes fraction", textcoords="offset points",
                    color=GOLD, fontsize=10.5)
    if save_path:
        ax.figure.savefig(save_path, dpi=150, bbox_inches="tight",
                          facecolor=ax.figure.get_facecolor())
    return ax


def _flag(country):
    """Square RGB flag array for ``country``, or None if unavailable."""
    if country == "England":  # not an ISO country: draw the St George's cross
        img = np.ones((120, 120, 3))
        img[49:71, :] = img[:, 49:71] = (0.80, 0.11, 0.15)
        return img
    if _flagpy is None:
        return None
    try:
        img = np.asarray(_flagpy.get_flag_img(_ALIAS.get(country, country)).convert("RGB"))
    except Exception:
        return None
    h, w = img.shape[:2]
    s = min(h, w)  # centre-crop to a square so the circle isn't distorted
    return img[(h - s) // 2:(h - s) // 2 + s, (w - s) // 2:(w - s) // 2 + s]


def _pick(pool, k, by):
    """First ``k`` rows of ``pool`` (highest ``by``) whose country has a flag."""
    rows = []
    for _, r in pool.sort_values(by, ascending=False).iterrows():
        if len(rows) >= k:
            break
        if _flag(r["Country"]) is not None:
            rows.append(r)
    return pd.DataFrame(rows, columns=pool.columns)


def _avatar(fig, cx, cy, dia, country):
    """A circular flag medallion centred at figure point (cx, cy)."""
    w = dia * fig.get_figheight() / fig.get_figwidth()  # keep the circle round
    a = fig.add_axes([cx - w / 2, cy - dia / 2, w, dia])
    a.set(xlim=(-1, 1), ylim=(-1, 1), aspect="equal")
    a.set_axis_off()
    img = _flag(country)
    if img is not None:
        im = a.imshow(img, extent=(-1, 1, -1, 1), aspect="auto", zorder=3)
        im.set_clip_path(Circle((0, 0), 0.97, transform=a.transData))
    else:
        a.add_patch(Circle((0, 0), 0.97, color="#332d28", zorder=2))
    a.add_patch(Circle((0, 0), 0.97, fill=False, lw=2.5, ec=CORAL, zorder=5))


def load(path):
    """Read a stats CSV, cleaning ``"fr France"`` squad codes into ``Country``."""
    df = pd.read_csv(path)
    df["Country"] = df["Squad"].astype(str).str.replace(
        r"^[a-z]{2,3}\s+", "", regex=True)
    for col in ["Gls", "Ast", "Min", "90s", "Age", "MP", "CrdY", "CrdR"]:
        if col in df:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def minutes_vs_goals(df, max_avatars=8, save_path=None):
    """Minutes played (x) vs goals scored (y) for a curated cast.

    Names the REQUIRED stars, then fills up to ``max_avatars`` more slots, split
    between most goals in fewest minutes and fewest goals in most minutes.
    """
    d = df[df["Min"] > 0].copy()
    d["per90"] = d["Gls"] * 90 / d["Min"]
    named = d[d["Player"].isin(REQUIRED)]
    remaining = max(0, max_avatars - len(named))
    high = _pick(d[~d["Player"].isin(named["Player"]) & (d["Min"] >= 180)
                   & (d["Gls"] >= 2)], remaining - remaining // 2, "per90")
    low = _pick(d[~d["Player"].isin(pd.concat([named, high])["Player"])
                  & (d["Gls"] == 0)], remaining // 2, "Min")
    cast = (pd.concat([named, high, low])
            .drop_duplicates("Player").sort_values("Min"))

    fig = plt.figure(figsize=(13, 9.5))
    fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0.07, 0.30, 0.90, 0.58])
    ax.set_facecolor(BG)
    ax.spines[:].set_visible(False)
    ax.tick_params(colors=MUTED, labelsize=9)

    xmax = float(cast["Min"].max())
    ax.plot([0, xmax], [0, xmax / 90], color=MUTED, lw=1, ls="--",
            alpha=0.55, zorder=1)
    ax.annotate("a goal every 90 min", xy=(xmax, xmax / 90), xytext=(-8, 9),
                textcoords="offset points", ha="right", color=MUTED,
                fontsize=9, style="italic")
    for size, alpha in ((1020, 0.05), (442, 0.12), (170, 1.0)):  # neon bloom
        ax.scatter(cast["Min"], cast["Gls"], s=size, color=CORAL, alpha=alpha,
                   edgecolors="none", zorder=5)
    ax.set_xlabel("Minutes played", color=MUTED, fontsize=11)
    ax.set_ylabel("Goals scored", color=MUTED, fontsize=11)
    ax.grid(True, color=GRID, lw=0.7, alpha=0.6)
    ax.margins(0.12)
    ax.set_ylim(bottom=-0.6)
    _finish(ax, "WHERE MINUTES BECOME GOALS",
            "2026 World Cup  ·  the sharpest finishers, and the grinders who never scored")

    over = fig.add_axes([0, 0, 1, 1])
    over.set_axis_off()
    over.set(xlim=(0, 1), ylim=(0, 1))
    over.patch.set_alpha(0)
    cy, dia = 0.135, 0.13
    for cx, (_, r) in zip(np.linspace(0.07, 0.95, len(cast)), cast.iterrows()):
        fx, fy = fig.transFigure.inverted().transform(
            ax.transData.transform((r["Min"], r["Gls"])))
        over.plot([fx, cx], [fy, cy + dia / 2], color=CORAL, lw=1.1,
                  alpha=0.45, zorder=1)
        _avatar(fig, cx, cy, dia, r["Country"])
        parts = r["Player"].split()
        label = parts[0] if len(parts) == 1 else f"{parts[0]}\n{parts[-1]}"
        over.text(cx, cy - dia / 2 - 0.015, label, ha="center", va="top",
                  color=INK, fontsize=8.5, fontweight="bold", linespacing=1.1,
                  zorder=6)

    if save_path:
        fig.savefig(save_path, dpi=150, facecolor=BG)
    return ax


def nation_firepower(df, n=12, save_path=None):
    """A simple bar chart of goals by the top ``n`` nations, each bar flag-tipped."""
    g = df.groupby("Country")["Gls"].sum().sort_values().tail(n)
    vals, top = g.values, g.values.max()
    fig = plt.figure(figsize=(10, 8))
    fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0.17, 0.08, 0.70, 0.82])
    ax.set_facecolor(BG)
    ax.spines[:].set_visible(False)
    ax.tick_params(colors=MUTED, labelsize=10)
    y = np.arange(len(g))
    ax.barh(y, vals, height=0.6, zorder=2,
            color=[GOLD if v == top else CORAL for v in vals])
    ax.set_yticks(y)
    ax.set_yticklabels(g.index, color=INK)
    ax.set_xticks([])
    ax.set_xlim(0, top * 1.22)
    for yi, v, country in zip(y, vals, g.index):
        fx, fy = fig.transFigure.inverted().transform(
            ax.transData.transform((v + top * 0.04, yi)))
        _avatar(fig, fx, fy, 0.052, country)
        ax.text(v + top * 0.095, yi, int(v), va="center", color=INK,
                fontsize=10, fontweight="bold")
    _finish(ax, "NATIONAL FIREPOWER",
            "2026 World Cup  ·  total goals scored by nation")
    if save_path:
        fig.savefig(save_path, dpi=150, facecolor=BG)
    return ax
