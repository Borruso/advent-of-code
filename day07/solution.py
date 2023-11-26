# -*- coding: utf-8 -*-

from dataclasses import dataclass


@dataclass
class File:
    name: str
    size: int

    def __add__(self, other):
        return self.size + other.size

    def __radd__(self, other):
        return self.size.__add__(other)


def get_commands_from_input(data):
    data = data.split("\n")
    return list(map(lambda x: x.strip().split(" "), data))


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_commands_from_input(data)


def run_commands(commands):
    directories = {}
    path = ["/"]
    joined_path = ""

    for command in commands:
        if "$" and "cd" in command:
            _, _, directory = command
            if directory == "/":
                path = ["/"]
            elif directory == '..':
                path.pop()
            else:
                path.append(directory)

            joined_path = "/".join(path)
            joined_path += "/"
            joined_path = joined_path[1:]
            if joined_path not in directories.keys():
                directories[joined_path] = list()

        if command[0].isnumeric():
            file_size, file_name = command
            file = File(file_name, int(file_size))
            directories[joined_path].append(file)

    return directories


def get_directories_sizes(directories):
    for key in directories.keys():
        directories[key] = sum(directories[key])

    for key in directories.keys():
        for key2 in directories.keys():
            if key2.startswith(key) and key2 != key:
                directories[key] += directories[key2]

    return directories


def total_sizes_directories(commands, size):
    directories = run_commands(commands)
    directories_sizes = get_directories_sizes(directories)

    size_filtered = {k: v for k, v in directories_sizes.items() if v <= size}
    total_sizes = sum(size_filtered.values())

    return total_sizes


def total_size_smallest_directory(commands, disk_space, space_need):
    directories = run_commands(commands)
    directories_sizes = get_directories_sizes(directories)

    free_space = disk_space - directories_sizes["/"]
    size_filtered = {k: v for k, v in directories_sizes.items() if free_space + v >= space_need}
    smallest_directory = min(size_filtered.values())

    return smallest_directory


if __name__ == "__main__":
    commands = read_file("input.txt")

    first_solution = total_sizes_directories(commands, size=100000)
    print(first_solution)

    second_solution = total_size_smallest_directory(
        commands, disk_space=70000000, space_need=30000000
    )
    print(second_solution)
