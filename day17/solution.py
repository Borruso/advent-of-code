# -*- coding: utf-8 -*-

import re


def get_target_area_from_input(data):
    return re.findall(r"x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)", data)


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_target_area_from_input(data)


def get_all_coords_in_target_area(x_min, x_max, y_min, y_max):
    target_area_coords = set()
    y = y_min
    while y <= y_max:
        x = x_min
        while x <= x_max:
            target_area_coords.add((x, y))
            x += 1
        y += 1
    return target_area_coords


def launch_probe(x_velocity, y_velocity, x_max, y_min, target_area_coords):
    x_probe, y_probe = (0, 0)
    while True:
        x_probe += x_velocity
        y_probe += y_velocity
        if (x_probe, y_probe) in target_area_coords:
            return True
        if x_velocity != 0:
            x_velocity -= 1 if x_velocity > 0 else -1
        y_velocity -= 1
        if y_probe < y_min or x_probe > x_max:
            return False


def count_distinct_velocity_response_true(target_area):
    x_min, x_max, y_min, y_max = [int(coord) for coord in target_area[0]]
    target_area_coords = get_all_coords_in_target_area(x_min, x_max, y_min, y_max)
    hits_list = []
    x_velocity = 0
    while x_velocity <= x_max:
        y_velocity = abs(y_min)
        while y_velocity >= y_min:
            response_launch = launch_probe(x_velocity, y_velocity, x_max, y_min, target_area_coords)
            if response_launch:
                hits_list.append((x_velocity, y_velocity))
            y_velocity -= 1
        x_velocity += 1
    return hits_list


def get_highest_height_position(target_area):
    hits_list = count_distinct_velocity_response_true(target_area)
    hits_list.sort(key=lambda h: h[1])
    max_height = sum(range(1, hits_list[-1][1] + 1))
    return max_height


if __name__ == "__main__":
    target_area = read_file("input.txt")

    first_solution = get_highest_height_position(target_area)
    print(first_solution)

    second_solution = len(count_distinct_velocity_response_true(target_area))
    print(second_solution)
