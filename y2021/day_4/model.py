from itertools import chain
from typing import List, Optional


class Board:
    _horizontal_lines: List[List[int]]
    _vertical_lines: List[List[int]]
    _lines: List[List[str]]
    result_horizontal: List[List[int]]
    result_vertical: List[List[int]]
    numbers_selected: List[int]

    _selected_horizontal_numbers: Optional[List[int]] = None
    _no_selected_horizontal_numbers: Optional[List[int]] = None

    _selected_vertical_numbers: Optional[List[int]] = None
    _no_selected_vertical_numbers: Optional[List[int]] = None

    lines = None

    def __init__(self, pk: int, raw: List[List[str]], lines:int=5):
        self.pk = pk
        self._lines = raw
        self.initiate_horizontal_line(raw)
        self.initiate_vertical_line(raw)
        self.initiate_board_results()
        self.numbers_selected = []
        self.lines = lines

    def initiate_horizontal_line(self, raw):
        self._horizontal_lines = [[int(number) for number in line] for line in raw]

    def initiate_vertical_line(self, raw):
        lines = []

        for i in range(len(raw)):
            vertical_line = []
            for line in raw:
                vertical_line.append(int(line[i]))
            lines.append(vertical_line)

        self._vertical_lines = lines

    def initiate_board_results(self, lines=5):
        self.result_horizontal = [list() for _ in range(lines)]
        self.result_vertical = [list() for _ in range(lines)]

    def check_horizontal_line(self, number):
        for index, line in enumerate(self._horizontal_lines):
            if number in line:
                self.set_selected_numbers(number)
                self.result_horizontal[index].append(number)

        for line in self.result_horizontal:
            if len(line) == 5:
                return True

        return False

    def check_vertical_line(self, number):
        for index, line in enumerate(self._vertical_lines):
            if number in line:
                self.result_vertical[index].append(number)
                self.set_selected_numbers(number)

        for line in self.result_vertical:
            if len(line) == self.lines:
                return True

        return False

    def check_is_winner(self, number):
        is_winner_horizontal = self.check_horizontal_line(number)
        is_winner_vertical = self.check_vertical_line(number)

        return is_winner_horizontal or is_winner_vertical

    def set_selected_numbers(self, number):
        if number not in self.numbers_selected:
            self.numbers_selected.append(number)

    def get_selected_numbers(self) -> List[int]:
        return self.numbers_selected

    def get_un_selected_numbers(self) -> List[int]:
        return [
            int(number)
            for number in chain(*self._lines)
            if int(number) not in self.numbers_selected
        ]