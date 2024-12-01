""" Advent of Code Utility Functions """

def read_input_lines(filename):
    """ Fetch some file contents in a normal way """
    with open(filename, 'r', encoding="utf-8") as file:
        input_data = file.read().splitlines()

    return input_data

def get_numbers(lines):
    """ Extract all the numbers from lines of text """
    numbers = []
    for line in lines:
        for number in line.split():
            numbers.append(number)

    return numbers

def fetch_columns(lines):
    """ Take a list of rows of two numbers, return two lists of columns """
    numbers = get_numbers(lines)
    lefts = []
    rights = []
    for i in range(int(len(numbers) / 2)):
        lefts.append(int(numbers[i * 2]))
        rights.append(int(numbers[(i * 2) + 1]))

    return [ lefts, rights ]

def frequency_analysis(numbers):
    """ Return a map of keys to frequency of occurrences """
    frequencies = {}
    for n in numbers:
        if n not in frequencies:
            frequencies[n] = 0
        frequencies[n] += 1
    return frequencies
