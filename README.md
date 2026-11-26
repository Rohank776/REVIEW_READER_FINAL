# Review Reader

**What it does:** reads a CSV of app-store reviews, gives each review one complaint label
(crash/bug, login, slow, price, ads, support, design, or no complaint), and shows the
**top 3 complaints for each week** as a text report and a bar chart.

**Who it is for:** a small app team that gets hundreds of reviews a month and has no time
to read them all, but needs to know what users are complaining about this week.

**Why it is built this way:** labels come from a keyword list (in `CLAUDE.md` and at the top of
`review_reader.py`), so every label can be explained and checked by hand. It needs no internet
and no API key.

## How to run

Needs Python 3 and matplotlib (`pip install matplotlib`).

```
python make_sample_data.py     # creates reviews.csv (200 synthetic reviews, Nov 2026)
python review_reader.py        # labels them and writes the outputs
```

`reviews.csv` is already in the repository, so the first command is optional.

## Run the agent

The project also works as an agent inside Claude Code:

1. Open Claude Code in this folder.
2. Type `/review-report`.

Claude runs `review_reader.py` as its tool, reads the report, checks up to 20 labels like a human
(it catches mistakes like "Not expensive" being counted as a price complaint), and writes
`weekly_summary.md` for the app team. The skill is in `.claude/skills/review-report/SKILL.md`.

## Outputs
| File | What is in it |
|---|---|
| `labeled_reviews.csv` | every review with its label (for checking by hand) |
| `report.txt` | top 3 complaints per week (also printed in the terminal) |
| `top_complaints.png` | bar chart of the complaints per week |
| `weekly_summary.md` | the agent's one-page summary (made by `/review-report`) |

## Files
| File | Purpose |
|---|---|
| `review_reader.py` | the tool |
| `make_sample_data.py` | makes the synthetic review data |
| `CLAUDE.md` | standing orders for Claude Code, including the label rubric |
| `BUILD_LOG.md` | what was tried, what did not work, what was changed |

## Known limitation
Keyword matching cannot understand negation: "Not expensive at all" is labeled `price`.
