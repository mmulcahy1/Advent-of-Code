import sys
import re

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

result = 0
for lineidx, line in enumerate(lines):
    #find each number in current line
    for num in re.finditer(r'\d+', line):
        start = max(num.start() - 1, 0)
        end = min(num.end()+1, len(line)-1)
        
        s = line[start] + line[end-1]                 #get elements directly before and after num  
        #check if first line
        if lineidx > 0:
            s = s + lines[lineidx-1][start:end]     #get adjacent elements in previous line
        #check if last line 
        if lineidx < len(lines)-1:
            s = s + lines[lineidx+1][start:end]     #get adjacent elements in next line
        if re.search(r'[^.\d]', s):
            result = result + int(num[0]) 
print(result)    

