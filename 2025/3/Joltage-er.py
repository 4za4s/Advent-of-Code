FileInput = open("2025/3/input.txt")
line = FileInput.readline()

jolts = []

first = "0"
second = "0"

while (line):
    first = line[0]
    second = line[1]
    line = line.strip()
    for i in range(2, len(line)-1):
        # print(line[i])
        if int(line[i]) > int(second):
            second = line[i]
        if int(second) > int(first):
            first = second
            second = line[i+1]

    if int(line[-1]) > int(second):
        second = line[-1]

    jolts.append(int(first + second))

    line = FileInput.readline()

print(sum(jolts))