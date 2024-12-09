import sys

line = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()][0]
disk = []
file = True
id = 0
new_disk = []
result = 0
last = []
empty_spaces = []
filled_spaces = []
ind = 0
for i in line:
    if file:
        disk += [id] * int(i)
        filled_spaces += range(ind, ind+int(i))
        id += 1

    else:
        disk += ['.'] * int(i) 
        empty_spaces += range(ind, ind+int(i))
        
    file = not file
    ind += int(i)

for e in empty_spaces:
    last_block = filled_spaces.pop()
    if e >= last_block:
        break
    else:
        disk[e] = disk[last_block]
        disk[last_block] = '.'
        
for i, id in enumerate(disk):
    if id == '.':
        break
    else:
        result += i * int(id)


print(result)