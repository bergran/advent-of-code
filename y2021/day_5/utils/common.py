import re
from itertools import chain
from typing import List, Tuple

from y2021.day_5.model import Line


pattern = re.compile("([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)")


def transform_input_to_lines(input_: List[str]) -> List[Line]:
    coordinates = []
    for line in input_:
        result = pattern.fullmatch(line)

        if result:
            coordinate_from = (int(result.group(1)), int(result.group(2)))
            coordinate_to = (int(result.group(3)), int(result.group(4)))
            coordinates.append(Line(coordinate_from, coordinate_to))

    return coordinates


def calculate_max_x_and_y(lines: List[Line]) -> Tuple[int, int]:
    max_x = 0
    max_y = 0

    for line in lines:
        max_x = max(max_x, line.from_[0], line.to_[0])
        max_y = max(max_y, line.from_[1], line.to_[1])

    return max_x, max_y


def init_array(x, y):
    return [[0 for _ in range(x)] for __ in range(y)]


def count_overlapping(board_result):
    count = 0
    for i in chain(*board_result):
        if i > 1:
            count += 1
    return count