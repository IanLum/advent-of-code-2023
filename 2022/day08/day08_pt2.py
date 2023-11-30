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
    shorter = trees[row, col] > trees[:row, col]
    seen = 0
    for i in np.flip(shorter):
        seen +=1
        if not i:
            return seen
    return seen

def seen_bottom(trees, row, col):
    shorter = trees[row, col] > trees[row+1:, col]
    seen = 0
    for i in shorter:
        seen +=1
        if not i:
            return seen
    return seen

def seen_left(trees, row, col):
    shorter = trees[row, col] > trees[row, :col]
    seen = 0
    for i in np.flip(shorter):
        seen +=1
        if not i:
            return seen
    return seen


def seen_right(trees, row, col):
    shorter = trees[row, col] > trees[row, col+1:]
    seen = 0
    for i in shorter:
        seen +=1
        if not i:
            return seen
    return seen

def seen(trees, row, col):
    return seen_top(trees, row, col) * seen_bottom(trees, row, col) * seen_left(trees, row, col) * seen_right(trees, row, col)

solution = 0
b = np.zeros((len(lines), len(lines)))

for row in range(len(trees)):
    for col in range(len(trees)):
        b[row, col] = seen(trees, row, col)

print(np.amax(b))