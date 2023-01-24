
class Food():
    def __init__(self, val):
        self.value = val
        self.radius = val * 2

    def getValue(self):
        return self.value

    def getRadius(self):
        return self.radius


class Empty():
    def __init__(self):
        self.contents = 'e'
