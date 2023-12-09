file_idx = 0
# real = 0, test = 1

files = ["day9_input.txt", "day9_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()


def part1(lines):
    summ = 0
    for line in lines:
        nums = list(map(int, line.split(" ")))
        curr = nums
        ends = [nums[-1]]
        while True:
            diff = []
            for i in range(len(curr) - 1):
                diff.append(curr[i + 1] - curr[i])
            if diff == [0] * len(diff):
                break
            else:
                ends.append(diff[-1])
                curr = diff
        summ += sum(ends)
    return summ


def part2(lines):
    summ = 0
    for line in lines:
        nums = list(map(int, line.split(" ")))
        curr = nums
        first = [nums[0]]
        while True:
            diff = []
            for i in range(len(curr) - 1):
                diff.append(curr[i + 1] - curr[i])
            if diff == [0] * len(diff):
                break
            else:
                first.append(diff[0])
                curr = diff

        curr = 0
        for i in reversed(first):
            curr = i - curr
        summ += curr
    return summ


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
