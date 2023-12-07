import sys
import re

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

seeds = re.findall(r'\d+', lines[0])

rounds = []
i = 3

#get mappings
while i < len(lines):
    round = []
    mapping = re.findall(r'\d+', lines[i])
    while i < len(lines) and len(re.findall(r'\d+', lines[i])) > 0:
        mapping = re.findall(r'\d+', lines[i])
        round.append(mapping)
        i += 1
    rounds.append(round)
    i += 1
    
#get location for each seed and find the min
for idx, seed in enumerate(seeds):
    s = int(seed)
    for r in rounds:
        for m in r:
            source = int(m[1])
            dest = int(m[0])
            length = int(m[2])
            if source <= s < source + length:   #check if seed in range
                s = s - source + dest           #set s to destination value
                break
    if idx == 0:
        minLoc = s
    else:
        minLoc = min(minLoc, s)

print(minLoc)