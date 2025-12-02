FileInput = open("2025/2/input.txt")
line = FileInput.readline()

ranges = line.split(',')
InvalidID = []

for sequence in ranges:
    sequence = sequence.split('-')
    start = int(sequence[0])
    end = int(sequence[1])
    #print(start, end)
    i = start
    #print("start", i)
    while i <= end:
        ID = str(i)
        IDlength = len(ID)
        if IDlength % 2 == 0:
            IDleft = ID[:IDlength//2]
            IDright = ID[IDlength//2:]
            if IDleft == IDright:
                InvalidID.append(i)
                #print("equals", i)
                #print(IDleft, IDright)

                left = (int(IDleft)+1)
                #print("1:", left)
                power = (10**(IDlength//2))
                #print("2:", power)
                i = left * power + left
                #print("next =", i)
            else:
                power = (10**(IDlength//2))
                if int(IDleft) > int(IDright):
                    i = int(IDleft) * power + int(IDleft)
                else:
                    i = (int(IDleft)+1) * power + int(IDleft)+1
                #print("next !=", i)
        else:
            i += (10**(IDlength)) - i
            #print("next %2", i)

#print(InvalidID)
print(sum(InvalidID))

