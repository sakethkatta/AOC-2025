from itertools import combinations
from pulp import LpProblem, LpVariable, LpInteger, lpSum, PULP_CBC_CMD, value

file = open("day10.txt")
lines = [line.strip().split() for line in file]

def part1(indicator, buttons):
    for presses in range(len(buttons) + 1):
        for combination in combinations(buttons, presses):
            result = [0] * len(indicator)
            for button in combination:
                for toggle in button:
                    result[toggle] ^= 1
            if result == indicator:
                return presses

def part2(buttons, joltage):
    problem = LpProblem()
    variables = [LpVariable(str(i), lowBound=0, cat=LpInteger) for i in range(len(buttons))]
    for j in range(len(joltage)):
        problem += lpSum(variables[i] for i in range(len(buttons)) if j in buttons[i]) == joltage[j]
    problem += lpSum(variables)
    problem.solve(PULP_CBC_CMD(msg=0))
    return int(value(problem.objective))

result1 = 0
result2 = 0
for line in lines:
    indicator = [1 if light == "#" else 0 for light in list(line[0])[1:-1]]
    buttons = [[int(toggle) for toggle in button[1:-1].split(",")] for button in line[1:-1]]
    joltage = [int(level) for level in line[-1][1:-1].split(",")]
    result1 += part1(indicator, buttons)
    result2 += part2(buttons, joltage)
print(f"Part 1: {result1}")
print(f"Part 2: {result2}")
