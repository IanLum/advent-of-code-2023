# 1 for test, 0 for real input
test = 0

if test:
    file = 'day06_test.txt'
else:
    file = 'day06_input.txt'
with open(file) as f:
    lines = f.read().splitlines()

solution = 3

# lines = ['bvwbjplbgvbhsrlpgdmjqwftvncz']

for idx,i in enumerate(lines[0][4:]):
    exit = True
    solution += 1
    b = lines[0][idx:(idx+4)]
    for j in b:
        if list(b).count(j) > 1:
            exit = False
    if exit:
        break

print(solution)

# print(lines[0][1988-5:1988])