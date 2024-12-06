import sys
import re

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]
updateRules = {}
result = 0

def isCorrect(pages):
    manual = []
    for page in pages:
        pageRules = updateRules.get(page.value, [])
        for r in pageRules:
            #if r is already in the manual, r is behind the page and the manual is incorrect
            if r in manual:
                return False
        manual.append(page.value)
                
    return True
    
class ManualPage:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return other.value in updateRules.get(self.value, [])

    

for line in lines:
    #find rules
    if '|' in line:
        updateRules[line.split('|')[0]] = updateRules.get(line.split('|')[0], []) + [line.split('|')[1]]
        
    
    elif len(line) > 0:
        pages = [ManualPage(page) for page in re.findall(r'\d+', line)]
        if not isCorrect(pages):
            pages.sort()
            result += int(pages[len(pages) // 2].value)


    
print(result)
        