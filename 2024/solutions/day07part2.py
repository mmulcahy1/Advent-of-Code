import sys
import re

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

def calculate_calibration(test_value, current_value, remaining,):
    if len(remaining) == 0 and current_value == test_value:
        return True
    elif len(remaining) == 0 and current_value != test_value:
        return False
    elif current_value > test_value:
        return False
    else:
        return calculate_calibration(test_value, current_value+remaining[0], remaining[1:]) or calculate_calibration(test_value, current_value*remaining[0], remaining[1:]) or calculate_calibration(test_value, int(str(current_value)+str(remaining[0])), remaining[1:])

result = 0
for line in lines:
    values = [int(x) for x in re.findall(r'\d+', line)]
    test_value = values[0]
    remaining = values[1:]
    if calculate_calibration(test_value, remaining[0], remaining[1:]):
        result += test_value
        
print(result)

    