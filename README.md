# viz_lib

A tiny, real Python library for quickly visualizing a pandas DataFrame with
matplotlib. No web app, no dashboard — just useful, installable, importable
plotting functions.

## Install

```bash
pip install viz_lib
```

Or install from a local checkout:

```bash
pip install -e .
```

## Usage

Every function takes a pandas `DataFrame` and returns a matplotlib `Axes`.
Pass `save_path=...` to write the chart straight to a file.

```python
import pandas as pd
import viz_lib

df = pd.read_csv("data.csv")

# Distribution of one numeric column
viz_lib.plot_histogram(df, "age")

# Value counts of a categorical column (top 10 categories)
viz_lib.plot_bar(df, "city", top=10)

# Relationship between two numeric columns
viz_lib.plot_scatter(df, "height", "weight")

# Correlation heatmap of all numeric columns
viz_lib.plot_correlation(df)

# Missing values per column
viz_lib.plot_missing(df, save_path="missing.png")

import matplotlib.pyplot as plt
plt.show()
```

## Functions

| Function | What it does |
| --- | --- |
| `plot_histogram(df, column, bins=20)` | Distribution of one numeric column |
| `plot_bar(df, column, top=None)` | Bar chart of a categorical column's value counts |
| `plot_multi_value_bar(df, column, sep=",", top=None)` | Counts for cells holding several values, e.g. `"Dramas, Comedies"` |
| `plot_scatter(df, x, y)` | Scatter plot of two numeric columns |
| `plot_correlation(df)` | Correlation heatmap of all numeric columns |
| `plot_missing(df)` | Count of missing values per column |

All functions also accept `ax=` (an existing matplotlib Axes) and
`save_path=` (a file path to save the figure).

## Example: the Netflix titles dataset

[`examples/netflix_analysis.py`](examples/netflix_analysis.py) explores the
[Netflix titles dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows).
Download `netflix_titles.csv` from Kaggle, then run:

```bash
python examples/netflix_analysis.py path/to/netflix_titles.csv
```

It saves a 6-panel `netflix_overview.png`: Movies vs TV Shows, release-year
and date-added distributions, top 10 genres, top 10 countries, and movie
runtimes. It also shows how the same functions compose into a grid by passing
each an `ax=`.

## Requirements

- Python 3.8+
- pandas
- matplotlib

## License

MIT — see [LICENSE](LICENSE).
