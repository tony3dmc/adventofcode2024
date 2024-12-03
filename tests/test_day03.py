""" Advent of Code - Tests for Day 3 """

import pytest # type: ignore
from src.day03 import part1, part2
from src import utils

@pytest.fixture(name="puzzle_input")
def input_data():
    """ Load the puzzle input through a test fixture """
    return utils.read_input_lines('inputs/day03_example.txt')[0]

@pytest.fixture(name="puzzle_input_part2")
def input_data_part2():
    """ Load the puzzle input through a test fixture """
    return utils.read_input_lines('inputs/day03_example_part2.txt')[0]

def test_day03_part1(puzzle_input):
    """ Check the final output matches our expected part 1 value """
    assert part1(puzzle_input) == 161

def test_day03_part2(puzzle_input_part2):
    """ Check the final output matches our expected part 2 value """
    assert part2(puzzle_input_part2) == 48
