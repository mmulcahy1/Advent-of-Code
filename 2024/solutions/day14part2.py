import sys
import re
import numpy as np

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

width = 101
height = 103
middle_width = width // 2
middle_height = height // 2
robot_positions = np.full((height,width), ' ')
robots = []

def sign(num):
    if num < 0:
        return -1
    else:
        return 1

for line in lines:
    robots += [[int(x) for x in re.findall(r'-?\d+', line)]]

i = 0
np.set_printoptions(threshold=sys.maxsize)
while True:
    i += 1
    unique_positions = set()
    robot_positions = np.full((height,width), ' ')
    for j, robot in enumerate(robots):
        x = robot[0]
        y = robot[1]
        velocity_x = robot[2]
        velocity_y = robot[3]
        next_x = (x + velocity_x) % width 
        next_y = (y + velocity_y) % height
        robot_positions[next_y, next_x] = '.'
        robot[0] = next_x
        robot[1] = next_y
        robots[j] = robot
        unique_positions.add((next_y, next_x))
    if len(unique_positions) == len(robots):
        for row in robot_positions:
            print(''.join(row), 'ending\n')
        print(i)
        print('all robots have unique positions')
        input('Press keyboard to get next positions ')



