import re
import numpy as np

f = open("./23.txt", "r")

def dist(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1]) + abs(b[2] - a[2])

def average(bots):
    return [np.average([n[0] for n in bots]), np.average([n[1] for n in bots]), np.average([n[2] for n in bots])]

def interpolate(pos, dest, amount):
    pos[0] += int((dest[0] - pos[0]) * amount)
    pos[1] += int((dest[1] - pos[1]) * amount)
    pos[2] += int((dest[2] - pos[2]) * amount)
    return pos

nanobots = []

for line in f:
    nanobots.append([int(s) for s in re.findall(r'[-\d]+', line)])

for bot in nanobots:
    print(bot)

nanobots.sort(key=lambda i: i[3], reverse=True)
print(len([n for n in nanobots if dist(nanobots[0], n) <= nanobots[0][3]]))

pos = [14641398, 45677204, 26936254]
outofrange = []

average(nanobots)

for x in range(1000):
    outofrange = [n for n in nanobots if dist(pos, n) > n[3]]
    pos = interpolate(pos, average(outofrange), len(outofrange) / (len(nanobots) * 1000))
    print("({} {} {}), {}".format(int(pos[0]), int(pos[1]), int(pos[2]), len(outofrange)))

#x: 14640000, 14643000
#y: 45677000, 45680000
#z: 26934000, 26938000

import z3

def zabs(x):
  return z3.If(x >= 0,x,-x)

(x, y, z) = (z3.Int('x'), z3.Int('y'), z3.Int('z'))
o = z3.Optimize()

range_count = z3.Int('sum')
in_ranges = [z3.Int('in_range_' + str(i)) for i in range(len(nanobots))]

for i in range(len(nanobots)):
    bx, by, bz, brange = nanobots[i]
    o.add(in_ranges[i] == z3.If(zabs(x - bx) + zabs(y - by) + zabs(z - bz) <= brange, 1, 0))
o.add(range_count == sum(in_ranges))
distance = z3.Int('dist')
o.add(distance == zabs(x) + zabs(y) + zabs(z))
h1 = o.maximize(range_count)
h2 = o.minimize(distance)
print(o.check())
print(o.lower(h2))
