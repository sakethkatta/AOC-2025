file = open("day1.txt")
lines = file.readlines()

result = 0
pointing_at = 50
for line in lines:
    rotation = line[0]
    distance = int(line[1:])
    if rotation == "L":
        pointing_at -= distance
    else:
        pointing_at += distance
    pointing_at %= 100
    if pointing_at == 0:
        result += 1
print(f"Part 1: {result}")

result = 0
pointing_at = 50
for line in lines:
    rotation = line[0]
    distance = int(line[1:])
    for _ in range(distance):  
        if rotation == "L":
            pointing_at -= 1
        else:
            pointing_at += 1
        pointing_at %= 100
        if pointing_at == 0:
            result += 1
print(f"Part 2: {result}")
