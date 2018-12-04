import os
os.chdir("C:/Users/Arnaud/Documents/4-Autres/Advent/2018")
path = "input/day2"

def day1(path):
    file = open(path, "r")
    compte2 = 0
    compte3 = 0
    for line in file:
        locDict = {}
        for elem in line:
            locDict[elem] =  locDict.get(elem, 0) + 1
        vue3 = False
        vue2 = False
        for key, value in locDict.items():
            if value == 3 and not vue3:
                vue3 = True
                compte3 += 1
            if value == 2 and not vue2:
                vue2 = True
                compte2 += 1
    print(compte2 * compte3)
    return(compte2 * compte3)
    

def day2(path):
    with open(path,"r") as file:
        rows = file.readlines()
    for posF in range(len(rows)):
        for posS in range(posF+1, len(rows)):
            mot1 = rows[posF][:-1] #To remove the /n
            mot2 = rows[posS][:-1]
            posDif = -1
            for posLettre in range(len(mot1)):
                if (mot1[posLettre] != mot2[posLettre]):
                    if posDif == -1:
                        posDif = posLettre
                    else:
                        posDif = -1
                        break
            if posDif!=-1:
                return (mot1[:posDif] + mot1[posDif+1:])