def part1():
    # races = [(7, 9), (15, 40), (30, 200)]
    races = [(46, 208), (85, 1412), (75, 1257), (82, 1410)]
    total = 1
    for time, dist in races:
        ways = 0
        for i in range(time):
            if i * (time - i) > dist:
                ways += 1
        if ways > 0:
            total *= ways
    return total


def part2():
    time = 46857582
    dist = 208141212571410
    ways = 0
    for i in range(time):
        if i * (time - i) > dist:
            ways += 1
    return ways


print("Part 1:", part1())
print("Part 2:", part2())
