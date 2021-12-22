# -*- coding: utf-8 -*-

from itertools import cycle


def get_players_from_input(data):
    player1, player2 = [int(line[-2:]) for line in data.split("\n")]
    return player1, player2


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_players_from_input(data)


def get_deterministic_die():
    return cycle(range(1, 101))


def perform_game(player1, player2, die, score1, score2, throws):
    if score2 >= 1000:
        return score1 * throws
    player1 += sum(next(die) for _ in range(3))
    player1 = (player1 - 1) % 10 + 1
    score1 += player1
    return perform_game(player2, player1, die, score2, score1, throws + 3)


def get_total_points_losing_player(player1, player2, score1=0, score2=0, throws=0):
    deterministic_die = cycle(range(1, 101))
    total_points = perform_game(player1, player2, deterministic_die, score1, score2, throws)
    return total_points


def get_roll_sums():
    three_roll_sums = []
    for one in (1, 2, 3):
        for two in (1, 2, 3):
            for three in (1, 2, 3):
                three_roll_sums.append(one + two + three)
    return three_roll_sums


def get_winner_in_more_universes(player1, player2, score1=0, score2=0):
    three_roll_sums = get_roll_sums()
    player_one_wins = 0
    player_two_wins = 0
    game_initial = (player1 - 1, score1, player2 - 1, score2, 1)
    games = {game_initial: 1}
    while games:
        new_games = {}
        for game, universes in games.items():
            throws = game[4]
            if throws == 1:
                pos, score = game[0], game[1]
            else:
                pos, score = game[2], game[3]
            for roll_sum in three_roll_sums:
                new_position = (pos + roll_sum) % 10
                new_score = score + new_position + 1
                if new_score >= 21:
                    if throws == 1:
                        player_one_wins += universes
                    else:
                        player_two_wins += universes
                else:
                    if throws == 1:
                        new_value = (new_position, new_score, game[2], game[3], 2)
                    else:
                        new_value = (game[0], game[1], new_position, new_score, 1)
                    new_games[new_value] = new_games.get(new_value, 0) + universes
        games = new_games
    return max(player_one_wins, player_two_wins)


if __name__ == "__main__":
    player1, player2 = read_file("input.txt")

    first_solution = get_total_points_losing_player(player1, player2)
    print(first_solution)

    second_solution = get_winner_in_more_universes(player1, player2)
    print(second_solution)
