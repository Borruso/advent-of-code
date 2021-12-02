# -*- coding: utf-8 -*-

def get_positions_from_input(data):
    lines = data.split("\n")
    return [line for line in lines]


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_positions_from_input(data)


def get_final_horizontal(positions):
    final_horizontal = 0
    for position in positions:
        value = position.split(" ")
        if value[0] == "forward":
            final_horizontal += int(value[1])
        else:
            continue
    return final_horizontal


def get_final_depth(positions):
    final_depth = 0
    for position in positions:
        value = position.split(" ")
        if value[0] == "down":
            final_depth += int(value[1])
        elif value[0] == "up":
            final_depth -= int(value[1])
        else:
            continue
    return final_depth


def get_final_depth_with_aim(positions):
    final_aim = 0
    final_depth = 0
    for position in positions:
        value = position.split(" ")
        if value[0] == "forward":
            final_aim += final_depth * int(value[1])
        elif value[0] == "down":
            final_depth += int(value[1])
        elif value[0] == "up":
            final_depth -= int(value[1])
    return final_aim


def count_final_position(final_horizontal, final_depth):
    return final_horizontal * final_depth


if __name__ == "__main__":
    positions = read_file("input.txt")

    final_horizontal = get_final_horizontal(positions)
    final_depth = get_final_depth(positions)
    first_solution = count_final_position(final_horizontal, final_depth)
    print(first_solution)

    final_horizontal = get_final_horizontal(positions)
    final_depth = get_final_depth_with_aim(positions)
    second_solution = count_final_position(final_horizontal, final_depth)
    print(second_solution)
