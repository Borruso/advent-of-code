# -*- coding: utf-8 -*-

NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_calibration_value_from_input(data):
    return data.split("\n")


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_calibration_value_from_input(data)


def compute_total_calibration_value(calibration_value, replace_calibration):
    total = 0
    for record in calibration_value:
        if replace_calibration:
            for num, digit in NUMBERS.items():
                # don't remove the word, since some words are used twice
                record = record.replace(num, f"{num[0]}{digit}{num[-1]}")

        list_number = [
            char
            for char in record
            if char.isnumeric()
        ]
        if list_number:
            number = list_number[0] + list_number[-1]
            total += int(number)
    return total


if __name__ == "__main__":
    calibration_value = read_file("input.txt")

    first_solution = compute_total_calibration_value(calibration_value, False)
    print(first_solution)

    second_solution = compute_total_calibration_value(calibration_value, True)
    print(second_solution)
