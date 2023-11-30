with open('day4_input.txt') as f:
    lines = f.read().splitlines()

overlap = 0

for line in lines:
    [p1range, p2range] = line.split(',')
    p1range = p1range.split('-')
    p2range = p2range.split('-')

    p1shifts = set(range(int(p1range[0]), int(p1range[1])+1))
    p2shifts = set(range(int(p2range[0]), int(p2range[1])+1))

    if p1shifts.intersection(p2shifts) != set():
        overlap += 1

print(overlap)