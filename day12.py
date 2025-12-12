file = open("day12.txt").read().split("\n\n")
regions = [region.replace("x", " ").replace(":", "").split() for region in file[-1].split("\n")]

result = 0
for region in regions:
    region = list(map(int, region))
    area = 0
    for i in range(len(region[2:])):
        area += 9 * region[2 + i]
    if area <= region[0] * region[1]:
        result += 1
print(f"Part 1: {result}")
