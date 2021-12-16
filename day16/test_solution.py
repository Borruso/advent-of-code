# -*- coding: utf-8 -*-

import unittest

from solution import get_binary_value_from_input, get_sum_version_numbers, get_value_expression

input_hexadecimal1 = """D2FE28"""
input_hexadecimal2 = """38006F45291200"""
input_hexadecimal3 = """EE00D40C823060"""
input_hexadecimal4 = """8A004A801A8002F478"""
input_hexadecimal5 = """620080001611562C8802118E34"""
input_hexadecimal6 = """C0015000016115A2E0802F182340"""
input_hexadecimal7 = """A0016C880162017C3686B18A3D4780"""

input_hexadecimal8 = """C200B40A82"""
input_hexadecimal9 = """04005AC33890"""
input_hexadecimal10 = """880086C3E88112"""
input_hexadecimal11 = """CE00C43D881120"""
input_hexadecimal12 = """D8005AC2A8F0"""
input_hexadecimal13 = """F600BC2D8F"""
input_hexadecimal14 = """9C005AC2F8F0"""
input_hexadecimal15 = """9C0141080250320F1802104A08"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.binary_value1 = get_binary_value_from_input(input_hexadecimal1)
        self.binary_value2 = get_binary_value_from_input(input_hexadecimal2)
        self.binary_value3 = get_binary_value_from_input(input_hexadecimal3)
        self.binary_value4 = get_binary_value_from_input(input_hexadecimal4)
        self.binary_value5 = get_binary_value_from_input(input_hexadecimal5)
        self.binary_value6 = get_binary_value_from_input(input_hexadecimal6)
        self.binary_value7 = get_binary_value_from_input(input_hexadecimal7)

        self.binary_value8 = get_binary_value_from_input(input_hexadecimal8)
        self.binary_value9 = get_binary_value_from_input(input_hexadecimal9)
        self.binary_value10 = get_binary_value_from_input(input_hexadecimal10)
        self.binary_value11 = get_binary_value_from_input(input_hexadecimal11)
        self.binary_value12 = get_binary_value_from_input(input_hexadecimal12)
        self.binary_value13 = get_binary_value_from_input(input_hexadecimal13)
        self.binary_value14 = get_binary_value_from_input(input_hexadecimal14)
        self.binary_value15 = get_binary_value_from_input(input_hexadecimal15)

    def test_get_sum_version_numbers(self):
        finish_index, count = get_sum_version_numbers(self.binary_value1, start_index=0)
        self.assertEqual(count, 6)
        finish_index, count = get_sum_version_numbers(self.binary_value2, start_index=0)
        self.assertEqual(count, 9)
        finish_index, count = get_sum_version_numbers(self.binary_value3, start_index=0)
        self.assertEqual(count, 14)
        finish_index, count = get_sum_version_numbers(self.binary_value4, start_index=0)
        self.assertEqual(count, 16)
        finish_index, count = get_sum_version_numbers(self.binary_value5, start_index=0)
        self.assertEqual(count, 12)
        finish_index, count = get_sum_version_numbers(self.binary_value6, start_index=0)
        self.assertEqual(count, 23)
        finish_index, count = get_sum_version_numbers(self.binary_value7, start_index=0)
        self.assertEqual(count, 31)

    def test_get_value_expression(self):
        finish_index, count = get_value_expression(self.binary_value8, start_index=0)
        self.assertEqual(count, 3)
        finish_index, count = get_value_expression(self.binary_value9, start_index=0)
        self.assertEqual(count, 54)
        finish_index, count = get_value_expression(self.binary_value10, start_index=0)
        self.assertEqual(count, 7)
        finish_index, count = get_value_expression(self.binary_value11, start_index=0)
        self.assertEqual(count, 9)
        finish_index, count = get_value_expression(self.binary_value12, start_index=0)
        self.assertEqual(count, 1)
        finish_index, count = get_value_expression(self.binary_value13, start_index=0)
        self.assertEqual(count, 0)
        finish_index, count = get_value_expression(self.binary_value14, start_index=0)
        self.assertEqual(count, 0)
        finish_index, count = get_value_expression(self.binary_value15, start_index=0)
        self.assertEqual(count, 1)
