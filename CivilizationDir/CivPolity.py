from CivEnums.EPolity import EPolity
from Drawing import ImageHandler


"""
this class handles the polity of each civilization
some getters and setters are implemented
"""


class CivPolity:

    def __init__(self, civ):
        self.civ = civ
        self.polity = EPolity.DESPOTISM
        self.armyCanBuildCity = False
        self.previouslyUnlockedPolity = None
        self.unlockedPolities = []
        self.unlock(EPolity.DESPOTISM)
        self.politySwitched = False

    def isPolitySwitched(self):
        return self.politySwitched

    def setPolitySwitched(self, switched):
        self.politySwitched = switched

    def getCivilizationEnum(self):
        return self.civ

    def isActive(self, polity):
        return self.polity is polity

    def getPolity(self):
        return self.polity

    def getPreviouslyUnlockedPolity(self):
        return self.previouslyUnlockedPolity

    def setPolity(self, polity):
        self.polity = polity
        if polity == EPolity.REPUBLIC:
            self.armyCanBuildCity = True
        else:
            self.armyCanBuildCity = False

    def getImg(self):
        return ImageHandler.getImageOfPolity(self.polity)

    def armyCanBuildCity(self):
        return self.armyCanBuildCity

    def unlock(self, polity):
        for p in self.unlockedPolities:
            if p is polity:
                return False
        self.unlockedPolities.append(polity)
        return True

    def getUnlockedPolities(self):
        return self.unlockedPolities

    def previouslyUnlockedPolity(self, polity):
        self.previouslyUnlockedPolity = polity

    def resetPreviousUnlockedPolity(self):
        self.previouslyUnlockedPolity = None
