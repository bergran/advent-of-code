from typing import Tuple

import pytest

from y2021.day_9.main import puzzle_1, Point, calculate_top_bottom_left_right


@pytest.mark.parametrize(
    "input_, expected",
    [
        pytest.param(
            [
                "2199943210",
                "3987894921",
                "9856789892",
                "8767896789",
                "9899965678",
            ],
            15,
            id="Given this input get 26 recognized digits",
        ),
        pytest.param(
            [
                "99999999999",
                "99999999999",
                "99999999999",
            ],
            0,
            id="Given this input get 26 recognized digits",
        ),
        pytest.param(
            [
                "00000000000000",
                "00000000000000",
                "00000000000000",
                "00000000000000",
                "00000000000000",
            ],
            0,
            id="Given this input get 26 recognized digits",
        ),
        pytest.param(
            [
                "00000000000000",
                "00000010000000",
                "00000201000000",
                "00000020000006",
                "00000000000030",
            ],
            4,
            id="Given this input get 26 recognized digits",
        ),
        pytest.param(
            [
                "00000000000010",
                "00000000000001",
                "00000000000000",
                "00000000000001",
                "00000000000020",
            ],
            2,
            id="Given this input get 26 recognized digits",
        ),
        pytest.param(
            [
                "01000000000000",
                "40000000000000",
                "00000000000000",
                "20000000000000",
                "06000000000000",
            ],
            3,
            id="Given this input get 26 recognized digits",
        ),
    ],
)
def test_puzzle_1(input_, expected):
    assert puzzle_1(input_) == expected


_adjacent_0 = (1, 2, 3, 4)
_adjacent_1 = (4, 5, 6, 7)
_adjacent_2 = (4, None, None, 7)


@pytest.mark.parametrize(
    "point, adjacent, expected_is_lower_point, expected_adjacent_point",
    [
        pytest.param(
            Point(0, (0, 0), *_adjacent_0),
            _adjacent_0,
            True,
            min(_adjacent_0),
            id="Lower point and 1 as min adjacent point is 1",
        ),
        pytest.param(
            Point(6, (1, 1), *_adjacent_0),
            _adjacent_0,
            False,
            min(_adjacent_0),
            id="Not lower point and 1 as min adjacent point",
        ),
        pytest.param(
            Point(5, (1, 1), *_adjacent_1),
            _adjacent_1,
            False,
            min(_adjacent_1),
            id="Not lower point and 4 as min adjacent point",
        ),
        pytest.param(
            Point(3, (1, 1), *_adjacent_1),
            _adjacent_1,
            True,
            min(_adjacent_1),
            id="Lower point and 4 as min adjacent point",
        ),
    ],
)
def test_point_is_lower_and_adjacent(
    point: Point,
    adjacent: Tuple[int, int, int, int],
    expected_is_lower_point: bool,
    expected_adjacent_point: int,
):
    assert point.is_low_point(*adjacent) == expected_is_lower_point
    assert point.adjacent == expected_adjacent_point


_matrix = [
    [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
    [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
    [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
    [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
    [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
]


@pytest.mark.parametrize(
    "x, y, input_, expected",
    [
        pytest.param(
            0,
            0,
            _matrix,
            (None, 1, None, 3),
            id="x: 0, y: 0 expect Left: None, Right: 1, Top: None, Bottom: 3",
        ),
        pytest.param(
            0,
            4,
            _matrix,
            (None, 8, 8, None),
            id="x: 0, y: 0 expect Left: None, Right: 8, Top: 8, Bottom: None",
        ),
        pytest.param(
            9,
            0,
            _matrix,
            (1, None, None, 1),
            id="x: 0, y: 0 expect Left: 1, Right: None, Top: None, Bottom: 1",
        ),
        pytest.param(
            9,
            4,
            _matrix,
            (7, None, 9, None),
            id="x: 0, y: 0 expect Left: 7, Right: 9, Top: None, Bottom: None",
        ),
        pytest.param(
            1,
            1,
            _matrix,
            (3, 8, 1, 8),
            id="x: 0, y: 0 expect Left: 3, Right: 8, Top: 1, Bottom: 8",
        ),
    ],
)
def test_calculate_top_bottom_left_right(x, y, input_, expected):
    assert calculate_top_bottom_left_right(x, y, input_) == expected
