# -*- coding: utf-8 -*-

def get_list_calories_from_input(data):
    return data.split("\n\n")


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_list_calories_from_input(data)


def count_calories(calories):
    return [
        sum(int(food) for food in calorie.split("\n"))
        for calorie in calories
    ]


def find_higher_calories(calories):
    all_calories = count_calories(calories)
    return max(all_calories)


def count_highers_calories(calories, top):
    all_calories = sorted(count_calories(calories), key=int, reverse=True)
    return sum(all_calories[:top])


if __name__ == "__main__":
    list_calories = read_file("input.txt")

    first_solution = find_higher_calories(list_calories)
    print(first_solution)

    second_solution = count_highers_calories(list_calories, 3)
    print(second_solution)
