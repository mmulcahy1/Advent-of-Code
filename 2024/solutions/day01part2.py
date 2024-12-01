import sys

lines  = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

leftDict = {}
rightDict = {}

for line in lines:
    left = line.split("   ")[0]
    right = line.split("   ")[1]
    
    leftDict[left] = leftDict.get(left, 0) + 1
    
    rightDict[right] = rightDict.get(right, 0) + 1

result = 0     
for locID, value in leftDict.items():
    result = result + (int(locID) * int(value) * int(rightDict.get(locID, 0)))

print(result)
  