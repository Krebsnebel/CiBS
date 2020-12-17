from CivEnums.EBuilding import EBuilding
from CivEnums.ECivilization import ECivilization
from CivEnums.EColor import EColor
from CivEnums.EFigure import EFigure
from CivEnums.EGreatPerson import EGreatPerson
from CivEnums.EWonder import EWonder
from CivObjects.Building import Building
from CivObjects.Figure import Figure
from CivObjects.GreatPerson import GreatPerson
from CivObjects.Wonder import Wonder
from Drawing.EImageObject import EImageObject
from Game.GameMap import GameMap


class CityPossibilities:

    def __init__(self, city):
        self.city = city

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

    def getPointsForObjectSetInCity(self, objType):
        if objType == EImageObject.WONDER:
            return self.potentiallyPointsForWonders
        elif objType == EImageObject.GREAT_PERSON:
            return self.potentiallyPointsForGreatPersons
        elif objType == EImageObject.FIGURE:
            return self.potentiallyPointsForFigures
        elif objType == EImageObject.UNIQUE_BUILDINGS:
            return self.potentiallyPointsForUniqueBuildings
        elif objType == EImageObject.BUILDINGS_ON_GRASSLAND:
            return self.potentiallyPointsForBuildingsOnGrasland
        elif objType == EImageObject.BUILDINGS_IN_MOUNTAIN:
            return self.potentiallyPointsForBuildingsInMountain
        elif objType == EImageObject.BUILDINGS_ON_WATER:
            return self.potentiallyPointsForBuildingsOnWater
        elif objType == EImageObject.BUILDINGS_IN_DESERT:
            return self.potentiallyPointsForBuildingsInDesert

    def clearPotentialPoints(self):
        self.potentiallyPointsForUniqueBuildings = []
        self.potentiallyPointsForBuildingsOnGrasland = []
        self.potentiallyPointsForBuildingsInMountain = []
        self.potentiallyPointsForBuildingsOnWater = []
        self.potentiallyPointsForBuildingsInDesert = []
        self.potentiallyPointsForWonders = []
        self.potentiallyPointsForFigures = []

    def setPotentialPointsForCity(self):
        for s in self.city.outskirts:
            self.addPotentialPointForObjectSetInCity(self.uniqueBuilding, s)
            self.addPotentialPointForObjectSetInCity(self.buildingGrassland, s)
            self.addPotentialPointForObjectSetInCity(self.buildingMountain, s)
            self.addPotentialPointForObjectSetInCity(self.buildingWater, s)
            self.addPotentialPointForObjectSetInCity(self.buildingDesert, s)
            self.addPotentialPointForObjectSetInCity(self.wonder, s)
            self.addPotentialPointForObjectSetInCity(self.greatPerson, s)
            self.addPotentialPointForObjectSetInCity(self.figure, s)

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


