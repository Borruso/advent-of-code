# -*- coding: utf-8 -*-
from itertools import product


def get_energy_level_map_from_input(data):
    lines = data.split("\n")
    return [[int(energy_level) for energy_level in line.strip()] for line in lines]


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_energy_level_map_from_input(data)


def get_coords_adjacent(next_energy_level_map, x, y):
    for dy, dx in product([-1, 0, 1], repeat=2):
        neighbour_x, neighbour_y = x + dy, y + dx
        if 0 <= neighbour_x < len(next_energy_level_map) and 0 <= neighbour_y < len(next_energy_level_map[0]):
            yield neighbour_x, neighbour_y


def compute_flash(next_energy_level_map, flashes, x, y):
    flashes[x][y] = True
    for neighbour_x, neighbour_y in get_coords_adjacent(next_energy_level_map, x, y):
        next_energy_level_map[neighbour_x][neighbour_y] += 1
        if not flashes[neighbour_x][neighbour_y] and next_energy_level_map[neighbour_x][neighbour_y] > 9:
            compute_flash(next_energy_level_map, flashes, neighbour_x, neighbour_y)


def next_step(energy_level_map):
    next_energy_level_map = [[0] * len(energy_level_map[0]) for _ in range(len(energy_level_map))]
    flashes = [[False] * len(energy_level_map[0]) for _ in range(len(energy_level_map))]
    for x, y in product(range(len(energy_level_map)), range(len(energy_level_map[0]))):
        next_energy_level_map[x][y] += energy_level_map[x][y] + 1
        if next_energy_level_map[x][y] > 9:
            compute_flash(next_energy_level_map, flashes, x, y)
    return [[0 if val > 9 else val for val in row] for row in next_energy_level_map]


def get_total_flashes(energy_level_map, steps):
    flashes = 0
    for _ in range(steps):
        energy_level_map = next_step(energy_level_map)
        flashes += sum(val == 0 for row in energy_level_map for val in row)
    return flashes


def get_step_octopus_flashes(energy_level_map):
    steps = 0
    while any(val for row in energy_level_map for val in row):
        energy_level_map = next_step(energy_level_map)
        steps += 1
    return steps


if __name__ == "__main__":
    energy_level_map = read_file("input.txt")

    first_solution = get_total_flashes(energy_level_map, steps=100)
    print(first_solution)

    second_solution = get_step_octopus_flashes(energy_level_map)
    print(second_solution)
