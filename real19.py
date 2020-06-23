inputfile = open("./real19t.txt", "r")

ip = 0
ipreg = None

instructions = []
registers = [0, 0, 0, 0, 0, 0]

def step(instruction):
    global ip
    global registers
    global ipreg
    registers[ipreg] = ip

    if instruction[0] == 'addr':
        registers[instruction[3]] = registers[instruction[1]] + registers[instruction[2]]
    elif instruction[0] == 'addi':
        registers[instruction[3]] = registers[instruction[1]] + instruction[2]

    elif instruction[0] == 'mulr':
        registers[instruction[3]] = registers[instruction[1]] * registers[instruction[2]]
    elif instruction[0] == 'muli':
        registers[instruction[3]] = registers[instruction[1]] * instruction[2]

    elif instruction[0] == 'banr':
        registers[instruction[3]] = registers[instruction[1]] & registers[instruction[2]]
    elif instruction[0] == 'bani':
        registers[instruction[3]] = registers[instruction[1]] & instruction[2]

    elif instruction[0] == 'borr':
        registers[instruction[3]] = registers[instruction[1]] | registers[instruction[2]]
    elif instruction[0] == 'bori':
        registers[instruction[3]] = registers[instruction[1]] | instruction[2]

    elif instruction[0] == 'setr':
        registers[instruction[3]] = registers[instruction[1]]
    elif instruction[0] == 'seti':
        registers[instruction[3]] = instruction[1]

    elif instruction[0] == 'gtir':
        registers[instruction[3]] = 1 if instruction[1] > registers[instruction[2]] else 0
    elif instruction[0] == 'gtri':
        registers[instruction[3]] = 1 if registers[instruction[1]] > instruction[2] else 0
    elif instruction[0] == 'gtrr':
        registers[instruction[3]] = 1 if registers[instruction[1]] > registers[instruction[2]] else 0

    elif instruction[0] == 'eqir':
        registers[instruction[3]] = 1 if instruction[1] == registers[instruction[2]] else 0
    elif instruction[0] == 'eqri':
        registers[instruction[3]] = 1 if registers[instruction[1]] == instruction[2] else 0
    elif instruction[0] == 'eqrr':
        registers[instruction[3]] = 1 if registers[instruction[1]] == registers[instruction[2]] else 0

    ip = registers[ipreg]
    ip += 1

for line in inputfile:
    if line[0] != '#':
        splits = line.split(" ")
        instructions.append([splits[0], int(splits[1]), int(splits[2]), int(splits[3])])
    else:
        ipreg = int(line[-2])

iteration = 0
oldR1 = 0
allR1 = []

print("{} {}".format(ip, registers))
while ip >= 0 and ip < len(instructions):
    step(instructions[ip])
    if (oldR1 != registers[1] and ip == 28):
        oldR1 = registers[1]
        if oldR1 in allR1:
            print("DUPLICATE {}".format(oldR1))
            exit(0)
        allR1.append(oldR1)
        print(registers[1])
        #print("{} {}".format(ip, registers))
    iteration += 1