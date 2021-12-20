# -*- coding: utf-8 -*-

import unittest

from solution import get_algorithm_image_from_input, get_image_coords, get_total_lit_pixels

input_test = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.enhancement_algorithm, self.input_image = get_algorithm_image_from_input(input_test)

    def test_get_total_lit_pixels(self):
        image_coords = get_image_coords(self.input_image)
        count = get_total_lit_pixels(self.enhancement_algorithm, image_coords, steps=2)
        self.assertEqual(count, 35)
        count = get_total_lit_pixels(self.enhancement_algorithm, image_coords, steps=50)
        self.assertEqual(count, 3351)
