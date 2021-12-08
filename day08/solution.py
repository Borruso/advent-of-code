# -*- coding: utf-8 -*-


def get_segments_from_input(data):
    lines = data.split("\n")
    return [line for line in lines]


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_segments_from_input(data)


def get_total_digits_unique(segments):
    total_digits_appear = 0
    for segment in segments:
        digit_output_value = segment.split(" | ")[1]
        for word in digit_output_value.split():
            if len(word) in [2, 3, 4, 7]:
                total_digits_appear += 1
    return total_digits_appear


def get_digits_from_patterns(unique_signal_patterns, digits_output_value):
    digits = {}
    digits_patterns_dict = {}
    for i in range(len(unique_signal_patterns)):
        if len(unique_signal_patterns[i]) == 2:
            digits[1] = set(unique_signal_patterns[i])
        if len(unique_signal_patterns[i]) == 4:
            digits[4] = set(unique_signal_patterns[i])
        if len(unique_signal_patterns[i]) == 3:
            digits[7] = set(unique_signal_patterns[i])
        if len(unique_signal_patterns[i]) == 7:
            digits[8] = set(unique_signal_patterns[i])

    digits_patterns_dict["a"] = digits[7] - digits[1]

    digits[9] = [
        set(pattern)
        for pattern in unique_signal_patterns
        if len(pattern) == 6 and len(set(pattern) - (digits[4] | digits_patterns_dict["a"])) == 1
    ][0]
    digits_patterns_dict["g"] = digits[8] - digits[9]

    digits_patterns_dict["e"] = [
        digits[8] - set(pattern)
        for pattern in unique_signal_patterns
        if len(pattern) == 6 and len(set(pattern) - (digits[4] | digits_patterns_dict["a"])) == 1
    ][0]

    digits[0] = [
        set(x)
        for x in unique_signal_patterns
        if len(x) == 6 and len(set(x) & (digits[1] | digits_patterns_dict["e"])) == 3
    ][0]
    digits_patterns_dict["d"] = digits[8] - digits[0]

    digits_patterns_dict["b"] = digits[4] - (digits[1] | digits_patterns_dict["d"])

    digits[6] = [
        set(x)
        for x in unique_signal_patterns
        if len(x) == 6 and set(x) not in [digits[0], digits[9]]
    ][0]
    digits_patterns_dict["c"] = digits[8] - digits[6]
    digits_patterns_dict["f"] = digits[1] - digits_patterns_dict["c"]

    digits[5] = digits[8] - (digits_patterns_dict["c"] | digits_patterns_dict["e"])

    digits[2] = digits[8] - (digits_patterns_dict["b"] | digits_patterns_dict["f"])
    digits[3] = digits[8] - (digits_patterns_dict["b"] | digits_patterns_dict["e"])

    output = ""
    for d in digits_output_value:
        for k, v in digits.items():
            if set(d) == v:
                output += str(k)
                break

    return int(output)


def get_total_digits(segments):
    total_digits_appear = 0
    for segment in segments:
        unique_signal_patterns, digits_output_value = segment.split(" | ")
        unique_signal_patterns = unique_signal_patterns.split()
        digits_output_value = digits_output_value.split()
        total_digits_appear += get_digits_from_patterns(unique_signal_patterns, digits_output_value)
    return total_digits_appear


if __name__ == "__main__":
    segments = read_file("input.txt")

    first_solution = get_total_digits_unique(segments)
    print(first_solution)

    second_solution = get_total_digits(segments)
    print(second_solution)
