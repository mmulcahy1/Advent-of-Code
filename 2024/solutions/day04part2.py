import sys
import re

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

height = len(lines)
width = len(lines[0])
result = 0

def isMAS(word):
    # print(word)
    return word in ('MAS', 'SAM')
    
for i in range(width):
    for j in range(height):
        # print('\n')
        # print('i: ' + str(i))
        # print('j: ' + str(j))
        # print('char:' + lines[j][i])
        
        #search top left to bottom right and top right to bottom left
        if j < height - 2 and i < width - 2:
            wordLeftToRight= ''
            wordRightToLeft = ''
            for x in range(3):
                wordLeftToRight += lines[j+x][i+x]
                wordRightToLeft += lines[j+x][i+2-x]
            if isMAS(wordLeftToRight) and isMAS(wordRightToLeft):
                result += 1

print(result)
                

