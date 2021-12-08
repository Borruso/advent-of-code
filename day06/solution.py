# -*- coding: utf-8 -*-


def get_initial_state_from_input(data):
    lines = data.split(",")
    return [int(line) for line in lines]


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_initial_state_from_input(data)


def prepare_list_lanterfish(list_lanternfish, number_lanternfish_born):
    for lanternfish in range(number_lanternfish_born):
        list_lanternfish.append(9)
    new_list_lanternfish = []
    for day_born in list_lanternfish:
        if day_born == 0:
            new_list_lanternfish.append(7)
        else:
            new_list_lanternfish.append(day_born)
    return new_list_lanternfish


def get_number_lanternfish(initial_state, days):
    i = 0
    number_lanternfish_born = 0
    list_lanternfish = initial_state
    while i < days:
        list_lanternfish = prepare_list_lanterfish(list_lanternfish, number_lanternfish_born)
        list_lanternfish = [day_born - 1 for day_born in list_lanternfish]
        number_lanternfish_born = sum(1 for number in list_lanternfish if number == 0)
        i += 1
    return sum(1 for number in list_lanternfish)


if __name__ == "__main__":
    initial_state = read_file("input.txt")

    first_solution = get_number_lanternfish(initial_state, days=80)
    print(first_solution)

    second_solution = get_number_lanternfish(initial_state, days=256)
    print(second_solution)
