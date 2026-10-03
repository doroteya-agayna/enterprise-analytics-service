import csv
from pathlib import Path

def load_revenue_values(file_path: Path) -> list[float]:
    revenue_values: list[float] = []

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
                
            revenue_values.append(revenue)

    return revenue_values