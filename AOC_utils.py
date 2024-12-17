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