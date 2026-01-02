file = open("day9.txt")
lines = [line.strip().split(",") for line in file]
tiles = [(int(x), int(y)) for x, y in lines]

result = 0
for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        width = abs(tiles[i][0] - tiles[j][0]) + 1
        height = abs(tiles[i][1] - tiles[j][1]) + 1
        result = max(result, width * height)
print(result)

max_x = max(tiles, key=lambda tile: tile[0])[0]
max_y = max(tiles, key=lambda tile: tile[1])[1]
reduce = 5000

for i in range(max_y // reduce + 1):
    for j in range(max_x // reduce + 1):
        has_tile = any(
            j * reduce <= x < (j + 1) * reduce and
            i * reduce <= y < (i + 1) * reduce
            for x, y in tiles
        )
        print("# " if has_tile else ". ", end="")
    print()
