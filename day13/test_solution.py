# -*- coding: utf-8 -*-

import unittest

from solution import get_transparent_paper_from_input, get_total_dots, get_code_to_activate

input_test = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

code_test = """#####
#   #
#   #
#   #
#####"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.points, self.folds = get_transparent_paper_from_input(input_test)

    def test_get_total_dots(self):
        count, points = get_total_dots(self.points, self.folds, num_step=1)
        self.assertEqual(count, 17)

    def test_get_code_to_activate(self):
        code = get_code_to_activate(self.points, self.folds)
        self.assertEqual(code, code_test)
