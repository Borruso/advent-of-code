# -*- coding: utf-8 -*-

import unittest

from solution import get_situation_map_from_input, get_first_step_no_sea_cucumbers_move

input_test = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.situation_map = get_situation_map_from_input(input_test)

    def test_get_first_step_no_sea_cucumbers_move(self):
        count = get_first_step_no_sea_cucumbers_move(self.situation_map)
        self.assertEqual(count, 58)
