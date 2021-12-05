from typing import List

from y2021.day_5.model import Line


def get_matching_lines(lines: List[Line]):
    return [
        line
        for line in lines if line.is_match()
    ]


def get_matching_lines_diagonal(lines: List[Line]):
    return [
        line
        for line in lines if line.is_match_diagonal()
    ]