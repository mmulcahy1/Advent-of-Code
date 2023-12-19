import sys
import re
lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]



def hashProcedure(label):
    currVal = 0
    for c in label:
        currVal += ord(c)
        currVal *= 17
        currVal = currVal % 256
        
    return currVal
    
initSeq = lines[0]
steps = initSeq.split(',')
#set up dict for boxes with the box number as the key
boxes = {}
for step in steps:
    r = re.split('=|-', step)
    label = r[0]
    focalLength = r[1]
    #get the box number with the label
    boxNumber = hashProcedure(label)
    if boxNumber in boxes:
        box = boxes[boxNumber]
    else:
        box = []
        
    if '-' in step:
        #delete the appropriate lens if it exists
        newBox = [lens for lens in box if lens[0] != label]
        
    elif "=" in step:
        newBox = []
        found = False
        for lens in box:
            #if the appropriate lens exists, update the focal length
            if lens[0] == label:
                lens[1] = focalLength
                found = True
            newBox.append(lens)
        
        #if the appropriate lens does not exist, append it to the box
        if not found:
            newBox.append([label, focalLength])

    boxes[boxNumber] = newBox


result = 0
for box in boxes.items():
    boxNumber = box[0]
    lenses = box[1]
    for i in range(len(lenses)):
        x = (boxNumber+1) * (i+1) * int(lenses[i][1])
        result += x
        
print(result)
