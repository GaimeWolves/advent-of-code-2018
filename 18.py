import re
from PIL import Image, ImageDraw

inputfile = open("./18.txt", "r")

coords = []

xMax = 0
yMax = 0

def image_grid(grid, xM, yM, iteration):
    sand = (194, 178, 128)
    flowing = (0, 0, 255)
    standing = (0, 255, 255)
    clay = (153, 0, 0)
    spring = (5, 91, 61)
    width = xM + 2
    height = yM
    img = Image.new('RGB', (width, height), color = sand)
    dr = ImageDraw.Draw(img)
    for y, row in enumerate(field):
        for x, char in enumerate(row):
            if y == 0 and x == 500:
                dr.rectangle(((x-1,y),(x+1,y)),fill=spring)
            elif char == '#':
                dr.rectangle(((x,y),(x,y)),fill=clay)
            elif char in '_|':
                dr.rectangle(((x,y),(x,y)),fill=flowing)
            elif char == '~':
                dr.rectangle(((x,y),(x,y)),fill=standing)
    img.save(str(iteration) + ".png")

for line in inputfile:
    coords.append([int(s) for s in re.findall(r'\d+', line)])
    if (line[0] == 'x'):
        if (coords[-1][0] > xMax):
            xMax = coords[-1][0]
        if (coords[-1][1] > yMax):
            yMax = coords[-1][1]
        if (coords[-1][2] > yMax):
            yMax = coords[-1][2]
    else:
        if (coords[-1][0] > yMax):
            yMax = coords[-1][0]
        if (coords[-1][1] > xMax):
            xMax = coords[-1][1]
        if (coords[-1][2] > xMax):
            xMax = coords[-1][2]
    coords[-1].append(line[0])

field = [['.' for x in range(xMax + 1)] for y in range(yMax + 1)]

field[0][500] = '+'
field[1][500] = '|'

for coord in coords:
    if(coord[3] == 'x'):
        for y in range(coord[1], coord[2] + 1):
            field[y][coord[0]] = '#'
    else:
        for x in range(coord[1], coord[2] + 1):
            field[coord[0]][x] = '#'

checked = []
iteration = 0
while True:
    iteration += 1
    print(iteration)

    checked = []
    change = False
    for y, row in enumerate(field):
        for x, char in enumerate(row):
            if (char == '|'):
                if (y == len(field) - 1):
                    continue
                tY = y + 1
                while tY < len(field) and field[tY][x] == '.':
                    field[tY][x] = '|'
                    #checked.append(str(tY) + str(x))
                    tY += 1
                    change = True
                if (field[y + 1][x] not in '.|_'):
                    field[y][x] = '_'
                if (field[y][x] == '_' and field[y + 1][x] in '#~'):
                    static = True
                    tX = x
                    minX = -1
                    maxX = -1
                    direction = 0
                    while True:
                        if (direction == 0):
                            if field[y][tX - 1] == '#':
                                direction = 1
                                minX = tX
                                tX = x
                                continue
                            elif (field[y][tX - 1] == '.' and field[y + 1][tX - 1] == '.') or field[y][tX - 1] == '|':
                                field[y][tX - 1] = '|'
                                change = True
                                checked.append(str(y) + str(tX - 1))
                                static = False
                                direction = 1
                                minX = tX
                                tX = x
                                continue
                            tX -= 1
                        else:
                            if field[y][tX + 1] == '#':
                                maxX = tX
                                break
                            elif (field[y][tX + 1] == '.' and field[y + 1][tX + 1] == '.') or field[y][tX -+ 1] == '|':
                                field[y][tX + 1] = '|'
                                change = True
                                checked.append(str(y) + str(tX + 1))
                                static = False
                                maxX = tX
                                break
                            tX += 1
                    for tX in range(minX, maxX + 1):
                        if static == True:
                            field[y][tX] = '~'
                            change = True
                        else:
                            field[y][tX] = '_'

    image_grid(field, xMax, yMax, iteration) 
    #for row in field:
    #    print(row)

    if change == False:
        break

amount = 0

for y in field:
    for char in y:
        if char in '_|~':
            amount += 1

print(amount)