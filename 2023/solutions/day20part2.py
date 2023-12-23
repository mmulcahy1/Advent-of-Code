import sys
import re
from collections import deque
import math
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
            
rxInputInputs = {}        
#get inputs for conjuction modules    
for m in modules:
    if modules[m][0] == '&':
        for n in modules:
            if m in modules[n][1]:
                modules[m][2][n] = 'low'
    
    #check if module is input for rx
    if 'rx' in modules[m][1]:
        rxInput = m

#find modules that output to rxInput        
for m in modules:
    if rxInput in modules[m][1]:
        rxInputInputs[m] = -1


pulses = deque()
successful = False
pulse = 0

while -1 in rxInputInputs.values():
    pulse += 1
   
    for destination in modules['broadcaster'][1]:
        pulses.append(['broadcaster', destination, 'low'])
    
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
                        
            elif modules[receiver][0] == '&':
                modules[receiver][2][sender] = receivedType
                
                if 'low' in modules[receiver][2].values():
                    sendType = 'high'
                else:
                    sendType = 'low'
            
                for nextDestination in modules[receiver][1]:
                    pulses.append([receiver, nextDestination, sendType])
                
                #check if an rxInput is sending a low pulse
                if sendType == 'high' and receiver in rxInputInputs and rxInputInputs[receiver] == -1:
                    rxInputInputs[receiver] = pulse
                
#find the first pulse number where rxInput has a high pulse record in memory for each input
#and sends rx a low pulse
result = math.lcm(*rxInputInputs.values())
print(result)
                
            