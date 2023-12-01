file_idx = 0
# real = 0, test = 1, test 2 = 2

import string, re

files = ["day1_input.txt", "day1_test.txt", "day1pt2_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()


def part1(lines):
    summ = 0
    for line in lines:
        digs = list(filter(lambda x: x in string.digits, line))
        num = digs[0] + digs[-1]
        summ += int(num)
    return summ


def part2(lines):
    lookup = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    summ = 0
    for line in lines:
        digs = re.findall(
            r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line
        )
        num = str(lookup.get(digs[0], digs[0])) + str(lookup.get(digs[-1], digs[-1]))
        summ += int(num)
    return summ


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
