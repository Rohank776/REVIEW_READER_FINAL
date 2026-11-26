# CLAUDE.md — Standing orders for the Review Reader project

Read this file at the start of every session and follow it.

## What this project is
**Review Reader**: a small Python tool that reads a CSV of app-store reviews,
gives each review one complaint label, and shows the **top 3 complaints per week**
as a chart and a short text report.

**Who it is for:** a small app team (product manager / marketer) that gets
hundreds of reviews a month and has no time to read them all.

## Who I am (the builder)
- I am a **beginner in Python**. Keep every piece of code **very simple**.
- I must be able to explain every line in my demo without the AI in front of me.

## Coding rules
1. Use only **plain Python** plus **matplotlib** for the chart. No pandas, no AI APIs, no web frameworks.
2. Use the built-in `csv` module and `collections.Counter`.
3. Write short functions with clear names. Put a one-line comment above each function saying what it does.
4. No classes, no decorators, no list-comprehension tricks that are hard to read. Plain `for` loops are preferred.
5. Every script must run with one command, e.g. `python review_reader.py`.
6. Keep the number of files small (see the plan). Do not add new files without telling me why.

## The label rubric (how a review gets its label)
Each review gets **exactly one** label. Check the labels **in this order** and use the
first one whose keywords appear in the review text (lower-cased, **whole words only**,
so "ad" must not match inside "read" or "download"):

| Order | Label | Example keywords |
|---|---|---|
| 1 | crash_bug | crash, crashes, bug, freeze, error, broken |
| 2 | login_account | login, log in, password, account, sign in |
| 3 | slow_performance | slow, lag, loading, battery |
| 4 | price | price, expensive, subscription, charge, refund, cost |
| 5 | ads | ad, ads, advert, popup |
| 6 | support | support, customer service, no reply, help desk |
| 7 | design_ui | confusing, design, layout, button, hard to find |
| 8 | no_complaint | anything else (praise or neutral) |

The keyword lists live in **one place** in the code (a dictionary at the top of
`review_reader.py`) so I can change them easily.

## The agent
The skill `/review-report` (`.claude/skills/review-report/SKILL.md`) turns Claude into the
Review Reader agent: it runs `review_reader.py` as its tool, checks labels like a human,
and writes `weekly_summary.md`. It never edits code or data.

## How we work
- **Plan first.** Before building anything new, show me a plan and wait for my OK.
- **Check by hand.** After a change, tell me one number I can count myself in the CSV to confirm it works.
- **Log attempts.** When something does not work and we change it, add a short entry to `BUILD_LOG.md`
  (what we tried, what went wrong, what we changed).
- Never hide a problem. If something is slow, wrong, or unfinished, say so plainly.
