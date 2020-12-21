from random import shuffle

from CivEnums.EConstants import EConstants
from CivEnums.ERotation import ERotation
from CivEnums.EUnitStrength import EUnitStrength
from CivEnums.EUnitType import EUnitType
from CivObjects.MilitaryUnit import MilitaryUnit
from CivObjects.Position import Position
from Drawing.EImageObject import EImageObject


"""
this class is a collection of military units on market map
stacks of cavalry, artillery, infantry and airForce with different strength are collected and shuffled here
depending of move of each player military units can be lifted off the stacks
there is a function to draw the stacks on market place
"""


class MilitaryUnitCollection:

    def __init__(self, imgInfoMarketMap):
        self.imgInfo = imgInfoMarketMap
        self.cavalry = []
        self.artillery = []
        self.infantry = []
        self.airForce = []

        self.shuffleCards(EUnitType.ALL_UNIT_TYPE)

        for i in range(2):
            self.airForce.append(MilitaryUnit(EUnitType.AIR_FORCE, EUnitStrength.STRONG))

        for i in range(3):
            self.artillery.append(MilitaryUnit(EUnitType.ARTILLERY, EUnitStrength.WEAK))
            self.artillery.append(MilitaryUnit(EUnitType.ARTILLERY, EUnitStrength.STRONG))
            self.cavalry.append(MilitaryUnit(EUnitType.CAVALRY, EUnitStrength.WEAK))
            self.cavalry.append(MilitaryUnit(EUnitType.CAVALRY, EUnitStrength.STRONG))
            self.infantry.append(MilitaryUnit(EUnitType.INFANTRY, EUnitStrength.WEAK))
            self.infantry.append(MilitaryUnit(EUnitType.INFANTRY, EUnitStrength.STRONG))
            self.airForce.append(MilitaryUnit(EUnitType.AIR_FORCE, EUnitStrength.WEAK))
            self.airForce.append(MilitaryUnit(EUnitType.AIR_FORCE, EUnitStrength.MEDIUM))

        for i in range(9):
            self.artillery.append(MilitaryUnit(EUnitType.ARTILLERY, EUnitStrength.MEDIUM))
            self.cavalry.append(MilitaryUnit(EUnitType.CAVALRY, EUnitStrength.MEDIUM))
            self.infantry.append(MilitaryUnit(EUnitType.INFANTRY, EUnitStrength.MEDIUM))

    def getStackLengthOfMilUnit(self, unitType):
        if unitType is EUnitType.ARTILLERY:
            return len(self.artillery)
        elif unitType is EUnitType.CAVALRY:
            return len(self.cavalry)
        elif unitType is EUnitType.INFANTRY:
            return len(self.infantry)
        elif unitType is EUnitType.AIR_FORCE:
            return len(self.airForce)
        else:
            return -1

    def shuffleCards(self, unitType):
        if unitType == EUnitType.ARTILLERY:
            shuffle(self.artillery)
        elif unitType == EUnitType.CAVALRY:
            shuffle(self.cavalry)
        elif unitType == EUnitType.INFANTRY:
            shuffle(self.infantry)
        elif unitType == EUnitType.AIR_FORCE:
            shuffle(self.airForce)
        else:   # unitType == EUnitType.ARTILLERY
            shuffle(self.artillery)
            shuffle(self.cavalry)
            shuffle(self.infantry)
            shuffle(self.airForce)

    def getArtillery(self):
        if len(self.artillery) > 0:
            return self.artillery.pop(0)
        else:
            return None

    def getCavalry(self):
        if len(self.cavalry) > 0:
            return self.cavalry.pop(0)
        else:
            return None

    def getInfantry(self):
        if len(self.infantry) > 0:
            return self.infantry.pop(0)
        else:
            return None

    def getAirForce(self):
        if len(self.airForce) > 0:
            return self.airForce.pop(0)
        else:
            return None

    def draw(self, window):
        resize = self.imgInfo.getResize(EImageObject.UNIT_CARDS)

        dx = EConstants.DELTA_MILITARY_UNIT_STACK.value
        delta = 0
        stackPos = self.imgInfo.getImgPosOf(EImageObject.INFANTRY_STACK)
        for u in self.infantry:
            pos = Position(stackPos.getX() + delta, stackPos.getY() - delta)
            u.draw(window, ERotation.NO_ROTATION, pos, resize)
            delta = delta + dx

        delta = 0
        stackPos = self.imgInfo.getImgPosOf(EImageObject.ARTILLERY_STACK)
        for u in self.artillery:
            pos = Position(stackPos.getX() + delta, stackPos.getY() - delta)
            u.draw(window, ERotation.NO_ROTATION, pos, resize)
            delta = delta + dx

        delta = 0
        stackPos = self.imgInfo.getImgPosOf(EImageObject.CAVALRY_STACK)
        for u in self.cavalry:
            pos = Position(stackPos.getX() + delta, stackPos.getY() - delta)
            u.draw(window, ERotation.NO_ROTATION, pos, resize)
            delta = delta + dx

        delta = 0
        stackPos = self.imgInfo.getImgPosOf(EImageObject.AIR_FORCE_STACK)
        for u in self.airForce:
            pos = Position(stackPos.getX() + delta, stackPos.getY() - delta)
            u.draw(window, ERotation.NO_ROTATION, pos, resize)
            delta = delta + dx
