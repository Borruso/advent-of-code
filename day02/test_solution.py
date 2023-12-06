# -*- coding: utf-8 -*-

import unittest

from solution import get_games_list_from_input, compute_total_ids_games, compute_total_power_games

input_test = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.games_list = get_games_list_from_input(input_test)

    def test_compute_total_ids_possible_games(self):
        bag = {"red": 12, "green": 13, "blue": 14}
        total_ids = compute_total_ids_games(self.games_list, bag)
        self.assertEqual(total_ids, 8)

    def test_compute_total_power_games(self):
        total_power_games = compute_total_power_games(self.games_list)
        self.assertEqual(total_power_games, 2286)
