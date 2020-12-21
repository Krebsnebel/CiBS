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

        self.options = None
        self.mouseAtPossiblePosition = None

        self.squareX = sx
        self.squareY = sy

    def setMousePosition(self, x, y):
        ImgInfo.setMousePosition(self, x, y)
        posGM = self.getMousePositionInGameMap()
        if self.options is not None and posGM is not None:
            if self.options[posGM.getX()][posGM.getY()]:
                self.mouseAtPossiblePosition = posGM
                print(str(posGM.getX()) + " " + str(posGM.getY()))
            else:
                self.mouseAtPossiblePosition = None
        else:
            self.mouseAtPossiblePosition = None

    def getMousePositionInGameMap(self):
        size = EImageObject.MAP_TILE.getSizeX()
        mousePosRel = self.getMousePosition(True)
        if mousePosRel is None:
            return None
        x = int(mousePosRel.getX() // (size / 4.0))
        y = int(mousePosRel.getY() // (size / 4.0))
        if 0 <= x < 16 and 0 <= y < 16:
            return Position(x, y)
        else:
            return None

    def getMousePressedAtPossiblePosition(self):
        if self.isLeftMouseButtonPressed():
            return self.mouseAtPossiblePosition
        else:
            return None

    def setOptions(self, options):
        self.options = options

    def draw(self, window):
        if self.options is not None:
            length = int(self.getPixelOfSquare() * self.scale)
            size = (length, length)
            possible_img = pygame.Surface(size, pygame.SRCALPHA)
            pygame.draw.rect(possible_img, (255, 0, 0), possible_img.get_rect(), 3)

            mouse_img = pygame.Surface(size, pygame.SRCALPHA)
            pygame.draw.rect(mouse_img, (255, 0, 0, 50), mouse_img.get_rect())

            for y in range(16):
                for x in range(16):
                    if self.options[x][y]:
                        posGM = Position(x, y)
                        imgPos = self.getImgPosOfSquare(posGM)
                        window.blit(possible_img, (imgPos.getX(), imgPos.getY()))

            if self.mouseAtPossiblePosition is not None:
                imgPos = self.getImgPosOfSquare(self.mouseAtPossiblePosition)
                window.blit(mouse_img, (imgPos.getX(), imgPos.getY()))

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
