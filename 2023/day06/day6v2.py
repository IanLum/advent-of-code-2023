file_idx = 0
# real = 0, test = 1

import re

files = ["day6_input.txt", "day6_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()


def part1(lines):
    times = map(int, re.findall("\d+", lines[0]))
    dists = map(int, re.findall("\d+", lines[1]))
    total = 1
    for time, dist in zip(times, dists):
        ways = 0
        for i in range(time):
            if i * (time - i) > dist:
                ways += 1
        if ways > 0:
            total *= ways
    return total


def part2(lines):
    time = int("".join(re.findall("\d+", lines[0])))
    dist = int("".join(re.findall("\d+", lines[1])))
    ways = 0
    for i in range(time):
        if i * (time - i) > dist:
            ways += 1
    return ways


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
