import sys
import re
lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

rows = [0] * len(lines)
columns = [0] * len(lines[0])
galaxyCoords = []

#get initial coordinates for each galaxy
#and keep track of number of galaxies encountered
#in each row and column
for lineIdx, line in enumerate(lines):
    galaxies = re.finditer('#', line)
    for galaxy in galaxies:
            galaxyCoords.append([galaxy.start(), lineIdx])
            rows[lineIdx] += 1
            columns[galaxy.start()] += 1


emptyRow = '.' * len(lines[0])
i = 0   

#add empty rows to galaxy coordinates        
for rowIdx, numGalaxies in enumerate(rows):
    if numGalaxies == 0:
        for gc in galaxyCoords:
            if gc[1] > rowIdx+i:
                gc[1] += 999999
        i += 999999

#add empty columns to galaxy coordinates 
j = 0 
for colIdx, numGalaxies in enumerate(columns):
    if numGalaxies == 0:
        for gc in galaxyCoords:
            if gc[0] > colIdx+j:
                gc[0] += 999999
        j += 999999       

result = 0
for firstOfPair in range(0, len(galaxyCoords)-1):
    galaxy1 = galaxyCoords[firstOfPair]
    for secondfOfPair in range(firstOfPair+1, len(galaxyCoords)):
        galaxy2 = galaxyCoords[secondfOfPair]
        result += abs(galaxy1[0]-galaxy2[0]) + abs(galaxy1[1]-galaxy2[1])
        
print(result)