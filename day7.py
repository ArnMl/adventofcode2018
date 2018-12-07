import os
import string


os.chdir("C:/Users/Arnaud/Documents/4-Autres/Advent/2018")
path = "input/day7"


def day7(path):
    DependsOn = {}
    with open(path) as f:
        for line in f:
            line = line.split()
            cond = line[1]
            depend = line[7]
            if cond not in DependsOn:
                DependsOn[cond] = set()
            if depend not in DependsOn:
                DependsOn[depend] = set()
            DependsOn[depend].add(cond)
    res = ""
    while 1:
        nextToDo = -1
        for key, item in DependsOn.items():
            if len(item) == 0:
                if nextToDo == -1:
                    nextToDo = key
                elif key < nextToDo:
                    nextToDo = key
        if nextToDo == -1:
            return res
        res += nextToDo
        DependsOn.pop(nextToDo)
        for key, item in DependsOn.items():
            if nextToDo in item:
                item.discard(nextToDo)

def day7t(path):
    DependsOn = {}
    with open(path) as f:
        for line in f:
            line = line.split()
            cond = line[1]
            depend = line[7]
            if cond not in DependsOn:
                DependsOn[cond] = set()
            if depend not in DependsOn:
                DependsOn[depend] = set()
            DependsOn[depend].add(cond)
    workers = [[0,0] for i in range(5)]
    res = ""
    tot = -1
    while 1:
        tot += 1
        done = []
        for indWorker in range(len(workers)):
            worker = workers[indWorker]
            worker[0] -= 1
            
            if worker[0] <= 0:
                done.append(indWorker)
                
                if worker[1] != 0:
                    for key, item in DependsOn.items():
                        if worker[1] in item:
                            item.discard(worker[1])
                    
        for finished in done:
            nextToDo = -1
            for key, item in DependsOn.items():
                if len(item) == 0:
                    if nextToDo == -1:
                        nextToDo = key
                    elif key < nextToDo:
                        nextToDo = key
            if nextToDo == -1:
                    workers[finished] = [0, 0]
            else:
                res += nextToDo
                DependsOn.pop(nextToDo)
                workers[finished]=[(ord(nextToDo) - (ord("A") - 1))+60, nextToDo]
        tousStop = True
        for elem in workers:
            if elem[1] != 0:
                tousStop = False
                break
        print(tot, workers)
        if tousStop:
            return tot
                
