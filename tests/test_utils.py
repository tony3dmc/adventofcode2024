""" Advent of Code - Tests for our Util library """

from src import utils

def test_get_numbers_single():
    """ Verify extraction of numbers from n=1 size list """
    test_input = [ "1 1 2 3 5 8 13" ]
    assert utils.get_numbers(test_input) == [ 1, 1, 2, 3, 5, 8, 13 ]

def test_get_numbers_multiple():
    """ Verify extraction of numbers from n=2 size list """
    test_input = [ "1 1 2 3", "5 8 13" ]
    assert utils.get_numbers(test_input) == [ 1, 1, 2, 3, 5, 8, 13 ]

def test_fetch_columns():
    """ Verify extraction of columns from list of strings """
    test_input = [ "1 5", "2 4", "3 3", "4 2", "5 1" ]
    assert utils.fetch_columns(test_input) == [[ 1, 2, 3, 4, 5 ], [ 5, 4, 3, 2, 1 ]]

def test_frequency_analysis():
    """ Verify value counting """
    test_input = [ 1, 1, 1, 2, 2, 3 ]
    assert utils.frequency_analysis(test_input) == { 1: 3, 2: 2, 3: 1 }

def test_numbers_changing_in_same_direction_good():
    """ Verify when all numbers move in the same direction """
    test_input = [ 1, 2, 3, 4, 5 ]
    assert utils.numbers_changing_in_same_direction(test_input) == 4

def test_numbers_changing_in_same_direction_bad():
    """ Verify when some numbers move in the same direction """
    test_input = [ 1, 2, 3, 2, 1 ]
    assert utils.numbers_changing_in_same_direction(test_input) == 2

def test_get_direction_between_up():
    """ Verify direction of upwards values """
    assert utils.get_direction_between(1, 2) == -1

def test_get_direction_between_across():
    """ Verify direction of unchanging values """
    assert utils.get_direction_between(2, 2) == 0

def test_get_direction_between_down():
    """ Verify direction of decreasing values """
    assert utils.get_direction_between(2, 1) == 1

def test_largest_gap_positive():
    """ Verify positive gaps between numbers """
    test_input = [ 1, 2, 5 ]
    assert utils.largest_gap(test_input) == 3

def test_largest_gap_negative():
    """ Verify negative gaps between numbers """
    test_input = [ 1, 2, -5 ]
    assert utils.largest_gap(test_input) == 7

def test_largest_gap_single():
    """ Verify n=1 number gap """
    test_input = [ 1 ]
    assert utils.largest_gap(test_input) == 0
