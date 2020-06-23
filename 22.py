from collections import defaultdict
import networkx as nx

f = open("./22.txt").read().strip("\n")

depth, tX, tY = [int(x) for x in f.split(" ") if x.isdigit()]

cave = defaultdict(lambda: [0, 0])
valid = {0: (1, 2), 1: (2, 0), 2: (1, 0)}

mod = 20183

cave[(0, 0)] = [0, depth % mod, depth % mod % 3]
cave[(tX, tY)] = [0, depth % mod, depth % mod % 3]

for y in range(tY + 101):
    cave[(0, y)] = [y * 48271, ((y * 48271) + depth) % mod, ((y * 48271) + depth) % mod % 3]

for x in range(tX + 101):
    cave[(x, 0)] = [x * 16807, ((x * 16807) + depth) % mod, ((x * 16807) + depth) % mod % 3]

for y in range(1, tY + 101):
    for x in range(1, tX + 101):
        if (x == tX and y == tY):
            continue
        gVal = cave[(x - 1, y)][1] * cave[(x, y - 1)][1]
        eVal = (gVal + depth) % mod
        cave[(x, y)] = [gVal, eVal, eVal % 3]

def printCave():
    global cave
    global tX
    global tY

    for y in range(0, tY + 101):
        for x in range(0, tX + 101):
            if (x == 0 and y == 0):
                print("M", end="")
                continue
            if (x == tX and y == tY):
                print("T", end="")
                continue
            rsk = cave[(x, y)][2]
            if (rsk == 0):
                print(".", end="")
            elif (rsk == 1):
                print("=", end="")
            else:
                print("|", end="")
        print()

def calcRisk():
    global cave
    global tX
    global tY

    risk = 0

    for y in range(0, tY + 1):
        for x in range(0, tX + 1):
            risk += cave[(x, y)][2]
    return risk

def pathfinding():
    global cave
    global tX
    global tY

    graph = nx.Graph()
    for y in range(0, tY + 101):
        for x in range(0, tX + 101):
            items = valid[cave[(x, y)][2]]
            graph.add_edge((x, y, items[0]), (x, y, items[1]), weight=7)
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if x + dx >= 0 and x + dx < tX + 101 and y + dy >= 0 and y + dy < tY + 101:
                    new_items = valid[cave[(x + dx, y + dy)][2]]
                    for item in set(new_items).intersection(set(items)):
                        graph.add_edge((x, y, item), (x + dx, y + dy, item), weight=1)
    
    return nx.dijkstra_path_length(graph, (0, 0, 1), (tX, tY, 1))


printCave()
print(calcRisk())
print(pathfinding())