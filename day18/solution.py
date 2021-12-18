# -*- coding: utf-8 -*-


def parse(line):
    result = []
    for char in line:
        try:
            result.append(int(char))
        except ValueError:
            result.append(char)
    return result


def get_snailfish_numbers_from_input(data):
    return [parse(line.strip()) for line in data.split("\n")]


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_snailfish_numbers_from_input(data)


def add_numbers(num1, num2):
    return ["["] + num1 + [","] + num2 + ["]"]


def check_need_to_explode(snailfish_number):
    pairs = 0
    for i in snailfish_number:
        if i == "[":
            pairs += 1
        elif i == "]":
            pairs -= 1
        if pairs > 4:
            return True
    return False


def perform_explode(snailfish_number):
    pairs = 0
    for index, char in enumerate(snailfish_number):
        if char == "[":
            pairs += 1
        elif char == "]":
            pairs -= 1
        if pairs > 4:
            left = snailfish_number[index + 1]
            right = snailfish_number[index + 3]
            left_index = index - 1
            while left_index > 0:
                if type(snailfish_number[left_index]) is int:
                    snailfish_number[left_index] += left
                    break
                left_index -= 1
            right_index = index + 5
            while right_index < len(snailfish_number) - 1:
                if type(snailfish_number[right_index]) is int:
                    snailfish_number[right_index] += right
                    break
                right_index += 1
            for _ in range(5):
                snailfish_number.pop(index)
            snailfish_number.insert(index, 0)
            return True
    return False


def check_need_to_split(snailfish_number):
    for char in snailfish_number:
        if type(char) is int and char > 9:
            return True


def perform_split(snailfish_number):
    for index, char in enumerate(snailfish_number):
        if type(char) is int and char > 9:
            snailfish_number.pop(index)
            snailfish_number.insert(index, "[")
            snailfish_number.insert(index + 1, char // 2)
            snailfish_number.insert(index + 2, ",")
            snailfish_number.insert(index + 3, (char + 1) // 2)
            snailfish_number.insert(index + 4, "]")
            return True
    return False


def reduce_snailfish_number(snailfish_number):
    reduced = False
    while not reduced:
        if check_need_to_explode(snailfish_number):
            perform_explode(snailfish_number)
        elif check_need_to_split(snailfish_number):
            perform_split(snailfish_number)
        else:
            reduced = True


def get_final_sum(snailfish_numbers):
    final_sum = snailfish_numbers[0]
    for number in snailfish_numbers[1:]:
        final_sum = add_numbers(final_sum, number)
        reduce_snailfish_number(final_sum)
    final_sum_formatted = "".join(str(char) for char in final_sum)
    return final_sum, final_sum_formatted


def get_magnitude_final_sum(final_sum):
    if len(final_sum) == 1:
        return final_sum[0]
    pairs = 0
    middle = 0
    for index, char in enumerate(final_sum):
        if char == "[":
            pairs += 1
        elif char == "]":
            pairs -= 1
        elif char == "," and pairs == 1:
            middle = index
            break
    return 3 * get_magnitude_final_sum(final_sum[1:middle]) + 2 * get_magnitude_final_sum(final_sum[middle + 1:-1])


def get_largest_magnitude_final_sum(snailfish_numbers):
    largest_magnitude = 0
    for index_num1 in range(len(snailfish_numbers)):
        for index_num2 in range(len(snailfish_numbers)):
            if index_num1 == index_num2:
                continue
            final_sum = add_numbers(snailfish_numbers[index_num1], snailfish_numbers[index_num2])
            reduce_snailfish_number(final_sum)
            largest_magnitude = max(largest_magnitude, get_magnitude_final_sum(final_sum))
    return largest_magnitude


if __name__ == "__main__":
    snailfish_numbers = read_file("input.txt")

    final_sum, final_sum_formatted = get_final_sum(snailfish_numbers)
    first_solution = get_magnitude_final_sum(final_sum)
    print(first_solution)

    second_solution = get_largest_magnitude_final_sum(snailfish_numbers)
    print(second_solution)
