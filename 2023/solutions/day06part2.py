import sys
import re
import math

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

time = 0
for i in re.findall(r'\d+', lines[0]):
    time = time * math.pow(10, len(i)) + int(i)
    
distance = 0
for j in re.findall(r'\d+', lines[1]):
    distance = distance * math.pow(10, len(j)) + int(j)



def solveQuadratic(a, b, c):
    base = math.sqrt(b*b - 4*a*c)
    b = 0 -b
    return([math.floor((b - base)/(2*a)), math.ceil((b + base)/(2*a))])
    
#get interval for winning push times
#the equation is pushTime * (time - pushTime) > distance
#since this is a quadratic inequality, find the factors and calculate the integers between the factors
x, y = solveQuadratic(1, 0-time, distance)
print(y-x-1)
