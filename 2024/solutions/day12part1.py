import sys
from collections import deque

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]
encountered_plots = set()
height = len(lines)
width = len(lines[0])
result = 0

def find_plot_price(y, x):
    #find all relevant plots
    plant = lines[y][x]
    next_plots = deque()
    visited_plots = set()
    plot_area = 0
    next_plots.append((y,x))
    perimeter = 0
    while next_plots:
        next_plot = next_plots.pop()
        y = next_plot[0]
        x = next_plot[1]
        #check if plot is on edge of grid
        if y == 0 or y == height - 1:
            perimeter += 1
        if x == 0 or x == width - 1:
            perimeter += 1
        
        #check surrounding plots
        if y > 0:
            if lines[y-1][x] == plant and (y-1,x) not in visited_plots:
                next_plots.append((y-1,x))
                visited_plots.add((y-1,x))
            elif lines[y-1][x] != plant:
                perimeter += 1
                
        if y < height - 1:
            if lines[y+1][x] == plant and (y+1,x) not in visited_plots:
                next_plots.append((y+1,x))
                visited_plots.add((y+1,x))
            elif lines[y+1][x] != plant:
                perimeter += 1
        
        if x > 0:
            if lines[y][x-1] == plant and (y,x-1) not in visited_plots:
                next_plots.append((y,x-1))
                visited_plots.add((y,x-1))
            elif lines[y][x-1] != plant:
                perimeter += 1
        
        if x < width - 1:
            if lines[y][x+1] == plant and (y,x+1) not in visited_plots:
                next_plots.append((y,x+1))
                visited_plots.add((y,x+1))
            elif lines[y][x+1] != plant:
                perimeter += 1   
        
        plot_area += 1
        visited_plots.add((y,x))
        encountered_plots.add((y,x))

    return plot_area * perimeter
            
            
for i in range(height):
    for j in range(width):
        if (i,j) not in encountered_plots:
            result += find_plot_price(i, j)
            encountered_plots.add((i,j))

print(result)