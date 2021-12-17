# -*- coding: utf-8 -*-

import unittest

from solution import get_target_area_from_input, get_highest_height_position, count_distinct_velocity_response_true

input_test = """target area: x=20..30, y=-10..-5"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.target_area = get_target_area_from_input(input_test)

    def test_get_highest_height_position(self):
        count = get_highest_height_position(self.target_area)
        self.assertEqual(count, 45)

    def test_count_distinct_velocity_response_true(self):
        count = count_distinct_velocity_response_true(self.target_area)
        self.assertEqual(count, 112)
