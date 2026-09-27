def calculate_average(values: list[float]) -> float:
    if not values:
        return 0.0

    return sum(values) / len(values)

def main() -> None:
    revenue_values = [
        1200.50,
        980.00,
        1430.75,
        1100.25,
        750.25
    ]

    total_revenue = sum(revenue_values)
    average_revenue = calculate_average(revenue_values)

    print(f"Number of records: {len(revenue_values)}")
    print(f"Total revenue: {total_revenue:.2f}")
    print(f"Average revenue: {average_revenue:.2f}")

if __name__ == "__main__":
    main()