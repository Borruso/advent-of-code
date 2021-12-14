# -*- coding: utf-8 -*-
from collections import Counter


def get_polymer_formula_from_input(data):
    polymer_template, pair_insertions = data.split("\n\n")
    pair_insertions_dict = dict(pair_insertion.split(" -> ") for pair_insertion in pair_insertions.split("\n"))
    return polymer_template, pair_insertions_dict


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_polymer_formula_from_input(data)


def get_pairs_polymer(polymer_template, pair_insertions_dict, num_steps):
    pairs_polymer = Counter([polymer_template[index:index + 2] for index in range(len(polymer_template) - 1)])
    for step in range(1, num_steps + 1):
        new_pairs_polymer = Counter()
        for pair in pairs_polymer:
            left, right = pair
            mid = pair_insertions_dict[pair]
            new_pairs_polymer[left + mid] += pairs_polymer[pair]
            new_pairs_polymer[mid + right] += pairs_polymer[pair]
        pairs_polymer = new_pairs_polymer
    return pairs_polymer


def get_most_least_element(polymer_template, pair_insertions_dict, num_steps):
    pairs_polymer = get_pairs_polymer(polymer_template, pair_insertions_dict, num_steps)
    char_counter = Counter()
    for pair in pairs_polymer:
        left, right = pair
        char_counter[left] += pairs_polymer[pair]
    char_counter[polymer_template[-1]] += 1
    return max(char_counter.values()), min(char_counter.values())


def get_result_polymer_template(most_element, least_element):
    return most_element - least_element


if __name__ == "__main__":
    polymer_template, pair_insertions_dict = read_file("input.txt")

    most_element, least_element = get_most_least_element(polymer_template, pair_insertions_dict, 10)
    first_solution = get_result_polymer_template(most_element, least_element)
    print(first_solution)

    most_element, least_element = get_most_least_element(polymer_template, pair_insertions_dict, 40)
    second_solution = get_result_polymer_template(most_element, least_element)
    print(second_solution)
