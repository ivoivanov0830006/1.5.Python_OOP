from unittest import TestCase, main


class TestCar(TestCase):

    def setUp(self):
        self.car = Car("Nissan", "GT-R", 15, 75)

    def test_correct_initializing(self):
        self.assertEqual("Nissan", self.car.make)
        self.assertEqual("GT-R", self.car.model)
        self.assertEqual(15, self.car.fuel_consumption)
        self.assertEqual(75, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_no_make_raise_exception(self):  # 1 #
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_model_raise_exception(self):  # 2 #
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_zero_fuel_consumption_raise_exception(self):  # 3 #
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_zero_fuel_capacity_raise_exception(self):  # 4 #
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_negative_fuel_amount_raise_exception(self):  # 5 #
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_zero_raise_exception(self):  # 6 #
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_more_fuel_than_capacity(self):  # 7 #
        self.car.refuel(self.car.fuel_capacity + 20)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_driving_without_more_than_possible_raise_exception(self):  # 8 #
        self.car.fuel_amount = 20
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_driving_valid_distance_expect_fuel_reduce(self):  # 9 #
        self.car.fuel_amount = 75
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount, 60)


if __name__ == "__main__":
    main()

    
"""
------------------------------------ Problem to resolve --------------------------------

You are provided with a class IntegerList. It should only store integers. The initial integers should
be set by the constructor. They are stored as a list. IntegerList has a functionality to add, remove_index,
get, insert, get the biggest number, and get the index of an element. Your task is to test the class.
Note: You are not allowed to change the structure of the provided code.
Constraints
•	add operation, should add an element and returns the list.
    *	If the element is not an integer, a ValueError is thrown
•	remove_index operation removes the element on that index and returns it.
    *	If the index is out of range, an IndexError is thrown
•	__init__ should only take integers, and store them
•	get should return the specific element
    *	If the index is out of range, an IndexError is thrown
•	insert
    *	If the index is out of range, IndexError is thrown
    *	If the element is not an integer, ValueError is thrown
•	get_biggest
•	get_index
Hint: Do not forget to test the constructor

-------------------------------------- Example inputs ----------------------------------

class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):  # 1 #
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):  # 2 #
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):  # 3 #
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):  # 4 #
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):  # 5 #
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):   # 6 #
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:   # 7 #
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:   # 8 #
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed   # 9 #


car = Car("a", "b", 1, 4)
car.make = ""
print(car)

"""


