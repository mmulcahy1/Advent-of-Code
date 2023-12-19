import sys
import re
lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

initSeq = lines[0]

result = 0
steps = initSeq.split(',')
for step in steps:
    currVal = 0
    for c in step:
        currVal += ord(c)
        currVal *= 17
        currVal = currVal % 256
        
    result += currVal
    
print(result)