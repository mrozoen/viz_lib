# viz_lib ⚽

A tiny, aesthetic Python library for visualizing **2026 World Cup player
statistics** with matplotlib. It's a minimal viable product: one package, two
bare-bones chart functions, and a single editorial look — a warm charcoal
background with **coral + gold** accents. No dashboards, no web app. Point it at
the season's CSV and get a poster-quality chart.

The whole library is **under 200 lines** ([`src/viz_lib/core.py`](src/viz_lib/core.py)).

## Install

From a local checkout:

```bash
pip install -e .
```

## The dataset

Player-level stats for the **2026 men's World Cup** — goals, assists, minutes,
position, nation, and more — in
[`examples/data/wcplayerstatistics2026.csv`](examples/data). Each row is one
player.

## Quickstart

```python
import matplotlib.pyplot as plt
import viz_lib

# load() cleans the "fr France" squad codes into a tidy Country column
df = viz_lib.load("examples/data/wcplayerstatistics2026.csv")

viz_lib.minutes_vs_goals(df)     # who turned minutes into goals
viz_lib.nation_firepower(df)     # goals by nation, as a flag-tipped bar chart
plt.show()

# every chart accepts save_path= to write a PNG straight to disk
viz_lib.minutes_vs_goals(df, save_path="minutes_vs_goals.png")
```

Or just run the bundled example, which builds both charts from the data folder:

```bash
python examples/worldcup_analysis.py
```

## The visualizations

### 🎯 Where Minutes Become Goals — `minutes_vs_goals(df, max_avatars=8)`

A curated cast plotted as **minutes played (x) vs goals scored (y)**, each
glowing coral and wearing their country's flag in a medallion below the chart —
an editorial photo strip, connected to their point. A dashed guide marks the
elite *"a goal every 90 minutes"* pace, so players above the line are
outscoring the clock and the grinders sit along the bottom.

The cast is a fixed set of stars (Ronaldo, Mbappé, Haaland, Bellingham, Lamine
Yamal, Neymar), and the remaining slots — capped by `max_avatars` to avoid
clutter — are split between the **most goals in the fewest minutes** and the
**fewest goals in the most minutes**.

![Where Minutes Become Goals](examples/charts/minutes_vs_goals.png)

### 🔥 National Firepower — `nation_firepower(df, n=12)`

A clean horizontal bar chart of total goals by the top `n` nations, ranked
highest-first. Each bar is **tipped with that country's flag** (the one small
flourish), values sit at the end, and the leaders are picked out in gold
(France and England, tied at 20).

![National Firepower](examples/charts/nation_firepower.png)

## API

| Function | What it does |
| --- | --- |
| `load(path)` | Read a stats CSV into a tidy DataFrame with a clean `Country` column |
| `minutes_vs_goals(df, max_avatars=8)` | Minutes-vs-goals scatter of a curated cast, with flag medallions |
| `nation_firepower(df, n=12)` | Horizontal bar chart of goals by the top `n` nations, flag-tipped |

Both chart functions return a matplotlib `Axes` (so you can keep tweaking) and
accept `save_path=` to write the figure to disk.

## Design notes

- **A shared warm-charcoal stage.** Both charts sit on the same `#211d1b`
  background with coral bars/marks and gold reserved for the standouts, so they
  read as one set.
- **Colour has one job.** Coral carries the data; gold marks the leaders (the
  top scorers, the top nations) — never a rainbow.
- **Honest marks.** The bloom on the scatter's points is drawn by stacking
  translucent copies, not faked with a second axis. Two variables on different
  scales (minutes vs goals) are shown as a scatter, never a dual-axis chart.
- **Flags, offline.** Country flags come from the bundled [`flagpy`](https://pypi.org/project/flagpy/)
  package (no network needed); England — which isn't an ISO country — is drawn
  as a St George's cross, and each flag is centre-cropped to a circle.

## Project layout

```
viz_lib/
├── pyproject.toml            # package metadata (build with setuptools)
├── src/viz_lib/
│   ├── __init__.py           # public API
│   └── core.py               # both charts + shared theme (< 200 lines)
└── examples/
    ├── worldcup_analysis.py  # runnable demo
    ├── data/                 # the 2026 World Cup CSV
    └── charts/               # generated PNGs (shown above)
```

## Requirements

Python 3.8+, plus `pandas`, `numpy`, `matplotlib`, and `flagpy` (installed
automatically).

## License

MIT — see [LICENSE](LICENSE).
