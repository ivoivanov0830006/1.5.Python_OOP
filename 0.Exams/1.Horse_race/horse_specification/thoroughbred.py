from project import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    INCREASE = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        if self.speed <= self.MAX_SPEED - self.INCREASE:
            self.speed += self.INCREASE
        else:
            self.speed = self.MAX_SPEED
