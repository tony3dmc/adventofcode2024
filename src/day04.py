""" Advent of Code - Day 4: Ceres Search """
from . import utils

def part1(m):
    """ Solution for part 1: Iterate the 2D space and check all directions if we find an X """
    answer = 0
    x_max = len(m[0])
    y_max = len(m)
    search = 'XMAS'
    w = len(search)
    for y in range(x_max):
        for x in range(y_max):
            if m[y][x] == 'X':
                vision = {
                    'up':    y >= w - 1,
                    'down':  y <= y_max - w,
                    'left':  x >= w - 1,
                    'right': x <= x_max - w
                }
                words = []
                if vision['up']:
                    words.append("".join([m[y - i][x] for i in range(w)]))
                    if vision['right']:
                        words.append("".join([m[y - i][x + i] for i in range(w)]))
                if vision['down']:
                    words.append("".join([m[y + i][x] for i in range(w)]))
                    if vision['left']:
                        words.append("".join([m[y + i][x - i] for i in range(w)]))
                if vision['left']:
                    words.append("".join([m[y][x - i] for i in range(w)]))
                    if vision['up']:
                        words.append("".join([m[y - i][x - i] for i in range(w)]))
                if vision['right']:
                    words.append("".join([m[y][x + i] for i in range(w)]))
                    if vision['down']:
                        words.append("".join([m[y + i][x + i] for i in range(w)]))

                answer += sum(word == search for word in words)

    return answer

def part2(m):
    """ Solution for part 2: ... """
    answer = 0
    x_max = len(m[0])
    y_max = len(m)
    for y in range(1, x_max - 1):
        for x in range(1, y_max - 1):
            if m[y][x] == 'A':
                word1 = "".join([m[y - 1][x - 1], m[y + 1][x + 1]])
                word2 = "".join([m[y - 1][x + 1], m[y + 1][x - 1]])
                if (word1 in ('MS', 'SM') and word2 in ('MS', 'SM')):
                    answer += 1
    return answer

def main():
    """ Run the solutions """
    puzzle_input = utils.read_input_lines('inputs/day04_input.txt')
    result = part1(puzzle_input)
    print(f"Solution to part 1: {result}")

    result = part2(puzzle_input)
    print(f"Solution to part 2: {result}")

if __name__ == '__main__':
    main()
