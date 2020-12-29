import pygame

from CivEnums.EArmyStrength import EArmyStrength
from CivEnums.ECity import ECity
from CivEnums.ECivilization import ECivilization
from CivEnums.EColor import EColor
from CivEnums.EFigure import EFigure
from CivEnums.EPolity import EPolity
from CivEnums.EResearch import EResearch
from CivEnums.ERotation import ERotation
from CivEnums.EUnitType import EUnitType
from CivEnums.EVisibility import EVisibility
from CivObjects.Figure import Figure
from CivilizationDir.City import City
from CivilizationDir.CivPolity import CivPolity
from CivilizationDir.CultureWonderAndGreatPersons import CultureWonderAndGreatPersons
from CivilizationDir.ResearchManager import ResearchManager
from Drawing.DrawCivObjects import DrawCivObjects
from Drawing.EImageObject import EImageObject
from Drawing.ImgInfoCivilization import ImgInfoCivilization
from Options.CivOptions import CivOptions

"""
this class represents each civilization, this means civilizations can be defined here
there are functions to
* count trading points
* get figures for founding city
* get list of potential city positions
* draw civilizations
* several getters and setters
** e.g. to set permission for specific terrains
"""


class Civilization:

    def __init__(self, imgInfoCiv, pl, map_tile, col, gameMap, gameStep):
        self.playerNr = pl
        self.imgInfo = imgInfoCiv
        self.gameMap = gameMap
        self.civ = map_tile.getCivilization()
        self.mapTile = map_tile
        self.civPolity = CivPolity(self.civ)
        self.color = col
        self.cities = []
        self.pioneer = []
        self.army = []
        self.militaryUnit = []
        self.figureLimit = 2
        self.movingRange = 2
        self.cultureCardLimit = 2
        self.computerTechnology = False
        self.thirdCityPossible = False
        self.unlockedBuildings = []
        self.wonderWithReducedCosts = []
        self.researchManager = ResearchManager(self, imgInfoCiv, pl)
        self.cultureWonderAndGreatPersons = CultureWonderAndGreatPersons(self, imgInfoCiv)
        self.cavalryStrength = EArmyStrength.FIRST_LEVEL
        self.artilleryStrength = EArmyStrength.FIRST_LEVEL
        self.infantryStrength = EArmyStrength.FIRST_LEVEL
        self.airForceStrength = EArmyStrength.NOT_ACTIVE
        self.cultureStepMarker = 0
        self.tradingPoints = 0
        self.goldPoints = 0
        self.img = pygame.image.load("Material/Civilizations/" + self.civ.getImgName() + ".jpg")
        self.imgTrade = pygame.image.load("Material/Civilizations/TradeDisk.png")
        self.imgGold = pygame.image.load("Material/Civilizations/GoldDisk.png")
        self.imgBack = pygame.image.load("Material/Civilizations/Civilization_Back.jpg")
        self.cities.append(City(ECity.KAPITOL, col, self.civ, EImageObject.KAPITOL))
        self.cities.append(City(ECity.TOWN, col, self.civ, EImageObject.CITY_1))
        self.cities.append(City(ECity.TOWN, col, self.civ, EImageObject.CITY_2))

        for i in range(2):
            self.pioneer.append(Figure(EFigure.PIONEER, self.civ, col))

        for i in range(6):
            self.army.append(Figure(EFigure.ARMY, self.civ, col))

        if self.civ == ECivilization.ROME:
            self.civPolity.setPolity(EPolity.REPUBLIC)
            self.researchManager.research(EResearch.LEGISLATION, 1, True)
        elif self.civ == ECivilization.RUSSIA:
            self.army.append(Figure(EFigure.ARMY, self.civ, EColor.WHITE))
            self.civPolity.setPolity(EPolity.COMMUNISM)
            self.researchManager.research(EResearch.COMMUNISM, 1, True)
        elif self.civ == ECivilization.AGYPT:
            self.researchManager.research(EResearch.CONSTRUCTION_INDUSTRY, 1, True)
        elif self.civ == ECivilization.GERMANY:
            self.researchManager.research(EResearch.IRON_PROCESSING, 1, True)
        elif self.civ == ECivilization.AMERICA:
            self.researchManager.research(EResearch.CURRENCY, 1, True)
        elif self.civ == ECivilization.CHINA:
            self.getCity(0).upgradeCity()
            self.researchManager.research(EResearch.SCRIPTURE, 1, True)

        self.options = CivOptions(gameMap, gameStep, self)

    def getValidChoiceWhileMousePressed(self):
        return self.imgInfo.getValidChoiceWhileMousePressed()

    def calculateOptions(self):
        self.options.setPointsForAllObjects()
        self.options.setOptionsInGameStep()

    def getCivPolity(self):
        return self.civPolity

    def isThirdCityPossible(self):
        return self.thirdCityPossible

    def activateThirdCity(self):
        self.thirdCityPossible = True

    def getImgInfo(self):
        return self.imgInfo

    def getFiguresForFoundingCity(self):
        listFig = []
        for pio in self.pioneer:
            if pio.getPosition() is not None:
                listFig.append(pio)
        if self.civPolity.isActive(EPolity.REPUBLIC):
            for a in self.army:
                if a.getPosition() is not None:
                    listFig.append(a)
        return listFig

    def getListOfPotentialCityPositions(self):
        points = []
        for pio in self.pioneer:
            p = pio.getPosition()
            if p is not None:
                points.append(p)

        if self.civPolity.armyCanBuildCity():
            for a in self.army:
                p = a.getPosition()
                if p is not None:
                    points.append(p)
        return points

    def countTradingPoints(self):
        tp = 0
        for c in self.cities:
            tp = tp + c.countTradingPoints()

        self.tradingPoints = self.tradingPoints + tp

    def getFigureLimit(self):
        return self.figureLimit

    def getColor(self):
        return self.color

    def unlockBuilding(self, building):
        self.unlockedBuildings.append(building)

    def addWonderWithReducedCosts(self, wonder):
        self.wonderWithReducedCosts.append(wonder)

    def unlockPolity(self, polity):
        self.civPolity.unlock(polity)

    def setArmyStrength(self, uType, desArmyStr):
        if uType is EUnitType.ARTILLERY:
            if self.artilleryStrength.value < desArmyStr.value:
                self.artilleryStrength = desArmyStr
        elif uType is EUnitType.CAVALRY:
            if self.cavalryStrength.value < desArmyStr.value:
                self.cavalryStrength = desArmyStr
        elif uType is EUnitType.INFANTRY:
            if self.infantryStrength.value < desArmyStr.value:
                self.infantryStrength = desArmyStr
        elif uType is EUnitType.AIR_FORCE:
            self.artilleryStrength = desArmyStr.value

    def setMovingRange(self, mr):
        if mr > self.movingRange:
            self.movingRange = mr

    def setFigureLimit(self, lim):
        if lim > self.figureLimit:
            self.movingRange = lim

    def increaseCultureCardLimit(self):
        # CERAMICS, PUBLIC_ADMINISTRATION, THEOLOGY
        self.cultureCardLimit = self.cultureCardLimit + 1

    def setAsResearched(self, research):
        if research is EResearch.COMPUTER_TECHNOLOGY:
            self.computerTechnology = True

    def setPermissionForFigures_MoveOverWater(self):
        for p in self.pioneer:
            p.setPermissionMoveOverWater()
        for a in self.army:
            a.setPermissionMoveOverWater()

    def setPermissionForFigures_StopOnWater(self):
        for p in self.pioneer:
            p.setPermissionStopOnWater()
        for a in self.army:
            a.setPermissionStopOnWater()

    def getResearchManager(self):
        return self.researchManager

    def getCivilizationEnum(self):
        return self.civ

    def popMapTile(self, x, y, rot):
        self.mapTile.setPosition(x, y, rot)
        return self.mapTile

    def addMilitaryUnit(self, unit):
        unit.changeVisibility(EVisibility.FOR_OWNER)
        self.militaryUnit.append(unit)

    def getCity(self, idx):
        return self.cities[idx]

    def getPioneer(self, idx):
        return self.pioneer[idx]

    def getArmy(self, idx):
        return self.army[idx]

    def draw(self, window):
        scale = self.imgInfo.getScale()
        rotTrade = ImgInfoCivilization.getRotationTradingPoints(self.tradingPoints)
        rotGold = ImgInfoCivilization.getRotationGoldPoints(self.tradingPoints, self.goldPoints)

        pos = self.imgInfo.getImgPosOf(EImageObject.CIVILIZATION_SHEET, True, False)
        resize = EImageObject.CIVILIZATION_SHEET.getResize()
        DrawCivObjects.drawImage(self.img, window, ERotation.NO_ROTATION, pos, resize, scale)

        pos = self.imgInfo.getImgPosOf(EImageObject.TRADE_DISK, True, False)
        resize = EImageObject.TRADE_DISK.getResize()
        DrawCivObjects.drawImage(self.imgTrade, window, rotTrade, pos, resize, scale)

        pos = self.imgInfo.getImgPosOf(EImageObject.GOLD_DISK, True, False)
        resize = EImageObject.GOLD_DISK.getResize()
        DrawCivObjects.drawImage(self.imgGold, window, rotGold, pos, resize, scale)

        pos = self.imgInfo.getImgPosOf(EImageObject.POLITY, True, False)
        resize = EImageObject.POLITY.getResize()
        DrawCivObjects.drawImage(self.civPolity.getImg(), window, ERotation.NO_ROTATION, pos, resize, scale)

        i = 0
        for p in self.pioneer:
            pos = self.imgInfo.getImgPosOfFigure(EFigure.PIONEER, i, True, False)
            resize = EImageObject.FIGURE.getResize()
            if p.getPosition() is None:
                p.draw(window, ERotation.NO_ROTATION, pos, resize, scale)
            i = i + 1

        i = 0
        for a in self.army:
            pos = self.imgInfo.getImgPosOfFigure(EFigure.ARMY, i, True, False)
            resize = EImageObject.FIGURE.getResize()
            if a.getPosition() is None:
                a.draw(window, ERotation.NO_ROTATION, pos, resize, scale)
            i = i + 1

        i = 3
        for c in self.cities:
            imgObj = c.getImgObj()
            pos = self.imgInfo.getImgPosOf(imgObj, True, False)
            resize = imgObj.getResize()
            if c.getPosition() is None:
                c.draw(window, ERotation.NO_ROTATION, pos, resize, scale)
            i = i - 1

        self.researchManager.draw(window)
        self.cultureWonderAndGreatPersons.draw(window)
        self.imgInfo.draw(window)
