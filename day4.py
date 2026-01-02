def find_at(grid, r, c):
    count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "@":
            count += 1
    return count

file = open("day4.txt")
grid = [list(line.strip()) for line in file.readlines()]

result = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "@" and find_at(grid, r, c) < 4:
            result += 1
print(f"Part 1: {result}")

result = 0
while True:
    removed = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@" and find_at(grid, r, c) < 4:
                grid[r][c] = "x"
                removed += 1
    if removed == 0:
        break
    result += removed
print(f"Part 2: {result}")
