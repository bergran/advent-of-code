import pytest

from y2021.day_5.main import puzzle_1, puzzle_2
from y2021.day_5.model import Line


@pytest.mark.parametrize(
    "input_, expected",
    [
        pytest.param(
            [
                "0,4 -> 4,4",
                "1,4 -> 3,4",
                "3,3 -> 5,4",
                "3,3 -> 4,4",
                "5,5 -> 4,4",
                "3,5 -> 4,4",
                "5,3 -> 4,4",
            ],
            4,
            id="Expected 3 overlapping",
        ),
    ],
)
def test_puzzle_1(input_, expected):
    assert puzzle_2(input_) == expected


@pytest.mark.parametrize("line, expected", [
    pytest.param(Line((5, 3), (5, 4)), True, id="match X"),
    pytest.param(Line((1, 4), (3, 4)), True, id="match Y"),
    pytest.param(Line((1, 5), (2, 7)), False, id="no match"),
    pytest.param(Line((5, 5), (5, 5)), True, id="match X and Y"),
    pytest.param(Line((1, 1), (3, 3)), True, id="match diagonal 1 plus plus"),
    pytest.param(Line((9, 7), (7, 9)), True, id="match diagonal 2 minus plus"),
    pytest.param(Line((4, 4), (5, 3)), True, id="match diagonal 3 plus minus"),
    pytest.param(Line((4, 6), (3, 5)), True, id="match diagonal 4 minus minus"),
    pytest.param(Line((3, 3), (5, 4)), False, id="No match"),
])
def test_line_match_diagonal_(line, expected):
    assert line.is_match_diagonal() is expected
