inputfile = open("./20.txt", "r")

roomlenghts = []
check = []
current = 0
last = []

amount = []
added = False

for line in inputfile:
    for x, char in enumerate(line):
        if char == '$':
            roomlenghts.append(current)
        if char in 'NWES':
            current += 1
            if (current > 1001):
                amount.append(current)
                added = True
            else:
                added = False
        if char == '(':
            check.append(current)
                
        if char == '|':
            difference = current - check[-1]
            if line[x + 1] != ')':
                roomlenghts.append(current)
            else:
                roomlenghts.append(check[-1] + difference / 2)

            if len(amount) > 0 and added == True:
                if line[x + 1] == ')':
                    for y in range(int(difference / 2) + 2):
                        if (check[-1] + difference / 2 + y) > 1003:
                            amount.pop()

            current = check.pop()
            check.append(current)
        if char == ')' and line[x - 1] != '|':
            roomlenghts.append(current)
            current = check.pop()
            if line[x + 1] in 'NWSE($' and added == True:
                tX = x
                amount.pop()
                count = 1
                while count > 0:
                    tX -= 1
                    if (line[tX] == '|' and count == 1):
                        amount.pop() 
                    if (line[tX] == ')'):
                        count += 1
                    if (line[tX] == '('):
                        count -= 1

                



print(max(roomlenghts))
print(len(amount))

#8618 too high
#8468 solution