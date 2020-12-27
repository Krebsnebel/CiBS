from CivEnums.ERefPoint import ERefPoint
from CivObjects.Position import Position
from Drawing.EImageObject import EImageObject
from Drawing.ImgInfo import ImgInfo
from Options.EOptionType import EOptionType
from Options.Option import Option

"""
* set mouse position, while mouse pressed and for highlighting
* getter of image position of image objects
* getter of image resize of image objects
"""


class ImgInfoPolity(ImgInfo):

    def __init__(self):
        super().__init__(650, 245, Position(300, 100), ERefPoint.TOP_LEFT)

    def setMousePositionForHighlighting(self, mousePosition):
        pass

    def leftMouseButtonPressed(self, mousePosition):
        pass

    def getImgPosOf(self, imgObj, posPol):
        pos = self.getPosOf(ERefPoint.TOP_LEFT, False, False)
        x = posPol.getX()
        y = posPol.getY()
        if x < 0 or x > 3:
            return Position(0, 0)
        if y < 0 or y > 1:
            return Position(0, 0)
        return Position(pos.getX() + imgObj.getX() * (x+1) + imgObj.getSizeX() * x,
                        pos.getY() + imgObj.getY() * (y+1) + imgObj.getSizeY() * y)

    def setOption(self, imgObj, idx):
        posPol = Position(idx % 4, idx // 4)
        imgPos = self.getImgPosOf(imgObj, posPol)
        self.options.append(Option(imgObj, imgPos.getX(), imgPos.getY(), EOptionType.SQUARE, self.emphasize, posPol))

    def setMousePosition(self, x, y):
        ImgInfo.setMousePosition(self, x, y)
        self.mouseAtPossiblePosition = None
        for opt in self.options:
            mousePos = self.getMousePosition(False)
            insideX = opt.getX() < mousePos.getX()/self.scale - self.getShiftX() <= opt.getX() + opt.getWidth()
            insideY = opt.getY() < mousePos.getY()/self.scale - self.getShiftY() <= opt.getY() + opt.getHeight()
            if insideX and insideY:
                self.mouseAtPossiblePosition = Option(opt.getImgObj(), opt.getX(), opt.getY(),
                                                      opt.getOptionType(), opt.getEmphasize(), opt.getPositionOfMap())

    def getValidChoiceWhileMousePressed(self):
        if self.isLeftMouseButtonPressed():
            return self.mouseAtPossiblePosition
        return None
