"""Visualize the 2026 World Cup player-stats dataset with viz_lib.

Usage:
    python examples/worldcup_analysis.py

Saves two PNGs into examples/charts/.
"""

import os

import viz_lib

HERE = os.path.dirname(__file__)
CSV = os.path.join(HERE, "data", "wcplayerstatistics2026.csv")
OUT = os.path.join(HERE, "charts")


def main():
    os.makedirs(OUT, exist_ok=True)
    df = viz_lib.load(CSV)
    print(f"2026 World Cup: {len(df)} players.")

    viz_lib.minutes_vs_goals(
        df, save_path=os.path.join(OUT, "minutes_vs_goals.png"))
    viz_lib.nation_firepower(
        df, save_path=os.path.join(OUT, "nation_firepower.png"))

    print(f"Saved 2 charts to {OUT}/")


if __name__ == "__main__":
    main()
