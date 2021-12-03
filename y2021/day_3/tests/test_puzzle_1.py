import pytest

from y2021.day_3.main import calculate_power_consumption, WrongLengthCodeError


def test_calculate_power_consumption_puzzle_explanation():
    input_ = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]

    assert calculate_power_consumption(input_) == 198


def test_calculate_power_consumption_puzzle_explanation_failed_length_validation():
    input_ = [
        "00100",
        "11110",
        "101101",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]

    with pytest.raises(WrongLengthCodeError):
        calculate_power_consumption(input_)

    assert True
