class BusinessObject:

    def __init__(self, tp, pp, cp, dp, res, s):
        self.tradingPoints = tp
        self.productionPoints = pp
        self.culturePoints = cp
        self.defencePoints = dp
        self.resource = res
        self.sign = s

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
