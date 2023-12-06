# -*- coding: utf-8 -*-

import re


def get_games_list_from_input(data):
    games_list = []
    for game_info in data.split("\n"):
        _, set_played = game_info.split(": ")
        games_list.append(set_played)
    return games_list


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_games_list_from_input(data)


def compute_total_ids_games(games_list, bag):
    total = 0
    for index, game_sets in enumerate(games_list, start=1):
        if all(
            int(count) <= bag[color]
            for count, color in re.findall(r"(\d+) (\w+)", game_sets)
        ):
            total += index
    return total


def compute_total_power_games(games_list):
    total = 0
    for index, game_sets in enumerate(games_list, start=1):
        game = {}
        for count, color in re.findall(r"(\d+) (\w+)", game_sets):
            if color not in game.keys():
                game[color] = int(count)
            else:
                if game[color] < int(count):
                    game[color] = int(count)
        power = 1
        for color, number in game.items():
            power *= number
        total += power
    return total


if __name__ == "__main__":
    games_list = read_file("input.txt")

    bag = {"red": 12, "green": 13, "blue": 14}
    first_solution = compute_total_ids_games(games_list, bag)
    print(first_solution)

    second_solution = compute_total_power_games(games_list)
    print(second_solution)
