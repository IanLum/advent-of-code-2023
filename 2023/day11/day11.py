file_idx = 0
# real = 0, test = 1

files = ["day11_input.txt", "day11_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()

import re
from collections import defaultdict
from itertools import combinations


def part1(lines):
    space = []
    cols = defaultdict(int)
    for line in lines:
        if set(line) == {"."}:
            space.append(line)
            space.append(line)
        else:
            space.append(line)
            for i in re.finditer("#", line):
                cols[i.start()] += 1
    blankcols = [i for i in range(len(line)) if cols[i] == 0]

    for i, line in enumerate(space):
        newline = ""
        for j, char in enumerate(line):
            if j in blankcols:
                newline += "."
            newline += char
        space[i] = newline

    galaxies = []
    for i, line in enumerate(space):
        for j, sym in enumerate(line):
            if sym == "#":
                galaxies.append(complex(j, i))

    pairs = list(combinations(galaxies, 2))
    summ = 0
    for pair in pairs:
        dist = pair[0] - pair[1]
        summ += abs(dist.real) + abs(dist.imag)
    return int(summ)


def part2(lines):
    grow = 999999
    galaxies = []
    blankrows = []
    cols = defaultdict(int)
    for i, line in enumerate(lines):
        if set(line) == {"."}:
            blankrows.append(i)
        else:
            for j in re.finditer("#", line):
                galaxies.append(complex(j.start(), i))
                cols[j.start()] += 1
    blankcols = [i for i in range(len(line)) if cols[i] == 0]
    for col in reversed(blankcols):
        for i, gal in enumerate(galaxies):
            if gal.real > col:
                galaxies[i] += complex(grow, 0)

    for row in reversed(blankrows):
        for i, gal in enumerate(galaxies):
            if gal.imag > row:
                galaxies[i] += complex(0, grow)

    pairs = list(combinations(galaxies, 2))
    summ = 0
    for pair in pairs:
        dist = pair[0] - pair[1]
        summ += abs(dist.real) + abs(dist.imag)
    return int(summ)


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
