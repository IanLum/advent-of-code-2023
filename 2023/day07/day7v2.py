file_idx = 0
# real = 0, test = 1

from collections import Counter

files = ["day7_input.txt", "day7_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()


def hand_rank(hand, pt2=False):
    if pt2:
        mostcom = Counter(hand).most_common(2)
        if mostcom[0][0] != "J":
            hand = hand.replace("J", mostcom[0][0])
        elif mostcom[0][1] != 5:
            hand = hand.replace("J", mostcom[1][0])

    matches = list(Counter(hand).values())
    matches.sort(reverse=True)

    match matches[0]:
        case 5:
            return 6
        case 4:
            return 5
        case 3:
            if matches[1] == 2:
                return 4
            else:
                return 3
        case 2:
            if matches[1] == 2:
                return 2
            else:
                return 1
        case 1:
            return 0


def part1(lines):
    cardval = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    hands = list(
        map(
            lambda x: {"hand": x[0], "bid": int(x[1])},
            map(lambda x: x.split(" "), lines),
        )
    )
    hands.sort(
        key=lambda x: (
            [hand_rank(x["hand"])]
            + [int(cardval.get(x["hand"][i], x["hand"][i])) for i in range(5)]
        )
    )
    summ = 0
    for i, hand in enumerate(hands):
        summ += (i + 1) * hand["bid"]
    return summ


def part2(lines):
    cardval = {"A": 14, "K": 13, "Q": 12, "J": -1, "T": 10}
    hands = list(
        map(
            lambda x: {"hand": x[0], "bid": int(x[1])},
            map(lambda x: x.split(" "), lines),
        )
    )
    hands.sort(
        key=lambda x: (
            [hand_rank(x["hand"], pt2=True)]
            + [int(cardval.get(x["hand"][i], x["hand"][i])) for i in range(5)]
        )
    )
    summ = 0
    for i, hand in enumerate(hands):
        summ += (i + 1) * hand["bid"]
    return summ


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
