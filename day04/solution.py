# -*- coding: utf-8 -*-

def get_numbers_from_input(data):
    lines = data.split(",")
    return [line for line in lines]


def read_file_numbers(filename):
    with open(filename) as file:
        data = file.read()
    return get_numbers_from_input(data)


def get_matrices_from_lines(lines, height):
    matrix = []
    matrices = []
    for index in range(len(lines)):
        split_line = lines[index].split(" ")
        matrix.append([item for item in split_line if item != ""])
        if len(matrix) == height:
            matrices.append(matrix)
            matrix = []
    return matrices


def get_boards_from_input(data, height):
    lines = data.split("\n")
    clear_lines = [lines[index] for index in range(len(lines)) if lines[index] != ""]
    matrices = get_matrices_from_lines(clear_lines, height)
    return matrices


def read_file_boards(filename, height):
    with open(filename) as file:
        data = file.read()
    return get_boards_from_input(data, height)


def check_number_in_boards(boards, number):
    for board in boards:
        for row in board:
            for index in range(len(row)):
                if row[index] == number:
                    row[index] = row[index] + "*"


def check_board_row(board, width):
    for row in board:
        numbers_found = 0
        for item in row:
            if any(char == "*" for char in item):
                numbers_found += 1
                if numbers_found == width:
                    return True
            else:
                continue
    return False


def check_board_column(board, height, width):
    for w in range(width):
        column = 0
        for h in range(height):
            if any(char == "*" for char in board[h][w]):
                column += 1
                if column == height:
                    return True
            else:
                continue
    return False


def check_new_wins_board(wins_boards, board):
    for wins_board in wins_boards:
        if wins_board == board:
            return False
    return True


def check_wins(boards, wins_boards, height, width, check):
    wins_found = 0
    new_wins_boards = []
    for board in boards:
        row = check_board_row(board, width)
        column = check_board_column(board, height, width)
        if row or column:
            wins_found += 1
            if not wins_boards:
                wins_boards.append(board)
            else:
                if check == "last":
                    if check_new_wins_board(wins_boards, board):
                        new_wins_boards.append(board)
                        wins_boards.append(board)
                else:
                    wins_boards.append(board)
    return wins_found, wins_boards, new_wins_boards


def get_unmarked_numbers(wins_boards):
    unmarked_numbers = []
    for board in wins_boards:
        for row in board:
            for item in row:
                if all(char != "*" for char in item):
                    unmarked_numbers.append(int(item))
                else:
                    continue
    return unmarked_numbers


def get_sum_unmarked_numbers(numbers, boards, wins, height, width, check=None):
    sum_unmarked_numbers = 0
    last_number = 0
    wins_boards = []
    previous_wins_found = 0
    for number in numbers:
        check_number_in_boards(boards, number)
        wins_found, wins_boards, new_wins_boards = check_wins(boards, wins_boards, height, width, check)
        if previous_wins_found != wins_found:
            if check == "last":
                if not new_wins_boards:
                    new_wins_boards = wins_boards
                unmarked_numbers = get_unmarked_numbers(new_wins_boards)
            else:
                unmarked_numbers = get_unmarked_numbers(wins_boards)
            sum_unmarked_numbers = sum(unmarked_numbers)
            last_number = int(number)
            previous_wins_found = wins_found
        if wins != "unlimited" and wins_found == wins:
            break
    return sum_unmarked_numbers, last_number


def get_final_score(sum_unmarked_numbers, last_number):
    return sum_unmarked_numbers * last_number


if __name__ == "__main__":
    numbers = read_file_numbers("numbers.txt")
    boards = read_file_boards("boards.txt", height=5)

    sum_unmarked_numbers, last_number = get_sum_unmarked_numbers(numbers, boards, wins=1, height=5, width=5)
    first_solution = get_final_score(sum_unmarked_numbers, last_number)
    print(first_solution)

    sum_last_unmarked_numbers, last_number = get_sum_unmarked_numbers(numbers, boards, wins="unlimited", height=5,
                                                                      width=5, check="last")
    second_solution = get_final_score(sum_last_unmarked_numbers, last_number)
    print(second_solution)
