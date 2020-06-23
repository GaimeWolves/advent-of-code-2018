input = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\9.txt", "r") #Normal case
#input = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\9-test.txt", "r") #Test case

playercount, lastpoints = [int(s) for s in input.readlines()[0].split(' ') if s.isdigit()]

# Aufgabe 2
lastpoints *= 100
# /Aufgabe 2

marbles = [0, 1]
points = [0 for x in range(playercount)]

currentplayer = 1
currentmarble = 2
currentpointer = 1
lastmultiple = -1

for x in range(lastpoints):
    if lastmultiple != -1:
        currentmarble = lastmultiple + 1
        lastmultiple = -1
    if currentmarble % 23 == 0:
        points[currentplayer] += currentmarble
        lastmultiple = currentmarble
        currentpointer = (currentpointer - 7) % len(marbles)
        points[currentplayer] += marbles[currentpointer]  
        del marbles[currentpointer]
        currentplayer = (currentplayer + 1) % playercount
        #print(marbles)
        continue
    else:
        currentpointer = (currentpointer + 2) % len(marbles)
        if currentpointer == 0:
            marbles.append(currentmarble)
            currentpointer = len(marbles) - 1
        else:
            marbles.insert(currentpointer, currentmarble)


    currentmarble += 1
    currentplayer = (currentplayer + 1) % playercount
    #print(marbles)

print(max(points))