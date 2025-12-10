import sys

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

part_1_solution = 0
red_tiles = []
green_or_red_tiles = []
array_size = 100000
tile_grid = [0] * array_size

for i, line in enumerate(lines):
    x_1 = line.split(',')[0]
    y_1 = line.split(',')[1]
    #array_size = max(array_size, int(x_1), int(y_1))
    
    # part 1
    for red_tile in red_tiles:
        x_2 = red_tile.split(',')[0]
        y_2 = red_tile.split(',')[1]
        
        rectangle = (abs(int(x_1) - int(x_2)) + 1) * (abs(int(y_1) - int(y_2)) + 1)
        part_1_solution = max(rectangle, part_1_solution)
            
    red_tiles.append(line)
    
    # part 2

print(part_1_solution)
#print(array_size)