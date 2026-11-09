from pathlib import Path
from runpy import run_path
from unittest import TestCase

ROOT = Path(__file__).resolve().parent


class LogicTests(TestCase):
    def check_cases(self, folder, method, cases):
        solution = run_path(str(ROOT / folder / "main.py"))["Solution"]()
        for value, expected in cases:
            with self.subTest(value=value):
                self.assertEqual(getattr(solution, method)(value), expected)

    def test_factorial(self):
        self.check_cases("1_find_tailing_zero", "find_tailing_zeroes", [
            (0, 0), (7, 1), (25, 6), (125, 31), (-10, "number can not be negative")])

    def test_max_index(self):
        self.check_cases("2_index_of_max", "find_max_index", [
            ([], "list can not blank"), ([-5, -2, -2], 1), ([1, 2, 1, 3, 5, 6, 4], 5)])

    def test_thai(self):
        self.check_cases("3_number_to_thai", "number_to_thai", [
            (0, "ศูนย์"), (1, "หนึ่ง"), (10, "สิบ"), (21, "ยี่สิบเอ็ด"), (101, "หนึ่งร้อยเอ็ด"),
            (1_000_001, "หนึ่งล้านเอ็ด"), (10_000_000, "สิบล้าน"), (-1, "number can not less than 0")])

    def test_roman(self):
        self.check_cases("4_number_to_roman", "number_to_roman", [
            (4, "IV"), (101, "CI"), (944, "CMXLIV"), (3999, "MMMCMXCIX"),
            (0, "number must be between 1 and 3999"), (-1, "number can not less than 0")])
