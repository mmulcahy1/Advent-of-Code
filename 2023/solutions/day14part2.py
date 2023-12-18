import sys
import re
lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

def rollRocks(rockLines, direction):
    if direction == 'north':
        for x in range(0, len(rockLines[0])):
            validEmptySpace = -1
            for y in range(0, len(rockLines)):
                position = rockLines[y][x]
                if position == 'O' and validEmptySpace != -1:
                    rockLines[validEmptySpace][x] = 'O'
                    rockLines[y][x] = '.'
                    validEmptySpace += 1
                    
                elif position == '#':
                    validEmptySpace = -1
                    
                elif position == '.':
                    if validEmptySpace == -1:
                        validEmptySpace = y
                        
        return rockLines
    
    elif direction == 'south':
        for x in range(0, len(rockLines[0])):
            validEmptySpace = -1
            for y in range(len(rockLines)-1, -1, -1):
                position = rockLines[y][x]
                if position == 'O' and validEmptySpace != -1:
                    rockLines[validEmptySpace][x] = 'O'
                    rockLines[y][x] = '.'
                    validEmptySpace -= 1
                    
                elif position == '#':
                    validEmptySpace = -1
                    
                elif position == '.':
                    if validEmptySpace == -1:
                        validEmptySpace = y
                        
        return rockLines
    
    elif direction == 'west':
        for y in range(0, len(rockLines)):
            validEmptySpace = -1
            for x in range(0, len(rockLines[0])):
                position = rockLines[y][x]
                if position == 'O' and validEmptySpace != -1:
                    rockLines[y][validEmptySpace] = 'O'
                    rockLines[y][x] = '.'
                    validEmptySpace += 1
                    
                elif position == '#':
                    validEmptySpace = -1
                    
                elif position == '.':
                    if validEmptySpace == -1:
                        validEmptySpace = x
                        
        return rockLines

    elif direction == 'east':
        for y in range(0, len(rockLines)):
            validEmptySpace = -1
            for x in range(len(rockLines[0])-1, -1, -1):
                position = rockLines[y][x]
                if position == 'O' and validEmptySpace != -1:
                    rockLines[y][validEmptySpace] = 'O'
                    rockLines[y][x] = '.'
                    validEmptySpace -= 1
                    
                elif position == '#':
                    validEmptySpace = -1
                    
                elif position == '.':
                    if validEmptySpace == -1:
                        validEmptySpace = x
                        
        return rockLines


rockLines = []           
for line in lines:
    rockLines.append(list(line))
  
i = 0
directions = ['north', 'west', 'south', 'east']
#dictionaries of encpuntered rock patterns for each direction
repeats = [{}, {}, {}, {}] 
foundLoop = False
#1000000000 means 4000000000 rolls
while i < 4000000000:
    print(i)
    rockLines = rollRocks(rockLines, directions[i % 4])
    if not foundLoop:
        s = ''
        for rockLine in rockLines:
            s += ''.join(rockLine)
        #if rock pattern for this direction already encountered
        #a loop exists
        #find remaining rolls after the last loop
        if s in repeats[i%4]:
            loopRolls = i - repeats[i%4][s]
            remainingRolls = (4000000000 - i) % loopRolls
            i = 4000000000 - remainingRolls
            foundLoop = True
        else:
            repeats[i%4][s] = i
            i += 1
    else:
        i += 1

totalLoad = 0            
for rockLineIdx, rockLine in enumerate(rockLines):
    r = ''.join(rockLine)
    totalLoad += len(re.findall('O', r)) * (len(rockLines) - rockLineIdx)
    
print(totalLoad)