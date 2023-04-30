from project import Fridge
from project import Stove
from project import TV
from project import Room


class OldCouple(Room):
    def __init__(self, name: str, pension_one: float, pension_two: float, members_count: int = 2):
        super().__init__(name, pension_one + pension_two, members_count)
        self.room_cost = 15
        self.appliances = [TV(), TV(), Stove(), Stove(), Fridge(), Fridge()]
        self.calculate_expenses(self.appliances)
