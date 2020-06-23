import datetime

input = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\4.txt", "r")

def getKey0(item):
    return item[0]

def getKey2(item):
    return item[2]

timestamps = []

for line in input:
    time = datetime.datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')

    if 'asleep' in line:
        timestamps.append([time, 'a'])
    elif 'wakes' in line:
        timestamps.append([time, 'w'])
    else:
        timestamps.append([time, int(line[26:].split(' ')[0])])

timestamps.sort(key=getKey0)

days = []
asleeptime = 0

g = []

for stamp in timestamps:
    if stamp[1] == 'a':
        asleeptime = stamp[0].minute
    elif stamp[1] == 'w':
        for x in range(asleeptime, stamp[0].minute):
            g[3][x] += 1
            g[2] += 1
    else:
        if len(g) > 0:
            days.append(g)
            g = []
        g.append(stamp[1])
        g.append(1)
        g.append(0)
        g.append([0 for x in range(60)])

days.append(g)

days.sort(key=getKey2)
for guard in days:
    print(guard)

guards = []

for day in days:
    found = False
    for guard in guards:
        if guard[0] == day[0]:
            for x in range(60):
                guard[-1][x] += day[-1][x]
            found = True
    if found == False:
        guards.append(day)

print()
for guard in guards:
    print(guard)

largest = -1
index = -1
for x in range(60):
    if guards[-1][-1][x] > largest:
        largest = guards[-1][-1][x]
        index = x

print(guards[-1][0] * index)

#aufgabe 2

id = 0
for guard in guards:
    for x in range(60):
        if guard[-1][x] > largest:
            largest = guard[-1][x]
            index = x
            id = guard[0]

print(id * index)