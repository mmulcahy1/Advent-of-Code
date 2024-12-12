import sys
import re

line = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()][0]
stones = re.findall(r'\d+', line)
encountered_stones = {}
result = 0


def find_number_of_stones(stone, blinks):
    if blinks == 0:
        return 1
    if (stone, blinks) in encountered_stones:
        return encountered_stones[(stone, blinks)]
    
    else:
        new_stones = []
        if stone == '0':
            number_of_stones = find_number_of_stones('1', blinks - 1)
        elif len(stone) % 2 == 0:
            half = len(stone) // 2
            first_stone = str(int(stone[:half]))
            second_stone = str(int(stone[half:])) 
            number_of_stones = find_number_of_stones(first_stone, blinks - 1) + find_number_of_stones(second_stone, blinks - 1)        
        else:
            next_stones = [str(int(stone)*2024)]
            number_of_stones = find_number_of_stones(str(int(stone)*2024), blinks - 1)
        
        encountered_stones[(stone, blinks)] = number_of_stones
        return number_of_stones

for stone in stones:
    result += find_number_of_stones(stone, 75)

print(result)        

#print(stones)