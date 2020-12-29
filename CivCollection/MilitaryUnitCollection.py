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

    def __init__(self, imgInfo):
        self.imgInfo = imgInfo
        self.cavalry = []
        self.artillery = []
        self.infantry = []
        self.airForce = []

        self.shuffleCards(EUnitType.ALL_UNIT_TYPE)

        idxAF = 0
        idxCV = 0
        idxIF = 0
        idxAT = 0
        for i in range(2):
            self.airForce.append(MilitaryUnit(EUnitType.AIR_FORCE, EUnitStrength.STRONG, imgInfo, idxAF))
            idxAF = idxAF + 1

        for i in range(3):
            self.artillery.append(MilitaryUnit(EUnitType.ARTILLERY, EUnitStrength.WEAK, imgInfo, idxAT))
            idxAT = idxAT + 1
            self.artillery.append(MilitaryUnit(EUnitType.ARTILLERY, EUnitStrength.STRONG, imgInfo, idxAT))
            idxAT = idxAT + 1
            self.cavalry.append(MilitaryUnit(EUnitType.CAVALRY, EUnitStrength.WEAK, imgInfo, idxCV))
            idxCV = idxCV + 1
            self.cavalry.append(MilitaryUnit(EUnitType.CAVALRY, EUnitStrength.STRONG, imgInfo, idxCV))
            idxCV = idxCV + 1
            self.infantry.append(MilitaryUnit(EUnitType.INFANTRY, EUnitStrength.WEAK, imgInfo, idxIF))
            idxIF = idxIF + 1
            self.infantry.append(MilitaryUnit(EUnitType.INFANTRY, EUnitStrength.STRONG, imgInfo, idxIF))
            idxIF = idxIF + 1
            self.airForce.append(MilitaryUnit(EUnitType.AIR_FORCE, EUnitStrength.WEAK, imgInfo, idxAF))
            idxAF = idxAF + 1
            self.airForce.append(MilitaryUnit(EUnitType.AIR_FORCE, EUnitStrength.MEDIUM, imgInfo, idxAF))
            idxAF = idxAF + 1

        for i in range(9):
            self.artillery.append(MilitaryUnit(EUnitType.ARTILLERY, EUnitStrength.MEDIUM, imgInfo, idxAT))
            idxAT = idxAT + 1
            self.cavalry.append(MilitaryUnit(EUnitType.CAVALRY, EUnitStrength.MEDIUM, imgInfo, idxCV))
            idxCV = idxCV + 1
            self.infantry.append(MilitaryUnit(EUnitType.INFANTRY, EUnitStrength.MEDIUM, imgInfo, idxIF))
            idxIF = idxIF + 1

    def resetCardIndex(self):
        for i in range(len(self.infantry)):
            self.infantry[i].setCardNr(i)

        for i in range(len(self.cavalry)):
            self.cavalry[i].setCardNr(i)

        for i in range(len(self.artillery)):
            self.artillery[i].setCardNr(i)

        for i in range(len(self.airForce)):
            self.airForce[i].setCardNr(i)

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
        self.resetCardIndex()

    def getCard(self, uType):
        if uType == EUnitType.ARTILLERY:
            stack = self.artillery
        elif uType == EUnitType.CAVALRY:
            stack = self.cavalry
        elif uType == EUnitType.INFANTRY:
            stack = self.infantry
        else:       # EUnitType.AIR_FORCE:
            stack = self.airForce
        if len(stack) > 0:
            return stack.pop(len(stack)-1)
        else:
            return None

    def draw(self, window):

        dx = EConstants.DELTA_MILITARY_UNIT_STACK.value
        delta = 0
        stackPos = self.imgInfo.getImgPosOf(EImageObject.INFANTRY_STACK, True, False)
        for u in self.infantry:
            pos = Position(stackPos.getX() + delta, stackPos.getY() - delta)
#            u.draw(window, ERotation.NO_ROTATION, pos, resize, scale)
            u.draw(window)
            delta = delta + dx

        delta = 0
        stackPos = self.imgInfo.getImgPosOf(EImageObject.ARTILLERY_STACK, True, False)
        for u in self.artillery:
            pos = Position(stackPos.getX() + delta, stackPos.getY() - delta)
#            u.draw(window, ERotation.NO_ROTATION, pos, resize, scale)
            u.draw(window)
            delta = delta + dx

        delta = 0
        stackPos = self.imgInfo.getImgPosOf(EImageObject.CAVALRY_STACK, True, False)
        for u in self.cavalry:
            pos = Position(stackPos.getX() + delta, stackPos.getY() - delta)
#            u.draw(window, ERotation.NO_ROTATION, pos, resize, scale)
            u.draw(window)
            delta = delta + dx

        delta = 0
        stackPos = self.imgInfo.getImgPosOf(EImageObject.AIR_FORCE_STACK, True, False)
        for u in self.airForce:
            pos = Position(stackPos.getX() + delta, stackPos.getY() - delta)
#            u.draw(window, ERotation.NO_ROTATION, pos, resize, scale)
            u.draw(window)
            delta = delta + dx
