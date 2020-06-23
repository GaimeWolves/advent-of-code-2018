from copy import deepcopy
from collections import defaultdict

registers = [0, 0, 0, 0]
testoutput = [0, 0, 0, 0]
opcode = [0, 0, 0, 0]

inputFile = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\16.txt", "r") #Normal case
inputFileTest = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\16-test.txt", "r") #Test case

def testOps(possible, input, opcode, output):
        possible = defaultdict(list)
        lenght = 0
        if input[opcode[1]] + input[opcode[2]] == output[opcode[3]]:
                possible[opcode[0]].append('addr')
                lenght += 1
        if input[opcode[1]] + opcode[2] == output[opcode[3]]:
                possible[opcode[0]].append('addi')
                lenght += 1

        if input[opcode[1]] * input[opcode[2]] == output[opcode[3]]:
                possible[opcode[0]].append('mulr')
                lenght += 1
        if input[opcode[1]] * opcode[2] == output[opcode[3]]:
                possible[opcode[0]].append('muli')
                lenght += 1

        if input[opcode[1]] & input[opcode[2]] == output[opcode[3]]:
                possible[opcode[0]].append('banr')
                lenght += 1
        if input[opcode[1]] & opcode[2] == output[opcode[3]]:
                possible[opcode[0]].append('bani')
                lenght += 1

        if input[opcode[1]] | input[opcode[2]] == output[opcode[3]]:
                possible[opcode[0]].append('borr')
                lenght += 1
        if input[opcode[1]] | opcode[2] == output[opcode[3]]:
                possible[opcode[0]].append('bori')
                lenght += 1

        if input[opcode[1]] == output[opcode[3]]:
                possible[opcode[0]].append('setr')
                lenght += 1
        if opcode[1] == output[opcode[3]]:
                possible[opcode[0]].append('seti')
                lenght += 1

        if (opcode[1] > input[opcode[2]] and output[opcode[3]] == 1) or (opcode[1] <= input[opcode[2]] and output[opcode[3]] == 0):
                possible[opcode[0]].append('gtir')
                lenght += 1
        if (input[opcode[1]] > opcode[2] and output[opcode[3]] == 1) or (input[opcode[1]] <= opcode[2] and output[opcode[3]] == 0):
                possible[opcode[0]].append('gtri')
                lenght += 1
        if (input[opcode[1]] > input[opcode[2]] and output[opcode[3]] == 1) or (input[opcode[1]] <= input[opcode[2]] and output[opcode[3]] == 0):
                possible[opcode[0]].append('gtrr')
                lenght += 1

        if (opcode[1] == input[opcode[2]] and output[opcode[3]] == 1) or (opcode[1] != input[opcode[2]] and output[opcode[3]] == 0):
                possible[opcode[0]].append('eqir')
                lenght += 1
        if (input[opcode[1]] == opcode[2] and output[opcode[3]] == 1) or (input[opcode[1]] != opcode[2] and output[opcode[3]] == 0):
                possible[opcode[0]].append('eqri')
                lenght += 1
        if (input[opcode[1]] == input[opcode[2]] and output[opcode[3]] == 1) or (input[opcode[1]] != input[opcode[2]] and output[opcode[3]] == 0):
                possible[opcode[0]].append('eqrr')
                lenght += 1

        return possible, lenght

possible = []
nof = 0

for line in inputFile:
        if 'Before: ' in line:
                registersText = line.split('[')[1]
                registersText = registersText.replace(',', '')
                registersText = registersText.replace(']', '')
                registersText = registersText.replace('\n', '')
                registers = [int(s) for s in registersText.split(' ') if s.isdigit()]
        elif 'After: ' in line:
                registersText = line.split('[')[1]
                registersText = registersText.replace(',', '')
                registersText = registersText.replace(']', '')
                registersText = registersText.replace('\n', '')
                testoutput = [int(s) for s in registersText.split(' ') if s.isdigit()]
        elif line == 'end':
                print(nof)
                exit()
        elif line != '\n' and 'Before: ' not in line and 'After: ' not in line:
                registersText = line.replace('\n', '')
                opcode = [int(s) for s in registersText.split(' ') if s.isdigit()]
        elif line == '\n':
                testinput = deepcopy(registers)
                possibledict, lenght = testOps(possible, testinput, opcode, testoutput)
                possible.append(possibledict)
                if lenght > 2:
                        nof += 1

def getopcode(possible, code):
        possibilities = [dictionary for dictionary in possible if code in dictionary]
        opcode = defaultdict(lambda: len(possibilities))
        for dictionary in possibilities:
                for k in dictionary[code]:
                        opcode[k] -= 1
        return opcode

opcodes = defaultdict(str)

numbers = []

for x in range(16):
        numbers.append(getopcode(possible, x))

while True:
        doExit = False
        for opcode, number in enumerate(numbers):
                if len(opcodes) == 16:
                        doExit = True
                        break
                if len([v for v in number.values() if v == 0]) == 1:
                        code = list(number.keys())[0]
                        opcodes[opcode] =  code
                        for number2 in numbers:
                                if code in number2:
                                        del number2[code]
        if doExit == True:
                break

print(opcodes)
print(registers)

def doOperation(opcodes, opcode, inputs):
        output = deepcopy(inputs)
        input = deepcopy(inputs)

        if   opcodes[opcode[0]] == 'addr':
                output[opcode[3]] = input[opcode[1]] + input[opcode[2]]
        elif opcodes[opcode[0]] == 'addi':
                output[opcode[3]] = input[opcode[1]] + opcode[2]

        elif opcodes[opcode[0]] == 'mulr':
                output[opcode[3]] = input[opcode[1]] * input[opcode[2]]
        elif opcodes[opcode[0]] == 'muli':
                output[opcode[3]] = input[opcode[1]] * opcode[2]

        elif opcodes[opcode[0]] == 'banr':
                output[opcode[3]] = input[opcode[1]] & input[opcode[2]]
        elif opcodes[opcode[0]] == 'bani':
                output[opcode[3]] = input[opcode[1]] & opcode[2]

        elif opcodes[opcode[0]] == 'borr':
                output[opcode[3]] = input[opcode[1]] | input[opcode[2]]
        elif opcodes[opcode[0]] == 'bori':
                output[opcode[3]] = input[opcode[1]] | opcode[2]

        elif opcodes[opcode[0]] == 'setr':
                output[opcode[3]] = input[opcode[1]]
        elif opcodes[opcode[0]] == 'seti':
                output[opcode[3]] = deepcopy(opcode[1])

        elif opcodes[opcode[0]] == 'gtir':
                output[opcode[3]] = 0
                if opcode[1] > input[opcode[2]]:
                        output[opcode[3]] = 1
        elif opcodes[opcode[0]] == 'gtri':
                output[opcode[3]] = 0
                if input[opcode[1]] > opcode[2]:
                        output[opcode[3]] = 1
        elif opcodes[opcode[0]] == 'gtrr':
                output[opcode[3]] = 0
                if input[opcode[1]] > input[opcode[2]]:
                        output[opcode[3]] = 1
                
        elif opcodes[opcode[0]] == 'eqir':
                output[opcode[3]] = 0
                if opcode[1] == input[opcode[2]]:
                        output[opcode[3]] = 1
        elif opcodes[opcode[0]] == 'eqri':
                output[opcode[3]] = 0
                if input[opcode[1]] == opcode[2]:
                        output[opcode[3]] = 1
        elif opcodes[opcode[0]] == 'eqrr':
                output[opcode[3]] = 0
                if input[opcode[1]] == input[opcode[2]]:
                        output[opcode[3]] = 1

        return output

#{5: 'eqir', 13: 'gtrr', 8: 'gtri', 9: 'eqri', 4: 'eqrr', 10: 'gtir', 15: 'banr', 1: 'bani', 3: 'seti', 6: 'setr', 11: 'borr', 12: 'addr', 14: 'mulr', 0: 'muli', 2: 'addi', 7: 'bori'}

registers = [0, 0, 0, 0]
for line in inputFileTest:
        registersText = line.replace('\n', '')
        opcode = [int(s) for s in registersText.split(' ') if s.isdigit()]
        old = deepcopy(registers)
        registers = doOperation(opcodes, opcode, registers)
        print('{} -> {} -> {}'.format(old, opcode, registers))


print(registers)

