""" Advent of Code Utility Functions """

def read_input_file(filename):
    """ Fetch some file contents in a normal way """
    with open(filename, 'r', encoding="utf-8") as file:
        input_data = file.read().strip()

    return input_data
