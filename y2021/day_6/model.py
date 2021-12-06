class LanternFish:
    days_to_reproduce: int = None
    _new_lantern_fish: int = 0

    def __init__(self, days_to_reproduce: int):
        self.days_to_reproduce = days_to_reproduce

    def new_day(self):
        self.days_to_reproduce -= 1

        if self.days_to_reproduce < 0:
            self._new_lantern_fish += 1
            self.days_to_reproduce = 6

    def get_new_lantern_fish(self):
        aux = self._new_lantern_fish
        self._new_lantern_fish = 0
        return aux