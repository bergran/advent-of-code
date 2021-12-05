import pytest

from y2021.day_4.main import (
    calculate_bingo_final_score,
    get_boards,
    get_winner_result,
)


@pytest.mark.parametrize(
    "input_, expected",
    [
        pytest.param(
            [
                "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
                "",
                "22 13 17 11  0",
                "8  2 23  4 24",
                "21  9 14 16  7",
                "6 10  3 18  5",
                "1 12 20 15 19",
                "",
                "3 15  0  2 22",
                "9 18 13 17  5",
                "19  8  7 25 23",
                "20 11 10 24  4",
                "14 21 16 12  6",
                "",
                "14 21 17 24  4",
                "10 16 15  9 19",
                "18  8 23 26 20",
                "22 11 13  6  5",
                "2  0 12  3  7",
            ],
            3,
            id="Expected 3 boards",
        ),
        pytest.param(
            [
                "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
                "",
            ],
            0,
            id="Expected 0 boards",
        ),
    ],
)
def test_get_boards(input_, expected):
    assert len(get_boards(input_)) == expected


def test_calculate_bingo_final_score_puzzle_explanation():
    input_ = [
        "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
        "",
        "22 13 17 11  0",
        "8  2 23  4 24",
        "21  9 14 16  7",
        "6 10  3 18  5",
        "1 12 20 15 19",
        "",
        "3 15  0  2 22",
        "9 18 13 17  5",
        "19  8  7 25 23",
        "20 11 10 24  4",
        "14 21 16 12  6",
        "",
        "14 21 17 24  4",
        "10 16 15  9 19",
        "18  8 23 26 20",
        "22 11 13  6  5",
        "2  0 12  3  7",
    ]

    assert calculate_bingo_final_score(input_).get("result") == 4512


def test_winner_result_no_winner():
    assert get_winner_result([], [1, 2, 3]) is None
