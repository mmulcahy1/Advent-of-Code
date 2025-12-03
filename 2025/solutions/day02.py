import sys
import itertools

id_ranges_string = open(sys.argv[1],'r').read()
id_ranges = id_ranges_string.split(',')

part_1_solution = 0
part_2_solution=0

invalid_ids = {}

for id_range in id_ranges:
    start = id_range.split('-')[0]
    end = id_range.split('-')[1]
    
    start_num_digits = len(start)
    end_num_digits = len(end)
    digit_list = ['0','1','2','3','4','5','6','7','8','9']
    
    #generate invalid IDs
    if start_num_digits % 2 == 0:
        digit_length = start_num_digits
    else:
        digit_length = start_num_digits + 1
    
    #print(id_range)
    
    #part 1
    while digit_length <= end_num_digits:
        sequence_length = digit_length // 2
        sequences = itertools.product(digit_list, repeat=sequence_length)
        #print([i for i in sequences])
        sequences = ["".join(seq) for seq in sequences if seq[0] != '0']
        #print(sequences)
        for seq in sequences:
            full_id = int(seq + seq)
            if full_id in range(int(start), int(end)+1):
                part_1_solution += full_id
                #print(full_id)
        digit_length += 2
        
        
    #part 2
    digit_length = start_num_digits
        
    while digit_length <= end_num_digits:
        if digit_length in invalid_ids:
            full_ids = invalid_ids[digit_length]
        else:
            full_ids = set()
            for sequence_length in range(1, digit_length //2 + 1):
                if digit_length % sequence_length == 0:
                    #print('sequence length is ' + str(sequence_length))
                    repetition = digit_length // sequence_length
                    #print(repetition)
                    sequences = list(itertools.product(digit_list, repeat=sequence_length))
                    sequences = ["".join(seq) for seq in sequences if seq[0] != '0']
                    full_ids.update([seq*repetition for seq in sequences])
                    #print(sequences)
                    
            invalid_ids[digit_length] = full_ids.copy()
                
        for full_id in full_ids:
            full_id = int(full_id)
            if full_id in range(int(start), int(end)+1):
                part_2_solution += full_id
                #print(full_id)
        digit_length += 1
    
    
    #print('\n')
        
print(part_1_solution)
print(part_2_solution)
    
    