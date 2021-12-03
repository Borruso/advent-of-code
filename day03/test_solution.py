# -*- coding: utf-8 -*-

import unittest

from solution import \
    get_diagnostic_report_from_input, \
    binary_to_decimal, \
    get_gamma_rate, \
    get_epsilon_rate, \
    count_power_consumption, \
    get_oxygen_generator_rating, \
    get_co2_scrubber_rating, \
    count_life_support_rating

input_test = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


class TestSolution(unittest.TestCase):
    numbers = None

    def setUp(self):
        self.diagnostic_report = get_diagnostic_report_from_input(input_test)

    def test_count_power_consumption(self):
        gamma_rate = get_gamma_rate(self.diagnostic_report)
        self.assertEqual(binary_to_decimal(gamma_rate), 22)
        epsilon_rate = get_epsilon_rate(self.diagnostic_report)
        self.assertEqual(binary_to_decimal(epsilon_rate), 9)
        count = count_power_consumption(gamma_rate, epsilon_rate)
        self.assertEqual(count, 198)

    def test_count_life_support_rating(self):
        oxygen_generator_rating = get_oxygen_generator_rating(self.diagnostic_report, 0)
        self.assertEqual(binary_to_decimal(oxygen_generator_rating), 23)
        co2_scrubber_rating = get_co2_scrubber_rating(self.diagnostic_report, 0)
        self.assertEqual(binary_to_decimal(co2_scrubber_rating), 10)
        count = count_life_support_rating(oxygen_generator_rating, co2_scrubber_rating)
        self.assertEqual(count, 230)
