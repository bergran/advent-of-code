import os
from typing import List

from src.utils import read_file_inputs

BASE_DIR_INPUTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs")


class InputNotArray(Exception):
    pass


class NotEnoughValues(Exception):
    pass


def depth_measure(input_: List[int]):
    count = 0
    prev = input_[0]

    if not isinstance(input_, list):
        raise InputNotArray()

    if len(input_) < 2:
        raise NotEnoughValues()

    for i in input_:
        if i > prev:
            count += 1
        prev = i

    return count


def get_num_sum(start: int, input_: List[int], window: int):
    return sum(input_[i] for i in range(start + window))


def depth_measure_with_window(input_: List[int], window: int = 3):
    if not isinstance(input_, list):
        raise InputNotArray()

    if len(input_) < window:
        raise NotEnoughValues()

    count = 0
    prev = get_num_sum(0, input_, window)

    for i, _ in enumerate(input_):
        try:
            sum_numbers = get_num_sum(i, input_, window)
        except IndexError:
            break
        if sum_numbers > prev:
            count += 1
        prev = sum_numbers
    return count


if __name__ == "__main__":  # pragma: no cover
    inputs_puzzle_1 = [
        int(i) for i in read_file_inputs(os.path.join(BASE_DIR_INPUTS, "input.txt"))
    ]
    inputs_puzzle_2 = inputs_puzzle_1

    print("solution 1", depth_measure(inputs_puzzle_1))
    print("solution 2", depth_measure_with_window(inputs_puzzle_2))
