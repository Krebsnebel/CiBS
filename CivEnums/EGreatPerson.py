from enum import Enum

from CivEnums.EResource import EResource


class EGreatPerson(Enum):

    def __init__(self, tp, pp, cp, dp, res, s, na, img):
        self.tradingPoints = tp
        self.productionPoints = pp
        self.culturePoints = cp
        self.defencePoints = dp
        self.resource = res
        self.sign = s
        self.gpName = na
        self.imgName = img

    def getTradingPoints(self):
        return self.tradingPoints

    def getProductionPoints(self):
        return self.productionPoints

    def getCulturePoints(self):
        return self.culturePoints

    def getDefencePoints(self):
        return self.defencePoints

    def getResource(self):
        return self.resource

    def getSign(self):
        return self.sign

    def getImgName(self):
        return self.imgName

    ARTIST = (1, 0, 2, 0, EResource.NONE, "j", "Künstler", "Artist")
    BUILDER = (0, 2, 0, 0, EResource.COIN, "b", "Baumeister", "Engineer")
    GENERAL = (0, 0, 0, 4, EResource.NONE, "g", "General", "General")
    HUMANITARIAN = (1, 1, 1, 0, EResource.COIN, "h", "Humanist", "Humanitarian")
    INDUSTRIALIST = (0, 0, 2, 0, EResource.COIN, "i", "Industrieller", "Industrialist")
    SCIENTIST = (2, 1, 0, 0, EResource.NONE, "w", "Wissenschaftler", "Scientist")
