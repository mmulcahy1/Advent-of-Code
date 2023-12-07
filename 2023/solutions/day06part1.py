import sys
import re
import math

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

times = [int(i) for i in re.findall(r'\d+', lines[0])]
distances = [int(i) for i in re.findall(r'\d+', lines[1])]

result = 1

def solveQuadratic(a, b, c):
    base = math.sqrt(b*b - 4*a*c)
    b = 0 -b
    return([math.floor((b - base)/(2*a)), math.ceil((b + base)/(2*a))])
    
for idx, time in enumerate(times):
    #get interval for winning push times
    #the equation is pushTime * (time - pushTime) > distance
    #since this is a quadratic inequality, find the factors and calculate the integers between the factors
    x, y = solveQuadratic(1, 0-time, distances[idx])
    result = result * (y-x-1)
    
print(result)