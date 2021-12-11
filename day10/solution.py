# -*- coding: utf-8 -*-


def get_chunks_from_input(data):
    lines = data.split("\n")
    return [line for line in lines]


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_chunks_from_input(data)


def get_legal_pairs():
    return {
        "(": ")",
        "{": "}",
        "<": ">",
        "[": "]",
    }


def get_corrupted_symbols(chunks):
    legal_pairs = get_legal_pairs()
    corrupted_symbols = []
    total_chunks = len(chunks)
    while total_chunks >= 0:
        total_chunks -= 1
        open_chunk_symbols = []
        for symbol in chunks[total_chunks]:
            if symbol in legal_pairs.keys():
                open_chunk_symbols.append(symbol)
            elif symbol != legal_pairs[open_chunk_symbols.pop()]:
                corrupted_symbols.append(symbol)
                del chunks[total_chunks]
                break
    return corrupted_symbols, chunks


def get_illegal_pairs_points():
    return {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }


def get_total_syntax_error_score(corrupted_symbols):
    illegal_pairs_points = get_illegal_pairs_points()
    return sum(illegal_pairs_points[corrupted_symbol] for corrupted_symbol in corrupted_symbols)


def get_closing_characters(incomplete_chunks):
    legal_pairs = get_legal_pairs()
    closing_characters = []
    for incomplete_chunk in incomplete_chunks:
        open_chunk_symbols = []
        for symbol in incomplete_chunk:
            if symbol in legal_pairs.keys():
                open_chunk_symbols.append(symbol)
            else:
                open_chunk_symbols.pop()
        finishing_chars = ""
        total_open_chunk_symbols = len(open_chunk_symbols)
        while total_open_chunk_symbols > 0:
            total_open_chunk_symbols -= 1
            finishing_chars += legal_pairs[open_chunk_symbols[total_open_chunk_symbols]]
        closing_characters.append(finishing_chars)
    return closing_characters


def get_value_pairs_points():
    return {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }


def get_middle_score(closing_characters):
    value_pairs_points = get_value_pairs_points()
    total_score_list = []
    for closing_character in closing_characters:
        total_score = 0
        for character in closing_character:
            total_score *= 5
            total_score += value_pairs_points[character]
        total_score_list.append(total_score)
    return sorted(total_score_list)[len(total_score_list) // 2]


if __name__ == "__main__":
    chunks = read_file("input.txt")

    corrupted_symbols, incomplete_chunks = get_corrupted_symbols(chunks)
    first_solution = get_total_syntax_error_score(corrupted_symbols)
    print(first_solution)

    corrupted_symbols, incomplete_chunks = get_corrupted_symbols(chunks)
    closing_characters = get_closing_characters(incomplete_chunks)
    second_solution = get_middle_score(closing_characters)
    print(second_solution)
