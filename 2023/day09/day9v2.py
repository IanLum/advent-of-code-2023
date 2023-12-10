file_idx = 0
# real = 0, test = 1

files = ["day9_input.txt", "day9_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()


def part1(lines):
    summ = 0
    for line in lines:
        nums = list(map(int, line.split(" ")))
        while not all(i == 0 for i in nums):
            summ += nums[-1]
            nums = [i - j for i, j in zip(nums[1:], nums)]
    return summ


def part2(lines):
    summ = 0
    for line in lines:
        first = []
        nums = list(map(int, line.split(" ")))
        while not all(i == 0 for i in nums):
            first.append(nums[0])
            nums = [i - j for i, j in zip(nums[1:], nums)]
        curr = 0
        for i in reversed(first):
            curr = i - curr
        summ += curr
    return summ


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
