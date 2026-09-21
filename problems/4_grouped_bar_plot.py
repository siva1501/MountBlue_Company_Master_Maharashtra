"""Grouped bar plot of company registrations."""

import csv
from collections import Counter, defaultdict
from datetime import datetime
from bar_plots import grouped_bar_plot

COMPANY_FILE = "data/company_master_data_2026-09-12.csv"


def load_data():
    """Load company registration data."""
    registrations = []

    with open(
        COMPANY_FILE,
        "r",
        encoding="utf-8",
        newline="",
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            date = row["Company Registration Date"].strip()
            activity = row["Company Industrial Classification"].strip()

            if not date or not activity:
                continue

            try:
                year = datetime.strptime(
                    date,
                    "%Y-%m-%d",
                ).year
            except ValueError:
                continue

            registrations.append((year, activity))

    return registrations


def find_top_activities(registrations, years):
    """Find the top five business activities."""
    activity_count = Counter()

    for year, activity in registrations:
        if year in years:
            activity_count[activity] += 1

    return [activity for activity, _ in activity_count.most_common(5)]


def count_registrations(
    registrations,
    years,
    activities,
):
    """Count registrations by year and activity."""
    counts = defaultdict(lambda: defaultdict(int))

    for year, activity in registrations:
        if year in years and activity in activities:
            counts[year][activity] += 1

    return counts


def execute():
    """Run the grouped bar plot program."""
    registrations = load_data()

    all_years = sorted({year for year, _ in registrations})

    years = all_years[-10:]

    activities = find_top_activities(
        registrations,
        years,
    )

    counts = count_registrations(
        registrations,
        years,
        activities,
    )

    print("\nTop 5 Business Activities - Last 10 Years\n")

    for year in years:
        print(f"\n{year}")

        for activity in activities:
            print(f"{activity}: {counts[year][activity]}")

    grouped_bar_plot(
        counts=counts,
        years=years,
        categories=activities,
        x_label="Year",
        y_label="Number of Registrations",
        title="Top 5 Business Activities - Last 10 Years",
    )


if __name__ == "__main__":
    execute()
