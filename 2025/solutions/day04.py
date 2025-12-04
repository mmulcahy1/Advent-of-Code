import sys

lines = [list(line.replace('\n','')) for line in open(sys.argv[1],'r').readlines()]

part_1_solution = 0
part_2_solution = 0

accessible_rolls = 0
initial_turn = True
height = len(lines)
width = len(lines[0])

while accessible_rolls > 0 or initial_turn:
    accessible_rolls = 0
    accessible_roll_positions = []
    for y in range(height):
        for x in range(width):
            if lines[y][x] == '@':
                adjacent_rolls = 0
                if y > 0 and lines[y-1][x] == '@':
                    adjacent_rolls += 1
                    
                if y < height-1 and lines[y+1][x] == '@':
                    adjacent_rolls += 1
                    
                if x > 0 and lines[y][x-1] == '@':
                    adjacent_rolls += 1
                    
                if x < width-1 and lines[y][x+1] == '@':
                    adjacent_rolls += 1
                
                if y > 0 and x > 0 and lines[y-1][x-1] == '@':
                    adjacent_rolls += 1
                    
                if y > 0 and x < width-1 and lines[y-1][x+1] == '@':
                    adjacent_rolls += 1
                    
                if y < height-1 and x > 0 and lines[y+1][x-1] == '@':
                    adjacent_rolls += 1
                    
                if y < height-1 and x < width-1 and lines[y+1][x+1] == '@':
                    adjacent_rolls += 1

                if adjacent_rolls < 4:
                    accessible_rolls += 1
                    accessible_roll_positions.append((y,x))
    
    for accessible_roll_position in accessible_roll_positions:
        lines[accessible_roll_position[0]][accessible_roll_position[1]] = '.'
    
    if initial_turn:
        part_1_solution = accessible_rolls
        initial_turn = False
        
    part_2_solution += accessible_rolls
    
                    

print(part_1_solution)
print(part_2_solution)