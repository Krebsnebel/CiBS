from CivEnums.EGameSection import EGameSection
from CivEnums.EVisibility import EVisibility
from Drawing.EImageObject import EImageObject


"""
this class represents the possibilities of each civilization
"""


class CivPossibilities:

    def __init__(self, gameMap, civ):
        self.gameMap = gameMap
        self.civ = civ
        self.citiesAreSet = [False, False, False]
        self.cities = []
        for i in range(3):
            self.cities.append(self.civ.getCity(i))

        self.cityObj = EImageObject.NO_OBJECT
        self.isSwitchingPolityPossible = True #False

        self.isMarketPossible = False
        self.isTemplePossible = False
        self.isGranaryPossible = False
        self.isLibraryPossible = False
        self.isBarrackPossible = False
        self.isBlacksmithPossible = False
        self.isMarinaPossible = False
        self.isTradingPostPossible = False
        self.isInfantryUnitPossible = False
        self.isArtilleryUnitPossible = False
        self.isCavalryUnitPossible = False
        self.isAirForceUnitPossible = False
        self.areVisibleWondersPossible = [False, False, False, False]

        self.pointsForKapitol = []
        self.currentPointsForTown = []

    def getObjImgForHighlighting(self):
        objImgList = []
        if self.isSwitchingPolityPossible:
            objImgList.append(EImageObject.POLITY)
        if self.cityObj is not EImageObject.NO_OBJECT:
            objImgList.append(self.cityObj)
        return objImgList

    def setCurrentPointsForTown(self):
        self.currentPointsForTown = []
        listFig = self.civ.getFiguresForFoundingCity()
        for fig in listFig:
            s = self.isPointInPotentiallyList(fig.getPosition(), self.gameMap.getPotentiallyPointsForTown())
            if s is not None:
                possible = self.gameMap.isPuttingTownOnSquareCurrentlyPossible(s, self.civ.getCivilizationEnum())
                fig.setPotentialCandidateForFoundingCity(possible)
                if possible:
                    self.currentPointsForTown.append(s)

    def getPointsOf(self, objType):
        if objType == EImageObject.KAPITOL:
            return self.pointsForKapitol
        else:
            return self.getPointsForObjectSetInCities(objType)

    def setGameSection(self, section):
        if section == EGameSection.START_ROUND:
            self.isSwitchingPolityPossible = True
            if len(self.currentPointsForTown) > 0:
                if not self.citiesAreSet[1]:
                    self.cityObj = EImageObject.CITY_1
                elif not self.citiesAreSet[2] and self.civ.isThirdCityPossible():
                    self.cityObj = EImageObject.CITY_2

    # refresh is necessary under following conditions:
    # * unique building is set / removed
    # * wonder is set / removed
    def refreshCityConstellation(self, cityNr, setCity):
        self.citiesAreSet[cityNr] = setCity
        city = self.cities[cityNr]
        city.clearPotentialPoints()
        if setCity:
            city.setPotentialPointsForCity()

    # only once for initialization
    def setPointsForKapitol(self):
        for y in range(16):
            for x in range(16):
                possible = True
                s = self.gameMap.getSquare(x, y)
                if s is None:
                    # print("Es gibt hier kein Terrain")
                    possible = False
                m = self.gameMap.findMapTile(x, y)
                if possible and m.getVisibility() == EVisibility.FOR_NOBODY:
                    # print("The Terrain is not discovered")
                    possible = False
                if possible:
                    # template town which represents all towns of civilizations
                    possible = self.gameMap.isPuttingKapitolOnSquarePossible(self.cities[0], s, m)
                if possible:
                    self.pointsForKapitol.append(s)

    def getPointsForObjectSetInCities(self, objType):
        sumPoints = []
        for c in self.cities:
            points = c.getPointsForObjectSetInCity(objType)
            if points is not None:
                for p in points:
                    sumPoints.append(p)
        return sumPoints

    @ classmethod
    def isPointInPotentiallyList(cls, p, potentiallyList):
        for s in potentiallyList:
            if p.isEqual(s.getposition()):
                return s
        return None
