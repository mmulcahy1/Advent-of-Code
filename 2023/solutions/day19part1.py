import sys
import re
import operator
lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

workflows = {}
parts = []
operators = {'>': operator.gt, '<': operator.lt}

def makeRule(category, opr, val, nextWorkFlow):
    result = lambda part: nextWorkFlow if operators[opr](part[category], val) else "go to next"
    return result
    
def makeRuleRorA(acceptedStatus):
    result = lambda part: acceptedStatus
    return result

wf = True
for line in lines:
    if len(line) == 0 and wf:
        wf = False
    
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
                r = makeRule(category, opr, val, nextWorkFlow)
                workflow.append(r)
            else:
                noMatch = rule
                r = makeRuleRorA(noMatch)
                workflow.append(r)
        
        workflows[name] = workflow
    
    else:
        part = {}
        partInfo = line[1:-1].split(',')
        for p in partInfo:
            category = p[0]
            val = int(re.search(r'\d+', p)[0])
            part[category] = val
        
        parts.append(part)


sumAccepted = 0
for part in parts:

    result = 'in'
    i = 0
    while result not in ['R', 'A']:
        if result == 'go to next':
            i += 1
        else:
            workflow = workflows[result]
            i = 0
            
        result = workflow[i](part)
        

        
    if result == 'A':
        sumAccepted += sum(part.values())
        
print(sumAccepted)
        
            
            
            