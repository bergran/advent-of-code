import pytest

from y2021.day_1.main import depth_measure, InputNotArray, NotEnoughValues


def test_depth_measure_success():
    input_ = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    assert depth_measure(input_) == 7


def test_depth_measure_input_lower_than_2():
    input_ = [199]

    with pytest.raises(NotEnoughValues):
        depth_measure(input_)

    assert True


def test_depth_measure_input_is_not_a_list():
    input_ = "[199]"

    with pytest.raises(InputNotArray):
        depth_measure(input_)

    assert True
