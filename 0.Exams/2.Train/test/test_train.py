from project.train.train import Train
from unittest import TestCase, main


class TestTrain(TestCase):
    def setUp(self):
        self.train = Train("Test", 2)

    def test_correct_initializing(self):
        self.assertEqual("Test", self.train.name)
        self.assertEqual(2, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_passenger_with_full_train_raise_ex(self):
        self.train.passengers = ["Ivan", "Petar"]
        with self.assertRaises(ValueError) as ve:
            self.train.add("Georgi")
        self.assertEqual("Train is full", str(ve.exception))
        self.assertEqual(["Ivan", "Petar"], self.train.passengers)

    def test_add_passenger_with_same_name_raise_ex(self):
        self.train.passengers = ["Ivan"]
        with self.assertRaises(ValueError) as ve:
            self.train.add("Ivan")
        self.assertEqual("Passenger Ivan Exists", str(ve.exception))

    def test_add_passenger_valid(self):
        self.train.passengers = ["Ivan"]
        result = self.train.add("Petar")
        self.assertEqual("Added passenger Petar", result)
        self.assertEqual(["Ivan", "Petar"], self.train.passengers)

    def test_remove_not_existing_passenger_raise_ex(self):
        self.train.passengers = ["Ivan", "Petar"]
        with self.assertRaises(ValueError) as ve:
            self.train.remove("Georgi")
        self.assertEqual("Passenger Not Found", str(ve.exception))

    def test_remove_passenger_valid(self):
        self.train.passengers = ["Ivan", "Petar"]
        result = self.train.remove("Ivan")
        self.assertEqual("Removed Ivan", result)
        self.assertEqual(["Petar"], self.train.passengers)


if __name__ == "__main__":
    main()
