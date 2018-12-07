import os
import numpy as np

os.chdir("C:/Users/Arnaud/Documents/4-Autres/Advent/2018")
path = "input/day6"

def day6(path):
    listPoints = []
    leftMost = 0
    rightMost = 0
    topMost = 0
    bottomMost = 0
    with open(path) as file:
        for elem in file:
            if not elem:
                continue
            elem=elem.split(", ")
            elem = [int(elem[0]), int(elem[1])]
            listPoints.append(elem)
            
            if elem[0] > rightMost:
                rightMost = elem[0]
            
            if elem[0] < leftMost:
                leftMost = elem[0]
            
            if elem[1] > topMost:
                topMost = elem[1]
            
            if elem[1] < bottomMost:
                bottomMost = elem[1]
    infinite = set()
    size = [0 for i in range(len(listPoints))]
    arena = np.full((rightMost+1,topMost+1),-1)
    for i in range(leftMost, rightMost +1):
        for j in range(bottomMost, topMost +1):
            equal = set()
            dist = 1000000000
            for indElem in range(len(listPoints)):
                elem = listPoints[indElem]
                locDist = abs(i-elem[0])+abs(j - elem[1])
                if locDist < dist:
                    dist = locDist
                    equal = set()
                    equal.add(indElem)
                if locDist == dist:
                    equal.add(indElem)
            if len(equal)==1:
                plusProche = equal.pop()
                arena[i][j] = plusProche
                if (i == leftMost or i == rightMost or j == bottomMost or j == topMost):
                    infinite.add(plusProche)
                size[plusProche] = size[plusProche] + 1
    best = 0
    for index in range(len(size)):
        if index not in infinite:
            if size[index] > best:
                best = size[index]
    return best
            

def day6t(path):

    listPoints = []

    leftMost = 10000000

    rightMost = 0

    topMost = 0

    bottomMost = 10000000

    with open(path) as file:

        for elem in file:

            if not elem:

                continue

            elem = elem.split(", ")

            elem = [int(elem[0]), int(elem[1])]

            listPoints.append(elem)

            if elem[0]<leftMost:

                leftMost = elem[0]

            

            if elem[0]>rightMost:

                rightMost = elem[0]

            

            if elem[1]<bottomMost:

                bottomMost = elem[1]

            

            if elem[1]>topMost:

                topMost = elem[1]

    size = 0

    for i in range(leftMost -205, rightMost + 205):

        for j in range(bottomMost - 205, topMost + 205):

            locDist = 0

            for elem in listPoints:

                locDist += abs(elem[0] - i) + abs(elem[1] - j)

                if locDist >= 10000:

                    break

            if locDist < 10000:

                size += 1

    return size
            
                        