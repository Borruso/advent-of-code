# -*- coding: utf-8 -*-

import unittest

from solution import get_instructions_from_input, giant_cargo_crane_operator, crate_mover_9001_crane_operator

input_test = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.crate_column, self.moves = get_instructions_from_input(input_test)

    def test_giant_cargo_crane_operator(self):
        top_crate_column = giant_cargo_crane_operator(self.crate_column, self.moves)
        self.assertEqual(top_crate_column, "CMZ")

    def test_crate_mover_9001_crane_operator(self):
        total_overlapping = crate_mover_9001_crane_operator(self.crate_column, self.moves)
        self.assertEqual(total_overlapping, "MCD")
