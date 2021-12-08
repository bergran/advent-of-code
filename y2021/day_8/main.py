import os
from typing import List

from src.utils import read_file_inputs

BASE_DIR_INPUTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs")

KNOW_DIGITS = {7: '8', 3: '7', 4: '4', 2: '1'}


class WrongFormat(Exception):
    pass


def transform_input_to_numbers(input_: List[str]):
    return [
        (line.split(" | ")[0].split(" "), line.split(" | ")[1].split(" "))
        for line in input_
    ]


def puzzle_1(input_: List[str]) -> int:
    signal_output_lines = transform_input_to_numbers(input_)

    return len(
        [
            output
            for signal, output in signal_output_lines
            for digit in output
            if len(digit) in KNOW_DIGITS
        ]
    )


def puzzle_2(input_: List[str]) -> int:
    signal_output_lines = transform_input_to_numbers(input_)
    add = 0
    for signal, output in signal_output_lines:
        pattern = get_pattern(signal)
        print(pattern)

        final_code = ""
        for digit in output:
            final_code += KNOW_DIGITS.get(len(digit)) or pattern.get(sorted_s(digit))

        add += int(final_code)

    return add


def sorted_s(digit):
    return "".join(sorted(digit))


def get_pattern(signal):
    one = [d for d in signal if len(d) == 2].pop()
    four = [d for d in signal if len(d) == 4].pop()
    seven = [d for d in signal if len(d) == 3].pop()
    eight = [d for d in signal if len(d) == 7].pop()
    b_d = list(set(four) - set(seven))

    zero_six_nine = set(d for d in signal if len(d) == 6)
    six = [digit for digit in zero_six_nine if one[0] not in digit or one[1] not in digit].pop()
    zero = [digit for digit in zero_six_nine if b_d[0] not in digit or b_d[1] not in digit].pop()
    nine = [digit for digit in zero_six_nine if digit not in [zero, six]].pop()

    two_three_five = [digit for digit in signal if len(digit) == 5]
    five = [digit for digit in two_three_five if b_d[0] in digit and b_d[1] in digit].pop()
    three = [digit for digit in two_three_five if one[0] in digit and one[1] in digit].pop()
    two = [digit for digit in two_three_five if digit not in [three, five]].pop()

    return {
        sorted_s(zero): '0',
        sorted_s(one): '1',
        sorted_s(two): '2',
        sorted_s(three): '3',
        sorted_s(four): '4',
        sorted_s(five): '5',
        sorted_s(six): '6',
        sorted_s(seven): '7',
        sorted_s(eight): '8',
        sorted_s(nine): '9'
    }


if __name__ == "__main__":  # pragma: no cover
    inputs_puzzle_1 = read_file_inputs(os.path.join(BASE_DIR_INPUTS, "input_1.txt"))
    inputs_puzzle_2 = read_file_inputs(os.path.join(BASE_DIR_INPUTS, "input_2.txt"))
    print("solution 1", puzzle_1(inputs_puzzle_1))
    print("solution 2", puzzle_2(inputs_puzzle_2))
