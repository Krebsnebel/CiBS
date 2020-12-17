from CivEnums.EPermission import EPermission
from CivEnums.EResource import EResource
from CivEnums.EVisibility import EVisibility
from CivObjects.BusinessObject import BusinessObject
from Drawing.DrawCivObjects import DrawCivObjects
from Drawing import ImageHandler


"""
class Wonder inherits by BusinessObject
with it all properties of each wonder can be defined
* trading points
* production points
* culture points
* defence points
* resource
* wonder type, name and sign
* visibility
* permission for each terrain
* pointer to image marker and card
"""


class Wonder(BusinessObject):

    def __init__(self, w):
        tp = 0
        pp = 0
        cp = w.getCulturePoints()
        dp = 0
        res = EResource.NONE
        s = w.getSign()
        super().__init__(tp, pp, cp, dp, res, s)
        self.visibility = EVisibility.FOR_NOBODY
        self.wonder = w
        self.permissionTerrain = EPermission.ALL_EXCEPT_WATER
        self.imgMarker = ImageHandler.getImageOfWonder(self.wonder, False, True)
        self.imgCard = ImageHandler.getImageOfWonder(self.wonder, True, False)

    def isVisible(self):
        self.visibility = EVisibility.FOR_ALL
        self.imgCard = ImageHandler.getImageOfWonder(self.wonder, True, True)

    def getCosts(self, alternative):
        if alternative:
            return self.wonder.getCostsAlternative()
        else:
            return self.wonder.getCosts()

    def getPermissionTerrain(self):
        return self.permissionTerrain

    def draw(self, window, rotation, pos, resize):
        DrawCivObjects.drawImage(self.imgMarker, window, rotation, pos, resize, 1)

    def drawCard(self, window, rotation, pos, resize):
        DrawCivObjects.drawImage(self.imgCard, window, rotation, pos, resize, 1)
