from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestPlayer(TestCase):
    def setUp(self):
        self.player1 = TennisPlayer("Test1", 20, 10)
        self.player2 = TennisPlayer("Test2", 22, 5)
        self.player3 = TennisPlayer("Test3", 18, 15)

    def test_correct_initializing(self):
        self.assertEqual("Test1", self.player1.name)
        self.assertEqual(20, self.player1.age)
        self.assertEqual(10, self.player1.points)
        self.assertEqual([], self.player1.wins)

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ve:
            self.player1.name = "Te"
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_valid_name(self):
        action = self.player1.name = "Test2"
        self.assertEqual("Test2", action)

    def test_invalid_year(self):
        with self.assertRaises(ValueError) as ve:
            self.player1.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_win_valid(self):
        self.player1.add_new_win("Test_tournament1")
        self.assertEqual(["Test_tournament1"], self.player1.wins)

    def test_add_win_invalid(self):
        self.player1.add_new_win("Test_tournament1")
        self.player1.add_new_win("Test_tournament2")
        self.assertEqual(["Test_tournament1", "Test_tournament2"], self.player1.wins)
        action = self.player1.add_new_win("Test_tournament1")
        self.assertEqual("Test_tournament1 has been already added to the list of wins!", action)

    def test_lower_than_other_valid(self):
        action = self.player1.__lt__(self.player3)
        self.assertEqual("Test3 is a top seeded player and he/she is better than Test1", action)

    def test_lower_than_other_invalid(self):
        action = self.player1.__lt__(self.player2)
        self.assertEqual("Test1 is a better player than Test2", action)

    def test__str__(self):
        self.player1.add_new_win("Test_tournament1")
        self.player1.add_new_win("Test_tournament2")
        action = self.player1.__str__()
        expected = "Tennis Player: Test1\nAge: 20\nPoints: 10.0\nTournaments won: Test_tournament1, Test_tournament2"
        self.assertEqual(expected, action)


if __name__ == "__main__":
    main()
