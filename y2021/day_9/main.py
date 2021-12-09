import os
from functools import reduce
from typing import List, Tuple

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
        center: int,
        coords: Tuple[int, int],
        left=None,
        right=None,
        top=None,
        bottom=None,
    ):
        self.center = center
        self.adjacent = self._get_adjacent(left, right, top, bottom)
        self.is_low_point()
        self.x = coords[0]
        self.y = coords[1]

    @staticmethod
    def _get_adjacent(bottom, left, right, top):
        return min([value for value in [left, right, top, bottom] if value is not None])

    def __repr__(self):
        return f"<Point: center: {self.center} adjacent: {self.adjacent} x: {self.x} y: {self.y}>"

    def is_low_point(self):
        return self.center < self.adjacent

    def get_basins(self, matrix: List[List[int]], num: int = None):
        num = self.center + 1 if num is None else num

        if num > 8:
            return set()

        basins = {(self.x, self.y)}
        for y in (-1, 0, 1):
            for x in (-1, 0, 1):
                new_x = self.x + x
                new_y = self.y + y
                if (
                    abs(x) != abs(y)
                    and 0 <= new_y < len(matrix)
                    and 0 <= new_x < len(matrix[new_y])
                    and matrix[new_y][new_x] == num
                ):
                    print("num", self.center, num, basins)
                    point = Point(
                        matrix[new_y][new_x],
                        (new_x, new_y),
                        matrix[new_y][new_x - 1] if new_x > 0 else None,
                        matrix[new_y][new_x + 1]
                        if new_x < len(matrix[new_y]) - 1
                        else None,
                        matrix[new_y - 1][new_x] if new_y > 0 else None,
                        matrix[new_y + 1][new_x] if new_y < len(matrix) - 1 else None,
                    )
                    basins |= point.get_basins(matrix, num + 1)

        return basins


def puzzle_1(input_: List[str]) -> int:
    signal_output_lines = transform_input_to_numbers(input_)
    points = get_low_points(signal_output_lines)

    return sum([point.center + 1 for point in points])


def calculate_top_bottom_left_right(
    x: int, y: int, signal_output_lines: List[List[int]]
):
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
    basins = sorted(get_low_points_basin(signal_output_lines))

    # print(basins)
    return reduce(lambda state, value: state * value, basins[-3:], 1)


def get_low_points(signal_output_lines):
    points = []
    for y, line in enumerate(signal_output_lines):
        for x, code in enumerate(line):
            left, right, top, bottom = calculate_top_bottom_left_right(
                x, y, signal_output_lines
            )

            current_point = Point(code, (x, y), left, right, top, bottom)

            if current_point.is_low_point():
                points.append(current_point)

    return points


def get_low_points_basin(signal_output_lines):
    basin_points = []
    for y, line in enumerate(signal_output_lines):
        for x, code in enumerate(line):
            left, right, top, bottom = calculate_top_bottom_left_right(
                x, y, signal_output_lines
            )

            current_point = Point(code, (x, y), left, right, top, bottom)

            if current_point.is_low_point():
                print(current_point.center, "*"*9)
                basins = current_point.get_basins(signal_output_lines)
                basin_points.append(len(basins))
                print("pepe", current_point.center, basins)
    return basin_points


if __name__ == "__main__":  # pragma: no cover
    inputs_puzzle_1 = read_file_inputs(os.path.join(BASE_DIR_INPUTS, "input_1.txt"))
    inputs_puzzle_2 = read_file_inputs(os.path.join(BASE_DIR_INPUTS, "input_2.txt"))
    print("solution 1", puzzle_1(inputs_puzzle_1))
    print("solution 2", puzzle_2(inputs_puzzle_2))
