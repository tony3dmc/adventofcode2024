# Advent of Code 2024 - Python Challenges

Another year, another Advent of Code challenge! I'm pretty busy with work and life commitments in December so I'm sticking with Python - but with an emphasis on test-driven development using `pytest`. No AI assistance with the puzzles - Copilot is disabled and I'm only working from general online Python references.

I'm approaching this year's challenge by writing tests first using the sample inputs and outputs, then solving the puzzles in separate files, building up a common library of functions to use in future solutions.

My primary goal is refining my Python skills, particularly in automated testing.

## Structure

The project is organized as follows:

- `src/`: Script files for each day's puzzle solutions.
- `tests/`: Contains `pytest` test files corresponding to each day.
- `inputs/`: Input files for each day - both the samples and my unique puzzle inputs
- `requirements.txt`: List of project dependencies.

## Clean code

I'm using pylint to ensure all files follow a coding standard, which is why you may see excessive docblocks and strict usage of params in function calls.

```bash
just lint
```

## Running the solution code

```bash
just run day01
```

## Running the tests

To run the tests, ensure you have a proper python environment setup (see NOTES.md for how mine was established) and run the following:

```bash
just testall
```

Or for a single day

```bash
just test day01
```

## Solution commentary

### Day 1: Historian Hysteria

The usual easy warmup. I decided to gather all the numbers in the puzzle input into a single list, and then perform n/2 iterations, building up a set of lefts and rights, followed by a simple loop over the sorted values to sum the differences. PyLint forced me to learn the built-in `enumerate` function when I was doing some poor loops. I was also educated on the proper use of checking for keys in dictionaries, which is purely me being a bit rusty in this language. I was also told off for the odd trailing semicolon from the muscle memory of writing PHP.

I will attempt to maintain and refactor the `utils.py` library of functions as we go, so previous puzzle solutions may be modified over time, as long as the tests pass. Good warmup, happy with my test rig and project layout this time.

### Day 2: Red-Nosed Reports

I tried too hard to create generic utils to help solve this one and ended up spending far too long on clever solutions. The twist in part 2 invalidated all my work as usual! My initial approach to the Problem Dampener concept was to write smarter algorithms to ignore anomalies, but I kept finding more corner cases where it wouldn't work. Eventually I resorted to a simpler approach by slicing out one level at at time and running them through the checks - inefficient, but ran out of time.

The linter humbled me once more by pointing out several bad code smells. It occurred to me that I haven't been using lambda expressions in my code yet, which would likely simplify things more. I'll keep this in mind for tomorrow.

I've only been writing tests for the overall solutions so far, but we need coverage over our utils as well, something else to do tomorrow.
