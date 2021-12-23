# -*- coding: utf-8 -*-

import re
from bisect import bisect


def get_reboot_steps_from_input(data):
    reboot_steps = []
    for line in data.split("\n"):
        turn, coords_step = line.split()
        min_x, max_x, min_y, max_y, min_z, max_z = map(int, re.findall(r"-?\d+", coords_step))
        reboot_steps.append((turn, min_x, max_x + 1, min_y, max_y + 1, min_z, max_z + 1))
    return reboot_steps


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_reboot_steps_from_input(data)


def get_total_cubes_on_inside_region(reboot_steps, region):
    initial_min_x, initial_max_x, initial_min_y, initial_max_y, initial_min_z, initial_max_z = region
    total_cubes = set()
    for turn, min_x, max_x, min_y, max_y, min_z, max_z in reboot_steps:
        if min_x >= initial_min_x and max_x <= initial_max_x \
                and min_y >= initial_min_y and max_y <= initial_max_y \
                and min_z >= initial_min_z and max_z <= initial_max_z:
            for x in range(min_x, max_x):
                for y in range(min_y, max_y):
                    for z in range(min_z, max_z):
                        if turn == "on":
                            total_cubes.add((x, y, z))
                        else:
                            total_cubes.discard((x, y, z))
    return len(total_cubes)


def get_all_x(reboot_steps):
    all_x = []
    for reboot_step in reboot_steps:
        all_x.append(reboot_step[1])
        all_x.append(reboot_step[2])
    return sorted(set(all_x))


def get_all_y(reboot_steps):
    all_y = []
    for reboot_step in reboot_steps:
        all_y.append(reboot_step[3])
        all_y.append(reboot_step[4])
    return sorted(set(all_y))


def get_all_z(reboot_steps):
    all_z = []
    for reboot_step in reboot_steps:
        all_z.append(reboot_step[5])
        all_z.append(reboot_step[6])
    return sorted(set(all_z))


def get_total_cubes_on(reboot_steps, all_x, all_y, all_z):
    regions = set()
    for turn, min_x, max_x, min_y, max_y, min_z, max_z in reboot_steps:
        for x in range(bisect(all_x, min_x), bisect(all_x, max_x)):
            for y in range(bisect(all_y, min_y), bisect(all_y, max_y)):
                for z in range(bisect(all_z, min_z), bisect(all_z, max_z)):
                    if turn == "on":
                        regions.add((x, y, z))
                    else:
                        regions.discard((x, y, z))
    for i in range(len(all_x) - 1, 0, -1):
        all_x[i] -= all_x[i - 1]
    for i in range(len(all_y) - 1, 0, -1):
        all_y[i] -= all_y[i - 1]
    for i in range(len(all_z) - 1, 0, -1):
        all_z[i] -= all_z[i - 1]
    return sum(all_x[x] * all_y[y] * all_z[z] for x, y, z in regions)


if __name__ == "__main__":
    reboot_steps = read_file("input.txt")

    first_solution = get_total_cubes_on_inside_region(reboot_steps, region=(-50, 50, -50, 50, -50, 50))
    print(first_solution)

    all_x = get_all_x(reboot_steps)
    all_y = get_all_y(reboot_steps)
    all_z = get_all_z(reboot_steps)
    second_solution = get_total_cubes_on(reboot_steps, all_x, all_y, all_z)
    print(second_solution)
