from models import RevenueRecord

def calculate_total_revenue(records: list[RevenueRecord]) -> float:
    return sum(record.revenue for record in records)

def calculate_average_revenue(records: list[RevenueRecord]) -> float:
    if not records:
        return 0.0

    total_revenue = calculate_total_revenue(records)

    return total_revenue / len(records)

def calculate_revenue_for_customer(
        records: list[RevenueRecord],
        customer: str,
) -> float:
    return sum(
        record.revenue
        for record in records
        if record.customer == customer
    )