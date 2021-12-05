# -*- coding: utf-8 -*-

import re


def get_lines_from_input(data):
    lines = data.split("\n")
    lines = [re.findall(r'(\d*),(\d*)', line) for line in lines]
    return [[(int(x), int(y)) for x, y in line] for line in lines]


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_lines_from_input(data)


def get_horizontal_lines(coordinates_dict, x1, y1, x2, y2):
    if y1 == y2:
        while True:
            coordinates = (x1, y1)
            if coordinates not in coordinates_dict:
                coordinates_dict[coordinates] = 1
            else:
                coordinates_dict[coordinates] += 1
            if x1 == x2:
                break
            if x1 < x2:
                x1 += 1
            else:
                x1 -= 1
    return coordinates_dict


def get_vertical_lines(coordinates_dict, initial_x1, x1, y1, x2, y2):
    if initial_x1 == x2:
        while True:
            coordinates = (x1, y1)
            if coordinates not in coordinates_dict:
                coordinates_dict[coordinates] = 1
            else:
                coordinates_dict[coordinates] += 1
            if y1 == y2:
                break
            if y1 < y2:
                y1 += 1
            else:
                y1 -= 1
    return coordinates_dict


def get_digonal_lines(coordinates_dict, x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return coordinates_dict
    while True:
        coordinates = (x1, y1)
        if coordinates not in coordinates_dict:
            coordinates_dict[coordinates] = 1
        else:
            coordinates_dict[coordinates] += 1
        if x1 == x2:
            break
        if x1 < x2:
            x1 += 1
        else:
            x1 -= 1
        if y1 < y2:
            y1 += 1
        else:
            y1 -= 1
    return coordinates_dict


def get_lines_overlap(lines, horizontal=True, vertical=True, diagonal=False):
    coordinates_dict = {}
    for line in lines:
        x1, y1 = line[0]
        x2, y2 = line[1]
        initial_x1 = x1
        if horizontal:
            coordinates_dict = get_horizontal_lines(coordinates_dict, x1, y1, x2, y2)
        if vertical:
            coordinates_dict = get_vertical_lines(coordinates_dict, initial_x1, x1, y1, x2, y2)
        if diagonal:
            coordinates_dict = get_digonal_lines(coordinates_dict, x1, y1, x2, y2)
    return sum([1 if coordinate > 1 else 0 for coordinate in coordinates_dict.values()])


if __name__ == "__main__":
    lines = read_file("input.txt")

    first_solution = get_lines_overlap(lines)
    print(first_solution)

    second_solution = get_lines_overlap(lines, diagonal=True)
    print(second_solution)
