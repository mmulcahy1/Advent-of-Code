import sys
import re
from queue import PriorityQueue

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]
rowLen = len(lines)
colLen = len(lines[0])


oppositeDirections = {'up':'down', 'down':'up','left':'right','right':'left'}

def getNeighbors(point, direction):
    possibleDirections = ['up', 'down', 'left', 'right']
    if direction != 'start':
        possibleDirections.remove(oppositeDirections[direction])  #don't go to previous point
        possibleDirections.remove(direction)   #don't go in current direction
        
    neighbors = []
    for d in possibleDirections:
        heatLoss = 0
        if d == 'up':
            for i in range(4, min(11, point[1]+1)):
                heatLoss += int(lines[point[1]-i][point[0]])
                neighbors.append(((point[0], point[1]-i), d, i))
        
        elif d == 'down':
            for i in range(4, min(11, rowLen-point[1])):
                heatLoss += int(lines[point[1]+i][point[0]])
                neighbors.append(((point[0], point[1]+i), d, i))
        
        elif d == 'right':
            for i in range(4, min(11, colLen-point[0])):
                heatLoss += int(lines[point[1]][point[0]+i])
                neighbors.append(((point[0]+i, point[1]), d, i))
        
        elif d == 'left':
            for i in range(4, min(11, point[0]+1)):
                heatLoss += int(lines[point[1]][point[0]-i])
                neighbors.append(((point[0]-i, point[1]), d, i))
            
    return neighbors


def getHeatLossInRoll(startPoint, endPoint, direction):
    heatLoss = 0
    if direction == 'up':
        for i in range(endPoint[1], startPoint[1]):
            heatLoss += int(lines[i][startPoint[0]])
    
    elif direction == 'down':
        for i in range(startPoint[1]+1, endPoint[1]+1):
            heatLoss += int(lines[i][startPoint[0]])
            
    elif direction == 'right':
        for i in range(startPoint[0]+1, endPoint[0]+1):
            heatLoss += int(lines[startPoint[1]][i])
            
    elif direction == 'left':
        for i in range(endPoint[0], startPoint[0]):
            heatLoss += int(lines[startPoint[1]][i])
            
    return heatLoss
        
q = PriorityQueue()
startPoint = ((0, 0), 'start', 0)
historyDict = {}    #stores history of the paths
q.put((0, startPoint))
target = (len(lines[0])-1, len(lines)-1)
heatLossSum = {}    #stores total heat loss for the path to the visited point, direction combination
historyDict[startPoint] = set()
heatLossSum[startPoint] = 0
orderH = {}


while q:
    u = q.get()[1]
    if u[0] == target:
        print(heatLossSum[u])
        break
    history = historyDict[u]
    neighbors = getNeighbors(u[0], u[1])
    for neighbor in neighbors:
        if neighbor not in history:
            #calculate total heat loss for neighbor in current path
            heatLoss = heatLossSum[u] + getHeatLossInRoll(u[0], neighbor[0], neighbor[1])
            #if heatLoss is less than the stored heat loss for a different path
            #or the point has not been encountered,
            #store the current heatloss to the heat loss dict
            #and add the point to the priority queue
            if neighbor not in heatLossSum or heatLoss < heatLossSum[neighbor]:
                heatLossSum[neighbor] = heatLoss
                nHist = set(historyDict[u])
                nHist.add(u)
                historyDict[neighbor] = set(nHist)
                q.put((heatLoss, neighbor))
 
