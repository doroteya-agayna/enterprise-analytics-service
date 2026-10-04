from datetime import date
from pathlib import Path
from data_loader import load_revenue_records

def test_load_revenue_records() -> None:
    file_path = Path("data/revenue.csv")

    records = load_revenue_records(file_path)

    assert len(records) == 5
    assert records[0].record_date == date(2026, 9, 1)
    assert records[0].customer == "customer A"
    assert records[0].revenue == 1200.50