"""Visualize the World Cup player-stats dataset with viz_lib.

Usage:
    python examples/worldcup_analysis.py            # uses examples/data/*.csv
    python examples/worldcup_analysis.py 2018       # pick a single tournament

Saves four PNGs into examples/charts/.
"""

import glob
import os
import re
import sys

import viz_lib

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, "data")
OUT = os.path.join(HERE, "charts")


def year_of(path):
    return int(re.search(r"(\d{4})", os.path.basename(path)).group(1))


def main():
    os.makedirs(OUT, exist_ok=True)
    paths = sorted(glob.glob(os.path.join(DATA, "wcplayerstatistics*.csv")))
    by_year = {year_of(p): viz_lib.load(p) for p in paths}

    year = int(sys.argv[1]) if len(sys.argv) > 1 else max(by_year)
    df = by_year[year]
    print(f"Featuring the {year} World Cup ({len(df)} players).")

    viz_lib.golden_boot(df, save_path=os.path.join(OUT, "golden_boot.png"))
    viz_lib.finishers_vs_playmakers(
        df, save_path=os.path.join(OUT, "finishers_vs_playmakers.png"))
    viz_lib.nation_firepower(
        df, save_path=os.path.join(OUT, "nation_firepower.png"))
    viz_lib.tournament_trend(
        by_year, save_path=os.path.join(OUT, "tournament_trend.png"))

    print(f"Saved 4 charts to {OUT}/")


if __name__ == "__main__":
    main()
