from space import Empty, Food
import itertools


class Agent():
    # include traits like size, speed, sense, strength, hunger
    def __init__(self, pos, map):
        self.pos = pos
        self.map = map
        self.energy = 500
        self.sense = 3
        self.speed = 1
        self.senseType = "far"
        self.facing = "up"
        self.activeZone = []

    def move(self, movePos):
        # successful move
        if self.energy == 0:
            return
        newPos = (self.pos[0] + movePos[0], self.pos[1] + movePos[1])
        spaceData = self.map.checkSpace(newPos)
        self.facing = self.getDirection(newPos)
        if spaceData[0]:
            self.map.placeElement(self.getPos(), Empty())
            self.pos = newPos
            self.map.placeElement(self.getPos(), self)
            self.energy -= 1
        if isinstance(spaceData[1], Food):
            self.energy += spaceData[1].getValue()

    def moveToward(self, pos):
        moveList = ""
        moveList = "h" * abs(int(pos[0] - self.getPos()[0]))
        moveList += "v" * abs(int(pos[1] - self.getPos()[1]))
        perms = list(itertools.permutations(moveList))
        print(list(set(["".join(p) for p in perms])))

    def getPos(self):
        return self.pos

    def getEngery(self):
        return self.energy

    def getSense(self):
        return self.sense

    def getSenseType(self):
        return self.senseType

    def setSenseType(self, type):
        if type in ['wide', 'far']:
            self.senseType = type
        elif type == 'toggle':
            if self.senseType == 'wide':
                self.senseType = 'far'
            else:
                self.senseType = 'wide'

    def getFacing(self):
        return self.facing

    def getDistance(self, pos):
        return abs(self.getPos()[0] - pos[0]) + abs(self.getPos()[1] - pos[1])

    def getDirection(self, pos):
        if self.getPos()[0] - pos[0] > 0 and self.getPos()[1] == pos[1]:
            return "left"
        if self.getPos()[0] - pos[0] < 0 and self.getPos()[1] == pos[1]:
            return "right"
        if self.getPos()[1] - pos[1] > 0 and self.getPos()[0] == pos[0]:
            return "up"
        if self.getPos()[1] - pos[1] < 0 and self.getPos()[0] == pos[0]:
            return "down"

    def senseCheck(self, pos):
        if self.senseType == "wide":
            return (abs(self.getPos()[0] - pos[0]) + abs(self.getPos()[1] - pos[1])) <= self.getSense()
        if self.senseType == "far":
            yDiff = self.getPos()[1] - pos[1]
            xDiff = self.getPos()[0] - pos[0]
            if self.facing == "up":
                if yDiff > 0 and yDiff < self.sense * 2 - 1:
                    if abs(xDiff) <= yDiff:
                        return True
            elif self.facing == "down":
                if yDiff < 0 and abs(yDiff) < self.sense * 2 - 1:
                    if abs(xDiff) <= abs(yDiff):
                        return True
            elif self.facing == "right":
                if xDiff < 0 and abs(xDiff) < self.sense * 2 - 1:
                    if abs(yDiff) <= abs(xDiff):
                        return True
            elif self.facing == "left":
                if xDiff > 0 and xDiff < self.sense * 2 - 1:
                    if abs(yDiff) <= xDiff:
                        return True
            if yDiff == 0 and xDiff == 0:
                return True

            return False
