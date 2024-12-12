import sys
import re

line = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()][0]
stones = re.findall(r'\d+', line)

for i in range(25):
    new_stones = []
    for stone in stones:
        if stone == '0':
            new_stones.append('1')
        elif len(stone) % 2 == 0:
            half = len(stone) // 2
            new_stones.append(str(int(stone[:half])))
            new_stones.append(str(int(stone[half:])))
        else:
            new_stones.append(str(int(stone)*2024))
    stones = new_stones.copy()

print(len(stones))        


