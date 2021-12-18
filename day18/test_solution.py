# -*- coding: utf-8 -*-

import unittest

from solution import \
    get_snailfish_numbers_from_input, \
    get_final_sum, \
    get_magnitude_final_sum, \
    get_largest_magnitude_final_sum

input_test1 = """[1,2]
[[3,4],5]"""
input_test2 = """[[[[4,3],4],4],[7,[[8,4],9]]]
[1,1]"""
input_test3 = """[1,1]
[2,2]
[3,3]
[4,4]"""
input_test4 = """[1,1]
[2,2]
[3,3]
[4,4]
[5,5]"""
input_test5 = """[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]"""
input_test6 = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]"""
input_test7 = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.snailfish_numbers1 = get_snailfish_numbers_from_input(input_test1)
        self.snailfish_numbers2 = get_snailfish_numbers_from_input(input_test2)
        self.snailfish_numbers3 = get_snailfish_numbers_from_input(input_test3)
        self.snailfish_numbers4 = get_snailfish_numbers_from_input(input_test4)
        self.snailfish_numbers5 = get_snailfish_numbers_from_input(input_test5)
        self.snailfish_numbers6 = get_snailfish_numbers_from_input(input_test6)
        self.snailfish_numbers7 = get_snailfish_numbers_from_input(input_test7)

    def test_get_final_sum(self):
        final_sum_list, count1 = get_final_sum(self.snailfish_numbers1)
        self.assertEqual(count1, "[[1,2],[[3,4],5]]")
        final_sum_list, count2 = get_final_sum(self.snailfish_numbers2)
        self.assertEqual(count2, "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")
        final_sum_list, count3 = get_final_sum(self.snailfish_numbers3)
        self.assertEqual(count3, "[[[[1,1],[2,2]],[3,3]],[4,4]]")
        final_sum_list, count4 = get_final_sum(self.snailfish_numbers4)
        self.assertEqual(count4, "[[[[3,0],[5,3]],[4,4]],[5,5]]")
        final_sum_list, count5 = get_final_sum(self.snailfish_numbers5)
        self.assertEqual(count5, "[[[[5,0],[7,4]],[5,5]],[6,6]]")
        final_sum_list, count6 = get_final_sum(self.snailfish_numbers6)
        self.assertEqual(count6, "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")
        final_sum_list, count7 = get_final_sum(self.snailfish_numbers7)
        self.assertEqual(count7, "[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]")

    def test_get_magnitude_final_sum(self):
        final_sum, final_sum_formatted = get_final_sum(self.snailfish_numbers1)
        count1 = get_magnitude_final_sum(final_sum)
        self.assertEqual(count1, 143)
        final_sum, final_sum_formatted = get_final_sum(self.snailfish_numbers2)
        count2 = get_magnitude_final_sum(final_sum)
        self.assertEqual(count2, 1384)
        final_sum, final_sum_formatted = get_final_sum(self.snailfish_numbers3)
        count3 = get_magnitude_final_sum(final_sum)
        self.assertEqual(count3, 445)
        final_sum, final_sum_formatted = get_final_sum(self.snailfish_numbers4)
        count4 = get_magnitude_final_sum(final_sum)
        self.assertEqual(count4, 791)
        final_sum, final_sum_formatted = get_final_sum(self.snailfish_numbers5)
        count5 = get_magnitude_final_sum(final_sum)
        self.assertEqual(count5, 1137)
        final_sum, final_sum_formatted = get_final_sum(self.snailfish_numbers6)
        count6 = get_magnitude_final_sum(final_sum)
        self.assertEqual(count6, 3488)
        final_sum, final_sum_formatted = get_final_sum(self.snailfish_numbers7)
        count7 = get_magnitude_final_sum(final_sum)
        self.assertEqual(count7, 4140)

    def test_get_largest_magnitude_final_sum(self):
        count7 = get_largest_magnitude_final_sum(self.snailfish_numbers7)
        self.assertEqual(count7, 3993)
