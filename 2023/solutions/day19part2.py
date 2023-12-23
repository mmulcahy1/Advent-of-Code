import sys
import re
import copy
lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

workflows = {}
partRanges = [[{'x':[1, 4000], 'm':[1,4000], 'a':[1,4000], 's': [1,4000]}, 'in', 0]]
acceptedParts = []


wf = True
for line in lines:
    if len(line) == 0 and wf:
        wf = False
        break
    
    elif wf:
        info = line.split('{')
        name = info[0]
        rules = info[1][:-1].split(',')
        
        workflow = []
        for rule in rules:
            if ':' in rule:
                category = rule[0]
                opr = rule[1]
                val = int(re.search(r'\d+', rule)[0])
                nextWorkFlow = re.search(r'\w+', rule.split(':')[1])[0]
                r = (category, opr, val, nextWorkFlow)
                workflow.append(r)
            else:
                noMatch = rule
                workflow.append(noMatch)
        
        workflows[name] = workflow
    

while partRanges:
    partRange = partRanges.pop()
    workflow = partRange[1]

    
    if workflow == 'A':
        acceptedParts.append(partRange[0])
    elif workflow != 'R': 
        i = partRange[2]
        result = workflows[workflow][i]
        #check if accepted
        if result == 'A':
            acceptedParts.append(partRange[0])
            
        #check if result is the name of a workflow
        elif type(result) == str and result != 'R':
            workflow = result
            partRange[1] = workflow
            partRange[2] = 0
            partRanges.append(partRange)
            
        #if result is a rule, apply the rule and find the passed and failed ranges
        elif result != 'R':
            category = result[0]
            catRange = partRange[0][category]
            low = catRange[0]
            high = catRange[1]
            
            opr = result[1]
            val = result[2]
            if opr == '<':
                if low < val:
                    passedLow = low
                    passedHigh = min(val - 1, high)
                    passedPartRange = copy.deepcopy(partRange)
                    passedPartRange[0][category] = [passedLow, passedHigh]
                    passedPartRange[1] = result[3]
                    passedPartRange[2] = 0
                    partRanges.append(passedPartRange)
                
                if high >= val:
                    failedLow = max(val, low)
                    failedHigh = high
                    failedPartRange = copy.deepcopy(partRange)
                    failedPartRange[0][category] = [failedLow, failedHigh]
                    failedPartRange[1] = workflow
                    failedPartRange[2] = i+1
                    partRanges.append(failedPartRange)
                    
            elif opr == '>':
                if high > val:
                    passedLow = max(val + 1, low)
                    passedHigh = high
                    passedPartRange = copy.deepcopy(partRange)
                    passedPartRange[0][category] = [passedLow, passedHigh]
                    passedPartRange[1] = result[3]
                    passedPartRange[2] = 0
                    partRanges.append(passedPartRange)
                    
                if low <= val:
                    failedLow = low
                    failedHigh = min(val, high)
                    failedPartRange = copy.deepcopy(partRange)
                    failedPartRange[0][category] = [failedLow, failedHigh]
                    failedPartRange[1] = workflow
                    failedPartRange[2] = i+1
                    partRanges.append(failedPartRange)
                        
            
   
        
totalCombinations = 0
for acceptedPartRange in acceptedParts:
    combinations = 1
    for catRange in acceptedPartRange.values():
        combinations *= catRange[1] - catRange[0] + 1
        
    totalCombinations += combinations    
        
print(totalCombinations)
        
            
            