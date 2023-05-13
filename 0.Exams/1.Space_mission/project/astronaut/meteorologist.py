from project import Astronaut


class Meteorologist(Astronaut):
    DEFAULT_BREATH = 15

    def __init__(self, name: str, oxygen: int = 90):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.DEFAULT_BREATH

    def increase_oxygen(self, amount):
        self.oxygen += amount
