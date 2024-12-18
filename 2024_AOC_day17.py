inp = '''Register A: 27334280
Register B: 0
Register C: 0

Program: 2,4,1,2,7,5,0,3,1,7,4,1,5,5,3,0'''

'''
# opcode then operand

A, B = inp.split("\n\n")

Registers = []
for line in A.split("\n"):
    colonIndex = line.index(":")
    Registers.append(int(line[colonIndex + 2:]))

colonIndex = B.index(":")
Program = list(map(int, B[colonIndex + 2:].split(",")))
Registers[0] = 100000000000001
currentIndex = 0
while currentIndex < len(Program) - 1:
    opcode = Program[currentIndex]
    literalOperand = Program[currentIndex + 1]
    comboOperand = literalOperand
    if 4 <= literalOperand <= 6:
        comboOperand = Registers[literalOperand - 4]
    if opcode == 0:
        Registers[0] = int(Registers[0] / (2 ** comboOperand))
    elif opcode == 1:
        Registers[1] = Registers[1] ^ literalOperand
    elif opcode == 2:
        Registers[1] = comboOperand % 8
    elif opcode == 3:
        if Registers[0] != 0:
            currentIndex = literalOperand
            continue
    elif opcode == 4:
        Registers[1] = Registers[1] ^ Registers[2]
    elif opcode == 5:
        print(comboOperand % 8,end=",")
    elif opcode == 6:
        Registers[1] = int(Registers[0] / (2 ** comboOperand))
    elif opcode == 7:
        Registers[2] = int(Registers[0] / (2 ** comboOperand))
    currentIndex += 2
'''

A, B = inp.split("\n\n")

Registers = []
for line in A.split("\n"):
    colonIndex = line.index(":")
    Registers.append(int(line[colonIndex + 2:]))

colonIndex = B.index(":")
Program = list(map(int, B[colonIndex + 2:].split(",")))

def getOctList(num):
    Lst = []
    while num > 0:
        Lst.append(num%8)
        num = num // 8
    return Lst

def octToNum(Vals):
    startValue = 0
    for x in range(len(Vals)):
        startValue += Vals[x] * (8 ** x)
    return startValue

def getFirstNum(aValue):
    Registers = [aValue, 0, 0]
    currentIndex = 0

    while currentIndex < len(Program) - 1:
        opcode = Program[currentIndex]
        literalOperand = Program[currentIndex + 1]
        comboOperand = literalOperand
        if 4 <= literalOperand <= 6:
            comboOperand = Registers[literalOperand - 4]

        if opcode == 0:
            Registers[0] = int(Registers[0] / (2 ** comboOperand))
        elif opcode == 1:
            Registers[1] = Registers[1] ^ literalOperand
        elif opcode == 2:
            Registers[1] = comboOperand % 8
        elif opcode == 3:
            if Registers[0] != 0:
                currentIndex = literalOperand
                continue
        elif opcode == 4:
            Registers[1] = Registers[1] ^ Registers[2]
        elif opcode == 5:
            return comboOperand % 8
        elif opcode == 6:
            Registers[1] = int(Registers[0] / (2 ** comboOperand))
        elif opcode == 7:
            Registers[2] = int(Registers[0] / (2 ** comboOperand))
        currentIndex += 2

def recursion(Vals, index, Answers):
    if index < 0:
        answer = octToNum(Vals)
        Answers.append(answer)
        return
    goal = Program[index]
    for x in range(8):
        newVals = [x] + Vals
        num = octToNum(newVals)
        firstNum = getFirstNum(num)
        if firstNum == goal:
            recursion(newVals, index - 1, Answers)

Vals = []
Answers = []
recursion(Vals, len(Program) - 1, Answers)
print(min(Answers))

