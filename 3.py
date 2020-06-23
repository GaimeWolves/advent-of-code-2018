input = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\3.txt", "r")

width = 0
height = 0

inputList = []

for line in input:
    parts = line.split()

    offsetString = parts[2]
    sizeString = parts[3]

    offsetX = int(offsetString.split(',')[0])
    offsetY = int(offsetString.split(',')[1][0: -1])

    sizeX = int(sizeString.split('x')[0])
    sizeY = int(sizeString.split('x')[1])

    id = int(parts[0].split('#')[1])

    inputList.append([offsetX, offsetY, sizeX, sizeY, id])

    if offsetX + sizeX > width:
        width = offsetX + sizeX

    if offsetY + sizeY > height:
        height = offsetY + sizeY

fabric = [['.' for y in range(height)] for x in range(width)]

for piece in inputList:
    oX = piece[0]
    oY = piece[1]
    for x in range(piece[2]):
        for y in range(piece[3]):
            if fabric[oX + x][oY + y] == '.':
                fabric[oX + x][oY + y] = '#'
            else:
                fabric[oX + x][oY + y] = 'X'

multiples = 0

for row in fabric:
    for inch in row:
        if inch == 'X':
            multiples += 1

print(multiples)

#Zweite Aufgabe

id = 0

for piece in inputList:
    oX = piece[0]
    oY = piece[1]

    got = True

    for x in range(piece[2]):
        for y in range(piece[3]):
            if fabric[oX + x][oY + y] != '#':
                got = False

    if got == True:
        id = piece[4]

print(id)