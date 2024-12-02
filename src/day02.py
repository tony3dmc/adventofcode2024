""" Advent of Code - Day 2: Red-Nosed Reports """
from . import utils

def part1(puzzle_input):
    """ Solution for part 1: ... """
    answer = 0
    for report in puzzle_input:
        if is_safe_report(utils.get_numbers([report])):
            answer += 1

    return answer

def part2(puzzle_input):
    """ Solution for part 2: ... """
    answer = 0
    for report in puzzle_input:
        levels = utils.get_numbers([report])
        if is_safe_report(levels):
            answer += 1
        else:
            for i in range(len(levels)):
                dampened_levels = levels[:i] + levels[i+1:]
                if is_safe_report(dampened_levels):
                    answer += 1
                    break
    return answer

def is_safe_report(levels):
    """ Check if the supplied levels are considered to be a safe report """
    threshold = 3
    directed_level_count = utils.numbers_changing_in_same_direction(levels)

    if directed_level_count != len(levels) - 1:
        return False

    max_gap = utils.largest_gap(levels)
    if max_gap > threshold:
        return False

    return True

def main():
    """ Run the solutions """
    puzzle_input = utils.read_input_lines('inputs/day02_input.txt')
    result = part1(puzzle_input)
    print(f"Solution to part 1: {result}")

    result = part2(puzzle_input)
    print(f"Solution to part 2: {result}")

if __name__ == '__main__':
    main()
