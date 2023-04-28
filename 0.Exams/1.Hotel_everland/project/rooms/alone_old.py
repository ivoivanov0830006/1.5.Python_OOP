from project import Room


class AloneOld(Room):
    def __init__(self, name: str, pension: float, members_count: int = 1):
        super().__init__(name, pension, members_count)
        self.room_cost = 10
