import sys
import re
import numpy as np
lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

def findEnergized(startBeam):
    result = 0

    energized = []

    beams = []
    beams.append(startBeam)
    history = set()
    while beams:
        beam = beams.pop()
        direction = beam[2]
        
        x = beam[0]
        y = beam[1]
        
        #check if beam is still in grid and the beam direction and posiition have not been encountered yet
        if x in range(len(lines[0])) and y in range(len(lines)) and beam not in history:
        
            history.add(beam)
            
            
            tile = lines[y][x]
            
            nextDirection = []
            
            if tile == '.':
                nextDirection.append(direction)
            elif tile == '/':
                if direction == 'right':
                    nextDirection.append('up')
                elif direction == 'left':
                    nextDirection.append('down')
                elif direction == 'up':
                    nextDirection.append('right')
                elif direction == 'down':
                    nextDirection.append('left')
            elif tile == '\\':
                if direction == 'right':
                    nextDirection.append('down')
                elif direction == 'left':
                    nextDirection.append('up')
                elif direction == 'up':
                    nextDirection.append('left')
                elif direction == 'down':
                    nextDirection.append('right')
            elif tile == '|':
                if direction in ['right', 'left']:
                    nextDirection.extend(['up', 'down'])
                else:
                    nextDirection.append(direction)
            elif tile == '-':
                if direction in ['up', 'down']:
                    nextDirection.extend(['right', 'left']) 
                else:
                    nextDirection.append(direction)
                    
            for d in nextDirection:
                if d == 'right':
                    beams.append((x+1, y, d))
                elif d == 'left':
                    beams.append((x-1, y, d))
                elif d == 'up':
                    beams.append((x, y-1, d))
                elif d == 'down':
                    beams.append((x, y+1, d))
    return len(set([(x,y) for x, y, _ in history]))


maxEnergized = 0
for ycoord in range(len(lines)):
    maxEnergized = max(findEnergized((0, ycoord, 'right')), maxEnergized)
    maxEnergized = max(findEnergized((len(lines[0])-1, ycoord, 'left')), maxEnergized)
    
for xcoord in range(len(lines[0])):
    maxEnergized = max(findEnergized((xcoord, 0, 'down')), maxEnergized)
    maxEnergized = max(findEnergized((xcoord, len(lines)-1, 'up')), maxEnergized)   

                    

print(maxEnergized )