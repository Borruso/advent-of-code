# -*- coding: utf-8 -*-

import unittest

from solution import get_assignments_from_input, total_assignments_fully_contain, total_assignments_overlapping

input_test = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.assignments = get_assignments_from_input(input_test)

    def test_total_assignments_fully_contain(self):
        total_fully_contain = total_assignments_fully_contain(self.assignments)
        self.assertEqual(total_fully_contain, 2)

    def test_total_assignments_overlapping(self):
        total_overlapping = total_assignments_overlapping(self.assignments)
        self.assertEqual(total_overlapping, 4)
