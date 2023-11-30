# 1 for test, 0 for real input
test = 1

if test:
    file = 'day[DAY]_test.txt'
else:
    file = 'day[DAY]_input.txt'
with open(file) as f:
    lines = f.read().splitlines()

solution = 0

print(solution)