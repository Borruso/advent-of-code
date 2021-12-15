# -*- coding: utf-8 -*-
from heapq import heappop, heappush


def get_map_risk_level_from_input(data):
    lines = data.split("\n")
    return [list(map(int, line)) for line in lines]


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_map_risk_level_from_input(data)


def get_neighbour_coords(x, y):
    return [[x + nx, y + ny] for nx, ny in [(1, 0), (0, 1), (-1, 0), (0, -1)]]


def get_lowest_total_risk(map_risk_level, num_path):
    heap = [(0, 0, 0)]
    position_checked = {(0, 0)}
    while heap:
        distance, x, y = heappop(heap)
        if x == num_path * len(map_risk_level) - 1 and y == num_path * len(map_risk_level[0]) - 1:
            return distance

        for neighbour_x, neighbour_y in get_neighbour_coords(x, y):
            if neighbour_x < 0 or neighbour_y < 0 \
                    or neighbour_x >= num_path * len(map_risk_level) or neighbour_y >= num_path * len(map_risk_level):
                continue

            quotient_x, remainder_x = divmod(neighbour_x, len(map_risk_level))
            quotient_y, remainder_y = divmod(neighbour_y, len(map_risk_level[0]))
            n = ((map_risk_level[remainder_x][remainder_y] + quotient_x + quotient_y) - 1) % 9 + 1

            if (neighbour_x, neighbour_y) not in position_checked:
                position_checked.add((neighbour_x, neighbour_y))
                heappush(heap, (distance + n, neighbour_x, neighbour_y))


if __name__ == "__main__":
    map_risk_level = read_file("input.txt")

    first_solution = get_lowest_total_risk(map_risk_level, num_path=1)
    print(first_solution)

    second_solution = get_lowest_total_risk(map_risk_level, num_path=5)
    print(second_solution)
