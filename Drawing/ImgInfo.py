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

        self.possibilities = []
        self.mouseHighlighting = None
        self.possibilitiesMarked = False

    def setMousePosition(self, x, y):
        self.mousePosition = Position(x, y)

    def getMousePosition(self, relative):
        if self.mousePosition is None:
            return None
        if relative:
            x = self.mousePosition.getX() - self.getPosOf(ERefPoint.TOP_LEFT, True).getX()
            y = self.mousePosition.getY() - self.getPosOf(ERefPoint.TOP_LEFT, True).getY()
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

    def getScale(self):
        return self.scale

    def getPosOf(self, refPoint, shift):
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
        if not shift:
            return pos
        x = pos.getX() + self.shiftX
        y = pos.getY() + self.shiftY
        return Position(x, y)

    def getShiftX(self):
        return self.shiftX

    def getShiftY(self):
        return self.shiftY

    def setTopLeft(self):
        refPos = self.getPosOf(ERefPoint.REF_POS, False)
        x = refPos.getX()
        y = refPos.getY()
        if self.refPoint == ERefPoint.TOP_RIGHT:
            x = x - self.width
            y = y
        elif self.refPoint == ERefPoint.TOP_LEFT:
            x = x
            y = y
        elif self.refPoint == ERefPoint.BOTTOM_RIGHT:
            x = x - self.width
            y = y - self.height
        else:  # BOTTOM_LEFT
            x = x
            y = y - self.height
        return Position(int(x), int(y))

    def setBottomRight(self):
        if self.refPoint == ERefPoint.TOP_RIGHT:
            x = self.refPos.getX()
            y = self.refPos.getY() + self.height
        elif self.refPoint == ERefPoint.TOP_LEFT:
            x = self.refPos.getX() + self.width
            y = self.refPos.getY() + self.height
        elif self.refPoint == ERefPoint.BOTTOM_RIGHT:
            x = self.refPos.getX()
            y = self.refPos.getY()
        else:  # BOTTOM_LEFT
            x = self.refPos.getX() + self.width
            y = self.refPos.getY()
        return Position(int(x), int(y))

    def setTopRight(self):
        return Position(self.posBottomRight.getX(), self.posTopLeft.getY())

    def setBottomLeft(self):
        return Position(self.posTopLeft.getX(), self.posBottomRight.getY())

    def getRefPoint(self):
        return self.refPoint
