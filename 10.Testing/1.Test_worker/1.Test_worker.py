from unittest import TestCase, main


class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker("TestGuy", 1000, 100)

    def test_correct_initializing(self):  # 1 #
        self.assertEqual("TestGuy", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_increase_energy_with_one_after_rest(self):     # 2 #
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_raise_exception_when_worker_has_0_or_negative_energy(self):    # 3 #
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_increment_money_on_worker_when_working(self):  # 4 #
        self.worker.work()
        self.assertEqual(self.worker.salary, self.worker.money)

    def test_decrease_energy_on_worker_when_working(self):  # 5 #
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_get_correct_info(self):    # 6 #
        self.assertEqual(f'TestGuy has saved 0 money.', self.worker.get_info())


if __name__ == "__main__":
    main()

    
"""
------------------------------------ Problem to resolve --------------------------------

Create a class WorkerTests
In judge you need to submit just the WokerTests class, with the unittest module imported.
Create the following tests:
•	# 1 # Test if the worker is initialized with the correct name, salary, and energy
•	# 2 # Test if the worker's energy is incremented after the rest method is called
•	# 3 # Test if an error is raised if the worker tries to work with negative energy or equal to 0
•	# 4 # Test if the worker's money is increased by his salary correctly after the work method is called
•	# 5 # Test if the worker's energy is decreased after the work method is called	
•	# 6 # Test if the get_info method returns the proper string with correct values


-------------------------------------- Example inputs ----------------------------------

class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'
        
"""
