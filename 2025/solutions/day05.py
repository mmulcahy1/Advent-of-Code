import sys

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

part_1_solution = 0
part_2_solution = 0
ingred_ranges = []


#part 1
for line in lines:
    if '-' in line:
        ingred_range = line.split('-')
        ingred_ranges += [ingred_range]
    elif line.strip():
        ingred_id = int(line)
        for ingred_range in ingred_ranges:
            if int(ingred_range[0]) <= ingred_id <= int(ingred_range[1]):
                part_1_solution += 1
                break

#part 2
old_ingred_ranges = []
for line in lines:
    new_ingred_ranges = []
    contained = False
    if '-' in line:
        low = int(line.split('-')[0])
        high = int(line.split('-')[1])
        
        new_low = low
        new_high = high
        
        for fresh_ingred_range in old_ingred_ranges:
            ingred_low = fresh_ingred_range[0]
            ingred_high = fresh_ingred_range[1]
            
            # if low is less than established low but high is within range
            if new_low < ingred_low and ingred_low <= new_high <= ingred_high:
                new_high = ingred_high
                new_low = new_low
            # if high is above established high but low is within range
            elif ingred_low <= new_low <= ingred_high  and new_high > ingred_high:
                new_low = ingred_low
                new_high = new_high
            # if new range is contained within established range
            elif new_low >= ingred_low and new_high <= ingred_high:
                new_ingred_ranges = old_ingred_ranges.copy()
                contained = True
                break
            # if new range contains established range
            elif new_low < ingred_low and new_high > ingred_high:
                new_high = new_high
                new_low = new_low
            # if new range is completely outside established range
            else:
                new_ingred_ranges += [fresh_ingred_range]
        
        if not contained:
            new_ingred_ranges += [[new_low, new_high]]
            
        old_ingred_ranges = new_ingred_ranges.copy()
        
    else:
        break

for ingred_range in old_ingred_ranges:
    part_2_solution += ingred_range[1] - ingred_range[0] + 1
        
print(part_1_solution)
print(part_2_solution)