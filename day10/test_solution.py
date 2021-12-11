# -*- coding: utf-8 -*-

import unittest

from solution import \
    get_chunks_from_input, \
    get_corrupted_symbols, \
    get_total_syntax_error_score, \
    get_closing_characters, \
    get_middle_score

input_test = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.chunks = get_chunks_from_input(input_test)

    def test_get_total_syntax_error_score(self):
        corrupted_chars, incomplete_chunks = get_corrupted_symbols(self.chunks)
        count = get_total_syntax_error_score(corrupted_chars)
        self.assertEqual(count, 26397)

    def test_get_middle_score(self):
        corrupted_chars, incomplete_chunks = get_corrupted_symbols(self.chunks)
        closing_characters = get_closing_characters(incomplete_chunks)
        count = get_middle_score(closing_characters)
        self.assertEqual(count, 288957)
