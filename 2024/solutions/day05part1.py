import sys
import re

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]
updateRules = {}
result = 0

def isCorrect(pages):
    manual = []
    for page in pages:
        pageRules = updateRules.get(page, [])
        for r in pageRules:
            #if r is already in the manual, r is behind the page and the manual is incorrect
            if r in manual:
                return False
        manual.append(page)
                
    return True

for line in lines:
    #find rules
    if '|' in line:
        updateRules[line.split('|')[0]] = updateRules.get(line.split('|')[0], []) + [line.split('|')[1]]
    
    elif len(line) > 0:
        pages = re.findall(r'\d+', line)
        if isCorrect(pages):
            result += int(pages[len(pages) // 2])
        
print(result)
        