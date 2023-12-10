file_idx = 0
# real = 0, test = 1

files = [
    "day10_input.txt",
    "day10_test.txt",
    "day10_test_pt2.txt",
    "day10_test2_pt2.txt",
    "day10_test3_pt2.txt",
]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()

from enum import Enum
from collections import Counter


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


def legalmoves(loc, traversed, mapp):
    legal = []
    for dir in [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]:
        match dir:
            case Direction.UP:
                if mapp.get(loc, None) in ["S", "|", "L", "J"]:
                    dest = loc + complex(0, -1)
                    if (
                        mapp.get(dest, None) in ["|", "F", "7"]
                        and dest not in traversed
                    ):
                        legal.append(dir)
            case Direction.RIGHT:
                if mapp.get(loc, None) in ["S", "-", "L", "F"]:
                    dest = loc + complex(1, 0)
                    if (
                        mapp.get(dest, None) in ["-", "J", "7"]
                        and dest not in traversed
                    ):
                        legal.append(dir)

            case Direction.DOWN:
                if mapp.get(loc, None) in ["S", "|", "F", "7"]:
                    dest = loc + complex(0, 1)
                    if (
                        mapp.get(dest, None) in ["|", "L", "J"]
                        and dest not in traversed
                    ):
                        legal.append(dir)
            case Direction.LEFT:
                if mapp.get(loc, None) in ["S", "-", "J", "7"]:
                    dest = loc + complex(-1, 0)
                    if (
                        mapp.get(dest, None) in ["-", "L", "F"]
                        and dest not in traversed
                    ):
                        legal.append(dir)
    return legal


def move(curr, traversed, mapp):
    for dir in legalmoves(curr, traversed, mapp):
        match dir:
            case Direction.UP:
                next = curr + complex(0, -1)
            case Direction.RIGHT:
                next = curr + complex(1, 0)
            case Direction.DOWN:
                next = curr + complex(0, 1)
            case Direction.LEFT:
                next = curr + complex(-1, 0)
        return next


def part1(lines):
    mapp = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            mapp[complex(j, i)] = char
            if char == "S":
                start = complex(j, i)

    path1 = [complex(72, 29)]
    path2 = [complex(73, 30)]
    while path1[-1] != path2[-1]:
        path1.append(move(path1[-1], path1, mapp))
        path2.append(move(path2[-1], path2, mapp))
    return len(path1)
    # print(len(path2))


def part2(lines):
    mapp = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            mapp[complex(j, i)] = char
            if char == "S":
                start = complex(j, i)

    match file_idx:
        case 0:
            # real
            path1 = [complex(72, 29)]
            path2 = [complex(73, 30)]
        case 2:
            # test 1 pt 2
            path1 = [complex(3, 0)]
            path2 = [complex(4, 1)]
        case 3:
            # test 1 pt 2
            path1 = [complex(1, 2)]
            path2 = [complex(2, 1)]
        case 4:
            # test 1 pt 2
            path1 = [complex(12, 5)]
            path2 = [complex(13, 4)]

    while path1[-1] != path2[-1]:
        path1.append(move(path1[-1], path1, mapp))
        path2.append(move(path2[-1], path2, mapp))

    loopp = path1 + path2 + [start]
    area = 0
    loopmap = dict((loc, mapp[loc]) for loc in loopp)
    height = len(lines)
    width = len(line)
    inside = []

    for loc in mapp.keys():
        if loc in loopp:
            continue

        up = [loopmap.get(loc + complex(0, -i - 1), None) for i in range(int(loc.imag))]

        down = [
            loopmap.get(loc + complex(0, i + 1), None)
            for i in range(height - int(loc.imag) - 1)
        ]

        left = [
            loopmap.get(loc + complex(-i - 1, 0), None) for i in range(int(loc.real))
        ]

        right = [
            loopmap.get(loc + complex(i + 1, 0), None)
            for i in range(width - int(loc.real) - 1)
        ]

        # in real input start is an L
        upcount = Counter(up)
        upcrosses = upcount.get("-", 0) + min(
            upcount.get("J", 0) + upcount.get("7", 0),
            upcount.get("S", 0) + upcount.get("L", 0) + upcount.get("F", 0),
        )
        leftcount = Counter(left)
        leftcrosses = leftcount.get("|", 0) + min(
            leftcount.get("J", 0) + leftcount.get("L", 0) + upcount.get("S", 0),
            leftcount.get("7", 0) + leftcount.get("F", 0),
        )
        if upcrosses % 2 != 0:  # and leftcrosses % 2 != 0:
            area += 1
            inside.append(loc)

    for i in range(height):
        l = ""
        for j in range(width):
            loc = complex(j, i)
            if loc == start:
                l += "S"
            elif loc in inside:
                l += "I"
            elif loc in loopmap:
                l += "@"
            else:
                l += "."
        # print(l)

    # print(loc)
    # if loc == complex(14, 3):
    #     print(up)
    #     print(down)

    #     print(left)
    #     print(right)
    #     a = Counter(up)
    #     print(a.get("-", 0))
    #     print(a.get("J", 0))
    #     print(Counter(up))

    # # up
    # inloop = 0
    # checkpos = loc
    # while checkpos in mapp.keys():
    #     if checkpos in loopp:
    #         inloop += 1
    #     checkpos += complex(0, -1)
    # if inloop % 2 == 0:
    #     continue

    # # right
    # inloop = 0
    # checkpos = loc
    # while checkpos in mapp.keys():
    #     if checkpos in loopp:
    #         inloop += 1
    #     checkpos += complex(1, 0)
    # if inloop % 2 == 0:
    #     continue

    # # down
    # inloop = 0
    # checkpos = loc
    # while checkpos in mapp.keys():
    #     if checkpos in loopp:
    #         inloop += 1
    #     checkpos += complex(0, 1)
    # if inloop % 2 == 0:
    #     continue

    # # left
    # inloop = 0
    # checkpos = loc
    # while checkpos in mapp.keys():
    #     if checkpos in loopp:
    #         inloop += 1
    #     checkpos += complex(-1, 0)
    # if inloop % 2 == 0:
    #     continue

    return area


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
