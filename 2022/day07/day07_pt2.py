# 1 for test, 0 for real input
test = 0

if test:
    file = 'day07_test.txt'
else:
    file = 'day07_input.txt'
with open(file) as f:
    lines = f.read().splitlines()

dir_contains = {}

for idx, i in enumerate(lines):
    if i == '$ ls':
        dir = lines[idx-1].split(' ')[-1]
        dir_contains[dir] = []
        dir_size = 0
        in_dir = True
        idx2 = idx + 1
        while in_dir:
            if lines[idx2][0] == "$":
                in_dir = False
            elif lines[idx2][0] == "d":
                dir_contains[dir].append(lines[idx2].split(' ')[-1])
            else:
                dir_size += int(lines[idx2].split(' ')[0])
            idx2 += 1
        dir_contains[dir].append(dir_size)

dir_real_size = {}

for dir in dir_contains:
    dir_stuff = dir_contains[dir]
    while not all(type(x) == int for x in dir_stuff):
        if type(dir_stuff[0]) == int:
            dir_stuff.append(dir_stuff[0])
        elif dir_contains[dir_stuff[0]] != []:
            dir_stuff.extend(dir_contains[dir_stuff[0]])
        dir_stuff.pop(0)
    dir_real_size[dir] = sum(dir_stuff)

smallest_size = 1000000000000000000
for i in dir_real_size:
    if dir_real_size[i] - 6552309 >= 0 and dir_real_size[i] < smallest_size:
        smallest_size = dir_real_size[i]

print(smallest_size)