inp = '''670A
974A
638A
319A
508A'''

'''
7 8 9
4 5 6
1 2 3
X 0 A

  ^ A
< v >  

  ^ A
< v >  

  ^ A
< v >  
'''

'''
L = inp.split("\n")

DirectionPad = {"^": (1, 0), "A": (2, 0), "<": (0, 1), "v": (1, 1), ">": (2, 1)}
DirectionCoords = {(1, 0): "^", (2, 0): "A", (0, 1): "<", (1, 1): "v", (2, 1): ">"}

NumberPad = {}
NumberCoords = {}
thing = "789456123X0A"
for i in range(len(thing)):
    x = i % 3
    y = i // 3
    coord = (x, y)
    if thing[i] == "X":
        continue
    NumberCoords[coord] = thing[i]
    NumberPad[thing[i]] = coord

def addTups(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def sign(num):
    if num == 0:
        return 0
    return int(num / abs(num))

def isValidOption(option, currentCoord, Coords):
    current = currentCoord
    for dir in option:
        current = addTups(current, dir)
        if current not in Coords:
            return False
    return True

def decompose(t1, t2, currentCoord, Coords):
    x = t2[0] - t1[0]
    y = t2[1] - t1[1]
    
    xSign = sign(x)
    ySign = sign(y)

    firstOption = abs(x) * [(xSign, 0)] + abs(y) * [(0, ySign)]
    secondOption = abs(y) * [(0, ySign)] + abs(x) * [(xSign, 0)]

    if not isValidOption(firstOption, currentCoord, Coords):
        firstOption = secondOption
    elif not isValidOption(secondOption, currentCoord, Coords):
        secondOption = firstOption

    if firstOption == secondOption:
        return [firstOption]
    return [firstOption, secondOption]



def getShortestCode(code, CurrentCoords, index):
    if index == -1:
        #print(code)
        return len(code)
    if index == 2:
        Pad = NumberPad
        Coords = NumberCoords
    else:
        Pad = DirectionPad
        Coords = DirectionCoords
    answer = 0
    for button in code:
        Options = decompose(CurrentCoords[index], Pad[button], CurrentCoords[index], Coords)
        CurrentCoords[index] = Pad[button]

        shortest = 10 ** 20
        for option in Options:     
            nextCode = ""
            for coord in option:
                nextCode += Directions[coord]
            nextCode += "A"
            
            shortest = min(shortest, getShortestCode(nextCode, CurrentCoords.copy(), index - 1))
        answer += shortest
    return answer


Around = {">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1)}
Directions = {(1, 0): ">", (0, 1): "v", (-1, 0): "<", (0, -1): "^"}

CurrentCoords = [(2, 0), (2, 0), (2, 3)] # robot1, robot2, robot3

answer = 0

for line in L:
    shortest = getShortestCode(line, CurrentCoords, 2)
    num = int(line[:-1])
    answer += shortest * num
print(answer)
'''

L = inp.split("\n")

DirectionPad = {"^": (1, 0), "A": (2, 0), "<": (0, 1), "v": (1, 1), ">": (2, 1)}
DirectionCoords = {(1, 0): "^", (2, 0): "A", (0, 1): "<", (1, 1): "v", (2, 1): ">"}

NumberPad = {}
NumberCoords = {}
thing = "789456123X0A"
for i in range(len(thing)):
    x = i % 3
    y = i // 3
    coord = (x, y)
    if thing[i] == "X":
        continue
    NumberCoords[coord] = thing[i]
    NumberPad[thing[i]] = coord

def addTups(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def sign(num):
    if num == 0:
        return 0
    return int(num / abs(num))

def isValidOption(option, currentCoord, Coords):
    current = currentCoord
    for dir in option:
        current = addTups(current, dir)
        if current not in Coords:
            return False
    return True

def decompose(t1, t2, currentCoord, Coords):
    x = t2[0] - t1[0]
    y = t2[1] - t1[1]
    
    xSign = sign(x)
    ySign = sign(y)

    firstOption = abs(x) * [(xSign, 0)] + abs(y) * [(0, ySign)]
    secondOption = abs(y) * [(0, ySign)] + abs(x) * [(xSign, 0)]

    if not isValidOption(firstOption, currentCoord, Coords):
        firstOption = secondOption
    elif not isValidOption(secondOption, currentCoord, Coords):
        secondOption = firstOption

    if firstOption == secondOption:
        return [firstOption]
    return [firstOption, secondOption]


dirRobotCount = 25
D = {}
def getShortestCode(code, CurrentCoords, index):
    if (code, index) in D:
        return D[(code, index)]
    if index == -1:
        #print(code)
        return len(code)
    if index == dirRobotCount:
        Pad = NumberPad
        Coords = NumberCoords
    else:
        Pad = DirectionPad
        Coords = DirectionCoords
    answer = 0
    for button in code:
        Options = decompose(CurrentCoords[index], Pad[button], CurrentCoords[index], Coords)
        CurrentCoords[index] = Pad[button]

        shortest = 10 ** 20
        for option in Options:     
            nextCode = ""
            for coord in option:
                nextCode += Directions[coord]
            nextCode += "A"
            
            shortest = min(shortest, getShortestCode(nextCode, CurrentCoords.copy(), index - 1))
        answer += shortest
    D[(code, index)] = answer
    return answer


Around = {">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1)}
Directions = {(1, 0): ">", (0, 1): "v", (-1, 0): "<", (0, -1): "^"}

CurrentCoords = [] # robot1, robot2, robot3, ...
for x in range(dirRobotCount):
    CurrentCoords.append((2, 0))
CurrentCoords.append((2, 3))
answer = 0

for line in L:
    shortest = getShortestCode(line, CurrentCoords, dirRobotCount)
    num = int(line[:-1])
    answer += shortest * num
print(answer)