with open('day3_input.txt') as f:
    lines = f.read().splitlines()

prio = 0

for bag_items in lines:
    half = int(len(bag_items)/2)
    comp1_items = bag_items[:half]
    comp2_items = bag_items[half:]
    unique1 = set(comp1_items)
    unique2 = set(comp2_items)

    for item in unique1:
        if item in unique2:
            if item.isupper():
                prio += ord(item) - 38
            else:
                prio += ord(item) -96

print(prio)