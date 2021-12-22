# -*- coding: utf-8 -*-

import unittest

from solution import get_players_from_input, get_total_points_losing_player, get_winner_in_more_universes

input_test = """Player 1 starting position: 4
Player 2 starting position: 8"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.player1, self.player2 = get_players_from_input(input_test)

    def test_get_total_points_losing_player(self):
        count = get_total_points_losing_player(self.player1, self.player2)
        self.assertEqual(count, 739785)

    def test_get_winner_in_more_universes(self):
        count = get_winner_in_more_universes(self.player1, self.player2)
        self.assertEqual(count, 444356092776315)
