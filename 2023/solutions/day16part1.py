import sys
import re
lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

result = 0

energized = [list(line) for line in lines]

beams = []
beams.append([[0,0], 'right'])
history = []
while beams:
    beam = beams.pop()
    currPosition = beam[0]
    direction = beam[1]
    
    x = currPosition[0]
    y = currPosition[1]
    
    #check if beam is still in grid and the beam direction and posiition have not been encountered yet
    if x < len(lines[0]) and x >= 0 and y < len(lines) and y >= 0 and beam not in history:
    
        history.append(beam)
        
        if energized[y][x] != '#':
            result += 1
            energized[y][x] = '#'
        
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
                beams.append([[x+1, y], d])
            elif d == 'left':
                beams.append([[x-1, y], d])
            elif d == 'up':
                beams.append([[x, y-1], d])
            elif d == 'down':
                beams.append([[x, y+1], d])
                    

print(result)