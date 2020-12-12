from CivEnums.EPermission import EPermissionTerrain
from CivEnums.EVisibility import EVisibility
from CivObjects.BusinessObject import BusinessObject
from Drawing import ImageHandler
from Drawing.DrawCivObjects import DrawCivObjects


"""
class GreatPerson inherits by BusinessObject
with it all properties of each great person can be defined
* great person type, name and sign
* visibility
* permission for each terrain
* trading points
* production points
* culture points
* defense points
* resource
* pointer to image
"""


class GreatPerson(BusinessObject):

    def __init__(self, gpType):
        self.gpType = gpType
        self.visibility = EVisibility.FOR_NOBODY
        self.permissionTerrain = EPermissionTerrain.ALL_EXCEPT_WATER
        tp = self.gpType.getTradingPoints()
        pp = self.gpType.getProductionPoints()
        cp = self.gpType.getCulturePoints()
        dp = self.gpType.getDefencePoints()
        res = self.gpType.getResource()
        s = self.gpType.getSign()
        super().__init__(tp, pp, cp, dp, res, s)
        self.img = ImageHandler.getImageOfGreatPerson(gpType, False)

    def getPermissionTerrain(self):
        return self.permissionTerrain

    def draw(self, window, rotation, pos, resize):
        DrawCivObjects.drawImage(self.img, window, rotation, pos, resize, 1)
