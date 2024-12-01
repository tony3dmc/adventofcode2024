""" Advent of Code - Day 1: Historian Hysteria """
from . import utils

def part1(puzzle_input):
    """ Solution for part 1: sort both lists then iterate, building the answer """
    (lefts, rights) = utils.fetch_columns(puzzle_input)

    lefts.sort()
    rights.sort()

    answer = 0
    for i, left in enumerate(lefts):
        answer += abs(left - rights[i])

    return answer

def part2(puzzle_input):
    """ Solution for part 2: perform frequency analysis and iterate left values """
    (lefts, rights) = utils.fetch_columns(puzzle_input)
    frequencies = utils.frequency_analysis(rights)

    answer = 0
    for n in lefts:
        if n in frequencies:
            answer += n * frequencies[n]

    return answer

def main():
    """ Run the solutions """
    puzzle_input = utils.read_input_lines('inputs/day01_input.txt')
    result = part1(puzzle_input)
    print(f"Solution to part 1: {result}")

    result = part2(puzzle_input)
    print(f"Solution to part 2: {result}")

if __name__ == '__main__':
    main()
