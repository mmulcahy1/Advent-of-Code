import sys
import re
lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]


totalLoad = 0
emptySpacesAbove = [0] * len(lines[0])


for lineIdx, line in enumerate(lines):
    rowsToSouth = len(lines) - lineIdx
    for positionIdx, position in enumerate(line):
        if position == 'O':
            totalLoad += rowsToSouth + emptySpacesAbove[positionIdx]
        elif position == "#":
            emptySpacesAbove[positionIdx] = 0
        else:
            emptySpacesAbove[positionIdx] += 1
            
print(totalLoad)
            
            
        