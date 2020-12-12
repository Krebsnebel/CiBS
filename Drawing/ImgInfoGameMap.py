import pygame

from CivEnums.ERefPoint import ERefPoint
from CivObjects.Position import Position
from Drawing.EImageObject import EImageObject
from Drawing.HighlightObject import HighlightObject
from Drawing.ImgInfo import ImgInfo


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

        self.squareX = sx
        self.squareY = sy

        self.expectGMPosition = False
        self.gameMapPosition = None

    def setMousePositionForHighlighting(self, mousePosition):
        pos = self.calcGameMapPosition(mousePosition)
        x = pos.getX()
        y = pos.getY()
        for p in self.possibilities:
            if p.getPosition().getX() == x and p.getPosition().getY() == y:
                self.mouseHighlighting = HighlightObject(EImageObject.SQUARE_OBJECT, pos)
                return
        self.mouseHighlighting = None

    def draw(self, window):
        length = int(self.getPixelOfSquare() * self.scale)
        size = (length, length)
        possible_img = pygame.Surface(size, pygame.SRCALPHA)
        pygame.draw.rect(possible_img, (255, 0, 0), possible_img.get_rect(), 3)

        mouse_img = pygame.Surface(size, pygame.SRCALPHA)
        pygame.draw.rect(mouse_img, (255, 0, 0, 50), mouse_img.get_rect())

        for p in self.possibilities:
            posGM = p.getPosition()
            if posGM is not None:
                imgPos = self.getImgPosOfSquare(posGM)
                window.blit(possible_img, (imgPos.getX(), imgPos.getY()))

        if self.mouseHighlighting is not None:
            posGM = self.mouseHighlighting.getPosition()
            if posGM is not None:
                imgPos = self.getImgPosOfSquare(posGM)
                window.blit(mouse_img, (imgPos.getX(), imgPos.getY()))

    def markSquaresForHighlighting(self, squareList):
        self.possibilities = []
        for s in squareList:
            posGM = s.getPosition()
            self.possibilities.append(HighlightObject(EImageObject.SQUARE_OBJECT, posGM))

    def isPuttingObjectOnSquarePossible(self, poi):
        for p in self.possibilities:
            if p.getPosition().getX() == poi.getX() and p.getPosition().getY() == poi.getY():
                return True
        return False

    def markSquareForHighlighting(self, posGameMap):
        self.possibilities.append(HighlightObject(EImageObject.SQUARE_OBJECT, posGameMap))

    def expectGameMapPosition(self):
        self.expectGMPosition = True

    def gameMapPositionUsed(self):
        self.expectGMPosition = False

    def getGameMapPosition(self):
        pos = self.gameMapPosition
        self.gameMapPosition = None
        return pos

    def leftMouseButtonPressed(self, mousePosition):
        pos = self.calcGameMapPosition(mousePosition)
        x = pos.getX()
        y = pos.getY()
        if 0 <= x < self.squareX and 0 <= y < self.squareY:
            self.gameMapPosition = Position(x, y)
        else:
            self.gameMapPosition = None

    def getPixelOfSquare(self):
        sizeX = EImageObject.SQUARE_OBJECT.getSizeX()
        return int(sizeX * self.getScale())

    @classmethod
    def getResizeSquareObj(cls):
        return EImageObject.SQUARE_OBJECT.getResize()

    @classmethod
    def getResizeMapTile(cls):
        return EImageObject.MAP_TILE.getResize()

    def getImgPosOfSquare(self, posGameMap):
        size = EImageObject.SQUARE_OBJECT.getSizeX()
        pixSquareScale = size * self.scale
        return Position(int(pixSquareScale * posGameMap.getX() + self.getPosOf(ERefPoint.TOP_LEFT, True).getX()),
                        int(pixSquareScale * posGameMap.getY() + self.getPosOf(ERefPoint.TOP_LEFT, True).getY()))

    def calcGameMapPosition(self, mousePosition):
        size = EImageObject.MAP_TILE.getSizeX()
        mousePosRel = self.getMousePosition(mousePosition)
        x = int(mousePosRel.getX() // (size / 4.0))
        y = int(mousePosRel.getY() // (size / 4.0))
        return Position(x, y)
