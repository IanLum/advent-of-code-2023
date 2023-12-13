file_idx = 1
# real = 0, test = 1

from itertools import product
import re

files = ["day12_input.txt", "day12_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()


def part1(lines):
    summ = 0
    for i, line in enumerate(lines):
        [springs, mapp] = line.split(" ")
        mapp = list(map(int, mapp.split(",")))
        unknown = springs.count("?")
        combs = ["".join(x) for x in product(["#", "."], repeat=unknown)]
        # if i % 20 == 0:
        #     print(i)
        for comb in combs:
            ct = 0
            attempt = ""
            for char in springs:
                if char == "?":
                    attempt += comb[ct]
                    ct += 1
                else:
                    attempt += char
            counts = list(map(len, re.findall("#+", attempt)))
            if counts == mapp:
                summ += 1
    return summ


def part2(lines):
    summ = 0
    for i, line in enumerate(lines):
        [springs, mapp] = line.split(" ")
        springs = springs + ("?" + springs) * 4
        mapp = list(map(int, mapp.split(","))) * 5


# print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
