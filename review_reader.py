# review_reader.py
# Reads reviews.csv, gives every review one complaint label,
# and shows the top 3 complaints for each week (terminal, report.txt, chart).

import csv
from collections import Counter
from datetime import date

import matplotlib
matplotlib.use("Agg")  # draw the chart into a file, no window needed
import matplotlib.pyplot as plt

# The label rubric from CLAUDE.md. Labels are checked in this order;
# the first label with a matching keyword wins.
LABEL_KEYWORDS = {
    "crash_bug": ["crash", "crashes", "crashed", "bug", "bugs", "freeze", "freezing", "error", "broken"],
    "login_account": ["login", "log in", "password", "account", "sign in"],
    "slow_performance": ["slow", "lag", "laggy", "loading", "battery"],
    "price": ["price", "expensive", "subscription", "charge", "charged", "refund", "cost"],
    "ads": ["ad", "ads", "advert", "popup"],
    "support": ["support", "customer service", "no reply", "help desk"],
    "design_ui": ["confusing", "design", "layout", "button", "hard to find"],
}

INPUT_FILE = "reviews.csv"
LABELED_FILE = "labeled_reviews.csv"
REPORT_FILE = "report.txt"
CHART_FILE = "top_complaints.png"


# Read the CSV file into a list of dictionaries (one per review).
def load_reviews(path):
    reviews = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            reviews.append(row)
    return reviews


# Make the text easy to search: lower case, punctuation turned into spaces,
# and a space at the start and end. "Bad ad!" becomes " bad ad  ".
def clean_text(text):
    text = text.lower()
    for mark in ".,!?;:()-'\"":
        text = text.replace(mark, " ")
    return " " + text + " "


# Return the first label whose keyword appears in the review text as a whole word.
# The spaces around the keyword stop "ad" from matching inside "read" or "download".
def label_review(text):
    text = clean_text(text)
    for label in LABEL_KEYWORDS:
        for keyword in LABEL_KEYWORDS[label]:
            if " " + keyword + " " in text:
                return label
    return "no_complaint"


# Turn a date like "2026-11-03" into a week name like "2026-W45".
def week_of(date_text):
    d = date.fromisoformat(date_text)
    year, week, weekday = d.isocalendar()
    return str(year) + "-W" + str(week).zfill(2)


# Count the complaint labels for each week (praise is not a complaint, so skip it).
def count_by_week(reviews):
    counts = {}
    for review in reviews:
        if review["label"] == "no_complaint":
            continue
        week = week_of(review["date"])
        if week not in counts:
            counts[week] = Counter()
        counts[week][review["label"]] += 1
    return counts


# Save every review with its new label, so the labels can be checked by hand.
def save_labeled(reviews, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["review_id", "date", "rating", "text", "label"])
        writer.writeheader()
        for review in reviews:
            writer.writerow(review)


# Build the text report: the top 3 complaints for each week.
def make_report(counts, total_reviews):
    lines = []
    lines.append("REVIEW READER - top 3 complaints per week")
    lines.append("Reviews read: " + str(total_reviews))
    lines.append("")
    for week in sorted(counts):
        lines.append(week)
        rank = 1
        for label, number in counts[week].most_common(3):
            lines.append("  " + str(rank) + ". " + label + ": " + str(number))
            rank = rank + 1
        lines.append("")
    return "\n".join(lines)


# Draw a bar chart: one group of bars per week, one bar per top-3 complaint.
def make_chart(counts, path):
    weeks = sorted(counts)

    # Collect every label that is in the top 3 of at least one week.
    top_labels = []
    for week in weeks:
        for label, number in counts[week].most_common(3):
            if label not in top_labels:
                top_labels.append(label)

    bar_width = 0.8 / len(top_labels)
    plt.figure(figsize=(10, 5))
    for i in range(len(top_labels)):
        label = top_labels[i]
        x_positions = []
        heights = []
        for w in range(len(weeks)):
            x_positions.append(w + i * bar_width)
            heights.append(counts[weeks[w]][label])
        plt.bar(x_positions, heights, width=bar_width, label=label)

    middle_positions = []
    for w in range(len(weeks)):
        middle_positions.append(w + 0.4 - bar_width / 2)
    plt.xticks(middle_positions, weeks)
    plt.ylabel("Number of reviews")
    plt.title("Top complaints per week")
    plt.legend()
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


# Run the whole tool: load, label, count, then write the three outputs.
def main():
    reviews = load_reviews(INPUT_FILE)
    for review in reviews:
        review["label"] = label_review(review["text"])

    counts = count_by_week(reviews)
    save_labeled(reviews, LABELED_FILE)

    report = make_report(counts, len(reviews))
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report)
    make_chart(counts, CHART_FILE)

    print(report)
    print("Saved:", LABELED_FILE, REPORT_FILE, CHART_FILE)


main()
