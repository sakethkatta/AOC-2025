file = open("input2.txt")
ranges = file.readline().split(",")

result = 0
for idRange in ranges:
    split = idRange.split("-")
    lower = int(split[0])
    upper = int(split[1])
    for id in range(lower, upper + 1):
        idStr = str(id)
        if len(idStr) % 2 == 0 and idStr[:len(idStr) // 2] * 2 == idStr:
            result += id
print(result)

result = 0
for idRange in ranges:
    split = idRange.split("-")
    lower = int(split[0])
    upper = int(split[1])
    for id in range(lower, upper + 1):
        idStr = str(id)
        if idStr in (idStr * 2)[1:-1]:
            result += id
print(result)
