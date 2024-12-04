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
just test utils
```

## Solution commentary

### Day 1: Historian Hysteria

The usual easy warmup. I decided to gather all the numbers in the puzzle input into a single list, and then perform n/2 iterations, building up a set of lefts and rights, followed by a simple loop over the sorted values to sum the differences. PyLint forced me to learn the built-in `enumerate` function when I was doing some poor loops. I was also educated on the proper use of checking for keys in dictionaries, which is purely me being a bit rusty in this language. I was also told off for the odd trailing semicolon from the muscle memory of writing PHP.

I will attempt to maintain and refactor the `utils.py` library of functions as we go, so previous puzzle solutions may be modified over time, as long as the tests pass. Good warmup, happy with my test rig and project layout this time.

### Day 2: Red-Nosed Reports

I tried too hard to create generic utils to help solve this one and ended up spending far too long on clever solutions. The twist in part 2 invalidated all my work as usual! My initial approach to the Problem Dampener concept was to write smarter algorithms to ignore anomalies, but I kept finding more corner cases where it wouldn't work. Eventually I resorted to a simpler approach by slicing out one level at at time and running them through the checks - inefficient, but ran out of time.

The linter humbled me once more by pointing out several bad code smells. It occurred to me that I haven't been using list comprehensions in my code yet, which would likely simplify things more. I'll keep this in mind for tomorrow.

I've only been writing tests for the overall solutions so far, but we need coverage over our utils as well, something else to do tomorrow.

### Day 3: Mull It Over

I was half expecting the second part to be a problem that I would need to solve by running over the input data, setting a do/don't flag and parsing the mul operations manually, until I realised that I could just remove the inactive chunks of code from the puzzle input. First submission was a bit low, but I was quick to figure out there would be an unterminated don't section at the end to clean up.

One more I am humbled by PyLint. My first use of list comprehension was to generate a list of the multiplications with `[x * y for x, y in matches]` and place that directly into the `sum()` function. However, there's no need to create it as a list to pass to `sum()` if I only plan on using it once, or dropping into one of the 'any', 'all', 'max', 'min' or 'sum' functions. It's cleaner syntax to supply a generator expression which will calculate the values on the fly instead of making and processing the list. Things like this are why learning the language is easier with a decent code smell tool.

I wrote up some functions to cover the Utils library but they're pretty basic. I just wanted to have full coverage. Most puzzle-input-processing functions won't need too many bounds tests - the puzzle input won't be empty or adversarial.

### Day 4: Ceres Search

I rewrote Part 1 a few times here, wanting to reduce the checks and complexities of word-searching in all eight directions. I decided to search the space for 'X' and then look around from there. Not too happy with the layout of my list comprehensions - this is where I'd normally drop it into AI and ask for help cleaning up.

It feels good when you run the linter without problems, can't wait for that to happen... This time the aspect I learned was the syntax `foo in (a, b, c)` to help simplify multiple checks. I really like sets in Python.
