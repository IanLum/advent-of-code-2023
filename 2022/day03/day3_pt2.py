with open('day3_input.txt') as f:
    lines = f.read().splitlines()

prio = 0

for group in range(int(len(lines)/3)):
    p1 = set(lines[group*3])
    p2 = set(lines[group*3+1])
    p3 = set(lines[group*3+2])
    common = p1.intersection(p2).intersection(p3).pop()
    if common.isupper():
        prio += ord(common) - 38
    else:
        prio += ord(common) -96

print(prio)