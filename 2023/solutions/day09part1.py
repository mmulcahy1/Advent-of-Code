import sys
import re
lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

result = 0

for line in lines:
    sequences = []
    currSeq = [int(i) for i in re.findall('-?\d+\.?\d*', line)]    #get initial sequence
    sequences.append(currSeq)
    while(not all(s==0 for s in currSeq)):  #check if current sequence is all zeroes
        nextSeq = []
        for i in range(0, len(currSeq)-1):              #get next sequence
            nextSeq.append(currSeq[i+1] - currSeq[i])
            
        sequences.append(nextSeq)
        currSeq = nextSeq
        
    val = 0
    #get next value for each sequence
    for j in range(len(sequences) - 1, -1, -1):
        val += sequences[j][-1]
    result += val
        
    
print(result)

    