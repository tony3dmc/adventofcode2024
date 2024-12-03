""" Advent of Code - Day 3: Mull It Over """
import re
from . import utils

def part1(puzzle_input):
    """ Solution for part 1: Calculate the sum of our mul operations across the puzzle input """
    return calculate_mul_expressions(puzzle_input)

def part2(puzzle_input):
    """ Solution for part 2: Remove instructions between don't() and do() chunks """
    puzzle_input = remove_invalid_chunks(puzzle_input)
    return calculate_mul_expressions(puzzle_input)

def calculate_mul_expressions(string):
    """ Return the sum of the mul() operations """
    matches = re.findall(r'mul\((\d+),(\d+)\)', string)
    return sum(int(x) * int(y) for x, y in matches)

def remove_invalid_chunks(string):
    """ Remove chunks between don't() and do(), plus anything after the last don't() """
    string = re.sub(r'don\'t\(\).*?do\(\)', '', string)
    string = re.sub(r'don\'t\(\).*$', '', string)
    return string

def main():
    """ Run the solutions """
    puzzle_input = "".join(utils.read_input_lines('inputs/day03_input.txt'))
    result = part1(puzzle_input)
    print(f"Solution to part 1: {result}")

    result = part2(puzzle_input)
    print(f"Solution to part 2: {result}")

if __name__ == '__main__':
    main()
