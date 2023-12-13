file_idx = 0
# real = 0, test = 1

files = ["day13_input.txt", "day13_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()

import numpy as np
from itertools import product


def find_mirror(mapp, avoid=0):
    for i, line in enumerate(mapp):
        if i == 0:
            continue
        if all(line == mapp[i - 1]):
            diff = 1
            while True:
                if i + diff >= len(mapp) or i - 1 - diff < 0:
                    if i != avoid:
                        return i
                    break
                if all(mapp[i + diff] == mapp[i - 1 - diff]):
                    diff += 1
                else:
                    break
    return 0


def part1(lines):
    summ = 0
    rows = []
    for line in lines:
        if line != "":
            rows.append(list(line))
        else:
            rows = np.array(rows)
            summ += 100 * find_mirror(rows)
            summ += find_mirror(rows.T)
            rows = []
    return summ


def part2(lines):
    summ = 0
    rows = []
    for line in lines:
        if line != "":
            rows.append(list(line))
        else:
            rows = np.array(rows)
            realh = find_mirror(rows)
            realv = find_mirror(rows.T)
            for x, y in list(product(range(len(rows[0])), range(len(rows)))):
                newrows = rows.copy()
                swap = {".": "#", "#": "."}
                newrows[y][x] = swap[newrows[y][x]]

                hmir = find_mirror(newrows, avoid=realh)
                vmir = find_mirror(newrows.T, avoid=realv)

                if hmir != 0:
                    summ += 100 * hmir
                    break
                if vmir != 0:
                    summ += vmir
                    break

            rows = []
    return summ


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
