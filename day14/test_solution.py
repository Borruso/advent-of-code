# -*- coding: utf-8 -*-

import unittest

from solution import get_polymer_formula_from_input, get_most_least_element, get_result_polymer_template

input_test = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.polymer_template, self.pair_insertion = get_polymer_formula_from_input(input_test)

    def test_get_result_polymer_template(self):
        most_element, least_element = get_most_least_element(self.polymer_template, self.pair_insertion, 10)
        count = get_result_polymer_template(most_element, least_element)
        self.assertEqual(count, 1588)
        most_element, least_element = get_most_least_element(self.polymer_template, self.pair_insertion, 40)
        code = get_result_polymer_template(most_element, least_element)
        self.assertEqual(code, 2188189693529)
