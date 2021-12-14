# -*- coding: utf-8 -*-


def get_transparent_paper_from_input(data):
    points, folds = data.split("\n\n")
    points = {tuple(map(int, point.split(","))) for point in points.split("\n")}
    folds = folds.split("\n")
    return points, folds


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_transparent_paper_from_input(data)


def get_total_dots(points, folds, num_step=float("inf")):
    for index, fold in enumerate(folds, 1):
        coord, position = fold.split()[-1].split("=")
        position = int(position)
        for x, y in list(points):
            points.remove((x, y))
            if coord == "x" and x > position:
                x = 2 * position - x
            if coord == "y" and y > position:
                y = 2 * position - y
            points.add((x, y))
        if index == num_step:
            return len(points), points
    return len(points), points


def get_code_to_activate(points, folds, num_step=float("inf")):
    total_dots, points = get_total_dots(points, folds, num_step)
    X, Y = zip(*points)
    code_to_activate = ""
    for y in range(max(Y) + 1):
        if code_to_activate:
            code_to_activate += "\n"
        for x in range(max(X) + 1):
            code_to_activate += "#" if (x, y) in points else " "
    return code_to_activate


if __name__ == "__main__":
    points, folds = read_file("input.txt")

    first_solution, points = get_total_dots(points, folds, 1)
    print(first_solution)

    second_solution = get_code_to_activate(points, folds)
    print(second_solution)
