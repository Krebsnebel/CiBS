from CivObjects.Position import Position


class Option:

    def __init__(self, imgObj, x, y, oStatus, oType, emphasize, mapPos):
        self.position = Position(x, y)
        self.imgObj = imgObj
        self.width = imgObj.getSizeX()
        self.height = imgObj.getSizeY()
        self.emphasize = emphasize
        self.oStatus = oStatus
        self.oType = oType
        self.mapPos = mapPos

    def getEmphasize(self):
        return self.emphasize

    def getPosition(self):
        return self.position

    def getRect(self, scale):
        return self.width * scale, self.height * scale

    def getX(self):
        return self.position.getX()

    def getY(self):
        return self.position.getY()

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getImgObj(self):
        return self.imgObj

    def getPositionOfMap(self):
        return self.mapPos

    def getOptionType(self):
        return self.oType

    def getOptionStatus(self):
        return self.oType
