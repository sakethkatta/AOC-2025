file = open("day3.txt")
lines = [line.strip() for line in file.readlines()]

result = 0
for line in lines:
    joltage = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            joltage = max(joltage, int(line[i] + line[j]))
    result += joltage
print(result)

result = 0
for line in lines:
    start = 0
    batteries = []
    turnOn = 12
    while turnOn > 0:
        end = len(line) - turnOn + 1
        maxBattery = max(line[start:end])
        batteryIndex = line.index(maxBattery, start, end)
        start = batteryIndex + 1
        batteries.append(maxBattery)
        turnOn -= 1
    result += int("".join(batteries))
print(result)
