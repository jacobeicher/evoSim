class Agent:
    # include traits like size, speed, sense, strength, hunger
    def __init__(self, pos, map):
        self.pos = pos
        self.map = map
        self.energy = 500
        self.sense = 3
        self.senseType = "far"
        self.facing = "up"

    def move(self, movePos):
        # successful move
        if self.energy == 0:
            return
        newPos = (self.pos[0] + movePos[0], self.pos[1] + movePos[1])
        spaceData = self.map.checkSpace(newPos)
        self.facing = self.getDirection(newPos)
        if spaceData[0]:
            self.map.placeElement(self.getPos(), 'e')
            self.pos = newPos
            self.map.placeElement(self.getPos(), 'a')
            self.energy -= 1
        if spaceData[1] == 'f':
            self.energy += 3

    def getPos(self):
        return self.pos

    def getEngery(self):
        return self.energy

    def getSense(self):
        return self.sense

    def getSenseType(self):
        return self.senseType

    def senseCheck(self, pos):
        if self.senseType == "wide":
            return ((self.getPos()[0] - (pos[0]))**2 + (self.getPos()[1] - (pos[1]))**2)**(1/2) <= self.getSense()
        if self.senseType == "far":
            yDiff = self.getPos()[1] - pos[1]
            xDiff = self.getPos()[0] - pos[0]
            if self.facing == "up":
                if yDiff > 0 and yDiff < self.sense * 2:
                    if abs(xDiff) <= yDiff:
                        return True
            elif self.facing == "down":
                if yDiff < 0 and abs(yDiff) < self.sense * 2:
                    if abs(xDiff) <= abs(yDiff):
                        return True
            elif self.facing == "right":
                if xDiff < 0 and abs(xDiff) < self.sense * 2:
                    if abs(yDiff) <= abs(xDiff):
                        return True
            elif self.facing == "left":
                if xDiff > 0 and xDiff < self.sense * 2:
                    if abs(yDiff) <= xDiff:
                        return True

            return False

    def getFacing(self):
        return self.facing

    def getDirection(self, pos):
        if self.getPos()[0] - pos[0] > 0 and self.getPos()[1] == pos[1]:
            return "left"
        if self.getPos()[0] - pos[0] < 0 and self.getPos()[1] == pos[1]:
            return "right"
        if self.getPos()[1] - pos[1] > 0 and self.getPos()[0] == pos[0]:
            return "up"
        if self.getPos()[1] - pos[1] < 0 and self.getPos()[0] == pos[0]:
            return "down"
