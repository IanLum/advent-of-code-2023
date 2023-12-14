file_idx = 0
# real = 0, test = 1

files = ["day14_input.txt", "day14_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()

import re


def part1(lines):
    summ = 0
    cols = []
    for i in range(len(lines[0])):
        cols.append("".join([row[i] for row in lines]))
    height = len(lines)
    for col in cols:
        sections = re.split("(#)", col)
        sort = list(map(lambda x: "".join(sorted(x, reverse=True)), sections))
        mapp = [height - i for i, char in enumerate("".join(sort)) if char == "O"]
        summ += sum(mapp)
    return summ


def transpose(rows):
    cols = []
    for i in range(len(rows[0])):
        cols.append("".join([row[i] for row in rows]))
    return cols


def tilt_left(lines):
    out = []
    for line in lines:
        sections = re.split("(#)", line)
        sort = list(map(lambda x: "".join(sorted(x, reverse=True)), sections))
        out.append("".join(sort))
    return out


def rotate90cw(lines):
    return list(map(lambda x: "".join(list(x[::-1])), zip(*lines)))


def rotate90ccw(lines):
    return list(map(lambda x: "".join(list(x)), zip(*lines)))[::-1]


def part2(lines):
    q = rotate90ccw(lines)
    mem = {}
    height = len(lines)
    cycles = 1000000000
    for i in range(cycles):
        if q in mem.values():
            repeated = [x[0] for x in mem.items() if x[1] == q][0]
            cycle_size = i - repeated
            offset = (cycles - repeated) % cycle_size
            goal = repeated + offset
            break
        mem[i] = q
        for i in range(4):
            q = tilt_left(q)
            q = rotate90cw(q)

    q = mem[goal]
    q = rotate90cw(q)
    mapp = [line.count("O") * (height - i) for i, line in enumerate(q)]
    return sum(mapp)


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
