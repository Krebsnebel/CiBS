import pygame

from CivEnums.ERefPoint import ERefPoint
from CivObjects.Position import Position
from Drawing.EImageObject import EImageObject
from Drawing.ImgInfo import ImgInfo
from Options.EOptionType import EOptionType
from Options.Option import Option

"""
this class is an image information of game map
* draw possibilities and highlighting
* set mouse position, while mouse pressed and for highlighting
* mark squares for highlighting
* check if putting object on square possible
* several functions for game map positions
* function to calculate image position for each square
* calculate square position depending of mouse position
"""


class ImgInfoGameMap(ImgInfo):

    def __init__(self, numPlayer):
        if numPlayer == 2:
            sx = 8
            sy = 16
            xPos = 720
            yPos = 60
        elif numPlayer == 3:
            sx = 16
            sy = 16
            xPos = 480
            yPos = 60
        else:
            sx = 16
            sy = 16
            xPos = 480
            yPos = 60
        sizeX = EImageObject.SQUARE_OBJECT.getSizeX()
        sizeY = EImageObject.SQUARE_OBJECT.getSizeY()
        super().__init__(int(sizeX * sx), int(sizeY * sy),
                         Position(xPos, yPos), ERefPoint.TOP_LEFT)

        self.optionsGameMap = None

        self.squareX = sx
        self.squareY = sy

    def setMousePosition(self, x, y):
        ImgInfo.setMousePosition(self, x, y)
        posGM = self.getMousePositionInGameMap()
        if self.optionsGameMap is not None and posGM is not None:
            if self.optionsGameMap[posGM.getX()][posGM.getY()]:
                imgObj = EImageObject.SQUARE
                size = imgObj.getSizeX()
                refPos = self.getPosOf(ERefPoint.TOP_LEFT, False, False)
                posX = refPos.getX() + posGM.getX() * size
                posY = refPos.getY() + posGM.getY() * size
                self.mouseAtPossiblePosition = Option(imgObj, posX, posY, EOptionType.SQUARE, self.emphasize, posGM)
            else:
                self.mouseAtPossiblePosition = None
        else:
            self.mouseAtPossiblePosition = None

    def getMousePositionInGameMap(self):
        size = EImageObject.MAP_TILE.getSizeX()
        mousePosRel = self.getMousePosition(True)
        if mousePosRel is None:
            return None
        x = int(mousePosRel.getX() // (size * self.getScale() / 4.0))
        y = int(mousePosRel.getY() // (size * self.getScale() / 4.0))
        if 0 <= x < 16 and 0 <= y < 16:
            return Position(x, y)
        else:
            return None

    def getValidGameMapPositionWhileMousePressed(self):
        if self.isLeftMouseButtonPressed():
            if self.mouseAtPossiblePosition is not None:
                return self.getMousePositionInGameMap()
        return None

    def setOptions(self, optionsGameMap):
        self.options = []
        if optionsGameMap is not None:
            imgObj = EImageObject.SQUARE
            size = imgObj.getSizeX()
            refPos = self.getPosOf(ERefPoint.TOP_LEFT, False, False)
            for y in range(16):
                for x in range(16):
                    if optionsGameMap[x][y]:
                        posX = refPos.getX() + x * size
                        posY = refPos.getY() + y * size
                        self.options.append(Option(imgObj, posX, posY, EOptionType.SQUARE,
                                                   self.emphasize, Position(x, y)))
        self.optionsGameMap = optionsGameMap

    @classmethod
    def getResizeSquareObj(cls):
        return EImageObject.SQUARE_OBJECT.getResize()

    @classmethod
    def getResizeMapTile(cls):
        return EImageObject.MAP_TILE.getResize()

    def getImgPosOfSquare(self, posGameMap, shift, scale):
        size = EImageObject.SQUARE_OBJECT.getSizeX()
        if scale:
            sc = self.getScale()
        else:
            sc = 1
        return Position(size * posGameMap.getX() * sc + self.getPosOf(ERefPoint.TOP_LEFT, shift, scale).getX(),
                        size * posGameMap.getY() * sc + self.getPosOf(ERefPoint.TOP_LEFT, shift, scale).getY())
