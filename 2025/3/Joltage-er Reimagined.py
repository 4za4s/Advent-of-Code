FileInput = open("2025/3/input.txt")
line = FileInput.readline()

jolts = []
x = 12

def makeXdigitNumeber(line, x):
    digits = []
    # where each digit 1-9 appears in the line
    numberIndexes = []
    for i in range(9):
        numberIndexes.append([])

    largestIndex = len(line) - x
    smallestIndex = 0

    for i in range(len(line)):
        numberIndexes[9 - int(line[i])].append(i)
    
    #print(numberIndexes)
    for i in range(x):
        for j in numberIndexes:
            for k in j:
                if k >= smallestIndex and k <= largestIndex:
                    digits.append(line[k])
                    smallestIndex = k+1
                    largestIndex += 1
                    break
            if len(digits) == i+1:
                break

    return int(''.join(digits))

while (line):
    jolts.append(makeXdigitNumeber(line.strip(), x))
    line = FileInput.readline()

#print(jolts)
print(sum(jolts))