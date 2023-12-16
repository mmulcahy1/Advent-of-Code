import sys
import re
lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

result  = 0


def findArrangement(record, brokenSprings, nextGroups):
    result = 0
    #determine if arrangement is valid
    if brokenSprings == 0:
        if re.search('#', record):
            return 0
        return 1
    if len(record) < brokenSprings or len(record) == 0:
        return 0
    
    #find stopping point
    maxEnd = len(record) - (sum(nextGroups) + len(nextGroups)-1)
    if re.search('#', record):
        maxEnd = min(maxEnd, re.search('#', record).start()-1)
    endRange = brokenSprings - 1
    startRange = 0

    #find next starting points
    while endRange < maxEnd:
        recordPart = record[startRange:endRange+1]
        if '.' not in recordPart:
            result += findArrangement(record[endRange+2::], nextGroups[0], nextGroups[1::])
                    
        startRange += 1
        endRange += 1
    
    #find first '#' occurence and any valid next starting points containing the occurence
    match = re.search('#+', record)
    if match:
        if len(match[0]) == brokenSprings:
            result += findArrangement(record[match.end()+1::], nextGroups[0], nextGroups[1::])
        elif len(match[0]) < brokenSprings:
            startRange = max(0, match.start()- (brokenSprings - len(match[0])))
            endRange = startRange + brokenSprings - 1
            i = 0
            while endRange < len(record) and startRange <= match.start():
                recordPart = record[startRange:endRange+1]
                if '.' not in recordPart:
                    if not (endRange + 1 < len(record) and record[endRange+1] == '#'):
                        result += findArrangement(record[endRange+2::], nextGroups[0], nextGroups[1::])
                
                startRange += 1
                endRange += 1

            
    return result
for line in lines:
    record = line.split(' ')[0]
    groups = [int(i) for i in re.findall('\d+', line.split(' ')[1])]
    groups.append(0)
    r = findArrangement(record, groups[0], groups[1::])
    
    result += r
        
print(result)