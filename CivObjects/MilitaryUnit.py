from CivEnums.EArmyStrength import EArmyStrength
from CivEnums.EUnitType import EUnitType
from CivEnums.EVisibility import EVisibility
from CivObjects.Position import Position
from Drawing import ImageHandler
from Drawing.DrawCivObjects import DrawCivObjects
from Drawing.Drawable import Drawable
from Drawing.EImgConst import EImgConst

"""
with it all properties of military unit can be defined
* unit type
* unit strength
* visibility
* image pointer of front and back
"""


class MilitaryUnit(Drawable):

    def __init__(self, uType, strength, imgDetail, cardNr):
        img = ImageHandler.getImageOfMilitaryUnit(uType, strength, False)
        if uType is EUnitType.INFANTRY:
            mapPos = Position(0, 0)
        elif uType is EUnitType.CAVALRY:
            mapPos = Position(0, 1)
        elif uType is EUnitType.ARTILLERY:
            mapPos = Position(1, 0)
        else:       # AIR_FORCE
            mapPos = Position(1, 1)
        super().__init__(img, EImgConst.MMAP_MILITARY_UNIT, imgDetail, cardNr, mapPos)
        self.uType = uType
        self.unitStrength = strength

    def getFightValue(self, rank):
        return self.unitStrength.getFightValue(rank)

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

    def setVisible(self, visible):
        Drawable.setVisible(self, visible)
        if visible:
            self.setImg(ImageHandler.getImageOfMilitaryUnit(self.uType, self.unitStrength, True))
        else:
            self.setImg(ImageHandler.getImageOfMilitaryUnit(self.uType, self.unitStrength, True))
