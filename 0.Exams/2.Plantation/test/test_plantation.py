from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):

    def setUp(self):
        self.plantation = Plantation(2)
        self.plants = {}
        self.workers = []

    def test_correct_initializing(self):
        self.assertEqual(2, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_invalid_raise_ex(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_invalid_raise_ex(self):
        self.plantation.workers = ["Pesho"]
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Pesho")
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_valid(self):
        self.plantation.workers = ["Pesho"]
        result = self.plantation.hire_worker("Gosho")
        self.assertEqual(len(self.plantation.workers), 2)
        self.assertEqual("Gosho successfully hired.", result)

    def test_planting_worker_invalid_raise_ex(self):
        self.plantation.workers = ["Pesho"]
        self.plantation.plants = {"Pesho": ["potato"]}
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Gosho", "tomato")
        self.assertEqual("Worker with name Gosho is not hired!", str(ve.exception))

    def test_plants_more_the_size_raise_ex(self):
        self.plantation.workers = ["Pesho"]
        self.plantation.planting("Pesho", "potato")
        self.plantation.planting("Pesho", "cucumber")
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Pesho", "tomato")
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_worker_plant_first_plant(self):
        self.plantation.workers = ["Pesho"]
        result = self.plantation.planting("Pesho", "potato")
        self.assertEqual(f"Pesho planted it's first potato.", result)

    def test_add_plants_to_workers_dict(self):
        self.plantation.hire_worker('Pesho')
        self.plantation.hire_worker('Gosho')
        self.plantation.plants['Pesho'] = ['potato']
        self.plantation.plants['Gosho'] = ['tomato']
        self.assertEqual(len(self.plantation), 2)

    def test_worker_plant_next_plant(self):
        self.plantation.workers = ["Pesho"]
        self.plantation.planting("Pesho", "potato")
        result = self.plantation.planting("Pesho", "tomato")
        self.assertEqual(f"Pesho planted tomato.", result)

    def test_str_(self):
        self.plantation.workers = ["Pesho", "Gosho"]
        self.plantation.planting("Pesho", "potato")
        self.plantation.planting("Gosho", "tomato")
        result = self.plantation.__str__()
        self.assertEqual("Plantation size: 2\nPesho, Gosho\nPesho planted: potato\nGosho planted: tomato", result)

    def test_repr_(self):
        self.plantation.workers = ["Pesho", "Gosho"]
        self.plantation.planting("Pesho", "potato")
        self.plantation.planting("Gosho", "tomato")
        result = self.plantation.__repr__()
        self.assertEqual("Size: 2\nWorkers: Pesho, Gosho", result)


if __name__ == "__main__":
    main()
