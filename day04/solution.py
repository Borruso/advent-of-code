# -*- coding: utf-8 -*-


def get_assignments_from_input(data):
    return data.split("\n")


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_assignments_from_input(data)


def get_assignments_range(assignment):
    start_number, end_number = assignment.split("-")
    return range(int(start_number), int(end_number) + 1)


def total_assignments_fully_contain(assignments):
    total_fully_contain = 0
    for assignment in assignments:
        first_elf, second_elf = assignment.split(",")
        first_assignments = set(get_assignments_range(first_elf))
        second_assignments = set(get_assignments_range(second_elf))
        if (
            first_assignments.issubset(second_assignments)
            or second_assignments.issubset(first_assignments)
        ):
            total_fully_contain += 1
    return total_fully_contain


def total_assignments_overlapping(assignments):
    total_overlapping = 0
    for assignment in assignments:
        first_elf, second_elf = assignment.split(",")
        first_assignments = set(get_assignments_range(first_elf))
        second_assignments = set(get_assignments_range(second_elf))
        if any(
            assignment in first_assignments
            for assignment in second_assignments
        ):
            total_overlapping += 1
    return total_overlapping


if __name__ == "__main__":
    assignments = read_file("input.txt")

    first_solution = total_assignments_fully_contain(assignments)
    print(first_solution)

    second_solution = total_assignments_overlapping(assignments)
    print(second_solution)
