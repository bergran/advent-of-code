import os
from typing import List

from src.utils import read_file_inputs
from y2021.day_3.exceptions import WrongLengthCodeError

BASE_DIR_INPUTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs")


def _get_length(input_):
    length = {}

    for code in input_:
        key = f"{len(code)}"
        length[key] = length.get(key, 0) + 1

    if len(length.keys()) != 1:
        raise WrongLengthCodeError()

    return int(list(length.keys())[0])


def calculate_power_consumption(input_: List[str]):
    gamma_rate = ""
    epsilon_rate = ""

    length = _get_length(input_)

    for index in range(length):
        count_bit_rate = {
            "1": 0,
            "0": 0
        }

        for code in input_:
            bit = code[index]
            count_bit_rate[bit] = count_bit_rate.get(bit, 0) + 1

        if count_bit_rate["1"] > count_bit_rate["0"]:
            gamma_rate += "1"
            epsilon_rate += "0"
        elif count_bit_rate["0"] > count_bit_rate["1"]:
            gamma_rate += "0"
            epsilon_rate += "1"

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def calculate_most_common_bit(input_: List[str], index):
    count_bit_rate = {
        "1": 0,
        "0": 0
    }

    for code in input_:
        bit = code[index]
        count_bit_rate[bit] = count_bit_rate.get(bit, 0) + 1

    if count_bit_rate["1"] > count_bit_rate["0"]:
        return "1"
    elif count_bit_rate["0"] > count_bit_rate["1"]:
        return "0"
    return None


def calculate_less_common_bit(input_: List[str], index):
    count_bit_rate = {
        "1": 0,
        "0": 0
    }

    for code in input_:
        bit = code[index]
        count_bit_rate[bit] = count_bit_rate.get(bit, 0) + 1

    if count_bit_rate["1"] < count_bit_rate["0"]:
        return "1"
    elif count_bit_rate["0"] < count_bit_rate["1"]:
        return "0"
    return None


def calculate_oxygen_generator_rating(input_: List[str], index: int = 0, oxygen_generator_rating: str = ""):
    if len(input_) == 1:
        return input_[0]
    else:
        most_common_bit = calculate_most_common_bit(input_, index)

        if most_common_bit is None:
            oxygen_generator_rating += "1"
        else:
            oxygen_generator_rating += most_common_bit

    new_inputs = list(filter(lambda x: x.startswith(oxygen_generator_rating), input_))
    return calculate_oxygen_generator_rating(new_inputs, index + 1, oxygen_generator_rating)


def calculate_co2_scrubber_rating(input_: List[str], index: int = 0, co2_scrubber_rating: str = ""):
    if len(input_) == 1:
        return input_[0]
    else:
        less_common_bit = calculate_less_common_bit(input_, index)

        if less_common_bit is None:
            co2_scrubber_rating += "0"
        else:
            co2_scrubber_rating += less_common_bit

    new_inputs = list(filter(lambda x: x.startswith(co2_scrubber_rating), input_))
    return calculate_co2_scrubber_rating(new_inputs, index + 1, co2_scrubber_rating)


def calculate_life_support_rating(input_: List[str]):
    oxygen_generator_rating = calculate_oxygen_generator_rating(input_)
    co2_scrubber_rating = calculate_co2_scrubber_rating(input_)

    return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)


if __name__ == "__main__":  # pragma: no cover
    inputs_puzzle_1 = read_file_inputs(os.path.join(BASE_DIR_INPUTS, "input_1.txt"))
    inputs_puzzle_2 = read_file_inputs(os.path.join(BASE_DIR_INPUTS, "input_2.txt"))

    print("solution 1", calculate_power_consumption(inputs_puzzle_1))
    print("solution 2", calculate_life_support_rating(inputs_puzzle_2))
