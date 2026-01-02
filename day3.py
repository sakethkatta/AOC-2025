file = open("day3.txt")
lines = [line.strip() for line in file.readlines()]

result = 0
for line in lines:
    joltage = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            joltage = max(joltage, int(line[i] + line[j]))
    result += joltage
print(f"Part 1: {result}")

result = 0
for line in lines:
    start = 0
    batteries = []
    turn_on = 12
    while turn_on > 0:
        end = len(line) - turn_on + 1
        max_battery = max(line[start:end])
        battery_idx = line.index(max_battery, start, end)
        start = battery_idx + 1
        batteries.append(max_battery)
        turn_on -= 1
    result += int("".join(batteries))
print(f"Part 2: {result}")
