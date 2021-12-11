# -*- coding: utf-8 -*-

import unittest

from solution import get_energy_level_map_from_input, get_total_flashes, get_step_octopus_flashes

input_test = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.energy_level_map = get_energy_level_map_from_input(input_test)

    def test_get_total_flashes(self):
        count10 = get_total_flashes(self.energy_level_map, steps=10)
        self.assertEqual(count10, 204)
        count100 = get_total_flashes(self.energy_level_map, steps=100)
        self.assertEqual(count100, 1656)

    def test_get_step_octopus_flashes(self):
        count = get_step_octopus_flashes(self.energy_level_map)
        self.assertEqual(count, 195)
