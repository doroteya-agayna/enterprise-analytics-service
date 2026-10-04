from datetime import date
from models import RevenueRecord

from analytics import calculate_average_revenue, calculate_total_revenue

def test_calculate_average_revenue() -> None:
    records = [
        RevenueRecord(
            record_date = date(2026, 9, 1),
            customer = "customer A",
            revenue = 100.0
        ),
        RevenueRecord(
            record_date = date(2026, 9, 2),
            customer = "customer B",
            revenue = 200.0
        ),
        RevenueRecord(
            record_date = date(2026, 9, 3),
            customer = "customer C",
            revenue = 300.0
        )
    ]

    result = calculate_average_revenue(records)

    assert result == 200.0

def test_calculate_average_revenue_with_empty_list() -> None:
    records: list[RevenueRecord] = []

    result = calculate_average_revenue(records)

    assert result == 0.0

def test_calculate_total_revenue() -> None:
    records = [
        RevenueRecord(
            record_date = date(2026, 9, 1),
            customer = "customer A",
            revenue = 100.0
        ),
        RevenueRecord(
            record_date = date(2026, 9, 2),
            customer = "customer B",
            revenue = 200.0
        ),
        RevenueRecord(
            record_date = date(2026, 9, 3),
            customer = "customer C",
            revenue = 300.0
        )
    ]

    result = calculate_total_revenue(records)

    assert result == 600.0