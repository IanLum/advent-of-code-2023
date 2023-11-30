file_idx = 0
# real = 0, test = 1

files = ["2022day1_input.txt", "2022day1_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()


def part1(lines):
    most = 0
    curr = 0
    for i in lines:
        if i == "":
            if curr > most:
                most = curr
            curr = 0
        else:
            curr += int(i)
    return most


def part2(lines):
    elf = []
    curr = 0
    for i in lines:
        if i == "":
            elf.append(curr)
            curr = 0
        else:
            curr += int(i)
    elf.sort()
    return sum(elf[-3:])


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
