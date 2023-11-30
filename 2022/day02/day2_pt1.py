with open('day2_input.txt') as f:
    lines = f.readlines()

score = 0

for i in lines:
    moves = i.strip('\n').split(' ')
    match moves[1]: # what I play
        case 'X': # rock
            score += 1
        case 'Y': # paper
            score += 2
        case 'Z': # scissors
            score += 3
    if moves in [['A','Y'], ['B','Z'], ['C','X']]: # win
        score += 6
    elif moves in [['A','X'], ['B','Y'], ['C','Z']]: # tie
        score += 3

print(score)