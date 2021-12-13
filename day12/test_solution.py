# -*- coding: utf-8 -*-

import unittest

from solution import get_paths_from_input, get_total_possible_paths

input_path1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

input_path2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

input_path3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.paths1 = get_paths_from_input(input_path1)
        self.paths2 = get_paths_from_input(input_path2)
        self.paths3 = get_paths_from_input(input_path3)

    def test_get_total_possible_paths(self):
        count1 = get_total_possible_paths(self.paths1, start="start", way={"start"}, small_cave_twice=False)
        self.assertEqual(count1, 10)
        count2 = get_total_possible_paths(self.paths2, start="start", way={"start"}, small_cave_twice=False)
        self.assertEqual(count2, 19)
        count3 = get_total_possible_paths(self.paths3, start="start", way={"start"}, small_cave_twice=False)
        self.assertEqual(count3, 226)

    def test_get_total_possible_paths_with_small_cave_twice(self):
        count1 = get_total_possible_paths(self.paths1, start="start", way={"start"}, small_cave_twice=True)
        self.assertEqual(count1, 36)
        count2 = get_total_possible_paths(self.paths2, start="start", way={"start"}, small_cave_twice=True)
        self.assertEqual(count2, 103)
        count3 = get_total_possible_paths(self.paths3, start="start", way={"start"}, small_cave_twice=True)
        self.assertEqual(count3, 3509)
