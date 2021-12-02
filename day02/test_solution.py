# -*- coding: utf-8 -*-

import unittest

from solution import get_positions_from_input, get_final_horizontal, get_final_depth, get_final_depth_with_aim, count_final_position

input_test = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


class TestSolution(unittest.TestCase):
    numbers = None

    def setUp(self):
        self.positions = get_positions_from_input(input_test)

    def test_count_final_position(self):
        final_horizontal = get_final_horizontal(self.positions)
        final_depth = get_final_depth(self.positions)
        count = count_final_position(final_horizontal, final_depth)
        self.assertEqual(count, 150)

    def test_count_final_position_with_aim(self):
        final_horizontal = get_final_horizontal(self.positions)
        final_depth = get_final_depth_with_aim(self.positions)
        count = count_final_position(final_horizontal, final_depth)
        self.assertEqual(count, 900)
