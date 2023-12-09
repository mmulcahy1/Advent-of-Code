import sys
import re
import math
import functools

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

instructions = lines[0]

nodes = {}
startingNodes = []

i = 2
#get nodes that end with A
while i < len(lines):
    coords = re.findall(r'\w+', lines[i])
    if coords[0][2] == 'A':
        startingNodes.append(coords[0])
    nodes[coords[0]] = [coords[1], coords[2]]
    i += 1


steps = []

#get number of steps it takes for each starting node to reach a node ending with Z
for location in startingNodes:
    currSteps = 0
    while location[2] != 'Z':
        instruction = instructions[currSteps %  len(instructions)]
        if instruction == 'R':
            location = nodes[location][1]
        else:
            location = nodes[location][0]
            
        currSteps += 1
    
    steps.append(currSteps)
        
#the least common multiple is the least amount of steps it takes for
#all starting modes to reach an ending node at the same time
result = math.lcm(*steps)
         
print(result)