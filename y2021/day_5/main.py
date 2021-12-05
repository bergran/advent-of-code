import os
from typing import List

from src.utils import read_file_inputs
from y2021.day_5.model import Line
from y2021.day_5.utils.common import transform_input_to_lines, calculate_max_x_and_y, init_array, count_overlapping
from y2021.day_5.utils.fillers import fill_diagonal, fill_no_diagonal
from y2021.day_5.utils.matchings import get_matching_lines, get_matching_lines_diagonal

BASE_DIR_INPUTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs")


def calculate_lines_overlapping(lines: List[Line]):
    x, y = calculate_max_x_and_y(lines)
    board = init_array(x + 1, y + 1)

    for line in lines:
        from_x, from_y = line.from_
        to_x, to_y = line.to_

        fill_no_diagonal(board, from_x, from_y, to_x, to_y)

    return board


def calculate_lines_overlapping_diagonal(lines: List[Line]):
    x, y = calculate_max_x_and_y(lines)
    board = init_array(x + 1, y + 1)

    for line in lines:
        from_x, from_y = line.from_
        to_x, to_y = line.to_

        if line.is_diagonal():
            y_diff = to_y - from_y
            for to_add_y in range(min(0, y_diff), max(0, y_diff) + 1):
                fill_diagonal(board, from_x, from_y, to_x, to_add_y)

        else:
            fill_no_diagonal(board, from_x, from_y, to_x, to_y)

    return board


def puzzle_1(input_):
    lines = get_matching_lines(transform_input_to_lines(input_))
    board_result = calculate_lines_overlapping(lines)

    return count_overlapping(board_result)


def puzzle_2(input_):
    lines = get_matching_lines_diagonal(transform_input_to_lines(input_))
    board_result = calculate_lines_overlapping_diagonal(lines)

    return count_overlapping(board_result)


if __name__ == "__main__":  # pragma: no cover
    inputs_puzzle_1 = read_file_inputs(os.path.join(BASE_DIR_INPUTS, "input_1.txt"))
    inputs_puzzle_2 = read_file_inputs(os.path.join(BASE_DIR_INPUTS, "input_2.txt"))

    print("solution 1", puzzle_1(inputs_puzzle_1))
    print("solution 2", puzzle_2(inputs_puzzle_2))
