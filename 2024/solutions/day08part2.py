import sys

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]
frequencies = {}
antinodes = set()

#find all antennas
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c != '.':
            frequencies[c] = frequencies.get(c, []) + [[i, j]]

# print(frequencies)
#go through each frequency and find antinodes
for x, frequency in frequencies.items():
    i = 0
    while i < (len(frequency)):
        antinodes.add((frequency[i][0], frequency[i][1]))
        j = i + 1
        while j < (len(frequency)):
            y, x = [a-b for a, b in zip(frequency[i], frequency[j])]
            # print(frequency[i])
            # print(f"{y}, {x}")
            #check above location for antinode
            above_y = frequency[i][0]+y
            above_x = frequency[i][1]+x
            while -1 < above_y < len(lines) and -1 < above_x < len(lines[0]):
                antinodes.add((above_y, above_x))
                above_y += y
                above_x += x
                
            #check below location for antinode
            below_y = frequency[j][0]-y
            below_x = frequency[j][1]-x
            while -1 < below_y < len(lines) and -1 < below_x < len(lines[0]):
                antinodes.add((below_y, below_x))
                below_y -= y
                below_x -= x
                
            j += 1
        i += 1
                


print(len(antinodes))
    