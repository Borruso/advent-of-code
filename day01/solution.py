# -*- coding: utf-8 -*-

def get_numbers_from_input(data):
    lines = data.split("\n")
    return [int(line) for line in lines]


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_numbers_from_input(data)


def count_total_depths(numbers):
    count = 0
    previous_number = numbers[0]
    for number in numbers:
        if number > previous_number:
            count += 1
        previous_number = number
    return count


def get_total_sum_windows(numbers, width):
    length = len(numbers) - (width - 1)
    list_windows = []
    for i in range(length):
        list_windows.append(sum(numbers[i: i + width]))
    return list_windows


def count_total_depths_windows(numbers, width):
    windows = get_total_sum_windows(numbers, width)
    count = count_total_depths(windows)
    return count


if __name__ == "__main__":
    numbers = read_file("input.txt")

    first_solution = count_total_depths(numbers)
    print(first_solution)

    second_solution = count_total_depths_windows(numbers, 3)
    print(second_solution)
