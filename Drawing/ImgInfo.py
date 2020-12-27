import pygame

from CivEnums.ERefPoint import ERefPoint
from CivObjects.Position import Position


"""
this class is a basis class for other ImgInfo classes
In this class all important properties for image sections are set
* shift x, shift y and scale
* width and height
* reference point and its position
* derivatives from its reference points
** top left
** top right
** bottom left
** bottom right
Furthermore common functions are implemented
* functions for set and clear possibilities
* set functions for each corner
* get position of each corner with or without shift
* get scale of image section
* get mouse position relative to image section
* get shift x and y
"""


class ImgInfo:

    def __init__(self, width, height, refPos, refPoint):
        self.emphasize = True
        self.mousePosition = None
        self.leftMouseButtonPressed = False
        self.shiftX = 0
        self.shiftY = 0
        self.scale = 1
        self.width = width
        self.height = height
        self.refPoint = refPoint
        self.refPos = refPos
        self.posTopLeft = self.setTopLeft()
        self.posBottomRight = self.setBottomRight()
        self.posTopRight = self.setTopRight()
        self.posBottomLeft = self.setBottomLeft()

        self.options = []
        self.mouseAtPossiblePosition = None

    def draw(self, window):
        scale = self.getScale()
        if self.options is not None:
            for opt in self.options:
                if opt.getEmphasize():
                    size = opt.getRect(scale)
                    possible_img = pygame.Surface(size, pygame.SRCALPHA)
                    pygame.draw.rect(possible_img, (255, 0, 0), possible_img.get_rect(), 3)
                    window.blit(possible_img, ((opt.getX() + self.getShiftX()) * scale,
                                               (opt.getY() + self.getShiftY()) * scale))

        mpp = self.mouseAtPossiblePosition
        if mpp is not None and mpp.getEmphasize():
            size = mpp.getRect(scale)
            mouse_img = pygame.Surface(size, pygame.SRCALPHA)
            pygame.draw.rect(mouse_img, (255, 0, 0, 50), mouse_img.get_rect())
            window.blit(mouse_img, ((mpp.getX() + self.getShiftX()) * scale, (mpp.getY() + self.getShiftY()) * scale))

    def setMousePosition(self, x, y):
        self.mousePosition = Position(x, y)

    def getMousePosition(self, relative):
        if self.mousePosition is None:
            return None
        if relative:
            x = self.mousePosition.getX() - self.getPosOf(ERefPoint.TOP_LEFT, True, True).getX()
            y = self.mousePosition.getY() - self.getPosOf(ERefPoint.TOP_LEFT, True, True).getY()
        else:
            x = self.mousePosition.getX()
            y = self.mousePosition.getY()
        return Position(x, y)

    def setLeftMouseButtonPressed(self):
        self.leftMouseButtonPressed = True

    def isLeftMouseButtonPressed(self):
        return self.leftMouseButtonPressed

    def clearMouseButtons(self):
        self.leftMouseButtonPressed = False

    def clearOptions(self):
        self.options = []

    def getScale(self):
        return self.scale

    def getPosOf(self, refPoint, shift, scale):
        if refPoint == ERefPoint.TOP_LEFT:
            pos = self.posTopLeft
        elif refPoint == ERefPoint.BOTTOM_RIGHT:
            pos = self.posBottomRight
        elif refPoint == ERefPoint.TOP_RIGHT:
            pos = self.posTopRight
        elif refPoint == ERefPoint.BOTTOM_LEFT:
            pos = self.posBottomLeft
        else:   # REF_POS
            pos = self.refPos
        if shift:
            sx = self.shiftX
            sy = self.shiftY
        else:
            sx = 0
            sy = 0
        if scale:
            sc = self.getScale()
        else:
            sc = 1
        x = (pos.getX() + sx) * sc
        y = (pos.getY() + sy) * sc
        return Position(x, y)

    def getShiftX(self):
        return self.shiftX

    def getShiftY(self):
        return self.shiftY

    def setTopLeft(self):
        x = self.refPos.getX()
        y = self.refPos.getY()
        if self.refPoint == ERefPoint.TOP_RIGHT:
            x = x - self.width
        elif self.refPoint == ERefPoint.BOTTOM_LEFT:
            y = y - self.height
        elif self.refPoint == ERefPoint.BOTTOM_RIGHT:
            x = x - self.width
            y = y - self.height
        return Position(x, y)

    def setBottomRight(self):
        x = self.refPos.getX()
        y = self.refPos.getY()
        if self.refPoint == ERefPoint.TOP_RIGHT:
            y = y + self.height
        elif self.refPoint == ERefPoint.TOP_LEFT:
            x = x + self.width
            y = y + self.height
        elif self.refPoint == ERefPoint.BOTTOM_LEFT:
            x = x + self.width
        return Position(x, y)

    def setTopRight(self):
        return Position(self.posBottomRight.getX(), self.posTopLeft.getY())

    def setBottomLeft(self):
        return Position(self.posTopLeft.getX(), self.posBottomRight.getY())

    def getRefPoint(self):
        return self.refPoint
