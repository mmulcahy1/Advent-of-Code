import sys

line = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()][0]
disk = []
file = True
id = 0
new_disk = []
result = 0
last = []
empty_spaces = []
blocks = []
ind = 0
for i in line:
    if file:
        disk += [id] * int(i)
        blocks += [[ind, ind+int(i)-1, id]]
        id += 1

    else:
        disk += ['.'] * int(i) 
        empty_spaces += [[ind, ind+int(i)-1]]
        
    file = not file
    ind += int(i)

for i in range(len(blocks)-1, -1, -1):
    block_size = blocks[i][1] - blocks[i][0] + 1
    for ind, e in enumerate(empty_spaces):
        e_size = e[1] - e[0] + 1
        if e[0] > blocks[i][0]:
            break
        elif block_size <= e_size and e[0] < blocks[i][0]:
            blocks[i][0] = e[0]
            blocks[i][1] = e[0] + block_size - 1
            if block_size == e_size:
                del empty_spaces[ind]
            else:
                empty_spaces[ind][0] = blocks[i][1]+1
            break
            
    result += sum(range(blocks[i][0], blocks[i][1]+1)) * blocks[i][2]
    

# for e in empty_spaces:
    # last_block = filled_spaces.pop()
    # if e >= last_block:
        # break
    # else:
        # disk[e] = disk[last_block]
        # disk[last_block] = '.'
        
# for i, id in enumerate(disk):
    # if id == '.':
        # break
    # else:
        # result += i * int(id)


print(result)