from pathlib import Path
from data_loader import load_revenue_records
from analytics import calculate_total_revenue
from analytics import calculate_average_revenue


def main() -> None:
    file_path = Path("data/revenue.csv")
    records = load_revenue_records(file_path)

    total_revenue = calculate_total_revenue(records)
    average_revenue = calculate_average_revenue(records)

    print(f"Number of records: {len(records)}")
    print(f"Total revenue: {total_revenue:.2f}")
    print(f"Average revenue: {average_revenue:.2f}")

if __name__ == "__main__":
    main()