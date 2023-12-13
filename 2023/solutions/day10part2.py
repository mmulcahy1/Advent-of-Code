import sys
import re
import random
lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

grid = []
originalPipes = []
for line in lines:
    grid.append(list(line))
    originalPipes.append(line)

pipes = {
    '|': {'north': 'north', 'south': 'south'},
    '-': {'east': 'east', 'west': 'west'},
    'L': {'south': 'east', 'west': 'north'},
    'J': {'south': 'west', 'east': 'north'},
    '7': {'north': 'west', 'east': 'south'},
    'F': {'north': 'east', 'west': 'south'},
    '.':{}
}


def moveThroughPipe(x, y, direction):
    pipe = grid[y][x]
    nextDirection = pipes[pipe][direction]
    
    match nextDirection:
        case 'north':
            y -= 1
        case 'south':
            y += 1
        case 'west':
            x -= 1
        case 'east':
            x += 1
            
    return ((x, y), nextDirection)
        
    

#find S, the starting point
for idx, gridLine in enumerate(grid):
    if 'S' in gridLine:
        start = (gridLine.index('S'), idx)
        break
        

path1prev = (-1, -1)

paths = []

path1Flag = 0
possiblePipes = []
if start[0] > 0 and 'west' in pipes[grid[start[1]][start[0]-1]]:
    paths.append(((start[0]-1, start[1]), 'west'))
    possiblePipes.extend(['7', '-', 'J',])
        
if start[0] < len(grid[0])-1 and 'east' in pipes[grid[start[1]][start[0]+1]]:
    paths.append(((start[0]+1, start[1]), 'east'))
    possiblePipes.extend(['-','F','L'])

if start[1] > 0 and 'north' in pipes[grid[start[1]-1][start[0]]]:
     paths.append(((start[0], start[1]-1), 'north'))
     possiblePipes.extend(['|','J','L'])
     
if start[1] < len(grid)-1 and 'south' in pipes[grid[start[1]+1][start[0]]]:
    paths.append(((start[0], start[1]+1), 'south'))
    possiblePipes.extend(['|','7','F'])

path1 = paths[0]
path2 = paths[1]

sPipe = [i for i in possiblePipes if possiblePipes.count(i) == 2][0]

grid[start[1]][start[0]] = sPipe
print(sPipe)
originalPipes[start[1]] = ''.join(grid[start[1]])

coords = []
coords.append(start)
path1prev = (-1, -1)
steps = 1
grid[start[1]][start[0]]= 'C'
while path1[0] != start:
    coords.append(path1[0])
    path1prev = path1
    path1 = moveThroughPipe(path1[0][0], path1[0][1], path1[1])
    steps += 1

area = 0
#shoelace formula
for i in range(1, len(coords)):
    area += (coords[(i+1) % (len(coords))][0]+coords[i][0]) * (coords[(i+1) % (len(coords))][1] - coords[i][1])
area = abs(area) / 2

#Pick's theorem
points = area +1 - (steps / 2)
print(points)