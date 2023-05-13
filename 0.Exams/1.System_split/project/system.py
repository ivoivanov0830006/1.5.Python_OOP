from project import HeavyHardware
from project import PowerHardware
from project import ExpressSoftware
from project import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def __find_hardware(hardware_name):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                return hardware

    @staticmethod
    def __find_software(software_name):
        for software in System._software:
            if software.name == software_name:
                return software

    @staticmethod
    def __total_memory_hardware():
        total = 0
        for hardware in System._hardware:
            total += hardware.memory
        return total

    @staticmethod
    def __total_memory_software():
        total = 0
        for software in System._software:
            total += software.memory_consumption
        return total

    @staticmethod
    def __total_capacity_hardware():
        total = 0
        for hardware in System._hardware:
            total += hardware.capacity
        return total

    @staticmethod
    def __total_capacity_software():
        total = 0
        for software in System._software:
            total += software.capacity_consumption
        return total
