import sys
from collections import deque


lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]
regions = []
encountered_plots = set()
height = len(lines)
width = len(lines[0])
result = 0

def find_number_of_sides(side_lists):
    total_sides = 0
    for key, side_list in side_lists.items():
        side_list.sort()
        sides = 1
        current_pos = side_list[0]
        if len(side_list) > 1:
            for s in side_list[1:]:
                # if s - curret_pos > 1, they are not connected
                if s - current_pos > 1:
                    sides += 1
                current_pos = s
        total_sides += sides
    return total_sides
            

        

def find_plot_price(y, x):
    #find all relevant plots
    plant = lines[y][x]
    next_plots = deque()
    visited_plots = set()
    plot_area = 0
    next_plots.append((y,x))
    perimeter = 0
    above_sides = {}
    below_sides = {}
    left_sides = {}
    right_sides = {}
    total_sides = 0
    while next_plots:
        next_plot = next_plots.pop()
        y = next_plot[0]
        x = next_plot[1]
        #check if plot is on edge of grid
        if y == 0:
            above_sides[0] = above_sides.get(0, []) + [x]
        if y == height - 1:
            below_sides[height-1] = below_sides.get(height-1, []) + [x]
        if x == 0:
            left_sides[0] = left_sides.get(0, []) + [y]
        if x == width - 1:
            right_sides[x] = right_sides.get(x, []) + [y]
        
        #check surrounding plots
        if y > 0:
            if lines[y-1][x] == plant and (y-1,x) not in visited_plots:
                next_plots.append((y-1,x))
                visited_plots.add((y-1,x))
            elif lines[y-1][x] != plant:
                above_sides[y] = above_sides.get(y, []) + [x]
                
        if y < height - 1:
            if lines[y+1][x] == plant and (y+1,x) not in visited_plots:
                next_plots.append((y+1,x))
                visited_plots.add((y+1,x))
            elif lines[y+1][x] != plant:
                below_sides[y] = below_sides.get(y, []) + [x]
        
        if x > 0:
            if lines[y][x-1] == plant and (y,x-1) not in visited_plots:
                next_plots.append((y,x-1))
                visited_plots.add((y,x-1))
            elif lines[y][x-1] != plant:
                left_sides[x] = left_sides.get(x, []) + [y]
        
        if x < width - 1:
            if lines[y][x+1] == plant and (y,x+1) not in visited_plots:
                next_plots.append((y,x+1))
                visited_plots.add((y,x+1))
            elif lines[y][x+1] != plant:
                right_sides[x] = right_sides.get(x, []) + [y]   
        
        plot_area += 1
        visited_plots.add((y,x))
        encountered_plots.add((y,x))
        
    total_sides += find_number_of_sides(above_sides)
    total_sides += find_number_of_sides(below_sides)
    total_sides += find_number_of_sides(left_sides)
    total_sides += find_number_of_sides(right_sides)

    return plot_area * total_sides
            
            
for i in range(height):
    for j in range(width):
        if (i,j) not in encountered_plots:
            result += find_plot_price(i, j)
            encountered_plots.add((i,j))

print(result)