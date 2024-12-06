import sys
import pdb

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]
height = len(lines)
width = len(lines[0])
directions = {'^': [-1, 0], 'v': [1, 0], '<': [0, -1], '>': [0, 1]}
directionChange = {'^':'>', 'v':'<', '<':'^', '>':'v'}
direction = '^'
encountered = set()
obstacles = set()
obstacleAttempts = set()
result = 0

def findStart(lines, height, width):
    for h in range(height):
        for w in range(width):
            if lines[h][w] == '^':
                encountered.add((h,w,'^'))
                obstacleAttempts.add((h,w))
                return([h, w]) 

def isLoop(cPos, d, e, grid):
    while True:
        nPos = [x + y for x, y in zip(cPos, directions[d])]
        # print('\n')
        # print('cpos: ' + str(cPos))
        # print(d)

        if (nPos[0], nPos[1], d) in e:
            return True
    
        elif nPos[0] in (-1, height) or nPos[1] in (-1, width):
            return False
        elif grid[nPos[0]][nPos[1]] == '#':
            d = directionChange.get(d)
        else:
            e.add((nPos[0], nPos[1], d))
            cPos = nPos

currentPos = findStart(lines, height, width)
direction = '^'
#pdb.set_trace()
while True:
    nextPos = [x + y for x, y in zip(currentPos, directions[direction])]
    
    if nextPos[0] in (-1, height) or nextPos[1] in (-1, width):
        print(len(obstacles))
        break
    elif lines[nextPos[0]][nextPos[1]] == '#':
        direction = directionChange.get(direction)
    else:
        if (nextPos[0],nextPos[1]) not in obstacleAttempts:
            withObstacle =[list(line) for line in lines]
            withObstacle[nextPos[0]][nextPos[1]] = '#'
            # print('obstacle: ' + str(nextPos))
            if isLoop(currentPos, direction, encountered.copy(), withObstacle):
                obstacles.add((nextPos[0], nextPos[1]))
            obstacleAttempts.add((nextPos[0], nextPos[1]))
        encountered.add((nextPos[0], nextPos[1], direction))
        currentPos = nextPos