file_idx = 0
# real = 0, test = 1

files = ["day16_input.txt", "day16_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()

from collections import defaultdict


def traverse(pos, dir, mapp):
    match dir:
        case "N":
            move = complex(0, -1)
        case "E":
            move = complex(1, 0)
        case "S":
            move = complex(0, 1)
        case "W":
            move = complex(-1, 0)
    dest = pos + move

    if dest not in mapp:
        return []

    match mapp[dest]:
        case ".":
            return [(dest, dir)]
        case "/":
            newdir = {"N": "E", "E": "N", "S": "W", "W": "S"}
            dir = newdir[dir]
            return [(dest, dir)]
        case "\\":
            newdir = {"N": "W", "E": "S", "S": "E", "W": "N"}
            dir = newdir[dir]
            return [(dest, dir)]
        case "-":
            return [(dest, "E"), (dest, "W")]
        case "|":
            return [(dest, "N"), (dest, "S")]


def send_beam(start_pos, start_dir, mapp):
    energized = defaultdict(list)
    queue = [(start_pos, start_dir)]
    while queue:
        pos, dir = queue.pop(0)
        for dest, dest_dir in traverse(pos, dir, mapp):
            if dest_dir not in energized.get(dest, []):
                energized[dest].append(dest_dir)
                queue.append((dest, dest_dir))
    return len(energized)


def part1(lines):
    mapp = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            mapp[complex(j, i)] = char

    return send_beam(complex(-1, 0), "E", mapp)


def part2(lines):
    mapp = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            mapp[complex(j, i)] = char

    h = len(lines)
    w = len(lines[0])

    res = []
    for y in range(h):
        res.append(send_beam(complex(-1, y), "E", mapp))
        res.append(send_beam(complex(w, y), "W", mapp))

    for x in range(w):
        res.append(send_beam(complex(x, -1), "S", mapp))
        res.append(send_beam(complex(x, h), "N", mapp))

    return max(res)


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
