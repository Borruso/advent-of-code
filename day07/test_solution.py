# -*- coding: utf-8 -*-

import unittest

from solution import get_initial_state_from_input, get_fuel_linear_cost, get_fuel_crab_engineering

input_test = """16,1,2,0,4,2,7,1,2,14"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.initial_state = get_initial_state_from_input(input_test)

    def test_get_fuel_linear_cost(self):
        count = min(get_fuel_linear_cost(self.initial_state))
        self.assertEqual(count, 37)

    def test_get_fuel_crab_engineering(self):
        count = min(get_fuel_crab_engineering(self.initial_state))
        self.assertEqual(count, 168)
