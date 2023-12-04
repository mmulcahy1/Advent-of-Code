import sys
import re

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

def findNumbers(start, end, line):
    nums = []
    #find each number in line
    for num in re.finditer(r'\d+', line):
        #check if num is within the range adjacent to gear
        if num.start() <= end and num.end()-1 >= start:
            nums.append(int(num[0]))
    return nums
    
result = 0
for lineidx, line in enumerate(lines):
    #find each gear in current line
    for gear in re.finditer(r'[*]', line):
        foundNums = []
        start = max(gear.start() - 1, 0)
        end = gear.end()
        
        foundNums.extend(findNumbers(start, end, line))     #look for numbers next to gear 
        #check if first line
        if lineidx > 0:
            foundNums.extend(findNumbers(start, end, lines[lineidx-1]))     #look for numbers above gear
        #check if last line 
        if lineidx < len(lines)-1:
            foundNums.extend(findNumbers(start, end, lines[lineidx+1]))     #look for numbers below gear
        # #check if there are exactly two found numbers adjacent to gear
        if len(foundNums) == 2:
            result = result + foundNums[0] * foundNums[1]
        
print(result)    
  

