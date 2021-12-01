import os

import pytest

from src.utils import read_file_inputs, EmptyFile

BASE_DIR_INPUTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs")


def test_read_file_inputs_with_inputs():
    lines = read_file_inputs(os.path.join(BASE_DIR_INPUTS, "input_in_lines.txt"))
    assert lines == ["1", "2", "3", "4", "5"]


def test_read_file_inputs_empty():
    lines = None
    with pytest.raises(EmptyFile):
        lines = read_file_inputs(os.path.join(BASE_DIR_INPUTS, "empty_file.txt"))

    assert lines is None
