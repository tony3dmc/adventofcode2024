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
            numbers.append(int(number))

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

def numbers_changing_in_same_direction(numbers):
    """ How many numbers in a list are increasing or decreasing in the same direction """
    if len(numbers) <= 1:
        return numbers

    directions = {-1: 0, 0: 0, 1: 0}
    for i, number in enumerate(numbers):
        if i == 0:
            continue

        direction = get_direction_between(number, numbers[i - 1])
        directions[direction] += 1

    longest_direction = max(directions, key=directions.get)
    return directions[longest_direction]

def get_direction_between(number1, number2):
    """ Are these numbers increasing, decreasing or the same? """
    if number1 == number2:
        return 0
    if number1 > number2:
        return 1
    return -1

def largest_gap(numbers):
    """ Find the largest gap between two sequential numbers in a list """
    max_gap = 0
    for i, number in enumerate(numbers):
        if i == 0:
            continue
        gap = abs(number - numbers[i - 1])
        max_gap = max(max_gap, gap)

    return max_gap
