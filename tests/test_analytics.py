from analytics import calculate_average

def test_calculate_average() -> None:
    values = [10.0, 20.0, 30.0]

    result = calculate_average(values)

    assert result == 20.0

def test_calculate_average_empty_list() -> None:
    values: list[float] = []

    result = calculate_average(values)

    assert result == 0.0