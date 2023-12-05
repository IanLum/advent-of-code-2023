file_idx = 0
# real = 0, test = 1

from collections import defaultdict

files = ["day5_input.txt", "day5_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()


def part1(lines):
    seeds = []
    for i, line in enumerate(lines):
        if i == 0:
            seednums = map(int, line.split(": ")[1].split(" "))
            for num in seednums:
                seeddict = defaultdict(int)
                seeddict["seed"] = num
                seeds.append(seeddict)
        elif "-to-" in line:
            [sourc, _, dest] = line.split(" ")[0].split("-")
        elif line != "":
            dest_start, sourc_start, leng = map(int, line.split(" "))
            for seed in seeds:
                if seed[sourc] in range(sourc_start, sourc_start + leng):
                    seed[dest] = seed[sourc] + (dest_start - sourc_start)
                elif seed[dest] == 0:
                    seed[dest] = seed[sourc]

    return min([i["location"] for i in seeds])


def chunk(rang, bounds):
    intersecting_bounds = list(filter(lambda x: x in rang and x != rang.start, bounds))
    if intersecting_bounds == []:
        return [rang]
    else:
        splt = intersecting_bounds[0]
        return chunk(range(rang.start, splt), bounds) + chunk(
            range(splt, rang.stop), bounds
        )


# this solution requires you to add two new lines to the end of the inputs
def part2(lines):
    seeds = defaultdict(list)
    for i, line in enumerate(lines):
        if i == 0:
            seednums = map(int, line.split(": ")[1].split(" "))
            seedpairs = zip(*(iter(seednums),) * 2)
            seeds["seed"] = list(
                map(lambda x: range(x[0], x[0] + x[1]), list(seedpairs))
            )
        elif i == 1:
            continue
        elif "-to-" in line:
            [sourc, _, dest] = line.split(" ")[0].split("-")
            mapp = []
        elif line != "":
            dest_start, sourc_start, leng = map(int, line.split(" "))
            mapp.append(
                (
                    range(sourc_start, sourc_start + leng),
                    range(dest_start, dest_start + leng),
                )
            )
        elif line == "":
            mapp.sort(key=lambda x: x[0].start)
            map_sourc_bounds = sum([[i[0].start, i[0].stop] for i in mapp], [])
            chunked = []
            for rang in seeds[sourc]:
                chunked += chunk(rang, map_sourc_bounds)

            for c in chunked:
                mapped = False
                for map_sourc, map_dest in mapp:
                    if c.start in map_sourc:
                        diff = map_dest.start - map_sourc.start
                        seeds[dest].append(range(c.start + diff, c.stop + diff))
                        mapped = True
                        break
                if not mapped:
                    seeds[dest].append(c)
            # seeds[dest].sort(key=lambda x: x.start)

    # for i in seeds.items():
    #     print(i)

    return min(seeds["location"], key=lambda x: x.start).start


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
