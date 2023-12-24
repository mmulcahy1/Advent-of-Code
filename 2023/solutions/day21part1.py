import sys
import re
lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

numColumns = len(lines[0])
numRows = len(lines)

def getNeighboringPlots(point):
    col = point[0]
    row = point[1]
    
    neighbors = []
    
    #check west
    if col > 0 and lines[row][col-1] in ['.','S']:
        neighbors.append((col-1, row))
       
    #check east
    if col < numColumns - 1 and lines[row][col+1] in ['.','S']:
        neighbors.append((col+1, row))
        
    #check north
    if row > 0 and lines[row-1][col] in ['.','S']:
        neighbors.append((col, row-1))
        
    #check south
    if row < numRows - 1 and lines[row+1][col] in ['.','S']:
        neighbors.append((col, row+1))
        
    return neighbors

for rowNum, line in enumerate(lines):
    if 'S' in line:
        startingPoint = (line.index('S'), rowNum)
        break

currentPlots = set()
currentPlots.add(startingPoint)        
for i in range(64):
    nextPlots = set()
    for plot in currentPlots:
        neighbors = getNeighboringPlots(plot)
        nextPlots.update(neighbors)
    currentPlots = nextPlots.copy()
    
result = len(currentPlots)
print(result)
