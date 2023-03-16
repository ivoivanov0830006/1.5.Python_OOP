from unittest import TestCase, main


class CatTest(TestCase):

    def setUp(self):
        self.cat = Cat("TestCat")

    def test_correct_initializing(self):  # 0 #
        self.assertEqual("TestCat", self.cat.name)
        self.assertEqual(False, self.cat.fed)       # self.assertFalse(self.cat.fed)
        self.assertEqual(False, self.cat.sleepy)    # self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_cat_increase_size(self):     # 1 #
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_after_eating_is_fed(self):     # 2 #
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_feeding_cat_raise_exception(self):     # 3 #
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_cannot_fall_asleep_when_not_fed_raise_exception(self):     # 4 #
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_not_sleepy_after_sleep(self):     # 5 #
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()

    
"""
------------------------------------ Problem to resolve --------------------------------

Create a class CatTests
In judge you need to submit just the CatTests class, with the unitttest module imported.
Create the following tests:
•	# 1 #  Cat's size is increased after eating
•	# 2 #  Cat is fed after eating
•	# 3 #  Cat cannot eat if already fed, raises an error
•	# 4 #  Cat cannot fall asleep if not fed, raises an error
•	# 5 #  Cat is not sleepy after sleeping

-------------------------------------- Example inputs ----------------------------------

class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False

"""
