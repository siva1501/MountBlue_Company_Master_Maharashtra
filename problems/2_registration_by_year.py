"""
Module to count the number of company registrations by year
and generate a bar plot for visualisation.
"""

import csv
from pathlib import Path

from bar_plots import bar_plot


DATA_CSV = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "company_master_data_2026-09-12.csv"
)

ZIP_CODE_MH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "zip_code_MH.csv"
)


def count_number_of_registrations(data_csv: str) -> dict:
    """
    Count the number of company registrations per year from a CSV file.

    Args:
        data_csv (str): Path to the CSV file containing company data.

    Returns:
        dict: Dictionary with years as keys and registration counts as values.
    """
    registrations_by_year = {}

    with open(
        data_csv,
        mode="r",
        encoding="utf-8",
        newline="",
    ) as fp:
        reader = csv.DictReader(fp)

        for row in reader:
            date = row["Company Registration Date"].strip()

            if not date:
                continue

            year = date[:4]

            registrations_by_year[year] = (
                registrations_by_year.get(year, 0) + 1
            )

    return registrations_by_year


if __name__ == "__main__":
    company_registrations_by_year = (
        count_number_of_registrations(DATA_CSV)
    )

    years = company_registrations_by_year.keys()
    number_of_registrations = company_registrations_by_year.values()

    bar_plot(
        x_bar=years,
        y_bar=number_of_registrations,
        x_label="Years",
        y_label="Number of Registrations",
        title="Bar Plot of Company Registration by Year",
    )