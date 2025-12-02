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
        #print(i)
        for j in range(1, IDlength//2+1):
            if IDlength % j == 0:
                repeat = ID[:j]
                repeats = True
                #print("----")
                for k in range(j, IDlength, j):
                    #print(repeat, ID[k:k+j])
                    if ID[k:k+j] != repeat:
                        repeats = False
                        break
                if repeats == True:
                    InvalidID.append(i)
                    break
        i+=1

print(InvalidID)
print(sum(InvalidID))

