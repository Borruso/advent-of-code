# -*- coding: utf-8 -*-

from collections import defaultdict
from heapq import heappush, heappop


def get_diagram_from_input(data):
    return data.split("\n")


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_diagram_from_input(data)


def get_state_from_diagram(diagram):
    state = defaultdict(set)
    for y, line in enumerate(diagram):
        for x, char in enumerate(line):
            if char in "ABCD":
                state[char].add((x, y))
    return tuple(pos for char in "ABCD" for pos in sorted(state[char]))


def perfrom_amphipod_in_room(x, y, positions, rooms, char, state, num_lines, hallway, new):
    if (x, y - 1) in positions:
        return False

    if rooms[char] == x:
        if all(
                (x, y_) in positions
                and char == "ABCD"[state.index((x, y_)) // num_lines]
                for y_ in range(y + 1, num_lines + 2)
        ):
            return False

    left_hallway = hallway[hallway.index(x - 1):: -1]
    right_hallway = hallway[hallway.index(x + 1):]
    for hallway_ in (left_hallway, right_hallway):
        for x_ in hallway_:
            if (x_, 1) in positions:
                break
            new.append((x_, 1))
    return new


def perfrom_amphipod_in_hallway(num_lines, rooms, char, positions, state, x, new):
    skip = False
    for y_ in range(num_lines + 1, 1, -1):
        if (rooms[char], y_) in positions:
            c_ = "ABCD"[state.index((rooms[char], y_)) // num_lines]
            if c_ != char:
                skip = True
                break
        else:
            break
    if skip:
        return False
    if x < rooms[char]:
        hallway_ = range(x + 1, rooms[char] + 1)
    else:
        hallway_ = range(x - 1, rooms[char] - 1, - 1)
    for x_ in hallway_:
        if (x_, 1) in positions:
            break
    else:
        assert rooms[char] == x_
        new.append((x_, y_))
    return new


def get_least_energy_organize_amphipods(diagram, num_lines):
    state = get_state_from_diagram(diagram)
    rooms = {"A": 3, "B": 5, "C": 7, "D": 9}
    hallway = [1, 2, 4, 6, 8, 10, 11]
    seen = {state: 0}
    visit = list([(0, state)])
    while visit:
        _, state = heappop(visit)
        cost = seen[state]
        if state == tuple((i, j) for i in range(3, 10, 2) for j in range(2, num_lines + 2)):
            return cost
        positions = set(state)
        for i in range(len(state)):
            new = []
            char = "ABCD"[i // num_lines]
            x, y = state[i]
            if y != 1:
                response = perfrom_amphipod_in_room(x, y, positions, rooms, char, state, num_lines, hallway, new)
                if response is False:
                    continue
                else:
                    new = response
            else:
                response = perfrom_amphipod_in_hallway(num_lines, rooms, char, positions, state, x, new)
                if response is False:
                    continue
                else:
                    new = response

            L = i // num_lines * num_lines
            R = L + num_lines
            left = state[:L]
            right = state[R:]
            mid = state[L:R]
            for x_, y_ in new:
                my_amphipods = tuple(sorted(tuple(xy for xy in mid if xy != (x, y)) + ((x_, y_),)))
                state_ = left + my_amphipods + right
                move_cost = pow(10, "ABCD".index(char))
                new_cost = cost + (abs(x - x_) + abs(y - y_)) * move_cost
                if state_ not in seen or seen[state_] > new_cost:
                    seen[state_] = new_cost
                    heappush(visit, (new_cost, state_))


if __name__ == "__main__":
    diagram = read_file("input.txt")

    first_solution = get_least_energy_organize_amphipods(diagram, num_lines=2)
    print(first_solution)

    new_diagram = diagram[:3] + ["  #D#C#B#A#", "  #D#B#A#C#"] + diagram[3:]
    second_solution = get_least_energy_organize_amphipods(new_diagram, num_lines=4)
    print(second_solution)
