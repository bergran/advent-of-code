import os
from typing import List

from src.utils import read_file_inputs
from y2021.day_4.model import Board

BASE_DIR_INPUTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs")


def get_random_bingo_numbers(input_) -> List[int]:
    return [int(number) for number in input_[0].split(",")]


def get_boards(input_: List[str]) -> List[Board]:
    boards = []
    board = []
    count_boards = 0
    for line in input_[2:]:

        if line != "":
            board.append(line.lstrip().replace("  ", " ").split(" "))

        if len(board) == 5:
            boards.append(Board(count_boards, board))
            count_boards += 1
            board = []

    return boards


def calculate_bingo_final_score(input_: List[str]):
    random_bingo_numbers = get_random_bingo_numbers(input_)
    boards = get_boards(input_)
    return get_winner_result(boards, random_bingo_numbers)


def get_winner_result(boards: List[Board], random_bingo_numbers: List[int]):
    board_winner = None
    last_number = None
    numbers_checked = []
    for number in random_bingo_numbers:
        numbers_checked.append(number)

        for board in boards:
            is_winner = board.check_is_winner(number)

            if is_winner:
                board_winner = board
                break

        if board_winner:
            last_number = number
            break

    if board_winner is None:
        # No winner
        return None

    return {
        "result": sum(board_winner.get_un_selected_numbers()) * int(last_number),
        "board": board_winner,
    }


def calculate_bingo_final_score_last_board_to_win(input_: List[str]):
    random_bingo_numbers = get_random_bingo_numbers(input_)
    boards = get_boards(input_)
    can_continue = True
    last_winner = None
    while can_continue:
        winner = get_winner_result(boards, random_bingo_numbers)

        if len(boards) >= 0 and winner is not None:
            boards = [Board(board.pk, board._lines) for board in boards if board.pk != winner.get("board").pk]
            last_winner = winner

        can_continue = len(boards) > 0

    return last_winner


if __name__ == "__main__":  # pragma: no cover
    inputs_puzzle_1 = read_file_inputs(os.path.join(BASE_DIR_INPUTS, "input_1.txt"))
    inputs_puzzle_2 = read_file_inputs(os.path.join(BASE_DIR_INPUTS, "input_2.txt"))

    print("solution 1", calculate_bingo_final_score(inputs_puzzle_1))
    print("solution 2", calculate_bingo_final_score_last_board_to_win(inputs_puzzle_2))
