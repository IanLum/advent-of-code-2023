import numpy as np

# 1 for test, 0 for real input
test = 0

if test:
    file = 'day08_test.txt'
else:
    file = 'day08_input.txt'
with open(file) as f:
    lines = f.read().splitlines()

trees = np.zeros((len(lines), len(lines)))
for idx, line in enumerate(lines):
    trees[idx] = np.array([int(x) for x in line])

def seen_top(trees, row, col):
    return all(trees[row, col] > trees[:row, col])

def seen_bottom(trees, row, col):
    return all(trees[row, col] > trees[row+1:, col])

def seen_left(trees, row, col):
    return all(trees[row, col] > trees[row, :col])

def seen_right(trees, row, col):
    return all(trees[row, col] > trees[row, col+1:])

def seen(trees, row, col):
    return seen_top(trees, row, col) or seen_bottom(trees, row, col) or seen_left(trees, row, col) or seen_right(trees, row, col)

solution = 0

for row in range(len(trees)):
    for col in range(len(trees)):
        solution += seen(trees, row, col)

print(solution)