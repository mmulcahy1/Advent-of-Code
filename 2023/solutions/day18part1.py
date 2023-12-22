import sys
import re
import random
lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

start = [1000000000,1000000000]
grid = ['.'] * 10000
vertices = [start]
curr = start
border = 0
prev = ''
for line in lines:
    direction = line[0]
    meters = int(re.search(r'\d+', line)[0])
    border += meters
    
    if direction == 'R':
        curr = [curr[0]+meters, curr[1]]
    elif direction == 'L':
        curr = [curr[0]-meters, curr[1]]
    elif direction == 'U':
        curr = [curr[0], curr[1]+meters]
    elif direction == 'D':
        curr = [curr[0], curr[1]-meters]
    
    if curr != start:
        vertices.append(curr)
  
area = 0
#shoelace formula
for i in range(0, len(vertices)):
    area += (vertices[(i+1) % (len(vertices))][0]+vertices[i][0]) * (vertices[(i+1) % (len(vertices))][1] - vertices[i][1])
area = abs(area) / 2

#Pick's theorem
inner = area +1 - (border / 2)

print(inner+border)