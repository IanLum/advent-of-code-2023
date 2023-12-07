file_idx = 0
# real = 0, test = 1

from collections import Counter

files = ["day7_input.txt", "day7_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()


def hand_rank(hand):
    matches = list(Counter(hand).items())
    matches.sort(reverse=True, key=lambda x: x[1])

    match matches[0][1]:
        case 5:
            return 6
        case 4:
            return 5
        case 3:
            if matches[1][1] == 2:
                return 4
            else:
                return 3
        case 2:
            if matches[1][1] == 2:
                return 2
            else:
                return 1
        case 1:
            return 0


def part1(lines):
    cardval = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    hands = []
    for line in lines:
        hands.append(line.split(" "))

    hands.sort(
        key=lambda x: (
            hand_rank(x[0]),
            int(cardval.get(x[0][0], x[0][0])),
            int(cardval.get(x[0][1], x[0][1])),
            int(cardval.get(x[0][2], x[0][2])),
            int(cardval.get(x[0][3], x[0][3])),
            int(cardval.get(x[0][4], x[0][4])),
        )
    )
    summ = 0
    for i, handt in enumerate(hands):
        summ += (i + 1) * int(handt[1])
    return summ


def hand_rank2(hand):
    matches = list(Counter(hand).items())
    matches.sort(reverse=True, key=lambda x: x[1])
    if matches[0][0] != "J":
        hand = hand.replace("J", matches[0][0])
    elif matches[0][1] != 5:
        hand = hand.replace("J", matches[1][0])
    matches = list(Counter(hand).items())
    matches.sort(reverse=True, key=lambda x: x[1])

    match matches[0][1]:
        case 5:
            return 6
        case 4:
            return 5
        case 3:
            if matches[1][1] == 2:
                return 4
            else:
                return 3
        case 2:
            if matches[1][1] == 2:
                return 2
            else:
                return 1
        case 1:
            return 0


def part2(lines):
    cardval = {"A": 14, "K": 13, "Q": 12, "J": -1, "T": 10}
    hands = []
    for line in lines:
        hands.append(line.split(" "))

    hands.sort(
        key=lambda x: (
            hand_rank2(x[0]),
            int(cardval.get(x[0][0], x[0][0])),
            int(cardval.get(x[0][1], x[0][1])),
            int(cardval.get(x[0][2], x[0][2])),
            int(cardval.get(x[0][3], x[0][3])),
            int(cardval.get(x[0][4], x[0][4])),
        )
    )
    summ = 0
    for i, handt in enumerate(hands):
        summ += (i + 1) * int(handt[1])

    return summ


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
