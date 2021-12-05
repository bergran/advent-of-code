from typing import List

import pytest

from y2021.day_4.model import Board


@pytest.mark.parametrize(
    "raw, numbers_checked, expected",
    [
        pytest.param(
            [
                ["22", "13", "17", "11", "0"],
                ["8", "2", "23", "4", "24"],
                ["21", "9", "14", "16", "7"],
                ["6", "10", "3", "18", "5"],
                ["1", "12", "20", "15", "19"],
            ],
            [8, 2, 23, 4, 24],
            True,
        ),
        pytest.param(
            [
                ["22", "13", "17", "11", "0"],
                ["8", "2", "23", "4", "24"],
                ["21", "9", "14", "16", "7"],
                ["6", "10", "3", "18", "5"],
                ["1", "12", "20", "15", "19"],
            ],
            [13, 2, 9, 10, 12],
            True,
        ),
        pytest.param(
            [
                ["22", "13", "17", "11", "0"],
                ["8", "2", "23", "4", "24"],
                ["21", "9", "14", "16", "7"],
                ["6", "10", "3", "18", "5"],
                ["1", "12", "20", "15", "19"],
            ],
            [8, 2, 23, 4, 25],
            False,
        ),
    ],
)
def test_board_check_winner(
    raw: List[List[str]], numbers_checked: List[int], expected: bool
):
    board = Board(1, raw)

    for number in numbers_checked[:-1]:
        board.check_is_winner(number)

    assert board.check_is_winner(numbers_checked[-1]) == expected


@pytest.mark.parametrize(
    "raw, numbers_checked, expected",
    [
        pytest.param(
            [
                ["22", "13", "17", "11", "0"],
                ["8", "2", "23", "4", "24"],
                ["21", "9", "14", "16", "7"],
                ["6", "10", "3", "18", "5"],
                ["1", "12", "20", "15", "19"],
            ],
            [8, 2, 23, 4, 24],
            [8, 2, 23, 4, 24],
        ),
        pytest.param(
            [
                ["22", "13", "17", "11", "0"],
                ["8", "2", "23", "4", "24"],
                ["21", "9", "14", "16", "7"],
                ["6", "10", "3", "18", "5"],
                ["1", "12", "20", "15", "19"],
            ],
            [13, 2, 9, 10, 12],
            [13, 2, 9, 10, 12],
        ),
        pytest.param(
            [
                ["22", "13", "17", "11", "0"],
                ["8", "2", "23", "4", "24"],
                ["21", "9", "14", "16", "7"],
                ["6", "10", "3", "18", "5"],
                ["1", "12", "20", "15", "19"],
            ],
            [8, 2, 23, 4, 25],
            [8, 2, 23, 4],
        ),
    ],
)
def test_board_selected_numbers(
    raw: List[List[str]], numbers_checked: List[int], expected: bool
):
    board = Board(1, raw)

    for number in numbers_checked:
        board.check_is_winner(number)

    assert board.get_selected_numbers() == expected


@pytest.mark.parametrize(
    "raw, numbers_checked, expected",
    [
        pytest.param(
            [
                ["22", "13", "17", "11", "0"],
                ["8", "2", "23", "4", "24"],
                ["21", "9", "14", "16", "7"],
                ["6", "10", "3", "18", "5"],
                ["1", "12", "20", "15", "19"],
            ],
            [8, 2, 23, 4, 24],
            [22, 13, 17, 11, 0, 21, 9, 14, 16, 7, 6, 10, 3, 18, 5, 1, 12, 20, 15, 19],
            id="select winner numbers"
        ),
        pytest.param(
            [
                ["22", "13", "17", "11", "0"],
                ["8", "2", "23", "4", "24"],
                ["21", "9", "14", "16", "7"],
                ["6", "10", "3", "18", "5"],
                ["1", "12", "20", "15", "19"],
            ],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
            [],
            id="select all numbers"
        ),
    ],
)
def test_board_no_selected_numbers(
    raw: List[List[str]], numbers_checked: List[int], expected: bool
):
    board = Board(1, raw)
    for number in numbers_checked:
        board.check_is_winner(number)

    assert board.get_un_selected_numbers() == expected
