from collections import defaultdict
import copy

inputFile = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\12.txt", "r") #Normal case
#inputFile = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\12-test.txt", "r") #Test case
outputfile = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\12o.txt", "w")

pots = defaultdict(lambda: '.')
ruleset = defaultdict(lambda: '.')

for line in inputFile:
    if 'initial state' in line:
        for i, c in enumerate(line.split(' ')[-2]):
            pots[i] = c 
    elif '=>' in line:
        parts = line.split(' ')
        ruleset[parts[0]] = parts[-2]

def printPots(pots, generation):
        outputfile.write('{:03d}: '.format(generation))
        sorted_by_value = sorted(pots.items(), key=lambda kv: kv[0])
        for v in sorted_by_value:
                outputfile.write('{}'.format(v[1]))
        outputfile.write('\n')

printPots(pots, 0)

for x in range(193):
        oldPots = copy.deepcopy(pots)
        for i in range(min(oldPots) - 2, max(oldPots) + 3):
                pots[i] = ruleset[oldPots[i - 2] + oldPots[i - 1] + oldPots[i] + oldPots[i + 1] + oldPots[i + 2]]
    
        printPots(pots, x + 1)
        #indices = []
        #for index, plant in pots.items():
        #    if plant == '.':
        #        indices.append(index)
        #for index in indices:
        #        del pots[index]

        #minI = min([k for k, v in pots.items() if v == '#']) + 1
        #maxI = max([k for k, v in pots.items() if v == '#']) + 1
#
        #for x in range(min(pots.keys()), minI):
        #        del pots[x]
        #for x in range(maxI, max(pots.keys())):
        #        del pots[x]

score = 0

for index, plant in pots.items():
        if plant == '#':
                score += index

## Nach 191 iterationen wird der score immer 34 größer (wird regelmäßig siehe 12o.txt)
print(6505 + (50000000000 - 191) * 34)
