# -*- coding: utf-8 -*-

def get_monad_from_input(data):
    return data.split("inp w\n")[1:]


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_monad_from_input(data)


def get_largest_model_number_accepted(MONAD):
    z = []
    max_monad = [0] * 14
    for i, instructions_to_perform in enumerate(MONAD):
        instructions = instructions_to_perform.split("\n")
        pop = int(instructions[3][-2:]) == 26
        x_add = int(instructions[4].split()[-1])
        y_add = int(instructions[14].split()[-1])
        if not pop:
            z.append((i, y_add))
        else:
            j, y_add = z.pop()
            difference = x_add + y_add
            if difference < 0:
                max_monad[i] = 9 + difference
                max_monad[j] = 9
            elif difference > 0:
                max_monad[i] = 9
                max_monad[j] = 9 - difference
            else:
                max_monad[i] = max_monad[j] = 9
    return "".join(map(str, max_monad))


def get_smallest_model_number_accepted(MONAD):
    z = []
    min_monad = [0] * 14
    for i, instructions_to_perform in enumerate(MONAD):
        instructions = instructions_to_perform.split("\n")
        pop = int(instructions[3][-2:]) == 26
        x_add = int(instructions[4].split()[-1])
        y_add = int(instructions[14].split()[-1])
        if not pop:
            z.append((i, y_add))
        else:
            j, y_add = z.pop()
            difference = x_add + y_add
            if difference < 0:
                min_monad[i] = 1
                min_monad[j] = 1 - difference
            elif difference > 0:
                min_monad[i] = 1 + difference
                min_monad[j] = 1
            else:
                min_monad[i] = min_monad[j] = 1
    return "".join(map(str, min_monad))


if __name__ == "__main__":
    MONAD = read_file("input.txt")

    first_solution = get_largest_model_number_accepted(MONAD)
    print(first_solution)

    second_solution = get_smallest_model_number_accepted(MONAD)
    print(second_solution)
