import os

file = open("vector.txt")
lines = [line.strip().split(",") for line in file]
tiles = [(int(x), int(y)) for x, y in lines]
reduce = 5000

grid_w = max(x for x, _ in tiles) // reduce + 1
grid_h = max(y for _, y in tiles) // reduce + 1
grid = [[False] * grid_h for _ in range(grid_w)]
for x, y in tiles:
    grid[x // reduce][y // reduce] = True

def visualize(min_x, max_x, min_y, max_y):
    min_i = min_x // reduce
    max_i = max_x // reduce
    min_j = min_y // reduce
    max_j = max_y // reduce
    rows = []
    for i in range(grid_w):
        row = []
        for j in range(grid_h):
            if min_i <= i <= max_i and min_j <= j <= max_j:
                row.append("O")
            elif grid[i][j]:
                row.append("#")
            else:
                row.append(".")
        rows.append(" ".join(row))
    return "\n".join(rows)

seen = set()
visuals = []
result = 0
resultVisual = None
for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        xi, yi = tiles[i]
        xj, yj = tiles[j]
        visual = visualize(min(xi, xj), max(xi, xj), min(yi, yj), max(yi, yj))
        if visual not in seen:
            seen.add(visual)
            visuals.append(visual)
        area = (abs(xi - xj) + 1) * (abs(yi - yj) + 1)
        if area > result:
            result = area
            resultVisual = visual

for visual in visuals:
    os.system("clear")
    print(visual)
    if input():
        os.system("clear")
        print(resultVisual)
        break
