import sys
import re
lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

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
    pipe = lines[y][x]
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
for idx, line in enumerate(lines):
    m = re.search('S', line)
    if m:
        start = (m.start(), idx)
        break
        

path1prev = (-1, -1)

paths = []

path1Flag = 0
if start[0] > 0 and 'west' in pipes[lines[start[1]][start[0]-1]]:
    paths.append(((start[0]-1, start[1]), 'west'))
        
if start[0] < len(lines[0])-1 and 'east' in pipes[lines[start[1]][start[0]+1]]:
    paths.append(((start[0]+1, start[1]), 'east'))

if start[1] > 0 and 'north' in pipes[lines[start[1]-1][start[0]]]:
     paths.append(((start[0], start[1]-1), 'north'))
     
if start[1] < len(lines)-1 and 'south' in pipes[lines[start[1]+1][start[0]]]:
    paths.append(((start[0], start[1]+1), 'south'))

path1 = paths[0]
path2 = paths[1]
path1prev = (-1, -1)
steps = 1
while path1[0] != path2[0] and path2[0] != path1prev[0]:
    print(steps)
    print(path1)
    print(path2)
    path1prev = path1
    path1 = moveThroughPipe(path1[0][0], path1[0][1], path1[1])
    path2 = moveThroughPipe(path2[0][0], path2[0][1], path2[1])
    steps += 1
    
print(steps)