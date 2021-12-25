# -*- coding: utf-8 -*-

from itertools import count


def get_situation_map_from_input(data):
    situation_map = {}
    for y, line in enumerate(data.split("\n")):
        for x, cucumbers in enumerate(line):
            situation_map[(x, y)] = cucumbers
    return situation_map


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_situation_map_from_input(data)


def get_first_step_no_sea_cucumbers_move(situation_map):
    max_x = max(x for x, y in situation_map) + 1
    max_y = max(y for x, y in situation_map) + 1
    for step in count(1):
        moved = False
        new_situation_map = situation_map.copy()
        for x, y in situation_map:
            new_x = (x + 1) % max_x
            new_y = y
            if situation_map[x, y] == ">" and situation_map[new_x, new_y] == ".":
                new_situation_map[x, y] = "."
                new_situation_map[new_x, new_y] = ">"
                moved = True
        situation_map = new_situation_map
        new_situation_map = situation_map.copy()
        for x, y in situation_map:
            new_x = x
            new_y = (y + 1) % max_y
            if situation_map[x, y] == "v" and situation_map[new_x, new_y] == ".":
                new_situation_map[x, y] = "."
                new_situation_map[new_x, new_y] = "v"
                moved = True
        situation_map = new_situation_map
        if not moved:
            return step


if __name__ == "__main__":
    situation_map = read_file("input.txt")

    first_solution = get_first_step_no_sea_cucumbers_move(situation_map)
    print(first_solution)
