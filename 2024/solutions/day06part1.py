import sys
import re

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]
height = len(lines)
width = len(lines[0])
directions = {'^': [-1, 0], 'v': [1, 0], '<': [0, -1], '>': [0, 1]}
directionChange = {'^':'>', 'v':'<', '<':'^', '>':'v'}
direction = '^'
encountered = set()

def findStart(lines, height, width):
    for h in range(height):
        for w in range(width):
            if lines[h][w] == '^':
                encountered.add((h,w))
                return([h, w]) 
                

        

currentPos = findStart(lines, height, width)



while True:
    nextPos = [x + y for x, y in zip(currentPos, directions[direction])]

    
    if nextPos[0] in (-1, height) or nextPos[1] in (-1, width):
        print(len(encountered))
        break
    elif lines[nextPos[0]][nextPos[1]] == '#':
        direction = directionChange.get(direction)
    else:
        encountered.add((nextPos[0], nextPos[1]))
        currentPos = nextPos