from sortedcontainers import SortedList
from collections import defaultdict

Around = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def getAroundList():
    Around = [(0, 1), (1, 0), (1, 1), (-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1)]
    return Around

def addTups(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def printBoard(Board, width, height):
    for y in range(height):
        for x in range(width):
            print(Board[(x, y)], end="")
        print("\n")


def mapSolver():
    L = inp.split("\n")

    S = set()
    D = {}
    turn = 0
    for line in L:
        turn += 1
        x, y = map(int, line.split(","))
        coord = (x, y)
        S.add(coord)
        if turn >= 1024:
            break

    Around = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    def addTups(t1, t2):
        return (t1[0] + t2[0], t1[1] + t2[1])

    start = (0, 0)
    end = (70, 70)

    Current = [start]
    steps = 0
    D[start] = 0
    Found = set([start])
    while len(Current) > 0:
        steps += 1
        Next = []
        for current in Current:
            for around in Around:
                newTup = addTups(current, around)

                if newTup in S:
                    continue
                if newTup not in Found and 0 <= newTup[0] <= 70 and 0 <= newTup[1] <= 70:
                    Found.add(newTup)

                    Next.append(newTup)

                    if newTup == end:
                        print(steps)
                        break
        Current = Next