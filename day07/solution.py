# -*- coding: utf-8 -*-


def get_initial_state_from_input(data):
    lines = data.split(",")
    return [int(line) for line in lines]


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_initial_state_from_input(data)


def get_fuel_linear_cost(initial_state):
    fuel_linear = [0] * len(initial_state)
    for i in range(len(initial_state)):
        for position in initial_state:
            move = abs(position - i)
            fuel_linear[i] += move
    return fuel_linear


def get_move_crab_engineering(position, i):
    return sum(range(1, abs(position - i) + 1))


def get_fuel_crab_engineering(initial_state):
    fuel_crab_engineering = [0] * len(initial_state)
    for i in range(len(initial_state)):
        for position in initial_state:
            move = get_move_crab_engineering(position, i)
            fuel_crab_engineering[i] += move
    return fuel_crab_engineering


if __name__ == "__main__":
    initial_state = read_file("input.txt")

    first_solution = min(get_fuel_linear_cost(initial_state))
    print(first_solution)

    second_solution = min(get_fuel_crab_engineering(initial_state))
    print(second_solution)
