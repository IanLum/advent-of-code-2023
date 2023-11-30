with open('day3_input.txt') as f:
    lines = f.read().splitlines()

prio = 0

for bag_items in lines:
    half = int(len(bag_items)/2)
    p1 = set(bag_items[:half])
    p2 = set(bag_items[half:])
    common = p1.intersection(p2).pop()
    if common.isupper():
        prio += ord(common) - 38
    else:
        prio += ord(common) -96

print(prio)