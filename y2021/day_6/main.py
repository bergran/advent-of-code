import os
import re
from typing import List

from src.utils import read_file_inputs
from y2021.day_6.exceptions import WrongFormatLanternFish
from y2021.day_6.model import LanternFish

BASE_DIR_INPUTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs")
pattern = re.compile(f"([0-9]+,?)+")


def transform_line_to_lantern_fish(input_: str) -> List[LanternFish]:
    result = pattern.fullmatch(input_)

    if result:
        return [
            LanternFish(int(lantern_fish_days))
            for lantern_fish_days in input_.split(",")
        ]
    raise WrongFormatLanternFish()


def transform_line_to_list_int(input_: str) -> List[int]:
    result = pattern.fullmatch(input_)

    if result:
        return [
            int(lantern_fish_days)
            for lantern_fish_days in input_.split(",")
        ]
    raise WrongFormatLanternFish()


def calculate_new_lantern_fish(lantern_fish: List[LanternFish], to_days: int) -> List[LanternFish]:
    for day in range(to_days):
        new_lantern_fish = []
        for lf in lantern_fish:
            lf.new_day()
            new_lantern_fish += [
                LanternFish(8) for _ in range(lf.get_new_lantern_fish())
            ]

        lantern_fish = lantern_fish + new_lantern_fish
    return lantern_fish


def calculate_new_lantern_fish_optimized(
    lantern_fish: List[int], to_days: int
) -> int:
    lantern_fish_dict = {}
    for lantern_fish in lantern_fish:
        lantern_fish_dict[lantern_fish] = (
            lantern_fish_dict.get(lantern_fish, 0) + 1
        )

    for day in range(to_days):
        new_fish = lantern_fish_dict.get(0, 0)
        for key in range(1, 9):
            lantern_fish_dict[key - 1] = lantern_fish_dict.get(key, 0)

        lantern_fish_dict[6] = lantern_fish_dict.get(6, 0) + new_fish
        lantern_fish_dict[8] = new_fish

    return sum([value for value in lantern_fish_dict.values()])


def puzzle_1(input_: str, to_days: int) -> int:
    lantern_fish = transform_line_to_lantern_fish(input_)
    return len(calculate_new_lantern_fish(lantern_fish, to_days))


def puzzle_2(input_: str, to_days: int) -> int:
    return calculate_new_lantern_fish_optimized(
        transform_line_to_list_int(input_), to_days
    )


if __name__ == "__main__":  # pragma: no cover
    inputs_puzzle_1 = read_file_inputs(os.path.join(BASE_DIR_INPUTS, "input_1.txt"))
    inputs_puzzle_2 = read_file_inputs(os.path.join(BASE_DIR_INPUTS, "input_2.txt"))
    print("solution 1", puzzle_1(inputs_puzzle_1[0], 80))
    print("solution 2", puzzle_2(inputs_puzzle_2[0], 256))
