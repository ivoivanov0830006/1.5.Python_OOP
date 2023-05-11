from project import Astronaut


class Biologist(Astronaut):
    DEFAULT_BREATH = 5

    def __init__(self, name: str, oxygen: int = 70):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.DEFAULT_BREATH

    def increase_oxygen(self, amount):
        self.oxygen += amount
