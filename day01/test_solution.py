# -*- coding: utf-8 -*-

import unittest

from solution import get_calibration_value_from_input, compute_total_calibration_value

input_test1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

input_test2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.calibration_value1 = get_calibration_value_from_input(input_test1)
        self.calibration_value2 = get_calibration_value_from_input(input_test2)

    def test_total_calibration_value(self):
        total_calibration_value1 = compute_total_calibration_value(self.calibration_value1, False)
        self.assertEqual(total_calibration_value1, 142)
        total_calibration_value2 = compute_total_calibration_value(self.calibration_value2, True)
        self.assertEqual(total_calibration_value2, 281)
