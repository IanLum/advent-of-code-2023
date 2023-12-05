file_idx = 0
# real = 0, test = 1

from collections import defaultdict

files = ["day5_input.txt", "day5_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()


def part1(lines):
    seeds = []
    seed2soil = defaultdict(int)
    soil2fert = defaultdict(int)
    fert2water = defaultdict(int)
    water2light = defaultdict(int)
    light2temp = defaultdict(int)
    temp2hum = defaultdict(int)
    hum2loc = defaultdict(int)
    curr = {}
    for i, line in enumerate(lines):
        print(line)
        if i == 0:
            seeds = line.split(": ")[1].split(" ")
        elif "-to-" in line:
            word = line.split("-")[0]
            match word:
                case "seed":
                    curr = seed2soil
                case "soil":
                    curr = soil2fert
                case "fertilizer":
                    curr = fert2water
                case "water":
                    curr = water2light
                case "light":
                    curr = light2temp
                case "temperature":
                    curr = temp2hum
                case "humidity":
                    curr = hum2loc
        elif line != "":
            dest, sourc, leng = line.split(" ")
            for i in range(int(leng)):
                curr[int(sourc) + i] = int(dest) + i

    locs = []
    for seed in seeds:
        soil = seed2soil.get(int(seed), int(seed))
        fert = soil2fert.get(soil, soil)
        water = fert2water.get(fert, fert)
        light = water2light.get(water, water)
        temp = light2temp.get(light, light)
        hum = temp2hum.get(temp, temp)
        loc = hum2loc.get(hum, hum)
        locs.append(loc)
    return min(locs)


def part2(lines):
    pass


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
