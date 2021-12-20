# -*- coding: utf-8 -*-

from itertools import count


def get_algorithm_image_from_input(data):
    enhancement_algorithm, input_image = data.split("\n\n")
    return enhancement_algorithm, input_image


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_algorithm_image_from_input(data)


def get_image_coords(input_image):
    image_coords = set()
    for y, row in enumerate(input_image.split("\n")):
        for x, pixel in enumerate(row):
            if pixel == "#":
                image_coords.add((x, y))
    return image_coords


def get_nine_pixels_marked(x, y):
    return [
        (x - 1, y - 1), (x + 0, y - 1), (x + 1, y - 1),
        (x - 1, y + 0), (x + 0, y + 0), (x + 1, y + 0),
        (x - 1, y + 1), (x + 0, y + 1), (x + 1, y + 1),
    ]


def get_total_lit_pixels(enhancement_algorithm, image_coords, steps):
    for step in count(1):
        new_image = set()
        minx = min(x for x, y in image_coords)
        maxx = max(x for x, y in image_coords)
        miny = min(y for x, y in image_coords)
        maxy = max(y for x, y in image_coords)
        for y in range(miny - 2, maxy + 2):
            for x in range(minx - 2, maxx + 2):
                binary = 0
                for b in range(3):
                    for a in range(3):
                        if (x + a, y + b) in image_coords:
                            binary += pow(2, (2 - b) * 3 + (2 - a))
                        elif enhancement_algorithm[0] == "#" and step % 2 == 0:
                            if (x + a) < minx or (x + a) > maxx:
                                binary += pow(2, (2 - b) * 3 + (2 - a))
                            elif (y + b) < miny or (y + b) > maxy:
                                binary += pow(2, (2 - b) * 3 + (2 - a))
                if enhancement_algorithm[binary] == "#":
                    new_image.add((x + 1, y + 1))
        image_coords = new_image
        if step == steps:
            return len(image_coords)


if __name__ == "__main__":
    enhancement_algorithm, input_image = read_file("input.txt")

    image_coords = get_image_coords(input_image)
    first_solution = get_total_lit_pixels(enhancement_algorithm, image_coords, steps=2)
    print(first_solution)

    second_solution = get_total_lit_pixels(enhancement_algorithm, image_coords, steps=50)
    print(second_solution)
