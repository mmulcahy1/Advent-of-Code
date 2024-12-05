import sys
import re

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]
result = 0
enabled = True
for line in lines:
    validCalcs = re.findall(r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)', line)
    for v in validCalcs:
        if v == 'do()':
            enabled = True
        elif v == 'don\'t()':
            enabled = False
        elif enabled:
            multipliers = re.findall(r'[0-9]+', v)
            result += int(multipliers[0]) * int(multipliers[1])
        print(v)
        print(enabled)

print(result)