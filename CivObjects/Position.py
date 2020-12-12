class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def isEqual(self, point):
        if self.x == point.getX() and self.y == point.getY():
            return True
        return False
