from collections import deque

input = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\9.txt", "r") #Normal case
#input = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\9-test.txt", "r") #Test case

playercount, lastpoints = [int(s) for s in input.readlines()[0].split(' ') if s.isdigit()]

# Aufgabe 2
lastpoints *= 100
# /Aufgabe 2

marbles = deque([0, 1])
marbles.rotate(-1)
points = [0 for x in range(playercount)]

for x in range(lastpoints):
    if x % 23 == 0:
        marbles.rotate(7)
        points[x % playercount] += x + marbles.pop()
        marbles.rotate(-1)
    else:
        marbles.rotate(-1)
        marbles.append(x)

print(max(points))