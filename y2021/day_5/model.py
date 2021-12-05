from dataclasses import dataclass
from typing import Tuple


@dataclass
class Line:
    from_: Tuple[int, int]
    to_: Tuple[int, int]

    def is_match(self):
        return self.from_[0] == self.to_[0] or self.from_[1] == self.to_[1]

    def is_diagonal(self):
        from_x, from_y = self.from_
        to_x, to_y = self.to_
        return abs(from_x - to_x) == abs(from_y - to_y)

    def is_match_diagonal(self):
        return self.is_match() or self.is_diagonal()