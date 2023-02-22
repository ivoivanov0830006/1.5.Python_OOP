class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def status(self):
        result = self.size - self.quantity
        return result

    def fill(self, current_quantity):
        free_space = self.size - self.quantity
        if free_space >= current_quantity:
            self.quantity += current_quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
