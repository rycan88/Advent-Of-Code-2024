inp = '''70949 6183 4 3825336 613971 0 15 182'''

'''
Current = inp.split(" ")
Next = []
for x in range(25):
    for string in Current:
        length = len(string)
        if (string == "0"):
            Next.append("1")
        elif (length % 2 == 0):
            Next.append(str(int(string[:int(length/2)])))
            Next.append(str(int(string[int(length/2):])))
        else:
            Next.append(str(int(string) * 2024))
    Current = Next[:]
    Next = []
print(len(Current)) 
''' 

from collections import defaultdict

L = inp.split(" ")

OldCount = defaultdict(int)
for string in L:
    OldCount[string] += 1

for x in range(75):
    Count = defaultdict(int)
    for string in OldCount:
        length = len(string)
        if (string == "0"):
            Count["1"] += OldCount[string] 
        elif (length % 2 == 0):
            Count[str(int(string[:int(length/2)]))] += OldCount[string]
            Count[str(int(string[int(length/2):]))] += OldCount[string] 
        else:
            Count[str(int(string) * 2024)] += OldCount[string] 

    OldCount = Count.copy()
 
print(sum(OldCount.values())) 