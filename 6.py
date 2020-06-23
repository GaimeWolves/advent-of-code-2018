input = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\6.txt", "r")

#coords = [[1, 1, 0],[1, 6, 1],[8, 3, 2],[3, 4, 3],[5, 5, 4],[8, 9, 5]] #Test input
coords = [[int(s) for s in line.split(', ')] for line in input]

#Koordinaten IDs geben
for x in range(len(coords)):
    coords[x].append(x)

#Minimum und maximum berechnen
maxX = max(coords, key=lambda item:item[0])[0] + 1
maxY = max(coords, key=lambda item:item[1])[1] + 1

minX = min(coords, key=lambda item:item[0])[0]
minY = min(coords, key=lambda item:item[1])[1]  

#Raum initialisieren
space = [['-' for x in range(0, maxX)] for y in range(0, maxY)]

#Raum bestücken wie im Beispiel
for x in range(minX, maxX):
    for y in range(minY, maxY):
        coords.sort(key= lambda p: abs(x - p[0]) + abs(y - p[1])) #Sortieren nach Distanz zum Punkt (x|y)
        if abs(x - coords[0][0]) + abs(y - coords[0][1]) == abs(x - coords[1][0]) + abs(y - coords[1][1]):
            space[y][x] = "."
        else:
            space[y][x] = str(coords[0][2])

#Distanzfeld initialisieren
distances = [0 for x in range(len(coords))]

#Im Feld alle IDs zusammenzählen und an der entsprechenden Stelle im Distanzfeld eingeben
for x in range(maxX):
    for y in range(maxY):
        if space[y][x].isdigit():
            distances[int(space[y][x])] += 1

#Die größte Anzahl an Distanzen ausgeben
distances.sort()
print(distances[-1])

#Distanzfeld neu initialisieren
distances = [['-' for x in range(0, maxX)] for y in range(0, maxY)]

#Für jedes Feld im Raum die Distanz zu allen Punkten summieren und abspeichern
for x in range(minX, maxX):
    for y in range(minY, maxY):
        if distances[y][x] == '-':
            distances[y][x] = 0
        for coord in coords:
            distances[y][x] += abs(x - coord[0]) + abs(y - coord[1])

#Anzahl Felder mit Gesamtdistanz von unter 10000 bestimmen und ausgeben
total = 0

for x in range(minX, maxX):
    for y in range(minY, maxY):
        if distances[y][x] != '-':
            if distances[y][x] < 10000:
                total += 1

print(total)