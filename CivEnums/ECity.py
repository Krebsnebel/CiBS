from enum import Enum


class ECity(Enum):

    def __init__(self, dp, dpu, s, su, na, nau, imgu, imgf):
        self.defencePoints = dp
        self.defencePointsUpgrade = dpu
        self.sign = s
        self.signUpgrade = su
        self.cityName = na
        self.cityNameUpgrade = nau
        self.imgUnpaved = imgu
        self.imgFortified = imgf

    def getDefencePoints(self, upgrade):
        if upgrade:
            return self.defencePointsUpgrade
        else:
            return self.defencePoints

    def getSign(self, upgrade):
        if upgrade:
            return self.signUpgrade
        else:
            return self.sign

    def getImgName(self, upgrade):
        if upgrade:
            return self.imgFortified
        else:
            return self.imgUnpaved

    TOWN = (6, 10, "V", "W", "Stadt", "befestigte Stadt", "Town_Unpaved", "Town_Fortified")
    KAPITOL = (12, 16, "M", "F", "Hauptstadt", "befestigte Hauptstadt", "Kapitol_Unpaved", "Kapitol_Fortified")
