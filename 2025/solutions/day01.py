import sys

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

position = 50
part_1_solution = 0 
part_2_solution = 0

for instruction in lines:
    direction = instruction[0]
    turns = int(instruction[1:])
    starting_position = position
    
    # print('starting position: ' + str(position))
    
    if direction == 'R':
        distance_to_zero = 100 - position
        position = (position + turns) % 100
    elif direction == 'L':
        distance_to_zero = position
        position = (position - turns) % 100
        
    if position == 0:
        part_1_solution += 1
    
    # print('instruction: ' + instruction)
    # print('direction: ' + direction)
    # print('turns: ' + str(turns))
    # print('distance to zero: ' + str(distance_to_zero))
    # print('position: ' + str(position))
    
    
    if turns >= distance_to_zero and turns != 0 :
        clicks_at_zero = ((turns - distance_to_zero) // 100)
        if distance_to_zero > 0:
            clicks_at_zero += 1
        part_2_solution += clicks_at_zero
    else:
        clicks_at_zero = 0
        
    # print('clicks at zero: ' + str(clicks_at_zero))
    # print('part_2_solution: ' + str(part_2_solution))
    # print('\n')
         

        
print('part 1 solution: ' + str(part_1_solution))
print('part 2 solution: ' + str(part_2_solution))