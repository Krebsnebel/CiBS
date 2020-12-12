from enum import Enum

from CivEnums.EException import EException


class ECivilization(Enum):

    def __init__(self, idx, civ_name, civ_imp, img, exception):
        self.civIndex = idx
        self.civName = civ_name
        self.civImperator = civ_imp
        self.imgName = img
        self.exception = exception

    def getException(self):
        return self.exception

    def __str__(self):
        return self.civName

    def getCivIndex(self):
        return self.civIndex

    def getCivName(self):
        return self.civName

    def getCivImperator(self):
        return self.civImperator

    def getImgName(self):
        return self.imgName

    NONE = (0, "none", "none", "-", EException.NO_EXCEPTION)
    AMERICA = (1, "Amerika", "Abraham Lincoln", "Civilization_America", EException.NO_EXCEPTION)
    AGYPT = (2, "Ägypten", "Kleopatra", "Civilization_Agypt", EException.NO_EXCEPTION)
    CHINA = (3, "China", "Wu-Zetian", "Civilization_China", EException.NO_EXCEPTION)
    ROME = (4, "Rom", "Augustus", "Civilization_Rome", EException.PIONEER_DISCOVER_COTTAGE)
    RUSSIA = (5, "Russland", "Katharina", "Civilization_Russia", EException.NO_EXCEPTION)
    GERMANY = (6, "Deutschland", "Bismark", "Civilization_Germany", EException.NO_EXCEPTION)