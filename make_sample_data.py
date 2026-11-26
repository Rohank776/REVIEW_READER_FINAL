# make_sample_data.py
# Creates reviews.csv: 200 fake app-store reviews over 4 weeks of November 2026.
# The data is synthetic (made up) so the project can be shown without real customer data.

import csv
import random
from datetime import date, timedelta

# Same seed = same "random" choices every run, so reviews.csv never changes.
random.seed(42)

# Hand-written review sentences, grouped by the complaint they are about.
# The tool does NOT see these groups; it only sees the text and must find the label itself.
SENTENCES = {
    "crash_bug": [
        "The app crashes every time I open the camera.",
        "Since the last update it keeps freezing on the home screen.",
        "Got an error message and lost all my notes.",
        "So many bugs after the update, please fix.",
        "The save button is broken, nothing happens.",
        "Bad update, the app crashed three times today.",
    ],
    "login_account": [
        "I cannot log in anymore, it says wrong password.",
        "Password reset email never arrives.",
        "My account was deleted for no reason.",
        "Sign in with Google does not work.",
    ],
    "slow_performance": [
        "Very slow to open, takes almost a minute.",
        "Loading takes forever on my phone.",
        "It drains my battery in two hours.",
        "Scrolling is laggy and the app feels slow.",
    ],
    "price": [
        "Too expensive for what it does.",
        "The subscription price doubled this month.",
        "They charged me twice and I want a refund.",
        "Nice app but the monthly cost is too high.",
    ],
    "ads": [
        "Way too many ads, one after every click.",
        "A popup ad covers the whole screen.",
        "I paid to remove ads and still see them.",
    ],
    "support": [
        "Customer service never answered my email.",
        "Wrote to support three times, no reply.",
        "The help desk just sends the same copy-paste answer.",
    ],
    "design_ui": [
        "The new layout is confusing.",
        "Settings are hard to find in the menu.",
        "The design looks nice but the button is too small.",
    ],
    "no_complaint": [
        "Love this app, use it every day!",
        "Great app, does exactly what I need.",
        "Five stars, works perfectly.",
        "Simple and useful, highly recommend.",
        "I read the news on it every morning.",
        "The download was quick and setup was easy.",
        "Not expensive at all, great value for money.",
    ],
}

# Star rating that fits each kind of review.
RATINGS = {
    "crash_bug": [1, 2],
    "login_account": [1, 2],
    "slow_performance": [2, 3],
    "price": [2, 3],
    "ads": [2, 3],
    "support": [1, 2],
    "design_ui": [3, 4],
    "no_complaint": [4, 5],
}

# How common each kind of review is in each week.
# Week 3 has a bad app update, so crash_bug jumps up. This gives the chart a story.
WEEK_WEIGHTS = [
    {"crash_bug": 2, "login_account": 2, "slow_performance": 2, "price": 4, "ads": 3, "support": 1, "design_ui": 2, "no_complaint": 6},
    {"crash_bug": 2, "login_account": 3, "slow_performance": 2, "price": 4, "ads": 3, "support": 2, "design_ui": 2, "no_complaint": 6},
    {"crash_bug": 9, "login_account": 2, "slow_performance": 3, "price": 3, "ads": 2, "support": 2, "design_ui": 1, "no_complaint": 4},
    {"crash_bug": 4, "login_account": 2, "slow_performance": 2, "price": 3, "ads": 2, "support": 4, "design_ui": 1, "no_complaint": 5},
]

FIRST_DAY = date(2026, 11, 2)  # a Monday
REVIEWS_PER_WEEK = 50


# Pick one kind of review for a week, using that week's weights.
def pick_kind(week_number):
    weights = WEEK_WEIGHTS[week_number]
    kinds = list(weights.keys())
    numbers = list(weights.values())
    return random.choices(kinds, weights=numbers)[0]


# Build the list of all fake reviews.
def make_reviews():
    reviews = []
    review_id = 1
    for week_number in range(4):
        for i in range(REVIEWS_PER_WEEK):
            kind = pick_kind(week_number)
            day = FIRST_DAY + timedelta(days=week_number * 7 + random.randint(0, 6))
            review = {
                "review_id": review_id,
                "date": day.isoformat(),
                "rating": random.choice(RATINGS[kind]),
                "text": random.choice(SENTENCES[kind]),
            }
            reviews.append(review)
            review_id = review_id + 1
    return reviews


# Write the reviews to a CSV file.
def save_reviews(reviews, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["review_id", "date", "rating", "text"])
        writer.writeheader()
        for review in reviews:
            writer.writerow(review)


reviews = make_reviews()
save_reviews(reviews, "reviews.csv")
print("Wrote", len(reviews), "reviews to reviews.csv")
