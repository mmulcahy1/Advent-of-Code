import sys
import re

lines  = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]


colors = {
    "red":12,
    "green":13,
    "blue": 14
}

idSum = 0

for line in lines:
    invalidGameFlag = 0
    for color in colors.keys():
        #get starting indexes of each occurrence of the color string
        idxs = [i.start() for i in re.finditer(color, line)]
        for idx in idxs:
            #get the number of cubes of the color
            cubes = ""      
            cubesIdx = idx-2    #end of cube digit string
            #if current char is a digit, append the char to the beginning of cubes
            #go backward until the char is not a digit
            while line[cubesIdx].isdigit():
                    cubes = line[cubesIdx] + cubes
                    cubesIdx = cubesIdx - 1
            if int(cubes) > colors[color]:
                invalidGameFlag = 1
                break
    gameID = line[5 : line.find(":")]       
    if invalidGameFlag == 0:
        idSum = idSum + int(gameID)
        
print(idSum)
                