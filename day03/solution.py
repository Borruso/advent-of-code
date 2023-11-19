# -*- coding: utf-8 -*-

import itertools


def get_rucksacks_from_input(data):
    return data.split("\n")


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_rucksacks_from_input(data)


def get_priority(first_compartment, second_compartment):
    return set(first_compartment).intersection(set(second_compartment))


def get_value_priority(priority):
    if 65 <= ord(priority) <= 90:
        return ord(priority) - 64 + 26
    elif 97 <= ord(priority) <= 122:
        return ord(priority) - 96
    else:
        print("No manage this priority")
        return 0


def total_rucksacks_priorities(rucksacks):
    total_score = 0
    for rucksack in rucksacks:
        half_length = len(rucksack) // 2
        first_compartment = rucksack[:half_length]
        second_compartment = rucksack[half_length:]
        priorities = get_priority(first_compartment, second_compartment)
        for priority in priorities:
            total_score += get_value_priority(priority)
    return total_score


def divide_chunks(rucksacks, elves_group):
    for i in range(0, len(rucksacks), elves_group):
        yield rucksacks[i:i + elves_group]


def total_elf_groups_priorities(rucksacks, elves_group):
    total_score = 0
    elf_groups_rucksacks = divide_chunks(rucksacks, elves_group)
    for elf_groups_rucksack in elf_groups_rucksacks:
        priorities = set()
        previous_elf_group_rucksack = ""
        for elf_group_rucksack in elf_groups_rucksack:
            if not previous_elf_group_rucksack:
                previous_elf_group_rucksack = elf_group_rucksack
                continue
            priorities = get_priority(previous_elf_group_rucksack, elf_group_rucksack)
            previous_elf_group_rucksack = "".join(filter(None, priorities))
        for priority in priorities:
            total_score += get_value_priority(priority)
    return total_score


if __name__ == "__main__":
    rucksacks = read_file("input.txt")

    first_solution = total_rucksacks_priorities(rucksacks)
    print(first_solution)

    second_solution = total_elf_groups_priorities(rucksacks, 3)
    print(second_solution)
