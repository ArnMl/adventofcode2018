import numpy as np

input = 7803

def day11(input = 7803):
    grid = np.zeros((300,300))
    for i in range(1,301):
        for j in range(1,301):
            grid[i-1][j-1] = calc(i, j, input)
    best = 0
    bestCoord = (0,0)
    for i in range(0,300):
        for j in range(0,300):
            zone = grid[i:i+3,j:j+3]
            loc = zone.sum()
            if loc > best:
                best = loc
                bestCoord = (i+1, j+1)
    return bestCoord


def day11t(input = 7803):
    grid = np.zeros((300,300))
    for i in range(1,301):
        for j in range(1,301):
            grid[i-1][j-1] = calc(i, j, input)
    best = 0
    bestCoord = (0,0,0)
    for size in range(1,301):
        for i in range(0,301-size):
            for j in range(0,301-size):
                zone = grid[i:i+size,j:j+size]
                loc = zone.sum()
                if loc > best:
                    best = loc
                    bestCoord = (i+1, j+1, size)
    return bestCoord

def calc(x, y, serial):
    id = 10+x
    res = id*y
    res += serial
    res = res * id
    res = int(str(res)[-3])
    return res-5
    