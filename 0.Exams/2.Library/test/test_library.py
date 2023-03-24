from project.library import Library
from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self):
        self.library = Library("Test")

    def test_correct_initializing(self):
        self.assertEqual("Test", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_invalid_raise_ex(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ""
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book_no_author(self):
        self.library.add_book("Author1", "Book1")
        self.assertEqual({'Author1': ['Book1']}, self.library.books_by_authors)

    def test_add_book_with_author(self):
        self.library.add_book("Author1", "Book1")
        self.library.add_book("Author1", "Book2")
        self.assertEqual({'Author1': ['Book1', 'Book2']}, self.library.books_by_authors)

    def test_add_book_with_another_author(self):
        self.library.books_by_authors = {'Author1': ['Book1']}
        self.library.add_book("Author2", "Book2")
        self.assertEqual({'Author1': ['Book1'], 'Author2': ['Book2']}, self.library.books_by_authors)

    def test_add_reader_invalid_already_added(self):
        self.library.readers = {"Georgi": [], "Ivan": []}
        result = self.library.add_reader("Georgi")
        self.assertEqual("Georgi is already registered in the Test library.", result)

    def test_add_reader_valid_already_added(self):
        self.library.add_reader("Georgi")
        self.assertEqual({'Georgi': []}, self.library.readers)

    def test_rent_book_reader_not_in_readers_invalid(self):
        self.library.readers = {"Georgi": [], "Ivan": []}
        result = self.library.rent_book("Pesho", "Author1", "Book1")
        self.assertEqual("Pesho is not registered in the Test Library.", result)

    def test_rent_book_author_not_in_authors_invalid(self):
        self.library.readers = {"Georgi": [], "Ivan": [], "Pesho": []}
        self.library.books_by_authors = {'Author1': ['Book1']}
        result = self.library.rent_book("Pesho", "Author2", "Book2")
        self.assertEqual("Test Library does not have any Author2's books.", result)

    def test_rent_book_not_in_books_invalid(self):
        self.library.readers = {"Georgi": [], "Ivan": [], "Pesho": []}
        self.library.books_by_authors = {'Author1': ['Book1']}
        result = self.library.rent_book("Pesho", "Author1", "Book2")
        self.assertEqual("""Test Library does not have Author1's "Book2".""", result)

    def test_rent_reader_author_book_valid(self):
        self.library.readers = {"Georgi": [], "Ivan": [], "Pesho": []}
        self.library.books_by_authors = {'Author1': ['Book1']}
        self.library.rent_book("Pesho", "Author1", "Book1")
        self.assertEqual({'Georgi': [], 'Ivan': [], 'Pesho': [{'Author1': 'Book1'}]}, self.library.readers)

    def test_rent_reader_author_book_removing_book_from_library_valid(self):
        self.library.readers = {"Georgi": [], "Ivan": [], "Pesho": []}
        self.library.books_by_authors = {'Author1': ['Book1']}
        self.library.rent_book("Pesho", "Author1", "Book1")
        self.assertEqual({'Author1': []}, self.library.books_by_authors)


if __name__ == "__main__":
    main()
