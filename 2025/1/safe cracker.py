FileInput = open("2025/1/input.txt")
line = FileInput.readline()

dial = 50
TimesPointedAtZero = 0
direction = 1

def rotate(dial, distance):
    dial += distance
    dial = dial % 100
    return dial

while(line):
    line.strip()

    direction = -1 if line[0] == 'L' else 1
    dial = rotate(dial, int(line[1:])*direction)
    #print(dial)

    if dial == 0:
        TimesPointedAtZero += 1

    line = FileInput.readline()

print(TimesPointedAtZero)
 