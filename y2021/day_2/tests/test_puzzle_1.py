import pytest

from y2021.day_2.exceptions import WrongCommand
from y2021.day_2.main import pilot_submarine


def test_depth_measure_success():
    input_ = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

    assert pilot_submarine(input_) == 150


def test_depth_measure_receives_bad_command():
    input_ = ["back 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

    with pytest.raises(WrongCommand):
        pilot_submarine(input_)

    assert True
