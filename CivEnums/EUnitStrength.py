from enum import Enum


class EUnitStrength(Enum):

    def __init__(self, i, ii, iii, iv, af, img):
        self.fightVal_I = i
        self.fightVal_II = ii
        self.fightVal_III = iii
        self.fightVal_IV = iv
        self.fightVal_airForce = af
        self.imgName = img

    def getImgName(self):
        return self.imgName

    WEAK = (1, 2, 3, 4, 5, "Weak")
    MEDIUM = (2, 3, 4, 5, 6, "Medium")
    STRONG = (3, 4, 5, 6, 7, "Strong")

    def getFightValue(self, rank):
        if rank == 1:
            return self.fightVal_I
        elif rank == 2:
            return self.fightVal_II
        elif rank == 3:
            return self.fightVal_III
        elif rank == 4:
            return self.fightVal_IV
        else:
            return self.fightVal_airForce
