from enum import Enum

from CivEnums.EPermission import EPermission
from CivEnums.EResource import EResource


class EBuilding(Enum):

    def __init__(self, p, ua, ui, tp, tpu, pp, ppu, cp, cpu, dp, dpu, res, resu, c, ca, s, su, na, nau, img, imgu):
        self.permissionTerrain = p
        self.upgradeable = ua
        self.unique = ui
        self.tradingPoints = tp
        self.tradingPointsUpgrade = tpu
        self.productionPoints = pp
        self.productionPointsUpgrade = ppu
        self.culturePoints = cp
        self.culturePointsUpgrade = cpu
        self.defencePoints = dp
        self.defencePointsUpgrade = dpu
        self.resource = res
        self.resourceUpgrade = resu
        self.costs = c
        self.costsAlternative = ca
        self.sign = s
        self.signUpgrade = su
        self.buildingName = na
        self.buildingNameUpgrade = nau
        self.img = img
        self.imgUpgrade = imgu

    def getPermissionTerrain(self):
        return self.permissionTerrain

    def getUnique(self):
        return self.unique

    def getTradingPoints(self, upgrade):
        if upgrade:
            return self.tradingPointsUpgrade
        else:
            return self.tradingPoints

    def getProductionPoints(self, upgrade):
        if upgrade:
            return self.productionPointsUpgrade
        else:
            return self.productionPoints

    def getCulturePoints(self, upgrade):
        if upgrade:
            return self.culturePointsUpgrade
        else:
            return self.culturePoints

    def getDefencePoints(self, upgrade):
        if upgrade:
            return self.defencePointsUpgrade
        else:
            return self.defencePoints

    def getResource(self, upgrade):
        if upgrade:
            return self.resourceUpgrade
        else:
            return self.resource

    def getCosts(self):
        return self.costs

    def getCostsAlternative(self):
        return self.costsAlternative

    def getSign(self, upgrade):
        if upgrade:
            return self.signUpgrade
        else:
            return self.sign

    def getImgName(self, upgrade):
        if upgrade:
            return self.imgUpgrade
        else:
            return self.img

    def getBackImg(self):
        return self.backImg

    MARINA = (EPermission.ONLY_WATER, False, False, 2, 2, 1, 1, 0, 0, 0, 0, EResource.NONE, EResource.NONE,
              7, 7, "M", "M", "Hafen", "Hafen", "Marina", "Marina")
    TRADING_POST = (EPermission.ONLY_DESERT, False, False, 2, 2, 0, 0, 1, 1, 0, 0, EResource.NONE,
                    EResource.NONE, 7, 7, "H", "H", "Handelsposten", "Handelsposten", "TradingPost", "TradingPost")
    BLACKSMITH = (EPermission.ONLY_MOUNTAIN, True, False, 0, 0, 3, 4, 0, 0, 0, 0, EResource.NONE, EResource.NONE,
                  7, 10, "S", "E", "Schmiede", "Eisenmine", "Blacksmith", "Ironmine")
    LIBRARY = (EPermission.ONLY_GRASSLAND, True, False, 1, 2, 0, 0, 1, 2, 0, 0, EResource.NONE, EResource.NONE,
               5, 8, "L", "U", "Bibliothek", "Universität", "Library", "University")
    GRANARY = (EPermission.ONLY_GRASSLAND, True, False, 1, 2, 1, 2, 0, 0, 0, 0, EResource.NONE, EResource.NONE,
               5, 8, "K", "A", "Kornspeicher", "Aquädukt", "Granary", "Aqueduct")
    MARKET = (EPermission.ALL_EXCEPT_WATER, True, True, 1, 1, 1, 1, 1, 1, 0, 0, EResource.NONE, EResource.COIN,
              7, 10, "R", "B", "Markt", "Bank", "Market", "Bank")
    TEMPLE = (EPermission.ALL_EXCEPT_WATER, True, True, 0, 0, 0, 0, 2, 3, 0, 0, EResource.NONE, EResource.NONE,
              7, 10, "T", "C", "Tempel", "Kathedrale", "Temple", "Cathedral")
    BARRACK = (EPermission.ALL_EXCEPT_WATER, True, True, 2, 2, 0, 0, 0, 0, 2, 4, EResource.NONE, EResource.NONE,
               7, 10, "B", "A", "Kaserne", "Akademie", "Barrack", "Academy")
