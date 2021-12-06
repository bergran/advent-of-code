import pytest

from y2021.day_6.main import puzzle_2


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
        pytest.param(
            "3,4,3,1,2",
            256,
            26984457539,
            id="Expected 5934 lanternfish after 80 days",
        ),
    ],
)
def test_puzzle_2(input_, days, expected):
    assert puzzle_2(input_, days) == expected
