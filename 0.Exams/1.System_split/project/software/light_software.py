from project import Software
from math import floor


class LightSoftware(Software):
    # pass
    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, "Light", capacity_consumption, memory_consumption)
        self.capacity_consumption = floor(0.5 * capacity_consumption + capacity_consumption)
        self.memory_consumption = floor(0.5 * memory_consumption)
