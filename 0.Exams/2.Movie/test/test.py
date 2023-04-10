from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("Test", 1990, 10)
        self.movie2 = Movie("Test2", 1980, 5)
        self.movie3 = Movie("Test3", 1970, 15)

    def test_correct_initializing(self):
        self.assertEqual("Test", self.movie.name)
        self.assertEqual(1990, self.movie.year)
        self.assertEqual(10, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_valid_name(self):
        action = self.movie.name = "Test2"
        self.assertEqual("Test2", action)

    def test_invalid_year(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor(self):
        self.movie.add_actor("Actor1")
        self.assertEqual(["Actor1"], self.movie.actors)

    def test_add_actor_again(self):
        self.movie.add_actor("Actor1")
        self.movie.add_actor("Actor2")
        self.assertEqual(["Actor1", "Actor2"], self.movie.actors)
        action = self.movie.add_actor("Actor2")
        self.assertEqual("Actor2 is already added in the list of actors!", action)

    def test_greater_than_other_valid(self):
        result = self.movie.__gt__(self.movie2)
        self.assertEqual(result, '"Test" is better than "Test2"')

    def test_greater_than_other_invalid(self):
        result = self.movie.__gt__(self.movie3)
        self.assertEqual(result, '"Test3" is better than "Test"')

    def test__repr__(self):
        self.movie.add_actor("Actor1")
        self.movie.add_actor("Actor2")
        result = self.movie.__repr__()
        expected = "Name: Test\nYear of Release: 1990\nRating: 10.00\nCast: Actor1, Actor2"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
