from math import dist, prod
from collections import defaultdict

file = open("day8.txt")
lines = [line.strip().split(",") for line in file]
points = [(int(line[0]), int(line[1]), int(line[2])) for line in lines]

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append((dist(points[i], points[j]), points[i], points[j]))
distances.sort()

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_x] = root_y
        return True
    return False

parent = {point: point for point in points}
for i in range(1000):
    _, x, y = distances[i]
    union(x, y)

circuits = defaultdict(int)
for point in points:
    circuits[find(point)] += 1
print(f"Part 1: {prod(sorted(circuits.values())[-3:])}")

parent = {point: point for point in points}
circuits = len(points)
for distance in distances:
    _, x, y = distance
    if union(x, y):
        circuits -= 1
    if circuits == 1:
        print(f"Part 2: {x[0] * y[0]}")
        break
