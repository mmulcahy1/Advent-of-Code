import sys
import re
from collections import deque
lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

modules = {}

for line in lines:
    moduleInfo = line.split('>')[0]
    destinations = re.findall(r'\w+',line.split('>')[1])
    
    moduleName = re.search(r'\w+', moduleInfo)[0]
    if moduleName == 'broadcaster':
        moduleType = 'broadcaster'
        modules[moduleName] = [moduleType, destinations]
    else:
        moduleType = moduleInfo[0]
        if moduleType == '%':
            modules[moduleName] = [moduleType, destinations, False]
        elif moduleType == '&':
            modules[moduleName] = [moduleType, destinations, {}]
            
        
#get inputs for conjuction modules    
for m in modules:
    if modules[m][0] == '&':
        for n in modules:
            if m in modules[n][1]:
                modules[m][2][n] = 'low'
                

pulses = deque()
#start with the 1000 initial low pulses from the button
pulsesCount = {'low': 1000, 'high':0}   
for pulse in range(1000):
    for destination in modules['broadcaster'][1]:
        pulses.append(['broadcaster', destination, 'low'])
        pulsesCount['low'] += 1
        
    while pulses:
        currentPulse = pulses.popleft()
        sender = currentPulse[0]
        receiver = currentPulse[1]
        receivedType = currentPulse[2]
        
        if receiver in modules:
        
            if modules[receiver][0] == '%':
                if receivedType == 'low':
                    if modules[receiver][2]:
                        sendType = 'low'
                    else:
                        sendType = 'high'
                
                    modules[receiver][2] = not modules[receiver][2]
                    
                    for nextDestination in modules[receiver][1]:
                        pulses.append([receiver, nextDestination, sendType])
                        pulsesCount[sendType] += 1
                        
            elif modules[receiver][0] == '&':
                modules[receiver][2][sender] = receivedType
                
                if 'low' in modules[receiver][2].values():
                    sendType = 'high'
                else:
                    sendType = 'low'
            
                for nextDestination in modules[receiver][1]:
                    pulses.append([receiver, nextDestination, sendType])
                    pulsesCount[sendType] += 1
                
result = pulsesCount['low'] * pulsesCount['high']
print(result)
            