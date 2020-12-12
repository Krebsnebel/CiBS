from CivObjects.BusinessObject import BusinessObject
from Drawing import ImageHandler
from Drawing.DrawCivObjects import DrawCivObjects

"""
class Building inherits by BusinessObject
with it all properties of each building can be defined
* trading points
* production points
* culture points
* defence points
* resource
* building type, name and sign
* permission for each terrain
* building upgrade
* costs and alternative costs
* pointer to image
"""
class Building(BusinessObject):

    def __init__(self, b):
        tp = b.getTradingPoints(False)
        pp = b.getProductionPoints(False)
        cp = b.getCulturePoints(False)
        dp = b.getDefencePoints(False)
        res = b.getResource(False)
        s = b.getSign(False)
        super().__init__(tp, pp, cp, dp, res, s)
        self.bType = b
        self.permissionTerrain = b.getPermissionTerrain()
        self.upgrade = False
        self.costs = b.getCosts()
        self.costsAlternative = b.getCostsAlternative()
        # self.img = pygame.image.load("Material/Buildings/" + b.getImgName(self.upgrade) + ".png")
        self.img = ImageHandler.getImageOfBuilding(self.bType, False)

    def draw(self, window, rotation, pos, resize):
        DrawCivObjects.drawImage(self.img, window, rotation, pos, resize, 1)

    def isLabeledUnique(self):
        return self.bType.getUnique()

    def getCosts(self, alternative):
        if alternative:
            return self.costsAlternative
        else:
            return self.costs

    def getPermissionTerrain(self):
        return self.permissionTerrain

    def getBuildingType(self):
        return self.bType
