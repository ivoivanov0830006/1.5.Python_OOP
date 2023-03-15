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
