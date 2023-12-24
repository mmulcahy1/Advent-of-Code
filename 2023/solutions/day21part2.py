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
    if lines[row%numRows][(col-1)%numColumns] in ['.','S']:
        neighbors.append((col-1, row))
       
    #check east
    if lines[row%numRows][(col+1)%numColumns] in ['.','S']:
        neighbors.append((col+1, row))
        
    #check north
    if lines[(row-1)%numRows][col%numColumns] in ['.','S']:
        neighbors.append((col, row-1))
        
    #check south
    if lines[(row+1)%numRows][col%numColumns] in ['.','S']:
        neighbors.append((col, row+1))
        
    return neighbors

for rowNum, line in enumerate(lines):
    if 'S' in line:
        startingPoint = (line.index('S'), rowNum)
        break


def findTotalPlots(steps):
    newPlots = set()
    visitedPlots = [set(), set()]
    newPlots.add(startingPoint)   
    visitedPlots[0].add(startingPoint)
    inactiveFlip = 1
    activeFlip  = 0 
    for i in range(steps):
        nextPlots = set()
        visitedPlotsActive = visitedPlots[activeFlip] 
        visitedPlotsInactive = visitedPlots[inactiveFlip]
        for plot in newPlots:
            neighbors = getNeighboringPlots(plot)
            for neighbor in neighbors:
                if neighbor not in visitedPlotsInactive:
                    nextPlots.add(neighbor)
            visitedPlotsInactive.update(neighbors)
        newPlots = nextPlots.copy()
        inactiveFlip ^= 1
        activeFlip ^= 1
    return len(visitedPlots[activeFlip])

#get first three points   
firstPoint = findTotalPlots(numColumns//2)
secondPoint = findTotalPlots((numColumns//2) + numColumns)
thirdPoint = findTotalPlots((numColumns//2) + (2*numColumns))

#using Newton's forward interpolation formula
s = (26501365 - numColumns//2) // numColumns
result = firstPoint + s*(secondPoint-firstPoint) + ((s*(s-1))//2) * ((thirdPoint-secondPoint)-(secondPoint-firstPoint))


print(result)
