from enum import Enum


class EFigure(Enum):

    def __init__(self, img):
        self.imgName = img

    def getImgName(self):
        return self.imgName

    ARMY = "Army"
    PIONEER = "Pioneer"
