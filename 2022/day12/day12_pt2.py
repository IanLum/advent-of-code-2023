# 1 for test, 0 for real input
test = 1

if test:
    file = 'day12_test.txt'
else:
    file = 'day12_input.txt'
with open(file) as f:
    lines = f.read().splitlines()

solution = 0

print(solution)