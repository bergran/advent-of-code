from typing import List

import pytest

from y2021.day_9.main import puzzle_2, Point


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
            1134,
            id="example",
        ),
    ],
)
def test_puzzle_2(input_, expected):
    assert puzzle_2(input_) == expected


_matrix = [
    [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
    [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
    [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
    [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
    [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
]


@pytest.mark.parametrize(
    "matrix, point, expected",
    [
        pytest.param(
            _matrix,
            Point(1, (1, 0), 2, 9, None, 9),
            3,
            id="example",
        ),
        pytest.param(
            _matrix,
            Point(0, (9, 0), 1, None, None, 1),
            9,
            id="example 2",
        ),
        pytest.param(
            _matrix,
            Point(5, (2, 2), 8, 6, 8, 6),
            14,
            id="example 3",
        ),
        pytest.param(
            _matrix,
            Point(5, (6, 4), 6, 6, 6, None),
            9,
            id="example 4",
        ),
    ],
)
def test_get_basins(matrix: List[List[int]], point: Point, expected):
    assert len(point.get_basins(matrix)) == expected
