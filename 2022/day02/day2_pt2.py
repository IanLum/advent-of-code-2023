with open('day2_input.txt') as f:
    lines = f.readlines()

score = 0

for i in lines:
    moves = i.strip('\n').split(' ')
    match moves[1]: # what happens
        case 'X': # lose
            score += 0
        case 'Y': # tie
            score += 3
        case 'Z': # win
            score += 6
    if moves in [['A','Y'], ['B','X'], ['C','Z']]: # rock
        score += 1
    elif moves in [['A','Z'], ['B','Y'], ['C','X']]: # paper
        score += 2
    else: # scissors
        score += 3

print(score)