import sys
import numpy as np

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]
walls = []
boxes = []
instructions = []
instruction_flag = False
w = []

height = len(lines)
width = len(lines[0])

for i in range(len(lines)):
    line = lines[i]
    if line.strip() == '':
        instruction_flag = True
    
    if not instruction_flag:
        w.append(list(line))
        #get robot
        for j in range(len(lines[i])):
            if lines[i][j] == '@':
                robot = [i,j]
    else:        
        #get robot directions
        for instruction in line:
            instructions.append(instruction)

warehouse = np.array(w)

def move_robot_and_boxes(current_pos, direction):
    next_pos = [sum(x) for x in zip(current_pos, direction)]
    if 0 < next_pos[0] < height and 0 < next_pos[1] < width and warehouse[next_pos[0], next_pos[1]] == '.':
        warehouse[next_pos[0], next_pos[1]] = warehouse[current_pos[0], current_pos[1]]
        warehouse[current_pos[0], current_pos[1]] = '.'
        return True
    elif  0 < next_pos[0] < height and 0 < next_pos[1] < width and warehouse[next_pos[0], next_pos[1]] != '#':
        if move_robot_and_boxes(next_pos, direction):
            warehouse[next_pos[0], next_pos[1]] = warehouse[current_pos[0], current_pos[1]]
            warehouse[current_pos[0], current_pos[1]] = '.'
            return True
    else:
        return False

#move robot           
for instruction in instructions:
    if instruction == '^':
        direction =  [-1, 0]
    elif instruction == 'v':
        direction = [1,0]
    elif instruction == '>':
        direction = [0, 1]
    elif instruction == '<':
        direction = [0, -1]
    if move_robot_and_boxes(robot, direction):
        robot = [sum(x) for x in zip(robot, direction)]



result = 0
boxes = np.argwhere(warehouse == 'O')
for box in boxes:
    gps = box[1] + (box[0] * 100)
    result += gps

print(result)
        

