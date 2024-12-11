import sys
from collections import deque

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]
trailheads = []
result = 0
width = len(lines[0])
height = len(lines)

#find trailheads
for i in range(len(lines)):
    line = lines[i]
    for j in range(len(line)):
        if line[j] == '0':
            trailheads.append([i, j])

# print(trailheads)

for trailhead in trailheads:
    next_steps = deque()
    score = 0
    next_steps.append(trailhead)
    while next_steps:
        current_step = next_steps.pop()
        current_x = current_step[1]
        current_y = current_step[0]
        current_hike_height = int(lines[current_y][current_x])
        if current_hike_height == 9:
            score += 1

        else:
            #get left step
            if current_step[1] > 0 and int(lines[current_y][current_x-1]) - current_hike_height == 1:
                next_steps.append([current_y, current_x-1])
            #get right step
            if current_step[1] < width - 1 and int(lines[current_y][current_x+1]) - current_hike_height == 1:
                next_steps.append([current_y, current_x+1])
            #get above step
            if current_step[0] > 0 and int(lines[current_y-1][current_x]) - current_hike_height == 1:
                next_steps.append([current_y-1, current_x])
            #get below step
            if current_step[0] < height - 1 and int(lines[current_y+1][current_x]) - current_hike_height == 1:
                next_steps.append([current_y+1, current_x])

    result += score

print(result)
        
            