file_idx = 0
# real = 0, test = 1

files = ["day17_input.txt", "day17_test.txt", "test2.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()

import heapq


def part1(lines):
    mapp = {}
    seen = set()
    for y, line in enumerate(lines):
        for x, weight in enumerate(line):
            mapp[(x, y)] = int(weight)
    h = len(lines) - 1
    w = len(lines[0]) - 1

    queue = [(0, (0, 0), "E"), (0, (0, 0), "S")]  # heat, position, direction
    while queue:
        heat, pos, dir = heapq.heappop(queue)
        if pos == (w, h):
            return heat
        if (pos, dir) in seen:
            continue
        seen.add((pos, dir))

        dest_heat = heat
        dest = pos
        for i in range(1, 4):
            match dir:
                case "N":
                    dest = (dest[0], dest[1] - 1)
                case "S":
                    dest = (dest[0], dest[1] + 1)
                case "E":
                    dest = (dest[0] + 1, dest[1])
                case "W":
                    dest = (dest[0] - 1, dest[1])
            if dest not in mapp:
                break

            dest_heat += mapp[dest]
            new_dirs = "EW" if dir in "NS" else "NS"
            for new_dir in new_dirs:
                heapq.heappush(queue, (dest_heat, dest, new_dir))


def part2(lines):
    mapp = {}
    seen = set()
    for y, line in enumerate(lines):
        for x, weight in enumerate(line):
            mapp[(x, y)] = int(weight)
    h = len(lines) - 1
    w = len(lines[0]) - 1

    queue = [(0, (0, 0), "E"), (0, (0, 0), "S")]  # heat, position, direction
    while queue:
        heat, pos, dir = heapq.heappop(queue)
        if pos == (w, h):
            return heat
        if (pos, dir) in seen:
            continue
        seen.add((pos, dir))

        dest_heat = heat
        dest = pos
        for i in range(1, 11):
            match dir:
                case "N":
                    dest = (dest[0], dest[1] - 1)
                case "S":
                    dest = (dest[0], dest[1] + 1)
                case "E":
                    dest = (dest[0] + 1, dest[1])
                case "W":
                    dest = (dest[0] - 1, dest[1])
            if dest not in mapp:
                break

            dest_heat += mapp[dest]
            if i >= 4:
                new_dirs = "EW" if dir in "NS" else "NS"
                for new_dir in new_dirs:
                    heapq.heappush(queue, (dest_heat, dest, new_dir))


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
