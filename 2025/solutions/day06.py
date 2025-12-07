import sys
import re
import math

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

part_1_solution = 0
part_2_solution = 0

problems = []
for line in lines:
    if any(i in line for i in ['*','+']):
        problem_operations = re.findall(r'[\*\+]', line)
        for idx, operation in enumerate(problem_operations):
            problem_nums = problems[idx]
            
            #part 1
            if operation == '+':
                problem_solution = sum(int(i) for i in problem_nums)
            elif operation == '*':
                problem_solution = math.prod(int(i) for i in problem_nums)
            
            part_1_solution += problem_solution
            
            
        # get range of indexes for each problem
        revised_problems = list(re.finditer(r'[\*\+]', line))
        i = 0
        while i < len(revised_problems):
            rev_prob = revised_problems[i]
            rev_prob_start = rev_prob.span()[0]
            operation = rev_prob.group()
            revised_problem_nums = []
            if i == len(revised_problems)-1:
                rev_prob_end = len(line)
            else:
                rev_prob_end = revised_problems[i+1].span()[0]-1
            
            # determine each column
            for col in range(rev_prob_start, rev_prob_end):
                new_num = "".join([j[col] for j in lines[0:-1] if j[col].isdigit()])
                revised_problem_nums.append(new_num)
            if operation == '+':
                revised_problem_solution = sum(int(i) for i in revised_problem_nums)
            elif operation == '*':
                revised_problem_solution = math.prod(int(i) for i in revised_problem_nums)
        
            part_2_solution += revised_problem_solution
            i += 1
    else:
        problems_values = re.findall(r'\d+', line)
        for idx, val in enumerate(problems_values):
            if idx > len(problems)-1:
                problems += [[val]]
            else:
                problems[idx] += [val]

print(part_1_solution)
print(part_2_solution)