file = open("day2.txt")
ranges = file.readline().split(",")

result = 0
for rng in ranges:
    split = rng.split("-")
    lower = int(split[0])
    upper = int(split[1])
    for id in range(lower, upper + 1):
        id_str = str(id)
        if id_str[:len(id_str) // 2] * 2 == id_str:
            result += id
print(f"Part 1: {result}")

result = 0
for rng in ranges:
    split = rng.split("-")
    lower = int(split[0])
    upper = int(split[1])
    for id in range(lower, upper + 1):
        id_str = str(id)
        if id_str in (id_str * 2)[1:-1]:
            result += id
print(f"Part 2: {result}")
