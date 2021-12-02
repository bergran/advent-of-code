import re
from typing import Dict, Tuple

from y2021.day_2.exceptions import WrongCommand

pattern = re.compile(r"(forward|down|up)\s([0-9])")


def sum_numbers(x: int, y: int) -> int:
    return x + y


def diff_numbers(x: int, y: int) -> int:
    return x - y


OPERATION_CHOICES = {"increase": sum_numbers, "decrease": diff_numbers}


def get_move_type_and_speed(command: str) -> Tuple[str, int]:
    pattern_result = pattern.fullmatch(command)
    if not pattern_result:
        raise WrongCommand(f"Cannot match {command}")
    move_type = pattern_result.group(1)
    speed = pattern_result.group(2)
    return move_type, int(speed)


def calculate_forward(position: Dict[str, int], operation: str, speed: int) -> None:
    position["horizontal"] = sum_numbers(position["horizontal"], speed)
    position["depth"] = sum_numbers(position["depth"], position["aim"] * speed)


def calculate_aim(position: Dict[str, Tuple[str, str]], operation: str, speed: int) -> None:
    position["aim"] = OPERATION_CHOICES[operation](position["aim"], speed)
