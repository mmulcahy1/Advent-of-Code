import sys
import re

lines  = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]


colors = ["red", "green", "blue"]

powerSum = 0

for line in lines:
    power = 1
    for color in colors:
        max = 0
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
            if int(cubes) > max:
                max = int(cubes)
       
        power = power * max
    
    powerSum = powerSum + power
    
print(powerSum)