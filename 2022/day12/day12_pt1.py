import numpy as np
from enum import Enum

class Direction(Enum):
    UP: 1
    RIGHT: 2
    DOWN: 3
    LEFT: 4

# 1 for test, 0 for real input
test = 1

if test:
    file = 'day12_test.txt'
else:
    file = 'day12_input.txt'
with open(file) as f:
    lines = f.read().splitlines()
    
def feasible_direction(map, pos):
    feas = {
        'up': False,
        'right': False,
        'down': False,
        'left': False,
    }
    loc_height = ord(map[pos[0]][pos[1]])
    if loc_height == 'S':
        loc_height = ord('a')
    elif loc_height == 'E':
        loc_height = ord('z')
    
    if pos[0] != 0: # up
        if abs(ord(map[pos[0]-1][pos[1]]) - loc_height) <= 1:
            feas['up'] = True

    if pos[0] != len(map) - 1: # down
        if abs(ord(map[pos[0]+1][pos[1]]) - loc_height) <= 1:
            feas['down'] = True

    if pos[1] != 0: # left
        if abs(ord(map[pos[0]][pos[1]-1]) - loc_height) <= 1:
            feas['left'] = True

    if pos[1] != len(map) - 1: # right
        if abs(ord(map[pos[0]][pos[1]+1]) - loc_height) <= 1:
            feas['right'] = True

    return feas

def where_go(map, cur_pos, goal_pos):
    row_dist = cur_pos[0] - goal_pos[0]
    col_dist = cur_pos[1] - goal_pos[1]

    if col_dist > row_dist:
        if 

map = np.array([list(i) for i in lines])

current_pos = np.where(map == 'S')
map[current_pos[0][0]][current_pos[1][0]] = 'a'
goal_pos = np.where(map == 'E')
map[goal_pos[0][0]][goal_pos[1][0]] = 'z'
# print(current_pos[0][0], current_pos[1][0])
# print(goal_pos[0][0], goal_pos[1][0])
feasible_direction(map, (1,6))