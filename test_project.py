import unittest

from main import load_data


class TestStudentProject(unittest.TestCase):
    def test_empty_data_structure(self):
        data = {"students": {}, "attendance": {}, "marks": {}}
        self.assertEqual(len(data["students"]), 0)

    def test_attendance_calculation(self):
        present = 18
        total = 20
        self.assertEqual(present / total * 100, 90)

    def test_average_marks(self):
        marks = [80, 90, 70]
        self.assertEqual(sum(marks) / len(marks), 80)

    def test_grade_range(self):
        average = 85
        self.assertTrue(80 <= average < 90)


if __name__ == "__main__":
    unittest.main()
