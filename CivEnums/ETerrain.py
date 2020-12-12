from enum import Enum


class ETerrain(Enum):

    def __init__(self, tp, pp, s, na, img):
        self.tradingPoints = tp
        self.productionPoints = pp
        self.sign = s
        self.gpName = na
        self.imgName = img

    def getTradingPoints(self):
        return self.tradingPoints

    def getProductionPoints(self):
        return self.productionPoints

    def getSign(self):
        return self.sign

    def getImgName(self):
        return self.imgName

    MOUNTAIN = (0, 1, "m", "Gebirge", "Mountain")
    GRASSLAND = (0, 0, "g", "Grasland", "Grassland")
    FOREST = (0, 2, "f", "Wald", "Forest")
    DESERT = (1, 0, "w", "Wüste", "Desert")
    SEA = (1, 0, "o", "Meer", "Sea")
    DROUGHT = (1, 0, "s", "Dürre", "Drought")
    DEFORESTATION = (0, 0, "a", "Abholzung", "Deforestation")
