from project import Fridge
from project import Laptop
from project import TV
from project import Room


class YoungCouple(Room):
    def __init__(self, name: str, salary_one: float, salary_two: float, members_count: int = 2):
        super().__init__(name, salary_one + salary_two, members_count)
        self.room_cost = 20
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]
        self.calculate_expenses(self.appliances)
