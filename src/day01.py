""" Advent of Code - Day 1: Historian Hysteria """
from . import utils

def part1(puzzle_input):
    """ Solution for part 1 """
    return puzzle_input

def part2(puzzle_input):
    """ Solution for part 2 """
    return puzzle_input


def main():
    """ Run the solutions """
    puzzle_input = utils.read_input_file('inputs/day01_input.txt')
    result = part1(puzzle_input)
    print(f"Solution to part 1: {result}")

    result = part2(puzzle_input)
    print(f"Solution to part 2: {result}")

if __name__ == '__main__':
    main()
