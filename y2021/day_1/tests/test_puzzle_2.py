import pytest

from y2021.day_1.main import InputNotArray, NotEnoughValues, depth_measure_with_window


def test_depth_measure_success():
    input_ = [607, 618, 618, 617, 647, 716, 769, 792]

    assert depth_measure_with_window(input_) == 5


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
