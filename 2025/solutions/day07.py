import sys
import re

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

part_1_solution = 0
part_2_solution = 0

starting_point = lines[0].index('S')
beams = set()
beams.add(starting_point)
beams_timelines = {starting_point:1}
for i in range(1, len(lines)-1):
    next_beams = set()
    next_beams_timelines = {}
    splitters = [match.start() for match in list(re.finditer(r'\^', lines[i+1]))]
    for beam in beams:
        if beam in splitters:
            next_beams.add(beam-1)
            next_beams.add(beam+1)
            part_1_solution += 1
           
            next_beams_timelines[beam-1] = next_beams_timelines.get(beam-1,0) + beams_timelines[beam]
            next_beams_timelines[beam+1] = next_beams_timelines.get(beam+1,0) + beams_timelines[beam]
        else:
            next_beams.add(beam)
            next_beams_timelines[beam] = next_beams_timelines.get(beam,0) + beams_timelines[beam]
            
    beams = next_beams.copy()
    beams_timelines = next_beams_timelines.copy()
    
part_2_solution = sum(beams_timelines.values())

print(part_1_solution)
print(part_2_solution)