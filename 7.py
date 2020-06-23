from string import ascii_uppercase
from collections import defaultdict
import copy

input = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\7.txt", "r") #Normal case
#input = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\7-test.txt", "r") #Test case

original = defaultdict(list)

order = ''

## Create the dictionary for every part eg. A to Z and their requirements eg. A requires D, F, Z => {'A': ['D', 'F', 'Z']}
#for char in ['A', 'B', 'C', 'D', 'E', 'F']: #Test case
for char in ascii_uppercase: #Normal case
    original[char] = []

for line in input:
    original[line[-13]].append(line[5])

directions = copy.deepcopy(original)

while True:
    current = ''

    ## Check for available parts to assemble eg. A = [] (No requirements)
    available = [part for part in directions if len(directions[part]) == 0]

    if len(available) > 0:
        current = min(available)
    else:
        break

    ## Add to building order
    order += current
    del directions[current]

    ## Delete key and every requirement for A
    for key, value in directions.items():
        index = [i for i, k in enumerate(value) if k == current]
        if len(index) > 0:
            del value[index[0]]
            directions[key] = value

## Print solution
print(order)

## Copy original directions
del directions
directions = copy.deepcopy(original)

## Initialize task list eg. [['A', 86 (seconds left)]] with first element of the old order
seconds = 0
tasks = []
#tasks = [['C', 3]] #Test case
tasks.append([order[0], ord(order[0]) - ord('A') + 61]) #Normal case
order = ''

while True:
    seconds += 1

    ## Create tasks for available parts
    available = [part for part in directions if len(directions[part]) == 0 and not any(part in sub for sub in tasks)] ## Every letter where no requirements are needed and no task is already running
    available.sort()

    for current in available:
        #if len(tasks) < 2: #Test case
        if len(tasks) < 5: #Normal case
            #tasks.append([current, ord(current) - ord('A') + 1]) #Test case
            tasks.append([current, ord(current) - ord('A') + 61]) #Normal case
            print('tasked: {}'.format(current))

    ## Test print
    print('tasks: {}    available: {}     order: {}    seconds: {}'.format(tasks, available, order, seconds))

    ## Update task timer and delete finished tasks
    for i, task in enumerate(tasks):
        task[1] -= 1
        if task[1] == 0:
            print('finished: {}'.format(task[0]))
            order += task[0]
            del directions[task[0]]
            for key, value in directions.items():
                index = [i for i, k in enumerate(value) if k == task[0]]
                if len(index) > 0:
                    del value[index[0]]
                    directions[key] = value
            if i < len(tasks) - 1:
                tasks[i + 1][1] -= 1
            del tasks[i]

    ## Test print
    print('tasks: {}    available: {}     order: {}    seconds: {}'.format(tasks, available, order, seconds))
    print()

    ## Exit when all directions are processed
    if len(tasks) == 0 and len(directions) == 0:
        break

## Print solution
print(seconds)    