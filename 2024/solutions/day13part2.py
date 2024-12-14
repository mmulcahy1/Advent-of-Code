import sys
import re
import numpy as np

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

result = 0

def find_determinant(x1,x2,y1,y2):
    return (x1 * y2) - (y1 * x2)
    
def find_solution(machine_a, machine_b, prize):
    machine_a_x = machine_a[0]
    machine_a_y = machine_a[1]
    machine_b_x = machine_b[0]
    machine_b_y = machine_b[1]
    prize_x = prize[0]
    prize_y = prize[1]
    
    coeff_det = find_determinant(machine_a_x, machine_a_y, machine_b_x, machine_b_y)
    a_det = find_determinant(prize_x, prize_y, machine_b_x, machine_b_y)
    b_det = find_determinant(machine_a_x, machine_a_y, prize_x, prize_y)
    a = a_det/coeff_det
    b = b_det/coeff_det
    if a.is_integer() and b.is_integer():
        return a*3 + b
    else:
        return 0

for i in range(len(lines))[::4]:
    machine_a = [int(x) for x in re.findall(r'\d+', lines[i])]
    machine_b = [int(x) for x in re.findall(r'\d+', lines[i+1])]
    prize = [10000000000000 + int(x) for x in re.findall(r'\d+', lines[i+2])]
    
    result += find_solution(machine_a, machine_b, prize)


print(int(result))

    
    