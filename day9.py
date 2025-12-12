from shapely.geometry import Polygon, box

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

result = 0
polygon = Polygon(tiles)
for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        xi, yi = tiles[i]
        xj, yj = tiles[j]   
        rectangle = box(min(xi, xj), min(yi, yj), max(xi, xj), max(yi, yj))
        if polygon.covers(rectangle):
            width = abs(xi - xj) + 1
            height = abs(yi - yj) + 1
            result = max(result, width * height)
print(result)
