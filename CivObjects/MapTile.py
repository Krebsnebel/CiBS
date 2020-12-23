from CivEnums.ECivilization import ECivilization
from CivEnums.ERotation import ERotation
from CivEnums.EVisibility import EVisibility
from CivObjects.Position import Position
from Drawing import ImageHandler
from Drawing.DrawCivObjects import DrawCivObjects


"""
with it all squares of each map tile can be defined, additionally definition of
* rotation
* civilization, if home map tile
* visibility
* position
* label
* pointer to images
following functions are implemented
* draw function of map tile and its objects
* getter of civilization, visibility, position and square object
* set city and position
* print function
"""


class MapTile:

    def __init__(self, civ, lab, ImgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20, s21, s22, s23, s30, s31,
                 s32, s33):
        self.civilization = civ
        self.imgInfo = ImgInfoGameMap
        if civ == ECivilization.NONE:
            self.visibility = EVisibility.FOR_NOBODY
        else:
            self.visibility = EVisibility.FOR_ALL
        self.position = None
        self.rotation = ERotation.NO_ROTATION
        self.label = lab
        self.mapTile = []
        self.mapTile.append(s00)
        self.mapTile.append(s01)
        self.mapTile.append(s02)
        self.mapTile.append(s03)
        self.mapTile.append(s10)
        self.mapTile.append(s11)
        self.mapTile.append(s12)
        self.mapTile.append(s13)
        self.mapTile.append(s20)
        self.mapTile.append(s21)
        self.mapTile.append(s22)
        self.mapTile.append(s23)
        self.mapTile.append(s30)
        self.mapTile.append(s31)
        self.mapTile.append(s32)
        self.mapTile.append(s33)
        self.frontImg = ImageHandler.getImageOfMapTile(self.label, True)
        self.backImg = ImageHandler.getImageOfMapTile(self.label, False)

    def draw(self, window, scale):
        if self.visibility is EVisibility.FOR_ALL:
            img = self.frontImg
        else:
            img = self.backImg
        pos = self.imgInfo.getImgPosOfSquare(self.position, True, False)
        resize = self.imgInfo.getResizeMapTile()
        DrawCivObjects.drawImage(img, window, self.rotation, pos, resize, scale)
        for s in self.mapTile:
            s.drawObjectsOfSquare(window, self.imgInfo, scale)

    def getCivilization(self):
        return self.civilization

    def getVisibility(self):
        return self.visibility

    def getSquare(self, x, y):
        x = int(x)
        y = int(y)
        idx = self.getIndex(x, y)
        return self.mapTile[idx]

    def setCity(self, city, x, y):
        idx = self.getIndex(x, y)
        self.mapTile[idx].setCity(city)

    def setPosition(self, x, y, rot):
        if self.position is None:
            self.position = Position(x, y)
        else:
            self.position.setPosition(x, y)
        self.rotation = rot
        for i in range(4):
            for j in range(4):
                idx = self.getIndex(i, j)
                self.mapTile[idx].setPosition(x + i, y + j)

    def getPosition(self):
        return self.position

    def getIndex(self, x, y):
        if self.rotation == ERotation.NO_ROTATION:
            return 4 * y + x
        elif self.rotation == ERotation.CLOCKWISE_90:
            return 4 * (3 - x) + y
        elif self.rotation == ERotation.CLOCKWISE_180:
            return 4 * (3 - y) + 3 - x
        else:  # ERotation.CLOCKWISE_270
            return 4 * x + 3 - y
