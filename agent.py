class Agent:
    # include traits like size, speed, sense, strength, hunger
    def __init__(self, pos, map):
        self.pos = pos
        self.map = map
        self.energy = 5

    def move(self, movePos):
        # successful move
        newPos = (self.pos[0] + movePos[0], self.pos[1] + movePos[1])
        if self.map.checkSpace(newPos):
            self.map.placeElement(self.getPos(), 'e')
            self.pos = newPos
            self.map.placeElement(self.getPos(), 'a')

    def getPos(self):
        return self.pos
