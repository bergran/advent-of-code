import pytest

from y2021.day_7.main import calculate_fuel_cost, puzzle_1, WrongFormat


@pytest.mark.parametrize(
    "position, input_, expected",
    [
        pytest.param(
            2,
            [16, 1, 2, 0, 4, 2, 7, 1, 2, 14],
            37,
            id="Calculate fuel cost of position 2 with the input",
        ),
        pytest.param(
            1,
            [5],
            4,
            id="Calculate fuel cost of position 1 with the input 5",
        ),
        pytest.param(
            0,
            [5, 10],
            15,
            id="Calculate fuel cost of position 0 with the input 5",
        ),
    ],
)
def test_calculate_fuel_cost(position, input_, expected):
    assert calculate_fuel_cost(position, input_) == expected


@pytest.mark.parametrize(
    "input_, expected",
    [
        pytest.param(
            "16,1,2,0,4,2,7,1,2,14",
            37,
            id="Calculate fuel cost of position 2 with the input",
        ),
        pytest.param(
            "5",
            0,
            id="Calculate fuel cost of position 1 with the input 5",
        ),
        pytest.param(
            "5,10",
            5,
            id="Calculate fuel cost of position 0 with the input 5",
        ),
    ],
)
def test_puzzle_1(input_, expected):
    assert puzzle_1(input_, calculate_fuel_cost) == expected


def test_puzzle_1_fail():
    with pytest.raises(WrongFormat):
        puzzle_1("123,b", calculate_fuel_cost)

    assert True