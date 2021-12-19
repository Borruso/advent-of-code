# -*- coding: utf-8 -*-
from itertools import starmap, cycle


def get_scanners_from_input(data):
    return [set(tuple(map(int, line.split(","))) for line in scanner.split("\n")[1:]) for scanner in data.split("\n\n")]


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_scanners_from_input(data)


def get_negations():
    return [
        lambda x, y, z: (x, y, z),
        lambda x, y, z: (-x, y, z),
        lambda x, y, z: (x, -y, z),
        lambda x, y, z: (x, y, -z),
        lambda x, y, z: (-x, -y, z),
        lambda x, y, z: (-x, y, -z),
        lambda x, y, z: (x, -y, -z),
        lambda x, y, z: (-x, -y, -z),
    ]


def get_rotations():
    return [
        lambda x, y, z: (x, y, z),
        lambda x, y, z: (x, z, y),
        lambda x, y, z: (z, y, x),
        lambda x, y, z: (y, x, z),
        lambda x, y, z: (y, z, x),
        lambda x, y, z: (z, x, y),
    ]


def get_total_beacons(scanners):
    scanner_positions = [(0, 0, 0)] * len(scanners)
    found = [-1] * len(scanners)
    done = len(found) - 1
    found[0] = 0
    for index in cycle(range(len(scanners))):
        if done == 0:
            break
        if found[index] == -1:
            continue
        for scanner in range(len(scanners)):
            if scanner == index or found[scanner] != -1:
                continue
            for negate in get_negations():
                if found[scanner] != -1:
                    break
                for rotate in get_rotations():
                    if found[scanner] != -1:
                        break
                    new_scanner = set(starmap(negate, starmap(rotate, scanners[scanner])))
                    for scanner_x, scanner_y, scanner_z in scanners[index]:
                        if found[scanner] != -1:
                            break
                        for new_scanner_x, new_scanner_y, new_scanner_z in new_scanner:
                            if found[scanner] != -1:
                                break
                            dx, dy, dz = scanner_x - new_scanner_x, scanner_y - new_scanner_y, scanner_z - new_scanner_z
                            moved = set((x + dx, y + dy, z + dz) for x, y, z in new_scanner)
                            if len(scanners[index].intersection(moved)) >= 12:
                                scanners[scanner] = moved
                                found[scanner] = found[index]
                                scanner_positions[scanner] = (dx, dy, dz)
                                done -= 1
                                break
    return scanner_positions, len(set.union(*scanners))


def get_largest_distance_between_scanner(scanner_positions):
    max_distance = 0
    for x1, y1, z1 in scanner_positions:
        for x2, y2, z2 in scanner_positions:
            max_distance = max(max_distance, abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2))
    return max_distance


if __name__ == "__main__":
    scanners = read_file("input.txt")

    scanner_positions, first_solution = get_total_beacons(scanners)
    print(first_solution)

    second_solution = get_largest_distance_between_scanner(scanner_positions)
    print(second_solution)
