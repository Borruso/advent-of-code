# -*- coding: utf-8 -*-


def get_binary_value_from_input(data):
    return bin(int(data, 16))[2:].zfill(len(data) * 4)


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_binary_value_from_input(data)


def get_sum_version_numbers(binary_value, start_index):
    version = int(binary_value[start_index:(start_index + 3)], 2)
    type_id = int(binary_value[(start_index + 3):(start_index + 6)], 2)
    if type_id == 4:
        start_index += 6
        while binary_value[start_index] == "1":
            start_index += 5
        return start_index + 4, version
    length_type = int(binary_value[start_index + 6])
    if length_type == 0:
        sub_length = int(binary_value[(start_index + 7):(start_index + 7 + 15)], 2)
        start_index += 7 + 15
        finish_index = start_index
        sum_version = version
        while finish_index != start_index + sub_length:
            finish_index, new_version = get_sum_version_numbers(binary_value, finish_index)
            finish_index += 1
            sum_version += new_version
        return finish_index - 1, sum_version
    else:
        sub_count = int(binary_value[(start_index + 7):(start_index + 7 + 11)], 2)
        start_index += 7 + 11
        finish_index = start_index
        sum_version = version
        while sub_count:
            sub_count -= 1
            finish_index, new_version = get_sum_version_numbers(binary_value, finish_index)
            finish_index += 1
            sum_version += new_version
        return finish_index - 1, sum_version


def get_value_expression(binary_value, start_index):
    version = int(binary_value[start_index:(start_index + 3)], 2)
    type_id = int(binary_value[(start_index + 3):(start_index + 6)], 2)
    if type_id == 4:
        start_index += 6
        value = ""
        while binary_value[start_index] == "1":
            value += binary_value[(start_index + 1):(start_index + 5)]
            start_index += 5
        value += binary_value[(start_index + 1):(start_index + 5)]
        return start_index + 4, int(value, 2)
    length_type = int(binary_value[start_index + 6])
    list_values = []
    if length_type == 0:
        sub_length = int(binary_value[(start_index + 7):(start_index + 7 + 15)], 2)
        start_index += 7 + 15
        finish_index = start_index
        result = version
        while finish_index != start_index + sub_length:
            finish_index, new_value = get_value_expression(binary_value, finish_index)
            finish_index += 1
            result += new_value
            list_values += [new_value]
    else:
        sub_count = int(binary_value[(start_index + 7):(start_index + 7 + 11)], 2)
        start_index += 7 + 11
        finish_index = start_index
        result = version
        while sub_count:
            sub_count -= 1
            finish_index, new_value = get_value_expression(binary_value, finish_index)
            finish_index += 1
            result += new_value
            list_values += [new_value]
    result = 0
    if type_id == 0:
        result = sum(list_values)
    if type_id == 1:
        result = 1
        for value in list_values:
            result *= value
    if type_id == 2:
        result = min(list_values)
    if type_id == 3:
        result = max(list_values)
    if type_id == 5:
        result = list_values[0] > list_values[1]
    if type_id == 6:
        result = list_values[0] < list_values[1]
    if type_id == 7:
        result = list_values[0] == list_values[1]
    return finish_index - 1, result


if __name__ == "__main__":
    binary_value = read_file("input.txt")

    finish_index, first_solution = get_sum_version_numbers(binary_value, start_index=0)
    print(first_solution)

    finish_index, second_solution = get_value_expression(binary_value, start_index=0)
    print(second_solution)
