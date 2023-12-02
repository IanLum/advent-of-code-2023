file_idx = 0
# real = 0, test = 1

files = ["day2_input.txt", "day2_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()


def part1(lines):
    impossible = []
    for i, line in enumerate(lines):
        game = i + 1
        sets = line.split(": ")[1].split("; ")
        for set in sets:
            for block in set.split(", "):
                s = block.split(" ")
                num = s[0]
                color = s[1]
                if color == "red":
                    if int(num) > 12:
                        impossible.append(game)
                if color == "green":
                    if int(num) > 13:
                        impossible.append(game)
                if color == "blue":
                    if int(num) > 14:
                        impossible.append(game)
    games = list(range(1, len(lines) + 1))
    possible = [i for i in games if i not in impossible]
    return sum(possible)


def part2(lines):
    summ = 0
    for line in lines:
        sets = line.split(": ")[1].split("; ")
        min_red = 0
        min_gre = 0
        min_blu = 0
        for set in sets:
            for block in set.split(", "):
                s = block.split(" ")
                num = int(s[0])
                color = s[1]
                if color == "red":
                    if num > min_red:
                        min_red = num
                if color == "green":
                    if num > min_gre:
                        min_gre = num
                if color == "blue":
                    if num > min_blu:
                        min_blu = num
        summ += min_red * min_blu * min_gre
    return summ


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
