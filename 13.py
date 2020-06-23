from collections import defaultdict
import copy

class Cart:
        globalID = 0
        id = None
        x = None
        y = None
        direction = None
        lastRotation = None
        moved = None

        def __init__(self):
                self.id = Cart.globalID
                Cart.globalID += 1

        def move(self):
                if self.direction == '^':
                        self.y -= 1
                elif self.direction == '>':
                        self.x += 1
                elif self.direction == 'v':
                        self.y += 1
                elif self.direction == '<':
                        self.x -= 1
                self.moved = True

        def step(self, nextChar):
                if nextChar == 'c':
                        self.direction == 'X'
                elif nextChar == '+':
                        if self.lastRotation == -1:
                                self.rotate(0)
                        elif self.lastRotation == 0:
                                self.rotate(1)
                        else:
                                self.rotate(-1)
                elif nextChar == '/':
                        if self.direction == '^':
                                self.direction = '>'
                        elif self.direction == '>':
                                self.direction = '^'
                        elif self.direction == 'v':
                                self.direction = '<'
                        elif self.direction == '<':
                                self.direction = 'v'
                elif nextChar == '\\':
                        if self.direction == '^':
                                self.direction = '<'
                        elif self.direction == '>':
                                self.direction = 'v'
                        elif self.direction == 'v':
                                self.direction = '>'
                        elif self.direction == '<':
                                self.direction = '^'

                                
        def rotate(self, rotation):
                if rotation == -1:
                        if self.direction == '^':
                                self.direction = '<'
                        elif self.direction == '>':
                                self.direction = '^'
                        elif self.direction == 'v':
                                self.direction = '>'
                        else:
                                self.direction = 'v'
                elif rotation == 1:
                        if self.direction == '^':
                                self.direction = '>'
                        elif self.direction == '>':
                                self.direction = 'v'
                        elif self.direction == 'v':
                                self.direction = '<'
                        else:
                                self.direction = '^'
                self.lastRotation = rotation


inputFile = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\13.txt", "r") #Normal case
#inputFile = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\13-test.txt", "r") #Test case

carts = []
railway = []

for y, line in enumerate(inputFile):
        railway.append([])
        for x, char in enumerate(line):
                if char != '\n':
                        railway[y].append(char)

def printrailway(railway, carts):
        foundx = False
        Xx = 0
        Yx = 0
        for y, line in enumerate(railway):
                for x, char in enumerate(line):
                        if char == 'X':
                                foundx = True
                                Xx = x
                                Yx = y
                        found = False
                        for cart in carts:
                                if cart.x == x and cart.y == y:
                                        found = True
                                        print(cart.direction, end='')
                        if found == False:
                                print(char, end='')
                print()
        print()
        if foundx == True:
                print('X: ({}|{})'.format(Xx, Yx))
                exit()

printrailway(railway, carts)

for y, line in enumerate(railway):
                for x, char in enumerate(line):
                        found = False
                        for cart in carts:
                                if cart.x == x and cart.y == y:
                                        found = True
                                        if cart.moved == False:
                                                cart.move()
                                                cart.step(railway[cart.y][cart.x])
                        if char in '^<>v' and found == False:
                                newCart = Cart()
                                newCart.x = x
                                newCart.y = y
                                newCart.direction = char
                                newCart.lastRotation = '1'
                                newCart.move()
                                newCart.step(railway[newCart.y][newCart.x])
                                carts.append(newCart)
                                if   railway[y][x] != ' ' and     (y > 0 and railway[y - 1][x] in '|+/\\') and     (y < len(railway) -1 and railway[y + 1][x] in '|+/\\') and     (x > 0 and railway[y][x - 1] in '-+/\\') and     (x < len(railway[0]) - 1 and railway[y][x + 1] in '-+/\\'):
                                     railway[y][x] = '+'
                                elif railway[y][x] != ' ' and     (y > 0 and railway[y - 1][x] in '|+/\\') and     (y < len(railway) -1 and railway[y + 1][x] in '|+/\\'):
                                     railway[y][x] = '|'
                                elif railway[y][x] != ' ' and     (x > 0 and railway[y][x - 1] in '-+/\\') and     (x < len(railway[0]) - 1 and railway[y][x + 1] in '-+/\\'):
                                     railway[y][x] = '-'
                                elif railway[y][x] != ' ' and     (y > 0 and railway[y - 1][x] in '|+/\\') and     (x > 0 and railway[y][x - 1] in '-+/\\'):
                                     railway[y][x] = '/'
                                elif railway[y][x] != ' ' and     (y < len(railway) -1 and railway[y + 1][x] in '|+/\\') and     (x < len(railway[0]) - 1 and railway[y][x + 1] in '-+/\\'):
                                     railway[y][x] = '/'
                                elif railway[y][x] != ' ' and     (y < len(railway) -1 and railway[y + 1][x] in '|+/\\') and     (x > 0 and railway[y][x - 1] in '-+/\\'):
                                     railway[y][x] = '\\'
                                elif railway[y][x] != ' ' and     (y > 0 and railway[y - 1][x] in '|+/\\') and     (x < len(railway[0]) - 1 and railway[y][x + 1] in '-+/\\'):
                                     railway[y][x] = '\\'

for cart in carts:
        cart.moved = False

printrailway(railway, carts)

counter = 0
while True:
#for x in range(0):
        print(counter)
        for y, line in enumerate(railway):
                for x, char in enumerate(line):
                        for cart in carts:
                                if cart.x == x and cart.y == y:
                                        if cart.moved == False:
                                                cart.move()
                                                if any(cart2.x == cart.x and cart2.y == cart.y and cart2.id != cart.id for cart2 in carts):
                                                        cart.step('c')
                                                        #railway[cart.y][cart.x] = 'X'
                                                        cart2 = [cart2 for cart2 in carts if cart2.x == cart.x and cart2.y == cart.y and cart2.id != cart.id]
                                                        carts.remove(cart2[0])
                                                        carts.remove(cart)
                                                else:
                                                        cart.step(railway[cart.y][cart.x])

        for cart in carts:
                cart.moved = False
        #printrailway(railway, carts)
        if len(carts) == 1:
                print()
                print('{},{}'.format(carts[0].x, carts[0].y))
                exit()
        counter += 1