file = open("day1.txt")
lines = file.readlines()

result = 0
pointing = 50
for line in lines:
    rotation = line[0]
    distance = int(line[1:])
    if rotation == "L":
        pointing -= distance
    else:
        pointing += distance
    pointing %= 100
    if pointing == 0:
        result += 1
print(result)

result = 0
pointing = 50
for line in lines:
    rotation = line[0]
    distance = int(line[1:])
    for _ in range(distance):  
        if rotation == "L":
            pointing -= 1
        else:
            pointing += 1
        pointing %= 100
        if pointing == 0:
            result += 1
print(result)
