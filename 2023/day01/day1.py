file_idx = 0
# real = 0, test = 1

files = ["day1_input.txt", "day1_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()


def part1(lines):
    summ = 0
    for line in lines:
        num = ""
        for char in line:
            if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                num += char
        realnum = num[0] + num[-1]
        summ += int(realnum)
    return summ


def part2(lines):
    summ = 0
    for line in lines:
        lookup = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }
        first = ""
        last = ""
        for i, char in enumerate(line):
            if first == "":
                if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    first = char
                elif line[i : i + 3] in ["one", "two", "six"]:
                    first = line[i : i + 3]
                elif line[i : i + 4] in ["four", "five", "nine"]:
                    first = line[i : i + 4]
                elif line[i : i + 5] in ["three", "seven", "eight"]:
                    first = line[i : i + 5]
            else:
                if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    last = char
                elif line[i : i + 3] in ["one", "two", "six"]:
                    last = line[i : i + 3]
                elif line[i : i + 4] in ["four", "five", "nine"]:
                    last = line[i : i + 4]
                elif line[i : i + 5] in ["three", "seven", "eight"]:
                    last = line[i : i + 5]

        if first not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            first = str(lookup[first])

        if last not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ""]:
            last = str(lookup[last])

        if last == "":
            last = first
        num = first + last
        summ += int(num)
    return summ


# print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
