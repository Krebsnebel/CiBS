from CivEnums.EArmyStrength import EArmyStrength
from CivEnums.EUnitType import EUnitType
from CivEnums.EVisibility import EVisibility
from Drawing import ImageHandler
from Drawing.DrawCivObjects import DrawCivObjects


"""
with it all properties of military unit can be defined
* unit type
* unit strength
* visibility
* image pointer of front and back
"""


class MilitaryUnit:

    def __init__(self, uType, strength):
        self.uType = uType
        self.unitStrength = strength
        self.visibility = EVisibility.FOR_NOBODY
        self.imgFront = ImageHandler.getImageOfMilitaryUnit(uType, strength, True)
        self.imgBack = ImageHandler.getImageOfMilitaryUnit(uType, strength, False)

    def getFightValue(self, rank):
        return self.unitStrength.getFightValue(rank)

    def changeVisibility(self, vis):
        self.visibility = vis

    def getCosts(self, rank):
        if self.uType == EUnitType.AIR_FORCE:
            return 12
        elif rank == EArmyStrength.FORTH_LEVEL:
            return 11
        elif rank == EArmyStrength.THIRD_LEVEL:
            return 9
        elif rank == EArmyStrength.SECOND_LEVEL:
            return 7
        else:
            return 5

    def draw(self, window, rotation, pos, resize):
        if self.visibility == EVisibility.FOR_NOBODY:
            img = self.imgBack
        else:
            img = self.imgFront
        DrawCivObjects.drawImage(img, window, rotation, pos, resize, 1)
