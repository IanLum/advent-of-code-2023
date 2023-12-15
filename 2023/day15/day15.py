file_idx = 0
# real = 0, test = 1

files = ["day15_input.txt", "day15_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()

from collections import defaultdict


def part1(lines):
    q = lines[0].split(",")
    summ = 0
    # q = ["HASH"]
    for i in q:
        val = 0
        for char in i:
            val += ord(char)
            val *= 17
            val %= 256
        summ += val
    return summ


def hash(s):
    val = 0
    for char in s:
        val += ord(char)
        val *= 17
        val %= 256
    return val


def part2(lines):
    boxes = defaultdict(list)
    q = lines[0].split(",")
    for i in q:
        if "=" in i:
            [label, value] = i.split("=")
            filt = list(filter(lambda x: x[0] == label, boxes[hash(label)]))
            if filt == []:
                boxes[hash(label)].append((label, int(value)))
            else:
                boxes[hash(label)][boxes[hash(label)].index(filt[0])] = (
                    label,
                    int(value),
                )
        elif "-" in i:
            label = i.split("-")[0]
            filt = list(filter(lambda x: x[0] == label, boxes[hash(label)]))
            if filt != []:
                boxes[hash(label)].remove(filt[0])

    summ = 0
    for box in boxes.items():
        num, lenses = box
        for i, lens in enumerate(lenses):
            summ += (num + 1) * lens[1] * (i + 1)
    return summ


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
