# -*- coding: utf-8 -*-

import unittest

from solution import \
    get_heightmap_from_input, \
    get_low_points, \
    get_total_risk_levels, \
    get_size_largest_basins, \
    get_multiply_largest_basins

input_test = """2199943210
3987894921
9856789892
8767896789
9899965678"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.heightmap = get_heightmap_from_input(input_test)

    def test_get_total_risk_levels(self):
        low_points, coords_low_points = get_low_points(self.heightmap)
        count = get_total_risk_levels(low_points)
        self.assertEqual(count, 15)

    def test_get_size_largest_basins(self):
        low_points, coords_low_points = get_low_points(self.heightmap)
        size_largest_basins = get_size_largest_basins(coords_low_points, self.heightmap)
        count = get_multiply_largest_basins(size_largest_basins, number=3)
        self.assertEqual(count, 1134)
