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

def visualize(lx, hx, ly, hy):
    min_i = lx // reduce
    max_i = hx // reduce
    min_j = ly // reduce
    max_j = hy // reduce
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
for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        xi, yi = tiles[i]
        xj, yj = tiles[j]
        visual = visualize(min(xi, xj), max(xi, xj), min(yi, yj), max(yi, yj))
        if visual not in seen:
            seen.add(visual)
            visuals.append(visual)

for visual in visuals:
    os.system("clear")
    print(visual)
    input()
