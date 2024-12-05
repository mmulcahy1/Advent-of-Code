import sys
import re

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

height = len(lines)
width = len(lines[0])
result = 0

def isXMAS(word):
    # print(word)
    return word in ('XMAS', 'SAMX')
    
for i in range(width):
    for j in range(height):
        # print('\n')
        # print('i: ' + str(i))
        # print('j: ' + str(j))
        # print('char:' + lines[j][i])
        #search left to right
        if i < width - 3:
            if isXMAS(lines[j][i:i+4]):
                result += 1
        
        #search top to bottom:
        if j < height - 3:
            word = ''.join(k[i] for k in lines[j:j+4])
            if isXMAS(word):
                result += 1
        
        #search top left to bottom right
        if j < height - 3 and i < width - 3:
            word = ''
            for x in range(4):
                word += lines[j+x][i+x]
            if isXMAS(word):
                result += 1
        #search top right to bottom left
        if j < height - 3 and i > 2:
            word = ''
            for x in range(4):
                word += lines[j+x][i-x]
            if isXMAS(word):
                result += 1

print(result)
                

