""" Advent of Code - Tests for Day 1 """

import pytest # type: ignore
from src.day01 import part1, part2
from src import utils

@pytest.fixture(name="puzzle_input")
def input_data():
    """ Load the puzzle imput through a test fixture """
    return utils.read_input_file('inputs/day01_example.txt')

def test_day01_part1(puzzle_input):
    """ Check the final output matches our expected part 1 value """
    assert part1(puzzle_input) == ''

def test_day01_part2(puzzle_input):
    """ Check the final output matches our expected part 2 value """
    assert part2(puzzle_input) == ''
