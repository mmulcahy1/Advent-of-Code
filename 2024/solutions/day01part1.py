import sys

lines  = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

leftList = []
rightList = []

for line in lines:
    leftList.append(line.split("   ")[0])
    rightList.append(line.split("   ")[1])
    
leftList.sort()
rightList.sort()

total = 0
length = len(leftList)
for i in range(length):
    total = total + abs(int(leftList[i]) - int(rightList[i]))
    
print(total)
  