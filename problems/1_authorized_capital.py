"""Plot companies by authorized capital."""

import csv
from pathlib import Path

from bar_plots import bar_plot


DATA_CSV = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "company_master_data_2026-09-12.csv"
)


def authorised_capital(data_csv):
    """Count companies by authorized capital range."""

    auth_capital = {
        "<= 1L": 0,
        "1L to 10L": 0,
        "10L to 1Cr": 0,
        "1Cr to 10Cr": 0,
        "> 10Cr": 0,
    }

    with open(data_csv, mode="r", encoding="utf-8", newline="") as file:
        data_reader = csv.DictReader(file)

        for row in data_reader:
            try:
                capital = float(row["Authorized Capital"])
            except (ValueError, TypeError):
                continue

            if capital <= 100000:
                auth_capital["<= 1L"] += 1
            elif capital <= 1000000:
                auth_capital["1L to 10L"] += 1
            elif capital <= 10000000:
                auth_capital["10L to 1Cr"] += 1
            elif capital <= 100000000:
                auth_capital["1Cr to 10Cr"] += 1
            else:
                auth_capital["> 10Cr"] += 1

    return auth_capital


auth_capital = authorised_capital(DATA_CSV)

print(auth_capital)

capital_range = auth_capital.keys()
capital = auth_capital.values()

bar_plot(
    x_bar=capital_range,
    y_bar=capital,
    x_label="Capital Range",
    y_label="Number of Companies",
    title="Bar Plot of Authorized Capital",
)