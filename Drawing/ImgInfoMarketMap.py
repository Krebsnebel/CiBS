from CivEnums.ERefPoint import ERefPoint
from CivObjects.Position import Position
from Drawing.ImgInfo import ImgInfo


"""
this class is an image information of market map
* set mouse position, while mouse pressed and for highlighting
* getter for resize and image position of image object
"""


class ImgInfoMarketMap(ImgInfo):

    def __init__(self):
        super().__init__(1843, 651, Position(90, -611), ERefPoint.TOP_LEFT)

    def setMousePositionForHighlighting(self, mousePosition):
        pass

    def leftMouseButtonPressed(self, mousePosition):
        pass

    def getResize(self, imgObj):
        return imgObj.getResize() * self.scale

    def getImgPosOf(self, imgObj):
        pos = self.getPosOf(ERefPoint.TOP_LEFT, True)
        return Position(pos.getX() + imgObj.getX(), pos.getY() + imgObj.getY())
