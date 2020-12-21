from CivEnums.EPermission import EPermission
from CivObjects.Building import Building
from CivObjects.Position import Position
from CivObjects.Wonder import Wonder
from Drawing import ImageHandler
from Drawing.DrawCivObjects import DrawCivObjects

"""
this class handles the city and its outskirt
following functions are yet implemented
* getter for each object type in city (list of points) 
* setter and clearer for current and potential points in city
* functions for position and outskirt
* draw function
* several getters and setters
"""


class City:

    def __init__(self, cType, col, civ, imgObj):
        self.cType = cType
        self.color = col
        self.civilization = civ
        self.imgObj = imgObj
        self.position = None
        self.upgrade = False
        self.outskirts = []

        self.permissionTerrain = EPermission.ALL_EXCEPT_WATER
        self.img = ImageHandler.getImageOfCity(cType, col, self.upgrade)

    def getImgObj(self):
        return self.imgObj

    def getOutskirts(self):
        return self.outskirts

    def draw(self, window, rotation, pos, resize):
        DrawCivObjects.drawImage(self.img, window, rotation, pos, resize, 1)

    def getCivilization(self):
        return self.civilization

    def getType(self):
        return self.cType

    def getColor(self):
        return self.color

    def getPermissionTerrain(self):
        return self.permissionTerrain

    def upgradeCity(self):
        b = not self.upgrade
        self.upgrade = True
        return b

    def getSign(self):
        return self.cType.getSign(self.upgrade)

    def setPosition(self, x, y):
        self.position = Position(x, y)

    def getPosition(self):
        return self.position

    def setOutskirt(self, s):
        self.outskirts.append(s)

    def isOutskirt(self, x, y):
        for s in self.outskirts:
            p = s.getPosition()
            if p.getX() == x and p.getY() == y:
                return True
        return False

    def isWonderInOutskirt(self):
        for s in self.outskirts:
            if isinstance(s.getBusinessObject(), Wonder):
                return True
        return False

    def isUniqueBuildingThere(self):
        for s in self.outskirts:
            b = s.getBusinessObject()
            if isinstance(b, Building):
                if b.isLabeledUnique:
                    return True
        return False

    def countTradingPoints(self):
        tp = 0
        for s in self.outskirts:
            tp = tp + s.countTradingPoints(self.civilization)
        return tp
