from pathlib import Path
from data_loader import load_revenue_records
from analytics import calculate_average


def main() -> None:
    file_path = Path("data/revenue.csv")
    records = load_revenue_records(file_path)

    revenue_values = [record.revenue for record in records]

    total_revenue = sum(revenue_values)
    average_revenue = calculate_average(revenue_values)

    print(f"Number of records: {len(revenue_values)}")
    print(f"Total revenue: {total_revenue:.2f}")
    print(f"Average revenue: {average_revenue:.2f}")

if __name__ == "__main__":
    main()