file_idx = 0
# real = 0, test = 1

files = ["day13_input.txt", "day13_test.txt"]
with open(files[file_idx]) as f:
    lines = f.read().splitlines()


def part1(lines):
    summ = 0
    mapp = []
    for line in lines:
        if line != "":
            mapp.append(line)
        else:
            cols = []
            for i in range(len(mapp[0])):
                cols.append("".join([row[i] for row in mapp]))

            for i, col in enumerate(cols):
                if i == 0:
                    continue
                if col == cols[i - 1]:
                    diff = 1
                    while True:
                        if i + diff >= len(cols) or i - 1 - diff < 0:
                            summ += i
                            break
                        if cols[i + diff] == cols[i - 1 - diff]:
                            diff += 1
                        else:
                            break

            for i, row in enumerate(mapp):
                if i == 0:
                    continue
                if row == mapp[i - 1]:
                    diff = 1
                    while True:
                        if i + diff >= len(mapp) or i - 1 - diff < 0:
                            summ += 100 * i
                            break
                        if mapp[i + diff] == mapp[i - 1 - diff]:
                            diff += 1
                        else:
                            break
            mapp = []
    return summ


def mirror(mapp, avoid=0):
    for i, row in enumerate(mapp):
        if i == 0:
            continue
        if row == mapp[i - 1]:
            diff = 1
            while True:
                if i + diff >= len(mapp) or i - 1 - diff < 0:
                    if i != avoid:
                        return i
                    break
                if mapp[i + diff] == mapp[i - 1 - diff]:
                    diff += 1
                else:
                    break
    return 0


def part2(lines):
    summ = 0
    mapp = []
    for line in lines:
        if line != "":
            mapp.append(line)
        else:
            found = False
            cols = []
            for i in range(len(mapp[0])):
                cols.append("".join([row[i] for row in mapp]))
            realh = mirror(mapp)
            realv = mirror(cols)
            for y in range(len(mapp)):
                for x in range(len(mapp[0])):
                    newrows = mapp.copy()
                    swap = {".": "#", "#": "."}
                    newrows[y] = (
                        newrows[y][:x] + swap[newrows[y][x]] + newrows[y][x + 1 :]
                    )
                    cols = []
                    for i in range(len(newrows[0])):
                        cols.append("".join([row[i] for row in newrows]))

                    hmir = mirror(newrows, avoid=realh)
                    vmir = mirror(cols, avoid=realv)

                    if hmir != realh and hmir != 0:
                        found = True
                        summ += 100 * hmir
                    if vmir != realv and vmir != 0:
                        found = True
                        summ += vmir
                    if found:
                        break
                if found:
                    break

            mapp = []
    return summ


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
