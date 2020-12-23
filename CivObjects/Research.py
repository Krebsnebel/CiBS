from CivEnums.EVisibility import EVisibility
from Drawing import ImageHandler
from Drawing.DrawCivObjects import DrawCivObjects


"""
with it all properties of research can be defined
* research type
* if it is researched or not
* visibility
* pointer to image
"""


class Research:

    def __init__(self, rType):
        self.research = rType
        self.researched = False
        self.visibility = EVisibility.FOR_NOBODY
        self.img = ImageHandler.getImageOfResearch(rType, False)

    def setVisible(self):
        self.visibility = EVisibility.FOR_ALL
        self.img = ImageHandler.getImageOfResearch(self.research, True)

    def hideResearchCard(self):
        self.visibility = EVisibility.FOR_NOBODY
        self.img = ImageHandler.getImageOfResearch(self.research, False)

    def draw(self, window, rotation, pos, resize, scale):
        DrawCivObjects.drawImage(self.img, window, rotation, pos, resize, scale)
