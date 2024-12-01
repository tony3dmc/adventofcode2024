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
