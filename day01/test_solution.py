# -*- coding: utf-8 -*-

import unittest

from solution import get_numbers_from_input, count_total_depths, count_total_depths_windows

input_test = """199
200
208
210
200
207
240
269
260
263"""


class TestSolution(unittest.TestCase):
    numbers = None

    def setUp(self):
        self.numbers = get_numbers_from_input(input_test)

    def test_count_total_depths(self):
        count = count_total_depths(self.numbers)
        self.assertEqual(count, 7)

    def test_count_total_depths_windows(self):
        count = count_total_depths_windows(self.numbers, 3)
        self.assertEqual(count, 5)
