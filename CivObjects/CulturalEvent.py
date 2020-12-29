from CivEnums.EVisibility import EVisibility
from Drawing import ImageHandler
from Drawing.DrawCivObjects import DrawCivObjects


"""
with it all properties of cultural event can be defined
* event
* visibility
* pointer to image
"""


class CulturalEvent:

    def __init__(self, event):
        self.event = event
        self.visibility = EVisibility.FOR_NOBODY
        self.imgCard = ImageHandler.getImageOfCulturalEvent(self.event, False)

    def setVisible(self, visible):
        if visible:
            self.visibility = EVisibility.FOR_ALL
            self.imgCard = ImageHandler.getImageOfCulturalEvent(self.event, True)
        else:
            self.visibility = EVisibility.FOR_NOBODY
            self.imgCard = ImageHandler.getImageOfCulturalEvent(self.event, False)

    def draw(self, window, rotation, pos, resize, scale):
        DrawCivObjects.drawImage(self.imgCard, window, rotation, pos, resize, scale)


