import sys
import re
lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]
lines.append('')

summary = 0
rows = []

def findReflections(mirrorLines):
    sumAboveReflection = 0
    for i in range(0,  len(mirrorLines)-1):
        if mirrorLines[i] == mirrorLines[i+1]:
            above = i-1
            below = i+2
            matches = True
            while above > -1 and below < len(mirrorLines):
                if mirrorLines[above] != mirrorLines[below]:
                    matches = False
                    break
                
                above -= 1
                below += 1
            if matches:
                sumAboveReflection = i + 1
                break
                
    return sumAboveReflection
    
def getColumns(rows):
    columns = [''] * len(rows[0])
    for row in rows:
        for idx, c in enumerate(row):
            columns[idx] += c
    
    return columns

for idx, line in enumerate(lines):
    if len(line) == 0:
        #get string of each column
        columns = getColumns(rows)
        
        #get number of rows above each vertical reflection
        vert = findReflections(columns)
        
        #get number of columns to the left of each horizontal reflection
        horiz = findReflections(rows) * 100
        
        summary += vert + horiz
        #empty rows for next pattern
        rows = []
    else:
        rows.append(line)
        
        
print(summary)