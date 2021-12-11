# -*- coding: utf-8 -*-


def get_heightmap_from_input(data):
    lines = data.split("\n")
    lines = [line for line in lines]
    heightmap = {}
    for y, line in enumerate(lines):
        for x, height in enumerate(line):
            heightmap[(x, y)] = int(height)
    return heightmap


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_heightmap_from_input(data)


def get_low_points(heightmap):
    low_points = []
    coords_low_points = []
    for coords, height in heightmap.items():
        x, y = coords
        adjacent = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        lowest = True
        for neighbour in adjacent:
            if heightmap.get(neighbour, 10) <= height:
                lowest = False
                break
        if lowest:
            low_points.append(height)
            coords_low_points.append(coords)
    return low_points, coords_low_points


def get_total_risk_levels(low_points):
    return sum(low_point + 1 for low_point in low_points)


def get_size_largest_basins(coords_low_points, heightmap):
    size_basins = []
    for coords_low_point in coords_low_points:
        coords_of_basin = {coords_low_point}
        coords_to_check = [coords_low_point]
        while coords_to_check:
            x, y = coords_to_check.pop()
            adjacent = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
            for neighbour in adjacent:
                neighbour_height = heightmap.get(neighbour, 0)
                if neighbour_height > heightmap[(x, y)] and neighbour_height != 9:
                    coords_of_basin.add(neighbour)
                    coords_to_check.append(neighbour)
        size_basins.append(len(coords_of_basin))
    size_basins.sort(reverse=True)
    return size_basins


def get_multiply_largest_basins(size_largest_basins, number):
    multiply_largest_basins = 1
    for size_largest_basin in size_largest_basins[:number]:
        multiply_largest_basins *= size_largest_basin
    return multiply_largest_basins


if __name__ == "__main__":
    heightmap = read_file("input.txt")

    low_points, coords_low_points = get_low_points(heightmap)
    first_solution = get_total_risk_levels(low_points)
    print(first_solution)

    low_points, coords_low_points = get_low_points(heightmap)
    size_largest_basins = get_size_largest_basins(coords_low_points, heightmap)
    second_solution = get_multiply_largest_basins(size_largest_basins, number=3)
    print(second_solution)
