# -*- coding: utf-8 -*-

import unittest

from solution import get_lines_from_input, get_lines_overlap

input_test = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.lines = get_lines_from_input(input_test)

    def test_get_lines_overlap(self):
        count = get_lines_overlap(self.lines)
        self.assertEqual(count, 5)

    def test_get_lines_overlap_with_diagonal_lines(self):
        count = get_lines_overlap(self.lines, diagonal=True)
        self.assertEqual(count, 12)
