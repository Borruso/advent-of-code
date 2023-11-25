# -*- coding: utf-8 -*-

import re


def get_crates(crates):
    number_column = max(
        int(number)
        for number in re.findall(r"\d+", crates.split("\n")[-1])
    )
    crate_column = {
        number + 1: []
        for number in range(number_column)
    }
    crates_lines = crates.split("\n")[:-1]
    for line in crates_lines:
        for number in range(number_column):
            crate = re.findall(r"\w", line[:4].strip())
            if crate:
                crate_column[number + 1].append(crate[0])
            line = line[4:]
    return crate_column


def get_instructions_from_input(data):
    info_crates, info_moves = data.split("\n\n")
    crate_column = get_crates(info_crates)
    moves = info_moves.split("\n")
    return crate_column, moves


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_instructions_from_input(data)


def giant_cargo_crane_operator(crate_column, moves):
    for move in moves:
        number_crate, from_column, to_column = re.findall(r"\d+", move)
        for _ in range(int(number_crate)):
            crate = crate_column[int(from_column)][0]
            crate_column[int(to_column)].insert(0, crate)
            crate_column[int(from_column)] = crate_column[int(from_column)][1:]
    return "".join(
        crate_column[number][0]
        for number in crate_column.keys()
    )


def crate_mover_9001_crane_operator(crate_column, moves):
    for move in moves:
        number_crate, from_column, to_column = re.findall(r"\d+", move)
        crates = crate_column[int(from_column)][:int(number_crate)]
        for index, _ in enumerate(crates, start=1):
            crate_column[int(to_column)].insert(0, crates[-index])
        crate_column[int(from_column)] = crate_column[int(from_column)][int(number_crate):]
    return "".join(
        crate_column[number][0]
        for number in crate_column.keys()
    )


if __name__ == "__main__":
    crate_column, moves = read_file("input.txt")
    first_solution = giant_cargo_crane_operator(crate_column, moves)
    print(first_solution)

    crate_column, moves = read_file("input.txt")
    second_solution = crate_mover_9001_crane_operator(crate_column, moves)
    print(second_solution)
