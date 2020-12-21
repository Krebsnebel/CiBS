from CivEnums.EProcess import EProcess
from CivEnums.ERefPoint import ERefPoint
from CivEnums.ERotation import ERotation
from CivObjects.Position import Position
from Drawing.EImageObject import EImageObject
from Drawing import ImageHandler
from Drawing.ImgInfoCivilization import ImgInfoCivilization
from Drawing.ImgInfoGameMap import ImgInfoGameMap
from Drawing.ImgInfo import ImgInfo
from Drawing.ImgInfoMarketMap import ImgInfoMarketMap
from Drawing.DrawCivObjects import DrawCivObjects


"""
this class is an image information of the whole game
in this class all image info objects are summarized
* imgInfoGameMap
* imgInfoMarketMap
* imgInfo of each civilization 
Furthermore functions are implemented
* top left and bottom right summarized over all image sections (with image frame)
* calculate shift x and y relative to current mouse position
* update shift x and y to to all imgInfo objects
* distribute mouse positions - while mouse pressed and for highlighting - to all imgInfo objects
* getters for all img info objects
"""


class ImgInfoGame(ImgInfo):

    def __init__(self, numPlayer):
        self.nextButton = True

        self.imgFramePix = 50
        self.imgInfoArray = []
        self.imgInfoCivilizations = []
        self.imgInfoGameMap = ImgInfoGameMap(numPlayer)
        self.imgInfoArray.append(self.imgInfoGameMap)
        self.imgInfoMarketMap = ImgInfoMarketMap()
        self.imgInfoArray.append(self.imgInfoMarketMap)

        for i in range(numPlayer):
            c = ImgInfoCivilization(i, numPlayer)
            self.imgInfoCivilizations.append(c)
            self.imgInfoArray.append(c)

        posTopLeft = self.setTopLeft()
        posBottomRight = self.setBottomRight()

        width = posBottomRight.getX() - posTopLeft.getX()
        height = posBottomRight.getY() - posTopLeft.getY()
        super().__init__(width, height, posTopLeft, ERefPoint.TOP_LEFT)

    def setLeftMouseButtonPressed(self):
        for imgInfo in self.imgInfoArray:
            imgInfo.setLeftMouseButtonPressed()

    def clearMouseButtons(self):
        for imgInfo in self.imgInfoArray:
            imgInfo.clearMouseButtons()

    def setTopLeft(self):
        topLefts = [self.imgInfoGameMap.getPosOf(ERefPoint.TOP_LEFT, False),
                    self.imgInfoMarketMap.getPosOf(ERefPoint.TOP_LEFT, False)]
        for c in self.imgInfoCivilizations:
            topLefts.append(c.getPosOf(ERefPoint.TOP_LEFT, False))

        tlp = Position(topLefts[0].getX(), topLefts[0].getY())
        for p in topLefts:
            if p.getX() < tlp.getX():
                tlp.setPosition(p.getX(), tlp.getY())
            if p.getY() < tlp.getY():
                tlp.setPosition(tlp.getX(), p.getY())

        return Position(int(tlp.getX() - self.imgFramePix), int(tlp.getY() - self.imgFramePix))

    def setBottomRight(self):
        bottomRights = [self.imgInfoGameMap.getPosOf(ERefPoint.BOTTOM_RIGHT, False),
                        self.imgInfoMarketMap.getPosOf(ERefPoint.BOTTOM_RIGHT, False)]
        for c in self.imgInfoCivilizations:
            bottomRights.append(c.getPosOf(ERefPoint.BOTTOM_RIGHT, False))

        brp = Position(bottomRights[0].getX(), bottomRights[0].getY())
        for p in bottomRights:
            if p.getX() > brp.getX():
                brp.setPosition(p.getX(), brp.getY())
            if p.getY() > brp.getY():
                brp.setPosition(brp.getX(), p.getY())
        return Position(int(brp.getX() + self.imgFramePix), int(brp.getY() + self.imgFramePix))

    def shift(self, window, mousePos):
        speed = 10

        if mousePos.getX() <= self.imgFramePix:
            self.shiftRight(window, speed)
        if mousePos.getX() >= window.get_width() - self.imgFramePix:
            self.shiftLeft(window, speed)
        if mousePos.getY() <= self.imgFramePix:
            self.shiftDown(window, speed)
        if mousePos.getY() >= window.get_height() - self.imgFramePix:
            self.shiftUp(window, speed)
        self.updateShiftsAndMousePosition(mousePos)

    def updateShiftsAndMousePosition(self, mousePos):
        for imgInfo in self.imgInfoArray:
            imgInfo.shiftX = self.shiftX
            imgInfo.shiftY = self.shiftY
            imgInfo.setMousePosition(mousePos.getX(), mousePos.getY())

    def shiftRight(self, window, dx):
        max_shift = -self.posTopLeft.getX()
        if self.shiftX + dx < max_shift:
            self.shiftX = self.shiftX + dx

    def shiftLeft(self, window, dx):
        max_shift = window.get_width() - self.posBottomRight.getX()
        if self.shiftX - dx > max_shift:
            self.shiftX = self.shiftX - dx

    def shiftDown(self, window, dy):
        max_shift = -self.posTopLeft.getY()
        if self.shiftY + dy < max_shift:
            self.shiftY = self.shiftY + dy

    def shiftUp(self, window, dy):
        max_shift = window.get_height() - self.posBottomRight.getY()
        if self.shiftY - dy > max_shift:
            self.shiftY = self.shiftY - dy

    def getGameMap(self):
        return self.imgInfoGameMap

    def getCivilization(self, idx):
        return self.imgInfoCivilizations[idx]

    def getMarketMap(self):
        return self.imgInfoMarketMap

    def draw(self, window):
        if self.nextButton:
            pos = Position(EImageObject.NEXT_BUTTON.getX(), EImageObject.NEXT_BUTTON.getY())
            img = ImageHandler.getImageOfProcess(EProcess.NEXT_BUTTON)
            resize = EImageObject.NEXT_BUTTON.getResize()
            DrawCivObjects.drawImage(img, window, ERotation.NO_ROTATION, pos, resize, 1)

    @classmethod
    def getRect(cls, imgObj):
        return int(imgObj.getSizeX()), int(imgObj.getSizeY())
