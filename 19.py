from copy import deepcopy

inputfile = open("./19.txt", "r")

field = [[0 for x in range(50)] for y in range(50)]

def printfield(field):
    for line in field:
        for num in line:
            if num == 0:
                print('.', end='')
            elif num == 1:
                print('|', end='')
            else:
                print('#', end='')
        print()
    print()

def value(char, trees, fields, yards):
    if char == 0:
        fields += 1
    elif char == 1:
        trees += 1
    else:
        yards += 1
    return trees, field, yards

for y, line in enumerate(inputfile):
    for x, char in enumerate(line):
        if char == '|':
            field[y][x] = 1
        elif char == '#':
            field[y][x] = 2

for iteration in range(1000000000):
    #if (x % 100 == 0):
    #    print("{} / {}".format(x, 1000000000))
    old = deepcopy(field)
    for y, line in enumerate(old):
        for x, num in enumerate(line):
            adjTrees = 0
            adjField = 0
            adjYards = 0

            if y > 0 and x > 0:
                if old[y - 1][x - 1] == 0:
                    adjField += 1
                elif old[y - 1][x - 1] == 1:
                    adjTrees += 1
                else:
                    adjYards += 1
            if y > 0:
                if old[y - 1][x] == 0:
                    adjField += 1
                elif old[y - 1][x] == 1:
                    adjTrees += 1
                else:
                    adjYards += 1
            if y > 0 and x < len(line) - 1:
                if old[y - 1][x + 1] == 0:
                    adjField += 1
                elif old[y - 1][x + 1] == 1:
                    adjTrees += 1
                else:
                    adjYards += 1

            if x > 0:
                if old[y][x - 1] == 0:
                    adjField += 1
                elif old[y][x - 1] == 1:
                    adjTrees += 1
                else:
                    adjYards += 1
            if x < len(line) - 1:
                if old[y][x + 1] == 0:
                    adjField += 1
                elif old[y][x + 1] == 1:
                    adjTrees += 1
                else:
                    adjYards += 1

            if y < len(old) - 1 and x > 0:
                if old[y + 1][x - 1] == 0:
                    adjField += 1
                elif old[y + 1][x - 1] == 1:
                    adjTrees += 1
                else:
                    adjYards += 1
            if y < len(old) - 1:
                if old[y + 1][x] == 0:
                    adjField += 1
                elif old[y + 1][x] == 1:
                    adjTrees += 1
                else:
                    adjYards += 1
            if y < len(old) - 1 and x < len(line) - 1:
                if old[y + 1][x + 1] == 0:
                    adjField += 1
                elif old[y + 1][x + 1] == 1:
                    adjTrees += 1
                else:
                    adjYards += 1

            if num == 0 and adjTrees >= 3:
                field[y][x] = 1
            elif num == 1 and adjYards >= 3:
                field[y][x] = 2
            elif num == 2 and (adjTrees < 1 or adjYards < 1):
                field[y][x] = 0

    #printfield(field)
    trees = 0
    yards = 0

    for line in field:
        for num in line:
            if num == 1:
                trees += 1
            elif num == 2:
                yards += 1

    print("{} {}".format(iteration, trees * yards))

#Periode = 28