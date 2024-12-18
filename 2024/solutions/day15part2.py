import sys
import re
import numpy as np

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]
walls = []
boxes = []
instructions = []
instruction_flag = False
w = []

height = len(lines)
width = len(lines[0]) * 2


for i in range(len(lines)):
    line = lines[i]
    widened_line = []
    if line.strip() == '':
        instruction_flag = True
    
    if not instruction_flag:
        #widen warehouse
        for j in range(len(lines[i])):
            if lines[i][j] == '@':
                robot = [i,2*j]
                widened_line.extend(['@', '.'])
            elif lines[i][j] == '#':
                widened_line.extend(['#', '#'])
            elif lines[i][j] == 'O':
                widened_line.extend(['[',']'])
            elif lines[i][j] == '.':
                widened_line.extend(['.', '.'])
        w.append(list(widened_line))
    else:        
        #get robot directions
        for instruction in line:
            instructions.append(instruction)

warehouse = np.array(w)
print('initial state')
for row in warehouse:
    print(''.join(row))
print('\n')

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

def move_robot_up_or_down(current_boxes, y, onlyRobot, direction):
    if onlyRobot:
        next_boxes = set()
        onlyPlace = current_boxes.pop()
        if warehouse[y+direction, onlyPlace] == '[':
            next_boxes.update([onlyPlace, onlyPlace+1])
        elif warehouse[y+direction, onlyPlace] == ']':
            next_boxes.update([onlyPlace-1, onlyPlace])
        elif warehouse[y+direction, onlyPlace] == '#':
            return False
        elif warehouse[y+direction, onlyPlace] == '.':
            warehouse[y+direction, onlyPlace] = '@'
            warehouse[y, onlyPlace] = '.'
            return True
         
        if move_robot_up_or_down(next_boxes, y+direction, False, direction,):
            warehouse[y+direction, onlyPlace] = warehouse[y, onlyPlace]
            warehouse[y, onlyPlace] = '.'
            return True
    else:

        next_boxes = set()
        for current_box in current_boxes:
            if warehouse[y+direction, current_box] == '#':
                return False
            elif warehouse[y+direction, current_box] == '[':
                next_boxes.update([current_box, current_box+1])
            elif warehouse[y+direction, current_box] == ']':
                next_boxes.update([current_box-1, current_box])
   
        if len(next_boxes) == 0:
            for current_box in current_boxes:
                warehouse[y+direction, current_box] = warehouse[y, current_box]
                warehouse[y, current_box] = '.'
            return True
        else:
            if move_robot_up_or_down(next_boxes, y+direction, False, direction):
                for current_box in current_boxes:
                    warehouse[y+direction, current_box] = warehouse[y, current_box]
                    warehouse[y, current_box] = '.'
                return True


def move_robot_left_or_right(current_pos, direction):
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
    
         
for i, instruction in enumerate(instructions):
    if instruction == '^':
        direction =  [-1, 0]
        is_moved = move_robot_up_or_down(set([robot[1]]), robot[0], True, -1)
    elif instruction == 'v':
        direction = [1,0]
        is_moved = move_robot_up_or_down(set([robot[1]]), robot[0], True, 1)
    elif instruction == '>':
        direction = [0, 1]
        is_moved = move_robot_left_or_right(robot, direction)
    elif instruction == '<':
        direction = [0, -1]
        is_moved = move_robot_left_or_right(robot, direction)
    if is_moved:
        robot = [sum(x) for x in zip(robot, direction)]


for row in warehouse:
    print(''.join(row))

result = 0
boxes = np.argwhere(warehouse == '[')
for box in boxes:
    gps = box[1] + (box[0] * 100)
    result += gps

print(result)
        

