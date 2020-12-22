import pygame

from CivEnums.EFigure import EFigure
from CivEnums.ERefPoint import ERefPoint
from CivObjects.Position import Position
from Drawing.EImageObject import EImageObject
from Drawing.ImgInfo import ImgInfo
from Options.EOptionType import EOptionType
from Options.Option import Option

"""
this class is an image information of each civilization
* draw possibilities and highlighting
* set mouse position, while mouse pressed and for highlighting
* mark areas for highlighting
* getter of image position of figures, research cards and other image objects
* getter of image rect
* getter of image resize
* get rotation of trading and gold disk
"""


class ImgInfoCivilization(ImgInfo):

    def __init__(self, i, numPlayer):

        self.selectPolity = False
        self.mouseHighlighting = None

        width = 1000
        height = 460
        if numPlayer == 2:
            if i == 0:
                refPoint = ERefPoint.TOP_RIGHT
                refPos = Position(700, 60)
            else:
                refPoint = ERefPoint.BOTTOM_LEFT
                refPos = Position(1180, 1020)
        elif numPlayer == 3:
            if i == 0:
                refPoint = ERefPoint.TOP_RIGHT
                refPos = Position(700, 60)
            elif i == 1:
                refPoint = ERefPoint.BOTTOM_RIGHT
                refPos = Position(460, 1020)
            else:
                refPoint = ERefPoint.BOTTOM_LEFT
                refPos = Position(1460, 1020)
        else:
            if i == 0:
                refPoint = ERefPoint.TOP_RIGHT
                refPos = Position(460, 60)
            elif i == 1:
                refPoint = ERefPoint.TOP_LEFT
                refPos = Position(1460, 60)
            elif i == 2:
                refPoint = ERefPoint.BOTTOM_RIGHT
                refPos = Position(460, 1020)
            else:
                refPoint = ERefPoint.BOTTOM_LEFT
                refPos = Position(1460, 1020)
        super().__init__(width, height, refPos, refPoint)

    def setMousePosition(self, x, y):
        ImgInfo.setMousePosition(self, x, y)
        self.mouseAtPossiblePosition = None
        for opt in self.options:
            mousePos = self.getMousePosition(False)
            insideX = opt.getX() < (mousePos.getX() - self.getShiftX()) <= opt.getX() + opt.getWidth()
            insideY = opt.getY() < (mousePos.getY() - self.getShiftY()) <= opt.getY() + opt.getHeight()
            if insideX and insideY:
                self.mouseAtPossiblePosition = Option(opt.getX(), opt.getY(), opt.getWidth(), opt.getHeight(),
                                                      EOptionType.SQUARE)

    def setOptions(self, selectPolity):
        self.options = []
        if selectPolity:
            imgObj = EImageObject.POLITY
            imgPos = self.getImgPosOf(imgObj, False)
            self.options.append(Option(imgPos.getX(), imgPos.getY(), imgObj.getSizeX(), imgObj.getSizeY(),
                                       EOptionType.SQUARE))

    def setWidth(self, level, stackLength):
        pass

    def leftMouseButtonPressed(self, mousePosition):
        pass

    def getResize(self, imgObj):
        return imgObj.getResize() * self.scale

    def getImgPosOf(self, imgObj, shift):
        civDx = EImageObject.CIVILIZATION_SHEET.getX()
        civDy = EImageObject.CIVILIZATION_SHEET.getY()
        figDx = EImageObject.FIGURE.getX()
        figDy = EImageObject.FIGURE.getY()
        cityDx = EImageObject.CITY.getX()
        researchDelta = EImageObject.RESEARCH_CARDS.getX()
        if self.refPoint == ERefPoint.BOTTOM_RIGHT or self.refPoint == ERefPoint.TOP_RIGHT:
            refPos = self.getPosOf(ERefPoint.BOTTOM_RIGHT, shift)
            pos = Position(refPos.getX() - civDx, refPos.getY() - civDy)
            resPos = Position(refPos.getX() - civDx - researchDelta, refPos.getY())
            figPos = Position(refPos.getX() - figDx, refPos.getY() - figDy)
            cityPos = Position(refPos.getX() - cityDx, refPos.getY())
        else:
            refPos = self.getPosOf(ERefPoint.BOTTOM_LEFT, shift)
            pos = Position(refPos.getX(), refPos.getY() - civDy)
            resPos = Position(refPos.getX() + civDx + researchDelta, refPos.getY())
            figPos = Position(refPos.getX() + figDx, refPos.getY() - figDy)
            cityPos = Position(refPos.getX(), refPos.getY())
        if imgObj == EImageObject.CIVILIZATION_SHEET:
            return pos
        elif imgObj == EImageObject.TRADE_DISK:
            trDx = imgObj.getX()
            trDy = imgObj.getY()
            return Position(pos.getX() + trDx, pos.getY() + trDy)
        elif imgObj == EImageObject.GOLD_DISK:
            gdDx = imgObj.getX()
            gdDy = imgObj.getY()
            return Position(pos.getX() + gdDx, pos.getY() + gdDy)
        elif imgObj == EImageObject.POLITY:
            polDx = imgObj.getX()
            polDy = imgObj.getY()
            return Position(pos.getX() + polDx, pos.getY() + polDy)
        elif imgObj == EImageObject.CIVILIZATION_RESEARCH:
            return resPos
        elif imgObj == EImageObject.FIGURE:
            return figPos
        elif imgObj == EImageObject.KAPITOL or imgObj == EImageObject.CITY_1 or imgObj == EImageObject.CITY_2:
            cityDy = imgObj.getY()
            return Position(cityPos.getX(), cityPos.getY() - cityDy)
        return None

    def getImgPosOfFigure(self, figureType, nr, shift):
        refPos = self.getImgPosOf(EImageObject.FIGURE, shift)
        if figureType == EFigure.ARMY and 0 <= nr < 7:
            armyDeltaX = EImageObject.ARMY.getX()
            armyDeltaY = EImageObject.ARMY.getY()
            return Position(refPos.getX() + armyDeltaX[nr], refPos.getY() + armyDeltaY[nr])
        elif figureType == EFigure.PIONEER and 0 <= nr < 2:
            pioneerDeltaX = EImageObject.ARMY.getX()
            pioneerDeltaY = EImageObject.ARMY.getY()
            return Position(refPos.getX() + pioneerDeltaX[nr], refPos.getY() + pioneerDeltaY[nr])
        return None

    def getImgPosOfResearchCard(self, level, cardNr, shift):
        refPos = self.getImgPosOf(EImageObject.CIVILIZATION_RESEARCH, shift)
        researchDx = EImageObject.RESEARCH_CARDS.getSizeX()
        researchDy = EImageObject.RESEARCH_CARDS.getSizeY()
        researchDelta = EImageObject.RESEARCH_CARDS.getX()
        dx = int(cardNr * (researchDx + researchDelta) +
                 (level-1) * ((researchDx + researchDelta) / 2.0))
        if self.refPoint == ERefPoint.BOTTOM_RIGHT or self.refPoint == ERefPoint.TOP_RIGHT:
            dx = int(-dx - researchDx)
        dy = int(-researchDy - (level-1) * (researchDy + researchDelta))
        return Position(refPos.getX() + dx, refPos.getY() + dy)

    @classmethod
    def getRotationTradingPoints(cls, tradingPoints):
        return int(237 - 360.0 / 28.0 * tradingPoints)

    @classmethod
    def getRotationGoldPoints(cls, tradingPoints, goldPoints):
        return int(261 - 360.0 / 28.0 * tradingPoints - 360.0 / 16.0 * goldPoints)

    @classmethod
    def getRect(cls, imgObj):
        return int(imgObj.getSizeX()), int(imgObj.getSizeY())
