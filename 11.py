import math
from collections import defaultdict

sn = 1309 #Real case
#sn = 18 #Test case

powerlevels = defaultdict(int)

for x in range(1, 301):
    print('{} / 300'.format(x))
    for y in range(1, 301):
        pl = 0
        for n in range(0, 300):
            if x + n > 300 or y + n > 300:
                continue
            if n > 0:
                for i in range(n + 1):
                    preHundreth = ((((x + i) + 10) * (y + n)) + sn) * ((x + i) + 10)
                    if preHundreth >= 100:
                        pl += int(str(preHundreth)[-3]) - 5
                    else:
                        pl -= 5
                for i in range(n):
                    preHundreth = ((((x + n) + 10) * (y + i)) + sn) * ((x + n) + 10)
                    if preHundreth >= 100:
                        pl += int(str(preHundreth)[-3]) - 5
                    else:
                        pl -= 5
            else:
                preHundreth = ((((x) + 10) * (y)) + sn) * ((x) + 10)
                if preHundreth >= 100:
                    pl += int(str(preHundreth)[-3]) - 5
                else:
                    pl -= 5
            powerlevels['{},{},{}'.format(x, y, n + 1)] = pl

value = max(powerlevels.values())
print('{}: {}'.format([k for k, v in powerlevels.items() if v == value], value))

