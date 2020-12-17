from CivEnums.EPermission import EPermission
from CivEnums.EResource import EResource
from CivEnums.ETerrain import ETerrain
from CivObjects.BusinessObject import BusinessObject
from Drawing import ImageHandler
from Drawing.DrawCivObjects import DrawCivObjects


"""
class DisasterMarker inherits by BusinessObject
with it all properties of each disaster marker can be defined
* disaster type, name and sign and which one is active
* permission for each terrain
* trading points
* production points
* culture points
* defence points
* resource
* pointer to image
"""


class DisasterMarker(BusinessObject):

    def __init__(self):
        self.terrain1 = ETerrain.DROUGHT
        self.terrain2 = ETerrain.DEFORESTATION
        self.terrain1active = True
        self.permissionTerrain = EPermission.ALL_EXCEPT_WATER_AND_MOUNTAIN
        tp = self.terrain1.getTradingPoints()
        pp = self.terrain1.getProductionPoints()
        cp = 0
        dp = 0
        s = self.terrain1.getSign()
        res = EResource.NONE
        super().__init__(tp, pp, cp, dp, res, s)
        self.img = ImageHandler.getImageOfDisasterMarker(True)

    def draw(self, window, rotation, pos, resize):
        DrawCivObjects.drawImage(self.img, window, rotation, pos, resize, 1)

    def chooseDrought(self):
        self.terrain1active = True
        self.tradingPoints = self.terrain1.getTradingPoints()
        self.productionPoints = self.terrain1.getProductionPoints()
        self.sign = self.terrain1.getSign()
        self.permissionTerrain = EPermission.ALL_EXCEPT_WATER_AND_MOUNTAIN
        self.img = ImageHandler.getImageOfDisasterMarker(True)

    def chooseDeforestation(self):
        self.terrain1active = False
        self.tradingPoints = self.terrain2.getTradingPoints()
        self.productionPoints = self.terrain2.getProductionPoints()
        self.sign = self.terrain2.getSign()
        self.permissionTerrain = EPermission.ONLY_FOREST
        self.img = ImageHandler.getImageOfDisasterMarker(False)

    def isDroughtChosen(self):
        return self.terrain1active

    def getPermissionTerrain(self):
        return self.permissionTerrain
