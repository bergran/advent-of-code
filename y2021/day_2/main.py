import os
from typing import List

from src.utils import read_file_inputs
from y2021.day_2.utils import get_move_type_and_speed, calculate_aim, calculate_forward, OPERATION_CHOICES

BASE_DIR_INPUTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs")


MOVE_RESULT_PUZZLE_1 = {
    "up": ("depth", "decrease"),
    "down": ("depth", "increase"),
    "forward": ("horizontal", "increase"),
}


MOVE_RESULT_PUZZLE_2 = {
    "up": ("aim", "decrease"),
    "down": ("aim", "increase"),
    "forward": ("horizontal", "increase"),
}


def pilot_submarine(input_: List[str]):
    position = {"horizontal": 0, "depth": 0, "none": 0}

    for command in input_:
        move_type, speed = get_move_type_and_speed(command)

        move_type_result, operation = MOVE_RESULT_PUZZLE_1.get(move_type)

        position[move_type_result] = OPERATION_CHOICES[operation](
            position.get(move_type_result, 0), int(speed)
        )
    return position["depth"] * position["horizontal"]


def pilot_submarine_with_aim(input_):
    position = {"horizontal": 0, "depth": 0, "aim": 0, "none": 0}
    move_choices = {"aim": calculate_aim, "horizontal": calculate_forward}

    for command in input_:
        move_type, speed = get_move_type_and_speed(command)
        move_type_result, operation = MOVE_RESULT_PUZZLE_2.get(move_type)

        move_choices[move_type_result](position, operation, int(speed))
    return position["depth"] * position["horizontal"]


if __name__ == "__main__":  # pragma: no cover
    inputs_puzzle_1 = read_file_inputs(os.path.join(BASE_DIR_INPUTS, "input_1.txt"))
    inputs_puzzle_2 = read_file_inputs(os.path.join(BASE_DIR_INPUTS, "input_2.txt"))

    print("solution 1", pilot_submarine(inputs_puzzle_1))
    print("solution 2", pilot_submarine_with_aim(inputs_puzzle_2))
