from CivEnums.EBuilding import EBuilding
from CivEnums.ECivilization import ECivilization
from CivEnums.EColor import EColor
from CivEnums.EConstants import EConstants
from CivEnums.EFigure import EFigure
from CivEnums.EGreatPerson import EGreatPerson
from CivEnums.EPermission import EPermission
from CivEnums.EGameSection import EGameSection
from CivEnums.EVisibility import EVisibility
from CivEnums.EWonder import EWonder
from CivObjects.Building import Building
from CivObjects.Figure import Figure
from CivObjects.GreatPerson import GreatPerson
from CivObjects.Wonder import Wonder
from CivilizationDir.City import City
from Drawing.EImageObject import EImageObject
from GameProcess.EGameStep import EGameStep

"""
this class represents the possibilities of each civilization
"""


class CivOptions:

    def __init__(self, game, gameStep, civ):
        self.gameStep = gameStep
        self.game = game
        self.gameMap = self.game.getGameMap()
        self.civ = civ
        self.cities = []
        for i in range(3):
            self.cities.append(self.civ.getCity(i))

        self.cityObj = EImageObject.NO_OBJECT

        # Objects from own civilization
        self.selectPolity = False
        self.selectCity1 = False
        self.selectCity2 = False

        # Objects from market place
        self.pickMarket = False
        self.pickTemple = False
        self.pickGranary = False
        self.pickLibrary = False
        self.pickBarrack = False
        self.pickBlacksmith = False
        self.pickTradingPost = False
        self.pickMarina = False
        self.pickWonderCardStack = True
        self.pickWonderCard1 = False
        self.pickWonderCard2 = False
        self.pickWonderCard3 = False
        self.pickWonderCard4 = False
        self.pickWonderMarker1 = False
        self.pickWonderMarker2 = False
        self.pickWonderMarker3 = False
        self.pickWonderMarker4 = False
        self.pickInfantry = False
        self.pickArtillery = False
        self.pickCavalry = False
        self.pickAirForce = False
        self.pickCultureCardI = False
        self.pickCultureCardII = False
        self.pickCultureCardIII = False
        self.pickIron = False
        self.pickIncense = False
        self.pickWheat = False
        self.pickSilk = False
        self.pickCoin = False
        self.pickCulture = False
        self.pickCottage = False
        self.pickBarbarian = False

        self.cultureStepArray = [False for i in range(EConstants.CULTURE_LEVELS.value)]

        self.pointsForKapitol = [[False for i in range(16)] for j in range(16)]
        self.pointsForNextTown = [[False for i in range(16)] for j in range(16)]
        self.pointsForUniqueBuildings = [[False for i in range(16)] for j in range(16)]
        self.pointsForBuildingsOnGrasland = [[False for i in range(16)] for j in range(16)]
        self.pointsForBuildingsInMountain = [[False for i in range(16)] for j in range(16)]
        self.pointsForBuildingsOnWater = [[False for i in range(16)] for j in range(16)]
        self.pointsForBuildingsInDesert = [[False for i in range(16)] for j in range(16)]
        self.pointsForObjectsOnLand = [[False for i in range(16)] for j in range(16)]
        self.pointsForFigures = [[False for i in range(16)] for j in range(16)]

        self.outskirtOfKaptiol = [[False for i in range(16)] for j in range(16)]
        self.outskirtOfTown1 = [[False for i in range(16)] for j in range(16)]
        self.outskirtOfTown2 = [[False for i in range(16)] for j in range(16)]
        self.pointsOfDisaster = [[False for i in range(16)] for j in range(16)]

        self.optionsGameMap = [[False for i in range(16)] for j in range(16)]
        self.mouseAtPossibleGameMapPosition = None
        self.mousePressedAtPossibleGameMapPosition = None

    def clearOptions(self):
        self.clearOptionsForMarketPlace()
        self.clearOptionsForCivilization()

    def clearOptionsForMarketPlace(self):
        self.pickMarket = False
        self.pickTemple = False
        self.pickGranary = False
        self.pickLibrary = False
        self.pickBarrack = False
        self.pickBlacksmith = False
        self.pickTradingPost = False
        self.pickMarina = False
        self.pickWonderCardStack = True
        self.pickWonderCard1 = False
        self.pickWonderCard2 = False
        self.pickWonderCard3 = False
        self.pickWonderCard4 = False
        self.pickWonderMarker1 = False
        self.pickWonderMarker2 = False
        self.pickWonderMarker3 = False
        self.pickWonderMarker4 = False
        self.pickInfantry = False
        self.pickArtillery = False
        self.pickCavalry = False
        self.pickAirForce = False
        self.pickCultureCardI = False
        self.pickCultureCardII = False
        self.pickCultureCardIII = False
        self.pickIron = False
        self.pickIncense = False
        self.pickWheat = False
        self.pickSilk = False
        self.pickCoin = False
        self.pickCulture = False
        self.pickCottage = False
        self.pickBarbarian = False

        self.cultureStepArray = [False for i in range(EConstants.CULTURE_LEVELS.value)]

    def clearOptionsForCivilization(self):
        self.selectPolity = False
        self.selectCity1 = False
        self.selectCity2 = False

    def setOptionsInGameStep(self):
        self.setOptionsInGameMap()
        self.setOtherOptionsInGameStep()

    def setCityIsPossible(self, idx):
        if idx == 1:
            if self.cities[1].isSet():
                return False
        else:   # idx == 2
            if not self.cities[1].isSet() or not self.civ.isThirdCityPossible():
                return False

        for y in range(16):
            for x in range(16):
                if self.pointsForNextTown[x][y]:
                    return True
        return False

    def setOtherOptionsInGameStep(self):
        if self.gameStep.getSection() == EGameSection.PREPARE_GAME:
            self.clearOptions()
        elif self.gameStep.getSection() == EGameSection.START_ROUND:
            self.clearOptions()
            if self.isInStep(EGameStep.GENERAL_SELECT):
                self.selectPolity = True
                self.selectCity1 = self.setCityIsPossible(1)
                self.selectCity2 = self.setCityIsPossible(2)
            elif self.isInStep(EGameStep.SELECT_POLITY):
                pass
            elif self.isInStep(EGameStep.POLITY_SELECTED):
                pass
            elif self.isInStep(EGameStep.WONDER_SKILL_SELECTED):
                pass
            elif self.isInStep(EGameStep.CULTURE_SKILL_SELECTED):
                pass
            elif self.isInStep(EGameStep.RESEARCH_SKILL_SELECTED):
                pass
            elif self.isInStep(EGameStep.SET_CITY):
                pass
            elif self.isInStep(EGameStep.SWITCH_CIVILIZATION):
                pass
        elif self.gameStep.getSection() == EGameSection.TRADE:
            pass
        elif self.gameStep.getSection() == EGameSection.CITY_ADMINISTRATION:
            pass
        elif self.gameStep.getSection() == EGameSection.MOVEMENT:
            pass
        elif self.gameStep.getSection() == EGameSection.RESEARCH:
            pass
        else:
            return False
        pol = self.selectPolity
        c1 = self.selectCity1
        c2 = self.selectCity2
        self.civ.getImgInfo().setOptions(pol, c1, c2)

        # set options for market place
        imgInfo = self.game.getMarketMap().getImgInfo()
        imgInfo.setOptionsForBuildings(self.pickMarket, self.pickTemple, self.pickGranary, self.pickLibrary,
                                       self.pickBarrack, self.pickBlacksmith, self.pickTradingPost, self.pickMarina)
        imgInfo.setOptionsForWonder(self.pickWonderCardStack, self.pickWonderCard1, self.pickWonderCard2,
                                    self.pickWonderCard3, self.pickWonderCard4, self.pickWonderMarker1,
                                    self.pickWonderMarker2, self.pickWonderMarker3, self.pickWonderMarker4)
        imgInfo.setOptionsForMilitaryAndCultureCards(self.pickInfantry, self.pickArtillery, self.pickCavalry,
                                                     self.pickAirForce, self.pickCultureCardI, self.pickCultureCardII,
                                                     self.pickCultureCardIII)
        imgInfo.setOptionsForMarker(self.pickIron, self.pickIncense, self.pickWheat, self.pickSilk, self.pickCoin,
                                    self.pickCulture, self.pickCottage, self.pickBarbarian)
        imgInfo.setOptionsForCultureLevelMarker(self.cultureStepArray)
        imgInfo.setOptions()

    def setOptionsInGameMap(self):
        for y in range(16):
            for x in range(16):
                if self.gameStep.getSection() == EGameSection.PREPARE_GAME:
                    if self.isInStep(EGameStep.MARK_SQUARES_FOR_HIGHLIGHTING_CITY):
                        self.optionsGameMap[x][y] = self.pointsForKapitol[x][y]
                    elif self.isInStep(EGameStep.SET_CITY):
                        self.optionsGameMap[x][y] = self.pointsForKapitol[x][y]
                    elif self.isInStep(EGameStep.SET_WONDER):
                        obj = Wonder(EWonder.STONEHENGE)
                        self.optionsGameMap[x][y] = self.isPlacingObjectAtCityPossible(x, y, obj, 1)
                    elif self.isInStep(EGameStep.SET_GREAT_PERSON):
                        obj = GreatPerson(EGreatPerson.ARTIST)
                        self.optionsGameMap[x][y] = self.isPlacingObjectAtCityPossible(x, y, obj, 1)
                    elif self.isInStep(EGameStep.SET_PIONEER):
                        obj = Figure(EFigure.PIONEER, ECivilization.NONE, EColor.NO_COLOR)
                        self.optionsGameMap[x][y] = self.isPlacingObjectAtCityPossible(x, y, obj, 1)
                    elif self.isInStep(EGameStep.SET_ARMY_NR1):
                        obj = Figure(EFigure.ARMY, ECivilization.NONE, EColor.NO_COLOR)
                        self.optionsGameMap[x][y] = self.isPlacingObjectAtCityPossible(x, y, obj, 1)
                    elif self.isInStep(EGameStep.SET_ARMY_NR2):
                        obj = Figure(EFigure.ARMY, ECivilization.NONE, EColor.NO_COLOR)
                        self.optionsGameMap[x][y] = self.isPlacingObjectAtCityPossible(x, y, obj, 1)
                    elif self.isInStep(EGameStep.COUNT_TRADING_POINTS):
                        self.optionsGameMap[x][y] = False
                    else:
                        return False
                elif self.gameStep.getSection() == EGameSection.START_ROUND:
                    if self.isInStep(EGameStep.GENERAL_SELECT):
                        pass
                    elif self.isInStep(EGameStep.SELECT_POLITY):
                        pass
                    elif self.isInStep(EGameStep.POLITY_SELECTED):
                        pass
                    elif self.isInStep(EGameStep.WONDER_SKILL_SELECTED):
                        pass
                    elif self.isInStep(EGameStep.CULTURE_SKILL_SELECTED):
                        pass
                    elif self.isInStep(EGameStep.RESEARCH_SKILL_SELECTED):
                        pass
                    elif self.isInStep(EGameStep.SET_CITY):
                        pass
                    elif self.isInStep(EGameStep.SWITCH_CIVILIZATION):
                        pass
                elif self.gameStep.getSection() == EGameSection.TRADE:
                    pass
                elif self.gameStep.getSection() == EGameSection.CITY_ADMINISTRATION:
                    pass
                elif self.gameStep.getSection() == EGameSection.MOVEMENT:
                    pass
                elif self.gameStep.getSection() == EGameSection.RESEARCH:
                    pass
                else:
                    return False
        self.gameMap.getImgInfo().setOptions(self.optionsGameMap)

    def setPointsForAllObjects(self):
        for y in range(16):
            for x in range(16):
                self.pointsForKapitol[x][y] = self.setPointsForKapitol(x, y)
                self.setPointForSpecificBuildings(x, y)

    def setPointsForKapitol(self, x, y):
        s = self.gameMap.getSquare(x, y)
        if s is None:
            # there is no terrain
            return False
        m = self.gameMap.findMapTile(x, y)
        if m.getVisibility() == EVisibility.FOR_NOBODY:
            # the Terrain is not discovered
            return False
        # template town which represents all towns of civilizations
        return self.gameMap.isPuttingKapitolOnSquarePossible(self.cities[0], s, m)

    def setPointForSpecificBuildings(self, x, y):
        self.outskirtOfKaptiol[x][y] = self.cities[0].isOutskirt(x, y)
        self.outskirtOfTown1[x][y] = self.cities[1].isOutskirt(x, y)
        self.outskirtOfTown2[x][y] = self.cities[2].isOutskirt(x, y)
        self.pointsOfDisaster[x][y] = self.gameMap.getSquare(x, y).getDisasterMarker() is not None
        bg = self.gameMap.isObjectOnTerrainPermitted(x, y, EPermission.ONLY_GRASSLAND, False)
        self.pointsForBuildingsOnGrasland[x][y] = bg
        bm = self.gameMap.isObjectOnTerrainPermitted(x, y, EPermission.ONLY_MOUNTAIN, False)
        self.pointsForBuildingsInMountain[x][y] = bm
        bw = self.gameMap.isObjectOnTerrainPermitted(x, y, EPermission.ONLY_WATER, False)
        self.pointsForBuildingsOnWater[x][y] = bw
        bd = self.gameMap.isObjectOnTerrainPermitted(x, y, EPermission.ONLY_DESERT, False)
        self.pointsForBuildingsInDesert[x][y] = bd
        bl = self.gameMap.isObjectOnTerrainPermitted(x, y, EPermission.ALL_EXCEPT_WATER, False)
        self.pointsForObjectsOnLand[x][y] = bl

    def isPlacingObjectAtCityPossible(self, x, y, obj, cityNr):
        o1 = self.outskirtOfKaptiol[x][y]
        o2 = self.outskirtOfTown1[x][y]
        o3 = self.outskirtOfTown2[x][y]
        if cityNr == 1:
            o = o1
        elif cityNr == 2:
            o = o2
        elif cityNr == 3:
            o = o3
        else:   # all cities:
            o = o1 or o2 or o3
        idx = cityNr - 1
        dm = self.pointsOfDisaster[x][y]
        if isinstance(obj, Building):
            bt = obj.getBuildingType()
            if bt is EBuilding.MARINA:
                bw = self.pointsForBuildingsOnWater[x][y]
                return o and bw and not dm
            elif bt is EBuilding.TRADING_POST:
                bd = self.pointsForBuildingsInDesert[x][y]
                return o and bd and not dm
            elif bt is EBuilding.BLACKSMITH:
                bm = self.pointsForBuildingsInMountain[x][y]
                return o and bm and not dm
            elif bt is EBuilding.LIBRARY or bt is EBuilding.GRANARY:
                bg = self.pointsForBuildingsOnGrasland[x][y]
                return o and bg and not dm
            else:           # bt is EBuilding.MARKET or EBuilding.TEMPLE or EBuilding.BARRACK
                bl = self.pointsForObjectsOnLand[x][y]
                if 0 <= idx < 3:
                    u = self.cities[idx].isUniqueBuildingThere()
                    return o and not u and bl and not dm
                else:
                    u1 = self.cities[0].isUniqueBuildingThere()
                    u2 = self.cities[1].isUniqueBuildingThere()
                    u3 = self.cities[2].isUniqueBuildingThere()
                    return ((o1 and not u1) or (o2 and not u2) or (o3 and not u3)) and bl and not dm
        elif isinstance(obj, Wonder):
            bl = self.pointsForObjectsOnLand[x][y]
            if 0 <= idx < 3:
                w = self.cities[idx].isWonderInOutskirt()
                return o and not w and bl and not dm
            else:
                w1 = self.cities[0].isWonderInOutskirt()
                w2 = self.cities[1].isWonderInOutskirt()
                w3 = self.cities[2].isWonderInOutskirt()
                return ((o1 and not w1) or (o2 and not w2) or (o3 and not w3)) and bl and not dm
        elif isinstance(obj, GreatPerson):
            bl = self.pointsForObjectsOnLand[x][y]
            return o and bl and not dm
        elif isinstance(obj, City):
            if cityNr == 1:
                return self.outskirtOfKaptiol[x][y]
            else:
                return self.pointsForNextTown[x][y]
        elif isinstance(obj, Figure):
            if obj.getPermissionTerrain() is EPermission.STOP_ON_WATER:
                return o and not dm
            else:
                bl = self.pointsForObjectsOnLand[x][y]
                return o and bl and not dm
        else:
            return False


#noch zu prüfen
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

    def getObjImgForHighlighting(self):
        objImgList = []
        if self.isSwitchingPolityPossible:
            objImgList.append(EImageObject.POLITY)
        if self.cityObj is not EImageObject.NO_OBJECT:
            objImgList.append(self.cityObj)
        return objImgList




    def setGameSection(self, section):
        if section == EGameSection.START_ROUND:
            self.isSwitchingPolityPossible = True
            if len(self.currentPointsForTown) > 0:
                if not self.citiesAreSet[1]:
                    self.cityObj = EImageObject.CITY_1
                elif not self.citiesAreSet[2] and self.civ.isThirdCityPossible():
                    self.cityObj = EImageObject.CITY_2


    @ classmethod
    def isPointInPotentiallyList(cls, p, potentiallyList):
        for s in potentiallyList:
            if p.isEqual(s.getposition()):
                return s
        return None

    def isInStep(self, step):
        return self.gameStep.getStep() == step

