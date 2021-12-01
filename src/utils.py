from typing import List, Any


class EmptyFile(Exception):
    pass


def read_file_inputs(filepath) -> List[Any]:
    with open(filepath, "r") as file:
        inputs_ = file.read().split("\n")

    if not inputs_ or inputs_ == [""]:
        raise EmptyFile()

    return inputs_
