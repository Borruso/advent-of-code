# -*- coding: utf-8 -*-

import unittest

from solution import get_matches_from_input, total_score_strategy_guide

input_test = """A Y
B X
C Z"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.matches = get_matches_from_input(input_test)

    def test_total_score_strategy_guide1(self):
        total_score = total_score_strategy_guide(self.matches, 1)
        self.assertEqual(total_score, 15)

    def test_total_score_strategy_guide2(self):
        total_score = total_score_strategy_guide(self.matches, 2)
        self.assertEqual(total_score, 12)
