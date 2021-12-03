# -*- coding: utf-8 -*-

def get_diagnostic_report_from_input(data):
    lines = data.split("\n")
    return [line for line in lines]


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_diagnostic_report_from_input(data)


def get_diagnostic_report_sorted(diagnostic_report):
    diagnostic_report_sorted = []
    for index in range(len(diagnostic_report[0])):
        list_bit = [report[index] for report in diagnostic_report if len(report) > 0]
        diagnostic_report_sorted.append("".join(list_bit))
    return diagnostic_report_sorted


def get_most_common(diagnostic_report, index):
    total_zero = diagnostic_report[index].count("0")
    total_one = diagnostic_report[index].count("1")
    if total_zero > total_one:
        return "0"
    else:
        return "1"


def get_gamma_rate(diagnostic_report):
    diagnostic_report_sorted = get_diagnostic_report_sorted(diagnostic_report)
    gamma_rate = ""
    for index in range(len(diagnostic_report_sorted)):
        gamma_rate += get_most_common(diagnostic_report_sorted, index)
    return gamma_rate


def get_least_common(diagnostic_report, index):
    total_zero = diagnostic_report[index].count("0")
    total_one = diagnostic_report[index].count("1")
    if total_zero > total_one:
        return "1"
    else:
        return "0"


def get_epsilon_rate(diagnostic_report):
    diagnostic_report_sorted = get_diagnostic_report_sorted(diagnostic_report)
    epsilon_rate = ""
    for index in range(len(diagnostic_report_sorted)):
        epsilon_rate += get_least_common(diagnostic_report_sorted, index)
    return epsilon_rate


def filter_by_bit_and_index(diagnostic_report, bit, index):
    return [report for report in diagnostic_report if report[index] == bit]


def get_oxygen_generator_rating(diagnostic_report, index):
    while len(diagnostic_report) > 1:
        diagnostic_report_sorted = get_diagnostic_report_sorted(diagnostic_report)
        most_bit = get_most_common(diagnostic_report_sorted, index)
        diagnostic_report = filter_by_bit_and_index(diagnostic_report, most_bit, index)
        index += 1
    return diagnostic_report[0]


def get_co2_scrubber_rating(diagnostic_report, index):
    while len(diagnostic_report) > 1:
        diagnostic_report_sorted = get_diagnostic_report_sorted(diagnostic_report)
        least_bit = get_least_common(diagnostic_report_sorted, index)
        diagnostic_report = filter_by_bit_and_index(diagnostic_report, least_bit, index)
        index += 1
    return diagnostic_report[0]


def binary_to_decimal(number):
    return int(number, 2)


def count_power_consumption(gamma_rate, epsilon_rate):
    gamma_rate_decimal = binary_to_decimal(gamma_rate)
    epsilon_rate_decimal = binary_to_decimal(epsilon_rate)
    return gamma_rate_decimal * epsilon_rate_decimal


def count_life_support_rating(oxygen_generator_rating, co2_scrubber_rating):
    oxygen_generator_rating_decimal = binary_to_decimal(oxygen_generator_rating)
    co2_scrubber_rating_decimal = binary_to_decimal(co2_scrubber_rating)
    return oxygen_generator_rating_decimal * co2_scrubber_rating_decimal


if __name__ == "__main__":
    diagnostic_report = read_file("input.txt")

    gamma_rate = get_gamma_rate(diagnostic_report)
    epsilon_rate = get_epsilon_rate(diagnostic_report)
    first_solution = count_power_consumption(gamma_rate, epsilon_rate)
    print(first_solution)

    oxygen_generator_rating = get_oxygen_generator_rating(diagnostic_report, 0)
    co2_scrubber_rating = get_co2_scrubber_rating(diagnostic_report, 0)
    second_solution = count_life_support_rating(oxygen_generator_rating, co2_scrubber_rating)
    print(second_solution)
