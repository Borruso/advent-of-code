# -*- coding: utf-8 -*-

import unittest

from solution import get_map_risk_level_from_input, get_lowest_total_risk

input_test = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.map_risk_level = get_map_risk_level_from_input(input_test)

    def test_get_lowest_total_risk(self):
        count = get_lowest_total_risk(self.map_risk_level, num_path=1)
        self.assertEqual(count, 40)
        count = get_lowest_total_risk(self.map_risk_level, num_path=5)
        self.assertEqual(count, 315)
