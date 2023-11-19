# -*- coding: utf-8 -*-

def get_matches_from_input(data):
    return data.split("\n")


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_matches_from_input(data)


def get_value_strategy1(me_play, opponent_play):
    if me_play == "X":
        if opponent_play == "A":
            return 3
        elif opponent_play == "B":
            return 0
        else:
            return 6
    elif me_play == "Y":
        if opponent_play == "A":
            return 6
        elif opponent_play == "B":
            return 3
        else:
            return 0
    else:
        if opponent_play == "A":
            return 0
        elif opponent_play == "B":
            return 6
        else:
            return 3


def get_value_strategy2(me_play):
    if me_play == "X":
        return 0
    elif me_play == "Y":
        return 3
    else:
        return 6


def get_match_result(me_play, opponent_play, strategy):
    if strategy == 1:
        return get_value_strategy1(me_play, opponent_play)
    elif strategy == 2:
        return get_value_strategy2(me_play)
    else:
        print("No manager this strategy")
        return 0


def get_sign_value(sign):
    return {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3,
    }[sign]


def get_sign_from_play(me_play, opponent_play):
    if opponent_play == "A":
        if me_play == "X":
            return "Z"
        elif me_play == "Y":
            return "X"
        else:
            return "Y"
    elif opponent_play == "B":
        if me_play == "X":
            return "X"
        elif me_play == "Y":
            return "Y"
        else:
            return "Z"
    else:
        if me_play == "X":
            return "Y"
        elif me_play == "Y":
            return "Z"
        else:
            return "X"


def get_value_play(me_play, opponent_play, strategy):
    if strategy == 1:
        return get_sign_value(me_play)
    elif strategy == 2:
        sign = get_sign_from_play(me_play, opponent_play)
        return get_sign_value(sign)
    else:
        print("No manager this strategy")
        return 0


def total_score_strategy_guide(matches, strategy):
    opponent_plays = [
        match[0]
        for match in matches
    ]
    me_plays = [
        match[-1]
        for match in matches
    ]
    total_score = 0
    for me_play, opponent_play in zip(me_plays, opponent_plays):
        result = get_match_result(me_play, opponent_play, strategy)
        me_play_value = get_value_play(me_play, opponent_play, strategy)
        total_score += result + me_play_value
    return total_score


if __name__ == "__main__":
    matches = read_file("input.txt")

    first_solution = total_score_strategy_guide(matches, 1)
    print(first_solution)

    second_solution = total_score_strategy_guide(matches, 2)
    print(second_solution)
