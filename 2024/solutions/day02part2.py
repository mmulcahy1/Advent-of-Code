import sys
import re

lines  = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

result = 0

def sign(number):
    if number < 0:
        return -1
    elif number > 0:
        return 1
    else:
        return 0



def isSafe(levels, direction, removed, prevDirection):
    
    if removed:
        safety = True
        if direction == 0:
            direction = sign(int(levels[0]) - int(levels[1]))
        for i in range(len(levels)-1):
            diff = (int(levels[i]) - int(levels[i+1]))
            if abs(diff) in range(1, 4) and (direction == sign(diff)):
                direction = sign(diff)
            else:
                safety = False
                break
        return safety
    else:
        safety = True
         
        for i in range(len(levels)-1):
            diff = (int(levels[i]) - int(levels[i+1]))
            if abs(diff) not in range(1, 4) or (direction != sign(diff) and direction != 0):
                
                if i == 0:
                    removeCurrent = levels[i+1:]
                else:
                    removeCurrent = [levels[i-1]] + levels[i+1:]
                
                    
                removeAfter = levels[i:]
                del removeAfter[1]
                
                if isSafe(removeCurrent, prevDirection, True, prevDirection) == True or isSafe(removeAfter, direction, True, direction):
                    return True
                else:
                    safety = False
                    break
                    
            prevDirection = direction
            direction = sign(diff)
            
                
        return safety

for report in lines:
    levels = re.findall(r'\d+', report)
  
    if isSafe(levels, 0, False, 0) or isSafe(levels[1:], 0, True, 0):
        result += 1

print(result)