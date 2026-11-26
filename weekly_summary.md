# Weekly review summary — November 2026

## Headline
Crash complaints jumped in week 47 (16 reviews, the biggest number of the month), and in week 48 support became the #1 complaint.

## Top 3 complaints per week
| Week | #1 | #2 | #3 |
|---|---|---|---|
| 2026-W45 | ads: 10 | slow_performance: 8 | price: 8 |
| 2026-W46 | login_account: 8 | price: 8 | design_ui: 6 |
| 2026-W47 | crash_bug: 16 | price: 7 | slow_performance: 5 |
| 2026-W48 | support: 9 | price: 8 | crash_bug: 6 |

Reviews read by the tool: 200.

## What changed
`crash_bug` was not in the top 3 in week 46 and jumped to #1 with 16 in week 47, which looks like a bad app update.
In week 48 crashes fell to 6, but `support` rose to #1 with 9, likely because users who hit the crash asked for help and got no answer.

## Labels I think are wrong
| review_id | text | given label | should be |
|---|---|---|---|
| 133 | Not expensive at all, great value for money. | price | no_complaint |
| 135 | Not expensive at all, great value for money. | price | no_complaint |

Both are praise. The keyword "expensive" matched, but the word "not" reverses the meaning.
So the `price: 7` for week 47 includes 2 reviews that are not complaints.
The same sentence appears in other weeks too, so `price` is over-counted across the month.

**Suggested keyword change (the user decides):** skip the `price` label when "not expensive" appears in the text.

## What to fix first
1. Find and fix what the week-47 update broke (crashes, freezes, the save button). It was the biggest spike of the month.
2. Answer the support backlog. Users say they get no reply or a copy-paste answer, and support is now the #1 complaint.
3. Keep watching `price`. It sits in the top 3 every week, but part of that count is praise ("not expensive") wrongly counted as a complaint.

## Checked
I read 22 reviews from week 47 (the biggest week) and week 48 (the newest week): every 5th review from Nov 16 onward, plus the 2 "Not expensive" reviews in week 47.
20 labels were right, and 2 were wrong (above).
