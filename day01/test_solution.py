# -*- coding: utf-8 -*-

import unittest

from solution import get_list_calories_from_input, find_higher_calories, count_highers_calories

input_test = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.list_calories = get_list_calories_from_input(input_test)

    def test_higher_calories_elf_carrying(self):
        higher_calories = find_higher_calories(self.list_calories)
        self.assertEqual(higher_calories, 24000)
        
    def test_count_highers_calories_elves_carrying(self):
        highers_calories = count_highers_calories(self.list_calories, 3)
        self.assertEqual(highers_calories, 45000)
