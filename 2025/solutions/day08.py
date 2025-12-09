import sys
import re
import math
import heapq
import pdb

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]
distances = []
junction_boxes = []
circuits_to_boxes = {}
boxes_to_circuits = {}
circuit_sizes = {}
circuit_number = 0

# if sample use 10, real input use 1000
connections = 1000 

for i, line in enumerate(lines):
    junction_box = line
    x_1 = int(line.split(',')[0])
    y_1 = int(line.split(',')[1])
    z_1 = int(line.split(',')[2])
    
    for junction_box_2 in junction_boxes:
        x_2 = int(junction_box_2.split(',')[0])
        y_2 = int(junction_box_2.split(',')[1])
        z_2 = int(junction_box_2.split(',')[2])
        
        distance = math.sqrt(((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2) + ((z_2 - z_1) ** 2))
        distances.append([distance, junction_box + '-' + junction_box_2])
        
    junction_boxes.append(junction_box)
    circuits_to_boxes[i] = [junction_box]
    boxes_to_circuits[junction_box] = i
    circuit_sizes[i] = 1
        
heapq.heapify(distances)
#breakpoint()
j = 0
while j < connections:
    
    shortest_distance = heapq.heappop(distances)
    first_box = shortest_distance[1].split('-')[0]
    second_box = shortest_distance[1].split('-')[1]
    
    if boxes_to_circuits[first_box] != boxes_to_circuits[second_box]:
        main_circuit = boxes_to_circuits[first_box]
        added_circuit = boxes_to_circuits[second_box]
        
        added_boxes = circuits_to_boxes[added_circuit]
        circuits_to_boxes[main_circuit] += added_boxes
        
        for added_box in added_boxes:
            boxes_to_circuits[added_box] = main_circuit
            circuit_sizes[main_circuit] += 1
        
        del circuits_to_boxes[added_circuit]
        del circuit_sizes[added_circuit]
    
    j += 1
        
#print(circuits_to_boxes)
#print(circuit_sizes)     
#print(boxes_to_circuits)   
three_largest_circuits = heapq.nlargest(3, circuit_sizes, key=circuit_sizes.get)
part_1_solution = math.prod([circuit_sizes[i] for i in three_largest_circuits])
#print(three_largest_circuits)
print(part_1_solution)
        
        
        
        
    
    
    