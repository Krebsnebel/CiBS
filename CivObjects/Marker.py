from CivEnums.ENote import ENote
from CivObjects.Position import Position
from Drawing.DrawCivObjects import DrawCivObjects
from Drawing import ImageHandler

"""
with it all properties of marker can be defined
* marker type
* resource
* visibility
"""


class Marker:

    def __init__(self, mType, res):
        self.imgPosMM = None
        self.markerType = mType
        self.resource = res
        if mType == ENote.RESOURCE:
            self.visibility = True
        else:
            self.visibility = False
        self.img = ImageHandler.getImageOfMarker(mType, res, False)

    def getSign(self):
        return self.markerType.getSign()

    def getType(self):
        return self.markerType

    def setPositionOnMarketMap(self, imgPosMM):
        self.imgPosMM.setPosition(imgPosMM.getX(), imgPosMM.getY())

    def draw(self, window, rotation, pos, resize):
        DrawCivObjects.drawImage(self.img, window, rotation, pos, resize, 1)
