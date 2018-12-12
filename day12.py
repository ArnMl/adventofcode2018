import os

os.chdir("C:/Users/Arnaud/Documents/4-Autres/Advent/2018")
path = "input/day12"


def day12(path = "input/day12"):
    patterns = []
    initial = []
    with open(path) as f:
        lines = f.readlines()
        firstLine = lines[0]
        if firstLine[-1] == "\n":
            firstLine = firstLine[:-1]
        firstLine.strip()
        initial = firstLine.split(": ")[1]
        initial = [1 if i == "#" else 0 for i in initial]
        
        for i in range(2,len(lines)):
            line = lines[i]
            
            if line[-1] == "\n":
                line = line[:-1]
            line = line.split(" => ")
            left = [1 if i == "#" else 0 for i in line[0]]
            right = 1 if line[1] == "#" else 0
            patterns.append((left,right))
    initial = [0]*80 + initial + [0]*80
    for ipen in range(20):
        nextList = [0 for a in range(len(initial))]
        for i in range(2,len(initial)-2):
            loc = initial[i-2:i+3]
            if sum(loc) ==0:
                continue
            for elem in patterns:
                if elem[0] == loc:
                    nextList[i] = elem[1]
                    break
        initial = nextList
    tot = 0
    for i in range(len(initial)):
        if initial[i] == 1:
            tot += (i-80)
    return tot

def day12t(path = "input/day12"):
    patterns = []
    initial = []
    with open(path) as f:
        lines = f.readlines()
        firstLine = lines[0]
        if firstLine[-1] == "\n":
            firstLine = firstLine[:-1]
        firstLine.strip()
        initial = firstLine.split(": ")[1]
        initial = [1 if i == "#" else 0 for i in initial]
        
        for i in range(2,len(lines)):
            line = lines[i]
            
            if line[-1] == "\n":
                line = line[:-1]
            line = line.split(" => ")
            left = [1 if i == "#" else 0 for i in line[0]]
            right = 1 if line[1] == "#" else 0
            patterns.append((left,right))
    initial = [0]* + initial + [0]*3
    leftOffset = 3
    for it in range(50000000000):
        nextList = [0 for a in range(len(initial))]
        for i in range(2,len(initial)-2):
            loc = initial[i-2:i+3]
            if sum(loc) ==0:
                continue
            for elem in patterns:
                if elem[0] == loc:
                    nextList[i] = elem[1]
                    break
        initial = nextList
        if (initial[0] == 1 or initial[1] == 1 or initial[2]==1):
            initial = [0]*3 + initial
            leftOffset +=3
        if (initial[-1]== 1 or initial[-2] == 1 or initial[-3] == 1):
            initial = initial + [0]*3
        if (it % 1000 == 0):
            print(it)
    tot = 0
    for i in range(len(initial)):
        if initial[i] == 1:
            tot += (i-leftOffset)
    return tot
