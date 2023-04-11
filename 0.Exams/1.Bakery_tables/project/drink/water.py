from project import Drink


class Water(Drink):
    DEFAULT_PRICE = 1.5

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, self.DEFAULT_PRICE, brand)
  
