import pytest

from y2021.day_6.main import puzzle_1
from y2021.day_6.exceptions import WrongFormatLanternFish


@pytest.mark.parametrize(
    "input_, days, expected",
    [
        pytest.param(
            "3,4,3,1,2",
            18,
            26,
            id="Expected 26 lanternfish after 18 days",
        ),
        pytest.param(
            "3,4,3,1,2",
            80,
            5934,
            id="Expected 5934 lanternfish after 80 days",
        ),
    ],
)
def test_puzzle_1(input_, days, expected):
    assert puzzle_1(input_, days) == expected


def test_transform_line_to_lantern_fish():
    with pytest.raises(WrongFormatLanternFish):
        puzzle_1("1,2,3,b", 10)

    assert True
