# -*- coding: utf-8 -*-
from collections import defaultdict


def get_paths_from_input(data):
    lines = data.split("\n")
    paths = defaultdict(set)
    for line in lines:
        start, end = line.strip().split("-")
        paths[start].add(end)
        paths[end].add(start)
    return paths


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_paths_from_input(data)


def get_total_possible_paths(paths, start, way, small_cave_twice=False):
    if start == "end":
        return 1
    s = 0
    for next_step in paths[start]:
        if next_step not in way:
            tmp = {next_step} if next_step == next_step.lower() else set()
            s += get_total_possible_paths(paths, next_step, way | tmp, small_cave_twice)
        elif small_cave_twice and next_step != "start":
            s += get_total_possible_paths(paths, next_step, way, False)

    return s


if __name__ == "__main__":
    paths = read_file("input.txt")

    first_solution = get_total_possible_paths(paths, start="start", way={"start"}, small_cave_twice=False)
    print(first_solution)

    second_solution = get_total_possible_paths(paths, start="start", way={"start"}, small_cave_twice=True)
    print(second_solution)
