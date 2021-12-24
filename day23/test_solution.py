# -*- coding: utf-8 -*-

import unittest

from solution import get_diagram_from_input, get_least_energy_organize_amphipods

input_test = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.diagram = get_diagram_from_input(input_test)

    def test_get_least_energy_organize_amphipods(self):
        count = get_least_energy_organize_amphipods(self.diagram, num_lines=2)
        self.assertEqual(count, 12521)
        new_diagram = self.diagram[:3] + ["  #D#C#B#A#", "  #D#B#A#C#"] + self.diagram[3:]
        count = get_least_energy_organize_amphipods(new_diagram, num_lines=4)
        self.assertEqual(count, 44169)
