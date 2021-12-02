import pytest

from y2021.day_1.main import InputNotArray, NotEnoughValues, depth_measure_with_window
from y2021.day_2.main import pilot_submarine_with_aim


def test_depth_measure_success():
    input_ = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

    assert pilot_submarine_with_aim(input_) == 900


def test_depth_measure_input_lower_than_2():
    input_ = [199]

    with pytest.raises(NotEnoughValues):
        depth_measure_with_window(input_)

    assert True


def test_depth_measure_input_is_not_a_list():
    input_ = "[199]"

    with pytest.raises(InputNotArray):
        depth_measure_with_window(input_)

    assert True
