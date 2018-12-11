import os
import numpy as np
from parse import *

os.chdir("C:/Users/Arnaud/Documents/4-Autres/Advent/2018")
path = "input/day10"

def day10(path = "input/day10"):
    elems = []
    with open(path) as f:
        for line in f:
            if not line:
                pass
            line = line.strip()
            res = parse("position=<{}, {}> velocity=<{}, {}>", line)
            posX, posY, vX, vY = int(res[0]), int(res[1]), int(res[2]), int(res[3])
            elem = [posX, posY, vX, vY]
            elems.append(elem)
    best= 999999999999999
    bestI = 0
    for i in range(0,20001):
        minx = min(x + i * vx for (x, y, vx, vy) in elems)
        maxx = max(x + i * vx for (x, y, vx, vy) in elems)
        miny = min(y + i * vy for (x, y, vx, vy) in elems)
        maxy = max(y + i * vy for (x, y, vx, vy) in elems)
        if best > maxx - minx + maxy - miny:
            best = maxx - minx + maxy - miny
            bestI = i
      
    map = [[' '] * 200 for j in range(401)]
    i = bestI
    for (x, y, vx, vy) in elems:
        map[y + i * vy][x + i * vx - 250] = '*'
    for m in map:
        print(''.join(m))
    print(bestI)