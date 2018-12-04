import os
import numpy as np

os.chdir("C:/Users/Arnaud/Documents/4-Autres/Advent/2018")
path = "input/day3"

def day3(path):
    with open(path) as f:
        rows = f.read().split("\n")
    fabric = np.zeros((1000,1000))
    for claim in rows:
        if not claim:
            continue
        claim = claim.split("@")[1]
        claim = claim.split(":")
        
        pos = claim[0]
        pos = pos.split(",")
        leftOffset = int(pos[0])
        topOffset = int(pos[1])
        
        size = claim[1].split("x")
        leftSize = int(size[0])
        topSize = int(size[1])
        
        fabric[leftOffset:leftOffset+leftSize,topOffset:topOffset+topSize] += 1
    print(len(fabric[ np.where( fabric> 1 ) ]))
    print(fabric.sum())

def day3t(path):
    with open(path) as f:
        rows = f.read().split("\n")
    fabric = np.zeros((1000,1000))
    for claim in rows:
        if not claim:
            continue
        claim = claim.split("@")[1]
        claim = claim.split(":")
        
        pos = claim[0]
        pos = pos.split(",")
        leftOffset = int(pos[0])
        topOffset = int(pos[1])
        
        size = claim[1].split("x")
        leftSize = int(size[0])
        topSize = int(size[1])
        
        fabric[leftOffset:leftOffset+leftSize,topOffset:topOffset+topSize] += 1
    
    for claim in rows:
        if not claim:
            continue
        claim = claim.split("@")
        id = claim[0]
        claim = claim[1]
        claim = claim.split(":")
        
        pos = claim[0]
        pos = pos.split(",")
        leftOffset = int(pos[0])
        topOffset = int(pos[1])
        
        size = claim[1].split("x")
        leftSize = int(size[0])
        topSize = int(size[1])
        if fabric[leftOffset:leftOffset+leftSize,topOffset:topOffset+topSize].sum() == (topSize * leftSize):
            return id