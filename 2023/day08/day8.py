file_idx = 0
# real = 0, test = 1

files = ["day8_input.txt", "day8_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()

import re, math


def part1(lines):
    # moves =
    mapp = {}
    for i, line in enumerate(lines):
        if i == 0:
            moves = line
        elif i == 1:
            continue
        else:
            start, left, right = re.findall("[A-Z]+", line)
            mapp[start] = (left, right)

    # print(mapp)
    curr = "AAA"
    for i, move in enumerate(moves * 1000000):
        if move == "L":
            curr = mapp[curr][0]
        else:
            curr = mapp[curr][1]
        if curr == "ZZZ":
            return i + 1


def part2(lines):
    # moves =
    starts = []
    mapp = {}
    for i, line in enumerate(lines):
        if i == 0:
            moves = line
        elif i == 1:
            continue
        else:
            start, left, right = re.findall("[A-Z]+", line)
            mapp[start] = (left, right)
            if start[-1] == "A":
                starts.append(start)

    start_dists = []
    zloop = []
    z2 = []
    zs = []
    for start in starts:
        curr = start
        atz = False
        for i, move in enumerate(moves * 1000):
            if move == "L":
                curr = mapp[curr][0]
            else:
                curr = mapp[curr][1]
            if curr[-1] == "Z":
                if atz:
                    z2.append(i + 1)
                    zloop.append(i + 1 - start_dists[-1])
                    break
                else:
                    zs.append(curr)
                    start_dists.append(i + 1)
                    atz = True
    return math.lcm(
        zloop[0],
        zloop[1],
        zloop[2],
        zloop[3],
        zloop[4],
        zloop[5],
    )


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
