file_idx = 0
# real = 0, test = 1

import re, math

files = ["day3_input.txt", "day3_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()


def part1(lines):
    sym_locs = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if not char.isdigit() and not char == ".":
                sym_locs.append((i, j))

    summ = 0

    for i, line in enumerate(lines):
        nums = re.findall("[0-9]+", line)
        j = 0
        prev_num = ""
        for num in nums:
            j = line.find(num, j + len(prev_num))
            prev_num = num
            adj_x = range(max(j - 1, 0), min(j + len(num), len(line)) + 1)
            adj_y = range(max(i - 1, 0), min(i + 1, len(lines)) + 1)
            for pos in sym_locs:
                if pos[0] in adj_y and pos[1] in adj_x:
                    summ += int(num)
                    break
    return summ


def part2(lines):
    class Gear:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.nums = []

    gears = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "*":
                gears.append(Gear(j, i))

    for i, line in enumerate(lines):
        nums = re.findall("[0-9]+", line)
        j = 0
        prev_num = ""
        for num in nums:
            j = line.find(num, j + len(prev_num))
            prev_num = num
            adj_x = range(max(j - 1, 0), min(j + len(num), len(line)) + 1)
            adj_y = range(max(i - 1, 0), min(i + 1, len(lines)) + 1)

            for gear in gears:
                if gear.x in adj_x and gear.y in adj_y:
                    gear.nums.append(int(num))

    summ = 0
    for gear in gears:
        if len(gear.nums) > 1:
            summ += math.prod(gear.nums)
    return summ


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
