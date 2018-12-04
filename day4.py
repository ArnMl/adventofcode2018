import os

os.chdir("C:/Users/Arnaud/Documents/4-Autres/Advent/2018")
path = "input/day4"

def day4(path):
    with open(path) as f:
        rows = f.read().split("\n")
    rows.sort()
    print(rows)
    shifts = {}
    currentGuy = ""
    for elem in rows:
        if not elem:
            continue
        if "#" in elem:
            res = elem.split("#")[1].split(" ")[0]
            currentGuy = res
            newList = [0 for i in range(60)]
            if currentGuy not in shifts:
                shifts[currentGuy] = newList
        elif "asleep" in elem:
            sleepDepuis = int(elem[elem.index(":")+1:elem.index(":")+3])
        else:
            finSleep = int(elem[elem.index(":")+1:elem.index(":")+3])
            for i in range(sleepDepuis, finSleep):
                shifts[currentGuy][i] = shifts[currentGuy][i] + 1
    bestGuy = -1
    bestValue = -1
    for key, value in shifts.items():
        tot = sum(value)
        if (bestValue < tot):
            bestGuy = key
            bestValue = tot
    totalSh = shifts[bestGuy]
    print(shifts)
    print(totalSh)
    return(int(totalSh[totalSh.index(max(totalSh))]) * int(bestGuy))
        