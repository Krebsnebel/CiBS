from CivCollection.GameMap import GameMap
from CivEnums.EBuilding import EBuilding
from CivEnums.ECivilization import ECivilization
from CivEnums.EColor import EColor
from CivEnums.EFigure import EFigure
from CivEnums.EGreatPerson import EGreatPerson
from CivEnums.EPermission import EPermissionTerrain
from CivEnums.EWonder import EWonder
from CivObjects.Building import Building
from CivObjects.Figure import Figure
from CivObjects.GreatPerson import GreatPerson
from CivObjects.Position import Position
from CivObjects.Wonder import Wonder
from Drawing import ImageHandler
from Drawing.DrawCivObjects import DrawCivObjects
from Drawing.EImageObject import EImageObject


"""
this class handles the city and its outskirt
following functions are yet implemented
* getter for each object type in city (list of points) 
* setter and clearer for current and potential points in city
* functions for position and outskirt
* draw function
* several getters and setters
"""


class City:

    def __init__(self, cType, col, civ, imgObj):
        self.cType = cType
        self.color = col
        self.civilization = civ
        self.imgObj = imgObj
        self.position = None
        self.upgrade = False
        self.outskirts = []

        self.uniqueBuilding = Building(EBuilding.MARKET)
        self.buildingGrassland = Building(EBuilding.GRANARY)
        self.buildingMountain = Building(EBuilding.BLACKSMITH)
        self.buildingWater = Building(EBuilding.MARINA)
        self.buildingDesert = Building(EBuilding.TRADING_POST)
        self.wonder = Wonder(EWonder.STONEHENGE)
        self.greatPerson = GreatPerson(EGreatPerson.ARTIST)
        self.figure = Figure(EFigure.PIONEER, ECivilization.NONE, EColor.NO_COLOR)

        self.potentiallyPointsForUniqueBuildings = []
        self.potentiallyPointsForBuildingsOnGrasland = []
        self.potentiallyPointsForBuildingsInMountain = []
        self.potentiallyPointsForBuildingsOnWater = []
        self.potentiallyPointsForBuildingsInDesert = []
        self.potentiallyPointsForWonders = []
        self.potentiallyPointsForGreatPersons = []
        self.potentiallyPointsForFigures = []

        self.currentPointsForUniqueBuildings = []
        self.currentPointsForBuildingsOnGrasland = []
        self.currentPointsForBuildingsInMountain = []
        self.currentPointsForBuildingsOnWater = []
        self.currentPointsForBuildingsInDesert = []
        self.currentPointsForWonders = []
        self.currentPointsForGreatPersons = []
        self.currentPointsForFigures = []

        self.permissionTerrain = EPermissionTerrain.ALL_EXCEPT_WATER
        self.img = ImageHandler.getImageOfCity(cType, col, self.upgrade)

    def getImgObj(self):
        return self.imgObj

    def getPointsForObjectSetInCity(self, objType):
        if objType == EImageObject.WONDER:
            return self.currentPointsForWonders
        elif objType == EImageObject.GREAT_PERSON:
            return self.currentPointsForGreatPersons
        elif objType == EImageObject.FIGURE:
            return self.currentPointsForFigures
        elif objType == EImageObject.UNIQUE_BUILDINGS:
            return self.currentPointsForUniqueBuildings
        elif objType == EImageObject.BUILDINGS_ON_GRASSLAND:
            return self.currentPointsForBuildingsOnGrasland
        elif objType == EImageObject.BUILDINGS_IN_MOUNTAIN:
            return self.currentPointsForBuildingsInMountain
        elif objType == EImageObject.BUILDINGS_ON_WATER:
            return self.currentPointsForBuildingsOnWater
        elif objType == EImageObject.BUILDINGS_IN_DESERT:
            return self.currentPointsForBuildingsInDesert

    def setPotentialPointsForCity(self):
        for s in self.outskirts:
            self.addPotentialPointForObjectSetInCity(self.uniqueBuilding, s)
            self.addPotentialPointForObjectSetInCity(self.buildingGrassland, s)
            self.addPotentialPointForObjectSetInCity(self.buildingMountain, s)
            self.addPotentialPointForObjectSetInCity(self.buildingWater, s)
            self.addPotentialPointForObjectSetInCity(self.buildingDesert, s)
            self.addPotentialPointForObjectSetInCity(self.wonder, s)
            self.addPotentialPointForObjectSetInCity(self.greatPerson, s)
            self.addPotentialPointForObjectSetInCity(self.figure, s)
        self.setCurrentPointsForCity()

    def setCurrentPointsForCity(self):
        self.currentPointsForUniqueBuildings = self.potentiallyPointsForUniqueBuildings
        self.currentPointsForBuildingsOnGrasland = self.potentiallyPointsForBuildingsOnGrasland
        self.currentPointsForBuildingsInMountain = self.potentiallyPointsForBuildingsInMountain
        self.currentPointsForBuildingsOnWater = self.potentiallyPointsForBuildingsOnWater
        self.currentPointsForBuildingsInDesert = self.potentiallyPointsForBuildingsInDesert
        self.currentPointsForWonders = self.potentiallyPointsForWonders
        self.currentPointsForFigures = self.potentiallyPointsForFigures

    def clearPotentialPoints(self):
        self.potentiallyPointsForUniqueBuildings = []
        self.potentiallyPointsForBuildingsOnGrasland = []
        self.potentiallyPointsForBuildingsInMountain = []
        self.potentiallyPointsForBuildingsOnWater = []
        self.potentiallyPointsForBuildingsInDesert = []
        self.potentiallyPointsForWonders = []
        self.potentiallyPointsForFigures = []

        self.currentPointsForUniqueBuildings = []
        self.currentPointsForBuildingsOnGrasland = []
        self.currentPointsForBuildingsInMountain = []
        self.currentPointsForBuildingsOnWater = []
        self.currentPointsForBuildingsInDesert = []
        self.currentPointsForWonders = []
        self.currentPointsForFigures = []

    def addPotentialPoint(self, obj, s):
        if isinstance(obj, Building):
            if obj.getBuildingType() == EBuilding.MARKET:
                self.potentiallyPointsForUniqueBuildings.append(s)
            elif obj.getBuildingType() == EBuilding.GRANARY:
                self.potentiallyPointsForBuildingsOnGrasland.append(s)
            elif obj.getBuildingType() == EBuilding.BLACKSMITH:
                self.potentiallyPointsForBuildingsInMountain.append(s)
            elif obj.getBuildingType() == EBuilding.MARINA:
                self.potentiallyPointsForBuildingsOnWater.append(s)
            elif obj.getBuildingType() == EBuilding.TRADING_POST:
                self.potentiallyPointsForBuildingsInDesert.append(s)
        elif isinstance(obj, Wonder):
            self.potentiallyPointsForWonders.append(s)
        elif isinstance(obj, Figure):
            self.potentiallyPointsForFigures.append(s)

    def addPotentialPointForObjectSetInCity(self, obj, s):
        p1 = GameMap.isPuttingObjectOnTerrainPossible(obj, s, False)
        if isinstance(obj, Figure):
            p2 = True
        else:
            p2 = self.isPuttingObjectInCityPossible(obj, s)
        if p1 and p2:
            self.addPotentialPoint(obj, s)

    def isPuttingObjectInCityPossible(self, obj, s):
        if isinstance(obj, Wonder):
            if self.isWonderInOutskirt():
                return False
            else:
                return True
        if isinstance(obj, Building):
            if obj.isLabeledUnique():
                if self.isUniqueBuildingThere():
                    return False
                else:
                    return True
        if s.getDisasterMarker() is not None:
            return False
        return True

    def getOutskirts(self):
        return self.outskirts

    def draw(self, window, rotation, pos, resize):
        DrawCivObjects.drawImage(self.img, window, rotation, pos, resize, 1)

    def getCivilization(self):
        return self.civilization

    def getType(self):
        return self.cType

    def getColor(self):
        return self.color

    def getPermissionTerrain(self):
        return self.permissionTerrain

    def upgradeCity(self):
        b = not self.upgrade
        self.upgrade = True
        return b

    def getSign(self):
        return self.cType.getSign(self.upgrade)

    def setPosition(self, x, y):
        self.position = Position(x, y)

    def getPosition(self):
        return self.position

    def setOutskirt(self, s):
        self.outskirts.append(s)

    def isOutskirt(self, x, y):
        for s in self.outskirts:
            p = s.getPosition()
            if p.getX() == x and p.getY() == y:
                return True
        return False

    def isWonderInOutskirt(self):
        for s in self.outskirts:
            if isinstance(s.getBusinessObject(), Wonder):
                return True
        return False

    def isUniqueBuildingThere(self):
        for s in self.outskirts:
            b = s.getBusinessObject()
            if isinstance(b, Building):
                if b.isLabeledUnique:
                    return True
        return False

    def countTradingPoints(self):
        tp = 0
        for s in self.outskirts:
            tp = tp + s.countTradingPoints(self.civilization)
        return tp
