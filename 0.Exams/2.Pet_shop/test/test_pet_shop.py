from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self):
        self.shop = PetShop("Test")

    def test_correct_initializing(self):
        self.assertEqual("Test", self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_adding_food_below_0_raise_ex(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_food("food1", -2)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_adding_food_valid(self):
        result = self.shop.add_food("food1", 200)
        self.assertEqual("Successfully added 200.00 grams of food1.", result)
        self.shop.add_food("food1", 200)
        self.shop.add_food("food2", 300)
        self.assertEqual({"food1": 400, "food2": 300}, self.shop.food)

    def test_adding_pet_invalid_name_raise_ex(self):
        self.shop.pets = ["pet1", "pet3"]
        with self.assertRaises(Exception) as ex:
            self.shop.add_pet("pet1")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_adding_pet_valid_name(self):
        result = self.shop.add_pet("pet1")
        self.assertEqual("Successfully added pet1.", result)
        self.shop.add_pet("pet2")
        self.assertEqual(["pet1", "pet2"], self.shop.pets)

    def test_feed_pet_invalid_pet_name_raise_ex(self):
        self.shop.pets = ["pet1", "pet3"]
        self.shop.food = {"food1": 500, "food3": 1000}
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet("food2","pet2")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_invalid_food_name(self):
        self.shop.pets = ["pet1", "pet2", "pet3"]
        self.shop.food = {"food1": 500, "food3": 1000}
        result = self.shop.feed_pet("food2", "pet2")
        self.assertEqual('You do not have food2', result)

    def test_feed_pet_food_below_100_invalid(self):
        self.shop.pets = ["pet1", "pet2", "pet3"]
        self.shop.food = {"food1": 500, "food2": 50, "food3": 1000}
        result = self.shop.feed_pet("food2", "pet2")
        self.assertEqual("Adding food...", result)
        self.assertEqual({"food1": 500, "food2": 1050.0, "food3": 1000}, self.shop.food)

    def test_feed_pet_valid(self):
        self.shop.pets = ["pet1", "pet2", "pet3"]
        self.shop.food = {"food1": 500, "food2": 650, "food3": 1000}
        result = self.shop.feed_pet("food2", "pet2")
        self.assertEqual("pet2 was successfully fed", result)
        self.assertEqual({"food1": 500, "food2": 550, "food3": 1000}, self.shop.food)

    def test_repr(self):
        self.shop.pets = ["pet1", "pet2"]
        result = self.shop.__repr__()
        self.assertEqual('Shop Test:\nPets: pet1, pet2', result)


if __name__ == "__main__":
    main()
