
from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self):
        self.student = StudentReportCard("Ivan", 12)

    def test_correct_initializing(self):
        self.assertEqual("Ivan", self.student.student_name)
        self.assertEqual(12, self.student.school_year)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.assertEqual({}, self.student.grades_by_subject)

    def test_correct_year(self):  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.student.school_year = 1   # !!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.assertEqual(1, self.student.school_year)

    def test_name_invalid_raise_ex(self):
        with self.assertRaises(ValueError) as ve:
            self.student.student_name = ""
        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_year_invalid_raise_ex(self):
        with self.assertRaises(ValueError) as ve:
            self.student.school_year = 20
        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_add_grade(self):
        self.student.add_grade("Math", 4)
        self.student.add_grade("Math", 6)
        self.student.add_grade("Chemistry", 5)
        result = self.student.grades_by_subject
        self.assertEqual({"Math": [4, 6], "Chemistry": [5]}, result)

    def test_average_grade_by_subject(self):
        self.student.add_grade("Math", 4)
        self.student.add_grade("Math", 6)
        self.student.add_grade("Chemistry", 5)
        result = self.student.average_grade_by_subject()
        self.assertEqual("Math: 5.00\nChemistry: 5.00", result)

    def test_average_grade_all_subjects(self):
        self.student.add_grade("Math", 4)
        self.student.add_grade("Math", 6)
        self.student.add_grade("Chemistry", 5)
        self.student.add_grade("Chemistry", 3)
        result = self.student.average_grade_for_all_subjects()
        self.assertEqual("Average Grade: 4.50", result)

    def test_repr_(self):
        self.student.add_grade("Math", 4)
        self.student.add_grade("Math", 6)
        self.student.add_grade("Chemistry", 5)
        self.student.add_grade("Chemistry", 3)
        result = self.student.__repr__()
        expected = "Name: Ivan\n" \
                   "Year: 12\n" \
                   "----------\n" \
                   "Math: 5.00\n" \
                   "Chemistry: 4.00\n" \
                   "----------\n" \
                   "Average Grade: 4.50"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
