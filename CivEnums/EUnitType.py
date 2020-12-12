from enum import Enum


class EUnitType(Enum):

    def __init__(self, na, img):
        self.unitName = na
        self.imgName = img

    def getImgName(self):
        return self.imgName

    ALL_UNIT_TYPE = ("Alle Einheitstypen", "AllUnitType")
    CAVALRY = ("Kavallerie", "Cavalry")
    INFANTRY = ("Infanterie", "Infantry")
    ARTILLERY = ("Artillerie", "Artillery")
    AIR_FORCE = ("Luftwaffe", "AirForce")
