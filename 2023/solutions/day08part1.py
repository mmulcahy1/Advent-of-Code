import sys
import re

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

instructions = lines[0]

nodes = {}

i = 2
while i < len(lines):
    coords = re.findall(r'\w+', lines[i])
    nodes[coords[0]] = [coords[1], coords[2]]
    i += 1
    
location = 'AAA'
steps = 0
while location != 'ZZZ':
    instruction = instructions[steps %  len(instructions)]
    if instruction == 'R':
        location = nodes[location][1]
    else:
        location = nodes[location][0]
    
    steps += 1
    

print(steps)