# -*- coding: utf-8 -*-

import unittest

from solution import get_commands_from_input, total_sizes_directories, total_size_smallest_directory

input_test = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.commands = get_commands_from_input(input_test)

    def test_total_sizes_directories_size_100000(self):
        total_sizes = total_sizes_directories(self.commands, size=100000)
        self.assertEqual(total_sizes, 95437)

    def test_total_size_smallest_directory(self):
        smallest_directory = total_size_smallest_directory(
            self.commands, disk_space=70000000, space_need=30000000
        )
        self.assertEqual(smallest_directory, 24933642)
