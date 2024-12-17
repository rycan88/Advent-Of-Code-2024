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
import sys
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

#Vals = [7,0,1, 0, 2,2,3, 5]

# [6, 4, 4, 6, 5, 2, 3, 5]

# [(4),6, 5, 2,3,5]
# [(6),6, 5, 2,3,5]
# [(6),6, 5, 2,3,5]
Vals = [0,1,0,2,2,3,5]

#2,4,1,2,7,5,0,3,1,7,4,1,5,5,3,0
Vals = [7,6,6,5, 2, 3, 5]

startValue = 0
for x in range(len(Vals)):
    startValue += Vals[x] * (8 ** x)
print(startValue) #11361574
print(getOctList(11361574))
#startValue = 149754979999990 #203554107309583 
aValue = startValue

Thing = [1,7,4,1,5,5,3,0] 
testing = False
while True:
    if aValue == startValue - 8:
        break
    Answer = []
    Registers = [aValue, 0, 0]
    currentIndex = 0
    answerIndex = 0
    if aValue % 1000000 == 0:
        print(aValue)
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
            val = comboOperand % 8
            
            if testing:
                if (answerIndex >= len(Thing) or Thing[answerIndex] != val):
                    if answerIndex >= len(Thing):
                        sys.quit()
                    break
             
            
            Answer.append(val)
            answerIndex += 1
            print(comboOperand % 8,end=",")
        elif opcode == 6:
            Registers[1] = int(Registers[0] / (2 ** comboOperand))
        elif opcode == 7:
            Registers[2] = int(Registers[0] / (2 ** comboOperand))
        currentIndex += 2
    
    '''
    if (Answer == Thing): #Program):
        print(aValue)
        break
    '''
    print("   :", bin(aValue))
    aValue -= 1


# 126000000,214000000, 308000000
#2,4,1,2,7,5,0,3,1,7,4,1,5,5,3,0
#7,1,4,7,3,2,5,6,4,3,1,4,2,2,6,5

#253397408990389
#203583007309583 HIGH