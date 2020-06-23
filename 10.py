import matplotlib.pyplot as plt
import matplotlib.animation as anim
import time

inputFile = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\10.txt", "r") #Normal case
#inputFile = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\10-test.txt", "r") #Test case

iX = []
iY = []

Vx = []
Vy = []

for line in inputFile:
    var = [int(s) for s in line.split(' ') if s.isdigit() or (s != '' and s[0] == '-')]
    iX.append(var[0])
    iY.append(-var[1])

    Vx.append(var[2])
    Vy.append(-var[3])

second = 15000

def update(sec):
    oX = [0] * len(iX)
    oY = [0] * len(iX)
    for i in range(len(iX)):
        oX[i] = iX[i] + Vx[i] * (sec + 10875)
        oY[i] = iY[i] + Vy[i] * (sec + 10875)
    ax.clear()
    ax.scatter(oX, oY)
    print(oX)
    print(sec)
    plt.savefig('{}.png'.format(sec + 10875))
    #time.sleep(3)

fig = plt.figure()
ax = fig.add_subplot(111)


    ##s = input('{} seconds f or b: '.format(second))

    ##if s == 'b':
        #second -= 1
    ##elif s == 'x':
        ##exit()
    ##else:
a = anim.FuncAnimation(fig, update, frames=25000, repeat=False)
plt.show()