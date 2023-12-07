import sys
import re

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

seedInfo = re.findall(r'\d+', lines[0])

seedRanges = []
for i in range(0, len(seedInfo), 2):
    seedRanges.append([int(seedInfo[i]), int(seedInfo[i]) + int(seedInfo[i+1])-1])

locations = {}
rounds = []
i = 3
#get seed numbers
while i < len(lines):
    round = []
    mapping = re.findall(r'\d+', lines[i])
    while i < len(lines) and len(re.findall(r'\d+', lines[i])) > 0:
        mapping = re.findall(r'\d+', lines[i])
        round.append(mapping)
        i += 1

    rounds.append(round)
    i += 2

firstSeedFlag = 1    
#get location for each seed and find the min
for r in rounds:
    nextRanges = []
    for seedRange in seedRanges:
        start = seedRange[0]
        end = seedRange[1]
        changed = 0
        for m in r:
            source = int(m[1])
            dest = int(m[0])
            length = int(m[2])

            #if the mapping range includes the entire seed range
            if start >= source and end < source + length:
                nextRanges.append([start - source + dest, end - source + dest])
                changed = 1
                break
            #if the mapping range includes the start of the seed range but not the end
            elif source <= start < source + length:
                nextRanges.append([start - source + dest, dest + length - 1])
                seedRanges.append([source + length, end]) 
                changed = 1
                break
            #if the mapping range includes the end of the seed range but not the start
            elif source <= end < source + length:
                nextRanges.append([dest, end - source + dest])
                seedRanges.append([start, source - 1])
                changed = 1
                break
            #if mapping range inside seed range but does not encompass entire range
            elif source > start and source + length - 1 < end:
                nextRanges.append([dest, dest+length-1])
                seedRanges.append([start, source - 1])
                seedRanges.append([source + length, end])
                changed = 1
                break
        if changed == 0:
            nextRanges.append([start, end])
                
    seedRanges = nextRanges
print(min([i[0] for i in seedRanges]))

