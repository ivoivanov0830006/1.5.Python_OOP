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
