from pathlib import Path

from data_loader import load_revenue_values

def calculate_average(values: list[float]) -> float:
    if not values:
        return 0.0

    return sum(values) / len(values)

def main() -> None:
    file_path = Path("data/revenue.csv")
    revenue_values = load_revenue_values(file_path)

    total_revenue = sum(revenue_values)
    average_revenue = calculate_average(revenue_values)

    print(f"Number of records: {len(revenue_values)}")
    print(f"Total revenue: {total_revenue:.2f}")
    print(f"Average revenue: {average_revenue:.2f}")

if __name__ == "__main__":
    main()