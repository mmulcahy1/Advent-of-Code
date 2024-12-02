import sys
import re

lines  = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

result = 0

def sign(number):
    if number < 0:
        return -1
    else:
        return 1

def isSafe(report):
    levels = re.findall(r'\d+', report)
    safety = True
    direction = sign(int(levels[0]) - int(levels[1]))
    for i in range(len(levels)-1):
        diff = (int(levels[i]) - int(levels[i+1]))
        if abs(diff) in range(1, 4) and (direction == sign(diff)):
            direction = sign(diff)
        else:
            safety = False
            break
    return safety

for report in lines:
    if isSafe(report):
        result += 1

print(result)