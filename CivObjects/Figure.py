from CivEnums.EPermission import EPermission
from CivObjects.Position import Position
from Drawing.DrawCivObjects import DrawCivObjects
from Drawing import ImageHandler


"""
with it all properties of each figure - army and pioneer - can be defined
* figure type, name and sign
* color
* civilization
* position
* ability for founding city
* permission for each terrain
* pointer to image
"""


class Figure:

    def __init__(self, ftype, civ, col):
        self.fType = ftype
        self.color = col
        self.civilization = civ
        self.position = None
        self.foundingCity = False
        self.permissionTerrain = EPermission.ALL_EXCEPT_WATER
        self.img = ImageHandler.getImageOfFigure(self.fType, self.color)

    def draw(self, window, rotation, pos, resize):
        DrawCivObjects.drawImage(self.img, window, rotation, pos, resize, 1)

    def isPotentialCandidateForFoundingCity(self):
        return self.foundingCity

    def setPotentialCandidateForFoundingCity(self, possible):
        self.foundingCity = possible

    def setPermissionMoveOverWater(self):
        self.permissionTerrain = EPermission.MOVE_OVER_WATER

    def setPermissionStopOnWater(self):
        self.permissionTerrain = EPermission.STOP_ON_WATER

    def getPermissionTerrain(self):
        return self.permissionTerrain

    def getType(self):
        return self.fType

    def getCivilization(self):
        return self.civilization

    def setPosition(self, x, y):
        if self.position is None:
            self.position = Position(x, y)
        else:
            self.position.setPosition(x, y)

    def getPosition(self):
        return self.position
