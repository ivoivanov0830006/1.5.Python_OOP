from project import BakedFood


class Cake(BakedFood):
    DEFAULT_PORTION = 245

    def __init__(self, name: str, price: float):
        super().__init__(name, self.DEFAULT_PORTION, price)