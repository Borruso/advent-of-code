# -*- coding: utf-8 -*-

import unittest

from solution import get_numbers_from_input, get_boards_from_input, get_sum_unmarked_numbers, get_final_score

numbers_test = "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1"

boards_test = """22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.numbers = get_numbers_from_input(numbers_test)
        self.boards = get_boards_from_input(boards_test, height=5)

    def test_count_final_score_first_board(self):
        sum_unmarked_numbers, last_number = get_sum_unmarked_numbers(self.numbers, self.boards, wins=1, height=5,
                                                                     width=5)
        self.assertEqual(sum_unmarked_numbers, 188)
        count = get_final_score(sum_unmarked_numbers, last_number)
        self.assertEqual(count, 4512)

    def test_count_final_score_last_board(self):
        sum_last_unmarked_numbers, last_number = get_sum_unmarked_numbers(self.numbers, self.boards, wins="unlimited",
                                                                          height=5, width=5, check="last")
        self.assertEqual(sum_last_unmarked_numbers, 148)
        count = get_final_score(sum_last_unmarked_numbers, last_number)
        self.assertEqual(count, 1924)
