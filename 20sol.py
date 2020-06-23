from collections import *
import itertools
import random
import sys
import re

f = open("./20.txt").read().strip("\n")

d = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0)
}

positions = []
prev_x, prev_y = x, y = 0, 0
distances = defaultdict(int)
for c in f[1:-1]:
    if c == "(":
        positions.append((x, y))
    elif c == ")":
        x, y = positions.pop()
    elif c == "|":
        x, y = positions[-1]
    else:
        dx, dy = d[c]
        x += dx
        y += dy
        if distances[(x, y)] != 0:
            distances[(x, y)] = min(distances[(x, y)], distances[(prev_x, prev_y)]+1)
        else:
            distances[(x, y)] = distances[(prev_x, prev_y)]+1
    prev_x, prev_y = x, y

print(max(distances.values()))
print(len([x for x in distances.values() if x >= 1000]))