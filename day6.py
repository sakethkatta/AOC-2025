from math import prod

file = open("day6.txt")
lines = [line.strip().split() for line in file]

result = 0
for i in range(len(lines[0])):
    numbers = [int(lines[j][i]) for j in range(4)]
    if lines[4][i] == "*":
        result += prod(numbers)
    else:
        result += sum(numbers)
print(f"Part 1: {result}")

file.seek(0)
lines = [line.strip("\n") for line in file]

result = 0
numbers = []
for i in range(len(lines[0]) - 1, -1, -1):
    number = "".join(lines[j][i] for j in range(4))
    if not number.isspace():
        numbers.append(int(number))
    if lines[4][i] == "*":
        result += prod(numbers)
        numbers = []
    elif lines[4][i] == "+":
        result += sum(numbers)
        numbers = []
print(f"Part 2: {result}")
