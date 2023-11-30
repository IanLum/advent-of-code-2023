with open('day4_input.txt') as f:
    lines = f.read().splitlines()

pairs = 0

for line in lines:
    [p1range, p2range] = line.split(',')
    p1range = p1range.split('-')
    p2range = p2range.split('-')

    p1shifts = set(range(int(p1range[0]), int(p1range[1])+1))
    p2shifts = set(range(int(p2range[0]), int(p2range[1])+1))

    if p1shifts.issubset(p2shifts) or p2shifts.issubset(p1shifts):
        pairs += 1

print(pairs)