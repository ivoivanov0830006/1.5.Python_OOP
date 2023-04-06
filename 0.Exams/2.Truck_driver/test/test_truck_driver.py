from test.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):

    def setUp(self):
        self.driver = TruckDriver("TestDriver", 10)

    def test_correct_initializing(self):
        self.assertEqual("TestDriver", self.driver.name)
        self.assertEqual(10, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_no_money_raise_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1
        self.assertEqual(f"{self.driver.name} went bankrupt.", str(ve.exception))

    def test_adding_already_added_cargo_offer_raise_exception(self):
        self.driver.add_cargo_offer("Varna", 100)
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Varna", 100)
        self.assertEqual(f"Cargo offer is already added.", str(ex.exception))

    def test_adding_not_added_cargo_offer_raise_exception(self):
        result = self.driver.add_cargo_offer("Varna", 100)
        self.assertEqual(f"Cargo for 100 to Varna was added as an offer.", result)
        self.assertEqual(self.driver.available_cargos, {"Varna": 100})

    def test_best_cargo_offer_valid(self):
        self.driver.add_cargo_offer("Varna", 100)
        self.driver.add_cargo_offer("Sofia", 1000)
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(f"{self.driver.name} is driving 1000 to Sofia.", result)
        self.assertEqual(self.driver.earned_money, 9875)
        self.assertEqual(self.driver.miles, 1000)

    def test_best_cargo_offer_invalid(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(f"There are no offers available.", result)

    def test_eat(self):
        self.driver.earned_money = 1000
        self.driver.eat(250)
        self.assertEqual(self.driver.earned_money, 980)

    def test_sleep(self):
        self.driver.earned_money = 1000
        self.driver.sleep(1000)
        self.assertEqual(self.driver.earned_money, 955)

    def test_pump_gas(self):
        self.driver.earned_money = 1000
        self.driver.pump_gas(1500)
        self.assertEqual(self.driver.earned_money, 500)

    def test_repair_truck(self):
        self.driver.earned_money = 10000
        self.driver.repair_truck(10000)
        self.assertEqual(self.driver.earned_money, 2500)

    def test_repr(self):
        self.assertEqual(f"{self.driver.name} has {self.driver.miles} miles behind his back.", str(self.driver))


if __name__ == "__main__":
    main()
