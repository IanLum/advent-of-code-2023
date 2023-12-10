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


def get_start_paths(mapp):
    start = [i[0] for i in mapp.items() if i[1] == "S"][0]
    moves = legalmoves(start, [], mapp)
    out = [start]
    for move in moves:
        match move:
            case Direction.UP:
                vec = complex(0, -1)
            case Direction.RIGHT:
                vec = complex(1, 0)
            case Direction.DOWN:
                vec = complex(0, 1)
            case Direction.LEFT:
                vec = complex(-1, 0)
        out.append([start + vec])
    return out


def visualize_pt2(height, width, start, inside, loopmap):
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
        print(l)


def pipe_type(mapp, start):
    moves = legalmoves(start, [], mapp)
    # match case doesnt work with sets :(
    if set(moves) == set([Direction.UP, Direction.RIGHT]):
        return "L"
    elif set(moves) == set([Direction.UP, Direction.DOWN]):
        return "|"
    elif set(moves) == set([Direction.UP, Direction.LEFT]):
        return "J"
    elif set(moves) == set([Direction.RIGHT, Direction.DOWN]):
        return "F"
    elif set(moves) == set([Direction.RIGHT, Direction.LEFT]):
        return "-"
    elif set(moves) == set([Direction.DOWN, Direction.LEFT]):
        return "7"


def part1(lines):
    mapp = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            mapp[complex(j, i)] = char

    start, path1, path2 = get_start_paths(mapp)
    while path1[-1] != path2[-1]:
        path1.append(move(path1[-1], path1, mapp))
        path2.append(move(path2[-1], path2, mapp))
    return len(path1)


def part2(lines):
    mapp = {}
    # build the map
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            mapp[complex(j, i)] = char

    # find the loop
    start, path1, path2 = get_start_paths(mapp)
    while path1[-1] != path2[-1]:
        path1.append(move(path1[-1], path1, mapp))
        path2.append(move(path2[-1], path2, mapp))

    # build map of the loop
    loopmap = dict((loc, mapp[loc]) for loc in path1 + path2 + [start])

    # replace start S with appropriate pipe type
    loopmap[start] = pipe_type(mapp, start)

    # determine inside points
    inside = []
    for loc in mapp.keys():
        if loc in loopmap:
            continue

        up = [loopmap.get(loc + complex(0, -i - 1), None) for i in range(int(loc.imag))]
        upcount = Counter(up)
        # find times pipe fully crosses above
        # J & 7 are left facing
        # L & F are right facing
        # one left facing and one right facing is a full cross
        upcrosses = upcount.get("-", 0) + min(
            upcount.get("J", 0) + upcount.get("7", 0),
            upcount.get("L", 0) + upcount.get("F", 0),
        )
        if upcrosses % 2 != 0:
            inside.append(loc)

    # visualize_pt2(len(lines), len(line), start, inside, loopmap)
    return len(inside)


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
