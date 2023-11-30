with open('calories.txt') as f:
    lines = f.readlines()
cals = []
currentcals = 0
for i in lines:
    line = i.strip('\n')
    if line == '': # this is doesn't catch the last line
        cals.append(currentcals)
        currentcals = 0
    else:
        currentcals += int(line)
cals.sort(reverse = True)
print(sum(cals[:3]))