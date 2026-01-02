file = open("day5.txt")
lines = [line.strip() for line in file]
blank = lines.index("")

ranges = []
for line in lines[:blank]:
    start, end = line.split("-")
    ranges.append((int(start), int(end)))

ids = []
for line in lines[blank + 1:]:
    ids.append(int(line))

result = 0
for id in ids:
    for rng in ranges:
        if rng[0] <= id <= rng[1]:
            result += 1
            break
print(f"Part 1: {result}")

ranges.sort()
for i in range(len(ranges) - 1):
    if ranges[i][1] >= ranges[i + 1][0]:
        ranges[i + 1] = (ranges[i][0], max(ranges[i][1], ranges[i + 1][1]))
        ranges[i] = (1, 0)

result = 0
for rng in ranges:
    result += rng[1] - rng[0] + 1
print(f"Part 2: {result}")
