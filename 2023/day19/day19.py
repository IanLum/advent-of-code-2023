file_idx = 1
# real = 0, test = 1

files = ["day19_input.txt", "day19_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()

import re
from itertools import product


def parse_workflows(wf_raw):
    workflows = {}
    for wf in wf_raw:
        name, rules = wf[:-1].split("{")

        for rule in reversed(rules.split(",")):
            if ":" not in rule:
                func = lambda part, rule=rule: rule
            else:
                cat, op, val, dest = re.findall(
                    "([a-z])([<>])([0-9]+):([a-zA-Z]+)", rule
                )[0]
                else_case = func
                match op:
                    case ">":
                        func = (
                            lambda part, cat=cat, val=val, dest=dest, else_case=else_case: dest
                            if part[cat] > int(val)
                            else else_case(part)
                        )
                    case "<":
                        func = (
                            lambda part, cat=cat, val=val, dest=dest, else_case=else_case: dest
                            if part[cat] < int(val)
                            else else_case(part)
                        )
        workflows[name] = func
    return workflows


def parse_parts(parts_raw):
    parts = []
    for raw in parts_raw:
        x, m, a, s = list(map(int, re.findall("[0-9]+", raw)))
        parts.append({"x": x, "m": m, "a": a, "s": s})
    return parts


def check_part(part, workflows, wf):
    res = workflows[wf](part)
    match res:
        case "A":
            return True
        case "R":
            return False
        case _:
            return check_part(part, workflows, res)


def part1(lines):
    blank = lines.index("")
    workflows = parse_workflows(lines[:blank])
    parts = parse_parts(lines[blank + 1 :])
    summ = 0
    for part in parts:
        if check_part(part, workflows, "in"):
            summ += sum(part.values())
    return summ


def part2(lines):
    blank = lines.index("")
    workflows = parse_workflows(lines[:blank])
    parts = []
    for x, m, a, s in product(range(1, 4), range(1, 4), range(1, 4), range(1, 4)):
        parts.append({"x": x, "m": m, "a": a, "s": s})
    summ = 0
    for part in parts:
        print(part)
        if check_part(part, workflows, "in"):
            summ += 1
    return summ


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
