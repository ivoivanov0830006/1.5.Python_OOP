from project import Fridge
from project import Laptop
from project import TV
from project import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, name: str, salary_one: float, salary_two: float, *children):
        super().__init__(name, salary_one + salary_two, 2 + len(children))
        self.room_cost = 30
        self.children = list(children)
        self.appliances = self.all_appliances()
        self.calculate_expenses(self.appliances, self.children)

    def all_appliances(self):
        total = []
        for member in range(self.members_count):
            total.append(TV())
            total.append(Laptop())
            total.append(Fridge())
        return total
