from CivObjects.Position import Position


class Option:

    def __init__(self, x, y, width, height, oType):
        self.position = Position(x, y)
        self.width = width
        self.height = height
        self.oType = oType

    def getPosition(self):
        return self.position

    def getRect(self):
        return self.width, self.height

    def getX(self):
        return self.position.getX()

    def getY(self):
        return self.position.getY()
