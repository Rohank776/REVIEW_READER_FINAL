# Build log

A running record of how I used Claude Code: what I asked, what I checked,
what did not work, and what I changed. (Source for the "How AI was used" slides.)

## 2026-11-25 — Session 1: setup
- **Asked:** Claude to read the project brief and suggest ideas. Picked **Review Reader**.
- **Decided:** synthetic data (no real reviews available), very basic Python (I am a beginner).
- **Wrote standing orders:** `CLAUDE.md` with the coding rules and the label rubric.
- **Plan first:** Claude proposed a build plan in plan mode; I read it before the build.
  - What I changed in the plan: rewrote the Context as a direct instruction and cut the plan
    down to just the files and functions (removed the extra sections).

## 2026-11-25 — Session 1: first build
- **Built:** `make_sample_data.py` (200 synthetic reviews, 4 weeks, a "bad update" crash spike
  in week 47) and `review_reader.py` (label → count per week → report + chart).
- **Tried:** labeling with a simple check: "is the keyword anywhere inside the text?"
- **What went wrong:** checking each distinct sentence by hand, two praise reviews were labeled `ads`:
  - "I **read** the news on it every morning" — "read" contains "ad"
  - "The **download** was quick and setup was easy" — "download" contains "ad"
  - Result: `ads` was wrongly the #1 complaint in week 45 (12) and week 48 (10).
- **What I changed:** match whole words only (`clean_text` turns punctuation into spaces and
  the keyword must have a space on both sides). After the fix: week 45 `ads` = 10,
  and `ads` dropped out of week 48's top 3 (support is now #1 there).
- **How I checked it by hand:** counted `price` rows dated Nov 2–8 in `labeled_reviews.csv` = 8,
  same as `report.txt`. Read all 34 distinct sentences and their labels.
- **Still wrong (named, not hidden):** "**Not** expensive at all, great value for money" is labeled
  `price`. Keywords cannot understand "not". Possible next step: let an AI model do the labeling.

## 2026-11-26 — Session 2: turning the script into an agent
- **Why:** the script follows fixed steps and cannot understand meaning ("Not expensive").
  An agent can read the output, judge the labels and explain what changed.
- **Options considered:** (1) a Claude Code skill, (2) AI labeling inside the script,
  (3) a full Python agent with the Claude API. Picked (1): no API key or cost, no new Python,
  and the working script stays as the agent's tool and as a safe fallback for the demo.
- **Plan first:** plan mode again. The plan was approved as written.
- **Built:** `.claude/skills/review-report/SKILL.md`, which runs the tool, copies numbers only from
  `report.txt`, checks up to 20 labels, writes `weekly_summary.md`, and never edits code or data.
- **What the agent found:** 2 wrong labels in week 47 (review ids 133 and 135, "Not expensive at all…"
  labeled `price`). The keyword tool missed these. It also linked the week-48 rise in support
  complaints to the week-47 crash spike.
- **Checked by hand:** `crash_bug` rows dated Nov 16–22 = 16, matching the report.
  Also counted all "Not expensive" rows in the month = 6, all labeled `price`.
- **Rule I added on purpose:** the agent must copy numbers from `report.txt` and never count them
  itself, so the numbers in the summary always match the tool.

## Template for each new entry
- **Tried:**
- **What went wrong:**
- **What I changed:**
- **How I checked it by hand:**
