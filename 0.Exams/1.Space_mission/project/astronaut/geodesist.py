from project import Astronaut


class Geodesist(Astronaut):
    DEFAULT_BREATH = 10

    def __init__(self, name: str, oxygen: int = 50):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.DEFAULT_BREATH

    def increase_oxygen(self, amount):
        self.oxygen += amount
