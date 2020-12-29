from enum import Enum

from CivEnums.EEra import EEra
from CivEnums.EResearch import EResearch
from CivEnums.EVisibility import EVisibility


class EWonder(Enum):

    def __init__(self, cp, c, ca, rred, era, s, n, img):
        self.culturePoints = cp
        self.costs = c
        self.costsAlternative = ca
        self.researchReduced = rred
        self.era = era
        self.sign = s
        self.wonderName = n
        self.imgNameMarker = "Marker_" + img
        self.imgNameCardFront = "Card_" + img
        self.imgNameCardBack = "Card_" + era.getImgName()

    def getCulturePoints(self):
        return self.culturePoints

    def getSign(self):
        return self.sign

    def getCosts(self):
        return self.costs

    def getCostsAlternative(self):
        return self.costsAlternative

    def getMarkerImgName(self):
        return self.imgNameMarker

    def getCardImgName(self, visible):
        if visible:
            return self.imgNameCardFront
        else:
            return self.imgNameCardBack

    STONEHENGE = (1, 10, 10, EResearch.NONE, EEra.ANCIENT, "S", "Stonehenge", "Stonehenge")
    THE_HANGING_GARDENS = (1, 15, 10, EResearch.STOCK_BREEDING, EEra.ANCIENT, "H", "Die hängenden Gärten",
                           "TheHangingGardens")
    THE_COLOSSUS = (1, 15, 10, EResearch.IRON_PROCESSING, EEra.ANCIENT, "C", "Der Koloss", "TheColossus")
    THE_ORACLE = (1, 15, 10, EResearch.LEGISLATION, EEra.ANCIENT, "O", "Das Orakel", "TheOracle")
    THE_LOUVRE = (2, 20, 15, EResearch.PRINTING_PRESS, EEra.MIDDLE_AGE, "L", "Der Louvre", "TheLouvre")
    CASTLE_HIMEJI = (2, 20, 15, EResearch.MONARCHY, EEra.MIDDLE_AGE, "B", "Burg Himeji", "CastleHimeji")
    ANGKOR_WAT = (2, 20, 15, EResearch.THEOLOGY, EEra.MIDDLE_AGE, "A", "Angkor Wat", "AngkorWat")
    PORCELAIN_TOWER = (2, 20, 15, EResearch.CONSTRUCTION_INDUSTRY, EEra.MIDDLE_AGE, "P", "Porzellanturm",
                       "ProcelainTower")
    PANAMA_CANAL = (3, 25, 20, EResearch.MECHANICAL_ENGINEERING, EEra.MODERN, "K", "Panamakanal", "PanamaCanal")
    OPERA_HOUSE_OF_SIDNEY = (3, 25, 25, EResearch.NONE, EEra.MODERN, "Y", "Opernhaus von Sydney",
                             "OperaHouseOfSydney")
    STATUE_OF_LIBERTY = (3, 25, 20, EResearch.METAL_CASTING, EEra.MODERN, "F", "Freiheitsstatue", "StatueOfLiberty")
    UNITED_NATIONS = (3, 20, 20, EResearch.NONE, EEra.MODERN, "U", "Vereinte Nationen", "UnitedNations")
