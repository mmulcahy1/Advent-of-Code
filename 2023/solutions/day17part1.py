import sys
import re
from queue import PriorityQueue
lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]


oppositeDirections = {'up':'down', 'down':'up','left':'right','right':'left'}

def getNeighbors(point, direction, directionCount):
    possibleDirections = {'up':0, 'down':0, 'left':0, 'right':0}
    if direction != 'start':
        del possibleDirections[oppositeDirections[direction]]   #don't go to previous point
        if directionCount == 3:
            del possibleDirections[direction]   #can't go more than 3 times in same direction
        else:
            possibleDirections[direction] = directionCount
        
    neighbors = []
    for d in possibleDirections:
        if d == 'up' and point[1] > 0:
            neighbors.append(((point[0], point[1]-1), d, possibleDirections[d]+1))
        elif d == 'down' and point[1] < len(lines) - 1:
            neighbors.append(((point[0], point[1]+1), d, possibleDirections[d]+1))
        elif d == 'right' and point[0] < len(lines[0])-1:
            neighbors.append(((point[0]+1, point[1]), d, possibleDirections[d]+1))
        elif d == 'left' and point[0] > 0:
            neighbors.append(((point[0]-1, point[1]), d, possibleDirections[d]+1))
            
    return neighbors



q = PriorityQueue()
startPoint = ((0, 0), 'start', 0)
historyDict = {}    #stores history of the paths
q.put((0, startPoint))
target = (len(lines[0])-1, len(lines)-1)
heatLossSum = {}    #stores total heat loss for the path to the visited point, direction combination
historyDict[startPoint] = set()
heatLossSum[startPoint] = 0
orderH = {}

orderH[startPoint] = []
while q:
    u = q.get()[1]
    if u[0] == target:
        print(heatLossSum[u])
        break
    history = historyDict[u]
    neighbors = getNeighbors(u[0], u[1], u[2])
    for neighbor in neighbors:
        if neighbor not in history:
            #calculate total heat loss for neighbor in current path
            heatLoss = heatLossSum[u] + int(lines[neighbor[0][1]][neighbor[0][0]])
            #if heatLoss is less than the stored heat loss for a different path
            #or the point has not been encountered,
            #store the current heatloss to the heat loss dict
            #and add the point to the priority queue
            if neighbor not in heatLossSum or heatLoss < heatLossSum[neighbor]:
                heatLossSum[neighbor] = heatLoss
                nHist = set(historyDict[u])
                nHist.add(u)
                historyDict[neighbor] = set(nHist)
                o = [n for n in orderH[u]]
                o.append(u)
                orderH[neighbor] = o
                q.put((heatLoss, neighbor))


