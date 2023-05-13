from project import Hardware
from math import floor


class HeavyHardware(Hardware):
    # pass
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, "Heavy", capacity, memory)
        self.capacity = 2 * capacity
        self.memory = floor(0.75 * memory)
