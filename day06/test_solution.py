# -*- coding: utf-8 -*-

import unittest

from solution import get_initial_state_from_input, get_number_lanternfish

input_test = """3,4,3,1,2"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.initial_state = get_initial_state_from_input(input_test)

    def test_get_number_lanternfish(self):
        count_days18 = get_number_lanternfish(self.initial_state, days=18)
        self.assertEqual(count_days18, 26)
        count_days80 = get_number_lanternfish(self.initial_state, days=80)
        self.assertEqual(count_days80, 5934)
        count_days256 = get_number_lanternfish(self.initial_state, days=256)
        self.assertEqual(count_days256, 26984457539)
