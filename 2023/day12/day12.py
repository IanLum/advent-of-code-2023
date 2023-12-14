file_idx = 0
# real = 0, test = 1

from itertools import product
from functools import cache
import re

files = ["day12_input.txt", "day12_test.txt", "test2.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()


def part1(lines):
    summ = 0
    for i, line in enumerate(lines):
        [springs, mapp] = line.split(" ")
        mapp = list(map(int, mapp.split(",")))
        unknown = springs.count("?")
        combs = ["".join(x) for x in product(["#", "."], repeat=unknown)]
        for comb in combs:
            ct = 0
            attempt = ""
            for char in springs:
                if char == "?":
                    attempt += comb[ct]
                    ct += 1
                else:
                    attempt += char
            counts = list(map(len, re.findall("#+", attempt)))
            if counts == mapp:
                summ += 1
    return summ


@cache
def arrangements(springs: str, damaged: tuple, debug=False):
    springs = springs.lstrip(".")
    if debug:
        print(springs, damaged)

    # if no more groups, it's a valid arrangement if there are no more damaged springs
    if damaged == ():
        if "#" not in springs:
            if debug:
                print("success")
            return 1
        else:
            if debug:
                print("damaged empty")
            return 0

    # at this point, we know damaged isn't empty, so we expect to have damaged or unknown springs in the springs string
    if "#" not in springs and "?" not in springs:
        if debug:
            print("expected damaged springs, found none")
        return 0

    # now we know there are damaged springs, and damaged spring groups we're looking for

    # if we see a ? in front, try either option ., or #
    if springs[0] == "?":
        if debug:
            print("branching")
        return arrangements("." + springs[1:], damaged, debug=debug) + arrangements(
            "#" + springs[1:], damaged, debug=debug
        )
    # at this point, we know it's a # in front
    else:
        fst_group = damaged[0]

        # can't make first group
        # either there aren't enough springs or a working spring (.) is in the way
        if len(springs) < fst_group or "." in springs[:fst_group]:
            if debug:
                print("can't make first group")
            return 0

        # from the if above, we already know there are only ?s and #s in the length of the first group
        # check to make sure the group ends with a . or ?
        elif springs[fst_group] == "#":
            # if theres a # after the first group, fail
            if debug:
                print("fails because # after first group")
            return 0

        # at this point, the first group is valid
        else:
            # keep solving after the group
            if debug:
                print("moving on")
            return arrangements(springs[fst_group + 1 :], damaged[1:], debug=debug)


def part2(lines):
    summ = 0
    for i, line in enumerate(lines):
        [springs, mapp] = line.split(" ")
        springs = springs + ("?" + springs) * 4
        mapp = tuple(map(int, mapp.split(","))) * 5
        a = arrangements(springs + ".", mapp, debug=False)
        summ += a
    return summ


# print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
