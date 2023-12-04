file_idx = 0
# real = 0, test = 1

from collections import defaultdict

files = ["day4_input.txt", "day4_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()


def part1(lines):
    total = 0
    for line in lines:
        pts = 0
        q = line.split(": ")[1].split(" | ")
        winning = q[0].split(" ")
        have = q[1].split(" ")
        for num in have:
            if num != "":
                if num in winning:
                    if pts == 0:
                        pts = 1
                    else:
                        pts *= 2
        total += pts
    return total


def part2(lines):
    copies = defaultdict(lambda: 1)
    for i, line in enumerate(lines):
        copies[i]
        q = line.split(": ")[1].split(" | ")
        winning = q[0].split(" ")
        have = q[1].split(" ")
        total = 0
        for num in have:
            if num != "":
                if num in winning:
                    total += 1
        cardswon = range(i + 1, i + 1 + total)
        for card in cardswon:
            copies[card] += copies[i]

    return sum(copies.values())


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
