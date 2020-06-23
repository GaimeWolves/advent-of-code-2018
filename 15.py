from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.breadth_first import BreadthFirstFinder
from copy import deepcopy


class Unit: #faction = 0: Elfs =1: Goblins
        hp = None
        atk = None
        x = None
        y = None
        faction = None
        moved = None

        def __init__(self, x, y, faction):
                self.hp = 200
                self.atk = 3
                self.x = x
                self.y = y
                self.faction = faction
                self.moved = False

        def attack(self, caves, allies, enemies):
                enemy = []
                if any(self.y - 1 == e.y and self.x == e.x for e in enemies):
                        for i, e in enumerate(enemies):
                                if self.y - 1 == e.y and self.x == e.x:
                                        if len(enemy) == 0:
                                                enemy = [e.hp, e, i]
                                        elif e.hp < enemy[0]:
                                                enemy = [e.hp, e, i]
                if any(self.y == e.y and self.x - 1 == e.x for e in enemies):
                        for i, e in enumerate(enemies):
                                if self.y == e.y and self.x - 1 == e.x:
                                        if len(enemy) == 0:
                                                enemy = [e.hp, e, i]
                                        elif e.hp < enemy[0]:
                                                enemy = [e.hp, e, i]
                if any(self.y == e.y and self.x + 1 == e.x for e in enemies):
                        for i, e in enumerate(enemies):
                                if self.y == e.y and self.x + 1 == e.x:
                                        if len(enemy) == 0:
                                                enemy = [e.hp, e, i]
                                        elif e.hp < enemy[0]:
                                                enemy = [e.hp, e, i]
                if any(self.y + 1 == e.y and self.x == e.x for e in enemies):
                        for i, e in enumerate(enemies):
                                if self.y + 1 == e.y and self.x == e.x:
                                        if len(enemy) == 0:
                                                enemy = [e.hp, e, i]
                                        elif e.hp < enemy[0]:
                                                enemy = [e.hp, e, i]
                enemies[enemy[2]].hp -= self.atk
                return enemies

        def move(self, caves, allies, enemies):
                possiblesquares = []
                for enemy in enemies:
                        if len(enemy.getadjacent(caves, allies, enemies)) > 0:
                                possiblesquares.append(enemy.getadjacent(caves, allies, enemies))
                if len(possiblesquares) > 0:
                        grid = Grid(matrix=createGrid(caves, allies, enemies))
                        finder = BreadthFirstFinder(diagonal_movement=DiagonalMovement.never)
                        start = grid.node(self.x, self.y)
                        minimum = None
                        for i, squares in enumerate(possiblesquares):
                                for square in squares:
                                        end = grid.node(square[0], square[1])
                                        path, runs = finder.find_path(start, end, grid)
                                        #if self.x == 3 and self.y == 1:
                                                #print(grid.grid_str(path=path, start=start, end=end))
                                        if len(path) == 0:
                                                continue
                                        if minimum == None or len(path) < minimum[0] or (len(path) == minimum[0] and square[2] < minimum[2]):
                                                minimum = [len(path), path[1], square[2], square[0], square[1]]
                                        grid.cleanup()
                                grid.cleanup()
                        if minimum != None:
                                selected = None
                                end = grid.node(minimum[3], minimum[4])
                                for mysquare in self.getadjacent(caves, allies, enemies):
                                        start = grid.node(mysquare[0], mysquare[1])
                                        path, runs = finder.find_path(start, end, grid)
                                        #print(grid.grid_str(path=path, start=start, end=end))
                                        if len(path) == 0:
                                                continue
                                        if selected == None or len(path) < selected[0] or (len(path) == selected[0] and mysquare[2] < selected[2]):
                                                selected = [len(path), path[0], mysquare[2], mysquare[0], mysquare[1]]
                                        grid.cleanup()
                                self.x = selected[3]
                                self.y = selected[4]
                                if any(self.y + 1 == e.y and self.x == e.x for e in enemies) or any(self.y - 1 == e.y and self.x == e.x for e in enemies) or any(self.y == e.y and self.x + 1 == e.x for e in enemies) or any(self.y == e.y and self.x - 1 == e.x for e in enemies):
                                        enemies = self.attack(caves, allies, enemies)
                return enemies

        def step(self, caves, allies, enemies):
                self.moved = True
                if any(self.y + 1 == e.y and self.x == e.x for e in enemies) or any(self.y - 1 == e.y and self.x == e.x for e in enemies) or any(self.y == e.y and self.x + 1 == e.x for e in enemies) or any(self.y == e.y and self.x - 1 == e.x for e in enemies):
                        enemies = self.attack(caves, allies, enemies)
                else:
                        enemies = self.move(caves, allies, enemies)
                return enemies

        def __eq__(self, other):
                return self.x == other.x and self.y == other.y

        def getadjacent(self, caves, elfs, goblins):
                o = []
                grid = createGrid(caves, elfs, goblins)
                if grid[self.y + 1][self.x] == 1:
                        o.append([self.x, self.y + 1, 3, self])
                if grid[self.y][self.x - 1] == 1:
                        o.append([self.x - 1, self.y, 1, self])
                if grid[self.y][self.x + 1] == 1:
                        o.append([self.x + 1, self.y, 2, self])
                if grid[self.y - 1][self.x] == 1:
                        o.append([self.x, self.y - 1, 0, self])
                return o

        def __str__(self):
                return 'Faction: {} at ({}|{}) with {} HP'.format(self.faction, self.x, self.y, self.hp)

def printcave(caves, elfs, goblins):
        print()
        for e in elfs:
                print(e)
        for g in goblins:
                print(g)
        for y, line in enumerate(caves):
                for x, tile in enumerate(line):
                        if any(y == e.y and x == e.x for e in elfs):
                                print('E', end='')
                        elif any(y == g.y and x == g.x for g in goblins):
                                print('G', end='')
                        elif tile == 1:
                                print('.', end='')
                        else:
                                print('#', end='')
                print()
        print()

def createGrid(caves, elfs, goblins):
        copy = deepcopy(caves)
        for y, line in enumerate(caves):
                for x, tile in enumerate(line):
                        if any(y == e.y and x == e.x for e in elfs):
                                copy[y][x] = 0
                        elif any(y == g.y and x == g.x for g in goblins):
                                copy[y][x] = 0
        return copy

def printsuccess(rounds, winner):
        print()
        score = 0
        for u in winner:
                score += u.hp
        print('Remaining HP: {}'.format(score))
        score *= rounds
        if winner[0].faction == 0:
                print('Rounds: {} Score: {} Winner: Elfs'.format(rounds, score))
        else:
                print('Rounds: {} Score: {} Winner: Goblins'.format(rounds, score))
        exit()

#inputFile = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\15.txt", "r") #Normal case
inputFile = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\15-test.txt", "r") #Test case

caves = []
goblins = []
elfs = []

for y, line in enumerate(inputFile):
        caves.append([])
        for x, char in enumerate(line):
                if char == '#':
                        caves[y].append(0)
                elif char == '.':
                        caves[y].append(1)
                elif char == 'G':
                        goblins.append(Unit(x, y, 1))
                        caves[y].append(1)
                elif char == 'E':
                        elfs.append(Unit(x, y, 0))
                        caves[y].append(1)
                
printcave(caves, elfs, goblins)

rounds = 0

while True:
#for iterations in range(2):
        for g in goblins:
                g.moved = False
        for e in elfs:
                e.moved = False     
        for y in range(len(caves)):
                for x in range(len(caves[0])):
                        if any(y == e.y and x == e.x and not e.moved for e in elfs):
                                if len(goblins) == 0:
                                        printsuccess(rounds, elfs)
                                elf = [e for e in elfs if y == e.y and x == e.x and not e.moved][0]
                                goblins = elf.step(caves, elfs, goblins)
                                deads = [g for g in goblins if g.hp <= 0]
                                if len(deads) > 0:
                                        goblins.remove(deads[0])
                        elif any(y == g.y and x == g.x and not g.moved for g in goblins):
                                if len(elfs) == 0:
                                        printsuccess(rounds, goblins)
                                goblin = [g for g in goblins if y == g.y and x == g.x and not g.moved][0]
                                elfs = goblin.step(caves, goblins, elfs)
                                deads = [e for e in elfs if e.hp <= 0]
                                if len(deads) > 0:
                                        elfs.remove(deads[0])
        
        printcave(caves, elfs, goblins)
        print()
        rounds += 1