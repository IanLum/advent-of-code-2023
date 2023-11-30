with open('test.txt') as cals:
    lines = cals.readlines()
maxcals = 0
currentcals = 0
for i in lines:
    line = i.strip('\n')
    if line == '': # this is doesn't catch the last line
        if currentcals > maxcals:
            maxcals = currentcals
            print(maxcals)
        currentcals = 0
    else:
        currentcals += int(line)
print(maxcals)