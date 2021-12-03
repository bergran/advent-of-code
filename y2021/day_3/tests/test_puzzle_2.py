import pytest

from y2021.day_3.main import (
    calculate_life_support_rating,
    calculate_oxygen_generator_rating, calculate_co2_scrubber_rating,
)


@pytest.mark.parametrize(
    "input_, expected",
    [
        pytest.param(["00100", "11011"], "11011", id="Test case draw bit"),
        pytest.param(
            [
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
            ],
            "10111", id="Test case puzzle 2"
        ),
    ],
)
def test_calculate_oxygen_generator_rating_result(input_, expected):
    assert calculate_oxygen_generator_rating(input_) == expected


@pytest.mark.parametrize(
    "input_, expected",
    [
        pytest.param(["00100", "11011"], "00100", id="Test case draw bit"),
        pytest.param(
            [
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
            ],
            "01010", id="Test case puzzle 2"
        ),
    ],
)
def test_calculate_co2_scrubber_rating_result(input_, expected):
    assert calculate_co2_scrubber_rating(input_) == expected


def test_depth_measure_with_duplicates():
    input_ = [
        "00100",
        "11011",
    ]

    assert calculate_life_support_rating(input_) == 108
