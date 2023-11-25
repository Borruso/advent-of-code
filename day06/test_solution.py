# -*- coding: utf-8 -*-

import unittest

from solution import get_datastream_buffer_from_input, find_first_start_packet_marker

input_test1 = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
input_test2 = """bvwbjplbgvbhsrlpgdmjqwftvncz"""
input_test3 = """nppdvjthqldpwncqszvftbrmjlhg"""
input_test4 = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""
input_test5 = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.datastream_buffer1 = get_datastream_buffer_from_input(input_test1)
        self.datastream_buffer2 = get_datastream_buffer_from_input(input_test2)
        self.datastream_buffer3 = get_datastream_buffer_from_input(input_test3)
        self.datastream_buffer4 = get_datastream_buffer_from_input(input_test4)
        self.datastream_buffer5 = get_datastream_buffer_from_input(input_test5)

    def test_find_first_start_packet_marker_size_4(self):
        first_start_packet_marker = find_first_start_packet_marker(self.datastream_buffer1, char_size=4)
        self.assertEqual(first_start_packet_marker, 7)

        first_start_packet_marker = find_first_start_packet_marker(self.datastream_buffer2, char_size=4)
        self.assertEqual(first_start_packet_marker, 5)

        first_start_packet_marker = find_first_start_packet_marker(self.datastream_buffer3, char_size=4)
        self.assertEqual(first_start_packet_marker, 6)

        first_start_packet_marker = find_first_start_packet_marker(self.datastream_buffer4, char_size=4)
        self.assertEqual(first_start_packet_marker, 10)

        first_start_packet_marker = find_first_start_packet_marker(self.datastream_buffer5, char_size=4)
        self.assertEqual(first_start_packet_marker, 11)

    def test_crate_mover_9001_crane_operator_size_14(self):
        first_start_packet_marker = find_first_start_packet_marker(self.datastream_buffer1, char_size=14)
        self.assertEqual(first_start_packet_marker, 19)

        first_start_packet_marker = find_first_start_packet_marker(self.datastream_buffer2, char_size=14)
        self.assertEqual(first_start_packet_marker, 23)

        first_start_packet_marker = find_first_start_packet_marker(self.datastream_buffer3, char_size=14)
        self.assertEqual(first_start_packet_marker, 23)

        first_start_packet_marker = find_first_start_packet_marker(self.datastream_buffer4, char_size=14)
        self.assertEqual(first_start_packet_marker, 29)

        first_start_packet_marker = find_first_start_packet_marker(self.datastream_buffer5, char_size=14)
        self.assertEqual(first_start_packet_marker, 26)
