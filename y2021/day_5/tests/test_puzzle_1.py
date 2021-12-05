import pytest

from y2021.day_5.main import puzzle_1
from y2021.day_5.model import Line


@pytest.mark.parametrize(
    "input_, expected",
    [
        pytest.param(
            [
                "0,9 -> 5,9",
                "8,0 -> 0,8",
                "9,4 -> 3,4",
                "2,2 -> 2,1",
                "7,0 -> 7,4",
                "6,4 -> 2,0",
                "0,9 -> 2,9",
                "3,4 -> 1,4",
                "0,0 -> 8,8",
                "5,5 -> 8,2",
            ],
            5,
            id="Expected 5 overlapping",
        ),
        pytest.param(
            [
                "0,4 -> 4,4",
                "1,4 -> 3,4",
                "3,3 -> 5,4",
            ],
            3,
            id="Expected 3 overlapping",
        ),
    ],
)
def test_puzzle_1(input_, expected):
    assert puzzle_1(input_) == expected


@pytest.mark.parametrize("line, expected", [
    pytest.param(Line((5, 3), (5, 4)), True, id="match X"),
    pytest.param(Line((1, 4), (3, 4)), True, id="match Y"),
    pytest.param(Line((1, 5), (3, 4)), False, id="no match"),
    pytest.param(Line((5, 5), (5, 5)), True, id="match X and Y"),
])
def test_line_match(line, expected):
    assert line.is_match() is expected
