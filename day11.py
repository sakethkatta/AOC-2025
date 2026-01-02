file = open("day11.txt")
lines = [line.replace(":", "").split() for line in file]
graph = {line[0] : line[1:] for line in lines}

def dfs(node):
    return 1 if node == "out" else sum(dfs(nbr) for nbr in graph[node])
print(f"Part 1: {dfs('you')}")

cache = {}
required = {"dac", "fft"}
def dfs(node, visited: set):
    if node == "out":
        return 1 if visited == required else 0
    key = (node, frozenset(visited))
    if key in cache:
        return cache[key]
    if node in required:
        visited.add(node)
    cache[key] = sum(dfs(nbr, visited) for nbr in graph[node])
    if node in required:
        visited.remove(node)
    return cache[key]
print(f"Part 2 {dfs('svr', set())}")
