import sys
import re
import numpy as np

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

width = 101
height = 103
middle_width = width // 2
middle_height = height // 2
final_positions = np.full((height,width), 0)


for line in lines:
    start_x, start_y, velocity_x, velocity_y = [int(x) for x in re.findall(r'-?\d+', line)]
    final_x = (start_x + (velocity_x * 100)) % width 
    final_y = (start_y + (velocity_y * 100)) % height
    
    final_positions[final_y, final_x] += 1


quadrant_one = np.sum(final_positions[0:middle_height, middle_width+1:])
quadrant_two = np.sum(final_positions[0:middle_height, 0:middle_width])
quadrant_three = np.sum(final_positions[middle_height+1:, 0:middle_width])
quadrant_four = np.sum(final_positions[middle_height+1:, middle_width+1:])

safety_factor = quadrant_one*quadrant_two*quadrant_three*quadrant_four
print(safety_factor)

