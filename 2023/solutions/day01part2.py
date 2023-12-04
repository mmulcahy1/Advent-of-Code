import sys

lines  = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

#dict for digit strings
digitDict = {
    "one": 1,
    "two": 2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}



calSum = 0
#iterate over each calibration line
for line in lines:
    calValue = 0
    digitFlag = 0
    for idx, char in enumerate(line):
        if char.isdigit():
            lastDigit = int(char)
            #check if first digit
            if digitFlag == 0:
                calValue = lastDigit * 10
                digitFlag = 1
            
        else:
            for digitString in digitDict:
                #check if a digit string starts at the current index
                length = len(digitString)
                s = line[idx : idx+length]
                if s == digitString:
                    lastDigit = digitDict[s]
                    #check if first digit
                    if digitFlag == 0:
                        calValue = lastDigit * 10
                        digitFlag = 1
                    
    calValue = calValue + lastDigit
        
    calSum = calSum + calValue
            
print(calSum)