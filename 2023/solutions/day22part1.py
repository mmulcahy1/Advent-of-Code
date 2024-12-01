import sys
import re
lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]


        
maxX = 0
maxY = 0
maxZ = 0
bricks = []
for line in lines:
    brick = []
    brickInfo = line.split('~')
    firstEdge = [int(n) for n in re.findall(r'\d+', brickInfo[0])]
    secondEdge = [int(n) for n in re.findall(r'\d+', brickInfo[1])]
    brick.append(firstEdge)
    brick.append(secondEdge)
    bricks.append(brick)
    maxX = max(maxX, firstEdge[0], secondEdge[0])
    maxY = max(maxY, firstEdge[1], secondEdge[1])
    maxZ = max(maxZ, firstEdge[2], secondEdge[2])
    
print(maxX)
print(maxY)
print(maxZ)
