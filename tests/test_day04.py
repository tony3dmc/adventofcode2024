""" Advent of Code - Tests for Day 4 """

import pytest # type: ignore
from src.day04 import part1, part2
from src import utils

@pytest.fixture(name="puzzle_input")
def input_data():
    """ Load the puzzle input through a test fixture """
    return utils.read_input_lines('inputs/day04_example.txt')

def test_day04_part1(puzzle_input):
    """ Check the final output matches our expected part 1 value """
    assert part1(puzzle_input) == 18

def test_day04_part2(puzzle_input):
    """ Check the final output matches our expected part 2 value """
    assert part2(puzzle_input) == 9