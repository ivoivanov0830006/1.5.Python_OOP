from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calc_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calc_area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, height, side):
        self.height = height
        self.side = side

    def calc_area(self):
        return self.side * self.height / 2


class AreaCalculator:
    def __init__(self, shapes):
        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calc_area()
        return total


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)


"""
------------------------------------ Problem to resolve --------------------------------

You are provided with code containing class Rectangle and class AreaCalculator. Refactor the 
code using the Open/Closed Principle so that the code is open for extension (adding more shapes) 
but closed for modification.

-------------------------------------- Example inputs ----------------------------------
Code Before: 

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

class AreaCalculator:

    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.width * shape.height

        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)

-------------------------------------------------------------------------------------
Test Code Before:                                                   Output Before:
shapes = [Rectangle(2, 3), Rectangle(1, 6)]                         The total area is:  12
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)


-------------------------------------------------------------------------------------
Test Code After:                                                    Output Before:
shapes = [Rectangle(1, 6), Triangle(2, 3)]                          The total area is:  9.0
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)


"""
