from collections import defaultdict

file = open("day7.txt")
start = file.readline().index("S")
lines = [line.strip() for line in file if "^" in line]

beams = {start}
result = 0
for line in lines:
    for beam in list(beams):
        if line[beam] == "^":
            result += 1
            beams.remove(beam)
            beams.add(beam - 1)
            beams.add(beam + 1)
print(f"Part 1: {result}")

beams = {start: 1}
for line in lines:
    new_beams = defaultdict(int)
    for beam, count in beams.items():
        if line[beam] == "^":
            new_beams[beam - 1] += count
            new_beams[beam + 1] += count
        else:
            new_beams[beam] += count
    beams = new_beams
print(f"Part 2: {sum(beams.values())}")
