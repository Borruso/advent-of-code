# -*- coding: utf-8 -*-


def get_datastream_buffer_from_input(data):
    return data


def read_file(filename):
    with open(filename) as file:
        data = file.read()
    return get_datastream_buffer_from_input(data)


def find_first_start_packet_marker(datastream_buffer, char_size):
    lo_range = range(0, len(datastream_buffer), 1)
    hi_range = range(char_size, len(datastream_buffer) + char_size, 1)
    markers = set()
    for i, j in zip(lo_range, hi_range):
        markers.update(list(datastream_buffer[i:j]))
        if len(markers) == char_size:
            return i + char_size
        else:
            markers = set()


if __name__ == "__main__":
    datastream_buffer = read_file("input.txt")

    first_solution = find_first_start_packet_marker(datastream_buffer, char_size=4)
    print(first_solution)

    second_solution = find_first_start_packet_marker(datastream_buffer, char_size=14)
    print(second_solution)
