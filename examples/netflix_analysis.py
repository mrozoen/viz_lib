"""Explore the Netflix titles dataset with viz_lib.

Dataset: https://www.kaggle.com/datasets/shivamb/netflix-shows

Download ``netflix_titles.csv`` from Kaggle, then run:

    python examples/netflix_analysis.py path/to/netflix_titles.csv

If you leave the path off, it looks for ``netflix_titles.csv`` in the
current directory. The script saves a 6-panel overview to
``netflix_overview.png`` and also shows it on screen.
"""

import sys

import matplotlib.pyplot as plt
import pandas as pd

import viz_lib


def load(path):
    """Load the CSV and derive two helper columns for plotting."""
    df = pd.read_csv(path)
    # Year each title was added to Netflix (date_added -> year).
    df["year_added"] = pd.to_datetime(df["date_added"], errors="coerce").dt.year
    # Movie runtime in minutes ("90 min" -> 90.0); NaN for TV shows.
    movies = df["type"] == "Movie"
    df.loc[movies, "duration_min"] = (
        df.loc[movies, "duration"].str.replace(" min", "", regex=False).astype(float)
    )
    return df


def main(path="netflix_titles.csv"):
    df = load(path)

    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle("Netflix titles — a quick look", fontsize=16)

    # Row 1: what kind of content, when it was made, when it was added.
    viz_lib.plot_bar(df, "type", ax=axes[0, 0])
    viz_lib.plot_histogram(df, "release_year", bins=30, ax=axes[0, 1])
    viz_lib.plot_histogram(df, "year_added", bins=15, ax=axes[0, 2])

    # Row 2: top genres, top countries, movie runtimes.
    viz_lib.plot_multi_value_bar(df, "listed_in", top=10, ax=axes[1, 0])
    viz_lib.plot_multi_value_bar(df, "country", top=10, ax=axes[1, 1])
    viz_lib.plot_histogram(df, "duration_min", bins=30, ax=axes[1, 2])

    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig("netflix_overview.png", dpi=150)
    print("Saved netflix_overview.png")
    plt.show()


if __name__ == "__main__":
    main(*sys.argv[1:])
