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
print(result)

beams = {start: 1}
for line in lines:
    newBeams = defaultdict(int)
    for beam, count in beams.items():
        if line[beam] == "^":
            newBeams[beam - 1] += count
            newBeams[beam + 1] += count
        else:
            newBeams[beam] += count
    beams = newBeams
print(sum(beams.values()))
