from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    WEIGHT_INCREASE = 1

    def __init__(self, name: str, kind: str, price: float, weight: int = 7):
        super().__init__(name, kind, price, weight)

    def eating(self):
        self.weight += self.WEIGHT_INCREASE

