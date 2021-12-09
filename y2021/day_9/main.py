import os
from typing import List, Optional, Tuple

from src.utils import read_file_inputs

BASE_DIR_INPUTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs")


def transform_input_to_numbers(input_: List[str]):
    return [[int(code) for code in list(line)] for line in input_]


class Point:
    center: int
    adjacent: int
    x: int
    y: int

    def __init__(
        self,
        center,
        coords: Tuple[int, int],
        left=None,
        right=None,
        top=None,
        bottom=None,
    ):
        self.center = center
        self.adjacent = self._get_adjacent(left, right, top, bottom)
        self.is_low_point(left, right, top, bottom)
        self.x = coords[0]
        self.y = coords[1]

    @staticmethod
    def _get_adjacent(bottom, left, right, top):
        return min([value for value in [left, right, top, bottom] if value is not None])

    def __repr__(self):
        return f"<Point: center: {self.center} adjacent: {self.adjacent} x: {self.x} y: {self.y}>"

    def is_low_point(self, left, right, top, bottom):
        return self.center < self._get_adjacent(left, right, top, bottom)


def puzzle_1(input_: List[str]) -> int:
    signal_output_lines = transform_input_to_numbers(input_)
    points = []
    for y, line in enumerate(signal_output_lines):
        for x, code in enumerate(line):
            left, right, top, bottom = calculate_top_bottom_left_right(
                x, y, signal_output_lines
            )

            current_point = Point(code, (x, y), left, right, top, bottom)

            if current_point.is_low_point(left, right, top, bottom):
                points.append(current_point)

            print(f"is_lower: {current_point.is_low_point(left, right, top, bottom)} center: {current_point.center} top: {top} bottom: {bottom} left: {left} right: {right}")

    for point in points:
        print(point)

    return sum([point.adjacent for point in points])


def calculate_top_bottom_left_right(x: int, y: int, signal_output_lines: List[List[int]]):
    line = signal_output_lines[y]

    if y == 0:
        top = None
    else:
        top = signal_output_lines[y - 1][x]

    if y == len(signal_output_lines) - 1:
        bottom = None
    else:
        bottom = signal_output_lines[y + 1][x]

    if x == 0:
        left = None
    else:
        left = line[x - 1]

    if x == len(line) - 1:
        right = None
    else:
        right = line[x + 1]

    return left, right, top, bottom


def puzzle_2(input_: List[str]) -> int:
    signal_output_lines = transform_input_to_numbers(input_)

    return 0


if __name__ == "__main__":  # pragma: no cover
    inputs_puzzle_1 = read_file_inputs(os.path.join(BASE_DIR_INPUTS, "input_1.txt"))
    inputs_puzzle_2 = read_file_inputs(os.path.join(BASE_DIR_INPUTS, "input_2.txt"))
    print("solution 1", puzzle_1(inputs_puzzle_1))
    print("solution 2", puzzle_2(inputs_puzzle_2))
