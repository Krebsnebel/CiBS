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
        self.imgPolity = ImageHandler.getImageOfPolity(self.polity)
        self.possiblePolities = []
        self.addPossiblePolity(EPolity.DESPOTISM)

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
        self.imgPolity = ImageHandler.getImageOfPolity(self.polity)

    def getImg(self):
        return self.imgPolity

    def armyCanBuildCity(self):
        return self.armyCanBuildCity

    def addPossiblePolity(self, polity):
        for p in self.possiblePolities:
            if p is polity:
                return False
        self.possiblePolities.append(polity)
        return True

    def getPossiblePolities(self):
        return self.possiblePolities

    def previouslyUnlockedPolity(self, polity):
        self.previouslyUnlockedPolity = polity

    def resetPreviousUnlockedPolity(self):
        self.previouslyUnlockedPolity = None
