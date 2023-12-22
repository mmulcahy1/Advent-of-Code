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
    info = line.split('#')[1]
    direction = info[5]
    meters = int(info[:5], 16)  #convert from hexadecimal to decimal
    border += meters
    
    if direction == '0':
        curr = [curr[0]+meters, curr[1]]
    elif direction == '2':
        curr = [curr[0]-meters, curr[1]]
    elif direction == '3':
        curr = [curr[0], curr[1]+meters]
    elif direction == '1':
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

#add inner area to digs on the border
print(inner+border)