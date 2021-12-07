import pytest

from y2021.day_7.main import calculate_fuel_cost_2


@pytest.mark.parametrize(
    "position, input_, expected",
    [
        pytest.param(
            5,
            [16, 1, 2, 0, 4, 2, 7, 1, 2, 14],
            168,
            id="Calculate fuel cost of position 5 with the input",
        ),
        pytest.param(
            1,
            [5],
            10,
            id="Calculate fuel cost of position 1 with the input 5",
        ),
        pytest.param(
            0,
            [5, 10],
            70,
            id="Calculate fuel cost of position 0 with the input 5",
        ),
    ],
)
def test_calculate_fuel_cost(position, input_, expected):
    assert calculate_fuel_cost_2(position, input_) == expected
