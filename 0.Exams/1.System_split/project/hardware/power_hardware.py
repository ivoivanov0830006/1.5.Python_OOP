from project import Hardware
from math import floor


class PowerHardware(Hardware):
    # pass
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, "Power", capacity, memory)
        self.capacity = floor(0.25 * capacity)
        self.memory = floor(0.75 * memory + memory)
