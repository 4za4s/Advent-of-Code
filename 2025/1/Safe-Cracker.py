FileInput = open("2025/1/input.txt")
line = FileInput.readline()

dial = 50
TimesPointedAtZero = 0
TimesPastZero = 0
direction = 1

def rotate(dial, distance, TimesPastZero):
    dialNew = dial + distance

    TimesPastZero += abs(distance) // 100
    if dial != 0:
        if distance < 0:
            TimesPastZero += 1 if abs(distance) % 100 >= dial else 0
        elif distance > 0:
            TimesPastZero += 1 if distance % 100 >= 100 - dial else 0

    dial = dialNew % 100
    return dial, TimesPastZero

while(line):
    line.strip()

    direction = -1 if line[0] == 'L' else 1
    dial, TimesPastZero = rotate(dial, int(line[1:])*direction, TimesPastZero)
    #print("\n", dial, TimesPastZero)

    if dial == 0:
        TimesPointedAtZero += 1

    line = FileInput.readline()

print(TimesPointedAtZero)
print(TimesPastZero)

