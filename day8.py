import os
import queue

os.chdir("C:/Users/Arnaud/Documents/4-Autres/Advent/2018")
path = "input/day8"


def day8(path = "input/day8"):
    with open(path) as f:
        content = f.read().split(" ")
        content = [int(i) for i in content]
    lifo = queue.LifoQueue()
    i = 2
    lifo.put([content[0],content[1]])
    tot = 0
    while True:
        current = lifo.get()
        if current[0] == 0: ## on a vu tous les fils de l'élément en cours
            for j in range(current[1]):
                tot += content[i+j]
            i = i + current[1]
        else:
            current[0] -= 1
            lifo.put(current)
            lifo.put([content[i],content[i+1]])
            i = i + 2
        if lifo.empty():
            return tot


def day8t(path = "input/day8"):
    with open(path) as f:
        content = f.read().split(" ")
        content = [int(i) for i in content]
    lifo = queue.LifoQueue()
    tree, _ = recCont(content, 0)
    return refCalc(tree)

def recCont(content, pos):
    nbrChild = content[pos]
    nbrMetaData = content[pos+1]
    pos += 2
    childs = [] 
    for i in range(nbrChild):
        child, pos = recCont(content, pos)
        childs.append(child)
    mds = []
    for i in range(nbrMetaData):
        mds.append(content[pos])
        pos += 1
    return ([childs, mds], pos)

def refCalc(elem):
    if len(elem[0]) == 0:
        return sum(elem[1])
    else:
        tot = 0
        for i in elem[1]:
            if i <= len(elem[0]):
                tot += refCalc(elem[0][i-1])
        return tot