import os

os.chdir("C:/Users/Arnaud/Documents/4-Autres/Advent/2018")
path = "input/day9"

class Link:
    def __init__(self, data, nextCW, nextCC):
        self.value = data
        self.nextCC = nextCC
        self.nextCW = nextCW

class CircularLinkedList:
    def __init__(self, value):
        self.head = Link(None, None, None) # this is the sentinel node!
        self.head.value = 0
        self.head.nextCW = self.head   # link it to itself
        self.head.nextCC = self.head

    def add(self, data):             # no special case code needed for an empty list
        newLink = Link(data, self.head.nextCW, self.head)
        self.head.nextCW.nextCC = newLink
        self.head.nextCW = newLink
        
    
    def remove(self):
        self.head.nextCW.nextCC = self.head.nextCC
        self.head.nextCC.nextCW = self.head.nextCW
        self.head = self.head.nextCW
    
    def advance(self, dist):
        for i in range(dist):
            self.head = self.head.nextCW
        return self
    
    def back(self, dist):
        for i in range(dist):
            self.head = self.head.nextCC
        return self
    
        
    def __contains__(self, value):    # example algorithm, implements the "in" operator
        current = self.head.next
        while current != self.head:
            if current.data == data: # element found
                return True
            current = current.nextCW
        return False

def day9(path = "input/day9"):
    with open(path) as f:
        cont = f.read().split(" ")
        nbrPlayer = int(cont[0])
        lastMarble = int(cont[6])
    scores = [0 for i in range(nbrPlayer)]
    circle = CircularLinkedList(0)
    currentPlayer = 0
    for marble in range(1,lastMarble +1):
        if marble % 23 == 0:
            scores[currentPlayer] += marble
            circle.back(7)
            scores[currentPlayer] += circle.head.value
            circle.remove()
        else:
            circle.advance(1)
            circle.add(marble)
            circle.advance(1)
        currentPlayer = (currentPlayer + 1) % nbrPlayer
    return(max(scores))