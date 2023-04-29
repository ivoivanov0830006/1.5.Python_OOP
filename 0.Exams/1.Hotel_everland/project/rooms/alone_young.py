from project import TV
from project import Room


class AloneYoung(Room):
    def __init__(self, name: str, salary: float, members_count: int = 1):
        super().__init__(name, salary, members_count)
        self.room_cost = 10
        self.appliances = [TV()]
        self.calculate_expenses(self.appliances)
