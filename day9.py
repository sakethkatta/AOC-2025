from shapely.geometry import Polygon, box

file = open("day9.txt")
lines = [line.strip().split(",") for line in file]
tiles = [(int(x), int(y)) for x, y in lines]

result = 0
for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        xi, yi = tiles[i]
        xj, yj = tiles[j]  
        area = (abs(xi - xj) + 1) * (abs(yi - yj) + 1)
        result = max(result, area)
print(f"Part 1: {result}")

result = 0
polygon = Polygon(tiles)
for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        xi, yi = tiles[i]
        xj, yj = tiles[j]   
        rectangle = box(min(xi, xj), min(yi, yj), max(xi, xj), max(yi, yj))
        if polygon.covers(rectangle):
            area = (abs(xi - xj) + 1) * (abs(yi - yj) + 1)
            result = max(result, area)
print(f"Part 2: {result}")
