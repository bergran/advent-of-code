import os
import re
from typing import List, Callable

from src.utils import read_file_inputs

BASE_DIR_INPUTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs")
pattern = re.compile(f"([0-9]+,?)+")


class WrongFormat(Exception):
    pass


def transform_input_to_numbers(input_: str):
    if pattern.fullmatch(input_):
        return [int(number) for number in input_.split(",") if number]

    raise WrongFormat()


def puzzle_1(input_: str, calculate_cost: Callable[[int, List[int]], int]) -> int:
    horizontal_positions = transform_input_to_numbers(input_)

    max_position = max(horizontal_positions)
    min_position = min(horizontal_positions)

    last_min_fuel_cost = calculate_cost(min_position, horizontal_positions)

    for position in range(min_position + 1, max_position):
        fuel_cost = calculate_cost(position, horizontal_positions)

        if fuel_cost < last_min_fuel_cost:
            last_min_fuel_cost = fuel_cost

    return last_min_fuel_cost


def calculate_fuel_cost(position, horizontal_positions):
    fuel_cost = 0
    for move in horizontal_positions:
        fuel_cost = fuel_cost + abs(move - position)
    return fuel_cost


def calculate_fuel_cost_2(position, horizontal_positions):
    fuel_cost = 0
    for move in horizontal_positions:
        move_result = abs(move - position)
        fuel_cost = fuel_cost + (move_result * (move_result + 1) // 2)
    return fuel_cost


if __name__ == "__main__":  # pragma: no cover
    inputs_puzzle_1 = read_file_inputs(os.path.join(BASE_DIR_INPUTS, "input_1.txt"))
    inputs_puzzle_2 = read_file_inputs(os.path.join(BASE_DIR_INPUTS, "input_2.txt"))
    print("solution 1", puzzle_1(inputs_puzzle_1[0], calculate_fuel_cost))
    print("solution 2", puzzle_1(inputs_puzzle_2[0], calculate_fuel_cost_2))
