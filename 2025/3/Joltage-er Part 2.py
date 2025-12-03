FileInput = open("2025/3/input.txt")
line = FileInput.readline()

jolts = []

while (line):
    digits = []
    line = line.strip()
    for i in range(12):
        digits.append(line[i])
    
    i = 1
    while i < len(line)-12:
        #print("i:", i, int(''.join(digits)))
        j = 0
        while j < 12:
            if int(line[i+j]) > int(digits[j]):
                #print("i:", i, int(line[i+j]), "j:", j, int(digits[j]))
                k = 0
                while k < 12 - j:
                    digits[j+k] = line[i+j+k]
                    k += 1 
                break
            j += 1
        i += 1

    #print(int(''.join(digits)))
    for i in range(12, 0, -1):
        if int(line[-i]) > int(digits[-i]):
            #print(i)
            #print(int(line[-i]), int(digits[-i]))
            j = 12 - i
            while j < 12:
                #print(j)
                digits[j] = line[-i]
                #print(digits)
                j += 1
                i -= 1
            break
    #print(int(''.join(digits)))

    jolts.append(int(''.join(digits)))

    line = FileInput.readline()

print(jolts)
print(sum(jolts))