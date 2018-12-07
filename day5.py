import os
import string

os.chdir("C:/Users/Arnaud/Documents/4-Autres/Advent/2018")
path = "input/day5"

def day5(path = "input/day5", chain = None):
    if chain is None:    
        with open(path) as f:
            chain = f.read()
    chain = list(chain)
    if (chain[-1] == "\n"):
        chain.pop()
    i = 1
    while True:
        if i<=0 :
            i = 1
            
        if compare(chain[i], chain[i-1]):
            del chain[i-1]
            del chain[i-1]
            i = i - 2
        else:
            i += 1
            
        if i >= len(chain):
            return len(chain)



def compare(a, b):
    if (a != b) and (a.upper() == b.upper()):
        return True
    else:
        return False
        

def day5t(path = "input/day5", chain = None):
    if chain is None:    
        with open(path) as f:
            chain = f.read()
    chain = list(chain)
    if (chain[-1] == "\n"):
        chain.pop()
    best = len(chain)
    listOfLetter = string.ascii_lowercase
    for letter in listOfLetter:
        locChain = [x for x in chain if (x!= letter and x!= letter.upper())]
        locLen = day5(chain = locChain)
        if (locLen < best):
            best = locLen
    return best