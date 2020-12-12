from enum import Enum


class EEra(Enum):

    def __init__(self, na, img):
        self.eraName = na
        self.imgName = img

    def getImgName(self):
        return self.imgName

    ANCIENT = ("Antike", "Ancient")
    MIDDLE_AGE = ("Mittelalter", "MiddleAge")
    MODERN = ("Moderne", "Modern")
