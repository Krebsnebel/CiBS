from CivEnums.ERefPoint import ERefPoint
from CivObjects.Position import Position
from Drawing.ImgInfo import ImgInfo


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

    def getResize(self, imgObj):
        return imgObj.getResize() * self.scale

    def getImgPosOf(self, imgObj, x, y):
        pos = self.getPosOf(ERefPoint.TOP_LEFT, False)
        if x < 0 or x > 3:
            return Position(0, 0)
        if y < 0 or y > 1:
            return Position(0, 0)
        return Position(pos.getX() + imgObj.getX() * (x+1) + imgObj.getSizeX() * x,
                        pos.getY() + imgObj.getY() * (y+1) + imgObj.getSizeY() * y)
