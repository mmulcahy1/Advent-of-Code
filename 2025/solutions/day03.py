import sys

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

part_1_solution = 0
part_2_solution = 0

#part 1
for bank in lines:
    highest_battery = max(bank[:-1])
    second_highest_battery = max(bank[bank.index(highest_battery)+1:])
    joltage = int(highest_battery + second_highest_battery)
    #print(voltage)
    part_1_solution += joltage
    
#part 2
for bank in lines:
    prev_battery_position = -1
    current_joltage = ''
    possible_next_batteries = bank
    # print(bank)
    for last_battery_position in range(-11, 1):
        # print('last_battery_position ' + str(last_battery_position))
        # print('prev_battery_position '+ str(prev_battery_position))
        # print('current_joltage' + current_joltage)
        
        if last_battery_position == 0:
            possible_next_batteries = bank[prev_battery_position+1:]
        else:
            possible_next_batteries = bank[prev_battery_position+1 : last_battery_position]
            
        next_battery = max(possible_next_batteries)
        current_joltage += next_battery
        prev_battery_position += possible_next_batteries.index(next_battery) + 1
        
        # print('poss batteries ' + str(possible_next_batteries))
        # print(next_battery)
            
    # print(current_joltage)
    # print('\n')
            
    part_2_solution += int(current_joltage)
   
   
        
    
        
        
    
print(part_1_solution)
print(part_2_solution)