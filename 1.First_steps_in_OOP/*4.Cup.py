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


"""
------------------------------------ Problem to resolve --------------------------------

Create a class called Cup. Upon initialization, it should receive size (integer) and quantity 
(an integer representing how much liquid is in it).
The class should have two methods:
    ⦁	fill(quantity) that will increase the amount of liquid in the cup with the given quantity 
    (if there is space in the cup, otherwise ignore).
    ⦁	status() that will return the amount of free space left in the cup.
Submit only the class in the judge system. Do not forget to test your code.
-------------------------------------- Example inputs ----------------------------------
Test Code	
cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())	
Output
50
10

"""
