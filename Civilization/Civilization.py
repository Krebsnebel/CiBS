import pygame

from Civilization.CivPolity import CivPolity
from Civilization.ResearchManager import ResearchManager
from CivEnums.EArmyStrength import EArmyStrength
from CivEnums.ECity import ECity
from CivEnums.ECivilization import ECivilization
from CivEnums.EColor import EColor
from CivEnums.EFigure import EFigure
from CivEnums.EPolity import EPolity
from CivEnums.EResearch import EResearch
from CivEnums.ERotation import ERotation
from CivEnums.EVisibility import EVisibility
from Civilization.City import City
from CivObjects.Figure import Figure
from Drawing.DrawCivObjects import DrawCivObjects
from Drawing.EImageObject import EImageObject
from Drawing.ImgInfoCivilization import ImgInfoCivilization


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

    def __init__(self, imgInfoCiv, pl, civ, map_tile, col, gameMap):
        self.playerNr = pl
        self.imgInfo = imgInfoCiv
        self.gameMap = gameMap
        self.civ = civ
        self.mapTile = map_tile
        self.civPolity = CivPolity(civ)
        self.imgPolity = self.civPolity.getImg()
        self.color = col
        self.city = []
        self.pioneer = []
        self.army = []
        self.militaryUnit = []
        self.figureLimit = 2
        self.movingRange = 2
        self.thirdCityPossible = False
        self.researchManager = ResearchManager(imgInfoCiv, pl)
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
        self.city.append(City(ECity.KAPITOL, col, civ, EImageObject.KAPITOL))
        self.city.append(City(ECity.TOWN, col, civ, EImageObject.CITY_1))
        self.city.append(City(ECity.TOWN, col, civ, EImageObject.CITY_2))

        for i in range(2):
            self.pioneer.append(Figure(EFigure.PIONEER, civ, col))

        for i in range(6):
            self.army.append(Figure(EFigure.ARMY, civ, col))

        if civ == ECivilization.ROME:
            self.civPolity.setPolity(EPolity.REPUBLIC)
            self.imgPolity = self.civPolity.getImg()
            self.researchManager.research(EResearch.LEGISLATION, 1, True)
        elif civ == ECivilization.RUSSIA:
            self.figureLimit += 1
            self.army.append(Figure(EFigure.ARMY, civ, EColor.WHITE))
            self.civPolity.setPolity(EPolity.COMMUNISM)
            self.imgPolity = self.civPolity.getImg()
            self.researchManager.research(EResearch.COMMUNISM, 1, True)
        elif civ == ECivilization.AGYPT:
            self.researchManager.research(EResearch.CONSTRUCTION_INDUSTRY, 1, True)
        elif civ == ECivilization.GERMANY:
            self.researchManager.research(EResearch.IRON_PROCESSING, 1, True)
        elif civ == ECivilization.AMERICA:
            self.researchManager.research(EResearch.CURRENCY, 1, True)
        elif civ == ECivilization.CHINA:
            self.getCity(0).upgradeCity()
            self.researchManager.research(EResearch.SCRIPTURE, 1, True)

    def getCivPolity(self):
        return self.civPolity

    def isThirdCityPossible(self):
        return self.thirdCityPossible

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
        for c in self.city:
            tp = tp + c.countTradingPoints()

        self.tradingPoints = self.tradingPoints + tp

    def getFigureLimit(self):
        return self.figureLimit

    def getColor(self):
        return self.color

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
        return self.city[idx]

    def getPioneer(self, idx):
        return self.pioneer[idx]

    def getArmy(self, idx):
        return self.army[idx]

    def draw(self, window):
        rotTrade = ImgInfoCivilization.getRotationTradingPoints(self.tradingPoints)
        rotGold = ImgInfoCivilization.getRotationGoldPoints(self.tradingPoints, self.goldPoints)

        pos = self.imgInfo.getImgPosOf(EImageObject.CIVILIZATION_SHEET)
        resize = self.imgInfo.getResize(EImageObject.CIVILIZATION_SHEET)
        DrawCivObjects.drawImage(self.img, window, ERotation.NO_ROTATION, pos, resize, 1)

        pos = self.imgInfo.getImgPosOf(EImageObject.TRADE_DISK)
        resize = self.imgInfo.getResize(EImageObject.TRADE_DISK)
        DrawCivObjects.drawImage(self.imgTrade, window, rotTrade, pos, resize, 1)

        pos = self.imgInfo.getImgPosOf(EImageObject.GOLD_DISK)
        resize = self.imgInfo.getResize(EImageObject.GOLD_DISK)
        DrawCivObjects.drawImage(self.imgGold, window, rotGold, pos, resize, 1)

        pos = self.imgInfo.getImgPosOf(EImageObject.POLITY)
        resize = self.imgInfo.getResize(EImageObject.POLITY)
        DrawCivObjects.drawImage(self.imgPolity, window, ERotation.NO_ROTATION, pos, resize, 1)

        i = 0
        for p in self.pioneer:
            pos = self.imgInfo.getImgPosOfFigure(EFigure.PIONEER, i)
            resize = self.imgInfo.getResize(EImageObject.FIGURE)
            if p.getPosition() is None:
                p.draw(window, ERotation.NO_ROTATION, pos, resize)
            i = i + 1

        i = 0
        for a in self.army:
            pos = self.imgInfo.getImgPosOfFigure(EFigure.ARMY, i)
            resize = self.imgInfo.getResize(EImageObject.FIGURE)
            if a.getPosition() is None:
                a.draw(window, ERotation.NO_ROTATION, pos, resize)
            i = i + 1

        i = 3
        for c in self.city:
            imgObj = c.getImgObj()
            pos = self.imgInfo.getImgPosOf(imgObj)
            resize = self.imgInfo.getResize(imgObj)
            if c.getPosition() is None:
                c.draw(window, ERotation.NO_ROTATION, pos, resize)
            i = i - 1

        self.researchManager.draw(window)
        self.imgInfo.draw(window)
