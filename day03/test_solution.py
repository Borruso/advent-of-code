# -*- coding: utf-8 -*-

import unittest

from solution import get_rucksacks_from_input, total_rucksacks_priorities, total_elf_groups_priorities

input_test = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.rucksacks = get_rucksacks_from_input(input_test)

    def test_total_rucksacks_priorities(self):
        total_score = total_rucksacks_priorities(self.rucksacks)
        self.assertEqual(total_score, 157)

    def test_total_elf_groups_priorities(self):
        total_score = total_elf_groups_priorities(self.rucksacks, 3)
        self.assertEqual(total_score, 70)
