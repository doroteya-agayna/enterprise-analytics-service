import csv
from datetime import date
from pathlib import Path
from models import RevenueRecord

def load_revenue_records(file_path: Path) -> list[RevenueRecord]:
    revenue_values: list[RevenueRecord] = []

    with file_path.open(mode = "r", encoding = "utf-8", newline = "") as file:
        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start = 2):
            revenue_text = row["revenue"]

            if revenue_text is None:
                raise ValueError(
                    f"Missing revenue value on CSV row {row_number}"
                )

            try:
                revenue = float(revenue_text)
            except ValueError as error: 
                raise ValueError(
                f"Invalid revenue value '{revenue_text}' "
                f"on CSV ROW {row_number}"
            ) from error

            record = RevenueRecord(
                record_date = date.fromisoformat(row["date"]),
                customer = row["customer"],
                revenue = revenue
            )
                
            revenue_values.append(record)

    return revenue_values