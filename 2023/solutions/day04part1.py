import sys
import re

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

sumPoints = 0
for line in lines:
    points = 0
    winningNums = re.findall(r'\d+', line.split('|')[0].split(':')[1])
    
    for numYouHave in re.finditer(r'\d+', line.split('|')[1]):
        if numYouHave[0] in winningNums:
            points = max(2*points, 1)       #if first winning number, set points to 1, otherwise double
    
    sumPoints = sumPoints + points
 
print(sumPoints)