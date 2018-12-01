import os
os.chdir("C:/Users/Arnaud/Documents/4-Autres/Advent/2018")


def day1(path):
    file = open(path,"r")
    tot = 0
    for ligne in file:
        elem = int(ligne)
        tot += elem
    return tot
    
def day1t(path):
    file = open(path,"r")
    dump = file.readlines()
    res = set()
    tot = 0
    while 1:
        for ligne in dump:
            elem = int(ligne)
            tot += elem
            if tot in res:
                return tot
            else:
                res.add(tot)

print(day1("input/day1"))
print(day1t("input/day1"))