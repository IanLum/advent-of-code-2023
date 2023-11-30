# 1 for test, 0 for real input
test = 0

if test:
    file = 'day05_test.txt'
else:
    file = 'day05_input.txt'
with open(file) as f:
    lines = f.read().splitlines()

#   [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

test_crates = [['Z','N'], ['M','C','D'],['P']]

# [S]                 [T] [Q]        
# [L]             [B] [M] [P]     [T]
# [F]     [S]     [Z] [N] [S]     [R]
# [Z] [R] [N]     [R] [D] [F]     [V]
# [D] [Z] [H] [J] [W] [G] [W]     [G]
# [B] [M] [C] [F] [H] [Z] [N] [R] [L]
# [R] [B] [L] [C] [G] [J] [L] [Z] [C]
# [H] [T] [Z] [S] [P] [V] [G] [M] [M]
#  1   2   3   4   5   6   7   8   9 

s1 = 'HRBDZFLS'
s2 = 'TBMZR'
s3 = 'ZLCHNS'
s4 = 'SCFJ'
s5 = 'PGHWRZB'
s6 = 'VJZGDNMT'
s7 = 'GLNWFSPQ'
s8 = 'MZR'
s9 = 'MCLGVRT'

real_crates = [[*s1],[*s2],[*s3],[*s4],[*s5],[*s6],[*s7],[*s8],[*s9]]

crates = real_crates

ints = '1234567890'

for line in lines:
    move = []
    for i in line:
        if i in ints:
            move.append(int(i))
    if len(move) == 4:
        move = [int(str(move[0])+str(move[1])), move[2], move[3]]
    for i in range(move[0]):
        crates[move[2]-1].append(crates[move[1]-1].pop())

for i in crates:
    print(i[-1])